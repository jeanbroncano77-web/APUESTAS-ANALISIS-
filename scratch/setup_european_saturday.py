# -*- coding: utf-8 -*-
"""
setup_european_saturday.py
Configura la cartelera de Sábado 10/10/2026 con los Gigantes de Europa:
1. Real Madrid vs Villarreal (LaLiga)
2. Barcelona vs Getafe (LaLiga)
3. Arsenal vs Leeds United (Premier League)
4. FC Augsburg vs Bayern Munich (Bundesliga)
5. Inter Milan vs Parma (Serie A)
6. Borussia Dortmund vs Werder Bremen (Bundesliga)
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

euro_teams = [
    "Real Madrid", "Villarreal", "Barcelona", "Getafe",
    "Arsenal", "Leeds United", "FC Augsburg", "Bayern Munich",
    "Inter Milan", "Parma", "Borussia Dortmund", "Werder Bremen"
]

for t in euro_teams:
    t_data = scout.get_team_history(t)
    if t_data:
        teams_db[t] = t_data
        print(f"  + Equipo inyectado: {t}")

with open(teams_file, "w", encoding="utf-8") as f:
    json.dump(teams_db, f, ensure_ascii=False, indent=2)

print(f"-> Total equipos en teams_database.json: {len(teams_db)}.")

# Inyectar metadatos de partidos
with open(matches_file, "r", encoding="utf-8") as f:
    matches_db = json.load(f)

euro_fixtures = [
    ("Real Madrid", "Villarreal"),
    ("Barcelona", "Getafe"),
    ("Arsenal", "Leeds United"),
    ("FC Augsburg", "Bayern Munich"),
    ("Inter Milan", "Parma"),
    ("Borussia Dortmund", "Werder Bremen")
]

for home, away in euro_fixtures:
    ctx = scout.get_match_context(home, away)
    if ctx:
        matches_db[f"{home} vs {away}"] = ctx
        print(f"  + Partido inyectado: {home} vs {away}")

with open(matches_file, "w", encoding="utf-8") as f:
    json.dump(matches_db, f, ensure_ascii=False, indent=2)

print("-> Metadatos de partidos europeos guardados.")

# Actualizar official_calendar.json para Sábado 10/10/2026
with open(cal_file, "r", encoding="utf-8") as f:
    cal_db = json.load(f)

cal_db["2026-10-10"] = {
    "date_str": "10/10/2026",
    "day_name": "Sábado",
    "competition": "Ligas Europeas de Élite (Sábado de Gigantes)",
    "fixtures": [
        ["Real Madrid", "Villarreal", "GOL_EQUIPO"],
        ["Barcelona", "Getafe", "DOBLE_OPORTUNIDAD"],
        ["Arsenal", "Leeds United", "DOBLE_OPORTUNIDAD"],
        ["FC Augsburg", "Bayern Munich", "GOL_EQUIPO"],
        ["Inter Milan", "Parma", "DOBLE_OPORTUNIDAD"],
        ["Borussia Dortmund", "Werder Bremen", "GOL_EQUIPO"]
    ]
}

with open(cal_file, "w", encoding="utf-8") as f:
    json.dump(cal_db, f, ensure_ascii=False, indent=2)

print("-> official_calendar.json configurado con los 6 Gigantes Europeos para Sábado 10/10/2026.")
