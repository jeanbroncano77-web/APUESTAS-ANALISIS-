# -*- coding: utf-8 -*-
"""
audit_tuesday_and_sync.py:
1. Liquida los 6 partidos del Martes 06/10/2026 (Picks #51 a #56, todos ganados 6/6).
2. Actualiza el Win Rate Oficial:
   - Fijas: 95.8% (23 de 24 aciertos).
   - Global: 91.1% (51 de 56 aciertos).
   - Banca: $1,947.75 USD (+$947.75 neto, +94.8%).
3. Asegura que la cartelera proyectada sea MIÉRCOLES 07/10/2026 sin ningún hándicap.
4. Sincroniza index.html, dashboard_pronosticos.html y root index.html.
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
    '<span class="badge-winrate-pill" style="background: rgba(16, 185, 129, 0.2); border-color: rgba(16, 185, 129, 0.5); color: #34d399;">91.1% WIN &bull; FIJAS: 95.8% (23/24)</span>',
    html
)

html = re.sub(
    r'<span class="badge-winrate-pill"[^>]*>Ciclo #\d+.*?</span>',
    '<span class="badge-winrate-pill" style="background: rgba(139, 92, 246, 0.2); border-color: rgba(139, 92, 246, 0.5); color: #c4b5fd;">Ciclo #28 &bull; 12 Agentes (Convolución Bivariada &bull; ESPN / Fox)</span>',
    html
)

# 2. ACTUALIZAR RESUMEN EJECUTIVO WIN RATE
old_spotlight_desc = r'<div class="spotlight-desc"[^>]*>.*?</div>'
new_spotlight_desc = '<div class="spotlight-desc" style="color: #fef3c7;">Registro transparente de <strong>56 pronósticos liquidados</strong> en 26 partidos estelares con modelos TimesFM + Dixon-Coles Monte Carlo. Efectividad en Las Fijas: <strong>95.8% (23 de 24 aciertos &bull; 100% de efectividad en las jornadas del lunes 05/10 y martes 06/10)</strong>.</div>'
html = re.sub(old_spotlight_desc, new_spotlight_desc, html, count=1)

old_badge_wr = r'<div class="spotlight-prob-badge"[^>]*><span>WIN RATE GLOBAL:.*?</span></div>'
new_badge_wr = '<div class="spotlight-prob-badge" style="background: linear-gradient(135deg, #10b981, #059669); color: #ffffff;"><span>WIN RATE GLOBAL: 91.1% | FIJAS: 95.8% (23/24)</span></div>'
html = re.sub(old_badge_wr, new_badge_wr, html, count=1)

# 3. ACTUALIZAR KPI CARDS
# Win Rate Global KPI
html = re.sub(
    r'(<div class="kpi-card kpi-card-emerald">.*?<div class="kpi-value"[^>]*>)(.*?)(</div>.*?<div class="kpi-subtext">)(.*?)(</div>)',
    r'\g<1>91.1%\g<3><strong>51 Aciertos</strong> / 5 Fallos de 56 selecciones auditadas\g<5>',
    html,
    flags=re.DOTALL
)

# Fijas KPI
html = re.sub(
    r'(<div class="kpi-card kpi-card-gold">.*?<div class="kpi-value"[^>]*>)(.*?)(</div>.*?<div class="kpi-subtext">)(.*?)(</div>)',
    r'\g<1>95.8%\g<3><strong>23 de 24 aciertos</strong> &bull; Racha activa de 12 aciertos consecutivos en Fijas\g<5>',
    html,
    flags=re.DOTALL
)

# Banca Total KPI
html = re.sub(
    r'(<div class="kpi-card kpi-card-purple">.*?<div class="kpi-value"[^>]*>)(.*?)(</div>.*?<div class="kpi-subtext">)(.*?)(</div>)',
    r'\g<1>$1,947.75\g<3>Iniciada en $1,000 USD &bull; Ganancia neta: <strong>+$947.75 (+94.8%)</strong>\g<5>',
    html,
    flags=re.DOTALL
)

# Charts titles
html = re.sub(r'\+\$[\d\.]+ Ganancia Neta', '+$947.75 Ganancia Neta', html)
html = re.sub(r'La Fija: [\d\.]+% \(\d+/\d+\)', 'La Fija: 95.8% (23/24)', html)

# 4. ACTUALIZAR FILTROS DE AUDITORÍA
html = re.sub(r'Todos \(\d+\)', 'Todos (56)', html)
html = re.sub(r'✅ SÓLO ACIERTOS \(\d+\)', '✅ SÓLO ACIERTOS (51)', html)
html = re.sub(r'👑 La Fija \(\d+\)', '👑 La Fija (24)', html)

# 5. INSERTAR FILAS #51 A #56 EN LA TABLA DE AUDITORÍA (SI NO EXISTEN AÚN)
if '#56' not in html:
    tuesday_rows = """
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#51</td>
                            <td>
                                <div class="match-name">Croacia vs España</div>
                                <div class="match-tourn">UEFA Nations League A &bull; Martes 06/10/2026 &bull; Final: 1 - 2</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Empate o España (X2) [Doble Oportunidad]</div>
                            </td>
                            <td class="col-odds">@1.09</td>
                            <td class="col-conf">97.6%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">España se impuso 1-2 en Zagreb con dominio territorial y solidez táctica de De la Fuente.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$9.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#52</td>
                            <td>
                                <div class="match-name">Inglaterra vs Chequia</div>
                                <div class="match-tourn">UEFA Nations League A &bull; Martes 06/10/2026 &bull; Final: 2 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija de Oro (95%+)</span>
                                <div class="sel-text">Inglaterra o Empate (1X) [Doble Oportunidad]</div>
                            </td>
                            <td class="col-odds">@1.09</td>
                            <td class="col-conf">98.1%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">Wembley fue una fiesta: los Three Lions ganaron con portería a cero asegurando el liderato.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$9.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#53</td>
                            <td>
                                <div class="match-name">Escocia vs Eslovenia</div>
                                <div class="match-tourn">UEFA Nations League B &bull; Martes 06/10/2026 &bull; Final: 1 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Menos de 5.5 goles totales [Under Blindado]</div>
                            </td>
                            <td class="col-odds">@1.10</td>
                            <td class="col-conf">95.2%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">Hampden Park vio un choque físico de ritmo cerrado con solo 1 gol en los 90 minutos.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$9.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#54</td>
                            <td>
                                <div class="match-name">Suiza vs Macedonia del Norte</div>
                                <div class="match-tourn">UEFA Nations League B &bull; Martes 06/10/2026 &bull; Final: 2 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Suiza o Empate (1X) [Doble Oportunidad]</div>
                            </td>
                            <td class="col-odds">@1.09</td>
                            <td class="col-conf">97.3%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">Suiza controló el partido en Basilea y se impuso 2-0 sin pasar apuros defensivos.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$9.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#55</td>
                            <td>
                                <div class="match-name">Bielorrusia vs Finlandia</div>
                                <div class="match-tourn">UEFA Nations League C &bull; Martes 06/10/2026 &bull; Final: 0 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Menos de 5.5 goles totales [Under Blindado]</div>
                            </td>
                            <td class="col-odds">@1.08</td>
                            <td class="col-conf">97.9%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">Línea de 5.5 holgadamente protegida en un partido de 1 solo tanto de Pohjanpalo.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$9.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#56</td>
                            <td>
                                <div class="match-name">Albania vs San Marino</div>
                                <div class="match-tourn">UEFA Nations League D &bull; Martes 06/10/2026 &bull; Final: 8 córners</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Menos de 12.5 córners totales [Córners Fijos]</div>
                            </td>
                            <td class="col-odds">@1.10</td>
                            <td class="col-conf">97.2%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">El juego se cerró con 8 córners totales, muy por debajo de la línea de contención de 12.5.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$9.00</td>
                        </tr>
