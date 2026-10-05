# -*- coding: utf-8 -*-
import json
import os

db_path = "sports_agents/teams_database.json"
with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

# 1. UCRANIA (FIFA Rank ~24, Liga B, Serhiy Rebrov)
db["Ucrania"] = {
    "fifa_rank": 24,
    "recent_form": ["W", "D", "L", "W", "W", "D", "L", "W"],
    "sequence": [
        {
            "goals_scored": 2, "goals_conceded": 1, "xg_for": 1.85, "xg_against": 1.10,
            "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 6,
            "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 53
        },
        {
            "goals_scored": 1, "goals_conceded": 1, "xg_for": 1.40, "xg_against": 1.25,
            "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 4,
            "yellow_cards": 3, "red_cards": 0, "fouls": 12, "possession": 49
        },
        {
            "goals_scored": 3, "goals_conceded": 1, "xg_for": 2.10, "xg_against": 0.95,
            "corners_for": 7, "corners_against": 3, "shots_total": 16, "shots_on_target": 7,
            "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 58
        },
        {
            "goals_scored": 0, "goals_conceded": 1, "xg_for": 0.90, "xg_against": 1.30,
            "corners_for": 4, "corners_against": 6, "shots_total": 9, "shots_on_target": 2,
            "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 46
        },
        {
            "goals_scored": 2, "goals_conceded": 0, "xg_for": 1.75, "xg_against": 0.70,
            "corners_for": 5, "corners_against": 3, "shots_total": 13, "shots_on_target": 5,
            "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 54
        },
        {
            "goals_scored": 1, "goals_conceded": 2, "xg_for": 1.20, "xg_against": 1.65,
            "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3,
            "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 48
        }
    ],
    "key_players": [
        {
            "name": "Artem Dovbyk",
            "position": "Delantero Centro AS Roma / Pichichi",
            "avg_shots_p90": 3.1,
            "avg_sot_p90": 1.5,
            "shot_creation_actions": 3.2,
            "goal_prob": 0.42
        },
        {
            "name": "Mykhailo Mudryk",
            "position": "Extremo Eléctrico Chelsea",
            "avg_shots_p90": 2.4,
            "avg_sot_p90": 1.1,
            "shot_creation_actions": 4.5,
            "goal_prob": 0.28
        },
        {
            "name": "Viktor Tsygankov",
            "position": "Extremo / Creador Girona",
            "avg_shots_p90": 2.2,
            "avg_sot_p90": 0.9,
            "shot_creation_actions": 5.1,
            "goal_prob": 0.26
        },
        {
            "name": "Georgiy Sudakov",
            "position": "Volante Ofensivo Shakhtar",
            "avg_shots_p90": 1.8,
            "avg_sot_p90": 0.8,
            "shot_creation_actions": 4.8,
            "goal_prob": 0.20
        }
    ]
}

# 2. IRLANDA DEL NORTE (FIFA Rank ~71, Liga B, Michael O'Neill)
db["Irlanda del Norte"] = {
    "fifa_rank": 71,
    "recent_form": ["W", "L", "D", "W", "L", "D"],
    "sequence": [
        {
            "goals_scored": 1, "goals_conceded": 0, "xg_for": 1.10, "xg_against": 0.85,
            "corners_for": 4, "corners_against": 5, "shots_total": 9, "shots_on_target": 3,
            "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 42
        },
        {
            "goals_scored": 0, "goals_conceded": 2, "xg_for": 0.70, "xg_against": 1.70,
            "corners_for": 3, "corners_against": 7, "shots_total": 7, "shots_on_target": 2,
            "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 38
        },
        {
            "goals_scored": 1, "goals_conceded": 1, "xg_for": 1.05, "xg_against": 1.20,
            "corners_for": 4, "corners_against": 4, "shots_total": 8, "shots_on_target": 3,
            "yellow_cards": 1, "red_cards": 0, "fouls": 12, "possession": 44
        },
        {
            "goals_scored": 2, "goals_conceded": 0, "xg_for": 1.50, "xg_against": 0.65,
            "corners_for": 6, "corners_against": 3, "shots_total": 11, "shots_on_target": 4,
            "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 47
        },
        {
            "goals_scored": 0, "goals_conceded": 1, "xg_for": 0.65, "xg_against": 1.35,
            "corners_for": 2, "corners_against": 6, "shots_total": 6, "shots_on_target": 1,
            "yellow_cards": 3, "red_cards": 0, "fouls": 16, "possession": 36
        }
    ],
    "key_players": [
        {
            "name": "Isaac Price",
            "position": "Volante de Llegada Standard Liege",
            "avg_shots_p90": 1.9,
            "avg_sot_p90": 0.8,
            "shot_creation_actions": 2.7,
            "goal_prob": 0.22
        },
        {
            "name": "Dion Charles",
            "position": "Delantero Centro Bolton",
            "avg_shots_p90": 2.1,
            "avg_sot_p90": 0.9,
            "shot_creation_actions": 2.1,
            "goal_prob": 0.26
        },
        {
            "name": "Conor Bradley",
            "position": "Lateral Derecho Liverpool",
            "avg_shots_p90": 1.3,
            "avg_sot_p90": 0.5,
            "shot_creation_actions": 3.6,
            "goal_prob": 0.14
        },
        {
            "name": "Shea Charles",
            "position": "Pivote Southampton",
            "avg_shots_p90": 0.8,
            "avg_sot_p90": 0.3,
            "shot_creation_actions": 1.9,
            "goal_prob": 0.08
        }
    ]
}

with open(db_path, "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("Ucrania e Irlanda del Norte agregadas exitosamente a teams_database.json.")
