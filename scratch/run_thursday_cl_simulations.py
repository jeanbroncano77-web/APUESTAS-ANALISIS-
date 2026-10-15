import os
import sys
import json
from datetime import datetime

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(base_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from sports_agents import SportsDirectorAgent

director = SportsDirectorAgent()

thursday_fixtures = [
    ("Benfica", "Celtic", "DOBLE_OPORTUNIDAD"),
    ("Red Bull Salzburg", "AC Milan", "DOBLE_OPORTUNIDAD"),
    ("Celta Vigo", "Juventus", "DOBLE_OPORTUNIDAD"),
    ("Lech Poznań", "Bayer Leverkusen", "DOBLE_OPORTUNIDAD"),
    ("Olympique Lyon", "Crystal Palace", "DOBLE_OPORTUNIDAD"),
    ("Hajduk Split", "AFC Ajax", "DOBLE_OPORTUNIDAD")
]

print("Simulando los 6 partidos estelares de UEFA Europa League y Conference League para Jueves 15/10/2026...")
results = []
for home, away, cat in thursday_fixtures:
    print(f"  -> Modelando: {home} vs {away} [{cat}]...")
    pred = director.predict_fixture(home, away, preferred_market_category=cat)
    fija = pred.get("la_fija_real", {})
    print(f"     ⭐ Fija: {fija.get('market')} -> {fija.get('selection')} @{fija.get('odds')} ({fija.get('probability')}%)")
    results.append(pred)

sim_path = "sports_agents/simulations_tomorrow_results.json"
sim_data = {
    "GeneratedAt": "2026-10-14 22:00:00",
    "TargetDay": "Jueves",
    "TargetDate": "15/10/2026",
    "TemporalLabel": "MAÑANA",
    "CompetitionHeader": "UEFA Europa League & UEFA Conference League • Fase de Liga (Jornada 2)",
    "Matches": results
}

with open(sim_path, "w", encoding="utf-8") as f:
    json.dump(sim_data, f, ensure_ascii=False, indent=2)

print(f"\n[ÉXITO] {sim_path} actualizado con los 6 partidos para Jueves 15/10/2026!")
