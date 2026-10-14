import os
import sys
import json
from datetime import datetime

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from sports_agents import SportsDirectorAgent

fixtures = [
    ("Atalanta", "Venezia", "DOBLE_OPORTUNIDAD"),
    ("Coventry City", "Newcastle", "DOBLE_OPORTUNIDAD"),
    ("Levante", "Sevilla", "DOBLE_OPORTUNIDAD"),
    ("Torino", "Udinese", "DOBLE_OPORTUNIDAD"),
    ("Racing Club", "Belgrano", "DOBLE_OPORTUNIDAD"),
    ("Bahia", "Mirassol", "DOBLE_OPORTUNIDAD")
]

director = SportsDirectorAgent()
results = []

print("Simulando los 6 partidos reales de Lunes 12 de Octubre de 2026...")
for home, away, cat in fixtures:
    print(f"-> Modelando: {home} vs {away} [{cat}]...")
    pred = director.predict_fixture(home, away, preferred_market_category=cat)
    fija = pred.get("la_fija_real", {})
    print(f"   ⭐ Fija: {fija.get('market')} -> {fija.get('selection')} @{fija.get('odds')} ({fija.get('probability')}%)")
    results.append(pred)

sim_file = os.path.join(base_dir, "sports_agents", "simulations_tomorrow_results.json")
sim_data = {
    "GeneratedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "TargetDay": "Lunes",
    "TargetDate": "12/10/2026",
    "TemporalLabel": "MAÑANA",
    "Matches": results
}

with open(sim_file, "w", encoding="utf-8") as f_sim:
    json.dump(sim_data, f_sim, ensure_ascii=False, indent=2)

print("simulations_tomorrow_results.json generado con éxito con los 6 partidos reales de LUNES.")
