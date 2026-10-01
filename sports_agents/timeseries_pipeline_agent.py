"""
TimeSeriesPipelineAgent:
Transforma las secuencias históricas crudas de partidos en series temporales numéricas
estructuradas, con normalización, cálculo de tasas continuas, estacionalidad reciente
y preparación de entradas multivariadas con covariables.
"""

from typing import Dict, List, Any
import numpy as np


class TimeSeriesPipelineAgent:
    def __init__(self):
        self.name = "TimeSeriesPipelineAgent"

    def extract_time_series(self, sequence: List[Dict[str, Any]], metric_key: str) -> np.ndarray:
        """
        Extrae un array 1D de una métrica específica a lo largo del tiempo.
        """
        return np.array([match.get(metric_key, 0.0) for match in sequence], dtype=np.float32)

    def prepare_match_features(self, home_team_data: Dict[str, Any], away_team_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Construye el conjunto de series temporales para el emparejamiento entre equipo local y visitante.
        """
        home_seq = home_team_data.get("sequence", [])
        away_seq = away_team_data.get("sequence", [])

        # Series temporales clave
        home_goals_for = self.extract_time_series(home_seq, "goals_scored")
        home_goals_against = self.extract_time_series(home_seq, "goals_conceded")
        home_xg_for = self.extract_time_series(home_seq, "xg_for")
        home_corners_for = self.extract_time_series(home_seq, "corners_for")
        home_corners_against = self.extract_time_series(home_seq, "corners_against")
        home_yellows = self.extract_time_series(home_seq, "yellow_cards")
        home_shots = self.extract_time_series(home_seq, "shots_total")
        home_sot = self.extract_time_series(home_seq, "shots_on_target")

        away_goals_for = self.extract_time_series(away_seq, "goals_scored")
        away_goals_against = self.extract_time_series(away_seq, "goals_conceded")
        away_xg_for = self.extract_time_series(away_seq, "xg_for")
        away_corners_for = self.extract_time_series(away_seq, "corners_for")
        away_corners_against = self.extract_time_series(away_seq, "corners_against")
        away_yellows = self.extract_time_series(away_seq, "yellow_cards")
        away_shots = self.extract_time_series(away_seq, "shots_total")
        away_sot = self.extract_time_series(away_seq, "shots_on_target")

        # Covariable: Diferencial de ranking FIFA
        home_rank = home_team_data.get("fifa_rank", 15)
        away_rank = away_team_data.get("fifa_rank", 15)
        rank_diff = float(away_rank - home_rank)  # Positivo si el local tiene mejor ranking (número menor)

        return {
            "home": {
                "goals_series": home_goals_for,
                "conceded_series": home_goals_against,
                "xg_series": home_xg_for,
                "corners_for_series": home_corners_for,
                "corners_against_series": home_corners_against,
                "yellows_series": home_yellows,
                "shots_series": home_shots,
                "sot_series": home_sot,
                "rank": home_rank,
                "key_players": home_team_data.get("key_players", [])
            },
            "away": {
                "goals_series": away_goals_for,
                "conceded_series": away_goals_against,
                "xg_series": away_xg_for,
                "corners_for_series": away_corners_for,
                "corners_against_series": away_corners_against,
                "yellows_series": away_yellows,
                "shots_series": away_shots,
                "sot_series": away_sot,
                "rank": away_rank,
                "key_players": away_team_data.get("key_players", [])
            },
            "rank_diff": rank_diff
        }
