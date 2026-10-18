import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

ac_start = text.find('id="view-container-autocorrect"')
table_pos = text.find('<table', ac_start)

# print from showcase-card end to table
sc_end = text.find('</div>\n            </div>', ac_start + 1000)
print("Content between agent showcase and table:")
print(text[sc_end:sc_end+3000])
