import sys
sys.path.append(".")
from sports_agents.sports_director_agent import SportsDirectorAgent

director = SportsDirectorAgent()

fixtures = [
    ("Real Madrid", "Sevilla", "VICTORIA_DIRECTA"),
    ("Barcelona", "Getafe", "VICTORIA_DIRECTA"),
    ("River Plate", "Vélez Sarsfield", "DOBLE_OPORTUNIDAD"),
    ("Olympique de Marseille", "Montpellier", "VICTORIA_DIRECTA"),
    ("Fiorentina", "Lecce", "DOBLE_OPORTUNIDAD"),
    ("Bayern Munich", "VfB Stuttgart", "VICTORIA_DIRECTA")
]

for home, away, cat in fixtures:
    pred = director.predict_fixture(home, away, preferred_market_category=cat)
    fija = pred.get("la_fija_real", {})
    print(f"{home} vs {away} [{cat}]:")
    print(f"   Selection: {fija.get('selection')}")
    print(f"   Odds: {fija.get('odds')} | Market: {fija.get('market_type')}")
    print(f"   Confidence: {fija.get('confidence')}% | Prob: {fija.get('probability')}%")
