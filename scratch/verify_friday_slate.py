import json
import re

html_path = "c:/Users/jeanb/Documents/Antigravity Proyectos/Analisis deportivo/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    c = f.read()

assert "Independiente del Valle" in c, "IDV missing"
assert "Macará" in c, "Macará missing"
assert "Bayern Múnich" in c, "Bayern missing"
assert "FC Köln" in c, "Köln missing"
assert "Athletic Club" in c, "Athletic missing"
assert "España Sub-17" in c, "España Sub-17 missing"
assert "Deportivo Cali" in c, "Cali missing"
assert "Millonarios" in c, "Millonarios missing"
assert "FC Metz" in c, "Metz missing"
assert "88.2%" in c, "Win rate 88.2% missing"
assert "$3,665.52" in c, "Bankroll missing"
assert "$24.90" in c, "User bankroll missing"
assert "Ciclo #138" in c, "Ciclo #138 missing"

matches = re.findall(r'<div id="match-(\d+)"', c)
assert len(matches) == 6, f"Expected 6 match views, found {len(matches)}"

# Filas de tabla
rows = re.findall(r'<td class="col-id">#(\d+)</td>', c)
print(f"Index HTML verification passed! Match views: {len(matches)}, Table rows: {len(rows)}")
assert len(rows) == 246, f"Expected 246 rows, found {len(rows)}"

# Check simulations_tomorrow_results.json
sim_path = "c:/Users/jeanb/Documents/Antigravity Proyectos/Analisis deportivo/sports_agents/simulations_tomorrow_results.json"
with open(sim_path, "r", encoding="utf-8") as f:
    sim = json.load(f)
assert sim.get("TargetDate") == "20/11/2026", f"TargetDate wrong: {sim.get('TargetDate')}"
assert len(sim.get("Matches", [])) == 6, f"Expected 6 recommendations in sim, found {len(sim.get('Matches', []))}"

# Check audit_history.json
audit_path = "c:/Users/jeanb/Documents/Antigravity Proyectos/Analisis deportivo/sports_agents/audit_history.json"
with open(audit_path, "r", encoding="utf-8") as f:
    audit = json.load(f)
assert audit["global_stats"]["total"] == 246, f"Audit total wrong: {audit['global_stats']['total']}"
assert audit["global_stats"]["wins"] == 217, f"Audit wins wrong: {audit['global_stats']['wins']}"
assert audit["global_stats"]["losses"] == 29, f"Audit losses wrong: {audit['global_stats']['losses']}"
assert audit["global_stats"]["win_rate"] == 88.2, f"Audit win rate wrong: {audit['global_stats']['win_rate']}"
assert audit["current_bankroll"] == 3665.52, f"Bankroll wrong: {audit['current_bankroll']}"

# Check autonomous_feedback_log.json
fb_path = "c:/Users/jeanb/Documents/Antigravity Proyectos/Analisis deportivo/sports_agents/autonomous_feedback_log.json"
with open(fb_path, "r", encoding="utf-8") as f:
    fb = json.load(f)
cycles = [c["cycle"] for c in fb.get("calibrations", [])]
assert 138 in cycles, "Cycle 138 not found in calibrations"

print("ALL FRIDAY 20/11 VERIFICATIONS PASSED PERFECTLY!")
