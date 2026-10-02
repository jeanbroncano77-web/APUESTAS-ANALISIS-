"""
DataScoutAgent:
Agente responsable de la ingesta y estructuración de datos deportivos históricos,
series temporales de partidos recientes, métricas de rendimiento y perfiles de jugadores.
Soporta los 6 partidos estelares de máxima audiencia internacional para la jornada de mañana.
"""

import os
import json
from typing import Dict, List, Any


class DataScoutAgent:
    def __init__(self):
        self.name = "DataScoutAgent"

    def get_team_history(self, team_name: str) -> Dict[str, Any]:
        """
        Retorna las secuencias cronológicas recientes para el equipo especificado.
        """
        # 1. Comprobar base de datos externa JSON si existe
        ext_teams_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "teams_database.json")
        if os.path.exists(ext_teams_file):
            try:
                with open(ext_teams_file, "r", encoding="utf-8") as f:
                    ext_data = json.load(f)
                    if team_name in ext_data:
                        return ext_data[team_name]
            except Exception:
                pass

        histories = {
            # --- PARTIDO 1: ALEMANIA VS SERBIA ---
            "Alemania": {
                "fifa_rank": 11,
                "recent_form": ["W", "W", "D", "W", "W", "L", "W", "W", "D", "W"],
                "sequence": [
                    {"goals_scored": 5, "goals_conceded": 0, "xg_for": 3.4, "xg_against": 0.4, "corners_for": 8, "corners_against": 2, "shots_total": 21, "shots_on_target": 9, "yellow_cards": 1, "red_cards": 0, "fouls": 9,  "possession": 68},
                    {"goals_scored": 2, "goals_conceded": 2, "xg_for": 2.1, "xg_against": 1.6, "corners_for": 6, "corners_against": 5, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 61},
                    {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.9, "xg_against": 1.1, "corners_for": 7, "corners_against": 4, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 64},
                    {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.8, "xg_against": 0.6, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 8,  "possession": 63},
                    {"goals_scored": 7, "goals_conceded": 0, "xg_for": 4.1, "xg_against": 0.2, "corners_for": 9, "corners_against": 1, "shots_total": 24, "shots_on_target": 12, "yellow_cards": 0, "red_cards": 0, "fouls": 7,  "possession": 73},
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.7, "xg_against": 1.2, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 5, "yellow_cards": 3, "red_cards": 0, "fouls": 12, "possession": 59},
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.2, "xg_against": 0.5, "corners_for": 7, "corners_against": 3, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 9,  "possession": 65},
                ],
                "key_players": [
                    {"name": "Jamal Musiala", "position": "Mediapunta / Extremo", "avg_shots_p90": 3.1, "avg_sot_p90": 1.5, "shot_creation_actions": 5.4, "goal_prob": 0.42},
                    {"name": "Florian Wirtz", "position": "Mediapunta Creador", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 5.8, "goal_prob": 0.38},
                    {"name": "Kai Havertz", "position": "Delantero Centro", "avg_shots_p90": 2.9, "avg_sot_p90": 1.4, "shot_creation_actions": 3.6, "goal_prob": 0.44},
                    {"name": "Deniz Undav", "position": "Delantero / Segundo Punta", "avg_shots_p90": 2.5, "avg_sot_p90": 1.2, "shot_creation_actions": 2.9, "goal_prob": 0.36},
                    {"name": "Joshua Kimmich", "position": "Lateral / Mediocentro", "avg_shots_p90": 1.3, "avg_sot_p90": 0.4, "shot_creation_actions": 4.5, "goal_prob": 0.12}
                ]
            },
            "Serbia": {
                "fifa_rank": 32,
                "recent_form": ["L", "D", "W", "D", "L", "D", "L", "W", "D"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.8, "xg_against": 1.7, "corners_for": 4, "corners_against": 6, "shots_total": 9,  "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 42},
                    {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.9, "xg_against": 1.9, "corners_for": 3, "corners_against": 7, "shots_total": 8,  "shots_on_target": 2, "yellow_cards": 4, "red_cards": 0, "fouls": 16, "possession": 44},
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.6, "xg_against": 1.0, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 48},
                    {"goals_scored": 0, "goals_conceded": 3, "xg_for": 0.7, "xg_against": 2.4, "corners_for": 3, "corners_against": 8, "shots_total": 7,  "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 39},
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.2, "xg_against": 1.3, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 4, "yellow_cards": 4, "red_cards": 0, "fouls": 17, "possession": 46},
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 1.1, "xg_against": 1.1, "corners_for": 4, "corners_against": 5, "shots_total": 11, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 47},
                ],
                "key_players": [
                    {"name": "Dušan Vlahović", "position": "Delantero Centro", "avg_shots_p90": 2.7, "avg_sot_p90": 1.2, "shot_creation_actions": 2.4, "goal_prob": 0.35},
                    {"name": "Aleksandar Mitrović", "position": "Delantero Centro", "avg_shots_p90": 2.6, "avg_sot_p90": 1.1, "shot_creation_actions": 2.1, "goal_prob": 0.36},
                    {"name": "Lazar Samardžić", "position": "Mediapunta Creativo", "avg_shots_p90": 1.7, "avg_sot_p90": 0.6, "shot_creation_actions": 3.8, "goal_prob": 0.18},
                    {"name": "Saša Lukić", "position": "Mediocentro", "avg_shots_p90": 1.1, "avg_sot_p90": 0.3, "shot_creation_actions": 2.2, "goal_prob": 0.10}
                ]
            },

            # --- PARTIDO 2: DINAMARCA VS PORTUGAL ---
            "Dinamarca": {
                "fifa_rank": 20,
                "recent_form": ["W", "W", "L", "D", "W", "D", "L", "W"],
                "sequence": [
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.9, "xg_against": 0.6, "corners_for": 6, "corners_against": 3, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 58},
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.8, "xg_against": 0.7, "corners_for": 7, "corners_against": 4, "shots_total": 15, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 56},
                    {"goals_scored": 0, "goals_conceded": 1, "xg_for": 1.1, "xg_against": 1.3, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 49},
                    {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.7, "xg_against": 1.5, "corners_for": 5, "corners_against": 6, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 52},
                    {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.2, "xg_against": 1.8, "corners_for": 4, "corners_against": 6, "shots_total": 10, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 47},
                ],
                "key_players": [
                    {"name": "Rasmus Højlund", "position": "Delantero Centro", "avg_shots_p90": 2.5, "avg_sot_p90": 1.2, "shot_creation_actions": 2.2, "goal_prob": 0.38},
                    {"name": "Christian Eriksen", "position": "Mediapunta Creador", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 5.2, "goal_prob": 0.22},
                    {"name": "Pierre-Emile Højbjerg", "position": "Mediocentro Llegada", "avg_shots_p90": 1.5, "avg_sot_p90": 0.6, "shot_creation_actions": 3.1, "goal_prob": 0.16},
                    {"name": "Mikkel Damsgaard", "position": "Extremo", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 3.6, "goal_prob": 0.20}
                ]
            },
            "Portugal": {
                "fifa_rank": 8,
                "recent_form": ["W", "W", "W", "D", "W", "D", "W", "W", "W"],
                "sequence": [
                    {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.2, "xg_against": 0.8, "corners_for": 7, "corners_against": 3, "shots_total": 18, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 9,  "possession": 62},
                    {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.4, "xg_against": 0.9, "corners_for": 8, "corners_against": 4, "shots_total": 19, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 65},
                    {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.7, "xg_against": 1.1, "corners_for": 6, "corners_against": 4, "shots_total": 17, "shots_on_target": 8, "yellow_cards": 2, "red_cards": 0, "fouls": 8,  "possession": 61},
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 1.4, "xg_against": 0.6, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 63},
                    {"goals_scored": 5, "goals_conceded": 1, "xg_for": 3.6, "xg_against": 0.8, "corners_for": 9, "corners_against": 2, "shots_total": 22, "shots_on_target": 11, "yellow_cards": 1, "red_cards": 0, "fouls": 8,  "possession": 67},
                ],
                "key_players": [
                    {"name": "Cristiano Ronaldo", "position": "Delantero Centro", "avg_shots_p90": 3.8, "avg_sot_p90": 1.8, "shot_creation_actions": 3.1, "goal_prob": 0.52},
                    {"name": "Bruno Fernandes", "position": "Mediapunta Organizador", "avg_shots_p90": 2.9, "avg_sot_p90": 1.3, "shot_creation_actions": 6.2, "goal_prob": 0.36},
                    {"name": "Rafael Leão", "position": "Extremo Desborde", "avg_shots_p90": 2.6, "avg_sot_p90": 1.1, "shot_creation_actions": 4.8, "goal_prob": 0.32},
                    {"name": "Bernardo Silva", "position": "Interior / Extremo", "avg_shots_p90": 1.7, "avg_sot_p90": 0.7, "shot_creation_actions": 5.1, "goal_prob": 0.22}
                ]
            },

            # --- PARTIDO 3: GRECIA VS PAÍSES BAJOS ---
            "Grecia": {
                "fifa_rank": 48,
                "recent_form": ["W", "W", "W", "L", "W", "D", "W", "L"],
                "sequence": [
                    {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.1, "xg_against": 0.5, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 54},
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.7, "xg_against": 0.8, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 49},
                    {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.8, "xg_against": 1.2, "corners_for": 5, "corners_against": 5, "shots_total": 13, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 48},
                    {"goals_scored": 0, "goals_conceded": 3, "xg_for": 0.7, "xg_against": 2.2, "corners_for": 3, "corners_against": 7, "shots_total": 8,  "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 16, "possession": 41},
                ],
                "key_players": [
                    {"name": "Vangelis Pavlidis", "position": "Delantero Centro", "avg_shots_p90": 2.6, "avg_sot_p90": 1.2, "shot_creation_actions": 2.5, "goal_prob": 0.35},
                    {"name": "Tasos Bakasetas", "position": "Mediapunta / Tiros Lejanos", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 4.1, "goal_prob": 0.26},
                    {"name": "Christos Tzolis", "position": "Extremo", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 3.2, "goal_prob": 0.22}
                ]
            },
            "Países Bajos": {
                "fifa_rank": 7,
                "recent_form": ["W", "D", "W", "W", "D", "W", "L", "W"],
                "sequence": [
                    {"goals_scored": 5, "goals_conceded": 2, "xg_for": 3.1, "xg_against": 1.3, "corners_for": 7, "corners_against": 3, "shots_total": 19, "shots_on_target": 9, "yellow_cards": 1, "red_cards": 0, "fouls": 9,  "possession": 66},
                    {"goals_scored": 2, "goals_conceded": 2, "xg_for": 2.0, "xg_against": 1.6, "corners_for": 6, "corners_against": 5, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 59},
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.5, "xg_against": 1.0, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 1, "fouls": 14, "possession": 56},
                    {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.9, "xg_against": 1.5, "corners_for": 4, "corners_against": 6, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 53},
                    {"goals_scored": 4, "goals_conceded": 0, "xg_for": 2.8, "xg_against": 0.5, "corners_for": 8, "corners_against": 2, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 8,  "possession": 64},
                ],
                "key_players": [
                    {"name": "Cody Gakpo", "position": "Extremo / Delantero", "avg_shots_p90": 3.2, "avg_sot_p90": 1.5, "shot_creation_actions": 4.6, "goal_prob": 0.45},
                    {"name": "Xavi Simons", "position": "Mediapunta Dinámico", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 5.2, "goal_prob": 0.32},
                    {"name": "Tijjani Reijnders", "position": "Centrocampista Llegada", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 4.0, "goal_prob": 0.28},
                    {"name": "Donyell Malen", "position": "Extremo / Delantero", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 2.8, "goal_prob": 0.30}
                ]
            },

            # --- PARTIDO 4: GALES VS NORUEGA ---
            "Gales": {
                "fifa_rank": 29,
                "recent_form": ["D", "W", "D", "W", "L", "D", "W"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 1.1, "xg_against": 0.9, "corners_for": 5, "corners_against": 4, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 51},
                    {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.7, "xg_against": 1.2, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 48},
                    {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.6, "xg_against": 1.5, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 52},
                    {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.4, "xg_against": 0.8, "corners_for": 5, "corners_against": 3, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 53},
                    {"goals_scored": 4, "goals_conceded": 1, "xg_for": 2.6, "xg_against": 0.9, "corners_for": 7, "corners_against": 3, "shots_total": 16, "shots_on_target": 8, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 57},
                ],
                "key_players": [
                    {"name": "Brennan Johnson", "position": "Extremo Veloz", "avg_shots_p90": 2.7, "avg_sot_p90": 1.2, "shot_creation_actions": 4.1, "goal_prob": 0.36},
                    {"name": "Harry Wilson", "position": "Mediapunta / Tiros Libres", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 4.8, "goal_prob": 0.30},
                    {"name": "Daniel James", "position": "Extremo Desborde", "avg_shots_p90": 1.9, "avg_sot_p90": 0.7, "shot_creation_actions": 3.2, "goal_prob": 0.20}
                ]
            },
            "Noruega": {
                "fifa_rank": 43,
                "recent_form": ["D", "W", "W", "L", "W", "D", "W"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 1.6, "xg_against": 0.7, "corners_for": 6, "corners_against": 3, "shots_total": 15, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 56},
                    {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.1, "xg_against": 0.9, "corners_for": 7, "corners_against": 3, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 9,  "possession": 59},
                    {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.8, "xg_against": 0.6, "corners_for": 8, "corners_against": 3, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 62},
                    {"goals_scored": 1, "goals_conceded": 5, "xg_for": 1.2, "xg_against": 2.6, "corners_for": 4, "corners_against": 6, "shots_total": 9,  "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 47},
                    {"goals_scored": 4, "goals_conceded": 1, "xg_for": 3.0, "xg_against": 0.8, "corners_for": 7, "corners_against": 3, "shots_total": 17, "shots_on_target": 8, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 60},
                ],
                "key_players": [
                    {"name": "Erling Haaland", "position": "Delantero Centro Élite", "avg_shots_p90": 4.1, "avg_sot_p90": 2.2, "shot_creation_actions": 2.8, "goal_prob": 0.62},
                    {"name": "Alexander Sørloth", "position": "Delantero / Segundo Punta", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 3.0, "goal_prob": 0.35},
                    {"name": "Antonio Nusa", "position": "Extremo Regate", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 4.2, "goal_prob": 0.25},
                    {"name": "Sander Berge", "position": "Mediocentro Físico", "avg_shots_p90": 1.1, "avg_sot_p90": 0.3, "shot_creation_actions": 2.6, "goal_prob": 0.10}
                ]
            },

            # --- PARTIDO 5: IRLANDA VS AUSTRIA ---
            "Irlanda": {
                "fifa_rank": 62,
                "recent_form": ["L", "L", "W", "L", "D", "W", "L"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.7, "xg_against": 1.8, "corners_for": 3, "corners_against": 6, "shots_total": 8,  "shots_on_target": 2, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 42},
                    {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.8, "xg_against": 1.6, "corners_for": 4, "corners_against": 5, "shots_total": 9,  "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 44},
                    {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.5, "xg_against": 1.2, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 49},
                    {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.9, "xg_against": 1.7, "corners_for": 4, "corners_against": 6, "shots_total": 9,  "shots_on_target": 2, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 45},
                ],
                "key_players": [
                    {"name": "Evan Ferguson", "position": "Delantero Centro", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 2.1, "goal_prob": 0.32},
                    {"name": "Sammie Szmodics", "position": "Mediapunta Llegada", "avg_shots_p90": 2.1, "avg_sot_p90": 0.8, "shot_creation_actions": 3.1, "goal_prob": 0.24},
                    {"name": "Chiedozie Ogbene", "position": "Extremo Veloz", "avg_shots_p90": 1.8, "avg_sot_p90": 0.6, "shot_creation_actions": 3.4, "goal_prob": 0.18}
                ]
            },
            "Austria": {
                "fifa_rank": 22,
                "recent_form": ["D", "L", "W", "W", "D", "W", "L"],
                "sequence": [
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.7, "xg_against": 1.1, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 15, "possession": 56},
                    {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.6, "xg_against": 1.4, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 16, "possession": 54},
                    {"goals_scored": 4, "goals_conceded": 0, "xg_for": 2.8, "xg_against": 0.5, "corners_for": 8, "corners_against": 2, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 13, "possession": 62},
                    {"goals_scored": 5, "goals_conceded": 1, "xg_for": 3.2, "xg_against": 0.9, "corners_for": 7, "corners_against": 3, "shots_total": 19, "shots_on_target": 9, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 61},
                ],
                "key_players": [
                    {"name": "Marcel Sabitzer", "position": "Centrocampista Llegada", "avg_shots_p90": 2.7, "avg_sot_p90": 1.2, "shot_creation_actions": 4.6, "goal_prob": 0.35},
                    {"name": "Christoph Baumgartner", "position": "Mediapunta Vertical", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 4.2, "goal_prob": 0.38},
                    {"name": "Konrad Laimer", "position": "Interior / Presión", "avg_shots_p90": 1.6, "avg_sot_p90": 0.6, "shot_creation_actions": 3.8, "goal_prob": 0.18},
                    {"name": "Marko Arnautović", "position": "Delantero Centro", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 2.6, "goal_prob": 0.40}
                ]
            },

            # --- PARTIDO 6: JAPÓN VS ECUADOR ---
            "Japón": {
                "fifa_rank": 16,
                "recent_form": ["W", "W", "W", "W", "D", "W", "W"],
                "sequence": [
                    {"goals_scored": 7, "goals_conceded": 0, "xg_for": 4.2, "xg_against": 0.2, "corners_for": 9, "corners_against": 1, "shots_total": 23, "shots_on_target": 12, "yellow_cards": 0, "red_cards": 0, "fouls": 8,  "possession": 72},
                    {"goals_scored": 5, "goals_conceded": 0, "xg_for": 3.5, "xg_against": 0.4, "corners_for": 8, "corners_against": 2, "shots_total": 20, "shots_on_target": 10, "yellow_cards": 1, "red_cards": 0, "fouls": 9,  "possession": 68},
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.2, "xg_against": 0.6, "corners_for": 6, "corners_against": 3, "shots_total": 15, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 61},
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.8, "xg_against": 0.9, "corners_for": 7, "corners_against": 4, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 59},
                    {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.5, "xg_against": 0.8, "corners_for": 7, "corners_against": 3, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 9,  "possession": 63},
                ],
                "key_players": [
                    {"name": "Kaoru Mitoma", "position": "Extremo Izquierdo Élite", "avg_shots_p90": 2.9, "avg_sot_p90": 1.4, "shot_creation_actions": 5.4, "goal_prob": 0.38},
                    {"name": "Takefusa Kubo", "position": "Extremo / Creador", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 5.6, "goal_prob": 0.34},
                    {"name": "Ritsu Doan", "position": "Interior / Extremo", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 4.1, "goal_prob": 0.28},
                    {"name": "Ayase Ueda", "position": "Delantero Centro", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 2.3, "goal_prob": 0.45}
                ]
            },
            "Ecuador": {
                "fifa_rank": 27,
                "recent_form": ["W", "D", "W", "L", "D", "W", "D"],
                "sequence": [
                    {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.6, "xg_against": 0.5, "corners_for": 5, "corners_against": 3, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 54},
                    {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.8, "xg_against": 1.4, "corners_for": 4, "corners_against": 5, "shots_total": 9,  "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 46},
                    {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.7, "xg_against": 0.6, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 56},
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.9, "xg_against": 0.9, "corners_for": 4, "corners_against": 4, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 48},
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 1.1, "xg_against": 0.8, "corners_for": 5, "corners_against": 4, "shots_total": 11, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 52},
                ],
                "key_players": [
                    {"name": "Enner Valencia", "position": "Delantero Histórico", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 2.4, "goal_prob": 0.36},
                    {"name": "Moisés Caicedo", "position": "Pivote / Motor", "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 3.8, "goal_prob": 0.14},
                    {"name": "Kendry Páez", "position": "Mediapunta Perla", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 4.5, "goal_prob": 0.26},
                    {"name": "Gonzalo Plata", "position": "Extremo Regate", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 3.6, "goal_prob": 0.22}
                ]
            },

            # --- JORNADA DE MAÑANA (TOP 6 ESTELARES CLUB FOOTBALL) ---
            "Real Madrid": {
                "fifa_rank": 2,
                "recent_form": ["W", "W", "D", "W", "W", "W", "W"],
                "sequence": [
                    {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.8, "xg_against": 0.8, "corners_for": 7, "corners_against": 3, "shots_total": 19, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 9,  "possession": 63},
                    {"goals_scored": 4, "goals_conceded": 1, "xg_for": 3.1, "xg_against": 0.9, "corners_for": 8, "corners_against": 4, "shots_total": 21, "shots_on_target": 9, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 65},
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.7, "xg_against": 1.2, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 58},
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.3, "xg_against": 0.6, "corners_for": 7, "corners_against": 3, "shots_total": 18, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 8,  "possession": 62},
                    {"goals_scored": 3, "goals_conceded": 2, "xg_for": 2.5, "xg_against": 1.4, "corners_for": 6, "corners_against": 4, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 9,  "possession": 61},
                ],
                "key_players": [
                    {"name": "Kylian Mbappé", "position": "Delantero Centro Élite", "avg_shots_p90": 4.3, "avg_sot_p90": 2.1, "shot_creation_actions": 4.5, "goal_prob": 0.68},
                    {"name": "Jude Bellingham", "position": "Mediapunta Llegada", "avg_shots_p90": 2.8, "avg_sot_p90": 1.4, "shot_creation_actions": 5.2, "goal_prob": 0.42},
                    {"name": "Vinícius Jr.", "position": "Extremo Desborde", "avg_shots_p90": 3.4, "avg_sot_p90": 1.6, "shot_creation_actions": 6.1, "goal_prob": 0.52},
                    {"name": "Federico Valverde", "position": "Interior / Potencia", "avg_shots_p90": 2.1, "avg_sot_p90": 0.8, "shot_creation_actions": 3.8, "goal_prob": 0.22}
                ]
            },
            "Villarreal": {
                "fifa_rank": 24,
                "recent_form": ["W", "L", "W", "W", "D", "W"],
                "sequence": [
                    {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.8, "xg_against": 1.2, "corners_for": 5, "corners_against": 5, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 51},
                    {"goals_scored": 1, "goals_conceded": 5, "xg_for": 1.3, "xg_against": 2.9, "corners_for": 4, "corners_against": 7, "shots_total": 10, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 44},
                    {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.2, "xg_against": 1.1, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 53},
                    {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.9, "xg_against": 1.7, "corners_for": 5, "corners_against": 5, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 49},
                ],
                "key_players": [
                    {"name": "Ayoze Pérez", "position": "Segundo Delantero", "avg_shots_p90": 2.7, "avg_sot_p90": 1.3, "shot_creation_actions": 3.4, "goal_prob": 0.40},
                    {"name": "Álex Baena", "position": "Mediapunta Creador", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 5.8, "goal_prob": 0.24},
                    {"name": "Thierno Barry", "position": "Delantero Centro Físico", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 2.1, "goal_prob": 0.35}
                ]
            },
            "Barcelona": {
                "fifa_rank": 3,
                "recent_form": ["W", "W", "W", "W", "L", "W", "W"],
                "sequence": [
                    {"goals_scored": 5, "goals_conceded": 1, "xg_for": 3.6, "xg_against": 0.8, "corners_for": 8, "corners_against": 3, "shots_total": 20, "shots_on_target": 9, "yellow_cards": 1, "red_cards": 0, "fouls": 9,  "possession": 66},
                    {"goals_scored": 1, "goals_conceded": 0, "xg_for": 2.1, "xg_against": 0.5, "corners_for": 7, "corners_against": 2, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 8,  "possession": 68},
                    {"goals_scored": 4, "goals_conceded": 2, "xg_for": 2.9, "xg_against": 1.3, "corners_for": 7, "corners_against": 4, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 64},
                    {"goals_scored": 5, "goals_conceded": 0, "xg_for": 3.8, "xg_against": 0.4, "corners_for": 9, "corners_against": 2, "shots_total": 22, "shots_on_target": 11, "yellow_cards": 0, "red_cards": 0, "fouls": 7,  "possession": 71},
                ],
                "key_players": [
                    {"name": "Robert Lewandowski", "position": "Delantero Centro Killer", "avg_shots_p90": 3.9, "avg_sot_p90": 2.0, "shot_creation_actions": 3.2, "goal_prob": 0.72},
                    {"name": "Lamine Yamal", "position": "Extremo Generacional", "avg_shots_p90": 3.2, "avg_sot_p90": 1.5, "shot_creation_actions": 6.8, "goal_prob": 0.46},
                    {"name": "Raphinha", "position": "Extremo / Conductor", "avg_shots_p90": 3.5, "avg_sot_p90": 1.7, "shot_creation_actions": 5.9, "goal_prob": 0.50},
                    {"name": "Pedri", "position": "Mediocentro Creativo", "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 5.4, "goal_prob": 0.18}
                ]
            },
            "Getafe": {
                "fifa_rank": 58,
                "recent_form": ["L", "D", "L", "W", "D", "L"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.6, "xg_against": 1.8, "corners_for": 3, "corners_against": 6, "shots_total": 7,  "shots_on_target": 2, "yellow_cards": 4, "red_cards": 0, "fouls": 18, "possession": 36},
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 0.9, "xg_against": 1.4, "corners_for": 4, "corners_against": 5, "shots_total": 9,  "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 16, "possession": 38},
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.5, "xg_against": 0.8, "corners_for": 4, "corners_against": 4, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 42},
                ],
                "key_players": [
                    {"name": "Borja Mayoral", "position": "Delantero Centro", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 2.0, "goal_prob": 0.28},
                    {"name": "Luis Milla", "position": "Pivote Organizador", "avg_shots_p90": 1.1, "avg_sot_p90": 0.3, "shot_creation_actions": 3.5, "goal_prob": 0.08},
                    {"name": "Mauro Arambarri", "position": "Mediocentro Físico", "avg_shots_p90": 1.6, "avg_sot_p90": 0.6, "shot_creation_actions": 2.2, "goal_prob": 0.15}
                ]
            },
            "Arsenal": {
                "fifa_rank": 4,
                "recent_form": ["W", "W", "D", "W", "W", "D", "W"],
                "sequence": [
                    {"goals_scored": 4, "goals_conceded": 2, "xg_for": 2.9, "xg_against": 1.0, "corners_for": 8, "corners_against": 3, "shots_total": 19, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 9,  "possession": 64},
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.2, "xg_against": 0.6, "corners_for": 7, "corners_against": 2, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 8,  "possession": 67},
                    {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.8, "xg_against": 1.5, "corners_for": 6, "corners_against": 5, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 1, "fouls": 11, "possession": 52},
                    {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.6, "xg_against": 0.7, "corners_for": 8, "corners_against": 3, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 9,  "possession": 63},
                ],
                "key_players": [
                    {"name": "Bukayo Saka", "position": "Extremo Derecho Élite", "avg_shots_p90": 3.3, "avg_sot_p90": 1.6, "shot_creation_actions": 6.4, "goal_prob": 0.48},
                    {"name": "Kai Havertz", "position": "Delantero Boya", "avg_shots_p90": 3.0, "avg_sot_p90": 1.4, "shot_creation_actions": 4.1, "goal_prob": 0.45},
                    {"name": "Gabriel Martinelli", "position": "Extremo Eléctrico", "avg_shots_p90": 2.8, "avg_sot_p90": 1.2, "shot_creation_actions": 4.8, "goal_prob": 0.38},
                    {"name": "Declan Rice", "position": "Pivote / Balón Parado", "avg_shots_p90": 1.6, "avg_sot_p90": 0.6, "shot_creation_actions": 4.2, "goal_prob": 0.16}
                ]
            },
            "Leeds United": {
                "fifa_rank": 65,
                "recent_form": ["W", "D", "W", "L", "W", "D"],
                "sequence": [
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.7, "xg_against": 0.8, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 56},
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.3, "xg_against": 1.2, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 52},
                    {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.9, "xg_against": 1.4, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 48},
                ],
                "key_players": [
                    {"name": "Joël Piroe", "position": "Delantero Centro", "avg_shots_p90": 2.6, "avg_sot_p90": 1.2, "shot_creation_actions": 2.6, "goal_prob": 0.36},
                    {"name": "Wilfried Gnonto", "position": "Extremo Desequilibrio", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 4.2, "goal_prob": 0.28},
                    {"name": "Brenden Aaronson", "position": "Mediapunta Presión", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 3.8, "goal_prob": 0.20}
                ]
            },
            "FC Augsburg": {
                "fifa_rank": 72,
                "recent_form": ["L", "L", "W", "L", "D"],
                "sequence": [
                    {"goals_scored": 1, "goals_conceded": 3, "xg_for": 1.1, "xg_against": 2.4, "corners_for": 4, "corners_against": 7, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 42},
                    {"goals_scored": 2, "goals_conceded": 3, "xg_for": 1.5, "xg_against": 2.2, "corners_for": 5, "corners_against": 6, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 44},
                    {"goals_scored": 3, "goals_conceded": 1, "xg_for": 1.9, "xg_against": 1.2, "corners_for": 5, "corners_against": 5, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 47},
                ],
                "key_players": [
                    {"name": "Phillip Tietz", "position": "Delantero Referencia", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 2.2, "goal_prob": 0.30},
                    {"name": "Alexis Claude-Maurice", "position": "Mediapunta", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 3.6, "goal_prob": 0.24}
                ]
            },
            "Bayern Munich": {
                "fifa_rank": 1,
                "recent_form": ["W", "W", "W", "D", "W", "W"],
                "sequence": [
                    {"goals_scored": 5, "goals_conceded": 0, "xg_for": 3.7, "xg_against": 0.5, "corners_for": 9, "corners_against": 2, "shots_total": 23, "shots_on_target": 11, "yellow_cards": 1, "red_cards": 0, "fouls": 8,  "possession": 70},
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 2.2, "xg_against": 0.7, "corners_for": 8, "corners_against": 2, "shots_total": 18, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 9,  "possession": 69},
                    {"goals_scored": 9, "goals_conceded": 2, "xg_for": 5.4, "xg_against": 1.0, "corners_for": 11, "corners_against": 3, "shots_total": 29, "shots_on_target": 17, "yellow_cards": 1, "red_cards": 0, "fouls": 7,  "possession": 72},
                    {"goals_scored": 6, "goals_conceded": 1, "xg_for": 4.1, "xg_against": 0.6, "corners_for": 8, "corners_against": 3, "shots_total": 22, "shots_on_target": 12, "yellow_cards": 1, "red_cards": 0, "fouls": 8,  "possession": 68},
                ],
                "key_players": [
                    {"name": "Harry Kane", "position": "Delantero Centro Total", "avg_shots_p90": 4.2, "avg_sot_p90": 2.3, "shot_creation_actions": 4.8, "goal_prob": 0.75},
                    {"name": "Michael Olise", "position": "Extremo Generador", "avg_shots_p90": 3.1, "avg_sot_p90": 1.5, "shot_creation_actions": 6.2, "goal_prob": 0.44},
                    {"name": "Jamal Musiala", "position": "Mediapunta Desborde", "avg_shots_p90": 3.3, "avg_sot_p90": 1.6, "shot_creation_actions": 5.8, "goal_prob": 0.45},
                    {"name": "Serge Gnabry", "position": "Extremo Llegada", "avg_shots_p90": 2.6, "avg_sot_p90": 1.2, "shot_creation_actions": 3.9, "goal_prob": 0.38}
                ]
            },
            "Inter Milan": {
                "fifa_rank": 5,
                "recent_form": ["W", "W", "D", "W", "W", "L", "W"],
                "sequence": [
                    {"goals_scored": 3, "goals_conceded": 2, "xg_for": 2.5, "xg_against": 1.1, "corners_for": 7, "corners_against": 4, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 61},
                    {"goals_scored": 4, "goals_conceded": 0, "xg_for": 3.2, "xg_against": 0.6, "corners_for": 8, "corners_against": 2, "shots_total": 19, "shots_on_target": 9, "yellow_cards": 1, "red_cards": 0, "fouls": 9,  "possession": 64},
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 1.7, "xg_against": 0.8, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 59},
                    {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.1, "xg_against": 0.9, "corners_for": 7, "corners_against": 3, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 62},
                ],
                "key_players": [
                    {"name": "Lautaro Martínez", "position": "Delantero Capitán", "avg_shots_p90": 3.8, "avg_sot_p90": 1.9, "shot_creation_actions": 3.6, "goal_prob": 0.65},
                    {"name": "Marcus Thuram", "position": "Delantero Potencia", "avg_shots_p90": 3.2, "avg_sot_p90": 1.5, "shot_creation_actions": 4.1, "goal_prob": 0.48},
                    {"name": "Hakan Çalhanoğlu", "position": "Pivote / Francotirador", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 5.4, "goal_prob": 0.28},
                    {"name": "Nicolò Barella", "position": "Interior Box-to-Box", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 4.8, "goal_prob": 0.20}
                ]
            },
            "Parma": {
                "fifa_rank": 85,
                "recent_form": ["L", "D", "L", "W", "D"],
                "sequence": [
                    {"goals_scored": 2, "goals_conceded": 3, "xg_for": 1.4, "xg_against": 2.1, "corners_for": 4, "corners_against": 6, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 46},
                    {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.6, "xg_against": 1.9, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 48},
                    {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.8, "xg_against": 1.5, "corners_for": 5, "corners_against": 6, "shots_total": 13, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 45},
                ],
                "key_players": [
                    {"name": "Ange-Yoan Bonny", "position": "Delantero Dinámico", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 3.0, "goal_prob": 0.32},
                    {"name": "Dennis Man", "position": "Extremo Zurdo", "avg_shots_p90": 2.5, "avg_sot_p90": 1.2, "shot_creation_actions": 4.5, "goal_prob": 0.34},
                    {"name": "Valentin Mihăilă", "position": "Extremo Diestro", "avg_shots_p90": 2.1, "avg_sot_p90": 0.8, "shot_creation_actions": 3.4, "goal_prob": 0.22}
                ]
            },
            "Borussia Dortmund": {
                "fifa_rank": 9,
                "recent_form": ["W", "W", "L", "W", "W", "D"],
                "sequence": [
                    {"goals_scored": 4, "goals_conceded": 2, "xg_for": 2.8, "xg_against": 1.2, "corners_for": 7, "corners_against": 4, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 9,  "possession": 62},
                    {"goals_scored": 7, "goals_conceded": 1, "xg_for": 4.6, "xg_against": 0.7, "corners_for": 9, "corners_against": 2, "shots_total": 24, "shots_on_target": 12, "yellow_cards": 1, "red_cards": 0, "fouls": 8,  "possession": 67},
                    {"goals_scored": 1, "goals_conceded": 5, "xg_for": 1.1, "xg_against": 3.2, "corners_for": 4, "corners_against": 6, "shots_total": 9,  "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 51},
                    {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.4, "xg_against": 0.6, "corners_for": 6, "corners_against": 3, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 60},
                ],
                "key_players": [
                    {"name": "Serhou Guirassy", "position": "Delantero Centro Killer", "avg_shots_p90": 3.7, "avg_sot_p90": 1.9, "shot_creation_actions": 3.2, "goal_prob": 0.66},
                    {"name": "Julian Brandt", "position": "Mediapunta Creador", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 6.1, "goal_prob": 0.28},
                    {"name": "Jamie Bynoe-Gittens", "position": "Extremo Desborde", "avg_shots_p90": 2.9, "avg_sot_p90": 1.4, "shot_creation_actions": 4.6, "goal_prob": 0.36},
                    {"name": "Karim Adeyemi", "position": "Extremo Supersónico", "avg_shots_p90": 3.1, "avg_sot_p90": 1.5, "shot_creation_actions": 4.2, "goal_prob": 0.44}
                ]
            },
            "Werder Bremen": {
                "fifa_rank": 60,
                "recent_form": ["W", "L", "W", "D", "D"],
                "sequence": [
                    {"goals_scored": 4, "goals_conceded": 3, "xg_for": 2.1, "xg_against": 2.0, "corners_for": 5, "corners_against": 6, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 49},
                    {"goals_scored": 0, "goals_conceded": 5, "xg_for": 0.3, "xg_against": 3.6, "corners_for": 2, "corners_against": 8, "shots_total": 5,  "shots_on_target": 1, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 34},
                    {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.7, "xg_against": 1.2, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 51},
                ],
                "key_players": [
                    {"name": "Marvin Ducksch", "position": "Delantero / Balón Parado", "avg_shots_p90": 2.8, "avg_sot_p90": 1.2, "shot_creation_actions": 4.6, "goal_prob": 0.38},
                    {"name": "Jens Stage", "position": "Mediocentro Llegada", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 2.8, "goal_prob": 0.26},
                    {"name": "Mitchell Weiser", "position": "Carrilero Ofensivo", "avg_shots_p90": 1.5, "avg_sot_p90": 0.6, "shot_creation_actions": 4.8, "goal_prob": 0.16}
                ]
            },

            # --- VIERNES ESTELAR: DORTMUND VS ST. PAULI ---
            "St. Pauli": {
                "fifa_rank": 82,
                "recent_form": ["L", "L", "W", "D", "L"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 3, "xg_for": 0.6, "xg_against": 2.4, "corners_for": 3, "corners_against": 7, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 41},
                    {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.2, "xg_against": 0.8, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 12, "possession": 52},
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.9, "xg_against": 1.1, "corners_for": 4, "corners_against": 5, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 44},
                ],
                "key_players": [
                    {"name": "Johannes Eggestein", "position": "Delantero Móvil", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 2.8, "goal_prob": 0.28},
                    {"name": "Morgan Guilavogui", "position": "Extremo Potente", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 3.4, "goal_prob": 0.30},
                    {"name": "Jackson Irvine", "position": "Capitán / Box-to-Box", "avg_shots_p90": 1.6, "avg_sot_p90": 0.6, "shot_creation_actions": 3.8, "goal_prob": 0.20}
                ]
            },

            # --- VIERNES ESTELAR: NAPOLI VS COMO ---
            "Napoli": {
                "fifa_rank": 14,
                "recent_form": ["W", "W", "D", "W", "W", "W"],
                "sequence": [
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.5, "xg_against": 0.5, "corners_for": 7, "corners_against": 3, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 63},
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 1.4, "xg_against": 0.9, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 56},
                    {"goals_scored": 4, "goals_conceded": 0, "xg_for": 3.1, "xg_against": 0.4, "corners_for": 8, "corners_against": 2, "shots_total": 19, "shots_on_target": 9, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 65},
                    {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.2, "xg_against": 0.8, "corners_for": 6, "corners_against": 3, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 60}
                ],
                "key_players": [
                    {"name": "Khvicha Kvaratskhelia", "position": "Extremo Gambeteador", "avg_shots_p90": 3.6, "avg_sot_p90": 1.7, "shot_creation_actions": 6.5, "goal_prob": 0.55},
                    {"name": "Romelu Lukaku", "position": "Boya / Ariete Físico", "avg_shots_p90": 3.2, "avg_sot_p90": 1.8, "shot_creation_actions": 3.4, "goal_prob": 0.62},
                    {"name": "Matteo Politano", "position": "Extremo Diestro Incisivo", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 4.8, "goal_prob": 0.28},
                    {"name": "Scott McTominay", "position": "Volante Llegador", "avg_shots_p90": 2.3, "avg_sot_p90": 1.1, "shot_creation_actions": 3.1, "goal_prob": 0.34}
                ]
            },
            "Como": {
                "fifa_rank": 88,
                "recent_form": ["W", "W", "D", "L", "D"],
                "sequence": [
                    {"goals_scored": 3, "goals_conceded": 2, "xg_for": 1.9, "xg_against": 1.7, "corners_for": 5, "corners_against": 5, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 53},
                    {"goals_scored": 3, "goals_conceded": 2, "xg_for": 2.1, "xg_against": 1.6, "corners_for": 5, "corners_against": 6, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 52},
                    {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.5, "xg_against": 1.8, "corners_for": 4, "corners_against": 6, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 48}
                ],
                "key_players": [
                    {"name": "Patrick Cutrone", "position": "Delantero Rematador", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 2.7, "goal_prob": 0.40},
                    {"name": "Gabriel Strefezza", "position": "Extremo / Creador", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 4.6, "goal_prob": 0.26},
                    {"name": "Nico Paz", "position": "Joya Mediapunta", "avg_shots_p90": 2.6, "avg_sot_p90": 1.2, "shot_creation_actions": 5.2, "goal_prob": 0.32}
                ]
            },

            # --- VIERNES ESTELAR: MARSEILLE VS ANGERS ---
            "Marseille": {
                "fifa_rank": 26,
                "recent_form": ["L", "W", "W", "W", "D", "W"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 1, "xg_for": 1.2, "xg_against": 1.3, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 65},
                    {"goals_scored": 3, "goals_conceded": 2, "xg_for": 2.4, "xg_against": 1.5, "corners_for": 5, "corners_against": 6, "shots_total": 15, "shots_on_target": 7, "yellow_cards": 3, "red_cards": 1, "fouls": 14, "possession": 58},
                    {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.7, "xg_against": 0.9, "corners_for": 7, "corners_against": 3, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 62}
                ],
                "key_players": [
                    {"name": "Mason Greenwood", "position": "Extremo Goleador", "avg_shots_p90": 3.8, "avg_sot_p90": 1.9, "shot_creation_actions": 4.9, "goal_prob": 0.60},
                    {"name": "Elye Wahi", "position": "Delantero Centro Rápido", "avg_shots_p90": 2.7, "avg_sot_p90": 1.3, "shot_creation_actions": 2.6, "goal_prob": 0.42},
                    {"name": "Amine Harit", "position": "Organizador Creativo", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 5.8, "goal_prob": 0.24},
                    {"name": "Luis Henrique", "position": "Extremo Desborde", "avg_shots_p90": 2.2, "avg_sot_p90": 1.1, "shot_creation_actions": 4.4, "goal_prob": 0.32}
                ]
            },
            "Angers": {
                "fifa_rank": 95,
                "recent_form": ["L", "D", "D", "D", "L"],
                "sequence": [
                    {"goals_scored": 1, "goals_conceded": 3, "xg_for": 0.9, "xg_against": 2.5, "corners_for": 4, "corners_against": 7, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 42},
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.1, "xg_against": 1.3, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 46},
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.0, "xg_against": 1.4, "corners_for": 3, "corners_against": 6, "shots_total": 8, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 44}
                ],
                "key_players": [
                    {"name": "Himad Abdelli", "position": "Enganche / Creativo", "avg_shots_p90": 2.1, "avg_sot_p90": 0.8, "shot_creation_actions": 4.2, "goal_prob": 0.25},
                    {"name": "Farid El Melali", "position": "Extremo Rápido", "avg_shots_p90": 2.0, "avg_sot_p90": 0.7, "shot_creation_actions": 3.1, "goal_prob": 0.22},
                    {"name": "Lois Diony", "position": "Delantero Centro", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 2.0, "goal_prob": 0.24}
                ]
            },

            # --- VIERNES ESTELAR: LEGANÉS VS VALENCIA ---
            "Leganés": {
                "fifa_rank": 78,
                "recent_form": ["D", "L", "L", "L", "D"],
                "sequence": [
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 0.8, "xg_against": 1.2, "corners_for": 4, "corners_against": 5, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 44},
                    {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.6, "xg_against": 1.8, "corners_for": 3, "corners_against": 6, "shots_total": 7, "shots_on_target": 2, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 41},
                    {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.7, "xg_against": 1.4, "corners_for": 4, "corners_against": 5, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 4, "red_cards": 0, "fouls": 16, "possession": 43}
                ],
                "key_players": [
                    {"name": "Juan Cruz", "position": "Extremo Desequilibrante", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 3.8, "goal_prob": 0.30},
                    {"name": "Dani Raba", "position": "Mediapunta Zurdo", "avg_shots_p90": 2.1, "avg_sot_p90": 0.8, "shot_creation_actions": 3.5, "goal_prob": 0.24},
                    {"name": "Miguel de la Fuente", "position": "Delantero de Choque", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 2.2, "goal_prob": 0.28}
                ]
            },
            "Valencia": {
                "fifa_rank": 38,
                "recent_form": ["L", "D", "W", "L", "D"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 3, "xg_for": 0.7, "xg_against": 2.2, "corners_for": 3, "corners_against": 7, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 42},
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 1.1, "xg_against": 1.0, "corners_for": 5, "corners_against": 4, "shots_total": 11, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 50},
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.8, "xg_against": 0.7, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 53}
                ],
                "key_players": [
                    {"name": "Hugo Duro", "position": "Ariete Luchador", "avg_shots_p90": 2.5, "avg_sot_p90": 1.2, "shot_creation_actions": 2.4, "goal_prob": 0.38},
                    {"name": "Diego López", "position": "Extremo / Segundo Punta", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 3.9, "goal_prob": 0.28},
                    {"name": "Pepelu", "position": "Metrónomo & Balón Parado", "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 4.5, "goal_prob": 0.18},
                    {"name": "Javi Guerra", "position": "Interior Box-to-Box", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 3.4, "goal_prob": 0.22}
                ]
            },

            # --- VIERNES ESTELAR: SUNDERLAND VS LEEDS UNITED ---
            "Sunderland": {
                "fifa_rank": 65,
                "recent_form": ["W", "W", "L", "W", "W"],
                "sequence": [
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.9, "xg_against": 0.8, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 54},
                    {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.3, "xg_against": 1.7, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 49},
                    {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.5, "xg_against": 0.6, "corners_for": 7, "corners_against": 3, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 56}
                ],
                "key_players": [
                    {"name": "Jobe Bellingham", "position": "Volante Llegador", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 3.8, "goal_prob": 0.32},
                    {"name": "Wilson Isidor", "position": "Delantero Rápido", "avg_shots_p90": 2.6, "avg_sot_p90": 1.3, "shot_creation_actions": 2.5, "goal_prob": 0.40},
                    {"name": "Romaine Mundle", "position": "Extremo Eléctrico", "avg_shots_p90": 2.7, "avg_sot_p90": 1.2, "shot_creation_actions": 4.6, "goal_prob": 0.36},
                    {"name": "Chris Rigg", "position": "Talento Creativo", "avg_shots_p90": 1.7, "avg_sot_p90": 0.7, "shot_creation_actions": 4.1, "goal_prob": 0.22}
                ]
            },

            # --- VIERNES ESTELAR: RIO AVE VS FAMALICÃO ---
            "Rio Ave": {
                "fifa_rank": 79,
                "recent_form": ["L", "D", "W", "L", "W"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 4, "xg_for": 0.5, "xg_against": 2.8, "corners_for": 3, "corners_against": 7, "shots_total": 7, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 16, "possession": 38},
                    {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.6, "xg_against": 1.5, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 51},
                    {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.4, "xg_against": 0.9, "corners_for": 6, "corners_against": 4, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 53}
                ],
                "key_players": [
                    {"name": "Clayton", "position": "Delantero Centro", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 2.6, "goal_prob": 0.36},
                    {"name": "Kiko Bondoso", "position": "Extremo Rápido", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 3.7, "goal_prob": 0.26},
                    {"name": "Tiago Morais", "position": "Extremo Incisivo", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 3.4, "goal_prob": 0.28}
                ]
            },
            "Famalicão": {
                "fifa_rank": 74,
                "recent_form": ["D", "D", "L", "W", "W"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.9, "xg_against": 0.8, "corners_for": 4, "corners_against": 4, "shots_total": 9, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 49},
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 1.0, "xg_against": 1.1, "corners_for": 5, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 4, "red_cards": 0, "fouls": 17, "possession": 48},
                    {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.2, "xg_against": 1.6, "corners_for": 4, "corners_against": 6, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 47}
                ],
                "key_players": [
                    {"name": "Mario González", "position": "Ariete Español", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 2.2, "goal_prob": 0.35},
                    {"name": "Zaydou Youssouf", "position": "Pivote Físico", "avg_shots_p90": 1.5, "avg_sot_p90": 0.5, "shot_creation_actions": 3.2, "goal_prob": 0.16},
                    {"name": "Gil Dias", "position": "Extremo Zurdo", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 3.6, "goal_prob": 0.24}
                ]
            }
        }
        return histories.get(team_name, {})

    def get_match_context(self, home_team: str, away_team: str) -> Dict[str, Any]:
        """
        Retorna contexto de arbitraje, estadio y estimación de espectadores para los 6 partidos.
        """
        # 1. Comprobar base de datos externa JSON si existe
        ext_matches_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "matches_database.json")
        if os.path.exists(ext_matches_file):
            try:
                with open(ext_matches_file, "r", encoding="utf-8") as f:
                    ext_matches = json.load(f)
                    for k, v in ext_matches.items():
                        if f"{home_team} vs {away_team}" in k or (home_team in k and away_team in k):
                            return v
            except Exception:
                pass

        matches = {
            ("Alemania", "Serbia"): {
                "tournament": "UEFA Nations League - Liga A",
                "stadium": "Signal Iduna Park (Dortmund)",
                "spectators_est": "75,000 en estadio (~22M audiencia global)",
                "referee": "Clément Turpin",
                "referee_avg_yellows": 3.8,
                "referee_avg_reds": 0.16,
                "intensity": "Muy Alta (Alemania busca afianzar liderato de grupo ante la potencia física serbia)"
            },
            ("Dinamarca", "Portugal"): {
                "tournament": "UEFA Nations League - Liga A",
                "stadium": "Parken Stadium (Copenhague)",
                "spectators_est": "38,000 en estadio (~28M audiencia global)",
                "referee": "Szymon Marciniak",
                "referee_avg_yellows": 4.2,
                "referee_avg_reds": 0.18,
                "intensity": "Máxima (Duelo de titanes por el liderato; Portugal con Cristiano Ronaldo y Bruno Fernandes)"
            },
            ("Grecia", "Países Bajos"): {
                "tournament": "UEFA Nations League - Liga A",
                "stadium": "OPAP Arena (Atenas)",
                "spectators_est": "32,500 en estadio (~16M audiencia global)",
                "referee": "Anthony Taylor",
                "referee_avg_yellows": 4.5,
                "referee_avg_reds": 0.20,
                "intensity": "Alta (Ambiente hostil en Atenas frente al juego de posesión y velocidad neerlandés)"
            },
            ("Gales", "Noruega"): {
                "tournament": "UEFA Nations League - Liga B",
                "stadium": "Cardiff City Stadium (Cardiff)",
                "spectators_est": "33,280 en estadio (~19M audiencia global)",
                "referee": "István Kovács",
                "referee_avg_yellows": 4.6,
                "referee_avg_reds": 0.22,
                "intensity": "Alta (Noruega comandada por Erling Haaland buscando el ascenso frente al muro galés)"
            },
            ("Irlanda", "Austria"): {
                "tournament": "UEFA Nations League - Liga B",
                "stadium": "Aviva Stadium (Dublín)",
                "spectators_est": "51,700 en estadio (~12M audiencia global)",
                "referee": "Slavko Vinčić",
                "referee_avg_yellows": 4.1,
                "referee_avg_reds": 0.15,
                "intensity": "Media-Alta (Presión asfixiante de Rangnick con Austria ante la combatividad irlandesa)"
            },
            ("Japón", "Ecuador"): {
                "tournament": "Copa Kirin / Amistoso Internacional Élite",
                "stadium": "Estadio Nacional (Tokio)",
                "spectators_est": "65,000 en estadio (~15M audiencia global en Asia y América)",
                "referee": "Kim Jong-hyeok",
                "referee_avg_yellows": 3.4,
                "referee_avg_reds": 0.12,
                "intensity": "Alta (Juego técnico y vertiginoso de Japón ante la potencia física y transiciones de Ecuador)"
            },

            # --- JORNADA DE MAÑANA (TOP 6 ESTELARES CLUB FOOTBALL) ---
            ("Real Madrid", "Villarreal"): {
                "tournament": "LaLiga EA Sports - Jornada 9 (Estelar)",
                "stadium": "Santiago Bernabéu (Madrid)",
                "spectators_est": "81,044 en estadio (~45M audiencia global)",
                "referee": "Guillermo Cuadra Fernández",
                "referee_avg_yellows": 4.4,
                "referee_avg_reds": 0.18,
                "intensity": "Máxima (Real Madrid en el Bernabéu buscando el liderato frente a un Villarreal muy goleador)"
            },
            ("Barcelona", "Getafe"): {
                "tournament": "LaLiga EA Sports - Jornada 9",
                "stadium": "Estadi Olímpic Lluís Companys (Montjuïc)",
                "spectators_est": "49,500 en estadio (~38M audiencia global)",
                "referee": "Pablo González Fuertes",
                "referee_avg_yellows": 4.8,
                "referee_avg_reds": 0.22,
                "intensity": "Alta (Duelo de estilos: La máquina ofensiva de Hansi Flick ante el cerrojo ultra-físico de Bordalás)"
            },
            ("Arsenal", "Leeds United"): {
                "tournament": "Premier League - Matchday 8",
                "stadium": "Emirates Stadium (Londres)",
                "spectators_est": "60,260 en estadio (~42M audiencia global)",
                "referee": "Michael Oliver",
                "referee_avg_yellows": 3.6,
                "referee_avg_reds": 0.14,
                "intensity": "Muy Alta (Arsenal de Arteta buscando imponer su jerarquía con Saka y Havertz)"
            },
            ("FC Augsburg", "Bayern Munich"): {
                "tournament": "Bundesliga - Jornada 6 (Derbi de Baviera)",
                "stadium": "WWK Arena (Augsburg)",
                "spectators_est": "30,660 en estadio (~28M audiencia global)",
                "referee": "Felix Zwayer",
                "referee_avg_yellows": 3.9,
                "referee_avg_reds": 0.15,
                "intensity": "Máxima (Derbi bávaro caliente; Bayern de Kompany con Kane y Olise promediando 4 goles)"
            },
            ("Inter Milan", "Parma"): {
                "tournament": "Serie A - Giornata 7",
                "stadium": "Stadio Giuseppe Meazza - San Siro (Milán)",
                "spectators_est": "72,500 en estadio (~25M audiencia global)",
                "referee": "Daniele Doveri",
                "referee_avg_yellows": 4.1,
                "referee_avg_reds": 0.16,
                "intensity": "Alta (El campeón de Italia ante el descaro y verticalidad al contragolpe del Parma de Man y Bonny)"
            },
            ("Borussia Dortmund", "Werder Bremen"): {
                "tournament": "Bundesliga - Jornada 6",
                "stadium": "Signal Iduna Park (Dortmund)",
                "spectators_est": "81,365 en estadio (~30M audiencia global)",
                "referee": "Daniel Siebert",
                "referee_avg_yellows": 4.0,
                "referee_avg_reds": 0.18,
                "intensity": "Muy Alta (El Muro Amarillo empujando a Guirassy y Brandt en un duelo históricamente vibrante)"
            },
            ("Borussia Dortmund", "St. Pauli"): {
                "tournament": "Bundesliga - Jornada 7 (Viernes Noche)",
                "stadium": "Signal Iduna Park (Dortmund)",
                "spectators_est": "81,365 en estadio (~32M audiencia global)",
                "referee": "Sascha Stegemann",
                "referee_avg_yellows": 4.1,
                "referee_avg_reds": 0.16,
                "intensity": "Máxima (Signal Iduna Park encendido; Dortmund de Sahin con Guirassy buscando el asalto al liderato)"
            },
            ("Napoli", "Como"): {
                "tournament": "Serie A - Giornata 7 (Estelar de Viernes)",
                "stadium": "Stadio Diego Armando Maradona (Nápoles)",
                "spectators_est": "50,500 en estadio (~28M audiencia global)",
                "referee": "Ermanno Feliciani",
                "referee_avg_yellows": 4.2,
                "referee_avg_reds": 0.15,
                "intensity": "Muy Alta (Napoli de Antonio Conte liderando la Serie A con Kvaratskhelia, Lukaku y McTominay)"
            },
            ("Marseille", "Angers"): {
                "tournament": "Ligue 1 McDonald's - Jornada 7 (Viernes)",
                "stadium": "Orange Vélodrome (Marsella)",
                "spectators_est": "64,000 en estadio (~22M audiencia global)",
                "referee": "Romain Lissorgue",
                "referee_avg_yellows": 3.9,
                "referee_avg_reds": 0.20,
                "intensity": "Alta (El Vélodrome rugiendo con De Zerbi y Greenwood en busca de puntos clave de Champions)"
            },
            ("Leganés", "Valencia"): {
                "tournament": "LaLiga EA Sports - Jornada 9 (Viernes)",
                "stadium": "Estadio Municipal Butarque (Leganés, Madrid)",
                "spectators_est": "12,450 en estadio (~18M audiencia global)",
                "referee": "Jorge Figueroa Vázquez",
                "referee_avg_yellows": 4.7,
                "referee_avg_reds": 0.24,
                "intensity": "Tensión Extrema (Duelo directo por la permanencia con defensas cerradas y alto roce físico)"
            },
            ("Sunderland", "Leeds United"): {
                "tournament": "EFL Championship - Matchday 9 (Viernes Estelar)",
                "stadium": "Stadium of Light (Sunderland)",
                "spectators_est": "41,500 en estadio (~14M audiencia global)",
                "referee": "Tim Robinson",
                "referee_avg_yellows": 3.8,
                "referee_avg_reds": 0.12,
                "intensity": "Máxima (Batalla por el ascenso directo a Premier League en un Stadium of Light a reventar)"
            },
            ("Rio Ave", "Famalicão"): {
                "tournament": "Liga Portugal Betclic - Jornada 8 (Viernes)",
                "stadium": "Estádio dos Arcos (Vila do Conde)",
                "spectators_est": "5,300 en estadio (~4M audiencia global)",
                "referee": "Gustavo Correia",
                "referee_avg_yellows": 5.4,
                "referee_avg_reds": 0.28,
                "intensity": "Alta (Duelo táctico portugués con alta fricción y arbitraje severo)"
            }
        }
        return matches.get((home_team, away_team), {
            "tournament": "Competición Internacional FIFA",
            "stadium": "Estadio Principal",
            "spectators_est": "45,000 espectadores",
            "referee": "Árbitro FIFA Internacional",
            "referee_avg_yellows": 4.0,
            "referee_avg_reds": 0.18,
            "intensity": "Alta"
        })
