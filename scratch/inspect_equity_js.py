import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

idx = text.find('chart-equity-curve')
while idx != -1:
    print(f"chart-equity-curve at {idx}:")
    print(text[idx-50:idx+350])
    print("-" * 50)
    idx = text.find('chart-equity-curve', idx + len('chart-equity-curve'))
