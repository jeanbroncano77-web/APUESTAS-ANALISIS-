import os
import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

wr_idx = text.find('id="view-container-winrate"')
ac_idx = text.find('id="view-container-autocorrect"')

print(f"view-container-winrate index: {wr_idx}")
if wr_idx != -1:
    print(text[wr_idx:wr_idx+1200])

print(f"\nview-container-autocorrect index: {ac_idx}")
if ac_idx != -1:
    print(text[ac_idx:ac_idx+1200])
