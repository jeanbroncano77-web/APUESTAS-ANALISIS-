import re

html = open("index.html", encoding="utf-8").read()

print("--- 1. VERIFICACIÓN DE CARTELERA (MIÉRCOLES 14/10) ---")
cl_matches = [
    "Manchester City vs Paris Saint-Germain",
    "Roma vs Real Madrid",
    "LASK vs Liverpool",
    "Bodø/Glimt vs Borussia Dortmund",
    "Aston Villa vs Fenerbahçe",
    "Feyenoord vs Como"
]
for m in cl_matches:
    print(f"  Match {m}: {m in html or m.replace('ø', '&oslash;').replace('ç', '&ccedil;') in html}")

for h in ["Champions League", "Miércoles 14/10/2026", "MAÑANA"]:
    print(f"  Header text '{h}': {h in html}")

print("\n--- 2. VERIFICACIÓN DE AUDITORÍA (ÁREA 2) ---")
rows = re.findall(r'<tr class="audit-row[^"]*"', html)
print(f"  Total audit rows in HTML: {len(rows)}")

last_rows = re.findall(r'<td class="col-id">#(\d+)</td>', html)
if last_rows:
    print(f"  First ID: #{last_rows[0]}, Last ID: #{last_rows[-1]}")

for m in ["Galatasaray vs Barcelona", "Arsenal vs Lille", "Inter Milan vs Club Brugge", "Viking FK vs Bayern Munich"]:
    print(f"  Audited match in table: {m} -> {m in html}")

print("\n--- 3. VERIFICACIÓN DE KPIS ---")
for p in [r'\d+\.?\d*%\s*WIN', r'FIJAS:\s*\d+\.?\d*%', r'\d+\s*Aciertos', r'Racha activa de \d+']:
    print(f"  {p}: {re.findall(p, html)[:2]}")

print("\n--- 4. VERIFICACIÓN DE AUTOAPRENDIZAJE (ÁREA 3) ---")
for kw in ["Ciclo #81", "Champions League", "92.7%", "95.3%", "14"]:
    print(f"  Keyword '{kw}': {kw in html}")
