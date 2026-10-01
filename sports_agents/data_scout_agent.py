"""
DataScoutAgent:
Agente responsable de la ingesta y estructuración de datos deportivos históricos,
series temporales de partidos recientes, métricas de rendimiento y perfiles de jugadores.
Soporta los 6 partidos estelares de máxima audiencia internacional para la jornada de mañana.
"""

from typing import Dict, List, Any


class DataScoutAgent:
    def __init__(self):
        self.name = "DataScoutAgent"

    def get_team_history(self, team_name: str) -> Dict[str, Any]:
        """
        Retorna las secuencias cronológicas recientes para el equipo especificado.
        """
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
            }
        }
        return histories.get(team_name, {})

    def get_match_context(self, home_team: str, away_team: str) -> Dict[str, Any]:
        """
        Retorna contexto de arbitraje, estadio y estimación de espectadores para los 6 partidos.
        """
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
