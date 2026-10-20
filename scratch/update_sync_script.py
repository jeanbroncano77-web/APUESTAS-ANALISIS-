import os
import sys

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
sync_script = os.path.join(base_dir, "sports_agents", "sync_complete_dashboard_3areas.py")

with open(sync_script, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update Ciclo #107 to Ciclo #108 in nav_patch
code = code.replace("Ciclo #107", "Ciclo #108")

# 2. Add Autopsia #9 and Caso de Exito Ecuabet to autopsies_patch
autopsies_addition = """
            <!-- AUTOPSIA #9: LEEDS UNITED 1-1 MANCHESTER UNITED (FALLO REAL EN PREMIER LEAGUE) -->
            <div class="autopsy-card" style="border: 2px solid rgba(239, 68, 68, 0.6); background: rgba(30, 27, 75, 0.7); box-shadow: 0 16px 36px -8px rgba(239, 68, 68, 0.35); margin-bottom: 2rem;">
                <div class="autopsy-header">
                    <div>
                        <div class="autopsy-match" style="color: #f87171; display: flex; align-items: center; gap: 0.5rem;">
                            <span>🚨 AUTOPSIA #9 (FALLO REAL AUDITADO EN VIVO):</span>
                        </div>
                        <div style="font-size: 1.25rem; font-weight: 800; color: #ffffff; margin-top: 0.25rem;">
                            Leeds United vs Manchester United (1-1) &bull; Fricción de Visitante en Elland Road & Advertencia del Usuario
                        </div>
                        <div style="font-size: 0.82rem; color: var(--text-muted); margin-top: 0.2rem;">
                            Componente: MarketRealityAgent &bull; TacticalManagerAgent &bull; Factor 'premier_league_away_favorite_friction'
                        </div>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 0.35rem;">
                        <span class="badge-status badge-loss" style="background: rgba(239, 68, 68, 0.25); border: 1px solid rgba(239, 68, 68, 0.6); color: #fca5a5; font-size: 0.85rem;">
                            ❌ FALLO REAL: -$100.00 USD
                        </span>
                        <span class="badge-status badge-win" style="background: rgba(16, 185, 129, 0.25); border: 1px solid rgba(16, 185, 129, 0.6); color: #6ee7b7; font-size: 0.85rem;">
                            🛡️ VETO 1X2 VISITANTE ACTIVO
                        </span>
                    </div>
                </div>
                
                <div class="autopsy-split">
                    <div class="box-flaw" style="border-color: rgba(239, 68, 68, 0.4); background: rgba(239, 68, 68, 0.1);">
                        <div class="box-title-flaw">
                            <span>❌ Diagnóstico del Error (¿Por qué falló el pronóstico?)</span>
                        </div>
                        <div class="box-text">
                            <p><strong>1. Subestimación de la Caldera de Elland Road:</strong> El United ganaba con gol de Bryan Mbeumo (35'), pero Leeds empujó con apoyo de su gente y empató mediante Dominic Calvert-Lewin al 51' (1-1). La victoria directa visitante no toleró la fricción del derbi.</p>
                            <p style="margin-top: 0.5rem;"><strong>2. Confirmación de la Hipótesis del Usuario:</strong> El usuario advirtió explícitamente: <em>"el arsenal va de visita no quieres que se dañe la fija que deley gane?"</em>. Esta alerta fue 100% profética: en Inglaterra, forzar victorias de visita sin seguro de empate rompe boletos.</p>
                        </div>
                    </div>
                    
                    <div class="box-fix" style="border-color: rgba(16, 185, 129, 0.4); background: rgba(6, 78, 59, 0.2);">
                        <div class="box-title-fix">
                            <span>🛡️ Calibración Matemática Implementada (FeedbackEngine 3.0)</span>
                        </div>
                        <div class="box-text">
                            <p><strong>1. Factor 'premier_league_away_favorite_friction' (1.28x):</strong> En partidos de Premier League fuera de casa con cuotas &gt; 1.50, se prohíbe de raíz la Victoria Directa como Fija de Oro.</p>
                            <p style="margin-top: 0.5rem;"><strong>2. Migración Obligatoria a DNB o X2:</strong> Todo favorito visitante en plazas hostiles debe llevar cobertura de Empate No Válido (DNB) o Doble Oportunidad, blindando la banca contra empates trampa.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- CASO DE ÉXITO & APRENDIZAJE #2: BOLETO DOBLE ECUABET (COBRO RATIFICADO DEL USUARIO) -->
            <div class="autopsy-card" style="border: 2px solid rgba(16, 185, 129, 0.6); background: rgba(6, 78, 59, 0.25); box-shadow: 0 16px 36px -8px rgba(16, 185, 129, 0.35); margin-bottom: 2rem;">
                <div class="autopsy-header">
                    <div>
                        <div class="autopsy-match" style="color: #34d399; display: flex; align-items: center; gap: 0.5rem;">
                            <span>⭐ CASO DE ÉXITO & APRENDIZAJE #2 (BOLETO USUARIO ECUABET COBRADO EN VIVO):</span>
                        </div>
                        <div style="font-size: 1.25rem; font-weight: 800; color: #ffffff; margin-top: 0.25rem;">
                            Arsenal DNB (@1.18) + Real Madrid 1X2 (@1.25) &bull; Cuota 1.47 Acertada al 100%
                        </div>
                        <div style="font-size: 0.82rem; color: var(--text-muted); margin-top: 0.2rem;">
                            Gestión de Capital Aplicada: $10 apostados &bull; Cobro de $14.77 netos (+$4.77) &bull; Capital sube a $74.77 USD
                        </div>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 0.35rem;">
                        <span class="badge-status badge-win" style="background: rgba(16, 185, 129, 0.3); border: 1px solid rgba(16, 185, 129, 0.7); color: #6ee7b7; font-size: 0.85rem;">
                            ✅ COBRO ECUABET: +$4.77 NETOS
                        </span>
                        <span class="badge-status badge-win" style="background: rgba(59, 130, 246, 0.25); border: 1px solid rgba(59, 130, 246, 0.6); color: #93c5fd; font-size: 0.85rem;">
                            👑 ESTRATEGIA DNB + 1X2 RATIFICADA
                        </span>
                    </div>
                </div>
                
                <div class="autopsy-split">
                    <div class="box-flaw" style="border-color: rgba(59, 130, 246, 0.4); background: rgba(59, 130, 246, 0.1);">
                        <div class="box-title-flaw" style="color: #93c5fd;">
                            <span>💡 La Estrategia Impecable del Usuario en Ecuabet</span>
                        </div>
                        <div class="box-text">
                            <p><strong>1. Protección de Capital:</strong> El usuario aplicó seguro DNB al Arsenal (visitante) y victoria simple al Real Madrid (local en Bernabéu), combinando a cuota @1.47 en Ecuabet.</p>
                            <p style="margin-top: 0.5rem;"><strong>2. Resultado en Cancha:</strong> Arsenal ganó 0-1 con gol de Madueke y Real Madrid goleó 4-1 con doblete de Mbappé y Güler. Boleto cobrado sin despeinarse.</p>
                        </div>
                    </div>
                    
                    <div class="box-fix" style="border-color: rgba(16, 185, 129, 0.4); background: rgba(6, 78, 59, 0.2);">
                        <div class="box-title-fix">
                            <span>🛡️ Conclusión Cuantitativa (Ciclo #108)</span>
                        </div>
                        <div class="box-text">
                            <p><strong>1. Eficiencia de Banca:</strong> Se ratifica la regla de no sobrearriesgar capital: apostar el 14% de la banca ($10 de $70) permite sumar beneficios constantes manteniendo $60 intocables.</p>
                            <p style="margin-top: 0.5rem;"><strong>2. Escalada hacia los $100 USD:</strong> Con este cobro, el capital personal del usuario asciende a $74.77 USD, cumpliendo el plan de crecimiento patrimonial seguro.</p>
                        </div>
                    </div>
                </div>
            </div>"""

target_insert = '<!-- CASO DE ÉXITO & APRENDIZAJE: FC BARCELONA 5-1 SEVILLA -->'
if target_insert in code:
    # insert before or after
    pos = code.find('</div>\n            </div>"""')
    if pos != -1:
        code = code[:pos] + autopsies_addition + code[pos:]

# 3. Robust autopsy_marker_start replacement
old_marker_block = """autopsy_marker_start = html.find('<!-- AUTOPSIA #6 DESTACADA')
if autopsy_marker_start != -1:
    autopsy_marker_end = html.find('<!-- SECCIÓN 3: CONTROL DE HIPERPARÁMETROS', autopsy_marker_start)
    if autopsy_marker_end == -1:
        autopsy_marker_end = html.find('<table', autopsy_marker_start)
    if autopsy_marker_end != -1:
        html = html[:autopsy_marker_start] + autopsies_patch + "\\n\\n            " + html[autopsy_marker_end:]
        print("   -> Autopsias actualizadas con Villarreal 1-1 Getafe, AS Roma 0-1 Inter y FC Barcelona 5-1.")"""

new_marker_block = """autopsy_marker_start = html.find('<!-- AUTOPSIAS DE APRENDIZAJE CUANTITATIVO RECIENTE')
if autopsy_marker_start == -1:
    autopsy_marker_start = html.find('<!-- AUTOPSIA #6 DESTACADA')

if autopsy_marker_start != -1:
    autopsy_marker_end = html.find('<!-- SECCIÓN 3: CONTROL DE HIPERPARÁMETROS', autopsy_marker_start)
    if autopsy_marker_end == -1:
        autopsy_marker_end = html.find('<table', autopsy_marker_start)
    if autopsy_marker_end != -1:
        html = html[:autopsy_marker_start] + autopsies_patch + "\\n\\n            " + html[autopsy_marker_end:]
        print("   -> Autopsias actualizadas con Villarreal, Roma-Inter, Barcelona, Leeds-United y Ecuabet.")"""

code = code.replace(old_marker_block, new_marker_block)

with open(sync_script, "w", encoding="utf-8") as f_w:
    f_w.write(code)

print("✓ sync_complete_dashboard_3areas.py mejorado con Autopsia #9 y Cobro Ecuabet.")
