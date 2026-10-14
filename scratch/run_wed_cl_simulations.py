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

wed_fixtures = [
    ("Manchester City", "Paris Saint-Germain", "DOBLE_OPORTUNIDAD"),
    ("Roma", "Real Madrid", "DOBLE_OPORTUNIDAD"),
    ("LASK", "Liverpool", "DOBLE_OPORTUNIDAD"),
    ("Bodø/Glimt", "Borussia Dortmund", "DOBLE_OPORTUNIDAD"),
    ("Aston Villa", "Fenerbahçe", "DOBLE_OPORTUNIDAD"),
    ("Feyenoord", "Como", "DOBLE_OPORTUNIDAD")
]

print("Simulando los 6 partidos estelares de UEFA Champions League para Miércoles 14/10/2026...")
results = []
for home, away, cat in wed_fixtures:
    print(f"  -> Modelando: {home} vs {away} [{cat}]...")
    pred = director.predict_fixture(home, away, preferred_market_category=cat)
    fija = pred.get("la_fija_real", {})
    print(f"     ⭐ Fija: {fija.get('market')} -> {fija.get('selection')} @{fija.get('odds')} ({fija.get('probability')}%)")
    results.append(pred)

sim_path = "sports_agents/simulations_tomorrow_results.json"
sim_data = {
    "GeneratedAt": "2026-10-13 21:35:00",
    "TargetDay": "Miércoles",
    "TargetDate": "14/10/2026",
    "TemporalLabel": "MAÑANA",
    "CompetitionHeader": "UEFA Champions League • Fase de Liga (Jornada 2 - Noche Estelar)",
    "Matches": results
}

with open(sim_path, "w", encoding="utf-8") as f:
    json.dump(sim_data, f, ensure_ascii=False, indent=2)

print(f"\n[ÉXITO] {sim_path} actualizado con los 6 partidos de UEFA Champions League para Miércoles 14/10/2026!")
