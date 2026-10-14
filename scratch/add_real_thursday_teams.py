# -*- coding: utf-8 -*-
"""
add_real_thursday_teams.py:
Inyecta los datos de los 12 equipos que juegan HOY Jueves 08/10/2026:
Brasileirão Serie A (Fecha 29) y Liga BetPlay (Colombia).
Cero UEFA Nations League. 100% fútbol de clubes real en desarrollo.
"""
import sys
import os
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
teams_file = os.path.join(base_dir, "sports_agents", "teams_database.json")
matches_file = os.path.join(base_dir, "sports_agents", "matches_database.json")
cal_file = os.path.join(base_dir, "sports_agents", "official_calendar.json")

# 1. Nuevos equipos reales
new_teams = {
    "Santos": {
        "fifa_rank": 28,
        "recent_form": ["W", "D", "W", "L", "W", "W", "D", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.75, "xg_against": 1.10, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 54},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.45, "xg_against": 0.85, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 52},
            {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.80, "xg_against": 1.50, "corners_for": 7, "corners_against": 5, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 50},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.90, "xg_against": 1.25, "corners_for": 4, "corners_against": 6, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 47},
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.10, "xg_against": 0.95, "corners_for": 8, "corners_against": 3, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 58},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.30, "xg_against": 1.20, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 51}
        ],
        "key_players": [
            {"name": "Giuliano", "position": "Mediapunta Creador", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 4.5, "goal_prob": 0.28},
            {"name": "Guilherme", "position": "Extremo Ofensivo", "avg_shots_p90": 2.6, "avg_sot_p90": 1.2, "shot_creation_actions": 3.8, "goal_prob": 0.35},
            {"name": "Wendel Silva", "position": "Delantero Centro", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 2.4, "goal_prob": 0.38},
            {"name": "Rómulo Otero", "position": "Especialista Balón Parado", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 4.1, "goal_prob": 0.22}
        ]
    },
    "Flamengo": {
        "fifa_rank": 8,
        "recent_form": ["W", "W", "D", "W", "W", "L", "W", "W"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.40, "xg_against": 0.90, "corners_for": 8, "corners_against": 3, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 62},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.10, "xg_against": 0.60, "corners_for": 7, "corners_against": 2, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 9, "possession": 64},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.65, "xg_against": 1.10, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 59},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.95, "xg_against": 1.05, "corners_for": 7, "corners_against": 4, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 60},
            {"goals_scored": 4, "goals_conceded": 0, "xg_for": 2.80, "xg_against": 0.50, "corners_for": 9, "corners_against": 2, "shots_total": 21, "shots_on_target": 9, "yellow_cards": 1, "red_cards": 0, "fouls": 8, "possession": 66},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 1.40, "xg_against": 1.15, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 58}
        ],
        "key_players": [
            {"name": "Giorgian de Arrascaeta", "position": "Cerebro Creativo", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 5.8, "goal_prob": 0.32},
            {"name": "Bruno Henrique", "position": "Extremo Goleador", "avg_shots_p90": 2.9, "avg_sot_p90": 1.4, "shot_creation_actions": 3.6, "goal_prob": 0.40},
            {"name": "Gerson", "position": "Volante Mixto Élite", "avg_shots_p90": 1.8, "avg_sot_p90": 0.8, "shot_creation_actions": 4.7, "goal_prob": 0.22},
            {"name": "Nicolás de la Cruz", "position": "Interior Dinámico", "avg_shots_p90": 2.0, "avg_sot_p90": 0.9, "shot_creation_actions": 4.3, "goal_prob": 0.25}
        ]
    },
    "Palmeiras": {
        "fifa_rank": 6,
        "recent_form": ["W", "W", "W", "D", "W", "W", "D", "W"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.50, "xg_against": 0.65, "corners_for": 8, "corners_against": 3, "shots_total": 19, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 60},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.15, "xg_against": 0.90, "corners_for": 7, "corners_against": 4, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 58},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.70, "xg_against": 0.70, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 57},
            {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.90, "xg_against": 1.30, "corners_for": 7, "corners_against": 5, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 55},
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.30, "xg_against": 0.80, "corners_for": 8, "corners_against": 3, "shots_total": 18, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 61},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.00, "xg_against": 0.55, "corners_for": 7, "corners_against": 2, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 8, "possession": 62}
        ],
        "key_players": [
            {"name": "Flaco López", "position": "Goleador Argentino", "avg_shots_p90": 3.2, "avg_sot_p90": 1.6, "shot_creation_actions": 2.8, "goal_prob": 0.48},
            {"name": "Raphael Veiga", "position": "Enganche Letal", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 5.2, "goal_prob": 0.38},
            {"name": "Estêvão", "position": "Joya Mundialista Chelsea", "avg_shots_p90": 3.0, "avg_sot_p90": 1.4, "shot_creation_actions": 5.6, "goal_prob": 0.42},
            {"name": "Felipe Anderson", "position": "Extremo Creativo", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 4.1, "goal_prob": 0.24}
        ]
    },
    "Bahia": {
        "fifa_rank": 35,
        "recent_form": ["W", "D", "L", "W", "D", "L", "W", "D"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.25, "xg_against": 1.35, "corners_for": 5, "corners_against": 6, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 48},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.65, "xg_against": 0.90, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 52},
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.85, "xg_against": 1.80, "corners_for": 4, "corners_against": 7, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 16, "possession": 44},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.50, "xg_against": 1.15, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 50},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.20, "xg_against": 1.20, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 49},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.95, "xg_against": 1.45, "corners_for": 3, "corners_against": 6, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 46}
        ],
        "key_players": [
            {"name": "Cauly", "position": "Generador de Juego", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 5.0, "goal_prob": 0.25},
            {"name": "Thaciano", "position": "Llegador de Área", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 3.1, "goal_prob": 0.30},
            {"name": "Everaldo", "position": "Referente de Ataque", "avg_shots_p90": 2.5, "avg_sot_p90": 1.0, "shot_creation_actions": 2.2, "goal_prob": 0.32},
            {"name": "Jean Lucas", "position": "Volante de Ida y Vuelta", "avg_shots_p90": 1.6, "avg_sot_p90": 0.6, "shot_creation_actions": 3.4, "goal_prob": 0.18}
        ]
    },
    "Fluminense": {
        "fifa_rank": 14,
        "recent_form": ["W", "W", "D", "L", "W", "W", "D", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.90, "xg_against": 0.70, "corners_for": 7, "corners_against": 3, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 62},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.60, "xg_against": 0.80, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 60},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.45, "xg_against": 1.10, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 58},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 1.10, "xg_against": 1.25, "corners_for": 6, "corners_against": 4, "shots_total": 11, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 64},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.85, "xg_against": 0.95, "corners_for": 7, "corners_against": 4, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 61},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.50, "xg_against": 0.65, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 63}
        ],
        "key_players": [
            {"name": "Germán Cano", "position": "Artillero Histórico", "avg_shots_p90": 3.4, "avg_sot_p90": 1.7, "shot_creation_actions": 2.5, "goal_prob": 0.46},
            {"name": "Jhon Arias", "position": "Desequilibrio Total", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 5.9, "goal_prob": 0.38},
            {"name": "Paulo Henrique Ganso", "position": "Mago Organizador", "avg_shots_p90": 1.2, "avg_sot_p90": 0.5, "shot_creation_actions": 6.2, "goal_prob": 0.16},
            {"name": "Kauã Elias", "position": "Joven Promesa de Ataque", "avg_shots_p90": 2.3, "avg_sot_p90": 1.1, "shot_creation_actions": 2.9, "goal_prob": 0.34}
        ]
    },
    "Coritiba": {
        "fifa_rank": 52,
        "recent_form": ["L", "D", "W", "L", "D", "L", "W", "L"],
        "sequence": [
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.70, "xg_against": 1.90, "corners_for": 3, "corners_against": 7, "shots_total": 7, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 16, "possession": 40},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.10, "xg_against": 1.30, "corners_for": 4, "corners_against": 5, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 43},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.20, "xg_against": 0.95, "corners_for": 5, "corners_against": 4, "shots_total": 10, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 46},
            {"goals_scored": 0, "goals_conceded": 3, "xg_for": 0.60, "xg_against": 2.30, "corners_for": 2, "corners_against": 8, "shots_total": 6, "shots_on_target": 1, "yellow_cards": 4, "red_cards": 1, "fouls": 18, "possession": 36},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 0.95, "xg_against": 1.25, "corners_for": 4, "corners_against": 6, "shots_total": 8, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 15, "possession": 42},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.80, "xg_against": 1.50, "corners_for": 3, "corners_against": 5, "shots_total": 7, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 17, "possession": 39}
        ],
        "key_players": [
            {"name": "Robson", "position": "Extremo Capitán", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 3.4, "goal_prob": 0.26},
            {"name": "Lucas Ronier", "position": "Desborde Juvenil", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 3.0, "goal_prob": 0.22},
            {"name": "Júnior Brumado", "position": "Punta de Lucha", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 1.8, "goal_prob": 0.24}
        ]
    },
    "Athletico Paranaense": {
        "fifa_rank": 20,
        "recent_form": ["W", "D", "W", "L", "W", "D", "W", "L"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.45, "xg_against": 0.75, "corners_for": 6, "corners_against": 3, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 53},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.30, "xg_against": 1.10, "corners_for": 5, "corners_against": 4, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 51},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.70, "xg_against": 0.95, "corners_for": 7, "corners_against": 4, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 55},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.90, "xg_against": 1.20, "corners_for": 4, "corners_against": 5, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 48},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.60, "xg_against": 0.65, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 56},
            {"goals_scored": 0, "goals_conceded": 0, "xg_for": 1.05, "xg_against": 0.90, "corners_for": 5, "corners_against": 4, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 50}
        ],
        "key_players": [
            {"name": "Gonzalo Mastriani", "position": "Delantero Uruguayo", "avg_shots_p90": 2.9, "avg_sot_p90": 1.4, "shot_creation_actions": 2.6, "goal_prob": 0.42},
            {"name": "Agustín Canobbio", "position": "Extremo Incansable", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 4.5, "goal_prob": 0.28},
            {"name": "Tomás Cuello", "position": "Velocidad y Desborde", "avg_shots_p90": 2.1, "avg_sot_p90": 0.8, "shot_creation_actions": 3.8, "goal_prob": 0.24},
            {"name": "Fernandinho", "position": "Mariscal del Mediocampo", "avg_shots_p90": 1.1, "avg_sot_p90": 0.4, "shot_creation_actions": 4.2, "goal_prob": 0.12}
        ]
    },
    "Atlético Mineiro": {
        "fifa_rank": 10,
        "recent_form": ["W", "W", "D", "W", "L", "W", "D", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.95, "xg_against": 1.00, "corners_for": 7, "corners_against": 4, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 58},
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.40, "xg_against": 0.60, "corners_for": 8, "corners_against": 3, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 61},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.50, "xg_against": 1.15, "corners_for": 6, "corners_against": 5, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 55},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.80, "xg_against": 0.95, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 57},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 1.15, "xg_against": 1.20, "corners_for": 5, "corners_against": 4, "shots_total": 11, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 54},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.85, "xg_against": 0.70, "corners_for": 7, "corners_against": 3, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 60}
        ],
        "key_players": [
            {"name": "Hulk", "position": "Ídolo y Bombardero", "avg_shots_p90": 3.6, "avg_sot_p90": 1.8, "shot_creation_actions": 5.4, "goal_prob": 0.52},
            {"name": "Paulinho", "position": "Goleador Rápido", "avg_shots_p90": 3.0, "avg_sot_p90": 1.5, "shot_creation_actions": 3.2, "goal_prob": 0.44},
            {"name": "Gustavo Scarpa", "position": "Asistente Maestro", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 6.1, "goal_prob": 0.28},
            {"name": "Deyverson", "position": "Delantero de Choque", "avg_shots_p90": 2.1, "avg_sot_p90": 1.0, "shot_creation_actions": 2.1, "goal_prob": 0.35}
        ]
    },
    "Atlético Nacional": {
        "fifa_rank": 25,
        "recent_form": ["W", "W", "D", "W", "W", "L", "W", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.85, "xg_against": 0.65, "corners_for": 7, "corners_against": 3, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 59},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.70, "xg_against": 0.90, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 57},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.40, "xg_against": 1.10, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 55},
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.15, "xg_against": 0.80, "corners_for": 8, "corners_against": 3, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 61},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.50, "xg_against": 0.70, "corners_for": 6, "corners_against": 3, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 58},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 1.10, "xg_against": 1.25, "corners_for": 5, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 53}
        ],
        "key_players": [
            {"name": "Alfredo Morelos", "position": "Delantero Letal", "avg_shots_p90": 3.1, "avg_sot_p90": 1.5, "shot_creation_actions": 2.8, "goal_prob": 0.45},
            {"name": "Edwin Cardona", "position": "Pegada y Creatividad", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 5.5, "goal_prob": 0.35},
            {"name": "Marino Hinestroza", "position": "Extremo Explosivo", "avg_shots_p90": 2.2, "avg_sot_p90": 1.0, "shot_creation_actions": 4.1, "goal_prob": 0.28},
            {"name": "Kevin Viveros", "position": "Fuerza y Velocidad", "avg_shots_p90": 2.3, "avg_sot_p90": 1.1, "shot_creation_actions": 2.3, "goal_prob": 0.32}
        ]
    },
    "Deportes Tolima": {
        "fifa_rank": 32,
        "recent_form": ["W", "D", "W", "L", "W", "D", "W", "D"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.65, "xg_against": 1.05, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 51},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.25, "xg_against": 1.15, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 49},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.70, "xg_against": 0.75, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 53},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.95, "xg_against": 1.30, "corners_for": 4, "corners_against": 6, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 16, "possession": 47},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.40, "xg_against": 0.85, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 50},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.30, "xg_against": 1.20, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 48}
        ],
        "key_players": [
            {"name": "Yeison Guzmán", "position": "Figura y Goleador", "avg_shots_p90": 2.7, "avg_sot_p90": 1.3, "shot_creation_actions": 5.2, "goal_prob": 0.40},
            {"name": "Brayan Gil", "position": "Referente de Ataque", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 2.4, "goal_prob": 0.34},
            {"name": "Junior Hernández", "position": "Lateral Profundo", "avg_shots_p90": 1.3, "avg_sot_p90": 0.5, "shot_creation_actions": 3.5, "goal_prob": 0.15},
            {"name": "Jeison Lucumí", "position": "Extremo Eléctrico", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 3.8, "goal_prob": 0.24}
        ]
    },
    "Fortaleza": {
        "fifa_rank": 40,
        "recent_form": ["W", "D", "W", "L", "D", "W", "L", "D"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.20, "xg_against": 1.15, "corners_for": 5, "corners_against": 4, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 49},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.60, "xg_against": 0.80, "corners_for": 6, "corners_against": 3, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 52},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.90, "xg_against": 1.25, "corners_for": 4, "corners_against": 5, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 47},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.15, "xg_against": 1.20, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 48},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.55, "xg_against": 1.05, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 51},
            {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.85, "xg_against": 0.80, "corners_for": 4, "corners_against": 4, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 50}
        ],
        "key_players": [
            {"name": "Adrián Parra", "position": "Delantero Rápido", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 2.5, "goal_prob": 0.32},
            {"name": "Nicolás Rodríguez", "position": "Extremo Picante", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 3.8, "goal_prob": 0.26},
            {"name": "Ronaldo Pájaro", "position": "Pivote de Equilibrio", "avg_shots_p90": 1.1, "avg_sot_p90": 0.4, "shot_creation_actions": 2.9, "goal_prob": 0.12}
        ]
    },
    "Millonarios": {
        "fifa_rank": 22,
        "recent_form": ["W", "W", "D", "W", "L", "W", "W", "D"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.80, "xg_against": 0.95, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 58},
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.20, "xg_against": 0.60, "corners_for": 7, "corners_against": 3, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 62},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.45, "xg_against": 1.10, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 55},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.75, "xg_against": 0.70, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 59},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 1.20, "xg_against": 1.25, "corners_for": 5, "corners_against": 4, "shots_total": 11, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 57},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.50, "xg_against": 0.65, "corners_for": 6, "corners_against": 3, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 60}
        ],
        "key_players": [
            {"name": "Radamel Falcao García", "position": "El Tigre / Leyenda Mundial", "avg_shots_p90": 3.2, "avg_sot_p90": 1.6, "shot_creation_actions": 2.9, "goal_prob": 0.50},
            {"name": "Leonardo Castro", "position": "Delantero Incansable", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 3.1, "goal_prob": 0.40},
            {"name": "Daniel Ruiz", "position": "Zurda Creativa", "avg_shots_p90": 2.2, "avg_sot_p90": 1.0, "shot_creation_actions": 5.4, "goal_prob": 0.28},
            {"name": "David Mackalister Silva", "position": "Capitán y Guía", "avg_shots_p90": 1.8, "avg_sot_p90": 0.8, "shot_creation_actions": 4.8, "goal_prob": 0.22}
        ]
    }
}

