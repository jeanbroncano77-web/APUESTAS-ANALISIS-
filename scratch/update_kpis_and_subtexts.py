# -*- coding: utf-8 -*-
"""
update_kpis_and_subtexts.py
Actualiza exactamente los KPIs, subtítulos y contadores en Area 2.
"""

import os

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
files = [
    os.path.join(base_dir, "index.html"),
    os.path.join(base_dir, "dashboard_pronosticos.html"),
    os.path.join(base_dir, "..", "index.html"),
    os.path.join(base_dir, "..", "dashboard_pronosticos.html")
]

old_kpi_block = '''            <div class="winrate-kpi-grid">
                <div class="kpi-card kpi-card-emerald">
                    <div class="kpi-title">
                        <span>Win Rate Global</span>
                        <span>🎯</span>
                    </div>
                    <div class="kpi-value" style="color: var(--emerald);">87.0%</div>
                    <div class="kpi-subtext"><strong>188 Aciertos</strong> / 28 Fallos de 216 selecciones auditadas</div>
                </div>

                <div class="kpi-card kpi-card-gold">
                    <div class="kpi-title">
                        <span>"La Fija" (95% - 98%)</span>
                        <span>👑</span>
                    </div>
                    <div class="kpi-value" style="color: var(--gold);">86.9%</div>
                    <div class="kpi-subtext"><strong>153 de 176 aciertos</strong> &bull; Racha activa: Melgar, PSG & Real Madrid</div>
                </div>

                <div class="kpi-card kpi-card-cyan">
                    <div class="kpi-title">
                        <span>Yield / ROI Financiero</span>
                        <span>📈</span>
                    </div>
                    <div class="kpi-value" style="color: var(--cyan);">+203.4%</div>
                    <div class="kpi-subtext"><strong>+$2,033.52 USD neto</strong> sobre banca inicial de $1,000 USD</div>
                </div>

                <div class="kpi-card kpi-card-purple">
                    <div class="kpi-title">
                        <span>Banca Total Liquidada</span>
                        <span>💰</span>
                    </div>
                    <div class="kpi-value" style="color: #c084fc;">$3,033.52</div>
                    <div class="kpi-subtext"><strong>+$2,033.52 USD neto</strong> (+203.4% ROI acumulado)</div>
                </div>
            </div>'''

new_kpi_block = '''            <div class="winrate-kpi-grid">
                <div class="kpi-card kpi-card-emerald">
                    <div class="kpi-title">
                        <span>Win Rate Global</span>
                        <span>🎯</span>
                    </div>
                    <div class="kpi-value" style="color: var(--emerald);">87.4%</div>
                    <div class="kpi-subtext"><strong>194 Aciertos</strong> / 28 Fallos de 222 selecciones auditadas</div>
                </div>

                <div class="kpi-card kpi-card-gold">
                    <div class="kpi-title">
                        <span>"La Fija" (95% - 98%)</span>
                        <span>👑</span>
                    </div>
                    <div class="kpi-value" style="color: var(--gold);">87.4%</div>
                    <div class="kpi-subtext"><strong>159 de 182 aciertos</strong> &bull; Racha activa: 9 Victorias Consecutivas (Pleno Dominical 6/6)</div>
                </div>

                <div class="kpi-card kpi-card-cyan">
                    <div class="kpi-title">
                        <span>Yield / ROI Financiero</span>
                        <span>📈</span>
                    </div>
                    <div class="kpi-value" style="color: var(--cyan);">+220.0%</div>
                    <div class="kpi-subtext"><strong>+$2,199.52 USD neto</strong> sobre banca inicial de $1,000 USD</div>
                </div>

                <div class="kpi-card kpi-card-purple">
                    <div class="kpi-title">
                        <span>Banca Total Liquidada</span>
                        <span>💰</span>
                    </div>
                    <div class="kpi-value" style="color: #c084fc;">$3,199.52</div>
                    <div class="kpi-subtext"><strong>+$2,199.52 USD neto</strong> (+220.0% ROI acumulado)</div>
                </div>
            </div>'''

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    if old_kpi_block in html:
        html = html.replace(old_kpi_block, new_kpi_block)
        print(f"[PASS] Replaced KPI block in {os.path.basename(fpath)}")
    else:
        print(f"[WARN] Old KPI block not found verbatim in {fpath}")

    # Subtítulos de gráficos
    html = html.replace("+$2,033.52 Ganancia Neta", "+$2,199.52 Ganancia Neta")
    html = html.replace("La Fija: 86.9% (153/176)", "La Fija: 87.4% (159/182)")
    html = html.replace("Mostrando 216 de 216 picks", "Mostrando 222 de 222 picks")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[PASS] Saved {fpath}")

print("KPI BLOCK UPDATED COMPLETELY!")

