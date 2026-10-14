# -*- coding: utf-8 -*-
import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

teams = re.findall(r'<div class="switcher-teams">\s*<span>(.*?)</span>\s*<span class="vs-text">vs</span>\s*<span>(.*?)</span>', c)
print('SWITCHER TEAMS:')
for idx, (h, a) in enumerate(teams):
    print(f'  {idx+1}: {h} vs {a}')

fija_oro = re.findall(r'class="badge-fija-oro">(.*?)</div>', c)
print('FIJA ORO:', fija_oro)

kpis = re.findall(r'class="kpi-value[^"]*">\s*([^<]+)\s*</div>', c)
print('KPIS:', kpis)

ids = re.findall(r'<td class="col-id">([^<]+)</td>', c)
print('AUDIT IDS (last 10):', ids[-10:] if ids else [])

cycles = re.findall(r'Ciclo #\d+', c)
print('CYCLES IN HTML:', list(dict.fromkeys(cycles))[-8:])
