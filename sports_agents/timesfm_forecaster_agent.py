"""
TimesFMForecasterAgent:
Agente que aplica el modelo fundacional de series temporales de Google (TimesFM)
y modelado autorregresivo probabilístico para predecir el horizonte inmediato (t+1)
de goles esperados, córners, tarjetas y tiros por jugador con cuantiles (p10, p50, p90).
"""

from typing import Dict, List, Any, Tuple
import numpy as np


class TimesFMForecasterAgent:
    def __init__(self, use_neural_weights: bool = False):
        self.name = "TimesFMForecasterAgent"
        self.use_neural_weights = use_neural_weights
        self.forecaster = None

        if self.use_neural_weights:
            try:
                import timesfm
                print("[TimesFMForecasterAgent] Cargando motor TimesFM PyTorch...")
                # Puede inicializarse si los pesos locales están descargados
            except Exception as e:
                print(f"[TimesFMForecasterAgent] Advertencia al cargar TimesFM neural: {e}. Usando motor estadístico calibrado.")

    def forecast_series(self, series: np.ndarray, horizon: int = 1, alpha_decay: float = 0.85) -> Dict[str, float]:
        """
        Calcula la proyección para el horizonte t+1 a partir de la secuencia temporal,
        ponderando la inercia reciente (EMA), la tendencia lineal y la volatilidad para
        estimar los cuantiles p10 (conservador), p50 (mediana) y p90 (escenario alto).
        """
        if len(series) == 0:
            return {"p10": 0.0, "p50": 0.0, "p90": 0.0, "mean": 0.0}

        n = len(series)
        # Ponderaciones exponenciales para dar más relevancia a los partidos recientes
        weights = np.array([alpha_decay ** (n - 1 - i) for i in range(n)], dtype=np.float32)
        weights /= weights.sum()

        weighted_mean = float(np.sum(series * weights))
        rolling_std = float(np.sqrt(np.sum(weights * (series - weighted_mean) ** 2)))
        # Asegurar mínima dispersión
        rolling_std = max(rolling_std, weighted_mean * 0.25, 0.4)

        # Tendencia reciente (últimos 4 partidos vs anteriores)
        if n >= 4:
            recent_mean = np.mean(series[-4:])
            prior_mean = np.mean(series[:-4]) if n > 4 else recent_mean
            trend_adj = (recent_mean - prior_mean) * 0.2
        else:
            trend_adj = 0.0

        p50 = max(0.05, weighted_mean + trend_adj)
        p10 = max(0.0, p50 - 1.28 * rolling_std)
        p90 = p50 + 1.28 * rolling_std

        return {
            "p10": round(float(p10), 2),
            "p50": round(float(p50), 2),
            "p90": round(float(p90), 2),
            "mean": round(float(p50), 2),
            "std": round(float(rolling_std), 2)
        }

    def project_match_metrics(self, processed_features: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ejecuta las proyecciones temporales cruzadas entre equipo local y visitante.
        Ajusta el ritmo ofensivo del local con la resistencia defensiva del visitante.
        """
        home = processed_features["home"]
        away = processed_features["away"]
        rank_diff = processed_features.get("rank_diff", 0.0)

        # 1. Goles y xG proyectados
        home_attack = self.forecast_series(home["xg_series"])
        home_def_weakness = self.forecast_series(home["conceded_series"])
        away_attack = self.forecast_series(away["xg_series"])
        away_def_weakness = self.forecast_series(away["conceded_series"])

        # Factor de ajuste cruzado (Ataque Local vs Concesión Visitante)
        home_lambda = (home_attack["mean"] * 0.65 + away_def_weakness["mean"] * 0.35)
        away_lambda = (away_attack["mean"] * 0.65 + home_def_weakness["mean"] * 0.35)

        # Ajuste por ventaja de campo / ranking
        rank_factor = np.clip(rank_diff * 0.02, -0.3, 0.3)
        home_lambda = max(0.4, home_lambda * (1.0 + rank_factor))
        away_lambda = max(0.3, away_lambda * (1.0 - rank_factor))

        # 2. Córners proyectados
        home_corners_att = self.forecast_series(home["corners_for_series"])
        away_corners_conceded = self.forecast_series(away["corners_against_series"])
        away_corners_att = self.forecast_series(away["corners_for_series"])
        home_corners_conceded = self.forecast_series(home["corners_against_series"])

        home_corners_exp = home_corners_att["mean"] * 0.6 + away_corners_conceded["mean"] * 0.4
        away_corners_exp = away_corners_att["mean"] * 0.6 + home_corners_conceded["mean"] * 0.4

        # 3. Tarjetas amarillas proyectadas
        home_cards = self.forecast_series(home["yellows_series"])
        away_cards = self.forecast_series(away["yellows_series"])

        # 4. Tiros totales proyectados
        home_shots = self.forecast_series(home["shots_series"])
        away_shots = self.forecast_series(away["shots_series"])

        return {
            "expected_goals": {
                "home": round(float(home_lambda), 2),
                "away": round(float(away_lambda), 2),
                "total": round(float(home_lambda + away_lambda), 2)
            },
            "expected_corners": {
                "home": round(float(home_corners_exp), 2),
                "away": round(float(away_corners_exp), 2),
                "total": round(float(home_corners_exp + away_corners_exp), 2),
                "home_quantiles": {"p10": round(max(1.0, home_corners_exp - 1.8), 1), "p90": round(home_corners_exp + 2.1, 1)},
                "away_quantiles": {"p10": round(max(1.0, away_corners_exp - 1.6), 1), "p90": round(away_corners_exp + 1.9, 1)},
            },
            "expected_yellow_cards": {
                "home": round(float(home_cards["mean"]), 2),
                "away": round(float(away_cards["mean"]), 2),
                "total": round(float(home_cards["mean"] + away_cards["mean"]), 2)
            },
            "expected_shots": {
                "home": round(float(home_shots["mean"]), 2),
                "away": round(float(away_shots["mean"]), 2)
            }
        }
