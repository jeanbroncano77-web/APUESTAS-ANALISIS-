import sys
sys.path.insert(0, ".")
from sports_agents.sports_director_agent import SportsDirectorAgent

director = SportsDirectorAgent()

test_fixtures = [
    ("Grecia", "Alemania", "UEFA Nations League"),
    ("Alemania", "Serbia", "UEFA Nations League"),
    ("Dinamarca", "Portugal", "UEFA Nations League"),
    ("Real Madrid", "Villarreal", "LaLiga")
]

for h, a, t in test_fixtures:
    print(f"=== FIXTURE: {h} vs {a} ({t}) ===")
    res = director.predict_fixture(h, a)
    fija = res["la_fija_real"]
    print(f"LA FIJA: {fija['market']} -> {fija['selection']} (@{fija['odds']} | {fija['probability']}%)")
    print(f"Rationale: {fija['rationale']}")
    exact = res["score_prediction"]["exact_market_probabilities"]
    print(f"1X2: H={exact['home_win_pct']}%, D={exact['draw_pct']}%, A={exact['away_win_pct']}%")
    print(f"Over 0.5={exact['over_0_5_pct']}%, Under 4.5={exact['under_4_5_pct']}%, Blowout Away 2+={exact['away_minus_1_5_pct']}%\n")
