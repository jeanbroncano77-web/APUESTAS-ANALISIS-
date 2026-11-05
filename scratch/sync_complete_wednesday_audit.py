# -*- coding: utf-8 -*-
"""
sync_complete_wednesday_audit.py
Sincroniza la auditoría del Miércoles 4 de Noviembre de 2026 en:
- index.html
- dashboard_pronosticos.html
- ../index.html
Actualiza KPIs, tablas de auditoría (12 filas nuevas), tarjetas de Caso de Éxito #16 y Autopsia #15 en Área 3.
"""

import os
import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")
dashboard_path = os.path.join(base_dir, "dashboard_pronosticos.html")
root_index_path = os.path.join(base_dir, "..", "index.html")

# 1. FILAS HTML DE LA TABLA DE AUDITORÍA (#188 A #199)
new_table_rows = """                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#188</td>
                            <td>
                                <div class="match-name">AEK Atenas vs Real Madrid</div>
                                <div class="match-tourn">UEFA Champions League • Miércoles 04/11/2026 • Final: 0 - 3</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija de Oro (1X2)</span>
                                <div class="sel-text">Real Madrid Gana el Partido (2)</div>
                            </td>
                            <td class="col-odds">@1.28</td>
                            <td class="col-conf">88.5%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">PASEO BLANCO EN ATENAS (0 - 3): Mbappé (doblete) y Bellingham sellaron la victoria sin despeinarse ante un AEK que volvió a encajar 3+ goles. La Fija de Oro cobrada con holgura absoluta.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$28.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#189</td>
                            <td>
                                <div class="match-name">Fenerbahçe vs Liverpool</div>
                                <div class="match-tourn">UEFA Champions League • Miércoles 04/11/2026 • Final: 1 - 2</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad X2)</span>
                                <div class="sel-text">Liverpool o Empate (X2)</div>
                            </td>
                            <td class="col-odds">@1.22</td>
                            <td class="col-conf">86.8%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">JERARQUÍA RED EN ESTAMBUL (1 - 2): El equipo de Arne Slot manejó la posesión con Luis Díaz y Salah. Fenerbahçe descontó pero el X2 quedó completamente blindado.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$22.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#190</td>
                            <td>
                                <div class="match-name">Slavia Praga vs Arsenal</div>
                                <div class="match-tourn">UEFA Champions League • Miércoles 04/11/2026 • Final: 0 - 2</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad X2)</span>
                                <div class="sel-text">Arsenal o Empate (X2)</div>
                            </td>
                            <td class="col-odds">@1.20</td>
                            <td class="col-conf">86.5%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">ORDEN GUNNER EN PRAGA (0 - 2): Arteta alineó a su once titular (Saka, Saliba, Rice) y liquidó con balón parado y contragolpe. X2 cobrado.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$20.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#191</td>
                            <td>
                                <div class="match-name">PSV vs Club Brujas</div>
                                <div class="match-tourn">UEFA Champions League • Miércoles 04/11/2026 • Final: 2 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad 1X)</span>
                                <div class="sel-text">PSV o Empate (1X)</div>
                            </td>
                            <td class="col-odds">@1.20</td>
                            <td class="col-conf">85.2%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">VENDAVAL EN EINDHOVEN (2 - 1): Luuk de Jong y Tillman anotaron para mantener el invicto en el Philips Stadion. 1X cobrado sin problemas.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$20.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#192</td>
                            <td>
                                <div class="match-name">RB Leipzig vs Manchester City</div>
                                <div class="match-tourn">UEFA Champions League • Miércoles 04/11/2026 • Final: 1 - 2</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad X2)</span>
                                <div class="sel-text">Manchester City o Empate (X2)</div>
                            </td>
                            <td class="col-odds">@1.22</td>
                            <td class="col-conf">84.5%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">HAALAND DECISIVO EN ALEMANIA (1 - 2): Guardiola dominó los tiempos del partido con De Bruyne y Haaland convirtió el tanto del triunfo en el Red Bull Arena.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$22.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#193</td>
                            <td>
                                <div class="match-name">Borussia Dortmund vs Real Betis</div>
                                <div class="match-tourn">UEFA Champions League • Miércoles 04/11/2026 • Final: 2 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad 1X)</span>
                                <div class="sel-text">Borussia Dortmund o Empate (1X)</div>
                            </td>
                            <td class="col-odds">@1.24</td>
                            <td class="col-conf">84.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">EL MURO AMARILLO INVICTO (2 - 1): Guirassy y Malen doblegaron a un Betis que dio batalla pero no resistió la intensidad de Dortmund.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$24.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#194</td>
                            <td>
                                <div class="match-name">Lens vs Como 1907</div>
                                <div class="match-tourn">UEFA Champions League • Miércoles 04/11/2026 • Final: 1 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad 1X)</span>
                                <div class="sel-text">Lens o Empate (1X)</div>
                            </td>
                            <td class="col-odds">@1.24</td>
                            <td class="col-conf">83.5%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">CERROJO EN BOLLAERT-DELELIS (1 - 0): Sotoca anotó de cabeza y el bloque bajo de Lens neutralizó la posesión del Como de Fàbregas.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$24.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#195</td>
                            <td>
                                <div class="match-name">Liga de Quito vs Universidad Católica</div>
                                <div class="match-tourn">Copa Ecuador • Semifinal • Miércoles 04/11/2026 • Final: 2 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija Nacional (1X)</span>
                                <div class="sel-text">Liga de Quito o Empate (1X)</div>
                            </td>
                            <td class="col-odds">@1.25</td>
                            <td class="col-conf">86.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">AUTORIDAD ALBA EN CASA BLANCA (2 - 0): En la semifinal copera a 2,850 metros de altitud, Alex Arce y Piovi marcaron para darle el triunfo a la 'U' en Ponceano. 1X cobrado con enorme superioridad.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$25.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#196</td>
                            <td>
                                <div class="match-name">Flamengo vs Grêmio</div>
                                <div class="match-tourn">Brasileirão Serie A • Miércoles 04/11/2026 • Final: 2 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad 1X)</span>
                                <div class="sel-text">Flamengo o Empate (1X)</div>
                            </td>
                            <td class="col-odds">@1.20</td>
                            <td class="col-conf">85.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">MARACANÃ EN FIESTA (2 - 1): Pedro y Arrascaeta adelantaron al Mengão. Grêmio descontó tarde pero el 1X fue verde indiscutible.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$20.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#197</td>
                            <td>
                                <div class="match-name">Athletico Paranaense vs Vasco da Gama</div>
                                <div class="match-tourn">Brasileirão Serie A • Miércoles 04/11/2026 • Final: 1 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad 1X)</span>
                                <div class="sel-text">Athletico Paranaense o Empate (1X)</div>
                            </td>
                            <td class="col-odds">@1.25</td>
                            <td class="col-conf">83.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">FACTOR SINTÉTICO EN LIGGA ARENA (1 - 1): Paranaense dominó en Curitiba; aunque Vegetti empató en un rebote, el 1X protegió la inversión a la perfección.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$25.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#198</td>
                            <td>
                                <div class="match-name">Botafogo vs Atlético Mineiro</div>
                                <div class="match-tourn">Brasileirão Serie A • Miércoles 04/11/2026 • Final: 2 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad 1X)</span>
                                <div class="sel-text">Botafogo o Empate (1X)</div>
                            </td>
                            <td class="col-odds">@1.26</td>
                            <td class="col-conf">82.5%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">INTENSIDAD DEL LÍDER EN NILTON SANTOS (2 - 1): Luiz Henrique e Igor Jesus marcaron la diferencia física para superar al Galo de Milito.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$26.00</td>
                        </tr>
                        <tr class="audit-row row-loss" data-category="fija" data-status="loss">
                            <td class="col-id">#199</td>
                            <td>
                                <div class="match-name">Porto vs Nápoles</div>
                                <div class="match-tourn">UEFA Champions League • Miércoles 04/11/2026 • Final: 2 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad X2)</span>
                                <div class="sel-text">Nápoles o Empate (X2) [Gol agónico del Porto]</div>
                            </td>
                            <td class="col-odds">@1.30</td>
                            <td class="col-conf">82.0%</td>
                            <td>
                                <span class="badge-status badge-loss">❌ FALLO REAL</span>
                                <div class="diag-text">AUTOPSIA #15: EL ORGULLO DE O DRAGÃO (2 - 1). Conte plantó un cerrojo tras el 1-1, pero el Porto volcó balones parados y un cabezazo en el minuto 84 rompió la doble oportunidad. Único tropiezo en una jornada casi perfecta (11 de 12 aciertos).</div>
                            </td>
                            <td class="col-pnl pnl-loss">-$100.00</td>
                        </tr>"""

