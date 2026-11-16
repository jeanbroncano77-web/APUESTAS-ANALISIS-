# -*- coding: utf-8 -*-
"""
verify_monday_slate.py
Verifica integralmente que index.html y los archivos JSON cumplan con todos los requisitos.
"""

import re
import json
import os

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

checks = [
    ("Title has Lunes 16/11 & 87.4%", "Lunes 16/11" in html and "87.4%" in html),
    ("6 Switcher Tabs present", len(re.findall(r'id="tab-\d+"', html)) == 6),
    ("6 Match Views present", len(re.findall(r'id="match-\d+"', html)) == 6),
    ("Alemania vs. Países Bajos present", "Alemania vs. Países Bajos" in html),
    ("Suiza vs. Escocia present", "Suiza vs. Escocia" in html),
    ("Sudán vs. Senegal present", "Sudán vs. Senegal" in html),
    ("Namibia vs. Camerún present", "Namibia vs. Camerún" in html),
    ("Lituania vs. Liechtenstein present", "Lituania vs. Liechtenstein" in html),
    ("Islandia vs. Luxemburgo present", "Islandia vs. Luxemburgo" in html),
    ("Area 2 Table has 222 rows", len(re.findall(r'<td class="col-id">#\d+</td>', html)) == 222),
    ("Area 3 has Ciclo #134", "Ciclo #134" in html),
    ("KPI Win Rate Global 87.4%", "87.4%" in html),
    ("KPI Total Pronósticos 222", "222" in html),
    ("KPI Aciertos Totales 194", "194" in html),
    ("KPI Fallos Registrados 28", "28" in html),
    ("KPI Racha Activa 9 Victorias", "Racha activa: 9 Victorias Consecutivas" in html),
    ("KPI Banca Total $3,199.52", "$3,199.52" in html),
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
assert sim.get("TargetDate") == "16/11/2026", "simulations TargetDate is not 16/11/2026"
assert len(sim.get("Matches", [])) == 6, "simulations does not have 6 matches"
print("[PASS] simulations_tomorrow_results.json has 6 matches for 16/11/2026")

with open(os.path.join(base_dir, "sports_agents", "audit_history.json"), "r", encoding="utf-8") as f:
    aud = json.load(f)
assert aud.get("global_stats", {}).get("total") == 222, "audit total is not 222"
assert aud.get("global_stats", {}).get("wins") == 194, "audit wins is not 194"
assert aud.get("global_stats", {}).get("losses") == 28, "audit losses is not 28"
assert aud.get("current_bankroll") == 3199.52, "audit bankroll is not 3199.52"
print("[PASS] audit_history.json verified (222 picks, 194 wins, 28 losses, $3,199.52)")

with open(os.path.join(base_dir, "sports_agents", "autonomous_feedback_log.json"), "r", encoding="utf-8") as f:
    feed = json.load(f)
assert feed.get("cycles_completed") == 134, "feedback cycles_completed is not 134"
print("[PASS] autonomous_feedback_log.json verified (Cycle #134)")

if all_passed:
    print("\n🎉 ALL 21 VERIFICATIONS PASSED CLEANLY!")
else:
    print("\n❌ SOME VERIFICATIONS FAILED!")
