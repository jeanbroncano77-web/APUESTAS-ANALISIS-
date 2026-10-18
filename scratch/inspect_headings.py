import os
import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

ac_idx = text.find('id="view-container-autocorrect"')
if ac_idx != -1:
    ac_content = text[ac_idx:ac_idx+20000]
    # find all headings or titles
    headings = re.findall(r'<div class="[^"]*title[^"]*">([^<]+)</div>', ac_content)
    print("Headings in autocorrect:", headings)
    # also search for Ciclo #
    ciclos = re.findall(r'Ciclo\s*#\d+', text[ac_idx:], re.IGNORECASE)
    print("Found Ciclos:", set(ciclos[:10]))
