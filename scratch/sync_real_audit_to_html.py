import re
import os
import sys

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"

for filename in ["index.html", "dashboard_pronosticos.html"]:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. ACTUALIZAR KPIS GLOBALES Y FIJAS
    html = html.replace('92.7% WIN &bull; FIJAS: 95.3% (61/64)', '90.6% WIN &bull; FIJAS: 92.2% (59/64)')
    html = html.replace('WIN RATE GLOBAL: 92.7% | FIJAS: 95.3% (61/64)', 'WIN RATE GLOBAL: 90.6% | FIJAS: 92.2% (59/64)')
    html = html.replace('Win Rate Global: 92.7% (89/96)', 'Win Rate Global: 90.6% (87/96)')
    html = html.replace('La Fija: 95.3% (61/64)', 'La Fija: 92.2% (59/64)')
    html = html.replace('95.3% (61 de 64 aciertos &bull; 14 aciertos consecutivos)', '92.2% (59 de 64 aciertos &bull; 2 fallos en Champions)')
    
    # KPI 1
    html = re.sub(
        r'<div class="kpi-value" style="color: var\(--emerald\);">92\.7%</div>\s*<div class="kpi-subtext"><strong>89 Aciertos</strong> / 7 Fallos de 96 selecciones auditadas</div>',
        r'<div class="kpi-value" style="color: var(--emerald);">90.6%</div>\n                    <div class="kpi-subtext"><strong>87 Aciertos</strong> / 9 Fallos de 96 selecciones auditadas</div>',
        html
    )

    # KPI 2
    html = re.sub(
        r'<div class="kpi-value" style="color: var\(--gold\);">95\.3%</div>\s*<div class="kpi-subtext"><strong>61 de 64 aciertos</strong> &bull; Racha activa de 14 aciertos consecutivos en Fijas</div>',
        r'<div class="kpi-value" style="color: var(--gold);">92.2%</div>\n                    <div class="kpi-subtext"><strong>59 de 64 aciertos</strong> &bull; Racha cortada (Inter 3-4 Brugge) &bull; 5 fallos históricos</div>',
        html
    )

    # KPI 3
    html = html.replace('$2,303.75', '$2,075.75')
    html = html.replace('+$1,303.75 USD neto</strong> sobre banca inicial de $1,000 (+130.4% ROI)', '+$1,075.75 USD neto</strong> sobre banca inicial de $1,000 (+107.6% ROI)')
    html = html.replace('+$1,303.75 USD neto</strong> (+130.4% ROI acumulado)', '+$1,075.75 USD neto</strong> (+107.6% ROI acumulado)')

    # 2. REEMPLAZAR FILAS 91 A 96 EN LA TABLA DE AUDITORÍA
    rows_real_html = """                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#91</td>
                            <td>
                                <div class="match-name">Arsenal vs Lille</div>
                                <div class="match-tourn">UEFA Champions League &bull; Martes 13/10/2026 &bull; Final: 3 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Arsenal o Empate (1X) [Doble Oportunidad]</div>
                            </td>
                            <td class="col-odds">@1.14</td>
                            <td class="col-conf">96.8%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">Arsenal impuso su solidez en el Emirates Stadium (3-0) con autoridad absoluta; la Doble Oportunidad 1X cumplió con solvencia europea.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$14.00</td>
                        </tr>

                        <tr class="audit-row row-loss" data-category="fija" data-status="loss">
                            <td class="col-id">#92</td>
                            <td>
                                <div class="match-name">Inter Milan vs Club Brugge</div>
                                <div class="match-tourn">UEFA Champions League &bull; Martes 13/10/2026 &bull; Final: 3 - 4</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Inter Milan o Empate (1X) [Doble Oportunidad]</div>
                            </td>
                            <td class="col-odds">@1.14</td>
                            <td class="col-conf">96.8%</td>
                            <td>
                                <span class="badge-status badge-loss">❌ FALLADO</span>
                                <div class="diag-text">FALLO CATASTRÓFICO: Inter Milan cayó 3-4 en San Siro ante Club Brugge (hat-trick de Nicolò Tresoldi). El modelo subestimó la sobrecarga muscular de Serie A y la letalidad belga al contraataque.</div>
                            </td>
                            <td class="col-pnl pnl-loss">-$100.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#93</td>
                            <td>
                                <div class="match-name">Galatasaray vs Barcelona</div>
                                <div class="match-tourn">UEFA Champions League &bull; Martes 13/10/2026 &bull; Final: 1 - 4</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Empate o Barcelona (X2) [Doble Oportunidad]</div>
                            </td>
                            <td class="col-odds">@1.14</td>
                            <td class="col-conf">96.8%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">ACIERTO X2 (Victoria 1-4 del Barça): El modelo sobreestimó la hostilidad de Estambul. El Barcelona de Flick aplastó 1-4 demostrando que la jerarquía y el pressing superaban con creces el factor cancha.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$14.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#94</td>
                            <td>
                                <div class="match-name">Viking FK vs Bayern Munich</div>
                                <div class="match-tourn">UEFA Champions League &bull; Martes 13/10/2026 &bull; Final: 0 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Empate o Bayern Munich (X2) [Doble Oportunidad]</div>
                            </td>
                            <td class="col-odds">@1.14</td>
                            <td class="col-conf">95.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">ACIERTO TÉCNICO X2 (Empate 0-0): El frío y el césped noruego frenaron la ofensiva bávara; el X2 salvó el pick pero confirmó que el clima y el viaje nórdico sí merman el volumen goleador.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$14.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#95</td>
                            <td>
                                <div class="match-name">Atlético de Madrid vs Manchester United</div>
                                <div class="match-tourn">UEFA Champions League &bull; Martes 13/10/2026 &bull; Final: 2 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Atlético de Madrid o Empate (1X) [Doble Oportunidad]</div>
                            </td>
                            <td class="col-odds">@1.14</td>
                            <td class="col-conf">95.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">ACIERTO SÓLIDO: Bastión del Metropolitano (2-0); el Atlético del Cholo neutralizó por completo el ataque del Manchester United.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$14.00</td>
                        </tr>

                        <tr class="audit-row row-loss" data-category="fija" data-status="loss">
                            <td class="col-id">#96</td>
                            <td>
                                <div class="match-name">Villarreal vs Napoli</div>
                                <div class="match-tourn">UEFA Champions League &bull; Martes 13/10/2026 &bull; Final: 1 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Empate o Napoli (X2) [Doble Oportunidad]</div>
                            </td>
                            <td class="col-odds">@1.14</td>
                            <td class="col-conf">96.8%</td>
                            <td>
                                <span class="badge-status badge-loss">❌ FALLADO</span>
                                <div class="diag-text">FALLO: Villarreal venció 1-0 en La Cerámica con gol en el tramo final. Napoli no tuvo contundencia en sus transiciones y cedió la victoria local.</div>
                            </td>
                            <td class="col-pnl pnl-loss">-$100.00</td>
                        </tr>"""

    # Encontrar y reemplazar desde #91 hasta el final de la tabla
    row91_pos = html.find('<td class="col-id">#91</td>')
    if row91_pos != -1:
        start_tr = html.rfind('<tr class="audit-row', 0, row91_pos)
        end_tbody = html.find('</tbody>', row91_pos)
        if start_tr != -1 and end_tbody != -1:
            html = html[:start_tr] + rows_real_html + "\n                    " + html[end_tbody:]

    # 3. ACTUALIZAR SECCIÓN DE AUTOAPRENDIZAJE (ÁREA 3)
    c81_header_old = "Ciclo #81 &bull; 12 Agentes (Veto de Raíz a Hándicaps y 5.5 Goles &bull; 100% Mercados Reales)"
    c81_header_new = "Ciclo #81 &bull; Post-Mortem Crítico Champions League (2 Fallos: Inter y Napoli &bull; Lección Táctica Barça)"
    html = html.replace(c81_header_old, c81_header_new)

    html = re.sub(
        r'Win Rate Fijas: 95\.3% \[61/64\] \| Win Rate Global: 92\.7% \[89/96\] \| Brier Score: ~0\.068 \| Racha Activa: 14 Verdes \| Ciclo #81',
        r'Win Rate Fijas: 92.2% [59/64] | Win Rate Global: 90.6% [87/96] | Racha Rota por Inter (3-4) | PnL: +$1,075.75 | Ciclo #81',
        html
    )

    # Reemplazar observaciones del ciclo #81
    old_obs_part = "6/6 pronósticos cumplidos con éxito (Arsenal, Inter, Barcelona, Bayern, Atlético, Napoli). Racha activa extendida a 14 aciertos consecutivos en Las Fijas."
    new_obs_part = "AUDITORÍA REAL MARTES 13/10 (4 Aciertos / 2 Fallos): Inter cayó 3-4 ante Club Brugge en San Siro y Villarreal superó 1-0 a Napoli. La racha de 9 se quebró."
    html = html.replace(old_obs_part, new_obs_part)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Archivo {filename} sincronizado con la auditoría real y métricas transparentes.")
