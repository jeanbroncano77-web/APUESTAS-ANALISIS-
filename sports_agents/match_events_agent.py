"""
MatchEventsAgent:
Especialista en mercados secundarios y eventos clave:
- Córners (esquinas): por equipo y totales con líneas Over/Under y cuantiles.
- Tarjetas: amarillas por equipo, rojas esperadas, total disciplinario y probabilidad de expulsión.
"""

from typing import Dict, List, Any
import numpy as np
from scipy.stats import poisson


class MatchEventsAgent:
    def __init__(self):
        self.name = "MatchEventsAgent"

    def analyze_corners(self, exp_corners: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calcula probabilidades para las esquinas por equipo y totales.
        """
        home_mu = exp_corners["home"]
        away_mu = exp_corners["away"]
        total_mu = home_mu + away_mu

        # Distribuciones Poisson para líneas de mercado comunes
        # Over 8.5 corners
        over_8_5 = 1.0 - sum(poisson.pmf(k, total_mu) for k in range(9))
        over_9_5 = 1.0 - sum(poisson.pmf(k, total_mu) for k in range(10))
        over_10_5 = 1.0 - sum(poisson.pmf(k, total_mu) for k in range(11))
        over_11_5 = 1.0 - sum(poisson.pmf(k, total_mu) for k in range(12))

        # Líneas de equipo
        home_over_4_5 = 1.0 - sum(poisson.pmf(k, home_mu) for k in range(5))
        home_over_5_5 = 1.0 - sum(poisson.pmf(k, home_mu) for k in range(6))
        away_over_3_5 = 1.0 - sum(poisson.pmf(k, away_mu) for k in range(4))
        away_over_4_5 = 1.0 - sum(poisson.pmf(k, away_mu) for k in range(5))

        return {
            "home_corners_expected": home_mu,
            "away_corners_expected": away_mu,
            "total_corners_expected": round(total_mu, 1),
            "most_likely_range": f"{int(np.floor(total_mu - 1))} - {int(np.ceil(total_mu + 1))} córners",
            "lines": {
                "over_8_5_pct": round(over_8_5 * 100, 1),
                "under_8_5_pct": round((1.0 - over_8_5) * 100, 1),
                "over_9_5_pct": round(over_9_5 * 100, 1),
                "under_9_5_pct": round((1.0 - over_9_5) * 100, 1),
                "over_10_5_pct": round(over_10_5 * 100, 1),
                "under_10_5_pct": round((1.0 - over_10_5) * 100, 1),
                "over_11_5_pct": round(over_11_5 * 100, 1),
                "under_11_5_pct": round((1.0 - over_11_5) * 100, 1),
            },
            "team_lines": {
                "home_over_4_5_pct": round(home_over_4_5 * 100, 1),
                "home_over_5_5_pct": round(home_over_5_5 * 100, 1),
                "away_over_3_5_pct": round(away_over_3_5 * 100, 1),
                "away_over_4_5_pct": round(away_over_4_5 * 100, 1),
            }
        }

    def analyze_cards(self, exp_yellows: Dict[str, Any], referee_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Proyecta tarjetas amarillas y rojas integrando el perfil del árbitro asignado.
        """
        ref_yellow_avg = referee_context.get("referee_avg_yellows", 4.0)
        ref_red_avg = referee_context.get("referee_avg_reds", 0.20)

        # Ajuste combinado entre tendencia del equipo y severidad del colegiado
        team_yellow_sum = exp_yellows["total"]
        adjusted_yellows = (team_yellow_sum * 0.55) + (ref_yellow_avg * 0.45)

        home_share = exp_yellows["home"] / max(0.1, team_yellow_sum)
        away_share = exp_yellows["away"] / max(0.1, team_yellow_sum)

        home_yellows = round(adjusted_yellows * home_share, 1)
        away_yellows = round(adjusted_yellows * away_share, 1)
        total_yellows = round(home_yellows + away_yellows, 1)

        # Tarjetas rojas (Poisson para expulsión en 90 min)
        red_lambda = ref_red_avg * 0.95
        home_red_prob = round((red_lambda * home_share) * 100, 1)
        away_red_prob = round((red_lambda * away_share) * 100, 1)
        any_red_prob = round((1.0 - np.exp(-red_lambda)) * 100, 1)

        # Líneas de tarjetas totales
        over_3_5_cards = 1.0 - sum(poisson.pmf(k, adjusted_yellows) for k in range(4))
        over_4_5_cards = 1.0 - sum(poisson.pmf(k, adjusted_yellows) for k in range(5))
        over_5_5_cards = 1.0 - sum(poisson.pmf(k, adjusted_yellows) for k in range(6))

        return {
            "referee": referee_context.get("referee", "Árbitro Designado"),
            "home_yellow_cards": home_yellows,
            "away_yellow_cards": away_yellows,
            "total_yellow_cards": total_yellows,
            "red_cards": {
                "expected_home_reds": round(red_lambda * home_share, 2),
                "expected_away_reds": round(red_lambda * away_share, 2),
                "expected_total_reds": round(red_lambda, 2),
                "home_red_prob_pct": home_red_prob,
                "away_red_prob_prob_pct": away_red_prob,
                "any_red_card_in_match_pct": any_red_prob
            },
            "total_cards_expected": round(total_yellows + red_lambda, 1),
            "card_lines": {
                "over_3_5_cards_pct": round(over_3_5_cards * 100, 1),
                "under_3_5_cards_pct": round((1.0 - over_3_5_cards) * 100, 1),
                "over_4_5_cards_pct": round(over_4_5_cards * 100, 1),
                "under_4_5_cards_pct": round((1.0 - over_4_5_cards) * 100, 1),
                "over_5_5_cards_pct": round(over_5_5_cards * 100, 1),
                "under_5_5_cards_pct": round((1.0 - over_5_5_cards) * 100, 1),
            }
        }
