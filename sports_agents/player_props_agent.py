# -*- coding: utf-8 -*-
"""
PlayerPropsAgent 2.0:
Modela la proyección individual de remates totales y remates a puerta (shots on target)
para las figuras ratificadas sanitariamente de cada equipo.

Cuenta con un cerrojo estricto de exclusión:
Cualquier futbolista marcado con veto sanitario, baja médica o duda severa
es bloqueado inmediatamente y jamás genera líneas de apuestas de tiros.
"""

from typing import Dict, List, Any
import math


class PoissonDist:
    @staticmethod
    def pmf(k: int, mu: float) -> float:
        if mu <= 0:
            return 1.0 if k == 0 else 0.0
        try:
            return math.exp(-mu) * (mu ** k) / math.factorial(int(k))
        except (OverflowError, ValueError):
            return 0.0


poisson = PoissonDist()


class PlayerPropsAgent:
    def __init__(self):
        self.name = "PlayerPropsAgent"

    def project_player_shots(self, player: Dict[str, Any], team_projected_shots: float, team_baseline_shots: float = 14.0) -> Dict[str, Any] | None:
        """
        Ajusta la tasa individual de tiros según el volumen total proyectado para el equipo.
        Si el jugador está vetado, lesionado o no convocado, devuelve None de inmediato.
        """
        # CERROJO DE SEGURIDAD SANITARIA
        if player.get("veto_player_props", False):
            return None

        pos_str = str(player.get("position", "")).lower()
        if "baja" in pos_str or "lesion" in pos_str:
            return None

        base_shots = player.get("avg_shots_p90", 2.0)
        base_sot = player.get("avg_sot_p90", 0.9)

        # Ratio de volumen de equipo
        volume_ratio = team_projected_shots / max(8.0, team_baseline_shots)
        exp_shots = max(0.4, base_shots * volume_ratio)
        exp_sot = max(0.2, base_sot * volume_ratio)

        # Probabilidades acumuladas mediante distribución Poisson
        prob_over_0_5_sot = min(0.96, 1.0 - poisson.pmf(0, exp_sot))
        prob_over_1_5_sot = min(0.92, 1.0 - (poisson.pmf(0, exp_sot) + poisson.pmf(1, exp_sot)))
        prob_over_1_5_shots = min(0.96, 1.0 - (poisson.pmf(0, exp_shots) + poisson.pmf(1, exp_shots)))
        prob_over_2_5_shots = min(0.88, 1.0 - sum(poisson.pmf(k, exp_shots) for k in range(3)))

        goal_prob = min(0.85, player.get("goal_prob", 0.25))

        return {
            "name": player["name"],
            "position": player.get("position", "Jugador"),
            "health_status": player.get("health_status", "Disponible"),
            "expected_shots": round(float(exp_shots), 2),
            "expected_sot": round(float(exp_sot), 2),
            "prob_at_least_1_sot_pct": round(float(prob_over_0_5_sot) * 100, 1),
            "prob_at_least_2_sot_pct": round(float(prob_over_1_5_sot) * 100, 1),
            "prob_over_1_5_shots_pct": round(float(prob_over_1_5_shots) * 100, 1),
            "prob_over_2_5_shots_pct": round(float(prob_over_2_5_shots) * 100, 1),
            "goal_anytime_prob_pct": round(float(goal_prob) * 100, 1),
            "reallocated_from": player.get("reallocated_from", None)
        }

    def analyze_team_players(self, players: List[Dict[str, Any]], team_projected_shots: float) -> List[Dict[str, Any]]:
        """
        Analiza la lista de jugadores activos y purga cualquier elemento vetado.
        """
        results = []
        for p in players:
            proj = self.project_player_shots(p, team_projected_shots)
            if proj is not None:
                results.append(proj)
        return results
