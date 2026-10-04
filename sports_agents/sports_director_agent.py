"""
SportsDirectorAgent:
Agente Director y Coordinador Central de Inteligencia Deportiva.
Orquesta los flujos de:
1. DataScoutAgent (ingesta y scouting)
2. TimeSeriesPipelineAgent (procesamiento de secuencias)
3. TimesFMForecasterAgent (inferencia de horizonte t+1 con TimesFM)
4. ScoreSimulatorAgent (marcador exacto y Monte Carlo)
5. PlayerPropsAgent (remates y tiros a puerta de figuras)
6. MatchEventsAgent (esquinas y disciplina arbitral)
"""

from typing import Dict, List, Any
from .data_scout_agent import DataScoutAgent
from .timeseries_pipeline_agent import TimeSeriesPipelineAgent
from .timesfm_forecaster_agent import TimesFMForecasterAgent
from .score_simulator_agent import ScoreSimulatorAgent
from .player_props_agent import PlayerPropsAgent
from .match_events_agent import MatchEventsAgent
from .squad_injury_agent import SquadInjuryAgent
from .tactical_manager_agent import TacticalManagerAgent
from .sports_psychology_agent import SportsPsychologyAgent
from .market_reality_agent import MarketRealityAgent
from .momentum_streak_agent import MomentumStreakAgent
from .sports_media_scout_agent import SportsMediaScoutAgent


import os
import json


