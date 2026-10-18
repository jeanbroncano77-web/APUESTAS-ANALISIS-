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

sunday_matches = [
    ("Liverpool", "Chelsea", "DOBLE_OPORTUNIDAD"),
    ("Wolverhampton", "Manchester City", "GOL_EQUIPO"),
    ("Atlético de Madrid", "Leganés", "DOBLE_OPORTUNIDAD"),
    ("AS Roma", "Inter Milan", "GOLES_OVER"),
    ("Villarreal", "Getafe", "DOBLE_OPORTUNIDAD"),
    ("River Plate", "Vélez Sarsfield", "GOLES_UNDER")
]

print("Simulando los 6 partidos estelares para DOMINGO 18 DE OCTUBRE 2026 (Reliability Shield 5.0)...")

results = []
for home, away, category in sunday_matches:
    print(f"  -> Modelando: {home} vs {away} [{category}]...")
    sim = director.predict_fixture(home, away, preferred_market_category=category)
    fija = sim.get("la_fija_real", {})
    tier = fija.get("confidence_tier", "TIER_1")
    print(f"     Fija: {fija.get('market')} -> {fija.get('selection')} @{fija.get('odds')} ({fija.get('probability')}%) [{tier}]")
    results.append(sim)

output_data = {
    "GeneratedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "TargetDay": "Domingo",
    "TargetDate": "18/10/2026",
    "TemporalLabel": "HOY DOMINGO",
    "CompetitionHeader": "Cartelera Estelar de DOMINGO • 18 de Octubre de 2026",
    "Matches": results
}

output_path = os.path.join(parent_dir, "sports_agents", "simulations_tomorrow_results.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("[EXITO] Domingo 18/10/2026 simulado con exito con el Escudo de Confiabilidad 5.0!")
