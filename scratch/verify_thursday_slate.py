import json
import re

html_path = "c:/Users/jeanb/Documents/Antigravity Proyectos/Analisis deportivo/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    c = f.read()

assert "Nueva Caledonia" in c, "Nueva Caledonia missing"
assert "Ecuador Sub-17" in c, "Ecuador Sub-17 missing"
assert "FC Barcelona" in c, "FC Barcelona missing"
assert "Argentina" in c, "Argentina missing"
assert "Bayern" in c, "Bayern missing"
assert "Peñarol" in c, "Peñarol missing"
assert "São Paulo" in c, "São Paulo missing"
assert "87.9%" in c, "Win rate 87.9% missing"
assert "$3,523.52" in c, "Bankroll missing"
assert "$24.90" in c, "User bankroll missing"
assert "Ciclo #137" in c, "Ciclo #137 missing"

matches = re.findall(r'<div id="match-(\d+)"', c)
assert len(matches) == 6, f"Expected 6 match views, found {len(matches)}"

# Filas de tabla
rows = re.findall(r'<td class="col-id">#(\d+)</td>', c)
print(f"Index HTML verification passed! Match views: {len(matches)}, Table rows: {len(rows)}")
assert len(rows) == 240, f"Expected 240 rows, found {len(rows)}"

# Check simulations_tomorrow_results.json
sim_path = "c:/Users/jeanb/Documents/Antigravity Proyectos/Analisis deportivo/sports_agents/simulations_tomorrow_results.json"
with open(sim_path, "r", encoding="utf-8") as f:
    sim = json.load(f)
assert sim.get("TargetDate") == "19/11/2026", f"TargetDate wrong: {sim.get('TargetDate')}"
assert len(sim.get("Matches", [])) == 6, f"Expected 6 recommendations in sim, found {len(sim.get('Matches', []))}"

# Check audit_history.json
audit_path = "c:/Users/jeanb/Documents/Antigravity Proyectos/Analisis deportivo/sports_agents/audit_history.json"
with open(audit_path, "r", encoding="utf-8") as f:
    audit = json.load(f)
assert audit["global_stats"]["total"] == 240, f"Audit total wrong: {audit['global_stats']['total']}"
assert audit["global_stats"]["wins"] == 211, f"Audit wins wrong: {audit['global_stats']['wins']}"
assert audit["global_stats"]["losses"] == 29, f"Audit losses wrong: {audit['global_stats']['losses']}"
assert audit["global_stats"]["win_rate"] == 87.9, f"Audit win rate wrong: {audit['global_stats']['win_rate']}"
assert audit["current_bankroll"] == 3523.52, f"Bankroll wrong: {audit['current_bankroll']}"

# Check autonomous_feedback_log.json
fb_path = "c:/Users/jeanb/Documents/Antigravity Proyectos/Analisis deportivo/sports_agents/autonomous_feedback_log.json"
with open(fb_path, "r", encoding="utf-8") as f:
    fb = json.load(f)
cycles = [c["cycle"] for c in fb.get("calibrations", [])]
assert 137 in cycles, "Cycle 137 not found in calibrations"

print("ALL THURSDAY 19/11 VERIFICATIONS PASSED PERFECTLY!")
