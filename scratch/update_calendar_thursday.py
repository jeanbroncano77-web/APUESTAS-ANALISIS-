import json
import os

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
cal_file = os.path.join(base_dir, "sports_agents", "official_calendar.json")

with open(cal_file, "r", encoding="utf-8") as f:
    cal = json.load(f)

cal["2026-10-15"] = {
    "date_str": "15/10/2026",
    "day_name": "Jueves",
    "competition": "UEFA Europa League & UEFA Conference League",
    "fixtures": [
        ["Benfica", "Celtic", "DOBLE_OPORTUNIDAD"],
        ["Red Bull Salzburg", "AC Milan", "DOBLE_OPORTUNIDAD"],
        ["Celta Vigo", "Juventus", "DOBLE_OPORTUNIDAD"],
        ["Lech Poznań", "Bayer Leverkusen", "DOBLE_OPORTUNIDAD"],
        ["Olympique Lyon", "Crystal Palace", "DOBLE_OPORTUNIDAD"],
        ["Hajduk Split", "AFC Ajax", "DOBLE_OPORTUNIDAD"]
    ]
}

with open(cal_file, "w", encoding="utf-8") as f:
    json.dump(cal, f, indent=2, ensure_ascii=False)

print("official_calendar.json actualizado para Jueves 15/10/2026 con Europa League & Conference League!")