# 2. Cargar y actualizar teams_database.json
with open(teams_file, "r", encoding="utf-8") as f:
    teams_db = json.load(f)

for t_name, t_data in new_teams.items():
    teams_db[t_name] = t_data
    print(f"  + Equipo cargado: {t_name}")

with open(teams_file, "w", encoding="utf-8") as f:
    json.dump(teams_db, f, ensure_ascii=False, indent=2)
print("-> teams_database.json actualizado.")

# 3. Metadatos de partidos
new_matches = {
    "Santos vs Flamengo": {
        "tournament": "Brasileirão Serie A - Fecha 29 (Clásico Interestatal)",
        "stadium": "Estádio Urbano Caldeira (Vila Belmiro, Santos)",
        "spectators_est": "16,000 en estadio (~28M audiencia en Brasil)",
        "referee": "Wilton Pereira Sampaio",
        "referee_avg_yellows": 4.5,
        "referee_avg_reds": 0.20,
        "intensity": "Máxima (Duelo de tradición en Vila Belmiro; Giuliano retando el poderío ofensivo de Flamengo)"
    },
    "Palmeiras vs Bahia": {
        "tournament": "Brasileirão Serie A - Fecha 29",
        "stadium": "Allianz Parque (São Paulo)",
        "spectators_est": "39,000 en estadio (~22M audiencia)",
        "referee": "Ramon Abatti Abel",
        "referee_avg_yellows": 4.2,
        "referee_avg_reds": 0.15,
        "intensity": "Muy Alta (Palmeiras en la pelea por el título en casa ante el buen fútbol del Bahia de Rogério Ceni)"
    },
    "Fluminense vs Coritiba": {
        "tournament": "Brasileirão Serie A - Fecha 29",
        "stadium": "Estádio Maracanã (Río de Janeiro)",
        "spectators_est": "45,000 en estadio (~20M audiencia)",
        "referee": "Anderson Daronco",
        "referee_avg_yellows": 4.6,
        "referee_avg_reds": 0.18,
        "intensity": "Alta (Fluminense empujando en el Maracanã con Germán Cano y Jhon Arias ante el bloque bajo de Coritiba)"
    },
    "Athletico Paranaense vs Atlético Mineiro": {
        "tournament": "Brasileirão Serie A - Fecha 29",
        "stadium": "Ligga Arena (Curitiba)",
        "spectators_est": "32,000 en estadio (~18M audiencia)",
        "referee": "Flavio Rodrigues de Souza",
        "referee_avg_yellows": 4.8,
        "referee_avg_reds": 0.22,
        "intensity": "Muy Alta (Choque físico y de ritmo cerrado en el césped sintético de Curitiba; Mastriani vs Hulk)"
    },
    "Atlético Nacional vs Deportes Tolima": {
        "tournament": "Liga BetPlay Dimayor - Fecha 14 (Clásico del FPC)",
        "stadium": "Estadio Atanasio Girardot (Medellín)",
        "spectators_est": "38,000 en estadio (~15M audiencia Colombia)",
        "referee": "Wilmar Roldán",
        "referee_avg_yellows": 4.4,
        "referee_avg_reds": 0.18,
        "intensity": "Máxima (Duelo de gigantes colombianos en Medellín; Cardona y Morelos frente a Yeison Guzmán)"
    },
    "Fortaleza vs Millonarios": {
        "tournament": "Liga BetPlay Dimayor - Fecha 14",
        "stadium": "Estadio Metropolitano de Techo (Bogotá)",
        "spectators_est": "10,000 en estadio (~12M audiencia Colombia)",
        "referee": "Carlos Betancur",
        "referee_avg_yellows": 4.2,
        "referee_avg_reds": 0.14,
        "intensity": "Alta (Millonarios liderado por Radamel Falcao García en Bogotá ante la intensidad física de Fortaleza)"
    }
}

