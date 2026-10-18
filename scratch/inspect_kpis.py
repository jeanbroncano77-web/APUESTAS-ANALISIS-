import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

wr_start = text.find('id="view-container-winrate"')
kpi_start = text.find('class="kpi-grid"', wr_start)
if kpi_start == -1:
    kpi_start = text.find('KPI Cards Grid', wr_start)

if kpi_start != -1:
    print(text[kpi_start:kpi_start+2000])
