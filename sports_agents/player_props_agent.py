"""
PlayerPropsAgent:
Modela la proyección individual de remates totales y remates a puerta (shots on target)
para las figuras más determinantes de cada selección, ajustando según el volumen colectivo
proyectado por TimesFM y la rigidez defensiva del rival.
"""

from typing import Dict, List, Any
import numpy as np
from scipy.stats import poisson


class PlayerPropsAgent:
    def __init__(self):
        self.name = "PlayerPropsAgent"

    def project_player_shots(self, player: Dict[str, Any], team_projected_shots: float, team_baseline_shots: float = 14.0) -> Dict[str, Any]:
        """
        Ajusta la tasa individual de tiros según el volumen total proyectado para el equipo.
        """
        base_shots = player.get("avg_shots_p90", 2.0)
        base_sot = player.get("avg_sot_p90", 0.9)

        # Ratio de volumen de equipo
        volume_ratio = team_projected_shots / max(8.0, team_baseline_shots)
        exp_shots = max(0.4, base_shots * volume_ratio)
        exp_sot = max(0.2, base_sot * volume_ratio)

        # Probabilidades acumuladas mediante distribución Poisson
        # P(X >= 1) = 1 - P(0)
        # P(X >= 2) = 1 - P(0) - P(1)
        prob_over_0_5_sot = 1.0 - poisson.pmf(0, exp_sot)
        prob_over_1_5_sot = 1.0 - (poisson.pmf(0, exp_sot) + poisson.pmf(1, exp_sot))
        prob_over_1_5_shots = 1.0 - (poisson.pmf(0, exp_shots) + poisson.pmf(1, exp_shots))
        prob_over_2_5_shots = 1.0 - sum(poisson.pmf(k, exp_shots) for k in range(3))

        return {
            "name": player["name"],
            "position": player.get("position", "Jugador"),
            "expected_shots": round(float(exp_shots), 2),
            "expected_sot": round(float(exp_sot), 2),
            "prob_at_least_1_sot_pct": round(float(prob_over_0_5_sot) * 100, 1),
            "prob_at_least_2_sot_pct": round(float(prob_over_1_5_sot) * 100, 1),
            "prob_over_1_5_shots_pct": round(float(prob_over_1_5_shots) * 100, 1),
            "prob_over_2_5_shots_pct": round(float(prob_over_2_5_shots) * 100, 1),
            "goal_anytime_prob_pct": round(player.get("goal_prob", 0.25) * 100, 1)
        }

    def analyze_team_players(self, players: List[Dict[str, Any]], team_projected_shots: float) -> List[Dict[str, Any]]:
        """
        Analiza la lista completa de jugadores clave del equipo.
        """
        return [self.project_player_shots(p, team_projected_shots) for p in players]
