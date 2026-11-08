import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    ("Title is Domingo 08/11", "Domingo 08/11" in re.search(r'<title>.*?</title>', html).group(0)),
    ("6 Switcher Tabs", len(re.findall(r'id="tab-\d+"', html)) == 6),
    ("6 Match Views", len(re.findall(r'id="match-\d+"', html)) == 6),
    ("Barcelona vs LDU present", "Barcelona SC vs. Liga de Quito" in html),
    ("Aucas vs IDV present", "Aucas vs. Independiente del Valle" in html),
    ("Atleti vs Barça present", "Atlético de Madrid vs. FC Barcelona" in html),
    ("Inter vs Como present", "Inter de Milán vs. Como 1907" in html),
    ("Napoli vs Lazio present", "Napoli vs. Lazio" in html),
    ("Lens vs Marsella present", "RC Lens vs. Olympique de Marsella" in html),
    ("Area 2 Table has 216 picks", len(re.findall(r'<td class="col-id">#\d+</td>', html)) == 216),
    ("Area 3 has Ciclo #133", "Ciclo #133" in html),
    ("KPI Win Rate 87.0%", "87.0%" in html),
    ("Banca Total $3,033.52", "$3,033.52" in html)
]

for name, res in checks:
    print(f"[{'PASS' if res else 'FAIL'}] {name}")
