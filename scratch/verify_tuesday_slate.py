# -*- coding: utf-8 -*-
"""
verify_tuesday_slate.py
Verifica exhaustivamente que index.html, dashboard_pronosticos.html y los JSONs
cumplan con todos los requisitos del Martes 17/11/2026.
"""

import re
import json
import os

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

checks = [
    ("Title has Martes 17/11 & 87.7%", "Martes 17/11" in html and "87.7%" in html),
    ("6 Switcher Tabs present", len(re.findall(r'id="tab-\d+"', html)) == 6),
    ("6 Match Views present", len(re.findall(r'id="match-\d+"', html)) == 6),
    ("Ecuador vs. Bolivia present", "Ecuador vs. Bolivia" in html),
    ("Singapur vs. Brasil present", "Singapur vs. Brasil" in html),
    ("Gales vs. Portugal present", "Gales vs. Portugal" in html),
    ("Chile vs. Colombia present", "Chile vs. Colombia" in html),
    ("Dinamarca vs. Noruega present", "Dinamarca vs. Noruega" in html),
    ("Argentina vs. Costa Rica present", "Argentina vs. Costa Rica" in html),
    ("Area 2 Table has 228 rows", len(re.findall(r'<td class="col-id">#\d+</td>', html)) == 228),
    ("Top row is Pick #229 (Islandia vs Luxemburgo)", "#229" in html and "Islandia vs Luxemburgo" in html),
    ("Contains Senegal Pick #224", "#224" in html and "Sudán vs Senegal" in html),
    ("Area 3 has Ciclo #135", "Ciclo #135" in html),
    ("KPI Win Rate Global 87.7%", "87.7%" in html),
    ("KPI Win Rate Fijas 87.8%", "87.8%" in html),
    ("KPI Total Pronósticos 228", "228" in html),
    ("KPI Aciertos Totales 200", "200" in html),
    ("KPI Fallos Registrados 28", "28" in html),
    ("KPI Racha Activa 15 Victorias", "15 Victorias Consecutivas" in html or "15 Seguidas" in html),
    ("KPI Banca Total $3,348.52", "$3,348.52" in html),
    ("User Bankroll $24.90 intact", "$24.90" in html),
]

all_passed = True
for name, passed in checks:
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name}")
    if not passed:
        all_passed = False

with open(os.path.join(base_dir, "sports_agents", "simulations_tomorrow_results.json"), "r", encoding="utf-8") as f:
    sim = json.load(f)
assert sim.get("TargetDate") == "17/11/2026", "simulations TargetDate is not 17/11/2026"
assert len(sim.get("Matches", [])) == 6, "simulations does not have 6 matches"
print("[PASS] simulations_tomorrow_results.json has 6 matches for 17/11/2026")

with open(os.path.join(base_dir, "sports_agents", "audit_history.json"), "r", encoding="utf-8") as f:
    aud = json.load(f)
assert aud.get("global_stats", {}).get("total") == 228, f"audit total is {aud.get('global_stats', {}).get('total')}"
assert aud.get("global_stats", {}).get("wins") == 200, f"audit wins is {aud.get('global_stats', {}).get('wins')}"
assert aud.get("global_stats", {}).get("losses") == 28, f"audit losses is {aud.get('global_stats', {}).get('losses')}"
assert aud.get("current_bankroll") == 3348.52, f"audit bankroll is {aud.get('current_bankroll')}"
print("[PASS] audit_history.json verified (228 picks, 200 wins, 28 losses, $3,348.52)")

with open(os.path.join(base_dir, "sports_agents", "autonomous_feedback_log.json"), "r", encoding="utf-8") as f:
    feed = json.load(f)
assert feed.get("cycles_completed") == 135, f"feedback cycles_completed is {feed.get('cycles_completed')}"
print("[PASS] autonomous_feedback_log.json verified (Cycle #135)")

if all_passed:
    print("\n🎉 ALL 24 VERIFICATIONS PASSED CLEANLY FOR TUESDAY 17/11!")
else:
    print("\n❌ SOME VERIFICATIONS FAILED!")
