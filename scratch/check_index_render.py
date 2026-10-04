import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

picks = re.findall(r'<div class="fija-selection-badge">(.*?)</div>', html, re.DOTALL)
print(f"PICKS PRINCIPALES ENCONTRADOS: {len(picks)}")
for idx, p in enumerate(picks[:6]):
    clean = re.sub(r"<[^>]+>", " ", p)
    clean = re.sub(r"\s+", " ", clean).strip()
    print(f" Match {idx+1}: {clean}")

probs = re.findall(r'<div class="fija-stat-val">(.*?)</div>', html, re.DOTALL)
print("\nVALORES DE FIJA (Cuota, Probabilidad, Seguridad):")
for idx in range(0, min(len(probs), 18), 3):
    match_num = (idx // 3) + 1
    trio = [p.strip() for p in probs[idx:idx+3]]
    print(f" Match {match_num}: Cuota={trio[0]} | Probabilidad={trio[1]} | Nivel={trio[2]}")
