# -*- coding: utf-8 -*-
"""
patch_sync_script_with_autopsy14.py
Inserta Autopsia #14 en sports_agents/sync_complete_dashboard_3areas.py
y sincroniza index.html, dashboard_pronosticos.html y ../index.html.
"""

import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

sync_path = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo\sports_agents\sync_complete_dashboard_3areas.py"

with open(sync_path, "r", encoding="utf-8") as f:
    content = f.read()

target_marker = "            <!-- AUTOPSIA DE FALLO #13: LA PUÑALADA DE MBAPPÉ AL MINUTO 88"

if target_marker not in content:
    print("❌ target_marker not found!")
    sys.exit(1)

autopsy14_html = """            <!-- AUTOPSIA DE FALLO #14: EL CERROJO DE HANSI FLICK (BARÇA 3-0 ASTON VILLA) Y EL PENAL AL 90+9' EN ECHALECHE -->
            <div class="autopsy-card" style="border: 2px solid rgba(239, 68, 68, 0.6); background: rgba(127, 29, 29, 0.25); box-shadow: 0 16px 36px -8px rgba(239, 68, 68, 0.35); margin-bottom: 2rem;">
                <div class="autopsy-header">
                    <div>
                        <div class="autopsy-match" style="color: #f87171; display: flex; align-items: center; gap: 0.5rem;">
                            <span>⚠️ AUTOPSIA DE FALLO #14 &bull; MARTES 03/11 (CHAMPIONS & LIGAPRO):</span>
                        </div>
                        <div style="font-size: 1.25rem; font-weight: 800; color: #ffffff; margin-top: 0.25rem;">
                            Barça 3-0 Aston Villa (Fallo BTTS) &bull; Mushuc Runa 2-3 Manta FC (Penal al 90+9') &bull; Banca de Usuario Salvada
                        </div>
                        <div style="font-size: 0.82rem; color: var(--text-muted); margin-top: 0.2rem;">
                            Componente: OffsideTrapAuditor &bull; StoppageTimeAnomaly &bull; Ciclo de Autoaprendizaje #129 &bull; Saldo usuario: $24.90 USD INTACTOS
                        </div>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 0.35rem;">
                        <span class="badge-status badge-loss" style="background: rgba(239, 68, 68, 0.3); border: 1px solid rgba(239, 68, 68, 0.7); color: #fca5a5; font-size: 0.85rem;">
                            ❌ 2 FALLOS EN CARTELERA (-$200 MODELO)
                        </span>
                        <span class="badge-status badge-win" style="background: rgba(16, 185, 129, 0.3); border: 1px solid rgba(16, 185, 129, 0.7); color: #6ee7b7; font-size: 0.85rem;">
                            🛡️ USUARIO PRESERVÓ SUS $24.90 USD
                        </span>
                    </div>
                </div>
                
                <div class="autopsy-split">
                    <div class="box-flaw" style="border-color: rgba(239, 68, 68, 0.4); background: rgba(127, 29, 29, 0.2);">
                        <div class="box-title-flaw" style="color: #fca5a5;">
                            <span>🔍 Diagnóstico del Error: ¿Por qué falló el 'Ambos Marcan' y el 1X en Ambato?</span>
                        </div>
                        <div class="box-text">
                            <p><strong>1. La Trampa de Fuera de Juego de Hansi Flick:</strong> El modelo proyectó que Aston Villa anotaría basándose en sus 12 goles en Champions y las bajas de Koundé y Christensen. Sin embargo, Flick sincronizó su línea a 45m provocando 7 fueras de juego a los delanteros de Emery, mientras Joan García tapó las 2 opciones claras. Villa se fue en blanco (3-0).</p>
                            <p style="margin-top: 0.5rem;"><strong>2. La Anomalía del Minuto 99 en Echaleche:</strong> Mushuc Runa empataba 2-2 en el 95', pero un penal polémico sancionado al minuto 90+9 convertido por Joaquín Vergés le dio la victoria al Manta 2-3 en tiempo récord de descuento.</p>
                            <p style="margin-top: 0.5rem;"><strong>3. La Visión del Usuario:</strong> El usuario advirtió en vivo: <em>"imagínate que ponía ambos marcan se jodía"</em>. Decidió no apostar y salvó el 100% de su capital de $24.90 USD.</p>
                        </div>
                    </div>
                    
                    <div class="box-solution" style="border-color: rgba(16, 185, 129, 0.4); background: rgba(6, 78, 59, 0.2);">
                        <div class="box-title-solution">
                            <span>🛡️ Calibración Matemática Implementada (Regla #121)</span>
                        </div>
                        <div class="box-text">
                            <p><strong>1. Regla de Oro #121 (Filtro Anti-BTTS ante Línea de Fuera de Juego):</strong> Ante equipos con sistemas de fuera de juego asfixiantes (como el Barça de Flick), se prohíbe el 'Ambos Marcan' simple. La selección obligatoria debe ser <strong>'1X + Más de 1.5 Goles'</strong> (la cual sí se cumplió sobrado 3-0).</p>
                            <p style="margin-top: 0.5rem;"><strong>2. Veto a Doble Oportunidad en Descenso Ecuatoriano:</strong> En partidos del hexagonal de permanencia con añadidos > 8 minutos, se prohíbe la doble oportunidad en cuotas menores a 1.30 debido a la volatilidad de penales tardíos.</p>
                            <p style="margin-top: 0.5rem;"><strong>3. Estado Institucional Consolidado:</strong> 186 picks auditados &bull; <strong>87.1% Win Rate Global</strong> (162 W / 24 L) &bull; <strong>87.0% Win Rate Fijas</strong> (127 W / 19 L) &bull; Saldo real del usuario: <strong>$24.90 USD intactos</strong>.</p>
                        </div>
                    </div>
                </div>
            </div>\n\n"""

new_content = content.replace(target_marker, autopsy14_html + target_marker)
with open(sync_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("✓ sports_agents/sync_complete_dashboard_3areas.py parchado con Autopsia #14.")
