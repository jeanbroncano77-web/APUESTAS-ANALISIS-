import json

with open("sports_agents/official_calendar.json", "r", encoding="utf-8") as f:
    cal = json.load(f)

cal["2026-10-12"] = {
    "date_str": "12/10/2026",
    "day_name": "Lunes",
    "competition": "Ligas de Élite Europea & Sudamérica (LaLiga, Premier, Serie A, LPF, Brasileirão)",
    "fixtures": [
        ["Atalanta", "Venezia", "DOBLE_OPORTUNIDAD"],
        ["Coventry City", "Newcastle", "DOBLE_OPORTUNIDAD"],
        ["Levante", "Sevilla", "DOBLE_OPORTUNIDAD"],
        ["Torino", "Udinese", "DOBLE_OPORTUNIDAD"],
        ["Racing Club", "Belgrano", "DOBLE_OPORTUNIDAD"],
        ["Bahia", "Mirassol", "DOBLE_OPORTUNIDAD"]
    ]
}

with open("sports_agents/official_calendar.json", "w", encoding="utf-8") as f:
    json.dump(cal, f, ensure_ascii=False, indent=2)

print("official_calendar.json actualizado para 2026-10-12 con las 6 fijas oficiales.")
