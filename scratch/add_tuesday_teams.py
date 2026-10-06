# -*- coding: utf-8 -*-
import json

db_path = "sports_agents/teams_database.json"
with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

# Bielorrusia
db["Bielorrusia"] = {
    "fifa_rank": 98,
    "recent_form": ["L", "D", "W", "L", "D", "L"],
    "sequence": [
        {
            "goals_scored": 0, "goals_conceded": 2, "xg_for": 0.65, "xg_against": 1.70,
            "corners_for": 3, "corners_against": 6, "shots_total": 7, "shots_on_target": 2,
            "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 41
        },
        {
            "goals_scored": 1, "goals_conceded": 1, "xg_for": 1.10, "xg_against": 1.25,
            "corners_for": 4, "corners_against": 5, "shots_total": 9, "shots_on_target": 3,
            "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 44
        },
        {
            "goals_scored": 1, "goals_conceded": 0, "xg_for": 1.20, "xg_against": 0.80,
            "corners_for": 5, "corners_against": 4, "shots_total": 11, "shots_on_target": 4,
            "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 48
        }
    ],
    "key_players": [
        {
            "name": "Max Ebong",
            "position": "Volante Central Astana",
            "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 2.8, "goal_prob": 0.16
        },
        {
            "name": "Vitali Lisakovich",
            "position": "Delantero Centro Rubin Kazan",
            "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 2.2, "goal_prob": 0.28
        }
    ]
}

# San Marino
db["San Marino"] = {
    "fifa_rank": 210,
    "recent_form": ["L", "L", "W", "L", "L", "L"],
    "sequence": [
        {
            "goals_scored": 0, "goals_conceded": 3, "xg_for": 0.25, "xg_against": 2.80,
            "corners_for": 1, "corners_against": 9, "shots_total": 4, "shots_on_target": 1,
            "yellow_cards": 3, "red_cards": 0, "fouls": 16, "possession": 28
        },
        {
            "goals_scored": 1, "goals_conceded": 0, "xg_for": 0.95, "xg_against": 0.85,
            "corners_for": 3, "corners_against": 5, "shots_total": 6, "shots_on_target": 2,
            "yellow_cards": 4, "red_cards": 0, "fouls": 18, "possession": 35
        },
        {
            "goals_scored": 0, "goals_conceded": 2, "xg_for": 0.35, "xg_against": 2.10,
            "corners_for": 2, "corners_against": 7, "shots_total": 5, "shots_on_target": 1,
            "yellow_cards": 2, "red_cards": 0, "fouls": 15, "possession": 31
        }
    ],
    "key_players": [
        {
            "name": "Nicko Sensoli",
            "position": "Extremo Histórico San Marino",
            "avg_shots_p90": 1.2, "avg_sot_p90": 0.4, "shot_creation_actions": 1.5, "goal_prob": 0.12
        },
        {
            "name": "Nicola Nanni",
            "position": "Delantero Centro Olbia",
            "avg_shots_p90": 1.5, "avg_sot_p90": 0.5, "shot_creation_actions": 1.8, "goal_prob": 0.15
        }
    ]
}

with open(db_path, "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("San Marino y Bielorrusia agregadas exitosamente a teams_database.json.")
