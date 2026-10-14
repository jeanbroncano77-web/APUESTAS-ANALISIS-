# -*- coding: utf-8 -*-
import os
import sys
import re
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

ids = re.findall(r'<td class="col-id">(#\d+)</td>', html)
print(f"Total Audit IDs found: {len(ids)}")
if ids:
    print(f"Range: {ids[0]} to {ids[-1]}")

wins = len(re.findall(r'badge-win', html))
losses = len(re.findall(r'badge-loss', html))
print(f"Badge wins: {wins}, Badge losses: {losses}")
