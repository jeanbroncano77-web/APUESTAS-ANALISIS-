# -*- coding: utf-8 -*-
"""
Run weekend simulations for Friday 16 / Saturday 17 October 2026:
Matches:
1. Borussia Dortmund vs St. Pauli [DOBLE_OPORTUNIDAD] -> La Fija de Oro Local
2. Celta de Vigo vs Real Madrid [TARJETAS] -> La Fija Estelar de Tarjetas en LaLiga (Sugerencia Usuario)
3. Barcelona vs Sevilla [DOBLE_OPORTUNIDAD]
4. Paris Saint-Germain vs Marseille [DOBLE_OPORTUNIDAD]
5. Arsenal vs Crystal Palace [DOBLE_OPORTUNIDAD]
6. Roma vs Inter Milan [DOBLE_OPORTUNIDAD]
"""
import os
import sys
import json
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(base_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from sports_agents import SportsDirectorAgent

director = SportsDirectorAgent()

matches_to_simulate = [
    ("Borussia Dortmund", "St. Pauli", "DOBLE_OPORTUNIDAD"),
    ("Celta de Vigo", "Real Madrid", "TARJETAS"),
    ("Barcelona", "Sevilla", "DOBLE_OPORTUNIDAD"),
    ("Paris Saint-Germain", "Marseille", "DOBLE_OPORTUNIDAD"),
    ("Arsenal", "Crystal Palace", "DOBLE_OPORTUNIDAD"),
    ("Roma", "Inter Milan", "DOBLE_OPORTUNIDAD")
]

print("Simulando los 6 partidos estelares para Viernes 16 / Sábado 17 de Octubre 2026...")

results = []
for home, away, category in matches_to_simulate:
    print(f"  -> Modelando: {home} vs {away} [{category}]...")
    sim = director.predict_fixture(home, away, preferred_market_category=category)
    fija = sim.get("la_fija_real", {})
    print(f"     ⭐ Fija: {fija.get('market')} -> {fija.get('selection')} @{fija.get('odds')} ({fija.get('probability')}%)")
    results.append(sim)

output_data = {
    "GeneratedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "TargetDay": "Viernes / Sábado",
    "TargetDate": "16/10/2026 - 17/10/2026",
    "TemporalLabel": "HOY Y MAÑANA",
    "Matches": results
}

output_path = "sports_agents/simulations_tomorrow_results.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"\n[ÉXITO] {output_path} actualizado con los 6 partidos estelares de Viernes y Fin de Semana!")
