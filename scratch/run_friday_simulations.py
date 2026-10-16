# -*- coding: utf-8 -*-
"""
Run simulations EXCLUSIVELY for TOMORROW: Viernes 16 de Octubre de 2026.
Matches:
1. Boca Juniors vs Talleres [DOBLE_OPORTUNIDAD] -> La Fija de Oro de Viernes
2. Banfield vs Lanús [TARJETAS] -> Clásico del Sur (Mercado de Tarjetas)
3. Defensa y Justicia vs Instituto [DOBLE_OPORTUNIDAD]
4. Cruzeiro vs Liga de Quito [DOBLE_OPORTUNIDAD]
5. Sarmiento vs Aldosivi [GOLES_UNDER]
6. Atlético Tucumán vs Central Córdoba [DOBLE_OPORTUNIDAD]
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

friday_matches_to_simulate = [
    ("Boca Juniors", "Talleres", "DOBLE_OPORTUNIDAD"),
    ("Banfield", "Lanús", "TARJETAS"),
    ("Defensa y Justicia", "Instituto", "DOBLE_OPORTUNIDAD"),
    ("Cruzeiro", "Liga de Quito", "DOBLE_OPORTUNIDAD"),
    ("Sarmiento", "Aldosivi", "GOLES_UNDER"),
    ("Atlético Tucumán", "Central Córdoba", "DOBLE_OPORTUNIDAD")
]

print("Simulando los 6 partidos estelares EXCLUSIVAMENTE para MAÑANA VIERNES 16 DE OCTUBRE 2026...")

results = []
for home, away, category in friday_matches_to_simulate:
    print(f"  -> Modelando: {home} vs {away} [{category}]...")
    sim = director.predict_fixture(home, away, preferred_market_category=category)
    fija = sim.get("la_fija_real", {})
    print(f"     ⭐ Fija: {fija.get('market')} -> {fija.get('selection')} @{fija.get('odds')} ({fija.get('probability')}%)")
    results.append(sim)

output_data = {
    "GeneratedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "TargetDay": "Viernes",
    "TargetDate": "16/10/2026",
    "TemporalLabel": "MAÑANA VIERNES",
    "CompetitionHeader": "Cartelera Estelar de MAÑANA • Viernes 16 de Octubre de 2026",
    "Matches": results
}

output_path = "sports_agents/simulations_tomorrow_results.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"\n[ÉXITO] {output_path} actualizado EXCLUSIVAMENTE con la cartelera de MAÑANA VIERNES 16/10/2026!")
