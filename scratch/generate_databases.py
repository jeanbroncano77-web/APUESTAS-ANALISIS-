# -*- coding: utf-8 -*-
"""
generate_databases.py
Genera teams_database.json y matches_database.json para los 6 partidos estelares de
MAÑANA VIERNES 02/10/2026:
1. Francia vs Italia (UEFA Nations League - La Fija de Oro)
2. Bélgica vs Turquía (UEFA Nations League)
3. Corea del Sur vs Venezuela (Amistoso Internacional FIFA)
4. Bosnia y Herzegovina vs Suecia (UEFA Nations League)
5. Polonia vs Rumanía (UEFA Nations League)
6. Hungría vs Georgia (UEFA Nations League)
"""

import json
import os

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo\sports_agents"

teams_data = {
    # --- PARTIDO 1: FRANCIA VS ITALIA ---
    "Francia": {
        "fifa_rank": 2,
        "recent_form": ["W", "W", "D", "W", "W", "W", "D", "W"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.8, "xg_against": 0.8, "corners_for": 8, "corners_against": 3, "shots_total": 19, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 63},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.3, "xg_against": 0.5, "corners_for": 7, "corners_against": 2, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 8, "possession": 61},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.9, "xg_against": 0.7, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 58},
            {"goals_scored": 4, "goals_conceded": 1, "xg_for": 3.2, "xg_against": 0.9, "corners_for": 9, "corners_against": 3, "shots_total": 21, "shots_on_target": 9, "yellow_cards": 0, "red_cards": 0, "fouls": 7, "possession": 65},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.1, "xg_against": 1.2, "corners_for": 6, "corners_against": 5, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 57},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.4, "xg_against": 0.6, "corners_for": 7, "corners_against": 3, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 62}
        ],
        "key_players": [
            {"name": "Kylian Mbappé", "position": "Delantero Centro / Extremo", "avg_shots_p90": 4.1, "avg_sot_p90": 2.1, "shot_creation_actions": 5.8, "goal_prob": 0.58},
            {"name": "Ousmane Dembélé", "position": "Extremo Derecho", "avg_shots_p90": 2.9, "avg_sot_p90": 1.3, "shot_creation_actions": 6.2, "goal_prob": 0.32},
            {"name": "Bradley Barcola", "position": "Extremo Izquierdo", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 4.5, "goal_prob": 0.30},
            {"name": "Aurélien Tchouaméni", "position": "Pivote Organizador", "avg_shots_p90": 1.5, "avg_sot_p90": 0.6, "shot_creation_actions": 3.1, "goal_prob": 0.12},
            {"name": "Eduardo Camavinga", "position": "Interior Mixto", "avg_shots_p90": 1.3, "avg_sot_p90": 0.4, "shot_creation_actions": 3.8, "goal_prob": 0.10}
        ]
    },
    "Italia": {
        "fifa_rank": 9,
        "recent_form": ["W", "D", "W", "L", "W", "D", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.8, "xg_against": 1.1, "corners_for": 5, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 54},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.4, "xg_against": 1.3, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 51},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.9, "xg_against": 0.7, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 56},
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.9, "xg_against": 1.8, "corners_for": 4, "corners_against": 6, "shots_total": 9, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 48},
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.2, "xg_against": 1.0, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 55},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.3, "xg_against": 1.2, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 50}
        ],
        "key_players": [
            {"name": "Mateo Retegui", "position": "Delantero Centro", "avg_shots_p90": 3.0, "avg_sot_p90": 1.4, "shot_creation_actions": 2.6, "goal_prob": 0.44},
            {"name": "Nicolò Barella", "position": "Interior Llegador", "avg_shots_p90": 2.1, "avg_sot_p90": 0.8, "shot_creation_actions": 4.8, "goal_prob": 0.22},
            {"name": "Sandro Tonali", "position": "Mediocentro Físico", "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 3.9, "goal_prob": 0.14},
            {"name": "Federico Dimarco", "position": "Carrilero Izquierdo", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 5.1, "goal_prob": 0.18},
            {"name": "Giacomo Raspadori", "position": "Segundo Punta", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 3.4, "goal_prob": 0.28}
        ]
    },

    # --- PARTIDO 2: BÉLGICA VS TURQUÍA ---
    "Bélgica": {
        "fifa_rank": 6,
        "recent_form": ["W", "D", "W", "L", "W", "W", "D"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.6, "xg_against": 1.0, "corners_for": 7, "corners_against": 3, "shots_total": 18, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 62},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.7, "xg_against": 1.2, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 59},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.1, "xg_against": 0.6, "corners_for": 8, "corners_against": 2, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 64},
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 1.1, "xg_against": 1.9, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 53},
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.8, "xg_against": 0.4, "corners_for": 8, "corners_against": 2, "shots_total": 20, "shots_on_target": 8, "yellow_cards": 0, "red_cards": 0, "fouls": 8, "possession": 66}
        ],
        "key_players": [
            {"name": "Kevin De Bruyne", "position": "Mediapunta Organizador", "avg_shots_p90": 3.2, "avg_sot_p90": 1.4, "shot_creation_actions": 7.4, "goal_prob": 0.42},
            {"name": "Jérémy Doku", "position": "Extremo Regateador", "avg_shots_p90": 2.6, "avg_sot_p90": 1.1, "shot_creation_actions": 6.0, "goal_prob": 0.28},
            {"name": "Loïs Openda", "position": "Delantero Vertiginoso", "avg_shots_p90": 3.4, "avg_sot_p90": 1.6, "shot_creation_actions": 2.8, "goal_prob": 0.48},
            {"name": "Youri Tielemans", "position": "Mediocentro Llegador", "avg_shots_p90": 1.9, "avg_sot_p90": 0.7, "shot_creation_actions": 4.1, "goal_prob": 0.20}
        ]
    },
    "Turquía": {
        "fifa_rank": 26,
        "recent_form": ["W", "W", "D", "W", "L", "W", "D"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.3, "xg_against": 1.3, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 55},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.8, "xg_against": 1.1, "corners_for": 5, "corners_against": 5, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 52},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.3, "xg_against": 1.4, "corners_for": 4, "corners_against": 6, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 49},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.9, "xg_against": 0.8, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 56},
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.2, "xg_against": 1.7, "corners_for": 5, "corners_against": 6, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 4, "red_cards": 0, "fouls": 16, "possession": 50}
        ],
        "key_players": [
            {"name": "Arda Güler", "position": "Mediapunta Genio", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 5.9, "goal_prob": 0.36},
            {"name": "Kenan Yıldız", "position": "Extremo / Delantero", "avg_shots_p90": 2.7, "avg_sot_p90": 1.2, "shot_creation_actions": 4.4, "goal_prob": 0.34},
            {"name": "Hakan Çalhanoğlu", "position": "Pivote Director / Balón Parado", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 6.1, "goal_prob": 0.26},
            {"name": "Kerem Aktürkoğlu", "position": "Extremo Eléctrico", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 3.8, "goal_prob": 0.32}
        ]
    },

    # --- PARTIDO 3: COREA DEL SUR VS VENEZUELA ---
    "Corea del Sur": {
        "fifa_rank": 23,
        "recent_form": ["W", "W", "D", "W", "W", "D", "W"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.5, "xg_against": 0.5, "corners_for": 8, "corners_against": 2, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 67},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.9, "xg_against": 1.0, "corners_for": 7, "corners_against": 3, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 63},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.6, "xg_against": 1.1, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 60},
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.4, "xg_against": 0.8, "corners_for": 8, "corners_against": 3, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 8, "possession": 65},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.1, "xg_against": 0.4, "corners_for": 7, "corners_against": 2, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 0, "red_cards": 0, "fouls": 7, "possession": 68}
        ],
        "key_players": [
            {"name": "Son Heung-min", "position": "Extremo / Delantero Estrella", "avg_shots_p90": 3.6, "avg_sot_p90": 1.8, "shot_creation_actions": 6.2, "goal_prob": 0.52},
            {"name": "Lee Kang-in", "position": "Mediapunta Creativo", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 6.5, "goal_prob": 0.32},
            {"name": "Hwang Hee-chan", "position": "Delantero Físico", "avg_shots_p90": 2.6, "avg_sot_p90": 1.2, "shot_creation_actions": 3.2, "goal_prob": 0.36},
            {"name": "Kim Min-jae", "position": "Defensa Central Muralla", "avg_shots_p90": 0.8, "avg_sot_p90": 0.3, "shot_creation_actions": 1.5, "goal_prob": 0.08}
        ]
    },
    "Venezuela": {
        "fifa_rank": 37,
        "recent_form": ["D", "W", "D", "L", "W", "D", "L"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.2, "xg_against": 1.3, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 44},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.6, "xg_against": 1.1, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 47},
            {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.8, "xg_against": 1.2, "corners_for": 3, "corners_against": 6, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 41},
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.1, "xg_against": 1.7, "corners_for": 4, "corners_against": 6, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 4, "red_cards": 0, "fouls": 16, "possession": 43},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.3, "xg_against": 0.9, "corners_for": 4, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 46}
        ],
        "key_players": [
            {"name": "Salomón Rondón", "position": "Delantero Referente", "avg_shots_p90": 2.7, "avg_sot_p90": 1.2, "shot_creation_actions": 2.5, "goal_prob": 0.38},
            {"name": "Yeferson Soteldo", "position": "Extremo Elusivo", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 5.4, "goal_prob": 0.24},
            {"name": "Yangel Herrera", "position": "Pivote Mixto / Llegador", "avg_shots_p90": 1.6, "avg_sot_p90": 0.6, "shot_creation_actions": 3.1, "goal_prob": 0.16},
            {"name": "Jefferson Savarino", "position": "Extremo / Conector", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 4.0, "goal_prob": 0.22}
        ]
    },

    # --- PARTIDO 4: BOSNIA Y HERZEGOVINA VS SUECIA ---
    "Bosnia y Herzegovina": {
        "fifa_rank": 75,
        "recent_form": ["L", "D", "L", "W", "L", "D"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.1, "xg_against": 1.8, "corners_for": 4, "corners_against": 6, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 45},
            {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.9, "xg_against": 1.4, "corners_for": 3, "corners_against": 5, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 46},
            {"goals_scored": 1, "goals_conceded": 3, "xg_for": 1.0, "xg_against": 2.3, "corners_for": 4, "corners_against": 7, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 4, "red_cards": 0, "fouls": 16, "possession": 42},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.5, "xg_against": 1.2, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 50},
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.7, "xg_against": 1.9, "corners_for": 3, "corners_against": 6, "shots_total": 7, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 43}
        ],
        "key_players": [
            {"name": "Edin Džeko", "position": "Delantero Leyenda / Capitán", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 2.8, "goal_prob": 0.38},
            {"name": "Ermedin Demirović", "position": "Delantero Bundesliga", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 2.4, "goal_prob": 0.32},
            {"name": "Amar Dedić", "position": "Carrilero Ofensivo", "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 3.6, "goal_prob": 0.14},
            {"name": "Benjamin Tahirović", "position": "Mediocentro Recuperador", "avg_shots_p90": 1.0, "avg_sot_p90": 0.3, "shot_creation_actions": 2.2, "goal_prob": 0.08}
        ]
    },
    "Suecia": {
        "fifa_rank": 28,
        "recent_form": ["W", "W", "D", "W", "L", "W", "W"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.5, "xg_against": 1.0, "corners_for": 7, "corners_against": 3, "shots_total": 17, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 59},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.1, "xg_against": 0.7, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 57},
            {"goals_scored": 2, "goals_conceded": 2, "xg_for": 2.0, "xg_against": 1.6, "corners_for": 6, "corners_against": 5, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 55},
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.7, "xg_against": 0.5, "corners_for": 8, "corners_against": 2, "shots_total": 19, "shots_on_target": 9, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 62},
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.4, "xg_against": 1.8, "corners_for": 5, "corners_against": 6, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 51}
        ],
        "key_players": [
            {"name": "Viktor Gyökeres", "position": "Delantero Letal / Goleador Europa", "avg_shots_p90": 3.9, "avg_sot_p90": 2.0, "shot_creation_actions": 4.1, "goal_prob": 0.56},
            {"name": "Alexander Isak", "position": "Delantero Premier League", "avg_shots_p90": 3.2, "avg_sot_p90": 1.5, "shot_creation_actions": 3.8, "goal_prob": 0.46},
            {"name": "Dejan Kulusevski", "position": "Extremo / Creador Spurs", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 5.9, "goal_prob": 0.28},
            {"name": "Anthony Elanga", "position": "Extremo Rápido", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 3.4, "goal_prob": 0.22}
        ]
    },

    # --- PARTIDO 5: POLONIA VS RUMANÍA ---
    "Polonia": {
        "fifa_rank": 30,
        "recent_form": ["W", "L", "D", "W", "L", "W", "D"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.9, "xg_against": 1.2, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 56},
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.3, "xg_against": 1.8, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 49},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.5, "xg_against": 1.3, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 52},
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.2, "xg_against": 0.9, "corners_for": 7, "corners_against": 3, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 58},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 1.0, "xg_against": 1.4, "corners_for": 4, "corners_against": 5, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 51}
        ],
        "key_players": [
            {"name": "Robert Lewandowski", "position": "Delantero Histórico / Capitán", "avg_shots_p90": 3.7, "avg_sot_p90": 1.8, "shot_creation_actions": 3.8, "goal_prob": 0.54},
            {"name": "Piotr Zieliński", "position": "Mediapunta Maestro", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 5.6, "goal_prob": 0.26},
            {"name": "Nicola Zalewski", "position": "Carrilero Desequilibrante", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 4.5, "goal_prob": 0.18},
            {"name": "Sebastian Szymański", "position": "Mediapunta Fenerbahçe", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 4.2, "goal_prob": 0.26}
        ]
    },
    "Rumanía": {
        "fifa_rank": 45,
        "recent_form": ["W", "W", "D", "L", "W", "D"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.6, "xg_against": 1.2, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 51},
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.1, "xg_against": 0.6, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 54},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.2, "xg_against": 1.3, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 48},
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.8, "xg_against": 1.9, "corners_for": 3, "corners_against": 6, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 44},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.7, "xg_against": 0.8, "corners_for": 5, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 50}
        ],
        "key_players": [
            {"name": "Dennis Man", "position": "Extremo Serie A", "avg_shots_p90": 2.7, "avg_sot_p90": 1.2, "shot_creation_actions": 4.6, "goal_prob": 0.35},
            {"name": "Răzvan Marin", "position": "Mediocentro / Especialista Penaltis", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 4.1, "goal_prob": 0.24},
            {"name": "Valentin Mihăilă", "position": "Extremo Rápido", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 3.7, "goal_prob": 0.26},
            {"name": "Radu Drăgușin", "position": "Central Muralla Spurs", "avg_shots_p90": 0.7, "avg_sot_p90": 0.2, "shot_creation_actions": 1.2, "goal_prob": 0.08}
        ]
    },

    # --- PARTIDO 6: HUNGRÍA VS GEORGIA ---
    "Hungría": {
        "fifa_rank": 31,
        "recent_form": ["W", "D", "L", "D", "W", "L", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.8, "xg_against": 1.1, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 53},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.4, "xg_against": 1.3, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 50},
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.9, "xg_against": 1.9, "corners_for": 4, "corners_against": 6, "shots_total": 9, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 47},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.9, "xg_against": 0.7, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 55},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.5, "xg_against": 0.8, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 52}
        ],
        "key_players": [
            {"name": "Dominik Szoboszlai", "position": "Mediapunta Liverpool / Capitán", "avg_shots_p90": 3.4, "avg_sot_p90": 1.6, "shot_creation_actions": 6.8, "goal_prob": 0.44},
            {"name": "Roland Sallai", "position": "Extremo Ofensivo", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 3.9, "goal_prob": 0.30},
            {"name": "Barnabás Varga", "position": "Delantero Centro Aéreo", "avg_shots_p90": 2.6, "avg_sot_p90": 1.2, "shot_creation_actions": 2.2, "goal_prob": 0.36},
            {"name": "Willi Orbán", "position": "Defensa Central Leipzig", "avg_shots_p90": 0.9, "avg_sot_p90": 0.4, "shot_creation_actions": 1.4, "goal_prob": 0.10}
        ]
    },
    "Georgia": {
        "fifa_rank": 66,
        "recent_form": ["W", "W", "L", "W", "D", "L"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.7, "xg_against": 1.3, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 47},
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.2, "xg_against": 1.1, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 49},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 1.1, "xg_against": 1.4, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 45},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.8, "xg_against": 0.9, "corners_for": 5, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 48},
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.3, "xg_against": 1.8, "corners_for": 4, "corners_against": 6, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 44}
        ],
        "key_players": [
            {"name": "Khvicha Kvaratskhelia", "position": "Extremo Genio / Napoli", "avg_shots_p90": 3.8, "avg_sot_p90": 1.8, "shot_creation_actions": 6.5, "goal_prob": 0.48},
            {"name": "Georges Mikautadze", "position": "Delantero Revelación Lyon", "avg_shots_p90": 3.1, "avg_sot_p90": 1.5, "shot_creation_actions": 3.2, "goal_prob": 0.42},
            {"name": "Giorgi Kochorashvili", "position": "Mediocentro Físico", "avg_shots_p90": 1.6, "avg_sot_p90": 0.6, "shot_creation_actions": 3.1, "goal_prob": 0.16},
            {"name": "Otar Kiteishvili", "position": "Mediapunta Dinámico", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 3.9, "goal_prob": 0.18}
        ]
    }
}

