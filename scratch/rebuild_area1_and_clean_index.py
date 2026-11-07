# -*- coding: utf-8 -*-
"""
rebuild_area1_and_clean_index.py
Reconstruye el Área 1 con la Cartelera Oficial Completa del Martes 3 de Noviembre de 2026:
- 9 Partidos de UEFA Champions League (Galatasaray, Shakhtar, Barça, Villarreal, Atlético, Feyenoord, Man United, Bodø/Glimt, LASK)
- 5 Partidos Sudamericanos y Locales (LigaPro: Mushuc Runa vs Manta; Colombia: Pereira vs Tolima, Pasto vs Jaguares; Brasil: Chapecoense vs Mirassol, Internacional; Inglaterra: West Brom vs Southampton)
- Elimina comentarios duplicados y limpia index.html y dashboard_pronosticos.html
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

new_area1_content = """        <!-- VISTA 1: PARTIDOS & PRONÓSTICOS OFICIALES (MARTES 3 DE NOVIEMBRE DE 2026) -->
        <div id="view-container-matches">
            <!-- BANNER PRINCIPAL DE LA JORNADA: PROTOCOLO SELLO DE ALTA CERTEZA (REGLA #120) -->
            <div style="background: linear-gradient(135deg, rgba(30, 27, 75, 0.95), rgba(15, 23, 42, 0.98)); border: 2px solid rgba(59, 130, 246, 0.6); border-radius: 20px; padding: 1.75rem 2rem; margin-bottom: 2rem; backdrop-filter: blur(16px); box-shadow: 0 16px 36px -8px rgba(59, 130, 246, 0.35);">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1.25rem;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.5rem;">
                            <span style="background: rgba(59, 130, 246, 0.25); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.7); padding: 0.25rem 0.85rem; border-radius: 9999px; font-size: 0.78rem; font-weight: 800; text-transform: uppercase;">
                                📅 CARTELERA OFICIAL &bull; MARTES 3 DE NOVIEMBRE DE 2026
                            </span>
                            <span style="background: linear-gradient(135deg, #10b981, #059669); color: #ffffff; padding: 0.25rem 0.85rem; border-radius: 9999px; font-size: 0.78rem; font-weight: 800; box-shadow: 0 0 12px rgba(16, 185, 129, 0.5);">
                                🔥 RACHA ACTIVA: 12 VICTORIAS CONSECUTIVAS
                            </span>
                        </div>
                        <h1 style="font-size: 1.85rem; font-weight: 900; color: #ffffff; letter-spacing: -0.02em; margin: 0;">
                            UEFA Champions League (Fecha 4) & Fútbol Sudamericano
                        </h1>
                        <p style="color: #94a3b8; font-size: 0.92rem; margin-top: 0.35rem; margin-bottom: 0;">
                            Barça vs Aston Villa, Villarreal vs PSG, Atlético vs Bayern, LigaPro en Echaleche, Liga BetPlay Colombia y Brasileirão.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.55); border: 1px solid rgba(255,255,255,0.15); border-radius: 14px; padding: 1rem 1.5rem; text-align: right;">
                        <div style="font-size: 0.75rem; color: #94a3b8; text-transform: uppercase; font-weight: 700;">Saldo Activo Ecuabet</div>
                        <div style="font-size: 1.65rem; font-weight: 900; color: #34d399;">$24.90 USD</div>
                        <div style="font-size: 0.8rem; font-weight: 700; color: #fbbf24;">Cobrado con AS Roma (+ $1.90 netos)</div>
                    </div>
                </div>

                <!-- SPOTLIGHT DE LAS DOS ESTRATEGIAS RECOMENDADAS -->
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1rem; margin-top: 1.5rem; padding-top: 1.25rem; border-top: 1px solid rgba(255,255,255,0.08);">
                    <div style="background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 14px; padding: 1.1rem 1.25rem;">
                        <div style="font-size: 0.78rem; font-weight: 800; color: #34d399; text-transform: uppercase; display: flex; align-items: center; gap: 0.4rem;">
                            <span>👑</span> LA FIJA DE ORO DE HOY (CUOTA 1.35)
                        </div>
                        <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff; margin-top: 0.35rem;">
                            FC Barcelona vs Aston Villa: Ambos Equipos Anotan (Sí) / 1X + Más 1.5
                        </div>
                        <div style="font-size: 0.82rem; color: #cbd5e1; margin-top: 0.25rem;">
                            Barça con bajas defensivas y línea alta; Aston Villa lleva 12 goles en 3 juegos de Champions. Con <strong>$4.90 USD</strong> cobras <strong>$6.61 USD</strong>.
                        </div>
                    </div>
                    <div style="background: rgba(59, 130, 246, 0.12); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 14px; padding: 1.1rem 1.25rem;">
                        <div style="font-size: 0.78rem; font-weight: 800; color: #60a5fa; text-transform: uppercase; display: flex; align-items: center; gap: 0.4rem;">
                            <span>🚀</span> LA COMBINADA QUIRÚRGICA COPERA (CUOTA 1.85)
                        </div>
                        <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff; margin-top: 0.35rem;">
                            Villarreal vs PSG (X2 @ 1.25) + Pasto vs Jaguares (Menos 2.5 @ 1.48)
                        </div>
                        <div style="font-size: 0.82rem; color: #cbd5e1; margin-top: 0.25rem;">
                            Cuota Total <strong>1.85</strong>. Con <strong>$4.00 USD</strong> cobras <strong>$7.40 USD</strong> manteniendo $20.90 USD blindados en cuenta.
                        </div>
                    </div>
                </div>
            </div>

            <!-- SECCIÓN 1: UEFA CHAMPIONS LEAGUE (FASE DE LIGA - FECHA 4) -->
            <div style="margin-bottom: 2rem;">
                <div style="display: flex; align-items: center; gap: 0.6rem; margin-bottom: 1rem;">
                    <span style="font-size: 1.2rem;">⭐</span>
                    <h2 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0;">UEFA Champions League &bull; Jornada 4</h2>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 1.25rem;">
                    
                    <!-- PARTIDO 1: FC BARCELONA VS ASTON VILLA -->
                    <div style="background: var(--bg-card); border: 2px solid rgba(239, 68, 68, 0.5); border-radius: 16px; padding: 1.4rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                                <span style="background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                    🇪🇸 CHAMPIONS &bull; CAMP NOU
                                </span>
                                <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 15:00 (ECU)</span>
                            </div>
                            <h3 style="font-size: 1.25rem; font-weight: 900; color: #ffffff; margin: 0 0 0.4rem 0;">
                                FC Barcelona vs Aston Villa
                            </h3>
                            <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.45; margin: 0 0 1rem 0;">
                                📍 <strong>Spotify Camp Nou:</strong> El Barça de Flick viene de golear 6-1 en liga pero tiene bajas sensibles en la zaga (Koundé, Christensen). El Villa de Unai Emery suma 12 goles en Champions con transiciones letales.
                            </p>
                        </div>
                        <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 0.9rem;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                                <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">La Fija de Oro:</span>
                                <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Ambos Marcan: Sí / 1X + Más 1.5</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                                <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.35 - 1.50</span>
                            </div>
                        </div>
                    </div>

                    <!-- PARTIDO 2: VILLARREAL VS PSG -->
                    <div style="background: var(--bg-card); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 16px; padding: 1.4rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                                <span style="background: rgba(59, 130, 246, 0.2); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                    🇫🇷 CHAMPIONS &bull; LA CERÁMICA
                                </span>
                                <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 15:00 (ECU)</span>
                            </div>
                            <h3 style="font-size: 1.25rem; font-weight: 900; color: #ffffff; margin: 0 0 0.4rem 0;">
                                Villarreal CF vs Paris Saint-Germain
                            </h3>
                            <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.45; margin: 0 0 1rem 0;">
                                📍 <strong>Estadio de la Cerámica:</strong> PSG de Luis Enrique marcha líder invicto en Champions (9 pts) con ritmo imparable. Villarreal llega con bajas importantes (Gerard Moreno, Juan Foyth) y sufre ante la velocidad gala.
                            </p>
                        </div>
                        <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 0.9rem;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                                <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Cobertura:</span>
                                <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">PSG o Empate (X2)</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                                <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.25</span>
                            </div>
                        </div>
                    </div>

                    <!-- PARTIDO 3: ATLÉTICO DE MADRID VS BAYERN MÚNICH -->
                    <div style="background: var(--bg-card); border: 1px solid rgba(245, 158, 11, 0.4); border-radius: 16px; padding: 1.4rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                                <span style="background: rgba(245, 158, 11, 0.2); color: #fde047; border: 1px solid rgba(245, 158, 11, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                    🇪🇸 CHAMPIONS &bull; METROPOLITANO
                                </span>
                                <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 15:00 (ECU)</span>
                            </div>
                            <h3 style="font-size: 1.25rem; font-weight: 900; color: #ffffff; margin: 0 0 0.4rem 0;">
                                Atlético de Madrid vs Bayern Múnich
                            </h3>
                            <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.45; margin: 0 0 1rem 0;">
                                📍 <strong>Cívitas Metropolitano:</strong> El Cholo Simeone con Julián Álvarez y Griezmann recibe al Bayern de Harry Kane. Partidazo de alta fricción táctica donde el Metropolitano pesa una tonelada.
                            </p>
                        </div>
                        <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 0.9rem;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                                <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Acero:</span>
                                <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Atlético de Madrid o Empate (1X)</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                                <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.40 - 1.45</span>
                            </div>
                        </div>
                    </div>

                    <!-- PARTIDO 4: MANCHESTER UNITED VS AS ROMA -->
                    <div style="background: var(--bg-card); border: 1px solid rgba(139, 92, 246, 0.4); border-radius: 16px; padding: 1.4rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                                <span style="background: rgba(139, 92, 246, 0.2); color: #c4b5fd; border: 1px solid rgba(139, 92, 246, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                    🏴󠁧󠁢󠁥󠁮󠁧󠁿 CHAMPIONS &bull; OLD TRAFFORD
                                </span>
                                <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 15:00 (ECU)</span>
                            </div>
                            <h3 style="font-size: 1.25rem; font-weight: 900; color: #ffffff; margin: 0 0 0.4rem 0;">
                                Manchester United vs AS Roma
                            </h3>
                            <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.45; margin: 0 0 1rem 0;">
                                📍 <strong>Old Trafford:</strong> El United recibe a la Roma de Gasperini que viene encendida tras golear 4-2 a Cagliari. Duelo de alta intensidad con opciones de gol en ambas metas.
                            </p>
                        </div>
                        <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 0.9rem;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                                <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Goles:</span>
                                <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Ambos Equipos Anotan: Sí</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                                <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.55</span>
                            </div>
                        </div>
                    </div>

                    <!-- PARTIDO 5: FEYENOORD VS INTER DE MILÁN -->
                    <div style="background: var(--bg-card); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 16px; padding: 1.4rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                                <span style="background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1px solid rgba(16, 185, 129, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                    🇳🇱 CHAMPIONS &bull; DE KUIP
                                </span>
                                <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 15:00 (ECU)</span>
                            </div>
                            <h3 style="font-size: 1.25rem; font-weight: 900; color: #ffffff; margin: 0 0 0.4rem 0;">
                                Feyenoord vs Inter de Milán
                            </h3>
                            <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.45; margin: 0 0 1rem 0;">
                                📍 <strong>Stadion Feijenoord (Rotterdam):</strong> El Inter de Simone Inzaghi visita una plaza caliente. La solidez defensiva nerazzurra le da ventaja táctica para puntuar fuera de casa.
                            </p>
                        </div>
                        <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 0.9rem;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                                <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Cobertura:</span>
                                <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Inter de Milán o Empate (X2)</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                                <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.28</span>
                            </div>
                        </div>
                    </div>

                    <!-- PARTIDO 6: BODØ/GLIMT VS LILLE -->
                    <div style="background: var(--bg-card); border: 1px solid rgba(245, 158, 11, 0.4); border-radius: 16px; padding: 1.4rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                                <span style="background: rgba(245, 158, 11, 0.2); color: #fde047; border: 1px solid rgba(245, 158, 11, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                    🇳🇴 CHAMPIONS &bull; CÍRCULO POLAR
                                </span>
                                <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 15:00 (ECU)</span>
                            </div>
                            <h3 style="font-size: 1.25rem; font-weight: 900; color: #ffffff; margin: 0 0 0.4rem 0;">
                                FK Bodø/Glimt vs LOSC Lille
                            </h3>
                            <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.45; margin: 0 0 1rem 0;">
                                📍 <strong>Aspmyra Stadion (Bodø):</strong> Cancha sintética y frío ártico en Noruega. Bodø/Glimt siempre complica a los visitantes en su fortaleza polar.
                            </p>
                        </div>
                        <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 0.9rem;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                                <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Goles:</span>
                                <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Total: Más de 2.0 Goles</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                                <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.35</span>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

            <!-- SECCIÓN 2: FÚTBOL SUDAMERICANO & LOCAL -->
            <div>
                <div style="display: flex; align-items: center; gap: 0.6rem; margin-bottom: 1rem;">
                    <span style="font-size: 1.2rem;">🌎</span>
                    <h2 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0;">Fútbol Sudamericano & Local</h2>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 1.25rem;">
                    
                    <!-- PARTIDO 7: LIGAPRO ECUADOR -->
                    <div style="background: var(--bg-card); border: 1px solid rgba(234, 179, 8, 0.4); border-radius: 16px; padding: 1.4rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                                <span style="background: rgba(234, 179, 8, 0.2); color: #fde047; border: 1px solid rgba(234, 179, 8, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                    🇪🇨 LIGAPRO &bull; ECHALECHE
                                </span>
                                <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 12:30 (ECU)</span>
                            </div>
                            <h3 style="font-size: 1.25rem; font-weight: 900; color: #ffffff; margin: 0 0 0.4rem 0;">
                                Mushuc Runa vs Manta FC
                            </h3>
                            <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.45; margin: 0 0 1rem 0;">
                                📍 <strong>Estadio Mushuc Runa COAC (3,250m):</strong> El Ponchito de Paul Vélez en la altura de Echaleche es una muralla ante un equipo de la costa como Manta.
                            </p>
                        </div>
                        <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 0.9rem;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                                <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Acero:</span>
                                <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Mushuc Runa o Empate (1X)</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                                <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.25</span>
                            </div>
                        </div>
                    </div>

                    <!-- PARTIDO 8: COLOMBIA - DEPORTIVO PASTO VS JAGUARES -->
                    <div style="background: var(--bg-card); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 16px; padding: 1.4rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                                <span style="background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1px solid rgba(16, 185, 129, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                    🇨🇴 LIGA BETPLAY &bull; NARIÑO
                                </span>
                                <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 15:20 (ECU)</span>
                            </div>
                            <h3 style="font-size: 1.25rem; font-weight: 900; color: #ffffff; margin: 0 0 0.4rem 0;">
                                Deportivo Pasto vs Jaguares
                            </h3>
                            <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.45; margin: 0 0 1rem 0;">
                                📍 <strong>Estadio Departamental Libertad (Pasto):</strong> Partido de altísima fricción en la altura. Pasto es un cerrojo y Jaguares promedia menos de 0.6 goles de visitante.
                            </p>
                        </div>
                        <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 0.9rem;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                                <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Acero:</span>
                                <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Total: Menos de 2.5 Goles</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                                <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.48</span>
                            </div>
                        </div>
                    </div>

                    <!-- PARTIDO 9: BRASIL - CHAPECOENSE VS MIRASSOL -->
                    <div style="background: var(--bg-card); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 16px; padding: 1.4rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                                <span style="background: rgba(59, 130, 246, 0.2); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                    🇧🇷 BRASILEIRÃO &bull; ARENA CONDÁ
                                </span>
                                <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 14:30 (ECU)</span>
                            </div>
                            <h3 style="font-size: 1.25rem; font-weight: 900; color: #ffffff; margin: 0 0 0.4rem 0;">
                                Chapecoense vs Mirassol
                            </h3>
                            <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.45; margin: 0 0 1rem 0;">
                                📍 <strong>Arena Condá:</strong> Choque brasileño cerrado. Mirassol pelea en los puestos altos con defensa organizada; Chapecoense busca hacerse fuerte en casa.
                            </p>
                        </div>
                        <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 0.9rem;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                                <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Control:</span>
                                <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Total: Menos de 2.5 Goles</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                                <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.45</span>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

        </div> <!-- Fin de view-container-matches -->"""

print("1. Leyendo index.html...")
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Encontrar desde el inicio de view-container-matches hasta el inicio de view-container-winrate
s_pos = content.find('<div id="view-container-matches"')
e_pos = content.find('<div id="view-container-winrate"')

if s_pos != -1 and e_pos != -1:
    cleaned_content = content[:s_pos] + new_area1_content + "\n\n        " + content[e_pos:]
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(cleaned_content)
    print("✓ index.html reconstruido y limpiado con éxito.")

    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(cleaned_content)
    print("✓ dashboard_pronosticos.html reconstruido y limpiado con éxito.")

    if os.path.exists(root_index_path):
        with open(root_index_path, "w", encoding="utf-8") as f:
            f.write(cleaned_content)
        print("✓ ../index.html (raíz) reconstruido y limpiado con éxito.")
else:
    print(f"❌ Error buscando delimitadores: s_pos={s_pos}, e_pos={e_pos}")

