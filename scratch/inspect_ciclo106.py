import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

ac_idx = text.find('id="view-container-autocorrect"')
end_idx = text.find('</div> <!-- Fin de view-container-autocorrect -->')
if end_idx == -1:
    end_idx = text.find('</div><!-- Fin de view-container-autocorrect -->')
if end_idx == -1:
    # search around
    pos = text.find('view-container-autocorrect')
    print("Length from ac_idx to end:", len(text) - pos)

# Let's find where Ciclo #106 is
c_idx = text.find('Ciclo #106')
print("Ciclo #106 position:", c_idx)
if c_idx != -1:
    print(text[c_idx-300:c_idx+1500])
