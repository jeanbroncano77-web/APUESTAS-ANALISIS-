# -*- coding: utf-8 -*-
import subprocess
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

res = subprocess.run(['git', 'show', 'origin/main:index.html'], capture_output=True, text=True, encoding='utf-8')
c = res.stdout
teams = re.findall(r'<div class="switcher-teams">\s*<span>(.*?)</span>\s*<span class="vs-text">vs</span>\s*<span>(.*?)</span>', c)
print('MATCHES IN ORIGIN/MAIN:')
for idx, (h, a) in enumerate(teams):
    print(f'  {idx+1}: {h} vs {a}')

fija_oro = re.findall(r'class="badge-fija-oro">(.*?)</div>', c)
print('FIJA ORO IN ORIGIN/MAIN:', fija_oro)
