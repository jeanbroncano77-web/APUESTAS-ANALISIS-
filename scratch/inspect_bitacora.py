import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

ac_idx = text.find('id="view-container-autocorrect"')
if ac_idx != -1:
    # look for bitacora or log-list
    b_idx = text.find('bitacora', ac_idx)
    if b_idx == -1:
        b_idx = text.find('ciclo', ac_idx)
    print("Found keyword at:", b_idx)
    if b_idx != -1:
        print(text[b_idx-200:b_idx+1200])
