# -*- coding: utf-8 -*-
import os
import sys
import json
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"

with open(os.path.join(base_dir, "sports_agents", "simulations_tomorrow_results.json"), "r", encoding="utf-8") as f:
    sim_data = json.load(f)

print("=== SIMULATIONS_TOMORROW_RESULTS.JSON ===")
print("Day:", sim_data.get("TargetDay"), sim_data.get("TargetDate"))
for idx, m in enumerate(sim_data.get("Matches", [])):
    h = m.get("home_team")
    a = m.get("away_team")
    fija = m.get("la_fija_real", {})
    score = m.get("score_prediction", {}).get("most_probable_score", "")
    print(f" {idx+1}. {h} vs {a} | Score: {score} | Fija: {fija.get('selection')} @{fija.get('odds')} ({fija.get('probability')}%)")

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

print("\n=== INDEX.HTML SWITCHER TABS ===")
tabs = re.findall(r'<div class="switcher-teams">\s*<span>([^<]+)</span>\s*<span class="vs-text">vs</span>\s*<span>([^<]+)</span>', html)
for idx, (h, a) in enumerate(tabs):
    print(f" Tab {idx+1}: {h.strip()} vs {a.strip()}")

print("\n=== JAVASCRIPT allFijasData in INDEX.HTML ===")
js_match = re.search(r'var allFijasData = (\[[\s\S]*?\]);', html)
if js_match:
    print(js_match.group(1)[:500])

print("\n=== KPIS in INDEX.HTML ===")
kpi_matches = re.findall(r'<div class="kpi-num"[^>]*>([^<]+)</div>', html)
print("KPI numbers:", kpi_matches[:8])
