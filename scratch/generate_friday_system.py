# -*- coding: utf-8 -*-
"""
generate_friday_system.py
Genera y simula la cartelera oficial de MAÑANA VIERNES con los 11 agentes de inteligencia deportiva:
1. Borussia Dortmund vs St. Pauli (Bundesliga)
2. Napoli vs Como (Serie A - Fija de Oro)
3. Marseille vs Angers (Ligue 1)
4. Leganés vs Valencia (LaLiga EA Sports)
5. Sunderland vs Leeds United (EFL Championship)
6. Rio Ave vs Famalicão (Liga Portugal)
"""

import os
import sys
import json
from datetime import datetime

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from sports_agents import SportsDirectorAgent
from sports_agents.whatsapp_notifier_agent import WhatsAppNotifierAgent

def main():
    print("=" * 60)
    print("EJECUTANDO SIMULACIÓN PARA MAÑANA VIERNES (02/10/2026)")
    print("=" * 60)

    director = SportsDirectorAgent()

    friday_fixtures = [
        ("Borussia Dortmund", "St. Pauli"),
        ("Napoli", "Como"),
        ("Marseille", "Angers"),
        ("Leganés", "Valencia"),
        ("Sunderland", "Leeds United"),
        ("Rio Ave", "Famalicão")
    ]

    results = []
    for h, a in friday_fixtures:
        print(f"Simulando con los 11 agentes: {h} vs {a}...")
        pred = director.predict_fixture(h, a)
        results.append(pred)

    sim_file = os.path.join(base_dir, "sports_agents", "simulations_tomorrow_results.json")
    with open(sim_file, "w", encoding="utf-8") as f:
        json.dump({
            "GeneratedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "TargetDay": "Viernes",
            "TargetDate": "2026-10-02",
            "Matches": results
        }, f, ensure_ascii=False, indent=2)

    print("simulations_tomorrow_results.json guardado con éxito con la cartelera de VIERNES.")

if __name__ == "__main__":
    main()
