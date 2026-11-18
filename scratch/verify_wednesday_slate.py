import json
import re

html_path = "c:/Users/jeanb/Documents/Antigravity Proyectos/Analisis deportivo/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    c = f.read()

assert "Carlos Alcaraz" in c, "Alcaraz missing"
assert "Alcoyano" in c, "Alcoyano missing"
assert "Tenerife" in c, "Tenerife missing"
assert "Cobolli" in c, "Cobolli missing"
assert "Nicaragua" in c, "Nicaragua missing"
assert "Utebo" in c, "Utebo missing"
assert "87.6%" in c, "Win rate 87.6% missing"
assert "$3,368.52" in c, "Bankroll missing"
assert "$24.90" in c, "User bankroll missing"
assert "Ciclo #136" in c, "Ciclo #136 missing"

matches = re.findall(r'<div id="match-(\d+)"', c)
assert len(matches) == 6, f"Expected 6 match views, found {len(matches)}"

rows = re.findall(r"<tr>\s*<td[^>]*>#(\d+)</td>", c)
print(f"Index HTML verification passed! Match views: {len(matches)}, Table rows: {len(rows)}")
assert len(rows) == 234, f"Expected 234 rows, found {len(rows)}"

# Check simulations_tomorrow_results.json
sim_path = "c:/Users/jeanb/Documents/Antigravity Proyectos/Analisis deportivo/sports_agents/simulations_tomorrow_results.json"
with open(sim_path, "r", encoding="utf-8") as f:
    sim = json.load(f)
assert sim.get("TargetDate") == "18/11/2026", f"TargetDate wrong: {sim.get('TargetDate')}"
assert len(sim.get("Matches", [])) == 6, f"Expected 6 recommendations in sim, found {len(sim.get('Matches', []))}"

# Check audit_history.json
audit_path = "c:/Users/jeanb/Documents/Antigravity Proyectos/Analisis deportivo/sports_agents/audit_history.json"
with open(audit_path, "r", encoding="utf-8") as f:
    audit = json.load(f)
assert audit["global_stats"]["total"] == 234
assert audit["global_stats"]["wins"] == 205
assert audit["global_stats"]["losses"] == 29
assert audit["global_stats"]["win_rate"] == 87.6

print("ALL VERIFICATIONS PASSED PERFECTLY!")
