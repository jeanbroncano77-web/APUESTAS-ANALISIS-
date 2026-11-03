# -*- coding: utf-8 -*-
"""
update_area1_champions_matchday4.py
Actualiza el Área 1 con la Cartelera Oficial de UEFA Champions League (Jornada 4)
Martes 3 y Miércoles 4 de Noviembre de 2026.
"""

import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")
dashboard_path = os.path.join(base_dir, "dashboard_pronosticos.html")
root_index_path = os.path.join(base_dir, "..", "index.html")

champions_html = """        <!-- VISTA 1: PARTIDOS Y PRONÓSTICOS (CHAMPIONS LEAGUE JORNADA 4 - NOVIEMBRE 2026) -->
        <div id="view-container-matches">
            <!-- BANNER PRINCIPAL: PROTOCOLO SELLO DE ALTA CERTEZA (REGLA #120) -->
            <div style="background: linear-gradient(135deg, rgba(30, 27, 75, 0.95), rgba(15, 23, 42, 0.98)); border: 2px solid rgba(59, 130, 246, 0.6); border-radius: 20px; padding: 1.75rem 2rem; margin-bottom: 2rem; backdrop-filter: blur(16px); box-shadow: 0 16px 36px -8px rgba(59, 130, 246, 0.35);">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1.25rem;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.5rem;">
                            <span style="background: rgba(59, 130, 246, 0.25); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.7); padding: 0.25rem 0.85rem; border-radius: 9999px; font-size: 0.78rem; font-weight: 800; text-transform: uppercase;">
                                🌟 UEFA CHAMPIONS LEAGUE &bull; FASE DE LIGA (FECHA 4)
                            </span>
                            <span style="background: linear-gradient(135deg, #10b981, #059669); color: #ffffff; padding: 0.25rem 0.85rem; border-radius: 9999px; font-size: 0.78rem; font-weight: 800; box-shadow: 0 0 12px rgba(16, 185, 129, 0.5);">
                                🔥 RACHA ACTIVA: 12 VICTORIAS CONSECUTIVAS
                            </span>
                        </div>
                        <h1 style="font-size: 1.8rem; font-weight: 900; color: #ffffff; letter-spacing: -0.02em; margin: 0;">
                            Cartelera Estelar Champions League: Noches Mágicas de Europa
                        </h1>
                        <p style="color: #94a3b8; font-size: 0.92rem; margin-top: 0.35rem; margin-bottom: 0;">
                            Barça vs Aston Villa, Villarreal vs PSG, Atlético vs Bayern, AEK vs Real Madrid y Leipzig vs Manchester City.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.15); border-radius: 14px; padding: 1rem 1.5rem; text-align: right;">
                        <div style="font-size: 0.75rem; color: #94a3b8; text-transform: uppercase; font-weight: 700;">Saldo Activo Ecuabet</div>
                        <div style="font-size: 1.6rem; font-weight: 900; color: #34d399;">$24.90 USD</div>
                        <div style="font-size: 0.8rem; font-weight: 700; color: #fbbf24;">Cobrado con AS Roma (+ $1.90 netos)</div>
                    </div>
                </div>

                <!-- SPOTLIGHT DE LAS DOS ESTRATEGIAS RECOMENDADAS -->
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1rem; margin-top: 1.5rem; padding-top: 1.25rem; border-top: 1px solid rgba(255,255,255,0.08);">
                    <div style="background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 14px; padding: 1.1rem 1.25rem;">
                        <div style="font-size: 0.78rem; font-weight: 800; color: #34d399; text-transform: uppercase; display: flex; align-items: center; gap: 0.4rem;">
                            <span>👑</span> LA FIJA DE ORO DE CHAMPIONS (CUOTA 1.35)
                        </div>
                        <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff; margin-top: 0.35rem;">
                            FC Barcelona o Empate (1X) + Más de 1.5 Goles @ 1.35
                        </div>
                        <div style="font-size: 0.82rem; color: #cbd5e1; margin-top: 0.25rem;">
                            El Barça de Flick en Montjuïc ante Aston Villa. Con <strong>$4.90 USD</strong> cobras <strong>$6.61 USD</strong> (saldo sube a $26.61 USD con 88% prob).
                        </div>
                    </div>
                    <div style="background: rgba(59, 130, 246, 0.12); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 14px; padding: 1.1rem 1.25rem;">
                        <div style="font-size: 0.78rem; font-weight: 800; color: #60a5fa; text-transform: uppercase; display: flex; align-items: center; gap: 0.4rem;">
                            <span>🚀</span> LA COMBINADA QUIRÚRGICA COPERA (CUOTA 1.85)
                        </div>
                        <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff; margin-top: 0.35rem;">
                            Barça 1X (1.18) + PSG o Empate X2 (1.22) + Real Madrid Gana en Grecia (1.28)
                        </div>
                        <div style="font-size: 0.82rem; color: #cbd5e1; margin-top: 0.25rem;">
                            Cuota Total <strong>1.85</strong>. Con <strong>$4.00 USD</strong> cobras <strong>$7.40 USD</strong> manteniendo $20.90 USD blindados en cuenta.
                        </div>
                    </div>
                </div>
            </div>

            <!-- GRID CON LAS 6 TARJETAS ESTELARES DE CHAMPIONS -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 1.5rem; margin-bottom: 3rem;">

                <!-- PARTIDO 1: BARCELONA VS ASTON VILLA -->
                <div style="background: var(--bg-card); border: 2px solid rgba(239, 68, 68, 0.4); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇪🇸 UEFA CHAMPIONS &bull; MONTJUÏC
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 15:00 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            FC Barcelona vs Aston Villa
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Estadi Olímpic Lluís Companys:</strong> El conjunto blaugrana de Hansi Flick busca asegurar el pase directo a octavos. Lamine Yamal y Raphinha llegan en estado de gracia ante los Villanos de Unai Emery.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">La Fija de Oro:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Barcelona 1X + Más 1.5</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.35</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 2: VILLARREAL VS PSG -->
                <div style="background: var(--bg-card); border: 1px solid rgba(59, 130, 246, 0.35); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(59, 130, 246, 0.2); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇫🇷 UEFA CHAMPIONS &bull; LA CERÁMICA
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 15:00 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            Villarreal CF vs Paris Saint-Germain
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Estadio de la Cerámica:</strong> Duelo hispano-francés de alto calibre. El PSG de Luis Enrique es líder en Francia y viene encendido, pero Villarreal en casa siempre compite con orden.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
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
                <div style="background: var(--bg-card); border: 1px solid rgba(245, 158, 11, 0.35); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(245, 158, 11, 0.2); color: #fde047; border: 1px solid rgba(245, 158, 11, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇪🇸 UEFA CHAMPIONS &bull; METROPOLITANO
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 15:00 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            Atlético de Madrid vs Bayern Múnich
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Cívitas Metropolitano:</strong> Choque colosal entre el bloque de Diego Simeone y la maquinaria bávara de Vincent Kompany. Partidazo de altísima fricción táctica.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Goles:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Ambos Marcan / Más 2.0</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.48 - 1.55</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 4: AEK ATENAS VS REAL MADRID -->
                <div style="background: var(--bg-card); border: 2px solid rgba(245, 158, 11, 0.4); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(245, 158, 11, 0.2); color: #fde047; border: 1px solid rgba(245, 158, 11, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                👑 UEFA CHAMPIONS &bull; ATENAS
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ Mié 15:00 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            AEK Atenas vs Real Madrid
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>OPAP Arena (Atenas):</strong> El rey de Europa viaja a Grecia con Kylian Mbappé y Jude Bellingham tras golear 0-3 al Racing. La jerarquía blanca debe imponerse para sellar el boleto.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Acero:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Real Madrid Gana el Partido (2)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.28</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 5: RB LEIPZIG VS MANCHESTER CITY -->
                <div style="background: var(--bg-card); border: 1px solid rgba(16, 185, 129, 0.35); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1px solid rgba(16, 185, 129, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇩🇪 UEFA CHAMPIONS &bull; RED BULL ARENA
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ Mié 15:00 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            RB Leipzig vs Manchester City
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Red Bull Arena:</strong> Los Ciudadanos de Guardiola quieren recuperarse tras tropezar en Premier ante Brighton. Erling Haaland visita Alemania donde siempre tiene hambre de gol.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Cobertura:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Man City o Empate (X2)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.22</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 6: FENERBAHÇE VS LIVERPOOL -->
                <div style="background: var(--bg-card); border: 1px solid rgba(239, 68, 68, 0.35); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇹🇷 UEFA CHAMPIONS &bull; ESTAMBUL
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ Mié 12:45 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            Fenerbahçe vs Liverpool
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Estadio Şükrü Saracoğlu:</strong> Visita de fuego para el Liverpool de Arne Slot en el infierno de Estambul. Choque de alta intensidad donde Liverpool buscará imponer su pegada ofensiva.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Cobertura:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Liverpool o Empate (X2)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.22</span>
                        </div>
                    </div>
                </div>

            </div>
        </div> <!-- Fin de view-container-matches -->"""

print("Reemplazando view-container-matches en index.html...")
with open(index_path, "r", encoding="utf-8") as f:
    c = f.read()

start_tag = '<div id="view-container-matches">'
end_tag = '</div> <!-- Fin de view-container-matches -->'

s_pos = c.find(start_tag)
e_pos = c.find(end_tag)

if s_pos != -1 and e_pos != -1:
    e_pos += len(end_tag)
    c_new = c[:s_pos] + champions_html + c[e_pos:]
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(c_new)
    print("✓ index.html actualizado con la Cartelera de Champions.")

    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(c_new)
    print("✓ dashboard_pronosticos.html actualizado.")

    if os.path.exists(root_index_path):
        with open(root_index_path, "w", encoding="utf-8") as f:
            f.write(c_new)
        print("✓ ../index.html (raíz) actualizado.")
else:
    print(f"❌ Error buscando etiquetas: s_pos={s_pos}, e_pos={e_pos}")

