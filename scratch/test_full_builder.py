# -*- coding: utf-8 -*-
"""
test_full_builder.py
Prueba del generador unificado integral de las 3 Áreas.
"""
import os
import sys
import json
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")
sim_path = os.path.join(base_dir, "sports_agents", "simulations_tomorrow_results.json")
audit_path = os.path.join(base_dir, "sports_agents", "audit_history.json")
feedback_path = os.path.join(base_dir, "sports_agents", "autonomous_feedback_log.json")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

with open(sim_path, "r", encoding="utf-8") as f:
    sim_data = json.load(f)

with open(audit_path, "r", encoding="utf-8") as f:
    audit_data = json.load(f)

with open(feedback_path, "r", encoding="utf-8") as f:
    fb_data = json.load(f)

# 1. Verificar reemplazo de allFijasData
fijas_js = "var allFijasData = [\n"
for idx, m in enumerate(sim_data["Matches"]):
    home = m.get("home_team", "")
    away = m.get("away_team", "")
    fija = m.get("la_fija_real", {})
    pick = fija.get("selection", "Gol de Equipo / Doble Oportunidad")
    prob = fija.get("probability", 95.0)
    odds = fija.get("odds", 1.15)
    fijas_js += f"            {{ id: {idx}, match: '{home} vs {away}', pick: '{pick}', prob: {prob}, odds: {odds} }},\n"
fijas_js = fijas_js.rstrip(",\n") + "\n        ];"
print("Fijas JS snippet:")
print(fijas_js)

# 2. Verificar reemplazo de chartConfigs
chart_js = "var chartConfigs = [\n"
for idx, m in enumerate(sim_data["Matches"]):
    home = m.get("home_team", "")
    away = m.get("away_team", "")
    probs = m.get("score_prediction", {}).get("1x2_probabilities", {})
    hw = round(probs.get("home_win_pct", 33.3), 1)
    dr = round(probs.get("draw_pct", 33.4), 1)
    aw = round(probs.get("away_win_pct", 33.3), 1)
    chart_js += f"            {{ id: 'chart1X2-{idx}', labels: ['{home} (1)', 'Empate (X)', '{away} (2)'], data: [{hw}, {dr}, {aw}] }},\n"
chart_js = chart_js.rstrip(",\n") + "\n        ];"
print("\nChart JS snippet:")
print(chart_js)
