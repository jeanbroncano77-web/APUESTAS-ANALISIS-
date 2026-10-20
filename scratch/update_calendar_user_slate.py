import json

cal_path = "sports_agents/official_calendar.json"
with open(cal_path, "r", encoding="utf-8") as f:
    cal = json.load(f)

cal["2026-10-19"] = {
    "date_str": "19/10/2026",
    "day_name": "Lunes",
    "competition": "LigaPro Ecuador, Premier League, LaLiga EA Sports & Serie A",
    "fixtures": [
        ["Mushuc Runa", "Orense SC", "DOBLE_OPORTUNIDAD"],
        ["Macará", "Independiente del Valle", "DOBLE_OPORTUNIDAD"],
        ["Tottenham Hotspur", "Coventry City", "VICTORIA_DIRECTA"],
        ["Getafe", "Rayo Vallecano", "DOBLE_OPORTUNIDAD"],
        ["Monza", "Cagliari", "DOBLE_OPORTUNIDAD"],
        ["Parma", "Torino", "DOBLE_OPORTUNIDAD"]
    ]
}

with open(cal_path, "w", encoding="utf-8") as f_w:
    json.dump(cal, f_w, ensure_ascii=False, indent=2)

print("Official calendar updated with user exact 6 fixtures for Monday 19/10/2026.")
