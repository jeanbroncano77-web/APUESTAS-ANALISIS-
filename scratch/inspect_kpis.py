import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's find "KPI Cards Grid"
idx = html.find('KPI Cards Grid')
if idx != -1:
    print("=== KPI CARDS GRID ===")
    print(html[idx:idx+2500])

# Let's find top nav / hero header
idx_hero = html.find('<header')
if idx_hero != -1:
    print("\n=== HEADER ===")
    print(html[idx_hero:idx_hero+1500])
else:
    # Look around first 2000 chars of body
    body_idx = html.find('<body')
    if body_idx != -1:
        print("\n=== BODY START ===")
        print(html[body_idx:body_idx+1500])
