import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

wr_start = text.find('id="view-container-winrate"')
wr_end = text.find('<!-- Fin de view-container-winrate -->')
if wr_end == -1:
    wr_end = text.find('<!-- Fin selector')
print(f"view-container-winrate start: {wr_start}, end: {wr_end}")

ac_start = text.find('id="view-container-autocorrect"')
ac_end = text.find('<!-- Fin de view-container-autocorrect -->')
print(f"view-container-autocorrect start: {ac_start}, end: {ac_end}")

# Check what comes after ac_start
if ac_start != -1:
    # find closing tag of view-container-autocorrect
    print("Next 500 chars after ac_start:")
    print(text[ac_start:ac_start+500])
    
    # search where footer or end of container is
    foot_idx = text.find('<footer', ac_start)
    print(f"Footer pos after ac_start: {foot_idx}")
