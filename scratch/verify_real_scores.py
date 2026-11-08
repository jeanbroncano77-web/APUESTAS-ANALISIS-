import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    ("Ciclo #133 with Madrid 0-3", "Madrid 0-3" in html and "Ciclo #133" in html),
    ("Row #212 Madrid WIN (0 - 3)", ">#212</td>" in html and "Final: 0 - 3" in html and "badge-win" in html[html.find('>#212</td>'):html.find('>#213</td>')]),
    ("Row #213 PSG WIN (1 - 0)", ">#213</td>" in html and "Final: 1 - 0" in html and "badge-win" in html[html.find('>#213</td>'):html.find('>#214</td>')]),
    ("Row #214 Libertad LOSS (0 - 1)", ">#214</td>" in html and "Final: 0 - 1" in html and "badge-loss" in html[html.find('>#214</td>'):html.find('>#215</td>')]),
    ("Row #215 Melgar WIN (2 - 1)", ">#215</td>" in html and "Final: 2 - 1" in html and "badge-win" in html[html.find('>#215</td>'):html.find('>#216</td>')]),
    ("Row #216 City LOSS (3 - 1)", ">#216</td>" in html and "Final: 3 - 1" in html and "badge-loss" in html[html.find('>#216</td>'):html.find('>#217</td>')]),
    ("Row #217 Cienciano LOSS (1 - 2)", ">#217</td>" in html and "Final: 1 - 2" in html and "badge-loss" in html[html.find('>#217</td>'):html.find('</tr>', html.find('>#217</td>'))]),
    ("KPI Global Win Rate 87.0%", "87.0%" in html and "188 Aciertos" in html and "216 selecciones" in html),
    ("KPI Fijas 86.9%", "86.9%" in html and "153 de 176 aciertos" in html),
    ("Banca Total $3,033.52", "$3,033.52" in html and "+$2,033.52 USD neto" in html),
    ("rawPoints ends at 3033.52", "3033.52]" in html),
    ("Total picks in table", len(re.findall(r'<td class="col-id">#\d+</td>', html)) == 216)
]

for name, res in checks:
    print(f"[{'PASS' if res else 'FAIL'}] {name}")

