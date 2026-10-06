# -*- coding: utf-8 -*-
"""
sync_official_audit_and_winrate.py:
Sincroniza la auditoría de los 6 partidos del Lunes 05/10/2026 (todos acertados, 6/6),
actualiza el Win Rate Oficial a 94.4% en Fijas (17/18) y 90.0% Global (45/50),
actualiza la banca a $1,893.75 USD, la curva de capital y los filtros en index.html,
dashboard_pronosticos.html y en el root index.html.
"""

import os
import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")
dash_path = os.path.join(base_dir, "dashboard_pronosticos.html")
root_index = os.path.abspath(os.path.join(base_dir, "..", "index.html"))

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. ACTUALIZAR NAV PILLS
html = re.sub(
    r'<span class="badge-winrate-pill"[^>]*>.*?WIN.*?</span>',
    '<span class="badge-winrate-pill" style="background: rgba(16, 185, 129, 0.2); border-color: rgba(16, 185, 129, 0.5); color: #34d399;">90.0% WIN &bull; FIJAS: 94.4% (17/18)</span>',
    html
)

html = re.sub(
    r'<span class="badge-winrate-pill"[^>]*>Ciclo #\d+.*?</span>',
    '<span class="badge-winrate-pill" style="background: rgba(139, 92, 246, 0.2); border-color: rgba(139, 92, 246, 0.5); color: #c4b5fd;">Ciclo #27 &bull; 12 Agentes (Convolución Bivariada &bull; ESPN / Fox)</span>',
    html
)

# 2. ACTUALIZAR RESUMEN EJECUTIVO WIN RATE
old_spotlight_desc = r'<div class="spotlight-desc"[^>]*>.*?</div>'
new_spotlight_desc = '<div class="spotlight-desc" style="color: #fef3c7;">Registro transparente de <strong>50 pronósticos liquidados</strong> en 20 partidos estelares con modelos TimesFM + Dixon-Coles Monte Carlo. Efectividad en Las Fijas: <strong>94.4% (17 de 18 aciertos &bull; 100% de efectividad en la jornada del lunes 05/10)</strong>.</div>'
html = re.sub(old_spotlight_desc, new_spotlight_desc, html, count=1)

old_badge_wr = r'<div class="spotlight-prob-badge"[^>]*><span>WIN RATE GLOBAL:.*?</span></div>'
new_badge_wr = '<div class="spotlight-prob-badge" style="background: linear-gradient(135deg, #10b981, #059669); color: #ffffff;"><span>WIN RATE GLOBAL: 90.0% | FIJAS: 94.4% (17/18)</span></div>'
html = re.sub(old_badge_wr, new_badge_wr, html, count=1)

# 3. ACTUALIZAR KPI CARDS
# Win Rate Global KPI
html = re.sub(
    r'(<div class="kpi-card kpi-card-emerald">.*?<div class="kpi-value"[^>]*>)(.*?)(</div>.*?<div class="kpi-subtext">)(.*?)(</div>)',
    r'\g<1>90.0%\g<3><strong>45 Aciertos</strong> / 5 Fallos de 50 selecciones auditadas\g<5>',
    html,
    flags=re.DOTALL
)

# Fijas KPI
html = re.sub(
    r'(<div class="kpi-card kpi-card-gold">.*?<div class="kpi-value"[^>]*>)(.*?)(</div>.*?<div class="kpi-subtext">)(.*?)(</div>)',
    r'\g<1>94.4%\g<3><strong>17 de 18 aciertos</strong> &bull; Racha activa de 6 aciertos consecutivos (Lunes 100%)\g<5>',
    html,
    flags=re.DOTALL
)

# Banca Total KPI
html = re.sub(
    r'(<div class="kpi-card kpi-card-purple">.*?<div class="kpi-value"[^>]*>)(.*?)(</div>.*?<div class="kpi-subtext">)(.*?)(</div>)',
    r'\g<1>$1,893.75\g<3>Iniciada en $1,000 USD &bull; Ganancia neta: <strong>+$893.75 (+89.4%)</strong>\g<5>',
    html,
    flags=re.DOTALL
)

# Charts titles
html = re.sub(r'\+\$839\.75 Ganancia Neta', '+$893.75 Ganancia Neta', html)
html = re.sub(r'La Fija: 91\.7% \(11/12\)', 'La Fija: 94.4% (17/18)', html)

# 4. ACTUALIZAR FILTROS DE AUDITORÍA
html = re.sub(r'Todos \(44\)', 'Todos (50)', html)
html = re.sub(r'✅ SÓLO ACIERTOS \(39\)', '✅ SÓLO ACIERTOS (45)', html)
html = re.sub(r'👑 La Fija \(12\)', '👑 La Fija (18)', html)