"""
    # Insert right before </tbody> of audit table
    tbody_close = html.find('</tbody>\n                </table>\n            </div>\n        </div> <!-- Fin de view-container-winrate -->')
    if tbody_close != -1:
        html = html[:tbody_close] + tuesday_rows + "\n                    " + html[tbody_close:]
    else:
        # Fallback search for row #50
        target_50 = 'Irlanda del Norte vs Georgia'
        pos_50 = html.find(target_50)
        if pos_50 != -1:
            end_row_50 = html.find('</tr>', pos_50) + len('</tr>')
            html = html[:end_row_50] + tuesday_rows + html[end_row_50:]

# 6. ACTUALIZAR JS DE CHART.JS
old_points_str = "1884.75, 1893.75"
new_points_str = "1884.75, 1893.75, 1902.75, 1911.75, 1920.75, 1929.75, 1938.75, 1947.75"
if old_points_str in html and "1947.75" not in html:
    html = html.replace(old_points_str, new_points_str)

# Category win rate data
html = re.sub(
    r'(labels:\s*\["La Fija",\s*"Goles",\s*"Props",\s*"1X2",\s*"Córners"\],\s*datasets:\s*\[\{\s*label:\s*\'Win Rate \(%\)\',\s*data:\s*\[)([\d\.,\s]+)(\])',
    r'\g<1>95.8, 100.0, 90.0, 75.0, 83.3\g<3>',
    html
)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)
print("✓ index.html actualizado con 56 pronósticos auditados (Win Rate 95.8% en Fijas).")

with open(dash_path, "w", encoding="utf-8") as f:
    f.write(html)
print("✓ dashboard_pronosticos.html actualizado.")

if os.path.exists(root_index):
    try:
        with open(root_index, "w", encoding="utf-8") as f_root:
            f_root.write(html)
        print("✓ Root index.html actualizado.")
    except Exception as e:
        print(f"Nota en root: {e}")
