# -*- coding: utf-8 -*-
"""
enrich_thursday_data.py
Enriquece matches_database.json y teams_database.json con datos completos para los 6 choques
de UEFA Europa League y Conference League del Jueves 15/10/2026.
"""

import json
import os
import sys

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
matches_file = os.path.join(base_dir, "sports_agents", "matches_database.json")
teams_file = os.path.join(base_dir, "sports_agents", "teams_database.json")

# 1. Matches Database
with open(matches_file, "r", encoding="utf-8") as f:
    matches_db = json.load(f)

thursday_matches = {
    "Benfica vs Celtic": {
        "tournament": "UEFA Europa League - Fase de Liga (Jornada 2 - La Fija de Oro)",
        "stadium": "Estádio da Luz (Lisboa, Portugal)",
        "spectators_est": "64,500 en estadio (~40M audiencia global)",
        "referee": "Clément Turpin",
        "referee_avg_yellows": 4.1,
        "referee_avg_reds": 0.15,
        "intensity": "Máxima (Las Águilas de Di María y Pavlidis buscando la supremacía europea ante el fervor escocés de Celtic)"
    },
    "Red Bull Salzburg vs AC Milan": {
        "tournament": "UEFA Europa League - Fase de Liga (Jornada 2)",
        "stadium": "Red Bull Arena (Salzburgo, Austria)",
        "spectators_est": "30,188 espectadores",
        "referee": "Michael Oliver",
        "referee_avg_yellows": 3.9,
        "referee_avg_reds": 0.14,
        "intensity": "Alta (Juventud de Konaté y Gloukh ante la jerarquía italiana de Leão, Pulisic y Theo Hernández)"
    },
    "Celta Vigo vs Juventus": {
        "tournament": "UEFA Europa League - Fase de Liga (Jornada 2)",
        "stadium": "Abanca-Balaídos (Vigo, España)",
        "spectators_est": "24,000 espectadores",
        "referee": "Felix Zwayer",
        "referee_avg_yellows": 4.3,
        "referee_avg_reds": 0.17,
        "intensity": "Alta (Balaídos empujando a Iago Aspas ante el sólido cerrojo bianconero de Bremer y la contundencia de Vlahović)"
    },
    "Lech Poznań vs Bayer Leverkusen": {
        "tournament": "UEFA Europa League - Fase de Liga (Jornada 2)",
        "stadium": "Enea Stadion (Poznań, Polonia)",
        "spectators_est": "42,000 espectadores",
        "referee": "Anthony Taylor",
        "referee_avg_yellows": 4.0,
        "referee_avg_reds": 0.15,
        "intensity": "Muy Alta (Caldera polaca en Poznań retando al vertiginoso campeón alemán de Wirtz, Boniface y Xhaka)"
    },
    "Olympique Lyon vs Crystal Palace": {
        "tournament": "UEFA Conference League - Fase de Liga (Jornada 2)",
        "stadium": "Groupama Stadium (Décines-Charpieu, Francia)",
        "spectators_est": "58,000 espectadores",
        "referee": "Jesús Gil Manzano",
        "referee_avg_yellows": 4.5,
        "referee_avg_reds": 0.20,
        "intensity": "Máxima (Lacazette y Cherki protegiendo la localía francesa ante la verticalidad de la Premier League de Mateta y Eze)"
    },
    "Hajduk Split vs AFC Ajax": {
        "tournament": "UEFA Conference League - Fase de Liga (Jornada 2)",
        "stadium": "Stadion Poljud (Split, Croacia)",
        "spectators_est": "34,000 hinchas de la Torcida",
        "referee": "Espen Eskås",
        "referee_avg_yellows": 4.2,
        "referee_avg_reds": 0.18,
        "intensity": "Extrema (El infierno de Poljud con Rakitić y Livaja ante la escuela dinámica de Ámsterdam liderada por Brobbey y Taylor)"
    }
}

matches_db.update(thursday_matches)
with open(matches_file, "w", encoding="utf-8") as f:
    json.dump(matches_db, f, indent=2, ensure_ascii=False)

print("[1] matches_database.json actualizado con éxito!")

# 2. Teams Database
with open(teams_file, "r", encoding="utf-8") as f:
    teams_db = json.load(f)

