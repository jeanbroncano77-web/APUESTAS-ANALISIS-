import re
import json

html = open("index.html", encoding="utf-8").read()
print("Length of index.html:", len(html))

# Search for Win Rate or stat values
for m in re.finditer(r'<div class="stat-[^"]*">([^<]+)</div>', html):
    print("Stat snippet:", m.group(1))

# Check table rows count
rows = re.findall(r'<tr[^>]*data-id="(\d+)"', html)
print(f"Audit rows with data-id: {len(rows)}")
if rows:
    print(f"First: {rows[0]}, Last: {rows[-1]}")

# Check any mention of win rate in script
js_vars = re.findall(r'(winRate[A-Za-z0-9_]*|auditStats[A-Za-z0-9_]*)\s*=\s*([^;]+);', html)
for k, v in js_vars:
    print(f"JS: {k} = {v[:60]}")

# Check matches in Area 1
matches_html = re.findall(r'<div class="match-card"[^>]*data-match="([^"]+)"', html)
print(f"Matches in Area 1: {matches_html}")
