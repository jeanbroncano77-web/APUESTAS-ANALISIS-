# -*- coding: utf-8 -*-
"""
model_dortmund_vs_bremen.py
Modela Borussia Dortmund vs Werder Bremen para hoy Viernes 09/10/2026
con los 11 agentes de SportsAI.
"""
import os
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
sys.path.insert(0, base_dir)

teams_file = os.path.join(base_dir, "sports_agents", "teams_database.json")
matches_file = os.path.join(base_dir, "sports_agents", "matches_database.json")

dortmund_teams = {
    "Borussia Dortmund": {
        "fifa_rank": 11,
        "recent_form": ["W", "W", "W", "W", "D", "W", "W", "W"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.65, "xg_against": 0.85, "corners_for": 8, "corners_against": 3, "shots_total": 18, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 62},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.20, "xg_against": 0.60, "corners_for": 7, "corners_against": 2, "shots_total": 16, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 64},
            {"goals_scored": 4, "goals_conceded": 2, "xg_for": 3.10, "xg_against": 1.25, "corners_for": 9, "corners_against": 4, "shots_total": 20, "shots_on_target": 9, "yellow_cards": 1, "red_cards": 0, "fouls": 8, "possession": 60},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.40, "xg_against": 0.95, "corners_for": 6, "corners_against": 4, "shots_total": 15, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 58}
        ],
        "key_players": [
            {"name": "Serhou Guirassy", "position": "Delantero Centro Goleador", "avg_shots_p90": 3.4, "avg_sot_p90": 1.6, "shot_creation_actions": 3.2, "goal_prob": 0.62},
            {"name": "Julian Brandt", "position": "Mediapunta Organizador", "avg_shots_p90": 2.3, "avg_sot_p90": 0.9, "shot_creation_actions": 5.4, "goal_prob": 0.28},
            {"name": "Karim Adeyemi", "position": "Extremo Eléctrico", "avg_shots_p90": 2.8, "avg_sot_p90": 1.2, "shot_creation_actions": 4.1, "goal_prob": 0.35},
            {"name": "Marcel Sabitzer", "position": "Volante Mixto con Pegada", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 3.6, "goal_prob": 0.18}
        ]
    },
    "Werder Bremen": {
        "fifa_rank": 36,
        "recent_form": ["L", "D", "W", "L", "D", "L", "W", "D"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.15, "xg_against": 2.10, "corners_for": 4, "corners_against": 7, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 42},
            {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.85, "xg_against": 2.30, "corners_for": 3, "corners_against": 8, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 40},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.40, "xg_against": 1.50, "corners_for": 5, "corners_against": 6, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 46}
        ],
        "key_players": [
            {"name": "Marvin Ducksch", "position": "Delantero Referente", "avg_shots_p90": 2.6, "avg_sot_p90": 1.0, "shot_creation_actions": 3.8, "goal_prob": 0.30},
            {"name": "Romano Schmid", "position": "Volante Ofensivo Rápido", "avg_shots_p90": 1.9, "avg_sot_p90": 0.7, "shot_creation_actions": 4.2, "goal_prob": 0.18},
            {"name": "Mitchell Weiser", "position": "Carrilero Derecho", "avg_shots_p90": 1.2, "avg_sot_p90": 0.4, "shot_creation_actions": 3.5, "goal_prob": 0.12}
        ]
    }
}

with open(teams_file, "r", encoding="utf-8") as f:
    teams_db = json.load(f)

for tk, tv in dortmund_teams.items():
    teams_db[tk] = tv

with open(teams_file, "w", encoding="utf-8") as f:
    json.dump(teams_db, f, ensure_ascii=False, indent=2)

print("-> Perfiles de Borussia Dortmund y Werder Bremen guardados.")

dortmund_match_meta = {
    "Borussia Dortmund vs Werder Bremen": {
        "tournament": "Bundesliga Alemana - Jornada 5 (Freitagsspiel)",
        "stadium": "Signal Iduna Park (Westfalenstadion, Dortmund)",
        "spectators_est": "81,365 en estadio (~30M audiencia global)",
        "referee": "Felix Zwayer",
        "referee_avg_yellows": 4.2,
        "referee_avg_reds": 0.14,
        "intensity": "Máxima (Duelo de viernes en la Muralla Amarilla; Dortmund busca afianzar el liderato invicto ante el Bremen)"
    }
}

with open(matches_file, "r", encoding="utf-8") as f:
    matches_db = json.load(f)

for mk, mv in dortmund_match_meta.items():
    matches_db[mk] = mv

with open(matches_file, "w", encoding="utf-8") as f:
    json.dump(matches_db, f, ensure_ascii=False, indent=2)

print("-> Metadatos de Borussia Dortmund vs Werder Bremen guardados.")

from sports_agents import SportsDirectorAgent
director = SportsDirectorAgent()

print("\n=== MODELANDO BORUSSIA DORTMUND VS WERDER BREMEN CON LOS 11 AGENTES ===")
pred = director.predict_fixture("Borussia Dortmund", "Werder Bremen", preferred_market_category="GOL_EQUIPO")

with open(os.path.join(base_dir, "scratch", "dortmund_prediction_result.json"), "w", encoding="utf-8") as f_res:
    json.dump(pred, f_res, ensure_ascii=False, indent=2)

print("-> Predicción completada y guardada en scratch/dortmund_prediction_result.json.")
