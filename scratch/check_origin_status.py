# -*- coding: utf-8 -*-
import subprocess, json, re, sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

res = subprocess.run(['git', 'show', 'origin/main:sports_agents/simulations_tomorrow_results.json'], capture_output=True, text=True, encoding='utf-8')
data = json.loads(res.stdout)
print('TargetDay:', data.get('TargetDay'), data.get('TargetDate'), 'Label:', data.get('TemporalLabel'))
for m in data.get('Matches', []):
    print(' ', m.get('home_team'), 'vs', m.get('away_team'))

res_html = subprocess.run(['git', 'show', 'origin/main:index.html'], capture_output=True, text=True, encoding='utf-8')
c = res_html.stdout
teams = re.findall(r'<div class="switcher-teams">\s*<span>(.*?)</span>\s*<span class="vs-text">vs</span>\s*<span>(.*?)</span>', c)
print('SWITCHER TEAMS ON GITHUB PAGES:')
for idx, (h, a) in enumerate(teams):
    print(f'  {idx+1}: {h} vs {a}')

fija_oro = re.findall(r'class="badge-fija-oro">(.*?)</div>', c)
print('FIJA ORO ON GITHUB PAGES:', fija_oro)

kpis = re.findall(r'class="kpi-value[^"]*">\s*([^<]+)\s*</div>', c)
print('KPIS ON GITHUB PAGES:', kpis)

ids = re.findall(r'<td class="col-id">([^<]+)</td>', c)
print('AUDIT ROWS ON GITHUB PAGES (last 5):', ids[-5:] if ids else [])
