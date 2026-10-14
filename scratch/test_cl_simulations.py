import os
import sys
import json

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(base_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from sports_agents import SportsDirectorAgent

director = SportsDirectorAgent()

fixtures = [
    ("Galatasaray", "Barcelona", "DOBLE_OPORTUNIDAD"),
    ("Arsenal", "Lille", "DOBLE_OPORTUNIDAD"),
    ("Atlético de Madrid", "Manchester United", "DOBLE_OPORTUNIDAD"),
    ("Inter Milan", "Club Brugge", "DOBLE_OPORTUNIDAD"),
    ("Viking FK", "Bayern Munich", "GOL_EQUIPO"),
    ("Villarreal", "Napoli", "DOBLE_OPORTUNIDAD")
]

print("Simulating 6 Champions League fixtures...")
results = []
for home, away, cat in fixtures:
    print(f"\n--- {home} vs {away} [{cat}] ---")
    pred = director.predict_fixture(home, away, preferred_market_category=cat)
    fija = pred.get("la_fija_real", {})
    print(f"Selection: {fija.get('selection')} | Cuota: @{fija.get('odds')} | Conf: {fija.get('probability')}%")
    results.append(pred)

print(f"\nAll {len(results)} matches simulated successfully!")
