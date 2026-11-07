import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    ("11 Partidos Estelares", "11 Partidos Estelares" in html),
    ("Partidos & Pronósticos (11)", "Partidos & Pronósticos (11)" in html),
    ("88.1% Win Rate Global", "88.1%" in html and "185 Aciertos" in html and "210 selecciones" in html),
    ("88.2% La Fija", "88.2%" in html and "150 de 170 aciertos" in html),
    ("+226.8% ROI", "+226.8%" in html and "+$2,267.52 USD neto" in html),
    ("$3,267.52 Banca Total", "$3,267.52" in html),
    ("Chart subtitle +$2,267.52", "+$2,267.52 Ganancia Neta" in html),
    ("Chart rawPoints ends with 3267.52", "3267.52]" in html),
    ("Ciclo #132 Present", "Ciclo #132" in html),
    ("Ciclo #131 Present", "Ciclo #131" in html),
    ("11 Pending Matches in Area 1", "Libertad FC vs. Emelec" in html and "Valencia vs. Real Madrid" in html and "PSG vs. Troyes" in html and "FBC Melgar vs. Juan Pablo II" in html)
]

for label, passed in checks:
    print(f"[{'PASS' if passed else 'FAIL'}] {label}")
