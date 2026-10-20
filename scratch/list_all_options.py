import os
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
sim_file = os.path.join(base_dir, "sports_agents", "simulations_tomorrow_results.json")

with open(sim_file, "r", encoding="utf-8") as f:
    d = json.load(f)

for m in d["Matches"]:
    print(f"\n=== {m['match']} ===")
    opts = m.get("all_fija_options", [])
    for opt in opts:
        code = opt.get("category_code")
        sel = opt.get("selection")
        odds = opt.get("odds")
        prob = opt.get("probability")
        rat = opt.get("rationale")
        print(f"  [{code}] {sel} @{odds} ({prob}%)")
        print(f"       -> {rat}")
