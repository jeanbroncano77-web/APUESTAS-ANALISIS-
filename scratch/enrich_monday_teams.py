import json

with open("sports_agents/teams_database.json", "r", encoding="utf-8") as f:
    teams = json.load(f)

new_teams = {
    "Levante": {
        "fifa_rank": 48,
        "recent_form": ["W", "D", "W", "L", "D", "W", "D"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.4, "xg_against": 1.1, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 49},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.1, "xg_against": 1.3, "corners_for": 4, "corners_against": 6, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 1, "red_cards": 0, "fouls": 13, "possession": 46},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.8, "xg_against": 0.8, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 53},
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.7, "xg_against": 1.9, "corners_for": 3, "corners_against": 7, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 42},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.3, "xg_against": 1.2, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 48}
        ],
        "key_players": [
            {"name": "José Luis Morales", "position": "Delantero Centro", "avg_shots_p90": 2.6, "avg_sot_p90": 1.2, "shot_creation_actions": 3.4, "goal_prob": 0.38},
            {"name": "Carlos Álvarez", "position": "Mediapunta / Extremo", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 4.5, "goal_prob": 0.24},
            {"name": "Roger Brugué", "position": "Extremo Derecho", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 2.8, "goal_prob": 0.20},
            {"name": "Oriol Rey", "position": "Pivote Defensivo", "avg_shots_p90": 0.8, "avg_sot_p90": 0.2, "shot_creation_actions": 2.1, "goal_prob": 0.05},
            {"name": "Andrés García", "position": "Lateral Ofensivo", "avg_shots_p90": 1.1, "avg_sot_p90": 0.3, "shot_creation_actions": 2.5, "goal_prob": 0.08}
        ]
    },
    "Sevilla": {
        "fifa_rank": 26,
        "recent_form": ["W", "W", "D", "L", "W", "D", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.8, "xg_against": 1.0, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 56},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.5, "xg_against": 0.7, "corners_for": 7, "corners_against": 3, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 59},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.2, "xg_against": 1.1, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 52},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.9, "xg_against": 1.4, "corners_for": 4, "corners_against": 6, "shots_total": 10, "shots_on_target": 2, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 51},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.9, "xg_against": 0.9, "corners_for": 6, "corners_against": 4, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 58}
        ],
        "key_players": [
            {"name": "Dodi Lukébakio", "position": "Extremo Derecho", "avg_shots_p90": 3.1, "avg_sot_p90": 1.4, "shot_creation_actions": 4.8, "goal_prob": 0.42},
            {"name": "Isaac Romero", "position": "Delantero Centro", "avg_shots_p90": 2.7, "avg_sot_p90": 1.2, "shot_creation_actions": 3.2, "goal_prob": 0.36},
            {"name": "Peque Fernández", "position": "Mediapunta", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 3.9, "goal_prob": 0.22},
            {"name": "Lucien Agoumé", "position": "Pivote Organizador", "avg_shots_p90": 0.9, "avg_sot_p90": 0.3, "shot_creation_actions": 2.6, "goal_prob": 0.08},
            {"name": "Saúl Ñíguez", "position": "Interior Mixto", "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 2.9, "goal_prob": 0.15}
        ]
    },
    "Coventry City": {
        "fifa_rank": 55,
        "recent_form": ["L", "W", "D", "L", "D", "L", "W"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.1, "xg_against": 1.8, "corners_for": 4, "corners_against": 7, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 44},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.6, "xg_against": 1.2, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 48},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.0, "xg_against": 1.4, "corners_for": 3, "corners_against": 6, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 45},
            {"goals_scored": 0, "goals_conceded": 3, "xg_for": 0.6, "xg_against": 2.4, "corners_for": 2, "corners_against": 8, "shots_total": 7, "shots_on_target": 1, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 39},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.2, "xg_against": 1.3, "corners_for": 4, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 46}
        ],
        "key_players": [
            {"name": "Haji Wright", "position": "Delantero / Extremo", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 3.1, "goal_prob": 0.35},
            {"name": "Ellis Simms", "position": "Delantero Centro", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 2.6, "goal_prob": 0.32},
            {"name": "Jack Rudoni", "position": "Mediapunta", "avg_shots_p90": 1.7, "avg_sot_p90": 0.6, "shot_creation_actions": 3.8, "goal_prob": 0.18},
            {"name": "Milan van Ewijk", "position": "Carrilero Derecho", "avg_shots_p90": 1.2, "avg_sot_p90": 0.4, "shot_creation_actions": 2.9, "goal_prob": 0.10},
            {"name": "Josh Eccles", "position": "Centrocampista", "avg_shots_p90": 1.0, "avg_sot_p90": 0.3, "shot_creation_actions": 2.4, "goal_prob": 0.08}
        ]
    },
    "Newcastle": {
        "fifa_rank": 14,
        "recent_form": ["W", "W", "D", "W", "W", "L", "W"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.5, "xg_against": 0.9, "corners_for": 7, "corners_against": 3, "shots_total": 18, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 60},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.1, "xg_against": 0.6, "corners_for": 8, "corners_against": 2, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 62},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.7, "xg_against": 1.2, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 55},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.0, "xg_against": 1.1, "corners_for": 7, "corners_against": 4, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 58},
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.8, "xg_against": 0.5, "corners_for": 9, "corners_against": 2, "shots_total": 20, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 8, "possession": 64}
        ],
        "key_players": [
            {"name": "Alexander Isak", "position": "Delantero Centro", "avg_shots_p90": 3.6, "avg_sot_p90": 1.8, "shot_creation_actions": 4.5, "goal_prob": 0.55},
            {"name": "Anthony Gordon", "position": "Extremo Izquierdo", "avg_shots_p90": 2.9, "avg_sot_p90": 1.3, "shot_creation_actions": 5.2, "goal_prob": 0.38},
            {"name": "Bruno Guimarães", "position": "Pivote Creativo", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 4.6, "goal_prob": 0.20},
            {"name": "Sandro Tonali", "position": "Interior Box-to-Box", "avg_shots_p90": 1.6, "avg_sot_p90": 0.6, "shot_creation_actions": 3.8, "goal_prob": 0.16},
            {"name": "Harvey Barnes", "position": "Extremo Derecho", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 3.7, "goal_prob": 0.30}
        ]
    },
    "Atalanta": {
        "fifa_rank": 15,
        "recent_form": ["W", "W", "W", "D", "W", "W", "L"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.6, "xg_against": 0.6, "corners_for": 8, "corners_against": 2, "shots_total": 19, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 62},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.2, "xg_against": 0.9, "corners_for": 7, "corners_against": 3, "shots_total": 17, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 59},
            {"goals_scored": 4, "goals_conceded": 1, "xg_for": 3.1, "xg_against": 1.0, "corners_for": 9, "corners_against": 3, "shots_total": 21, "shots_on_target": 9, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 65},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.8, "xg_against": 1.1, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 57},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.0, "xg_against": 0.7, "corners_for": 7, "corners_against": 2, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 61}
        ],
        "key_players": [
            {"name": "Mateo Retegui", "position": "Delantero Centro", "avg_shots_p90": 3.5, "avg_sot_p90": 1.7, "shot_creation_actions": 3.8, "goal_prob": 0.52},
            {"name": "Ademola Lookman", "position": "Segundo Delantero", "avg_shots_p90": 3.2, "avg_sot_p90": 1.5, "shot_creation_actions": 5.4, "goal_prob": 0.44},
            {"name": "Charles De Ketelaere", "position": "Mediapunta", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 4.9, "goal_prob": 0.30},
            {"name": "Éderson", "position": "Centrocampista Total", "avg_shots_p90": 1.7, "avg_sot_p90": 0.6, "shot_creation_actions": 3.5, "goal_prob": 0.16},
            {"name": "Mario Pašalić", "position": "Llegador", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 3.1, "goal_prob": 0.25}
        ]
    },
    "Venezia": {
        "fifa_rank": 58,
        "recent_form": ["L", "L", "D", "W", "L", "D", "L"],
        "sequence": [
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.7, "xg_against": 2.2, "corners_for": 3, "corners_against": 8, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 38},
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.0, "xg_against": 1.9, "corners_for": 4, "corners_against": 6, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 42},
            {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.6, "xg_against": 1.3, "corners_for": 2, "corners_against": 7, "shots_total": 7, "shots_on_target": 1, "yellow_cards": 2, "red_cards": 0, "fouls": 15, "possession": 36},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.5, "xg_against": 1.2, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 45},
            {"goals_scored": 0, "goals_conceded": 3, "xg_for": 0.5, "xg_against": 2.5, "corners_for": 3, "corners_against": 8, "shots_total": 6, "shots_on_target": 1, "yellow_cards": 3, "red_cards": 0, "fouls": 16, "possession": 35}
        ],
        "key_players": [
            {"name": "Joel Pohjanpalo", "position": "Delantero Centro", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 2.5, "goal_prob": 0.32},
            {"name": "Gaetano Oristanio", "position": "Segundo Delantero", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 3.7, "goal_prob": 0.22},
            {"name": "Gianluca Busio", "position": "Centrocampista Creativo", "avg_shots_p90": 1.5, "avg_sot_p90": 0.5, "shot_creation_actions": 3.2, "goal_prob": 0.14},
            {"name": "Hans Nicolussi Caviglia", "position": "Pivote", "avg_shots_p90": 1.1, "avg_sot_p90": 0.3, "shot_creation_actions": 2.8, "goal_prob": 0.09},
            {"name": "Mikael Ellertsson", "position": "Interior Mixto", "avg_shots_p90": 1.0, "avg_sot_p90": 0.3, "shot_creation_actions": 2.2, "goal_prob": 0.08}
        ]
    },
    "Torino": {
        "fifa_rank": 35,
        "recent_form": ["W", "D", "L", "W", "D", "W", "L"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.3, "xg_against": 0.8, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 51},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.6, "xg_against": 1.1, "corners_for": 6, "corners_against": 5, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 53},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.9, "xg_against": 1.3, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 48},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.2, "xg_against": 1.0, "corners_for": 5, "corners_against": 4, "shots_total": 11, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 50},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.7, "xg_against": 0.7, "corners_for": 6, "corners_against": 3, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 54}
        ],
        "key_players": [
            {"name": "Ché Adams", "position": "Delantero Centro", "avg_shots_p90": 2.7, "avg_sot_p90": 1.2, "shot_creation_actions": 3.1, "goal_prob": 0.36},
            {"name": "Antonio Sanabria", "position": "Delantero Centro", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 2.8, "goal_prob": 0.32},
            {"name": "Samuele Ricci", "position": "Pivote Organizador", "avg_shots_p90": 1.2, "avg_sot_p90": 0.4, "shot_creation_actions": 4.1, "goal_prob": 0.12},
            {"name": "Nikola Vlašić", "position": "Mediapunta", "avg_shots_p90": 2.1, "avg_sot_p90": 0.8, "shot_creation_actions": 4.5, "goal_prob": 0.24},
            {"name": "Valentino Lazaro", "position": "Carrilero Derecho", "avg_shots_p90": 1.1, "avg_sot_p90": 0.3, "shot_creation_actions": 3.0, "goal_prob": 0.08}
        ]
    },
    "Udinese": {
        "fifa_rank": 38,
        "recent_form": ["L", "W", "D", "L", "W", "L", "D"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.1, "xg_against": 1.2, "corners_for": 4, "corners_against": 5, "shots_total": 11, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 47},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.5, "xg_against": 1.3, "corners_for": 5, "corners_against": 6, "shots_total": 13, "shots_on_target": 4, "yellow_cards": 1, "red_cards": 0, "fouls": 12, "possession": 49},
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.8, "xg_against": 1.8, "corners_for": 3, "corners_against": 7, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 43},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.2, "xg_against": 0.9, "corners_for": 5, "corners_against": 4, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 48},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.9, "xg_against": 1.4, "corners_for": 4, "corners_against": 5, "shots_total": 9, "shots_on_target": 2, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 45}
        ],
        "key_players": [
            {"name": "Lorenzo Lucca", "position": "Delantero Referencia", "avg_shots_p90": 2.8, "avg_sot_p90": 1.2, "shot_creation_actions": 2.9, "goal_prob": 0.38},
            {"name": "Florian Thauvin", "position": "Extremo / Segundo Delantero", "avg_shots_p90": 2.6, "avg_sot_p90": 1.1, "shot_creation_actions": 4.8, "goal_prob": 0.34},
            {"name": "Sandi Lovrić", "position": "Centrocampista Llegador", "avg_shots_p90": 1.6, "avg_sot_p90": 0.6, "shot_creation_actions": 3.4, "goal_prob": 0.18},
            {"name": "Jesper Karlström", "position": "Pivote Defensivo", "avg_shots_p90": 0.7, "avg_sot_p90": 0.2, "shot_creation_actions": 2.1, "goal_prob": 0.05},
            {"name": "Kingsley Ehizibue", "position": "Carrilero Físico", "avg_shots_p90": 0.9, "avg_sot_p90": 0.3, "shot_creation_actions": 2.3, "goal_prob": 0.06}
        ]
    }
}

teams.update(new_teams)

with open("sports_agents/teams_database.json", "w", encoding="utf-8") as f:
    json.dump(teams, f, ensure_ascii=False, indent=2)

print("8 nuevos equipos incorporados con éxito a teams_database.json.")
