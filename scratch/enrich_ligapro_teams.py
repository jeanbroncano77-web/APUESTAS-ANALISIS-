import json
import os

db_path = "sports_agents/teams_database.json"
with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

ecuador_teams = {
    "Orense SC": {
        "league": "LigaPro Ecuador",
        "home_power": 64.0,
        "away_power": 48.0,
        "xg_for_home": 1.35,
        "xg_against_home": 1.15,
        "xg_for_away": 0.85,
        "xg_against_away": 1.55,
        "goals_scored_avg": 1.10,
        "goals_conceded_avg": 1.35,
        "possession_avg": 46.5,
        "cards_avg": 4.6,
        "corners_avg": 4.2,
        "form_last_5": ["E", "D", "V", "D", "E"],
        "injuries": [],
        "style": "Transición rápida de costa, sufre en altura extrema (+3,000m)"
    },
    "Orense": {
        "league": "LigaPro Ecuador",
        "home_power": 64.0,
        "away_power": 48.0,
        "xg_for_home": 1.35,
        "xg_against_home": 1.15,
        "xg_for_away": 0.85,
        "xg_against_away": 1.55,
        "goals_scored_avg": 1.10,
        "goals_conceded_avg": 1.35,
        "possession_avg": 46.5,
        "cards_avg": 4.6,
        "corners_avg": 4.2,
        "form_last_5": ["E", "D", "V", "D", "E"],
        "injuries": [],
        "style": "Transición rápida de costa, sufre en altura extrema (+3,000m)"
    },
    "Macará": {
        "league": "LigaPro Ecuador",
        "home_power": 68.0,
        "away_power": 52.0,
        "xg_for_home": 1.40,
        "xg_against_home": 1.20,
        "xg_for_away": 0.95,
        "xg_against_away": 1.45,
        "goals_scored_avg": 1.18,
        "goals_conceded_avg": 1.32,
        "possession_avg": 48.0,
        "cards_avg": 4.8,
        "corners_avg": 4.5,
        "form_last_5": ["D", "E", "D", "V", "D"],
        "injuries": [],
        "style": "Bloque medio andino, defensivo y juego aéreo en Bellavista"
    },
    "Macara": {
        "league": "LigaPro Ecuador",
        "home_power": 68.0,
        "away_power": 52.0,
        "xg_for_home": 1.40,
        "xg_against_home": 1.20,
        "xg_for_away": 0.95,
        "xg_against_away": 1.45,
        "goals_scored_avg": 1.18,
        "goals_conceded_avg": 1.32,
        "possession_avg": 48.0,
        "cards_avg": 4.8,
        "corners_avg": 4.5,
        "form_last_5": ["D", "E", "D", "V", "D"],
        "injuries": [],
        "style": "Bloque medio andino, defensivo y juego aéreo en Bellavista"
    },
    "Independiente del Valle": {
        "league": "LigaPro Ecuador",
        "home_power": 86.0,
        "away_power": 80.0,
        "xg_for_home": 2.15,
        "xg_against_home": 0.75,
        "xg_for_away": 1.75,
        "xg_against_away": 0.95,
        "goals_scored_avg": 1.95,
        "goals_conceded_avg": 0.85,
        "possession_avg": 59.8,
        "cards_avg": 3.8,
        "corners_avg": 6.2,
        "form_last_5": ["V", "V", "V", "E", "V"],
        "injuries": [],
        "style": "Posesión dominante, presión alta, plantilla de jerarquía internacional que busca el título"
    },
    "Tottenham": {
        "league": "Premier League",
        "home_power": 84.0,
        "away_power": 75.0,
        "xg_for_home": 2.20,
        "xg_against_home": 1.10,
        "xg_for_away": 1.60,
        "xg_against_away": 1.40,
        "goals_scored_avg": 2.05,
        "goals_conceded_avg": 1.25,
        "possession_avg": 59.5,
        "cards_avg": 3.9,
        "corners_avg": 6.8,
        "form_last_5": ["V", "V", "E", "D", "V"],
        "injuries": [],
        "style": "Fútbol ofensivo vertical, presión intensa y desborde por bandas"
    }
}

for k, v in ecuador_teams.items():
    db[k] = v

with open(db_path, "w", encoding="utf-8") as f_w:
    json.dump(db, f_w, ensure_ascii=False, indent=2)

print("Teams database enriched successfully with LigaPro teams and Tottenham alias.")