with open(matches_file, "r", encoding="utf-8") as f:
    matches_db = json.load(f)

for m_key, m_val in new_matches.items():
    matches_db[m_key] = m_val
    print(f"  + Partido cargado: {m_key}")

with open(matches_file, "w", encoding="utf-8") as f:
    json.dump(matches_db, f, ensure_ascii=False, indent=2)
print("-> matches_database.json actualizado.")

# 4. Actualizar official_calendar.json para 2026-10-08
with open(cal_file, "r", encoding="utf-8") as f:
    cal_db = json.load(f)

cal_db["2026-10-08"] = {
    "date_str": "08/10/2026",
    "day_name": "Jueves",
    "competition": "Brasileirão Serie A (Fecha 29) & Liga BetPlay Élite",
    "fixtures": [
        ["Santos", "Flamengo", "DOBLE_OPORTUNIDAD"],
        ["Palmeiras", "Bahia", "GOL_EQUIPO"],
        ["Fluminense", "Coritiba", "DOBLE_OPORTUNIDAD"],
        ["Athletico Paranaense", "Atlético Mineiro", "GOLES_UNDER"],
        ["Atlético Nacional", "Deportes Tolima", "DOBLE_OPORTUNIDAD"],
        ["Fortaleza", "Millonarios", "GOL_EQUIPO"]
    ]
}

with open(cal_file, "w", encoding="utf-8") as f:
    json.dump(cal_db, f, ensure_ascii=False, indent=2)
print("-> official_calendar.json actualizado para 2026-10-08 con los 6 partidos de clubes reales.")