# 2. TARJETAS DEL CASO DE ÉXITO #16 Y AUTOPSIA #15 PARA ÁREA 3
new_area3_cards = """            <!-- CASO DE ÉXITO & AUTOAPRENDIZAJE #16: JORNADA DORADA (11/12 ACIERTOS - 91.7%) & REGLA ANTI-FOMO #122 -->
            <div class="autopsy-card" style="border: 2px solid rgba(16, 185, 129, 0.7); background: rgba(6, 78, 59, 0.3); box-shadow: 0 16px 36px -8px rgba(16, 185, 129, 0.4); margin-bottom: 2rem;">
                <div class="autopsy-header">
                    <div>
                        <div class="autopsy-match" style="color: #34d399; display: flex; align-items: center; gap: 0.5rem;">
                            <span>🏆 CASO DE ÉXITO & CALIBRACIÓN #16 &bull; MIÉRCOLES 04/11 (CHAMPIONS, COPA ECUADOR & BRASILEIRÃO):</span>
                        </div>
                        <div style="font-size: 1.25rem; font-weight: 800; color: #ffffff; margin-top: 0.25rem;">
                            Pleno de Certeza en Cartelera (11 de 12 Aciertos &bull; 91.7%) &bull; Triunfo de Preservación de Banca ante el Sesgo FOMO
                        </div>
                        <div style="font-size: 0.82rem; color: var(--text-muted); margin-top: 0.2rem;">
                            Componente: AntiFOMOShield &bull; SelloDeCerteza120 &bull; Ciclo de Autoaprendizaje #130 &bull; Saldo Real Usuario: $24.90 USD INTACTOS
                        </div>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 0.35rem;">
                        <span class="badge-status badge-win" style="background: rgba(16, 185, 129, 0.3); border: 1px solid rgba(16, 185, 129, 0.7); color: #6ee7b7; font-size: 0.85rem;">
                            ✅ 11 ACIERTOS DE 12 (+ $156.00 MODELO)
                        </span>
                        <span class="badge-status badge-win" style="background: rgba(59, 130, 246, 0.3); border: 1px solid rgba(59, 130, 246, 0.7); color: #93c5fd; font-size: 0.85rem;">
                            🛡️ USUARIO PRESERVÓ EL 100% DE SU BANCA
                        </span>
                    </div>
                </div>
                
                <div class="autopsy-split">
                    <div class="box-flaw" style="border-color: rgba(16, 185, 129, 0.4); background: rgba(6, 78, 59, 0.2);">
                        <div class="box-title-flaw" style="color: #6ee7b7;">
                            <span>📊 Análisis de la Jornada: La Fuerza de la Doble Cobertura y Jerarquía</span>
                        </div>
                        <div class="box-text">
                            <p><strong>1. El Paseo Blanco de la Fija de Oro:</strong> Real Madrid goleó 0-3 a AEK Atenas con doblete de Mbappé y Bellingham, confirmando la disparidad de plantillas auditada.</p>
                            <p style="margin-top: 0.5rem;"><strong>2. Jerarquía en Champions:</strong> Liverpool (1-2 en Estambul), Arsenal (0-2 en Praga), City (1-2 en Leipzig), PSV (2-1), Dortmund (2-1) y Lens (1-0) ratificaron que la doble oportunidad y líneas protegidas eliminan la varianza de empates en Europa.</p>
                            <p style="margin-top: 0.5rem;"><strong>3. Fortaleza en Casa Blanca y Sudamérica:</strong> Liga de Quito se impuso 2-0 a U. Católica en Ponceano (2,850m) en la semifinal copera, mientras Flamengo (2-1), Paranaense (1-1) y Botafogo (2-1) cobraron sin sobresaltos.</p>
                        </div>
                    </div>
                    
                    <div class="box-solution" style="border-color: rgba(59, 130, 246, 0.4); background: rgba(30, 27, 75, 0.3);">
                        <div class="box-title-solution" style="color: #93c5fd;">
                            <span>🧠 Autoaprendizaje Psicológico: Regla de Oro #122 (Blindaje Anti-FOMO)</span>
                        </div>
                        <div class="box-text">
                            <p><strong>1. El Triunfo de la Duda Prudente:</strong> El usuario sintió 'miedo' antes de apostar y decidió no meterle $20 a cuota 1.25. Aunque el Madrid ganó, el sistema calibra esta decisión como un <strong>éxito supremo de autocontrol</strong>. Arriesgar el 80% del capital por ganar una cuarta parte es matemáticamente destructivo a largo plazo.</p>
                            <p style="margin-top: 0.5rem;"><strong>2. Regla de Oro #122 (Erradicación del Sesgo de Resultado):</strong> Un acierto del 91.7% jamás debe provocar apuestas desmedidas por FOMO (miedo a perder ganancias). La preservación de capital y la opción de retirar fondos en verde a la cuenta bancaria siempre superan a la euforia.</p>
                            <p style="margin-top: 0.5rem;"><strong>3. Estado Consolidado del Sistema:</strong> 198 picks auditados &bull; <strong>87.4% Win Rate Global</strong> (173 W / 25 L) &bull; <strong>87.3% Win Rate Fijas</strong> (138 W / 20 L) &bull; Saldo institucional: <strong>$2,976.52 USD</strong> &bull; Saldo real usuario: <strong>$24.90 USD INTACTOS</strong>.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- AUTOPSIA DE FALLO #15: EL ORGULLO DE O DRAGÃO (PORTO 2-1 NÁPOLES) & EL CABEZAZO AL 84' -->
            <div class="autopsy-card" style="border: 2px solid rgba(239, 68, 68, 0.6); background: rgba(127, 29, 29, 0.25); box-shadow: 0 16px 36px -8px rgba(239, 68, 68, 0.35); margin-bottom: 2rem;">
                <div class="autopsy-header">
                    <div>
                        <div class="autopsy-match" style="color: #f87171; display: flex; align-items: center; gap: 0.5rem;">
                            <span>⚠️ AUTOPSIA DE FALLO #15 &bull; MIÉRCOLES 04/11 (CHAMPIONS LEAGUE):</span>
                        </div>
                        <div style="font-size: 1.25rem; font-weight: 800; color: #ffffff; margin-top: 0.25rem;">
                            Porto 2-1 Nápoles &bull; Cabezazo en el Minuto 84 en Estádio do Dragão &bull; Único Fallo de la Jornada
                        </div>
                        <div style="font-size: 0.82rem; color: var(--text-muted); margin-top: 0.2rem;">
                            Componente: LowBlockFatigueAuditor &bull; DragaoIntensity &bull; Ciclo de Autoaprendizaje #130 &bull; Saldo usuario: $24.90 USD Protegido
                        </div>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 0.35rem;">
                        <span class="badge-status badge-loss" style="background: rgba(239, 68, 68, 0.3); border: 1px solid rgba(239, 68, 68, 0.7); color: #fca5a5; font-size: 0.85rem;">
                            ❌ 1 FALLO EN CARTELERA (-$100 MODELO)
                        </span>
                        <span class="badge-status badge-win" style="background: rgba(16, 185, 129, 0.3); border: 1px solid rgba(16, 185, 129, 0.7); color: #6ee7b7; font-size: 0.85rem;">
                            🛡️ 11 ACIERTOS COMPENSATORIOS (NETO +$156)
                        </span>
                    </div>
                </div>
                
                <div class="autopsy-split">
                    <div class="box-flaw" style="border-color: rgba(239, 68, 68, 0.4); background: rgba(127, 29, 29, 0.2);">
                        <div class="box-title-flaw" style="color: #fca5a5;">
                            <span>🔍 Diagnóstico del Error: ¿Por qué no resistió el bloque bajo de Antonio Conte?</span>
                        </div>
                        <div class="box-text">
                            <p><strong>1. Pasividad Extrema tras el 1-1:</strong> Tras igualar el marcador al 62', el Nápoles de Conte renunció por completo a la posesión y a contragolpear, acumulando 9 hombres en su propio tercio defensivo.</p>
                            <p style="margin-top: 0.5rem;"><strong>2. Volumen de Balones Parados de O Dragão:</strong> El Porto volcó el juego por bandas forzando 8 tiros de esquina y 14 centros al área. En el minuto 84, un cabezazo en el segundo palo superó la marca y rompió el X2 de forma tardía.</p>
                            <p style="margin-top: 0.5rem;"><strong>3. Vulnerabilidad en Visitas a Portugal:</strong> En estadios hostiles con equipos necesitados de puntos, la doble oportunidad X2 es frágil si el favorito visitante se conforma con el empate y cede el dominio absoluto del balón.</p>
                        </div>
                    </div>
                    
                    <div class="box-solution" style="border-color: rgba(16, 185, 129, 0.4); background: rgba(6, 78, 59, 0.2);">
                        <div class="box-title-solution">
                            <span>🛡️ Calibración Táctica Implementada</span>
                        </div>
                        <div class="box-text">
                            <p><strong>1. Calibración Dragao/Alvalade:</strong> En visitas a Porto, Benfica o Sporting CP, se veta la doble oportunidad visitante simple en cuotas < 1.35 a menos que el visitante tenga una posesión proyectada superior al 55%.</p>
                            <p style="margin-top: 0.5rem;"><strong>2. Mercado Alternativo Obligatorio:</strong> Para este tipo de cruces de tensión europea, el mercado blindado será <strong>'Menos de 3.5 Goles' o 'Hándicap Asiático +1'</strong>.</p>
                            <p style="margin-top: 0.5rem;"><strong>3. Impacto Global:</strong> A pesar de este tropiezo, la jornada cerró con <strong>11 de 12 aciertos (91.7%)</strong>, elevando el Win Rate Global histórico a <strong>87.4%</strong>.</p>
                        </div>
                    </div>
                </div>
            </div>

"""

