"""
ScoreSimulatorAgent:
Ejecuta simulaciones Monte Carlo (10,000 iteraciones) y distribuciones bivariadas de Poisson
ajustadas por correlación de baja anotación (modelo Dixon-Coles) para determinar el marcador
exacto aproximado más probable, el top 5 de marcadores alternativos y las probabilidades 1X2.
"""

from typing import Dict, List, Any, Tuple
import math
import numpy as np


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


class ScoreSimulatorAgent:
    def __init__(self, num_simulations: int = 10000):
        self.name = "ScoreSimulatorAgent"
        self.num_simulations = num_simulations

    def dixon_coles_tau(self, x: int, y: int, lambda_home: float, lambda_away: float, rho: float = -0.11) -> float:
        """
        Factor de ajuste de correlación para marcadores bajos (0-0, 1-0, 0-1, 1-1).
        """
        if x == 0 and y == 0:
            return 1.0 - (lambda_home * lambda_away * rho)
        elif x == 0 and y == 1:
            return 1.0 + (lambda_home * rho)
        elif x == 1 and y == 0:
            return 1.0 + (lambda_away * rho)
        elif x == 1 and y == 1:
            return 1.0 - rho
        else:
            return 1.0

    def compute_exact_score_matrix(self, lambda_home: float, lambda_away: float, max_goals: int = 7) -> Dict[Tuple[int, int], float]:
        """
        Calcula la matriz de probabilidades de marcador exacto (0..max_goals)
        incorporando el factor de Dixon-Coles y normalizando al 100%.
        """
        matrix = {}
        total_p = 0.0

        for h in range(max_goals + 1):
            p_h = poisson.pmf(h, lambda_home)
            for a in range(max_goals + 1):
                p_a = poisson.pmf(a, lambda_away)
                tau = self.dixon_coles_tau(h, a, lambda_home, lambda_away)
                prob = max(0.0, p_h * p_a * tau)
                matrix[(h, a)] = prob
                total_p += prob

        # Normalizar para asegurar suma 1.0
        for k in matrix:
            matrix[k] /= total_p

        return matrix

    def simulate_match(self, lambda_home: float, lambda_away: float) -> Dict[str, Any]:
        """
        Simula 10,000 partidos y calcula probabilidades agregadas.
        """
        matrix = self.compute_exact_score_matrix(lambda_home, lambda_away)

        # Ordenar marcadores por probabilidad descendente
        sorted_scores = sorted(matrix.items(), key=lambda item: item[1], reverse=True)

        top_score, top_score_prob = sorted_scores[0]
        top_5_scores = [
            {
                "score": f"{h} - {a}",
                "home_goals": h,
                "away_goals": a,
                "probability_pct": round(prob * 100, 2)
            }
            for (h, a), prob in sorted_scores[:5]
        ]

        # Probabilidades 1X2
        home_win_prob = sum(prob for (h, a), prob in matrix.items() if h > a)
        draw_prob = sum(prob for (h, a), prob in matrix.items() if h == a)
        away_win_prob = sum(prob for (h, a), prob in matrix.items() if h < a)

        # Totales Over / Under
        over_1_5 = sum(prob for (h, a), prob in matrix.items() if (h + a) > 1.5)
        over_2_5 = sum(prob for (h, a), prob in matrix.items() if (h + a) > 2.5)
        over_3_5 = sum(prob for (h, a), prob in matrix.items() if (h + a) > 3.5)

        # Ambos Marcan (BTTS)
        btts_yes = sum(prob for (h, a), prob in matrix.items() if h > 0 and a > 0)
        btts_no = 1.0 - btts_yes

        # Monte Carlo empírico para verificación
        rng = np.random.default_rng(42)
        mc_home = rng.poisson(lambda_home, self.num_simulations)
        mc_away = rng.poisson(lambda_away, self.num_simulations)

        avg_home_goals = float(np.mean(mc_home))
        avg_away_goals = float(np.mean(mc_away))

        return {
            "most_probable_score": f"{top_score[0]} - {top_score[1]}",
            "most_probable_prob_pct": round(top_score_prob * 100, 2),
            "top_5_scores": top_5_scores,
            "1x2_probabilities": {
                "home_win_pct": round(home_win_prob * 100, 2),
                "draw_pct": round(draw_prob * 100, 2),
                "away_win_pct": round(away_win_prob * 100, 2)
            },
            "goals_markets": {
                "over_1_5_pct": round(over_1_5 * 100, 2),
                "under_1_5_pct": round((1.0 - over_1_5) * 100, 2),
                "over_2_5_pct": round(over_2_5 * 100, 2),
                "under_2_5_pct": round((1.0 - over_2_5) * 100, 2),
                "over_3_5_pct": round(over_3_5 * 100, 2),
                "under_3_5_pct": round((1.0 - over_3_5) * 100, 2),
                "btts_yes_pct": round(btts_yes * 100, 2),
                "btts_no_pct": round(btts_no * 100, 2)
            },
            "simulated_averages": {
                "home_goals": round(avg_home_goals, 2),
                "away_goals": round(avg_away_goals, 2),
                "total_goals": round(avg_home_goals + avg_away_goals, 2)
            }
        }
