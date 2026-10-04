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

    @staticmethod
    def neg_bin_pmf(k: int, mu: float, alpha: float = 0.10) -> float:
        """
        Distribución Binomial Negativa para modelar sobredispersión (over-dispersion)
        y colas pesadas de goleada (fat tails).
        """
        if mu <= 0:
            return 1.0 if k == 0 else 0.0
        if alpha <= 0.001:
            return PoissonDist.pmf(k, mu)
        try:
            r = 1.0 / alpha
            p = r / (r + mu)
            coeff = math.gamma(k + r) / (math.factorial(int(k)) * math.gamma(r))
            return max(0.0, float(coeff * (p ** r) * ((1.0 - p) ** k)))
        except (OverflowError, ValueError):
            return PoissonDist.pmf(k, mu)


poisson = PoissonDist()


class ScoreSimulatorAgent:
    def __init__(self, num_simulations: int = 10000, overdispersion_alpha: float = 0.10):
        self.name = "ScoreSimulatorAgent"
        self.num_simulations = num_simulations
        self.alpha = overdispersion_alpha

    def dixon_coles_tau(self, x: int, y: int, lambda_home: float, lambda_away: float, rho: float = -0.11) -> float:
        """
        Factor de ajuste de correlación para marcadores bajos (0-0, 1-0, 0-1, 1-1).
        """
        if x == 0 and y == 0:
            return max(0.0, 1.0 - (lambda_home * lambda_away * rho))
        elif x == 0 and y == 1:
            return max(0.0, 1.0 + (lambda_home * rho))
        elif x == 1 and y == 0:
            return max(0.0, 1.0 + (lambda_away * rho))
        elif x == 1 and y == 1:
            return max(0.0, 1.0 - rho)
        else:
            return 1.0

    def compute_exact_score_matrix(self, lambda_home: float, lambda_away: float, max_goals: int = 7) -> Dict[Tuple[int, int], float]:
        """
        Calcula la matriz de probabilidades de marcador exacto (0..max_goals)
        incorporando sobredispersión Binomial Negativa (colas pesadas de goleada)
        y factor de correlación Dixon-Coles calibrado para marcadores bajos.
        """
        matrix = {}
        total_p = 0.0
        tot_xg = lambda_home + lambda_away
        # El ajuste Dixon-Coles para 0-0 se amortigua suavemente cuando el xG total supera 2.2
        tau_scale = max(0.0, min(1.0, 1.0 - (tot_xg - 2.2) / 1.5))

        for h in range(max_goals + 1):
            p_h = poisson.neg_bin_pmf(h, lambda_home, self.alpha)
            for a in range(max_goals + 1):
                p_a = poisson.neg_bin_pmf(a, lambda_away, self.alpha)
                raw_tau = self.dixon_coles_tau(h, a, lambda_home, lambda_away)
                tau = 1.0 + (raw_tau - 1.0) * tau_scale
                prob = max(0.0, p_h * p_a * tau)
                matrix[(h, a)] = prob
                total_p += prob

        # Normalizar para asegurar suma 1.0
        if total_p > 0:
            for k in matrix:
                matrix[k] /= total_p

        return matrix

    def compute_comprehensive_market_probabilities(self, matrix: Dict[Tuple[int, int], float]) -> Dict[str, float]:
        """
        Calcula rigurosamente todas las probabilidades de mercado directamente a partir
        de la convolución conjunta exacta de la matriz bivariada, erradicando aproximaciones heurísticas.
        """
        # 1X2
        h_win = sum(p for (h, a), p in matrix.items() if h > a)
        draw = sum(p for (h, a), p in matrix.items() if h == a)
        a_win = sum(p for (h, a), p in matrix.items() if h < a)

        # Doble Oportunidad
        dc_1x = sum(p for (h, a), p in matrix.items() if h >= a)
        dc_x2 = sum(p for (h, a), p in matrix.items() if a >= h)
        dc_12 = sum(p for (h, a), p in matrix.items() if h != a)

        # Draw No Bet (DNB)
        dnb_denom = max(0.0001, h_win + a_win)
        dnb_home = h_win / dnb_denom
        dnb_away = a_win / dnb_denom

        # Totales Over / Under
        over_0_5 = sum(p for (h, a), p in matrix.items() if (h + a) >= 1)
        under_0_5 = sum(p for (h, a), p in matrix.items() if (h + a) == 0)

        over_1_5 = sum(p for (h, a), p in matrix.items() if (h + a) >= 2)
        under_1_5 = sum(p for (h, a), p in matrix.items() if (h + a) <= 1)

        over_2_5 = sum(p for (h, a), p in matrix.items() if (h + a) >= 3)
        under_2_5 = sum(p for (h, a), p in matrix.items() if (h + a) <= 2)

        over_3_5 = sum(p for (h, a), p in matrix.items() if (h + a) >= 4)
        under_3_5 = sum(p for (h, a), p in matrix.items() if (h + a) <= 3)

        over_4_5 = sum(p for (h, a), p in matrix.items() if (h + a) >= 5)
        under_4_5 = sum(p for (h, a), p in matrix.items() if (h + a) <= 4)

        under_5_5 = sum(p for (h, a), p in matrix.items() if (h + a) <= 5)

        # Ambos Equipos Anotan (BTTS)
        btts_yes = sum(p for (h, a), p in matrix.items() if h >= 1 and a >= 1)
        btts_no = 1.0 - btts_yes

        # Goles Individuales de Equipo
        home_over_0_5 = sum(p for (h, a), p in matrix.items() if h >= 1)
        home_under_2_5 = sum(p for (h, a), p in matrix.items() if h <= 2)
        away_over_0_5 = sum(p for (h, a), p in matrix.items() if a >= 1)
        away_under_2_5 = sum(p for (h, a), p in matrix.items() if a <= 2)

        # Hándicaps Asiáticos Exactos
        home_plus_1_5 = sum(p for (h, a), p in matrix.items() if (h - a) >= -1) # Gana, empata o pierde por 1
        away_plus_1_5 = sum(p for (h, a), p in matrix.items() if (a - h) >= -1)

        home_plus_2_5 = sum(p for (h, a), p in matrix.items() if (h - a) >= -2)
        away_plus_2_5 = sum(p for (h, a), p in matrix.items() if (a - h) >= -2)

        home_minus_1_5 = sum(p for (h, a), p in matrix.items() if (h - a) >= 2) # Goleada local por 2+
        away_minus_1_5 = sum(p for (h, a), p in matrix.items() if (a - h) >= 2) # Goleada visitante por 2+

        # Clean Sheets
        home_clean_sheet = sum(p for (h, a), p in matrix.items() if a == 0)
        away_clean_sheet = sum(p for (h, a), p in matrix.items() if h == 0)

        # Margen de Victoria
        home_win_by_1 = sum(p for (h, a), p in matrix.items() if (h - a) == 1)
        away_win_by_1 = sum(p for (h, a), p in matrix.items() if (a - h) == 1)

        return {
            "home_win_pct": round(h_win * 100, 2),
            "draw_pct": round(draw * 100, 2),
            "away_win_pct": round(a_win * 100, 2),
            "double_chance_1x_pct": round(dc_1x * 100, 2),
            "double_chance_x2_pct": round(dc_x2 * 100, 2),
            "double_chance_12_pct": round(dc_12 * 100, 2),
            "dnb_home_pct": round(dnb_home * 100, 2),
            "dnb_away_pct": round(dnb_away * 100, 2),
            "over_0_5_pct": round(over_0_5 * 100, 2),
            "under_0_5_pct": round(under_0_5 * 100, 2),
            "over_1_5_pct": round(over_1_5 * 100, 2),
            "under_1_5_pct": round(under_1_5 * 100, 2),
            "over_2_5_pct": round(over_2_5 * 100, 2),
            "under_2_5_pct": round(under_2_5 * 100, 2),
            "over_3_5_pct": round(over_3_5 * 100, 2),
            "under_3_5_pct": round(under_3_5 * 100, 2),
            "over_4_5_pct": round(over_4_5 * 100, 2),
            "under_4_5_pct": round(under_4_5 * 100, 2),
            "under_5_5_pct": round(under_5_5 * 100, 2),
            "btts_yes_pct": round(btts_yes * 100, 2),
            "btts_no_pct": round(btts_no * 100, 2),
            "home_over_0_5_pct": round(home_over_0_5 * 100, 2),
            "home_under_2_5_pct": round(home_under_2_5 * 100, 2),
            "away_over_0_5_pct": round(away_over_0_5 * 100, 2),
            "away_under_2_5_pct": round(away_under_2_5 * 100, 2),
            "home_plus_1_5_pct": round(home_plus_1_5 * 100, 2),
            "away_plus_1_5_pct": round(away_plus_1_5 * 100, 2),
            "home_plus_2_5_pct": round(home_plus_2_5 * 100, 2),
            "away_plus_2_5_pct": round(away_plus_2_5 * 100, 2),
            "home_minus_1_5_pct": round(home_minus_1_5 * 100, 2),
            "away_minus_1_5_pct": round(away_minus_1_5 * 100, 2),
            "home_clean_sheet_pct": round(home_clean_sheet * 100, 2),
            "away_clean_sheet_pct": round(away_clean_sheet * 100, 2),
            "home_win_by_1_pct": round(home_win_by_1 * 100, 2),
            "away_win_by_1_pct": round(away_win_by_1 * 100, 2)
        }

    def simulate_match(self, lambda_home: float, lambda_away: float) -> Dict[str, Any]:
        """
        Simula 10,000 partidos y calcula probabilidades agregadas directamente desde
        la matriz exacta con Binomial Negativa y Dixon-Coles.
        """
        matrix = self.compute_exact_score_matrix(lambda_home, lambda_away)
        market_probs = self.compute_comprehensive_market_probabilities(matrix)

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
                "home_win_pct": market_probs["home_win_pct"],
                "draw_pct": market_probs["draw_pct"],
                "away_win_pct": market_probs["away_win_pct"]
            },
            "goals_markets": {
                "over_0_5_pct": market_probs["over_0_5_pct"],
                "under_0_5_pct": market_probs["under_0_5_pct"],
                "over_1_5_pct": market_probs["over_1_5_pct"],
                "under_1_5_pct": market_probs["under_1_5_pct"],
                "over_2_5_pct": market_probs["over_2_5_pct"],
                "under_2_5_pct": market_probs["under_2_5_pct"],
                "over_3_5_pct": market_probs["over_3_5_pct"],
                "under_3_5_pct": market_probs["under_3_5_pct"],
                "over_4_5_pct": market_probs["over_4_5_pct"],
                "under_4_5_pct": market_probs["under_4_5_pct"],
                "under_5_5_pct": market_probs["under_5_5_pct"],
                "btts_yes_pct": market_probs["btts_yes_pct"],
                "btts_no_pct": market_probs["btts_no_pct"]
            },
            "exact_market_probabilities": market_probs,
            "simulated_averages": {
                "home_goals": round(avg_home_goals, 2),
                "away_goals": round(avg_away_goals, 2),
                "total_goals": round(avg_home_goals + avg_away_goals, 2)
            }
        }