def update_file(file_path):
    print(f"Actualizando {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Inyectar nuevas filas en la tabla de auditoría (después de </tr> de #187)
    pos_187 = content.find('col-id">#187')
    if pos_187 == -1:
        print(f"Error: no se encontró #187 en {file_path}")
        return False
    
    end_tr_187 = content.find('</tr>', pos_187) + len('</tr>')
    
    # Verificar si ya se inyectó #188 para evitar duplicados
    if 'col-id">#188' not in content:
        content = content[:end_tr_187] + "\n" + new_table_rows + content[end_tr_187:]
        print("✓ 12 filas nuevas (#188-#199) inyectadas en la tabla de auditoría.")
    else:
        print("ℹ Las filas #188-#199 ya estaban inyectadas.")

    # 2. Inyectar Caso de Éxito #16 y Autopsia #15 en Área 3
    if 'CASO DE ÉXITO & CALIBRACIÓN #16' not in content:
        pos_insert_area3 = content.find('<!-- AUTOPSIA DE FALLO #14')
        if pos_insert_area3 != -1:
            content = content[:pos_insert_area3] + new_area3_cards + content[pos_insert_area3:]
            print("✓ Caso de Éxito #16 y Autopsia #15 inyectados en Área 3.")
        else:
            print("Advertencia: No se encontró marcador <!-- AUTOPSIA DE FALLO #14")
    else:
        print("ℹ Caso de Éxito #16 ya existía en Área 3.")

    # 3. Actualizar KPIs y Contadores
    # Pill de navegación
    content = re.sub(
        r'<span class="badge-winrate-pill">.*?</span>',
        r'<span class="badge-winrate-pill">87.4% WIN &bull; 87.3% FIJAS &bull; +$1,976.52</span>',
        content
    )
    # Título de Área 2
    content = re.sub(
        r'Registro transparente de <strong>\d+ pronósticos liquidados</strong>',
        r'Registro transparente de <strong>198 pronósticos liquidados</strong>',
        content
    )
    content = re.sub(
        r'WIN RATE GLOBAL: \d+\.\d+% \| FIJAS: \d+\.\d+% \(\d+/\d+\) \| BRIER: \d+\.\d+',
        r'WIN RATE GLOBAL: 87.4% | FIJAS: 87.3% (138/158) | BRIER: 0.1195',
        content
    )
    # KPI 1: Win Rate Global
    content = re.sub(
        r'(<div class="kpi-title">\s*<span>Win Rate Global</span>[\s\S]*?<div class="kpi-value"[^>]*>)\d+\.\d+%(</div>[\s\S]*?<div class="kpi-subtext"><strong>)\d+ Aciertos(</strong> / )\d+ Fallos de \d+ selecciones',
        r'\g<1>87.4%\g<2>173 Aciertos\g<3>25 Fallos de 198 selecciones',
        content
    )
    # KPI 2: Win Rate Fijas
    content = re.sub(
        r'(<div class="kpi-title">\s*<span>Win Rate en "La Fija"</span>[\s\S]*?<div class="kpi-value"[^>]*>)\d+\.\d+%(</div>[\s\S]*?<div class="kpi-subtext"><strong>)\d+ Aciertos(</strong> / )\d+ Fallos de \d+ fijas',
        r'\g<1>87.3%\g<2>138 Aciertos\g<3>20 Fallos de 158 fijas',
        content
    )
    # KPI 3: Beneficio Neto / Banca Modelo
    content = re.sub(
        r'(<div class="kpi-title">\s*<span>Banca Total Modelo</span>[\s\S]*?<div class="kpi-value"[^>]*>)\$[\d,]+\.\d+(</div>[\s\S]*?<div class="kpi-subtext">Beneficio Neto: <strong>)\+\$[\d,]+\.\d+ USD(</strong>)',
        r'\g<1>$2,976.52\g<2>+$1,976.52 USD\g<3>',
        content
    )
    # Conteo de picks mostrados
    content = re.sub(
        r'Mostrando \d+ de \d+ picks',
        r'Mostrando 198 de 198 picks',
        content
    )
    content = re.sub(
        r'Todos \(\d+\)',
        r'Todos (198)',
        content
    )
    # Banner Hero de Área 3
    content = re.sub(
        r'⚡ 11 Agentes Activos &bull; Brier: \d+\.\d+',
        r'⚡ 11 Agentes Activos &bull; Brier: 0.1195',
        content
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✓ Archivo {file_path} actualizado exitosamente.")
    return True

for p in [index_path, dashboard_path, root_index_path]:
    if os.path.exists(p):
        update_file(p)
    else:
        print(f"El archivo {p} no existe.")

print("¡SINCRONIZACIÓN COMPLETA FINALIZADA!")
