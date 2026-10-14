import json

teams_path = "sports_agents/teams_database.json"
with open(teams_path, "r", encoding="utf-8") as f:
    teams_db = json.load(f)

# Also ensure "Roma" maps to "AS Roma"
if "AS Roma" in teams_db:
    teams_db["Roma"] = teams_db["AS Roma"]

new_teams = {
    "Paris Saint-Germain": {
        "fifa_rank": 6,
        "recent_form": ["W", "W", "W", "D", "W", "W", "D", "W"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.5, "xg_against": 0.9, "corners_for": 7, "corners_against": 4, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 64},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.1, "xg_against": 0.6, "corners_for": 6, "corners_against": 3, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 62},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.9, "xg_against": 1.2, "corners_for": 8, "corners_against": 4, "shots_total": 16, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 60},
            {"goals_scored": 4, "goals_conceded": 1, "xg_for": 2.9, "xg_against": 0.8, "corners_for": 7, "corners_against": 3, "shots_total": 19, "shots_on_target": 9, "yellow_cards": 1, "red_cards": 0, "fouls": 8, "possession": 65},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.0, "xg_against": 0.7, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 59}
        ],
        "key_players": [
            {"name": "Ousmane Dembélé", "position": "Extremo Derecho / Generador", "avg_shots_p90": 3.4, "avg_sot_p90": 1.5, "shot_creation_actions": 7.8, "goal_prob": 0.42},
            {"name": "Bradley Barcola", "position": "Extremo Izquierdo / Desequilibrio", "avg_shots_p90": 3.2, "avg_sot_p90": 1.6, "shot_creation_actions": 5.9, "goal_prob": 0.48},
            {"name": "Vitinha", "position": "Eje del Mediocampo", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 6.2, "goal_prob": 0.22},
            {"name": "Warren Zaïre-Emery", "position": "Interior Físico", "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 4.1, "goal_prob": 0.18},
            {"name": "Achraf Hakimi", "position": "Lateral Ofensivo", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 5.0, "goal_prob": 0.25}
        ]
    },
    "PSG": {
        "fifa_rank": 6,
        "recent_form": ["W", "W", "W", "D", "W", "W", "D", "W"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.5, "xg_against": 0.9, "corners_for": 7, "corners_against": 4, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 64},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.1, "xg_against": 0.6, "corners_for": 6, "corners_against": 3, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 62}
        ],
        "key_players": [
            {"name": "Ousmane Dembélé", "position": "Extremo Derecho", "avg_shots_p90": 3.4, "avg_sot_p90": 1.5, "shot_creation_actions": 7.8, "goal_prob": 0.42},
            {"name": "Bradley Barcola", "position": "Extremo Izquierdo", "avg_shots_p90": 3.2, "avg_sot_p90": 1.6, "shot_creation_actions": 5.9, "goal_prob": 0.48}
        ]
    },
    "LASK": {
        "fifa_rank": 75,
        "recent_form": ["W", "L", "D", "W", "L", "W", "D", "L"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.1, "xg_against": 2.2, "corners_for": 4, "corners_against": 7, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 42},
            {"goals_scored": 0, "goals_conceded": 3, "xg_for": 0.7, "xg_against": 2.7, "corners_for": 3, "corners_against": 8, "shots_total": 7, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 38},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.4, "xg_against": 1.3, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 46}
        ],
        "key_players": [
            {"name": "Robert Žulj", "position": "Mediapunta / Capitán", "avg_shots_p90": 2.4, "avg_sot_p90": 0.9, "shot_creation_actions": 4.5, "goal_prob": 0.32},
            {"name": "Marin Ljubičić", "position": "Delantero Centro", "avg_shots_p90": 2.6, "avg_sot_p90": 1.1, "shot_creation_actions": 2.9, "goal_prob": 0.35},
            {"name": "Valon Berisha", "position": "Centrocampista", "avg_shots_p90": 1.2, "avg_sot_p90": 0.4, "shot_creation_actions": 3.8, "goal_prob": 0.12}
        ]
    },
    "Bodø/Glimt": {
        "fifa_rank": 48,
        "recent_form": ["W", "W", "D", "W", "L", "W", "W", "D"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.8, "xg_against": 1.2, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 54},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.5, "xg_against": 1.4, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 51},
            {"goals_scored": 3, "goals_conceded": 2, "xg_for": 2.1, "xg_against": 1.7, "corners_for": 7, "corners_against": 6, "shots_total": 15, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 53}
        ],
        "key_players": [
            {"name": "Jens Petter Hauge", "position": "Extremo Izquierdo", "avg_shots_p90": 2.9, "avg_sot_p90": 1.3, "shot_creation_actions": 5.2, "goal_prob": 0.38},
            {"name": "Kasper Høgh", "position": "Delantero Centro", "avg_shots_p90": 2.7, "avg_sot_p90": 1.2, "shot_creation_actions": 3.1, "goal_prob": 0.40},
            {"name": "Patrick Berg", "position": "Pivote Organizador", "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 4.8, "goal_prob": 0.16}
        ]
    },
    "Aston Villa": {
        "fifa_rank": 16,
        "recent_form": ["W", "W", "W", "D", "W", "L", "W", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.0, "xg_against": 0.7, "corners_for": 6, "corners_against": 3, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 55},
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.4, "xg_against": 1.0, "corners_for": 7, "corners_against": 4, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 57},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.7, "xg_against": 0.8, "corners_for": 5, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 53}
        ],
        "key_players": [
            {"name": "Ollie Watkins", "position": "Delantero Centro Élite", "avg_shots_p90": 3.6, "avg_sot_p90": 1.7, "shot_creation_actions": 4.9, "goal_prob": 0.50},
            {"name": "Youri Tielemans", "position": "Centrocampista Organizador", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 6.1, "goal_prob": 0.22},
            {"name": "Morgan Rogers", "position": "Mediapunta Vertical", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 5.4, "goal_prob": 0.35},
            {"name": "Leon Bailey", "position": "Extremo Desequilibrante", "avg_shots_p90": 2.8, "avg_sot_p90": 1.2, "shot_creation_actions": 5.1, "goal_prob": 0.36}
        ]
    },
    "Fenerbahçe": {
        "fifa_rank": 36,
        "recent_form": ["W", "W", "D", "W", "W", "D", "L", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.9, "xg_against": 1.1, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 56},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.6, "xg_against": 1.3, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 53}
        ],
        "key_players": [
            {"name": "Edin Džeko", "position": "Delantero Centro", "avg_shots_p90": 3.2, "avg_sot_p90": 1.5, "shot_creation_actions": 3.8, "goal_prob": 0.44},
            {"name": "Dušan Tadić", "position": "Mediapunta / Conector", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 6.8, "goal_prob": 0.30},
            {"name": "Youssef En-Nesyri", "position": "Delantero de Área", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 3.2, "goal_prob": 0.40}
        ]
    },
    "Feyenoord": {
        "fifa_rank": 30,
        "recent_form": ["W", "W", "D", "W", "D", "W", "W", "D"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.1, "xg_against": 0.7, "corners_for": 7, "corners_against": 3, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 59},
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.3, "xg_against": 1.0, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 58}
        ],
        "key_players": [
            {"name": "Santiago Giménez", "position": "Delantero Centro", "avg_shots_p90": 3.5, "avg_sot_p90": 1.7, "shot_creation_actions": 4.1, "goal_prob": 0.52},
            {"name": "Quinten Timber", "position": "Centrocampista", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 5.2, "goal_prob": 0.28},
            {"name": "Igor Paixão", "position": "Extremo Rápido", "avg_shots_p90": 2.6, "avg_sot_p90": 1.1, "shot_creation_actions": 4.9, "goal_prob": 0.34}
        ]
    }
}

for k, v in new_teams.items():
    teams_db[k] = v

with open(teams_path, "w", encoding="utf-8") as f:
    json.dump(teams_db, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_teams)} teams for Wednesday Champions League!")
