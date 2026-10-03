# -*- coding: utf-8 -*-
"""
Enriquece teams_database.json y data_scout_agent.py con las selecciones oficiales
de la jornada UEFA Nations League de HOY SÁBADO 3 DE OCTUBRE DE 2026.
"""

import os
import json

teams_file = os.path.join(os.path.dirname(__file__), "..", "sports_agents", "teams_database.json")
with open(teams_file, "r", encoding="utf-8") as f:
    teams = json.load(f)

new_teams = {
    "España": {
        "fifa_rank": 3,
        "recent_form": ["W", "W", "W", "W", "D", "W", "W", "W"],
        "sequence": [
            {"goals_scored": 4, "goals_conceded": 1, "xg_for": 3.1, "xg_against": 0.7, "corners_for": 8, "corners_against": 3, "shots_total": 20, "shots_on_target": 9, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 69},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.4, "xg_against": 0.9, "corners_for": 7, "corners_against": 3, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 67},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.2, "xg_against": 1.0, "corners_for": 6, "corners_against": 4, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 8, "possession": 65},
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.8, "xg_against": 0.5, "corners_for": 8, "corners_against": 2, "shots_total": 19, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 71}
        ],
        "key_players": [
            {"name": "Lamine Yamal", "position": "Extremo Generacional / Desequilibrio", "avg_shots_p90": 3.4, "avg_sot_p90": 1.7, "shot_creation_actions": 6.8, "goal_prob": 0.48},
            {"name": "Nico Williams", "position": "Extremo Eléctrico", "avg_shots_p90": 3.1, "avg_sot_p90": 1.5, "shot_creation_actions": 5.8, "goal_prob": 0.42},
            {"name": "Álvaro Morata", "position": "Delantero Centro Capitán", "avg_shots_p90": 2.8, "avg_sot_p90": 1.4, "shot_creation_actions": 3.2, "goal_prob": 0.46},
            {"name": "Pedri", "position": "Interior Organizador", "avg_shots_p90": 1.5, "avg_sot_p90": 0.6, "shot_creation_actions": 5.4, "goal_prob": 0.18},
            {"name": "Martín Zubimendi", "position": "Pivote / Posicional", "avg_shots_p90": 1.1, "avg_sot_p90": 0.3, "shot_creation_actions": 3.5, "goal_prob": 0.10}
        ]
    },
    "Chequia": {
        "fifa_rank": 36,
        "recent_form": ["L", "D", "W", "L", "D", "W"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.1, "xg_against": 2.2, "corners_for": 4, "corners_against": 7, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 41},
            {"goals_scored": 3, "goals_conceded": 2, "xg_for": 1.8, "xg_against": 1.6, "corners_for": 5, "corners_against": 5, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 48},
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.8, "xg_against": 1.9, "corners_for": 3, "corners_against": 6, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 38}
        ],
        "key_players": [
            {"name": "Patrik Schick", "position": "Delantero Centro Killer", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 2.6, "goal_prob": 0.38},
            {"name": "Tomas Soucek", "position": "Mediocentro Llegador / Balón Parado", "avg_shots_p90": 2.2, "avg_sot_p90": 1.0, "shot_creation_actions": 3.1, "goal_prob": 0.28},
            {"name": "Vladimir Coufal", "position": "Lateral Derecho / Centros", "avg_shots_p90": 0.9, "avg_sot_p90": 0.2, "shot_creation_actions": 3.8, "goal_prob": 0.06}
        ]
    },
    "Croacia": {
        "fifa_rank": 12,
        "recent_form": ["W", "L", "D", "D", "W", "W"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.6, "xg_against": 0.8, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 56},
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.3, "xg_against": 1.7, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 53},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.4, "xg_against": 1.3, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 54}
        ],
        "key_players": [
            {"name": "Luka Modric", "position": "Organizador / Director de Orquesta", "avg_shots_p90": 1.7, "avg_sot_p90": 0.7, "shot_creation_actions": 5.6, "goal_prob": 0.18},
            {"name": "Mateo Kovacic", "position": "Mediocentro Conducción y Ruptura", "avg_shots_p90": 1.8, "avg_sot_p90": 0.8, "shot_creation_actions": 4.5, "goal_prob": 0.22},
            {"name": "Andrej Kramaric", "position": "Segundo Delantero / Movilidad", "avg_shots_p90": 2.7, "avg_sot_p90": 1.3, "shot_creation_actions": 3.8, "goal_prob": 0.38},
            {"name": "Josko Gvardiol", "position": "Defensa Total / Llegada", "avg_shots_p90": 1.3, "avg_sot_p90": 0.5, "shot_creation_actions": 2.8, "goal_prob": 0.14}
        ]
    },
    "Inglaterra": {
        "fifa_rank": 4,
        "recent_form": ["W", "W", "L", "W", "W", "D"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.2, "xg_against": 0.5, "corners_for": 7, "corners_against": 2, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 8, "possession": 64},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.5, "xg_against": 0.6, "corners_for": 8, "corners_against": 3, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 68},
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.5, "xg_against": 1.8, "corners_for": 6, "corners_against": 5, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 59}
        ],
        "key_players": [
            {"name": "Harry Kane", "position": "Delantero Centro Killer", "avg_shots_p90": 3.8, "avg_sot_p90": 1.9, "shot_creation_actions": 3.8, "goal_prob": 0.62},
            {"name": "Jude Bellingham", "position": "Mediapunta Llegada", "avg_shots_p90": 2.9, "avg_sot_p90": 1.4, "shot_creation_actions": 5.4, "goal_prob": 0.42},
            {"name": "Bukayo Saka", "position": "Extremo Derecho Élite", "avg_shots_p90": 3.2, "avg_sot_p90": 1.6, "shot_creation_actions": 6.2, "goal_prob": 0.46},
            {"name": "Declan Rice", "position": "Pivote / Balón Parado", "avg_shots_p90": 1.6, "avg_sot_p90": 0.6, "shot_creation_actions": 4.2, "goal_prob": 0.16}
        ]
    },
    "Suiza": {
        "fifa_rank": 15,
        "recent_form": ["L", "L", "D", "W", "D", "W"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 4, "xg_for": 1.2, "xg_against": 2.5, "corners_for": 5, "corners_against": 6, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 49},
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.9, "xg_against": 1.7, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 1, "fouls": 14, "possession": 46},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.6, "xg_against": 1.1, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 55}
        ],
        "key_players": [
            {"name": "Granit Xhaka", "position": "Líder / Eje Central", "avg_shots_p90": 1.6, "avg_sot_p90": 0.6, "shot_creation_actions": 4.8, "goal_prob": 0.16},
            {"name": "Breel Embolo", "position": "Delantero Centro Físico", "avg_shots_p90": 2.6, "avg_sot_p90": 1.2, "shot_creation_actions": 2.8, "goal_prob": 0.38},
            {"name": "Dan Ndoye", "position": "Extremo Eléctrico", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 4.2, "goal_prob": 0.28}
        ]
    },
    "Eslovenia": {
        "fifa_rank": 52,
        "recent_form": ["W", "D", "D", "D", "D", "W"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.1, "xg_against": 0.6, "corners_for": 5, "corners_against": 4, "shots_total": 13, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 47},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.2, "xg_against": 1.4, "corners_for": 4, "corners_against": 6, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 44},
            {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.7, "xg_against": 1.6, "corners_for": 3, "corners_against": 7, "shots_total": 7, "shots_on_target": 2, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 38}
        ],
        "key_players": [
            {"name": "Benjamin Sesko", "position": "Delantero Centro Estrella", "avg_shots_p90": 3.2, "avg_sot_p90": 1.6, "shot_creation_actions": 3.1, "goal_prob": 0.48},
            {"name": "Petar Stojanovic", "position": "Carrilero Derecho", "avg_shots_p90": 1.2, "avg_sot_p90": 0.4, "shot_creation_actions": 3.2, "goal_prob": 0.12},
            {"name": "Andraz Sporar", "position": "Segundo Delantero", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 2.2, "goal_prob": 0.26}
        ]
    },
    "Finlandia": {
        "fifa_rank": 63,
        "recent_form": ["L", "L", "D", "W", "L"],
        "sequence": [
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.6, "xg_against": 2.1, "corners_for": 3, "corners_against": 7, "shots_total": 7, "shots_on_target": 2, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 40},
            {"goals_scored": 0, "goals_conceded": 3, "xg_for": 0.8, "xg_against": 2.4, "corners_for": 4, "corners_against": 6, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 42}
        ],
        "key_players": [
            {"name": "Teemu Pukki", "position": "Delantero Referencia", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 2.1, "goal_prob": 0.32},
            {"name": "Joel Pohjanpalo", "position": "Delantero Área", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 1.8, "goal_prob": 0.30}
        ]
    },
    "Albania": {
        "fifa_rank": 67,
        "recent_form": ["L", "W", "L", "D", "L"],
        "sequence": [
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.9, "xg_against": 1.4, "corners_for": 4, "corners_against": 5, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 45},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.7, "xg_against": 1.1, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 52}
        ],
        "key_players": [
            {"name": "Armando Broja", "position": "Delantero Centro Potencia", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 2.3, "goal_prob": 0.34},
            {"name": "Kristjan Asllani", "position": "Pivote Organizador", "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 4.1, "goal_prob": 0.15}
        ]
    },
    "Macedonia del Norte": {
        "fifa_rank": 72,
        "recent_form": ["W", "D", "L", "L", "D"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.8, "xg_against": 0.8, "corners_for": 6, "corners_against": 3, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 51},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.2, "xg_against": 1.3, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 47}
        ],
        "key_players": [
            {"name": "Eljif Elmas", "position": "Mediapunta Creador", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 4.5, "goal_prob": 0.28},
            {"name": "Enis Bardhi", "position": "Mediocentro / Balón Parado", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 4.2, "goal_prob": 0.24}
        ]
    },
    "Escocia": {
        "fifa_rank": 48,
        "recent_form": ["L", "L", "L", "D", "L"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.3, "xg_against": 1.8, "corners_for": 5, "corners_against": 6, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 46},
            {"goals_scored": 2, "goals_conceded": 3, "xg_for": 1.7, "xg_against": 2.4, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 3, "red_cards": 0, "fouls": 12, "possession": 44}
        ],
        "key_players": [
            {"name": "Scott McTominay", "position": "Volante Llegador / Goleador", "avg_shots_p90": 2.7, "avg_sot_p90": 1.3, "shot_creation_actions": 3.2, "goal_prob": 0.38},
            {"name": "John McGinn", "position": "Interior / Presión", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 3.8, "goal_prob": 0.22},
            {"name": "Billy Gilmour", "position": "Pivote Distribuidor", "avg_shots_p90": 0.8, "avg_sot_p90": 0.2, "shot_creation_actions": 4.1, "goal_prob": 0.08}
        ]
    },
    "Estados Unidos": {
        "fifa_rank": 16,
        "recent_form": ["D", "L", "L", "W", "L"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.4, "xg_against": 1.2, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 53},
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.2, "xg_against": 1.7, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 50}
        ],
        "key_players": [
            {"name": "Christian Pulisic", "position": "Extremo / Capitán América", "avg_shots_p90": 3.1, "avg_sot_p90": 1.5, "shot_creation_actions": 5.4, "goal_prob": 0.44},
            {"name": "Folarin Balogun", "position": "Delantero Centro", "avg_shots_p90": 2.5, "avg_sot_p90": 1.2, "shot_creation_actions": 2.2, "goal_prob": 0.36},
            {"name": "Weston McKennie", "position": "Interior Llegador", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 3.4, "goal_prob": 0.20}
        ]
    },
    "México": {
        "fifa_rank": 17,
        "recent_form": ["D", "W", "D", "W", "L"],
        "sequence": [
            {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.9, "xg_against": 1.0, "corners_for": 4, "corners_against": 4, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 51},
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.3, "xg_against": 0.6, "corners_for": 7, "corners_against": 3, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 60}
        ],
        "key_players": [
            {"name": "Santiago Giménez", "position": "Delantero Centro Killer", "avg_shots_p90": 2.9, "avg_sot_p90": 1.4, "shot_creation_actions": 2.6, "goal_prob": 0.42},
            {"name": "Orbelín Pineda", "position": "Mediapunta Dinámico", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 4.1, "goal_prob": 0.22},
            {"name": "Edson Álvarez", "position": "Pivote / Jerarquía", "avg_shots_p90": 1.2, "avg_sot_p90": 0.4, "shot_creation_actions": 2.8, "goal_prob": 0.12}
        ]
    }
}

teams.update(new_teams)

with open(teams_file, "w", encoding="utf-8") as f:
    json.dump(teams, f, ensure_ascii=False, indent=2)

print(f"teams_database.json actualizado con éxito con {len(new_teams)} nuevas selecciones oficiales de Fecha FIFA.")
