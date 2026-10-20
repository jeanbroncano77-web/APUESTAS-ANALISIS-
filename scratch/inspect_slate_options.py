import os
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
sim_file = os.path.join(base_dir, "sports_agents", "simulations_tomorrow_results.json")

with open(sim_file, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Date: {data.get('TargetDay')} {data.get('TargetDate')}")
for idx, m in enumerate(data.get("Matches", []), 1):
    h = m.get("home_team")
    a = m.get("away_team")
    probs = m.get("score_prediction", {}).get("1x2_probabilities", {})
    modal = m.get("score_prediction", {}).get("most_probable_score", "1-0")
    fija = m.get("la_fija_real", {})
    markets = m.get("betting_markets", {})
    xg = m.get("projections", {}).get("expected_goals", {})

    print(f"\n[{idx}] {h} vs {a}")
    print(f"    xG: {h} {xg.get('home')} - {a} {xg.get('away')} (Total: {xg.get('total')})")
    print(f"    1X2 Probs: 1: {probs.get('home_win_pct')}% | X: {probs.get('draw_pct')}% | 2: {probs.get('away_win_pct')}%")
    print(f"    Modal Score: {modal}")
    print(f"    ⭐ LA FIJA: {fija.get('market')} -> {fija.get('selection')} @{fija.get('odds')} ({fija.get('probability')}%)")
    
    # print all markets
    print("    Mercados Clave:")
    for m_cat, m_opts in markets.items():
        if isinstance(m_opts, list):
            for opt in m_opts[:2]:
                print(f"      - {m_cat}: {opt.get('selection')} @{opt.get('odds')} ({opt.get('probability')}%)")
