# -*- coding: utf-8 -*-
import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find KPI cards
matches = re.findall(r'<div class="kpi-card[^"]*">[\s\S]*?</div>\s*</div>', c)
print(f"Found {len(matches)} KPI cards:")
for idx, m in enumerate(matches):
    print(f"Card {idx+1}:\n{m}\n")

# Find Spotlight / header winrate
spotlight = re.findall(r'<div class="spotlight-[^"]*">[\s\S]*?</div>', c)
for s in spotlight[:5]:
    print("Spotlight:", s)

# Find pills
pills = re.findall(r'<span class="badge-winrate-pill"[^>]*>[\s\S]*?</span>', c)
print("Pills:", pills)
