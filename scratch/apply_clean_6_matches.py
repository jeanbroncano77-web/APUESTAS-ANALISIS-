# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_elite_6_saturday_slate import MATCHES_DATA, switcher_html, views_html, chart_configs_js, all_fijas_js, sim_results
import json
import re

# Banner Superior de la Jornada
banner_html = '''        <div id="view-container-matches">
            <!-- BANNER PRINCIPAL DE LA JORNADA: LOS 6 PARTIDOS ESTELARES -->
            <div style="background: linear-gradient(135deg, rgba(30, 27, 75, 0.95), rgba(15, 23, 42, 0.98)); border: 2px solid rgba(59, 130, 246, 0.6); border-radius: 20px; padding: 1.75rem 2rem; margin-bottom: 2rem; backdrop-filter: blur(16px); box-shadow: 0 16px 36px -8px rgba(59, 130, 246, 0.35);">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 1rem;">
                    <div>
                        <span style="background: #3b82f6; color: #ffffff; padding: 0.35rem 0.85rem; border-radius: 9999px; font-weight: 800; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.8px;">
                            JORNADA OFICIAL &bull; SÁBADO 7 DE NOVIEMBRE DE 2026
                        </span>
                        <h2 style="font-size: 1.75rem; font-weight: 900; color: #ffffff; margin: 0.6rem 0 0.2rem 0; letter-spacing: -0.5px;">
                            Los 6 Partidos Estelares &bull; Tarde & Noche (12:30 a 20:30 ECU)
                        </h2>
                        <div style="color: #94a3b8; font-size: 0.92rem;">
                            Haz clic en cada partido para abrir su análisis profundo multi-agente, xG, cuotas Ecuabet, props y La Fija de Oro.
                        </div>
                    </div>
                    <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 14px; padding: 0.75rem 1.25rem; text-align: right;">
                        <div style="font-size: 0.75rem; color: #6ee7b7; font-weight: 700; text-transform: uppercase;">Saldo Personal Ecuabet</div>
                        <div style="font-size: 1.4rem; font-weight: 900; color: #ffffff;">$24.90 USD <span style="font-size: 0.8rem; color: #10b981;">(INTACTO)</span></div>
                        <div style="font-size: 0.7rem; color: #94a3b8;">Muralla de $20 protegida &bull; $4.90 de colchón</div>
                    </div>
                </div>

                <!-- Estrategias de Apuesta -->
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-top: 1.25rem;">
                    <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 12px; padding: 1rem;">
                        <div style="font-size: 0.75rem; color: #f59e0b; font-weight: 800; text-transform: uppercase;">Opción 1: El Francotirador Solitario</div>
                        <div style="font-size: 1rem; font-weight: 800; color: #ffffff; margin: 0.25rem 0;">PSG Gana Directo @ 1.20</div>
                        <div style="font-size: 0.8rem; color: #94a3b8;">Con $4.90 USD cobras <strong>$5.88 USD</strong> en el Parque de los Príncipes.</div>
                    </div>
                    <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 12px; padding: 1rem;">
                        <div style="font-size: 0.75rem; color: #10b981; font-weight: 800; text-transform: uppercase;">Opción 2: La Fija Doble (Recomendada)</div>
                        <div style="font-size: 1rem; font-weight: 800; color: #ffffff; margin: 0.25rem 0;">PSG Gana (1) + Real Madrid X2 @ 1.49</div>
                        <div style="font-size: 0.8rem; color: #94a3b8;">Con $4.90 USD cobras <strong>$7.30 USD</strong> (+$2.40 netos, saldo a $27.30 USD).</div>
                    </div>
                </div>
            </div>

            <!-- Switcher Tabs (0 a 5) -->
'''

new_area1_content = banner_html + switcher_html + views_html + '        </div> <!-- Fin de view-container-matches -->\n\n'

files_to_update = ['index.html', 'dashboard_pronosticos.html', '../index.html']

for fpath in files_to_update:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Skipping {fpath}: {e}")
        continue

    # Encontrar inicio de view-container-matches
    start_tag = '<div id="view-container-matches">'
    start_idx = html.find(start_tag)
    if start_idx == -1:
        print(f"Error: {start_tag} not found in {fpath}")
        continue

    # Encontrar inicio de VISTA 2
    end_tag = '<!-- VISTA 2: WIN RATE & AUDITORÍA EN VIVO -->'
    end_idx = html.find(end_tag)
    if end_idx == -1:
        print(f"Error: {end_tag} not found in {fpath}")
        continue

    # Reemplazar exactamente el bloque
    html = html[:start_idx] + new_area1_content + html[end_idx:]

    # Asegurar chartConfigs
    html = re.sub(r'var chartConfigs = \[.*?\];', chart_configs_js, html, flags=re.DOTALL)
    
    # Asegurar allFijasData
    html = re.sub(r'var allFijasData = \[.*?\];', all_fijas_js, html, flags=re.DOTALL)

    # Asegurar títulos y botones de cabecera a 6 Partidos
    html = re.sub(
        r'<title>.*?</title>',
        '<title>SportsAI Analytics &middot; 6 Partidos Estelares &bull; Sábado 07/11 &bull; Win Rate & Autoaprendizaje</title>',
        html
    )
    html = re.sub(
        r'Motor Predictivo Multi-Agente &bull; \d+ Partidos Estelares &bull; [^<]+',
        'Motor Predictivo Multi-Agente &bull; 6 Partidos Estelares &bull; Sábado 07/11 (Tarde & Noche)',
        html
    )
    html = re.sub(
        r'⚽ Partidos &amp; Pronósticos \(\d+\)|⚽ Partidos & Pronósticos \(\d+\)',
        '⚽ Partidos & Pronósticos (6)',
        html
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Successfully injected 6 interactive match views into {fpath}")

with open('sports_agents/simulations_tomorrow_results.json', 'w', encoding='utf-8') as f:
    json.dump(sim_results, f, ensure_ascii=False, indent=2)
print("Updated sports_agents/simulations_tomorrow_results.json with 6 matches.")