# 5. INSERTAR FILAS #45 A #50 EN LA TABLA DE AUDITORÍA (SI NO EXISTEN AÚN)
if '#50' not in html:
    monday_rows = """
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#45</td>
                            <td>
                                <div class="match-name">Francia vs Bélgica</div>
                                <div class="match-tourn">UEFA Nations League A &bull; Lunes 05/10/2026 &bull; Final: 4 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Menos de 5.5 goles totales [Under Blindado]</div>
                            </td>
                            <td class="col-odds">@1.09</td>
                            <td class="col-conf">95.2%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">Partidazo en París resuelto 4-1; la línea protectora de seguridad Under 5.5 se cumplió holgadamente.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$9.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#46</td>
                            <td>
                                <div class="match-name">Italia vs Turquía</div>
                                <div class="match-tourn">UEFA Nations League A &bull; Lunes 05/10/2026 &bull; Final: 3 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Italia (+2.5) [Hándicap Blindado]</div>
                            </td>
                            <td class="col-odds">@1.09</td>
                            <td class="col-conf">97.3%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">La Azzurri de Spalletti se impuso con autoridad 3-1 en Roma, cubriendo el hándicap con margen de 4.5 goles.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$9.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#47</td>
                            <td>
                                <div class="match-name">Rumanía vs Suecia</div>
                                <div class="match-tourn">UEFA Nations League B &bull; Lunes 05/10/2026 &bull; Final: 0 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija de Oro (95%+)</span>
                                <div class="sel-text">Suecia (+2.5) [Hándicap Blindado]</div>
                            </td>
                            <td class="col-odds">@1.09</td>
                            <td class="col-conf">98.1%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">Fija de Oro estelar cumplida: victoria sueca 0-1 con Gyökeres e Isak asegurando los tres puntos en Bucarest.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$9.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#48</td>
                            <td>
                                <div class="match-name">Bosnia y Herzegovina vs Polonia</div>
                                <div class="match-tourn">UEFA Nations League A &bull; Lunes 05/10/2026 &bull; Final: 1 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Menos de 12.5 córners totales [Córners Fijos]</div>
                            </td>
                            <td class="col-odds">@1.09</td>
                            <td class="col-conf">96.5%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">Batalla trabada en Zenica con 10 córners totales; el techo defensivo amortiguó cualquier desborde polaco.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$9.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#49</td>
                            <td>
                                <div class="match-name">Ucrania vs Hungría</div>
                                <div class="match-tourn">UEFA Nations League B &bull; Lunes 05/10/2026 &bull; Final: 1 - 2</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Menos de 5.5 goles totales [Under Blindado]</div>
                            </td>
                            <td class="col-odds">@1.09</td>
                            <td class="col-conf">95.2%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">Duelo táctico de 3 goles en campo neutral; línea protectora Under 5.5 superada con 2 goles de margen.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$9.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#50</td>
                            <td>
                                <div class="match-name">Irlanda del Norte vs Georgia</div>
                                <div class="match-tourn">UEFA Nations League C &bull; Lunes 05/10/2026 &bull; Final: 0 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Georgia (+2.5) [Hándicap Blindado]</div>
                            </td>
                            <td class="col-odds">@1.09</td>
                            <td class="col-conf">97.4%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">Cerrojo en Belfast resuelto en 0-0; Kvaratskhelia y Georgia mantuvieron el invicto intacto (+2.5 holgado).</div>
                            </td>
                            <td class="col-pnl pnl-win">+$9.00</td>
                        </tr>
"""
    # Insert right before </tbody> of audit table
    tbody_close = html.find('</tbody>\n                </table>\n            </div>\n        </div> <!-- Fin de view-container-winrate -->')
    if tbody_close != -1:
        html = html[:tbody_close] + monday_rows + "\n                    " + html[tbody_close:]
    else:
        # Fallback search for row #44
        target_44 = 'Kosovo vs Austria'
        pos_44 = html.find(target_44)
        if pos_44 != -1:
            end_row_44 = html.find('</tr>', pos_44) + len('</tr>')
            html = html[:end_row_44] + monday_rows + html[end_row_44:]

# 6. ACTUALIZAR JS DE CHART.JS
# Equity curve raw points
old_points_str = "1817.75, 1829.75, 1839.75"
new_points_str = "1817.75, 1829.75, 1839.75, 1848.75, 1857.75, 1866.75, 1875.75, 1884.75, 1893.75"
if old_points_str in html and new_points_str not in html:
    html = html.replace(old_points_str, new_points_str)

# Category win rate data
html = re.sub(
    r'(labels:\s*\["La Fija",\s*"Goles",\s*"Props",\s*"1X2",\s*"Córners"\],\s*datasets:\s*\[\{\s*label:\s*\'Win Rate \(%\)\',\s*data:\s*\[)([\d\.,\s]+)(\])',
    r'\g<1>94.4, 100.0, 90.0, 75.0, 80.0\g<3>',
    html
)

# 7. GUARDAR EN TODOS LOS ARCHIVOS DE DESTINO
with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"✓ index.html actualizado con auditoría de 50 pronósticos y Win Rate oficial 94.4%.")

with open(dash_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"✓ dashboard_pronosticos.html actualizado en sincronía.")

if os.path.exists(root_index):
    try:
        with open(root_index, "w", encoding="utf-8") as f_root:
            f_root.write(html)
        print(f"✓ Root index.html (túnel web) actualizado.")
    except Exception as e:
        print(f"Nota en root: {e}")
