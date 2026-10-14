import re
import json

html = open("index.html", encoding="utf-8").read()

print("--- 1. VERIFICACIÓN DE CARTELERA (ÁREA 1) ---")
cl_matches = [
    "Galatasaray vs Barcelona",
    "Arsenal vs Lille",
    "Atlético de Madrid vs Manchester United",
    "Inter Milan vs Club Brugge",
    "Viking FK vs Bayern Munich",
    "Villarreal vs Napoli"
]
for m in cl_matches:
    found = m in html or m.replace("é", "&eacute;").replace("á", "&aacute;") in html
    print(f"  Match in HTML: {m} -> {found}")

# Check Competition Header
for h in ["Champions League", "Martes 13/10/2026", "MAÑANA"]:
    print(f"  Header string '{h}' in HTML: {h in html}")

print("\n--- 2. VERIFICACIÓN DE AUDITORÍA (ÁREA 2) ---")
# Check table rows count
rows = re.findall(r'<tr class="audit-row[^"]*"', html)
print(f"  Total audit rows in HTML table: {len(rows)}")

# Check last row
last_rows = re.findall(r'<td class="col-id">#(\d+)</td>', html)
if last_rows:
    print(f"  First row ID: #{last_rows[0]}, Last row ID: #{last_rows[-1]}")

# Check Monday matches in table
for m in ["Atalanta vs Venezia", "Coventry City vs Newcastle", "Levante vs Sevilla", "Torino vs Udinese", "Racing Club vs Belgrano", "Bahia vs Mirassol"]:
    print(f"  Audited match in table: {m} -> {m in html}")

# Check KPIs
print("  KPIs / Badges:")
for pattern in [r'\d+\.?\d*%\s*WIN', r'FIJAS:\s*\d+\.?\d*%', r'\d+\s*Aciertos', r'Racha activa de \d+']:
    matches = re.findall(pattern, html)
    print(f"    Match for {pattern}: {matches[:2]}")

print("\n--- 3. VERIFICACIÓN DE AUTOAPRENDIZAJE (ÁREA 3) ---")
for kw in ["Ciclo #70", "Champions League", "92.2%", "94.8%"]:
    print(f"  Keyword '{kw}' in Area 3: {kw in html}")

print("\n--- 4. VERIFICACIÓN DE TICKET CUANTITATIVO ---")
for t in ["ticket cuantitativo", "Añadir al Ticket", "slip-drawer"]:
    print(f"  Found '{t}' in HTML: {t.lower() in html.lower()}")
