# -*- coding: utf-8 -*-
"""
setup_european_sunday.py
Configura la cartelera de Domingo 11/10/2026 con los Gigantes y Ligas Europeas:
1. Napoli vs Como (Serie A - Giornata 7) -> DOBLE_OPORTUNIDAD (1X)
2. Marseille vs Angers (Ligue 1 - Jornada 7) -> GOL_EQUIPO (>0.5)
3. Borussia Dortmund vs St. Pauli (Bundesliga - Jornada 7) -> GOL_EQUIPO (>0.5)
4. Leganés vs Valencia (LaLiga EA Sports - Jornada 9) -> GOLES_UNDER (<3.5)
5. Sunderland vs Leeds United (EFL Championship / Inglaterra) -> GOLES_UNDER (<3.5)
6. Rio Ave vs Famalicão (Liga Portugal - Jornada 8) -> GOLES_UNDER (<3.5)
"""
import os
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
sys.path.insert(0, base_dir)

from sports_agents.data_scout_agent import DataScoutAgent

scout = DataScoutAgent()

teams_file = os.path.join(base_dir, "sports_agents", "teams_database.json")
matches_file = os.path.join(base_dir, "sports_agents", "matches_database.json")
cal_file = os.path.join(base_dir, "sports_agents", "official_calendar.json")

# Inyectar perfiles desde data_scout_agent
with open(teams_file, "r", encoding="utf-8") as f:
    teams_db = json.load(f)

sunday_teams = [
    "Napoli", "Como", "Marseille", "Angers",
    "Leganés", "Valencia", "Borussia Dortmund", "St. Pauli",
    "Sunderland", "Leeds United", "Rio Ave", "Famalicão"
]

for t in sunday_teams:
    t_data = scout.get_team_history(t)
    if t_data:
        teams_db[t] = t_data
        print(f"  + Equipo domingo inyectado: {t}")

with open(teams_file, "w", encoding="utf-8") as f:
    json.dump(teams_db, f, ensure_ascii=False, indent=2)

print(f"-> Total equipos en teams_database.json: {len(teams_db)}.")

# Inyectar metadatos de partidos
with open(matches_file, "r", encoding="utf-8") as f:
    matches_db = json.load(f)

sunday_fixtures = [
    ("Napoli", "Como"),
    ("Marseille", "Angers"),
    ("Borussia Dortmund", "St. Pauli"),
    ("Leganés", "Valencia"),
    ("Sunderland", "Leeds United"),
    ("Rio Ave", "Famalicão")
]

for home, away in sunday_fixtures:
    ctx = scout.get_match_context(home, away)
    if ctx:
        matches_db[f"{home} vs {away}"] = ctx
        print(f"  + Partido domingo inyectado: {home} vs {away}")

with open(matches_file, "w", encoding="utf-8") as f:
    json.dump(matches_db, f, ensure_ascii=False, indent=2)

print("-> Metadatos de partidos europeos de domingo guardados.")

# Actualizar official_calendar.json para Domingo 11/10/2026
with open(cal_file, "r", encoding="utf-8") as f:
    cal_db = json.load(f)

cal_db["2026-10-11"] = {
    "date_str": "11/10/2026",
    "day_name": "Domingo",
    "competition": "Ligas Europeas de Élite (Domingo de Grandes)",
    "fixtures": [
        ["Napoli", "Como", "DOBLE_OPORTUNIDAD"],
        ["Marseille", "Angers", "GOL_EQUIPO"],
        ["Borussia Dortmund", "St. Pauli", "GOL_EQUIPO"],
        ["Leganés", "Valencia", "GOLES_UNDER"],
        ["Sunderland", "Leeds United", "GOLES_UNDER"],
        ["Rio Ave", "Famalicão", "GOLES_UNDER"]
    ]
}

with open(cal_file, "w", encoding="utf-8") as f:
    json.dump(cal_db, f, ensure_ascii=False, indent=2)

print("-> official_calendar.json configurado con los 6 Europeos para Domingo 11/10/2026.")
