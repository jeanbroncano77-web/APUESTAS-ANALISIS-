import json

cal_path = "sports_agents/official_calendar.json"
with open(cal_path, "r", encoding="utf-8") as f:
    cal_db = json.load(f)

cal_db["2026-10-14"] = {
    "date_str": "14/10/2026",
    "day_name": "Miércoles",
    "competition": "UEFA Champions League • Fase de Liga (Jornada 2)",
    "fixtures": [
        ["Manchester City", "Paris Saint-Germain", "DOBLE_OPORTUNIDAD"],
        ["Roma", "Real Madrid", "DOBLE_OPORTUNIDAD"],
        ["LASK", "Liverpool", "DOBLE_OPORTUNIDAD"],
        ["Bodø/Glimt", "Borussia Dortmund", "DOBLE_OPORTUNIDAD"],
        ["Aston Villa", "Fenerbahçe", "DOBLE_OPORTUNIDAD"],
        ["Feyenoord", "Como", "DOBLE_OPORTUNIDAD"]
    ]
}

with open(cal_path, "w", encoding="utf-8") as f:
    json.dump(cal_db, f, ensure_ascii=False, indent=2)

print("official_calendar.json updated with Wednesday UEFA Champions League!")
