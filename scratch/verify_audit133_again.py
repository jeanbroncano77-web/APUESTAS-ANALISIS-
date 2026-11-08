import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    ("Ciclo #133 present", "Ciclo #133" in html),
    ("Row #212 (Valencia vs Real Madrid) present", ">#212</td>" in html and "Valencia vs Real Madrid" in html),
    ("Row #213 (PSG vs Troyes) present", ">#213</td>" in html and "Paris Saint-Germain vs Troyes" in html),
    ("Row #214 (Libertad vs Emelec) present", ">#214</td>" in html and "Libertad FC vs Emelec" in html),
    ("Row #215 (Melgar vs Juan Pablo II) present", ">#215</td>" in html and "FBC Melgar vs Juan Pablo II" in html),
    ("Row #216 (Man City vs Forest) present", ">#216</td>" in html and "Nottingham Forest vs Manchester City" in html),
    ("Row #217 (Cienciano vs Huancayo) present", ">#217</td>" in html and "Cienciano vs Sport Huancayo" in html),
    ("Win Rate Global 87.5%", "87.5%" in html and "189 Aciertos" in html and "216 selecciones" in html),
    ("La Fija 87.5%", "154 de 176 aciertos" in html and "Racha activa: 3 victorias" in html),
    ("Banca Total $3,174.52", "$3,174.52" in html and "+$2,174.52 USD neto" in html),
    ("rawPoints ends at 3174.52", "3174.52]" in html),
    ("Total col-id count", len(re.findall(r'<td class="col-id">#\d+</td>', html)) == 216)
]

for name, res in checks:
    print(f"[{'PASS' if res else 'FAIL'}] {name}")
