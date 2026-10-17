# -*- coding: utf-8 -*-
import os
import sys
import json
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(base_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from sports_agents import SportsDirectorAgent

director = SportsDirectorAgent()

saturday_matches = [
    ("Real Betis", "Barcelona", "DOBLE_OPORTUNIDAD"),
    ("Real Madrid", "Sevilla", "DOBLE_OPORTUNIDAD"),
    ("Manchester City", "Ipswich Town", "GOL_EQUIPO"),
    ("Bayern Munich", "RB Leipzig", "GOLES_OVER"),
    ("AS Roma", "Genoa", "DOBLE_OPORTUNIDAD"),
    ("Banfield", "Lanús", "TARJETAS")
]

print("Simulando los 6 partidos estelares para SÁBADO 17 DE OCTUBRE 2026...")

results = []
for home, away, category in saturday_matches:
    print(f"  -> Modelando: {home} vs {away} [{category}]...")
    sim = director.predict_fixture(home, away, preferred_market_category=category)
    fija = sim.get("la_fija_real", {})
    print(f"     Fija: {fija.get('market')} -> {fija.get('selection')} @{fija.get('odds')} ({fija.get('probability')}%)")
    results.append(sim)

output_data = {
    "GeneratedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "TargetDay": "Sábado",
    "TargetDate": "17/10/2026",
    "TemporalLabel": "HOY SÁBADO",
    "CompetitionHeader": "Cartelera Estelar • Sábado 17 de Octubre de 2026",
    "Matches": results
}

output_path = os.path.join(parent_dir, "sports_agents", "simulations_tomorrow_results.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("[ÉXITO] Sábado 17/10/2026 simulado con éxito.")
