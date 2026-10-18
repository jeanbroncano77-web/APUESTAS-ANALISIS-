# -*- coding: utf-8 -*-
import sys, os

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo")
from sports_agents import SportsDirectorAgent
director = SportsDirectorAgent()

test_fixtures = [
    ("Celta de Vigo", "Real Madrid", "VICTORIA_DIRECTA"),
    ("Wolverhampton", "Manchester City", "VICTORIA_DIRECTA"),
    ("Atlético de Madrid", "Leganés", "VICTORIA_DIRECTA"),
    ("Liverpool", "Chelsea", "DOBLE_OPORTUNIDAD"),
    ("AS Roma", "Inter Milan", "AMBOS_ANOTAN"),
    ("Villarreal", "Getafe", "VICTORIA_DIRECTA")
]

print("=== VERIFICANDO LA CARTELERA DEL DOMINGO 18 DE OCTUBRE CON EL REAL MADRID ===")
for h, a, cat in test_fixtures:
    res = director.predict_fixture(h, a, preferred_market_category=cat)
    fija = res["la_fija_real"]
    print(f"{h} vs {a}:")
    print(f"   -> Fija: {fija.get('selection')} @ {fija.get('odds')} ({fija.get('probability')}%) [{fija.get('category_code')}]")
    print(f"   -> Rationale: {fija.get('rationale')}")
