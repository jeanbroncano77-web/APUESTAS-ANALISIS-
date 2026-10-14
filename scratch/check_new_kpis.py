import re
import sys
sys.stdout.reconfigure(encoding="utf-8")

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

print("90.6% count:", text.count("90.6%"))
print("92.2% count:", text.count("92.2%"))
print("87 Aciertos count:", text.count("87 Aciertos"))
print("9 Fallos count:", text.count("9 Fallos"))
print("$2,075.75 count:", text.count("$2,075.75"))
print("+107.6% count:", text.count("+107.6%"))

rows = re.findall(r'<tr class="audit-row[^"]*"[^>]*>.*?</tr>', text, re.DOTALL)
print(f"Total audit rows: {len(rows)}")
for idx in [90, 91, 92, 93, 94, 95]:
    r = rows[idx]
    id_m = re.search(r'#(\d+)', r).group(1)
    name_m = re.search(r'<div class="match-name">(.*?)</div>', r).group(1)
    status_m = "WIN" if "badge-win" in r else "LOSS"
    pnl_m = re.search(r'col-pnl[^"]*">(.*?)</td>', r).group(1)
    print(f"Row {id_m}: {name_m} -> {status_m} | {pnl_m}")
