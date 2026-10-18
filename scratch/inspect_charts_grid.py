import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

wr_start = text.find('id="view-container-winrate"')
cg_start = text.find('class="winrate-charts-grid"', wr_start)
tb_start = text.find('<table', wr_start)

if cg_start != -1 and tb_start != -1:
    print(text[cg_start:tb_start])
