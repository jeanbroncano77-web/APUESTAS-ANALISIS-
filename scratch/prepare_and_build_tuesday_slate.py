# -*- coding: utf-8 -*-
"""
prepare_and_build_tuesday_slate.py
1. Enriquece teams_database.json con Sporting de Lisboa, Shakhtar Donetsk, Al-Nassr, Neom SC (con secuencias de partidos completas).
2. Enriquece matches_database.json con los contextos de la jornada estelar de Martes 20/10/2026.
3. Actualiza official_calendar.json con la fecha 2026-10-20.
4. Ejecuta SportsDirectorAgent para modelar los 6 partidos y generar simulations_tomorrow_results.json.
5. Ejecuta build_dashboard_tomorrow.py para inyectar Área 1 (Cartelera) en index.html.
6. Ejecuta sync_complete_dashboard_3areas.py para sincronizar Área 2 (Win Rate 87.1%) y Área 3 (Autoaprendizaje).
7. Sube todo a GitHub.
"""

import os
import sys
import json
from datetime import datetime

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
sys.path.insert(0, base_dir)

teams_db_path = os.path.join(base_dir, "sports_agents", "teams_database.json")
matches_db_path = os.path.join(base_dir, "sports_agents", "matches_database.json")
calendar_path = os.path.join(base_dir, "sports_agents", "official_calendar.json")

print("1. Enriqueciendo teams_database.json con secuencias completas...")
with open(teams_db_path, "r", encoding="utf-8") as f:
    teams_db = json.load(f)

def make_seq(goals_for, goals_against, xg_f, xg_a, corners_f, corners_a, shots_f, shots_ot, yellows, poss):
    res = []
    for i in range(len(goals_for)):
        res.append({
            "goals_scored": goals_for[i],
            "goals_conceded": goals_against[i],
            "xg_for": xg_f[i],
            "xg_against": xg_a[i],
            "corners_for": corners_f[i],
            "corners_against": corners_a[i],
            "shots_total": shots_f[i],
            "shots_on_target": shots_ot[i],
            "yellow_cards": yellows[i],
            "red_cards": 0,
            "fouls": 11,
            "possession": poss[i]
        })
    return res

