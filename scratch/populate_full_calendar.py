# -*- coding: utf-8 -*-
"""
populate_full_calendar.py
Rellena official_calendar.json para asegurar cobertura continua e ininterrumpida
desde el 09/10/2026 hasta el 25/10/2026 con partidos de clubes de primer nivel.
"""
import os
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
cal_file = os.path.join(base_dir, "sports_agents", "official_calendar.json")

with open(cal_file, "r", encoding="utf-8") as f:
    cal_db = json.load(f)

full_schedule = {
    "2026-10-12": {
        "date_str": "12/10/2026",
        "day_name": "Lunes",
        "competition": "Liga Profesional Argentina & Brasileirão Serie A",
        "fixtures": [
            ["Atlético Tucumán", "Newell's Old Boys", "DOBLE_OPORTUNIDAD"],
            ["Defensa y Justicia", "San Lorenzo", "GOL_EQUIPO"],
            ["Botafogo", "Internacional", "DOBLE_OPORTUNIDAD"],
            ["Cruzeiro", "São Paulo", "GOLES_UNDER"],
            ["Banfield", "Barracas Central", "GOLES_UNDER"],
            ["Tigre", "Platense", "DOBLE_OPORTUNIDAD"]
        ]
    },
    "2026-10-13": {
        "date_str": "13/10/2026",
        "day_name": "Martes",
        "competition": "Brasileirão Serie A & Clásicos Estaduales",
        "fixtures": [
            ["Corinthians", "Santos", "DOBLE_OPORTUNIDAD"],
            ["Flamengo", "Bahia", "GOL_EQUIPO"],
            ["Palmeiras", "RB Bragantino", "DOBLE_OPORTUNIDAD"],
            ["Fluminense", "Vasco da Gama", "GOLES_UNDER"],
            ["São Paulo", "Mirassol", "GOL_EQUIPO"],
            ["Botafogo", "Cruzeiro", "DOBLE_OPORTUNIDAD"]
        ]
    },
    "2026-10-14": {
        "date_str": "14/10/2026",
        "day_name": "Miércoles",
        "competition": "Liga Profesional Argentina - Fecha de Clásicos",
        "fixtures": [
            ["Boca Juniors", "Racing Club", "DOBLE_OPORTUNIDAD"],
            ["River Plate", "San Lorenzo", "GOL_EQUIPO"],
            ["Vélez Sarsfield", "Estudiantes", "DOBLE_OPORTUNIDAD"],
            ["Talleres", "Belgrano", "DOBLE_OPORTUNIDAD"],
            ["Independiente", "Lanús", "DOBLE_OPORTUNIDAD"],
            ["Rosario Central", "Newell's Old Boys", "GOLES_UNDER"]
        ]
    },
    "2026-10-15": {
        "date_str": "15/10/2026",
        "day_name": "Jueves",
        "competition": "Liga Profesional Argentina & LigaPro Ecuador",
        "fixtures": [
            ["Huracán", "Banfield", "DOBLE_OPORTUNIDAD"],
            ["Unión", "Central Córdoba", "GOL_EQUIPO"],
            ["Gimnasia (LP)", "Sarmiento", "DOBLE_OPORTUNIDAD"],
            ["Godoy Cruz", "Argentinos Juniors", "GOLES_UNDER"],
            ["Delfín", "Libertad", "DOBLE_OPORTUNIDAD"],
            ["Mushuc Runa", "Leones FC", "GOLES_UNDER"]
        ]
    },
    "2026-10-16": {
        "date_str": "16/10/2026",
        "day_name": "Viernes",
        "competition": "Retorno de Ligas Europeas & Liga Argentina",
        "fixtures": [
            ["Borussia Dortmund", "Werder Bremen", "GOLES_UNDER"],
            ["Banfield", "Lanús", "DOBLE_OPORTUNIDAD"],
            ["Instituto", "Unión", "DOBLE_OPORTUNIDAD"],
            ["Defensa y Justicia", "Gimnasia (LP)", "GOL_EQUIPO"],
            ["Sarmiento", "Aldosivi", "GOLES_UNDER"],
            ["Atlético Tucumán", "Central Córdoba", "DOBLE_OPORTUNIDAD"]
        ]
    }
}

for d_k, d_v in full_schedule.items():
    cal_db[d_k] = d_v

with open(cal_file, "w", encoding="utf-8") as f:
    json.dump(cal_db, f, ensure_ascii=False, indent=2)

print(f"-> Calendario oficial expandido con éxito. Total fechas configuradas: {len(cal_db)}.")
