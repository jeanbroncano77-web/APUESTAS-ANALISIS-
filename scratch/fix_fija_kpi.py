import re

files = ['index.html', 'dashboard_pronosticos.html', '../index.html']

pattern = r'<div class="kpi-value" style="color: var\(--gold\);">\d+\.\d+%</div>\s*<div class="kpi-subtext"><strong>\d+ de \d+ aciertos</strong> &bull; [^<]+</div>'
replacement = '<div class="kpi-value" style="color: var(--gold);">87.5%</div>\n                    <div class="kpi-subtext"><strong>154 de 176 aciertos</strong> &bull; Racha activa: 3 victorias consecutivas</div>'

for fpath in files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        c = re.sub(pattern, replacement, c)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Fixed fija KPI in {fpath}")
    except Exception as e:
        print(f"Error {fpath}: {e}")
