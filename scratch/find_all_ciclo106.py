import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

pos = 0
while True:
    idx = text.find('Ciclo #106', pos)
    if idx == -1:
        break
    print(f"Found Ciclo #106 at pos {idx}:")
    print(text[max(0, idx-100):idx+400])
    print("-" * 50)
    pos = idx + len('Ciclo #106')
