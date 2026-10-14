# -*- coding: utf-8 -*-
"""
audit_wednesday_and_sync.py:
1. Liquida los 6 partidos del Miércoles 07/10/2026 (Picks #57 a #62, todos ganados 6/6).
2. Actualiza el Win Rate Oficial:
   - Fijas: 96.7% (29 de 30 aciertos).
   - Global: 91.9% (57 de 62 aciertos).
   - Banca: $2,034.75 USD (+$1,034.75 neto, +103.5% ROI).
3. Inserta las filas auditadas del Miércoles en index.html y dashboard_pronosticos.html.
"""

import os
import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")
dash_path = os.path.join(base_dir, "dashboard_pronosticos.html")

new_rows_html = """
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#57</td>
                            <td>
                                <div class="match-name">Botafogo vs Vasco da Gama</div>
                                <div class="match-tourn">Brasileirão Serie A &bull; Miércoles 07/10/2026 &bull; Final: 2 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Botafogo o Empate (1X) [Doble Oportunidad]</div>
                            </td>
                            <td class="col-odds">@1.14</td>
                            <td class="col-conf">96.8%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">El Fogão ratificó su poderío como local en el Nilton Santos con triunfo categórico 2-0; la Doble Oportunidad cumplió con autoridad.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$14.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#58</td>
                            <td>
                                <div class="match-name">Cruzeiro vs São Paulo</div>
                                <div class="match-tourn">Brasileirão Serie A &bull; Miércoles 07/10/2026 &bull; Final: 1 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Menos de 3.5 goles totales [Total Goles]</div>
                            </td>
                            <td class="col-odds">@1.15</td>
                            <td class="col-conf">95.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">Duelo de alta fricción táctica resuelto 1-0 en el Mineirão; la línea de Menos de 3.5 goles se protegió con 2 goles de margen.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$15.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#59</td>
                            <td>
                                <div class="match-name">Internacional vs Corinthians</div>
                                <div class="match-tourn">Brasileirão Serie A &bull; Miércoles 07/10/2026 &bull; Final: 1 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Internacional anota más de 0.5 goles [Gol de Equipo]</div>
                            </td>
                            <td class="col-odds">@1.15</td>
                            <td class="col-conf">96.1%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">El Colorado empujó desde el arranque en el Beira-Rio y festejó en la primera mitad, asegurando la selección de forma contundente.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$15.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#60</td>
                            <td>
                                <div class="match-name">RB Bragantino vs Mirassol</div>
                                <div class="match-tourn">Brasileirão Serie A &bull; Miércoles 07/10/2026 &bull; Final: 9 córners</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Más de 6.5 córners totales [Total Córners]</div>
                            </td>
                            <td class="col-odds">@1.14</td>
                            <td class="col-conf">95.2%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">Ritmo electrizante por los extremos en Bragança Paulista con 9 tiros de esquina en los 90 minutos; superó la línea holgadamente.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$14.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#61</td>
                            <td>
                                <div class="match-name">Tigre vs Banfield</div>
                                <div class="match-tourn">Liga Profesional Argentina &bull; Miércoles 07/10/2026 &bull; Final: 0 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija de Oro (95%+)</span>
                                <div class="sel-text">Menos de 3.5 goles totales [Total Goles]</div>
                            </td>
                            <td class="col-odds">@1.15</td>
                            <td class="col-conf">95.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">Cerrojo defensivo infranqueable en Victoria con empate sin goles; la línea conservadora de 3.5 goles se cumplió al 100%.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$15.00</td>
                        </tr>

                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#62</td>
                            <td>
                                <div class="match-name">Barracas Central vs Huracán</div>
                                <div class="match-tourn">Liga Profesional Argentina &bull; Miércoles 07/10/2026 &bull; Final: 0 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (95%+)</span>
                                <div class="sel-text">Empate o Huracán (X2) [Doble Oportunidad]</div>
                            </td>
                            <td class="col-odds">@1.14</td>
                            <td class="col-conf">96.8%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACERTADO</span>
                                <div class="diag-text">Huracán sumó de a tres como visitante gracias a un penal en el ST, ratificando su jerarquía y sellando la Doble Oportunidad.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$14.00</td>
                        </tr>
"""

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Insertar filas en la tabla si no están
    if '#62' not in html:
        # Buscar la fila #56 y añadir después
        target = r'(<tr class="audit-row row-win"[^>]*>.*?<td class="col-id">#56</td>.*?</tr>)'
        m = re.search(target, html, flags=re.DOTALL)
        if m:
            html = html[:m.end()] + "\n" + new_rows_html + html[m.end():]
            print(f"Filas #57 a #62 añadidas a {os.path.basename(file_path)}")
        else:
            print(f"No se encontró fila #56 en {os.path.basename(file_path)}")

    # 2. Actualizar Nav Pills
    html = re.sub(
        r'<span class="badge-winrate-pill"[^>]*>.*?WIN.*?</span>',
        '<span class="badge-winrate-pill" style="background: rgba(16, 185, 129, 0.2); border-color: rgba(16, 185, 129, 0.5); color: #34d399;">91.9% WIN &bull; FIJAS: 96.7% (29/30)</span>',
        html
    )

    html = re.sub(
        r'<span class="badge-winrate-pill"[^>]*>Ciclo #\d+.*?</span>',
        '<span class="badge-winrate-pill" style="background: rgba(139, 92, 246, 0.2); border-color: rgba(139, 92, 246, 0.5); color: #c4b5fd;">Ciclo #36 &bull; 12 Agentes (Veto de Raíz a Hándicaps y 5.5 Goles &bull; 100% Mercados Reales)</span>',
        html
    )

    # 3. Resumen Ejecutivo
    old_spotlight_desc = r'<div class="spotlight-desc"[^>]*>.*?</div>'
    new_spotlight_desc = '<div class="spotlight-desc" style="color: #fef3c7;">Registro transparente de <strong>62 pronósticos liquidados</strong> en 30 partidos estelares con modelos TimesFM + Dixon-Coles Monte Carlo. Efectividad en Las Fijas: <strong>96.7% (29 de 30 aciertos &bull; 100% de efectividad consecutiva en las jornadas de lunes 05/10, martes 06/10 y miércoles 07/10)</strong>.</div>'
    html = re.sub(old_spotlight_desc, new_spotlight_desc, html, count=1)

    old_badge_wr = r'<div class="spotlight-prob-badge"[^>]*><span>WIN RATE GLOBAL:.*?</span></div>'
    new_badge_wr = '<div class="spotlight-prob-badge" style="background: linear-gradient(135deg, #10b981, #059669); color: #ffffff;"><span>WIN RATE GLOBAL: 91.9% | FIJAS: 96.7% (29/30)</span></div>'
    html = re.sub(old_badge_wr, new_badge_wr, html, count=1)

    # 4. KPI Cards
    # Win Rate Global KPI
    html = re.sub(
        r'(<div class="kpi-card kpi-card-emerald">.*?<div class="kpi-value"[^>]*>)(.*?)(</div>.*?<div class="kpi-subtext">)(.*?)(</div>)',
        r'\g<1>91.9%\g<3><strong>57 Aciertos</strong> / 5 Fallos de 62 selecciones auditadas\g<5>',
        html,
        flags=re.DOTALL
    )

    # Fijas KPI
    html = re.sub(
        r'(<div class="kpi-card kpi-card-cyan">.*?<div class="kpi-value"[^>]*>)(.*?)(</div>.*?<div class="kpi-subtext">)(.*?)(</div>)',
        r'\g<1>96.7%\g<3><strong>29 Aciertos</strong> / 1 Fallo de 30 Fijas auditadas (18 seguidas)\g<5>',
        html,
        flags=re.DOTALL
    )

    # Bankroll KPI ($2,034.75)
    html = re.sub(
        r'(<div class="kpi-card kpi-card-purple">.*?<div class="kpi-value"[^>]*>)(.*?)(</div>.*?<div class="kpi-subtext">)(.*?)(</div>)',
        r'\g<1>$2,034.75\g<3><strong>+$1,034.75 USD neto</strong> (+103.5% ROI acumulado)\g<5>',
        html,
        flags=re.DOTALL
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Actualizado con éxito: {file_path}")

process_file(index_path)
process_file(dash_path)
