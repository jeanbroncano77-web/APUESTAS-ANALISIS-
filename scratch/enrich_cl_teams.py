import json
import os

teams_path = "sports_agents/teams_database.json"
with open(teams_path, "r", encoding="utf-8") as f:
    teams_db = json.load(f)

new_teams = {
    "Galatasaray": {
        "fifa_rank": 35,
        "recent_form": ["W", "W", "D", "W", "W", "W", "D", "W"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.2, "xg_against": 1.1, "corners_for": 7, "corners_against": 4, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 58},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.9, "xg_against": 0.8, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 11, "possession": 56},
            {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.8, "xg_against": 1.5, "corners_for": 5, "corners_against": 5, "shots_total": 13, "shots_on_target": 6, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 52},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.6, "xg_against": 0.9, "corners_for": 6, "corners_against": 4, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 55},
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.4, "xg_against": 1.0, "corners_for": 8, "corners_against": 3, "shots_total": 17, "shots_on_target": 8, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 60}
        ],
        "key_players": [
            {"name": "Victor Osimhen", "position": "Delantero Centro", "avg_shots_p90": 3.9, "avg_sot_p90": 1.8, "shot_creation_actions": 4.2, "goal_prob": 0.52},
            {"name": "Mauro Icardi", "position": "Delantero Centro", "avg_shots_p90": 3.1, "avg_sot_p90": 1.5, "shot_creation_actions": 3.5, "goal_prob": 0.45},
            {"name": "Barış Alper Yılmaz", "position": "Extremo Ofensivo", "avg_shots_p90": 2.6, "avg_sot_p90": 1.1, "shot_creation_actions": 4.0, "goal_prob": 0.32},
            {"name": "Lucas Torreira", "position": "Pivote Defensivo", "avg_shots_p90": 1.1, "avg_sot_p90": 0.4, "shot_creation_actions": 3.1, "goal_prob": 0.12},
            {"name": "Dries Mertens", "position": "Mediapunta", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 4.8, "goal_prob": 0.28}
        ]
    },
    "Lille": {
        "fifa_rank": 28,
        "recent_form": ["W", "D", "W", "L", "W", "W", "D", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.7, "xg_against": 1.2, "corners_for": 5, "corners_against": 5, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 52},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.5, "xg_against": 0.7, "corners_for": 6, "corners_against": 3, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 55},
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.1, "xg_against": 1.0, "corners_for": 7, "corners_against": 4, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 54},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 1.1, "xg_against": 1.3, "corners_for": 4, "corners_against": 6, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 48},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.8, "xg_against": 0.8, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 56}
        ],
        "key_players": [
            {"name": "Jonathan David", "position": "Delantero Centro", "avg_shots_p90": 3.4, "avg_sot_p90": 1.7, "shot_creation_actions": 4.5, "goal_prob": 0.48},
            {"name": "Edon Zhegrova", "position": "Extremo Derecho", "avg_shots_p90": 2.9, "avg_sot_p90": 1.2, "shot_creation_actions": 5.8, "goal_prob": 0.35},
            {"name": "Angel Gomes", "position": "Mediapunta", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 5.2, "goal_prob": 0.22},
            {"name": "Benjamin André", "position": "Pivote", "avg_shots_p90": 0.9, "avg_sot_p90": 0.3, "shot_creation_actions": 2.8, "goal_prob": 0.08},
            {"name": "Osame Sahraoui", "position": "Extremo Izquierdo", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 4.1, "goal_prob": 0.25}
        ]
    },
    "Atlético de Madrid": {
        "fifa_rank": 10,
        "recent_form": ["W", "W", "D", "W", "W", "D", "W", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.1, "xg_against": 0.6, "corners_for": 7, "corners_against": 3, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 57},
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.4, "xg_against": 0.9, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 54},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.8, "xg_against": 0.8, "corners_for": 8, "corners_against": 3, "shots_total": 17, "shots_on_target": 6, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 59},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.0, "xg_against": 0.5, "corners_for": 7, "corners_against": 2, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 55},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.7, "xg_against": 0.7, "corners_for": 5, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 53}
        ],
        "key_players": [
            {"name": "Julián Álvarez", "position": "Delantero Centro", "avg_shots_p90": 3.7, "avg_sot_p90": 1.8, "shot_creation_actions": 5.2, "goal_prob": 0.52},
            {"name": "Antoine Griezmann", "position": "Mediapunta / Segundo Delantero", "avg_shots_p90": 2.9, "avg_sot_p90": 1.4, "shot_creation_actions": 6.8, "goal_prob": 0.44},
            {"name": "Alexander Sørloth", "position": "Delantero Centro", "avg_shots_p90": 3.2, "avg_sot_p90": 1.5, "shot_creation_actions": 3.4, "goal_prob": 0.46},
            {"name": "Rodrigo De Paul", "position": "Centrocampista", "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 4.5, "goal_prob": 0.15},
            {"name": "Marcos Llorente", "position": "Carrilero / Interior", "avg_shots_p90": 1.6, "avg_sot_p90": 0.7, "shot_creation_actions": 3.8, "goal_prob": 0.20}
        ]
    },
    "Manchester United": {
        "fifa_rank": 18,
        "recent_form": ["W", "D", "L", "W", "W", "D", "L", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.8, "xg_against": 1.3, "corners_for": 6, "corners_against": 5, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 53},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.5, "xg_against": 1.4, "corners_for": 5, "corners_against": 6, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 50},
            {"goals_scored": 3, "goals_conceded": 2, "xg_for": 2.2, "xg_against": 1.8, "corners_for": 7, "corners_against": 5, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 55},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 1.2, "xg_against": 1.5, "corners_for": 5, "corners_against": 6, "shots_total": 11, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 52},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.9, "xg_against": 0.9, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 56}
        ],
        "key_players": [
            {"name": "Bruno Fernandes", "position": "Mediapunta Creativo", "avg_shots_p90": 3.3, "avg_sot_p90": 1.3, "shot_creation_actions": 7.1, "goal_prob": 0.38},
            {"name": "Rasmus Højlund", "position": "Delantero Centro", "avg_shots_p90": 2.7, "avg_sot_p90": 1.4, "shot_creation_actions": 3.2, "goal_prob": 0.42},
            {"name": "Alejandro Garnacho", "position": "Extremo Vertical", "avg_shots_p90": 3.5, "avg_sot_p90": 1.5, "shot_creation_actions": 5.4, "goal_prob": 0.40},
            {"name": "Marcus Rashford", "position": "Extremo / Delantero", "avg_shots_p90": 2.9, "avg_sot_p90": 1.2, "shot_creation_actions": 4.6, "goal_prob": 0.36},
            {"name": "Kobbie Mainoo", "position": "Centrocampista", "avg_shots_p90": 1.2, "avg_sot_p90": 0.4, "shot_creation_actions": 3.8, "goal_prob": 0.15}
        ]
    },
    "Club Brugge": {
        "fifa_rank": 32,
        "recent_form": ["W", "W", "D", "W", "D", "L", "W", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.8, "xg_against": 1.1, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 56},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.4, "xg_against": 1.3, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 53},
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.2, "xg_against": 0.7, "corners_for": 7, "corners_against": 3, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 60},
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.3, "xg_against": 1.6, "corners_for": 4, "corners_against": 6, "shots_total": 11, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 49},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.9, "xg_against": 0.8, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 55}
        ],
        "key_players": [
            {"name": "Christos Tzolis", "position": "Extremo Ofensivo", "avg_shots_p90": 3.1, "avg_sot_p90": 1.4, "shot_creation_actions": 4.8, "goal_prob": 0.40},
            {"name": "Ferran Jutglà", "position": "Delantero Centro", "avg_shots_p90": 2.8, "avg_sot_p90": 1.2, "shot_creation_actions": 3.5, "goal_prob": 0.38},
            {"name": "Hans Vanaken", "position": "Capitán y Mediapunta", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 5.9, "goal_prob": 0.30},
            {"name": "Maxim De Cuyper", "position": "Lateral Ofensivo", "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 4.2, "goal_prob": 0.16},
            {"name": "Raphael Onyedika", "position": "Pivote", "avg_shots_p90": 0.9, "avg_sot_p90": 0.3, "shot_creation_actions": 2.5, "goal_prob": 0.08}
        ]
    },
    "Viking FK": {
        "fifa_rank": 80,
        "recent_form": ["W", "D", "W", "W", "L", "W", "D", "L"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.2, "xg_against": 2.1, "corners_for": 4, "corners_against": 7, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 42},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.6, "xg_against": 1.4, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 48},
            {"goals_scored": 0, "goals_conceded": 3, "xg_for": 0.8, "xg_against": 2.8, "corners_for": 3, "corners_against": 9, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 36},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.3, "xg_against": 1.5, "corners_for": 4, "corners_against": 6, "shots_total": 11, "shots_on_target": 3, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 45},
            {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.5, "xg_against": 1.9, "corners_for": 5, "corners_against": 6, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 44}
        ],
        "key_players": [
            {"name": "Zlatko Tripić", "position": "Extremo / Capitán", "avg_shots_p90": 2.8, "avg_sot_p90": 1.2, "shot_creation_actions": 4.6, "goal_prob": 0.35},
            {"name": "Lars-Jørgen Salvesen", "position": "Delantero Centro", "avg_shots_p90": 2.5, "avg_sot_p90": 1.0, "shot_creation_actions": 3.0, "goal_prob": 0.32},
            {"name": "Joe Bell", "position": "Centrocampista", "avg_shots_p90": 1.1, "avg_sot_p90": 0.4, "shot_creation_actions": 3.8, "goal_prob": 0.12},
            {"name": "Simen Kvia-Egeskog", "position": "Mediapunta", "avg_shots_p90": 1.9, "avg_sot_p90": 0.7, "shot_creation_actions": 3.5, "goal_prob": 0.22},
            {"name": "Sondre Langås", "position": "Defensa Central", "avg_shots_p90": 0.6, "avg_sot_p90": 0.2, "shot_creation_actions": 1.2, "goal_prob": 0.06}
        ]
    }
}

for name, data in new_teams.items():
    teams_db[name] = data

with open(teams_path, "w", encoding="utf-8") as f:
    json.dump(teams_db, f, ensure_ascii=False, indent=2)

print(f"Successfully added {len(new_teams)} teams to {teams_path}!")