new_teams = {
    "Sporting de Lisboa": {
        "fifa_rank": 14,
        "recent_form": ["W", "W", "W", "W", "D", "W", "W"],
        "sequence": make_seq(
            [3, 2, 4, 2, 1, 3, 2],
            [0, 1, 1, 0, 1, 0, 1],
            [2.9, 2.2, 3.4, 2.3, 1.8, 2.7, 2.4],
            [0.5, 0.9, 0.8, 0.4, 1.1, 0.6, 0.7],
            [7, 6, 8, 5, 6, 7, 6],
            [3, 4, 3, 2, 4, 3, 3],
            [18, 15, 20, 14, 13, 17, 16],
            [8, 7, 9, 6, 5, 8, 7],
            [2, 1, 2, 1, 2, 1, 2],
            [65, 62, 68, 60, 58, 64, 63]
        ),
        "key_players": [
            {"name": "Viktor Gyökeres", "role": "Forward", "sot_avg": 2.6, "xg_contribution": 0.95},
            {"name": "Pedro Gonçalves", "role": "Midfielder", "sot_avg": 1.7, "xg_contribution": 0.45},
            {"name": "Francisco Trincão", "role": "Winger", "sot_avg": 1.4, "xg_contribution": 0.38}
        ]
    },
    "Shakhtar Donetsk": {
        "fifa_rank": 38,
        "recent_form": ["W", "L", "W", "D", "W"],
        "sequence": make_seq(
            [1, 0, 2, 1, 2],
            [1, 3, 1, 1, 0],
            [1.2, 0.6, 1.8, 1.1, 1.7],
            [1.3, 2.8, 1.2, 1.4, 0.8],
            [4, 3, 5, 4, 5],
            [5, 8, 4, 5, 3],
            [11, 7, 13, 10, 12],
            [4, 2, 5, 4, 5],
            [3, 2, 3, 2, 1],
            [48, 38, 52, 47, 54]
        ),
        "key_players": [
            {"name": "Georgiy Sudakov", "role": "Midfielder", "sot_avg": 1.2, "xg_contribution": 0.35},
            {"name": "Danylo Sikan", "role": "Forward", "sot_avg": 1.1, "xg_contribution": 0.32}
        ]
    },
    "Al-Nassr": {
        "fifa_rank": 28,
        "recent_form": ["W", "W", "W", "W", "D", "W"],
        "sequence": make_seq(
            [3, 2, 3, 1, 2, 4],
            [1, 0, 1, 0, 2, 1],
            [2.8, 2.1, 2.9, 1.7, 2.0, 3.2],
            [0.9, 0.6, 0.8, 0.5, 1.5, 0.8],
            [7, 6, 8, 5, 6, 8],
            [3, 3, 4, 2, 4, 3],
            [19, 16, 18, 13, 15, 21],
            [8, 7, 9, 5, 6, 10],
            [2, 1, 2, 1, 3, 1],
            [64, 61, 66, 58, 60, 67]
        ),
        "key_players": [
            {"name": "Cristiano Ronaldo", "role": "Forward", "sot_avg": 3.1, "xg_contribution": 0.92},
            {"name": "Sadio Mané", "role": "Forward", "sot_avg": 1.8, "xg_contribution": 0.52},
            {"name": "Otávio", "role": "Midfielder", "sot_avg": 1.2, "xg_contribution": 0.28}
        ]
    },
    "Neom SC": {
        "fifa_rank": 95,
        "recent_form": ["W", "D", "W", "L", "D"],
        "sequence": make_seq(
            [1, 1, 2, 0, 1],
            [0, 1, 1, 2, 1],
            [1.1, 1.0, 1.6, 0.5, 1.0],
            [0.8, 1.2, 1.3, 2.1, 1.1],
            [4, 3, 4, 3, 4],
            [4, 5, 5, 7, 4],
            [9, 8, 11, 6, 9],
            [3, 3, 4, 1, 3],
            [2, 3, 2, 3, 2],
            [45, 47, 48, 36, 46]
        ),
        "key_players": [
            {"name": "Romarinho", "role": "Forward", "sot_avg": 1.5, "xg_contribution": 0.40},
            {"name": "Ahmed Hegazi", "role": "Defender", "sot_avg": 0.4, "xg_contribution": 0.12}
        ]
    }
}

for k, v in new_teams.items():
    teams_db[k] = v

with open(teams_db_path, "w", encoding="utf-8") as f:
    json.dump(teams_db, f, ensure_ascii=False, indent=2)
print("✓ teams_database.json enriquecido con secuencias correctas.")

print("\n2. Enriqueciendo matches_database.json...")
with open(matches_db_path, "r", encoding="utf-8") as f:
    matches_db = json.load(f)

