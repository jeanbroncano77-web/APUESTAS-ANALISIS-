import json

db_path = "sports_agents/teams_database.json"
with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

# Independiente del Valle
db["Independiente del Valle"] = {
    "fifa_rank": 18,
    "recent_form": ["W", "W", "W", "D", "W", "W", "D", "W"],
    "sequence": [
        {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.1, "xg_against": 0.6, "corners_for": 7, "corners_against": 3, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 9, "possession": 62},
        {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.4, "xg_against": 0.8, "corners_for": 8, "corners_against": 4, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 65},
        {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.7, "xg_against": 0.9, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 59},
        {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.9, "xg_against": 0.7, "corners_for": 7, "corners_against": 2, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 8, "possession": 63},
        {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.0, "xg_against": 1.0, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 3, "red_cards": 0, "fouls": 12, "possession": 60}
    ],
    "key_players": [
        {"name": "Kendry Páez", "position": "Mediapunta / Creador", "avg_shots_p90": 2.9, "avg_sot_p90": 1.4, "shot_creation_actions": 5.2, "goal_prob": 0.42},
        {"name": "Michael Hoyos", "position": "Delantero Centro", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 3.4, "goal_prob": 0.45},
        {"name": "Júnior Sornoza", "position": "Organizador / 10", "avg_shots_p90": 2.2, "avg_sot_p90": 1.1, "shot_creation_actions": 5.8, "goal_prob": 0.35},
        {"name": "Renato Ibarra", "position": "Extremo Ofensivo", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 4.1, "goal_prob": 0.30}
    ]
}

# Macará
db["Macará"] = {
    "fifa_rank": 42,
    "recent_form": ["D", "L", "D", "W", "L", "D", "W", "L"],
    "sequence": [
        {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.1, "xg_against": 1.3, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 47},
        {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.8, "xg_against": 1.8, "corners_for": 3, "corners_against": 7, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 4, "red_cards": 0, "fouls": 16, "possession": 42},
        {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.4, "xg_against": 1.1, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 51},
        {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.9, "xg_against": 1.0, "corners_for": 4, "corners_against": 4, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 46}
    ],
    "key_players": [
        {"name": "Facundo Pons", "position": "Delantero Centro", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 2.8, "goal_prob": 0.35},
        {"name": "Janpol Morales", "position": "Extremo", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 3.5, "goal_prob": 0.28},
        {"name": "Emiliano Romero", "position": "Volante Central", "avg_shots_p90": 1.1, "avg_sot_p90": 0.3, "shot_creation_actions": 2.2, "goal_prob": 0.10}
    ]
}
db["Macara"] = db["Macará"]

# Orense SC
db["Orense SC"] = {
    "fifa_rank": 45,
    "recent_form": ["L", "D", "L", "W", "D", "L", "D", "L"],
    "sequence": [
        {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.7, "xg_against": 1.8, "corners_for": 3, "corners_against": 6, "shots_total": 7, "shots_on_target": 2, "yellow_cards": 4, "red_cards": 0, "fouls": 15, "possession": 42},
        {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.0, "xg_against": 1.2, "corners_for": 4, "corners_against": 5, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 45},
        {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.8, "xg_against": 1.5, "corners_for": 3, "corners_against": 7, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 43},
        {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.2, "xg_against": 0.9, "corners_for": 5, "corners_against": 4, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 48}
    ],
    "key_players": [
        {"name": "Miguel Parrales", "position": "Delantero Centro", "avg_shots_p90": 2.6, "avg_sot_p90": 1.2, "shot_creation_actions": 2.7, "goal_prob": 0.38},
        {"name": "Robert Burbano", "position": "Extremo Rápido", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 3.6, "goal_prob": 0.22},
        {"name": "Agustín Herrera", "position": "Segundo Punta", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 2.9, "goal_prob": 0.25}
    ]
}
db["Orense"] = db["Orense SC"]

with open(db_path, "w", encoding="utf-8") as f_w:
    json.dump(db, f_w, ensure_ascii=False, indent=2)

print("Teams database enriched with complete sequence and key players for LigaPro teams.")