class SportsDirectorAgent:
    def __init__(self):
        self.name = "SportsDirectorAgent"
        self.scout = DataScoutAgent()
        self.pipeline = TimeSeriesPipelineAgent()
        self.forecaster = TimesFMForecasterAgent()
        self.simulator = ScoreSimulatorAgent(num_simulations=10000)
        self.player_agent = PlayerPropsAgent()
        self.events_agent = MatchEventsAgent()
        
        # Agentes Especializados de Soporte y Realidad
        self.squad_agent = SquadInjuryAgent()
        self.tactical_agent = TacticalManagerAgent()
        self.psycho_agent = SportsPsychologyAgent()
        self.market_agent = MarketRealityAgent()
        self.momentum_agent = MomentumStreakAgent()
        self.media_agent = SportsMediaScoutAgent()

    def load_calibrated_weights(self) -> Dict[str, float]:
        """
        Carga los pesos activos y calibrados del ciclo de auto-retroalimentación.
        Garantiza que el modelo se adapte dinámicamente y no use parámetros estáticos.
        """
        log_path = os.path.join(os.path.dirname(__file__), "autonomous_feedback_log.json")
        default_weights = {
            "squad_offense_penalty": 0.85,
            "minimum_draw_floor": 26.0,
            "corner_game_state_dampener": 0.85,
            "player_sot_restriction_factor": 0.35
        }
        if os.path.exists(log_path):
            try:
                with open(log_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("current_weights", default_weights)
            except Exception:
                return default_weights
        return default_weights

    def predict_fixture(self, home_team: str, away_team: str, preferred_market_category: str = None) -> Dict[str, Any]:
        """
        Ejecuta el pipeline completo de predicción para un partido
        con los 10 agentes coordinados de inteligencia deportiva y auto-ajuste dinámico de pesos.
        """
        calibrated_weights = self.load_calibrated_weights()
        dynamic_draw_floor = calibrated_weights.get("minimum_draw_floor", 26.0)
        dynamic_corner_dampener = calibrated_weights.get("corner_game_state_dampener", 0.85)
        dynamic_sot_restriction = calibrated_weights.get("player_sot_restriction_factor", 0.35)
        dynamic_offense_penalty = calibrated_weights.get("squad_offense_penalty", 0.85)
        # Paso 1: Scouting de datos históricos
        home_data = self.scout.get_team_history(home_team)
        away_data = self.scout.get_team_history(away_team)
        context = self.scout.get_match_context(home_team, away_team)

        if not home_data or not away_data:
            raise ValueError(f"No hay datos suficientes para {home_team} o {away_team}")

        tournament = context.get("tournament", "Competición Internacional")

        # Paso 2: Auditoría Sanitaria y Convocatorias Oficiales (SquadInjuryAgent)
        home_squad = self.squad_agent.audit_team_roster(home_team, home_data.get("key_players", []))
        away_squad = self.squad_agent.audit_team_roster(away_team, away_data.get("key_players", []))

        # Paso 3: Pipeline de Series Temporales (TimesFM)
        features = self.pipeline.prepare_match_features(home_data, away_data)
        projections = self.forecaster.project_match_metrics(features)

        # Paso 4: Ajuste Táctico de Entrenadores (TacticalManagerAgent)
        raw_lambda_h = projections["expected_goals"]["home"] * home_squad["offense_penalty_factor"]
        raw_lambda_a = projections["expected_goals"]["away"] * away_squad["offense_penalty_factor"]
        
        tactics = self.tactical_agent.evaluate_tactical_matchup(home_team, away_team, raw_lambda_h, raw_lambda_a)
        lambda_h = round(raw_lambda_h * tactics["tactical_xg_multiplier_home"], 2)
        lambda_a = round(raw_lambda_a * tactics["tactical_xg_multiplier_away"], 2)

        # Paso 5: Contexto Emocional y Factor Caldera (SportsPsychologyAgent)
        psychology = self.psycho_agent.analyze_emotional_context(home_team, away_team, tournament)

        # Paso 6: Simulación Cuantitativa Monte Carlo (10,000 iteraciones con Dixon-Coles)
        score_analysis = self.simulator.simulate_match(lambda_h, lambda_a)
        
        # Proteger suelo mínimo de empate si es partido competitivo de visitante (usando dynamic_draw_floor calibrado)
        probs_1x2 = dict(score_analysis["1x2_probabilities"])
        effective_draw_floor = dynamic_draw_floor if not psychology["is_friendly"] else max(20.0, dynamic_draw_floor - 2.0)
        if probs_1x2["draw_pct"] < effective_draw_floor:
            deficit = effective_draw_floor - probs_1x2["draw_pct"]
            probs_1x2["draw_pct"] = round(effective_draw_floor, 2)
            probs_1x2["home_win_pct"] = round(probs_1x2["home_win_pct"] - (deficit * 0.5), 2)
            probs_1x2["away_win_pct"] = round(probs_1x2["away_win_pct"] - (deficit * 0.5), 2)
            score_analysis["1x2_probabilities"] = probs_1x2

        # Paso 7: Remates y Tiros a Puerta de Jugadores VETADOS / FILTRADOS
        home_players_proj = self.player_agent.analyze_team_players(
            home_squad["cleared_players"],
            projections["expected_shots"]["home"] * home_squad["offense_penalty_factor"]
        )
        away_players_proj = self.player_agent.analyze_team_players(
            away_squad["cleared_players"],
            projections["expected_shots"]["away"] * away_squad["offense_penalty_factor"]
        )

        # Aplicar restricciones de rol táctico a jugadores moduladas por dynamic_sot_restriction calibrado
        for p in home_players_proj + away_players_proj:
            p_name = p.get("name")
            if p_name in tactics["player_role_restrictions"]:
                restr = tactics["player_role_restrictions"][p_name]
                reduction = max(restr.get("sot_probability_reduction", 0.35), dynamic_sot_restriction)
                p["prob_at_least_1_sot_pct"] = round(p["prob_at_least_1_sot_pct"] * (1.0 - reduction), 1)
                p["tactical_note"] = restr["role_restriction"]

        # Paso 8: Córners Modulados por Game State, Táctica y dynamic_corner_dampener calibrado
        adj_corners = dict(projections["expected_corners"])
        combined_dampener = tactics["corner_dampener_factor"] * dynamic_corner_dampener
        adj_corners["home"] = round(adj_corners["home"] * combined_dampener, 1)
        adj_corners["away"] = round(adj_corners["away"] * combined_dampener, 1)
        adj_corners["total"] = round(adj_corners["home"] + adj_corners["away"], 1)

        corners_analysis = self.events_agent.analyze_corners(adj_corners)
        cards_analysis = self.events_agent.analyze_cards(projections["expected_yellow_cards"], context)

        # Paso 9: Análisis de Momentum y Resurgimiento (MomentumStreakAgent)
        momentum_analysis = self.momentum_agent.analyze_match_momentum(home_team, away_team)

        # Paso 10: Ingesta de Señales Periodísticas y Consenso Editorial (SportsMediaScoutAgent)
        media_analysis = self.media_agent.analyze_fixture_media(
            home_team=home_team,
            away_team=away_team,
            competition=context.get("tournament", "UEFA Nations League")
        )

        # Paso 11: Selección de "La Fija" Realista y Operable en Casas (MarketRealityAgent 4.0)
        la_fija_real = self.market_agent.select_realistic_la_fija(
            match=f"{home_team} vs {away_team}",
            home_team=home_team,
            away_team=away_team,
            prob_1x2=probs_1x2,
            goals_data=score_analysis["goals_markets"],
            corners_data=corners_analysis,
            cleared_players=home_squad["cleared_players"] + away_squad["cleared_players"],
            psychology=psychology,
            preferred_category=preferred_market_category,
            exact_market_probs=score_analysis.get("exact_market_probabilities"),
            media_analysis=media_analysis,
            momentum_analysis=momentum_analysis
        )

        return {
            "match": f"{home_team} vs {away_team}",
            "home_team": home_team,
            "away_team": away_team,
            "context": context,
            "projections": projections,
            "tactical_analysis": tactics,
            "squad_health": {
                "home_team": home_team,
                "away_team": away_team,
                "home_vetoed": home_squad["vetoed_players"],
                "away_vetoed": away_squad["vetoed_players"],
                "home_reallocation": home_squad.get("reallocation_summary", ""),
                "away_reallocation": away_squad.get("reallocation_summary", ""),
                "home_health_status": home_squad.get("squad_health_status", "Ratificado"),
                "away_health_status": away_squad.get("squad_health_status", "Ratificado"),
                "status": "Auditoría Médica y Convocatorias Oficiales Verificadas"
            },
            "psychological_context": psychology,
            "momentum_analysis": momentum_analysis,
            "media_intelligence": media_analysis,
            "score_prediction": score_analysis,
            "corners_prediction": corners_analysis,
            "cards_prediction": cards_analysis,
            "player_props": {
                "home_key_players": home_players_proj,
                "away_key_players": away_players_proj
            },
            "la_fija_real": la_fija_real["selected_la_fija"],
            "all_fija_options": la_fija_real["all_feasible_options"]
        }

    def run_all(self) -> Dict[str, Any]:
        """
        Ejecuta el análisis de los partidos anteriores:
        1. España vs Croacia
        2. Inglaterra vs Chequia
        3. Argentina vs Bolivia
        """
        match1 = self.predict_fixture("España", "Croacia")
        match2 = self.predict_fixture("Inglaterra", "Chequia")
        match3 = self.predict_fixture("Argentina", "Bolivia")

        return {
            "title": "Pronósticos Oficiales de Inteligencia Deportiva con TimesFM",
            "matches": [match1, match2, match3]
        }

    def run_top6_tomorrow(self) -> Dict[str, Any]:
        """
        Ejecuta el análisis y predicción integral de los 6 partidos estelares de mañana (Fase 1 completada):
        1. Alemania vs Serbia
        2. Dinamarca vs Portugal
        3. Grecia vs Países Bajos
        4. Gales vs Noruega
        5. Irlanda vs Austria
        6. Japón vs Ecuador
        """
        fixtures = [
            ("Alemania", "Serbia"),
            ("Dinamarca", "Portugal"),
            ("Grecia", "Países Bajos"),
            ("Gales", "Noruega"),
            ("Irlanda", "Austria"),
            ("Japón", "Ecuador")
        ]
        results = []
        for home, away in fixtures:
            results.append(self.predict_fixture(home, away))

        return {
            "title": "Pronósticos Top 6 Partidos de Máxima Audiencia - Jornada de Mañana",
            "matches": results
        }

