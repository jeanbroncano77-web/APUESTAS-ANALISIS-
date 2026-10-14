import re

html = open("index.html", encoding="utf-8").read()

print("Search for 'Atalanta':", "Atalanta" in html)
print("Search for 'Corinthians':", "Corinthians" in html)
print("Search for 'audit-table':", "audit-table" in html)
print("Search for 'Liverpool':", "Liverpool" in html)

# Let's find tr tags
trs = re.findall(r'<tr[^>]*>', html)
print(f"Total <tr tags: {len(trs)}")
if trs:
    print("Sample trs:", trs[:5])

# Let's find sections or headings
headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', html)
print("Headings sample:", headings[:10])

# Let's find matches in simulations_tomorrow_results.json vs index.html
import json
with open("sports_agents/simulations_tomorrow_results.json", encoding="utf-8") as f:
    sim = json.load(f)
print("Sim TargetDay:", sim.get("TargetDay"), "TargetDate:", sim.get("TargetDate"))
for m in sim.get("Matches", []):
    name = m.get("match")
    print("Match in sim:", name, "In index.html?", name in html)
