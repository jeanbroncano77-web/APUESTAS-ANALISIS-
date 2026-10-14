import json

cal_path = "sports_agents/official_calendar.json"
with open(cal_path, "r", encoding="utf-8") as f:
    cal_db = json.load(f)

cal_db["2026-10-13"] = {
    "date_str": "13/10/2026",
    "day_name": "Martes",
    "competition": "UEFA Champions League - Fase de Liga (Jornada 2)",
    "fixtures": [
        ["Galatasaray", "Barcelona", "DOBLE_OPORTUNIDAD"],
        ["Arsenal", "Lille", "DOBLE_OPORTUNIDAD"],
        ["Atlético de Madrid", "Manchester United", "DOBLE_OPORTUNIDAD"],
        ["Inter Milan", "Club Brugge", "DOBLE_OPORTUNIDAD"],
        ["Viking FK", "Bayern Munich", "GOL_EQUIPO"],
        ["Villarreal", "Napoli", "DOBLE_OPORTUNIDAD"]
    ]
}

with open(cal_path, "w", encoding="utf-8") as f:
    json.dump(cal_db, f, ensure_ascii=False, indent=2)

print("official_calendar.json updated for 2026-10-13 UEFA Champions League!")
