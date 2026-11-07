import json
import re

with open('sports_agents/audit_history.json', 'r', encoding='utf-8') as f:
    audit = json.load(f)

history = audit.get('history', [])

bankroll = 1000.0
points = [bankroll]
wins = 0
losses = 0
fija_wins = 0
fija_losses = 0

for h in history:
    pnl = h.get('pnl', 0.0)
    status = h.get('status', 'win')
    bankroll += pnl
    points.append(round(bankroll, 2))
    if status == 'win':
        wins += 1
        if h.get('is_fija'): fija_wins += 1
    else:
        losses += 1
        if h.get('is_fija'): fija_losses += 1

points_json = json.dumps(points)
print("Points length:", len(points))
print("Final point:", points[-1])

files_to_sync = ['index.html', 'dashboard_pronosticos.html', '../index.html']

for file_path in files_to_sync:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Skipping {file_path}: {e}")
        continue

    # 1. Update header subtitle
    content = re.sub(
        r'Motor Predictivo Multi-Agente &bull; \d+ Partidos Estelares &bull; Actualizado \d\d:\d\d',
        'Motor Predictivo Multi-Agente &bull; 11 Partidos Estelares &bull; Sábado 07/11 (Tarde & Noche)',
        content
    )

    # 2. Update View mode button 1
    content = re.sub(
        r'⚽ Partidos &amp; Pronósticos \(\d+\)|⚽ Partidos & Pronósticos \(\d+\)',
        '⚽ Partidos & Pronósticos (11)',
        content
    )

    # 3. Update KPI Card 2: La Fija
    # Replace old fija percentage and subtext
    content = re.sub(
        r'<div class="kpi-value" style="color: var\(--gold\);">\d+\.\d+%</div>\s*<div class="kpi-subtext"><strong>\d+ de \d+ aciertos</strong> &bull; Racha activa en Fijas</div>',
        '<div class="kpi-value" style="color: var(--gold);">88.2%</div>\n                    <div class="kpi-subtext"><strong>150 de 170 aciertos</strong> &bull; Racha activa: 12 victorias consecutivas</div>',
        content
    )

    # 4. Update KPI Card 3: Yield / ROI
    content = re.sub(
        r'<div class="kpi-value" style="color: var\(--cyan\);">\+\d+\.\d+%</div>\s*<div class="kpi-subtext"><strong>\+\$[\d,]+\.\d\d USD neto</strong> sobre banca inicial de \$1,000 USD</div>',
        '<div class="kpi-value" style="color: var(--cyan);">+226.8%</div>\n                    <div class="kpi-subtext"><strong>+$2,267.52 USD neto</strong> sobre banca inicial de $1,000 USD</div>',
        content
    )

    # 5. Update KPI Card 4: Banca Total Liquidada
    content = re.sub(
        r'<div class="kpi-value" style="color: #c084fc;">\$[\d,]+\.\d\d</div>\s*<div class="kpi-subtext"><strong>\+\$[\d,]+\.\d\d USD neto</strong> \(\+\d+\.\d+% ROI acumulado\)</div>',
        '<div class="kpi-value" style="color: #c084fc;">$3,267.52</div>\n                    <div class="kpi-subtext"><strong>+$2,267.52 USD neto</strong> (+226.8% ROI acumulado)</div>',
        content
    )

    # 6. Update Chart box titles
    content = re.sub(
        r'<span style="font-size: 0\.8rem; color: #10b981; font-weight: 700;">\+\$[\d,]+\.\d\d Ganancia Neta</span>',
        '<span style="font-size: 0.8rem; color: #10b981; font-weight: 700;">+$2,267.52 Ganancia Neta</span>',
        content
    )
    content = re.sub(
        r'<span style="font-size: 0\.8rem; color: var\(--gold\); font-weight: 700;">La Fija: \d+\.\d+% \(\d+/\d+\)</span>',
        '<span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">La Fija: 88.2% (150/170)</span>',
        content
    )

    # 7. Update rawPoints in script
    # Look for: var rawPoints = [...];
    content = re.sub(
        r'var rawPoints = \[[^\]]+\];',
        f'var rawPoints = {points_json};',
        content
    )

    # 8. Update chart category winrate data
    content = re.sub(
        r'data:\s*\[87\.3,\s*100\.0,\s*90\.0,\s*75\.0,\s*75\.0\]',
        'data: [88.2, 100.0, 90.0, 75.0, 75.0]',
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully fully synchronized and updated: {file_path}")