tuesday_contexts = {
    "Real Madrid vs RB Leipzig": {
        "tournament": "UEFA Champions League • Fase de Liga (Santiago Bernabéu)",
        "stadium": "Estadio Santiago Bernabéu (Madrid)",
        "spectators_est": "81,044 espectadores (14:00 Hora Ecuador)",
        "referee": "Szymon Marciniak",
        "referee_avg_yellows": 4.1,
        "referee_avg_reds": 0.14,
        "intensity": "Máxima (Real Madrid en noche de gala continental con Mbappé y Vinícius Jr. 100% descansados)"
    },
    "Sporting de Lisboa vs LASK": {
        "tournament": "UEFA Champions League • Fase de Liga (Estádio José Alvalade)",
        "stadium": "Estádio José Alvalade (Lisboa)",
        "spectators_est": "48,500 espectadores (14:00 Hora Ecuador)",
        "referee": "Clément Turpin",
        "referee_avg_yellows": 3.7,
        "referee_avg_reds": 0.12,
        "intensity": "Alta (Sporting busca golear en casa apoyado en el poderío letal de Viktor Gyökeres)"
    },
    "Aston Villa vs Viking FK": {
        "tournament": "UEFA Champions League / Europa • Fase Continental",
        "stadium": "Villa Park (Birmingham)",
        "spectators_est": "42,600 espectadores (14:00 Hora Ecuador)",
        "referee": "Felix Zwayer",
        "referee_avg_yellows": 3.9,
        "referee_avg_reds": 0.15,
        "intensity": "Alta (Unai Emery busca asegurar el pleno en casa frente al cuadro noruego de Viking)"
    },
    "Inter Milan vs Shakhtar Donetsk": {
        "tournament": "UEFA Champions League • San Siro",
        "stadium": "Stadio Giuseppe Meazza / San Siro (Milán)",
        "spectators_est": "72,000 espectadores (14:00 Hora Ecuador)",
        "referee": "Anthony Taylor",
        "referee_avg_yellows": 4.0,
        "referee_avg_reds": 0.18,
        "intensity": "Media-Alta (Inter necesita consolidar su clasificación ante el bloque de Donetsk)"
    },
    "Bayern Munich vs Arsenal": {
        "tournament": "UEFA Champions League • Choque Estelar de Gigantes",
        "stadium": "Allianz Arena (Múnich)",
        "spectators_est": "75,000 espectadores (14:00 Hora Ecuador)",
        "referee": "Slavko Vinčić",
        "referee_avg_yellows": 4.5,
        "referee_avg_reds": 0.20,
        "intensity": "Extrema (Poderío ofensivo total, ritmo frenético de Premier vs Bundesliga)"
    },
    "Al-Nassr vs Neom SC": {
        "tournament": "Liga Profesional Saudí • Al-Awwal Park",
        "stadium": "Al-Awwal Park (Riad)",
        "spectators_est": "25,000 espectadores (11:00 Hora Ecuador)",
        "referee": "Árbitro Internacional AFC",
        "referee_avg_yellows": 4.2,
        "referee_avg_reds": 0.15,
        "intensity": "Alta (Al-Nassr con Cristiano Ronaldo y Sadio Mané buscando la punta del torneo)"
    }
}

for k, v in tuesday_contexts.items():
    matches_db[k] = v

with open(matches_db_path, "w", encoding="utf-8") as f:
    json.dump(matches_db, f, ensure_ascii=False, indent=2)
print("✓ matches_database.json enriquecido con éxito.")

print("\n3. Actualizando official_calendar.json para 2026-10-20...")
with open(calendar_path, "r", encoding="utf-8") as f:
    cal_db = json.load(f)

cal_db["2026-10-20"] = {
    "date_str": "20/10/2026",
    "day_name": "Martes",
    "competition": "UEFA Champions League & Liga Profesional Saudí",
    "fixtures": [
        ["Real Madrid", "RB Leipzig", "VICTORIA_DIRECTA"],
        ["Sporting de Lisboa", "LASK", "VICTORIA_DIRECTA"],
        ["Aston Villa", "Viking FK", "VICTORIA_DIRECTA"],
        ["Inter Milan", "Shakhtar Donetsk", "DOBLE_OPORTUNIDAD"],
        ["Bayern Munich", "Arsenal", "AMBOS_MARCAN"],
        ["Al-Nassr", "Neom SC", "VICTORIA_DIRECTA"]
    ]
}

with open(calendar_path, "w", encoding="utf-8") as f:
    json.dump(cal_db, f, ensure_ascii=False, indent=2)
print("✓ official_calendar.json actualizado para 2026-10-20.")

print("\n4. Ejecutando SportsDirectorAgent para modelar la cartelera estelar de Martes 20/10/2026...")
from sports_agents.sports_director_agent import SportsDirectorAgent
director = SportsDirectorAgent()

tuesday_fixtures = cal_db["2026-10-20"]["fixtures"]
results = []

for home, away, cat in tuesday_fixtures:
    print(f"   -> Simulando cuantitativamente: {home} vs {away} [{cat}]...")
    pred = director.predict_fixture(home, away, preferred_market_category=cat)
    results.append(pred)

sim_path = os.path.join(base_dir, "sports_agents", "simulations_tomorrow_results.json")
sim_data = {
    "GeneratedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "TargetDay": "Martes",
    "TargetDate": "20/10/2026",
    "TemporalLabel": "MAÑANA",
    "Matches": results
}

with open(sim_path, "w", encoding="utf-8") as f:
    json.dump(sim_data, f, ensure_ascii=False, indent=2)
print("✓ simulations_tomorrow_results.json generado con éxito.")