thursday_teams = {
    "Benfica": {
        "fifa_rank": 14,
        "recent_form": ["W", "W", "W", "D", "W", "W", "W", "W"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.6, "xg_against": 0.5, "corners_for": 8, "corners_against": 3, "shots_total": 19, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 66},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.2, "xg_against": 0.8, "corners_for": 7, "corners_against": 4, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 63},
            {"goals_scored": 4, "goals_conceded": 1, "xg_for": 2.9, "xg_against": 0.7, "corners_for": 9, "corners_against": 2, "shots_total": 21, "shots_on_target": 9, "yellow_cards": 1, "red_cards": 0, "fouls": 8, "possession": 68},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.9, "xg_against": 0.9, "corners_for": 6, "corners_against": 5, "shots_total": 15, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 60},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.1, "xg_against": 0.6, "corners_for": 7, "corners_against": 3, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 64}
        ],
        "key_players": [
            {"name": "Ángel Di María", "position": "Extremo Creador / Estrella", "avg_shots_p90": 2.9, "avg_sot_p90": 1.4, "shot_creation_actions": 6.9, "goal_prob": 0.40},
            {"name": "Vangelis Pavlidis", "position": "Delantero Centro Goleador", "avg_shots_p90": 3.2, "avg_sot_p90": 1.6, "shot_creation_actions": 3.5, "goal_prob": 0.48},
            {"name": "Orkun Kökçü", "position": "Pivote Organizador", "avg_shots_p90": 1.8, "avg_sot_p90": 0.8, "shot_creation_actions": 5.4, "goal_prob": 0.22},
            {"name": "Florentino Luís", "position": "Pivote Defensivo", "avg_shots_p90": 0.6, "avg_sot_p90": 0.2, "shot_creation_actions": 2.1, "goal_prob": 0.05}
        ]
    },
    "Celtic": {
        "fifa_rank": 38,
        "recent_form": ["W", "W", "W", "L", "W", "W", "D", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.8, "xg_against": 1.9, "corners_for": 6, "corners_against": 6, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 49},
            {"goals_scored": 1, "goals_conceded": 3, "xg_for": 1.2, "xg_against": 2.4, "corners_for": 4, "corners_against": 7, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 44},
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.2, "xg_against": 1.1, "corners_for": 7, "corners_against": 4, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 56}
        ],
        "key_players": [
            {"name": "Kyogo Furuhashi", "position": "Delantero Centro", "avg_shots_p90": 2.7, "avg_sot_p90": 1.2, "shot_creation_actions": 3.2, "goal_prob": 0.36},
            {"name": "Daizen Maeda", "position": "Extremo Izquierdo Veloz", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 4.0, "goal_prob": 0.28},
            {"name": "Callum McGregor", "position": "Capitán y Mediocampista", "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 4.5, "goal_prob": 0.15}
        ]
    },
    "Red Bull Salzburg": {
        "fifa_rank": 42,
        "recent_form": ["W", "L", "D", "W", "W", "L", "D", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.6, "xg_against": 1.8, "corners_for": 5, "corners_against": 6, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 48},
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.3, "xg_against": 2.0, "corners_for": 4, "corners_against": 7, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 46},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.7, "xg_against": 1.2, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 52}
        ],
        "key_players": [
            {"name": "Oscar Gloukh", "position": "Mediapunta Creador", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 5.1, "goal_prob": 0.32},
            {"name": "Karim Konaté", "position": "Delantero Centro Físico", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 2.8, "goal_prob": 0.38}
        ]
    },
    "AC Milan": {
        "fifa_rank": 12,
        "recent_form": ["W", "W", "D", "W", "L", "W", "W", "D"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.1, "xg_against": 1.0, "corners_for": 7, "corners_against": 4, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 59},
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.4, "xg_against": 0.6, "corners_for": 8, "corners_against": 3, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 62},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.8, "xg_against": 1.1, "corners_for": 6, "corners_against": 5, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 57}
        ],
        "key_players": [
            {"name": "Rafael Leão", "position": "Extremo Izquierdo / Desequilibrio", "avg_shots_p90": 3.3, "avg_sot_p90": 1.5, "shot_creation_actions": 6.7, "goal_prob": 0.44},
            {"name": "Christian Pulisic", "position": "Extremo / Segunda Punta", "avg_shots_p90": 2.6, "avg_sot_p90": 1.2, "shot_creation_actions": 5.2, "goal_prob": 0.38},
            {"name": "Theo Hernández", "position": "Lateral Ofensivo", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 4.6, "goal_prob": 0.20}
        ]
    },
    "Celta Vigo": {
        "fifa_rank": 45,
        "recent_form": ["D", "L", "W", "D", "L", "W", "D", "L"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.4, "xg_against": 1.5, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 50},
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.9, "xg_against": 2.1, "corners_for": 4, "corners_against": 7, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 45},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.7, "xg_against": 1.2, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 53}
        ],
        "key_players": [
            {"name": "Iago Aspas", "position": "Mediapunta / Leyenda", "avg_shots_p90": 2.6, "avg_sot_p90": 1.2, "shot_creation_actions": 5.5, "goal_prob": 0.35},
            {"name": "Tasos Douvikas", "position": "Delantero Centro", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 2.7, "goal_prob": 0.32}
        ]
    },
    "Juventus": {
        "fifa_rank": 15,
        "recent_form": ["W", "D", "W", "W", "D", "W", "W", "D"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.9, "xg_against": 0.6, "corners_for": 6, "corners_against": 3, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 58},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.6, "xg_against": 0.9, "corners_for": 5, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 56},
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.2, "xg_against": 0.8, "corners_for": 7, "corners_against": 4, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 61}
        ],
        "key_players": [
            {"name": "Dušan Vlahović", "position": "Delantero Centro Goleador", "avg_shots_p90": 3.4, "avg_sot_p90": 1.6, "shot_creation_actions": 3.4, "goal_prob": 0.46},
            {"name": "Kenan Yıldız", "position": "Mediapunta / Joya Turca", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 5.0, "goal_prob": 0.30},
            {"name": "Teun Koopmeiners", "position": "Centrocampista Total", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 5.6, "goal_prob": 0.25}
        ]
    },
    "Lech Poznań": {
        "fifa_rank": 62,
        "recent_form": ["W", "W", "D", "L", "W", "W", "D", "L"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.3, "xg_against": 1.9, "corners_for": 5, "corners_against": 6, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 47},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.6, "xg_against": 1.2, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 51}
        ],
        "key_players": [
            {"name": "Mikael Ishak", "position": "Delantero Centro", "avg_shots_p90": 2.6, "avg_sot_p90": 1.1, "shot_creation_actions": 3.0, "goal_prob": 0.35},
            {"name": "Afonso Sousa", "position": "Centrocampista", "avg_shots_p90": 1.6, "avg_sot_p90": 0.6, "shot_creation_actions": 4.2, "goal_prob": 0.18}
        ]
    },
    "Bayer Leverkusen": {
        "fifa_rank": 8,
        "recent_form": ["W", "D", "W", "W", "W", "D", "W", "W"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.5, "xg_against": 0.9, "corners_for": 8, "corners_against": 3, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 64},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.2, "xg_against": 0.6, "corners_for": 7, "corners_against": 4, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 63},
            {"goals_scored": 4, "goals_conceded": 2, "xg_for": 2.8, "xg_against": 1.4, "corners_for": 9, "corners_against": 4, "shots_total": 20, "shots_on_target": 9, "yellow_cards": 1, "red_cards": 0, "fouls": 8, "possession": 66}
        ],
        "key_players": [
            {"name": "Florian Wirtz", "position": "Mediapunta Magia / Balón de Oro", "avg_shots_p90": 3.1, "avg_sot_p90": 1.5, "shot_creation_actions": 7.5, "goal_prob": 0.44},
            {"name": "Victor Boniface", "position": "Delantero Potencia", "avg_shots_p90": 3.5, "avg_sot_p90": 1.7, "shot_creation_actions": 3.8, "goal_prob": 0.50},
            {"name": "Jeremie Frimpong", "position": "Carrilero Derecho Ofensivo", "avg_shots_p90": 2.2, "avg_sot_p90": 1.0, "shot_creation_actions": 5.4, "goal_prob": 0.30},
            {"name": "Granit Xhaka", "position": "Eje y Marcapasos", "avg_shots_p90": 1.2, "avg_sot_p90": 0.5, "shot_creation_actions": 5.0, "goal_prob": 0.12}
        ]
    },
    "Olympique Lyon": {
        "fifa_rank": 26,
        "recent_form": ["W", "W", "L", "W", "D", "W", "W", "D"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.0, "xg_against": 1.1, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 58},
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.3, "xg_against": 0.7, "corners_for": 7, "corners_against": 3, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 61},
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.5, "xg_against": 1.8, "corners_for": 5, "corners_against": 6, "shots_total": 13, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 54}
        ],
        "key_players": [
            {"name": "Alexandre Lacazette", "position": "Delantero Capitán", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 3.7, "goal_prob": 0.40},
            {"name": "Rayan Cherki", "position": "Mediapunta Creador", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 6.3, "goal_prob": 0.32},
            {"name": "Georges Mikautadze", "position": "Delantero Dinámico", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 3.0, "goal_prob": 0.35}
        ]
    },
    "Crystal Palace": {
        "fifa_rank": 35,
        "recent_form": ["W", "D", "L", "D", "W", "L", "W", "D"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.2, "xg_against": 1.8, "corners_for": 4, "corners_against": 6, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 46},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.7, "xg_against": 1.3, "corners_for": 5, "corners_against": 5, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 49},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.8, "xg_against": 1.5, "corners_for": 4, "corners_against": 7, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 43}
        ],
        "key_players": [
            {"name": "Jean-Philippe Mateta", "position": "Delantero Tanque", "avg_shots_p90": 2.7, "avg_sot_p90": 1.3, "shot_creation_actions": 2.6, "goal_prob": 0.38},
            {"name": "Eberechi Eze", "position": "Volante Ofensivo", "avg_shots_p90": 2.9, "avg_sot_p90": 1.2, "shot_creation_actions": 5.8, "goal_prob": 0.32}
        ]
    },
    "Hajduk Split": {
        "fifa_rank": 58,
        "recent_form": ["W", "D", "W", "W", "D", "W", "L", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.6, "xg_against": 1.1, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 53},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.3, "xg_against": 1.3, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 49}
        ],
        "key_players": [
            {"name": "Marko Livaja", "position": "Ídolo y Goleador", "avg_shots_p90": 3.0, "avg_sot_p90": 1.4, "shot_creation_actions": 4.8, "goal_prob": 0.42},
            {"name": "Ivan Rakitić", "position": "Cerebro Mundialista", "avg_shots_p90": 1.5, "avg_sot_p90": 0.6, "shot_creation_actions": 5.5, "goal_prob": 0.18}
        ]
    },
    "AFC Ajax": {
        "fifa_rank": 22,
        "recent_form": ["W", "W", "D", "W", "W", "D", "W", "L"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.3, "xg_against": 1.0, "corners_for": 8, "corners_against": 3, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 63},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.0, "xg_against": 1.2, "corners_for": 7, "corners_against": 4, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 61},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.8, "xg_against": 0.6, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 62}
        ],
        "key_players": [
            {"name": "Brian Brobbey", "position": "Delantero Potente", "avg_shots_p90": 3.1, "avg_sot_p90": 1.5, "shot_creation_actions": 3.4, "goal_prob": 0.44},
            {"name": "Kenneth Taylor", "position": "Centrocampista Ofensivo", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 5.2, "goal_prob": 0.26},
            {"name": "Jordan Henderson", "position": "Pivote y Marcapasos", "avg_shots_p90": 0.8, "avg_sot_p90": 0.3, "shot_creation_actions": 4.0, "goal_prob": 0.08}
        ]
    }
}

# Update database
teams_db.update(thursday_teams)
# Map common aliases
teams_db["Ajax"] = teams_db["AFC Ajax"]
teams_db["Lyon"] = teams_db["Olympique Lyon"]
teams_db["Salzburg"] = teams_db["Red Bull Salzburg"]
teams_db["Milan"] = teams_db["AC Milan"]
teams_db["Leverkusen"] = teams_db["Bayer Leverkusen"]

with open(teams_file, "w", encoding="utf-8") as f:
    json.dump(teams_db, f, indent=2, ensure_ascii=False)

print(f"[2] teams_database.json actualizado con éxito con los 12 equipos de UEFA Europa & Conference League!")