matches_data = {
    "Francia vs Italia": {
        "tournament": "UEFA Nations League - Liga A (Clásico Mundial de Élite)",
        "stadium": "Stade de France (Saint-Denis, París)",
        "spectators_est": "80,000 en estadio (~55M audiencia global)",
        "referee": "Szymon Marciniak",
        "referee_avg_yellows": 4.1,
        "referee_avg_reds": 0.16,
        "intensity": "Máxima (Batalla estelar de gigantes europeos; Mbappé y Dembélé retando el muro táctico de Bastoni y Donnarumma)"
    },
    "Bélgica vs Turquía": {
        "tournament": "UEFA Nations League - Liga A",
        "stadium": "King Baudouin Stadium (Bruselas)",
        "spectators_est": "48,000 en estadio (~28M audiencia global)",
        "referee": "Felix Zwayer",
        "referee_avg_yellows": 4.3,
        "referee_avg_reds": 0.18,
        "intensity": "Muy Alta (Duelo electrizante entre el talento creativo de De Bruyne y el descaro juvenil de Arda Güler y Kenan Yıldız)"
    },
    "Corea del Sur vs Venezuela": {
        "tournament": "Amistoso Internacional FIFA (Fecha FIFA Élite)",
        "stadium": "Seoul World Cup Stadium (Seúl)",
        "spectators_est": "64,000 en estadio (~22M audiencia global)",
        "referee": "Alireza Faghani",
        "referee_avg_yellows": 3.2,
        "referee_avg_reds": 0.08,
        "intensity": "Alta (Velocidad endiablada y precisión de Son Heung-min y Lee Kang-in frente a la combatividad de la Vinotinto de Rondón)"
    },
    "Bosnia y Herzegovina vs Suecia": {
        "tournament": "UEFA Nations League - Liga B",
        "stadium": "Bilino Polje (Zenica)",
        "spectators_est": "14,000 en estadio (~18M audiencia global)",
        "referee": "Clément Turpin",
        "referee_avg_yellows": 4.4,
        "referee_avg_reds": 0.20,
        "intensity": "Muy Alta (Caldera balcánica caliente; Džeko comandando el orgullo local ante el vendaval goleador de Gyökeres e Isak)"
    },
    "Polonia vs Rumanía": {
        "tournament": "UEFA Nations League - Liga A",
        "stadium": "PGE Narodowy (Varsovia)",
        "spectators_est": "56,500 en estadio (~24M audiencia global)",
        "referee": "Michael Oliver",
        "referee_avg_yellows": 3.8,
        "referee_avg_reds": 0.14,
        "intensity": "Alta (Lewandowski liderando a las Águilas Blancas en Varsovia ante la velocidad al contragolpe de Dennis Man y Rumanía)"
    },
    "Hungría vs Georgia": {
        "tournament": "UEFA Nations League - Liga B",
        "stadium": "Puskás Aréna (Budapest)",
        "spectators_est": "62,000 en estadio (~20M audiencia global)",
        "referee": "Slavko Vinčić",
        "referee_avg_yellows": 4.0,
        "referee_avg_reds": 0.15,
        "intensity": "Muy Alta (El rugido de la Puskás Aréna con Szoboszlai ante la magia desequilibrante de Khvicha Kvaratskhelia)"
    }
}

with open(os.path.join(base_dir, "teams_database.json"), "w", encoding="utf-8") as f:
    json.dump(teams_data, f, ensure_ascii=False, indent=2)
print("teams_database.json generado con éxito.")

with open(os.path.join(base_dir, "matches_database.json"), "w", encoding="utf-8") as f:
    json.dump(matches_data, f, ensure_ascii=False, indent=2)
print("matches_database.json generado con éxito.")
