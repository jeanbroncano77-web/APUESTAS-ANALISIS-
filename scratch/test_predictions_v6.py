# -*- coding: utf-8 -*-
import sys, os, json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo")

from sports_agents import SportsDirectorAgent

director = SportsDirectorAgent()

fixtures = [
    ("Liverpool", "Chelsea", "DOBLE_OPORTUNIDAD"),
    ("Wolverhampton", "Manchester City", "VICTORIA_DIRECTA"),
    ("Atlético de Madrid", "Leganés", "VICTORIA_DIRECTA"),
    ("AS Roma", "Inter Milan", "AMBOS_ANOTAN"),
    ("Villarreal", "Getafe", "VICTORIA_DIRECTA"),
    ("River Plate", "Vélez Sarsfield", "DOBLE_OPORTUNIDAD")
]

print("=== PROBANDO SELECCIÓN V6.0 PARA LOS 6 PARTIDOS DE HOY/DOMINGO ===")
for home, away, cat in fixtures:
    res = director.predict_fixture(home, away, preferred_market_category=cat)
    fija = res["la_fija_real"]
    print(f"\n⚽ {home} vs {away} [{cat}]:")
    print(f"   -> 1X2 Probs: H={res['score_prediction']['1x2_probabilities']['home_win_pct']}% | D={res['score_prediction']['1x2_probabilities']['draw_pct']}% | A={res['score_prediction']['1x2_probabilities']['away_win_pct']}%")
    print(f"   -> ⭐ LA FIJA: {fija.get('selection')} @ {fija.get('odds')} ({fija.get('probability')}%) [{fija.get('category_code')}]")
    print(f"   -> Rationale: {fija.get('rationale')}")
