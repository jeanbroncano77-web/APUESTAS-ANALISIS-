# -*- coding: utf-8 -*-
"""
inject_area1_monday_26.py
Reemplaza el contenido de view-container-matches en index.html y dashboard_pronosticos.html
con la Cartelera Oficial de 7 Partidos para el Lunes 26 de Octubre de 2026.
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

new_area1 = """        <!-- VISTA 1: PARTIDOS Y PRONÓSTICOS (LUNES 26 DE OCTUBRE DE 2026) -->
        <div id="view-container-matches">
            <!-- BANNER PRINCIPAL DE RECONSTRUCCIÓN -->
            <div style="background: linear-gradient(135deg, rgba(30, 27, 75, 0.85), rgba(15, 23, 42, 0.95)); border: 2px solid rgba(245, 158, 11, 0.5); border-radius: 20px; padding: 1.75rem 2rem; margin-bottom: 2rem; backdrop-filter: blur(16px); box-shadow: 0 16px 36px -8px rgba(245, 158, 11, 0.25);">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1.25rem;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.5rem;">
                            <span style="background: rgba(245, 158, 11, 0.25); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.6); padding: 0.25rem 0.85rem; border-radius: 9999px; font-size: 0.78rem; font-weight: 800; text-transform: uppercase;">
                                📅 CARTELERA OFICIAL &bull; LUNES 26 DE OCTUBRE DE 2026
                            </span>
                            <span style="background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.78rem; font-weight: 700;">
                                🛡️ REGLA #118 ACTIVA
                            </span>
                        </div>
                        <h1 style="font-size: 1.75rem; font-weight: 900; color: #ffffff; letter-spacing: -0.02em; margin: 0;">
                            Plan de Reconstrucción de Banca: 7 Encuentros Quirúrgicos
                        </h1>
                        <p style="color: #94a3b8; font-size: 0.92rem; margin-top: 0.35rem; margin-bottom: 0;">
                            Clásico de Turquía en RAMS Park, LigaPro en Ambato, PSG vs Lyon, Sevilla, Benfica en Azores, Maracaná y El Tráfico de Los Ángeles.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.45); border: 1px solid rgba(255,255,255,0.12); border-radius: 14px; padding: 1rem 1.5rem; text-align: right;">
                        <div style="font-size: 0.75rem; color: #94a3b8; text-transform: uppercase; font-weight: 700;">Saldo Activo Ecuabet</div>
                        <div style="font-size: 1.6rem; font-weight: 900; color: #fbbf24;">$23.00 USD</div>
                        <div style="font-size: 0.8rem; font-weight: 700; color: #34d399;">Stake Quirúrgico: $3.00 - $5.00 USD</div>
                    </div>
                </div>

                <!-- SPOTLIGHT DE LAS DOS ESTRATEGIAS RECOMENDADAS -->
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1rem; margin-top: 1.5rem; padding-top: 1.25rem; border-top: 1px solid rgba(255,255,255,0.08);">
                    <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.35); border-radius: 12px; padding: 1rem 1.25rem;">
                        <div style="font-size: 0.78rem; font-weight: 800; color: #34d399; text-transform: uppercase;">
                            🥇 OPCIÓN 1: LA FIJA SOLITARIA (CONSERVADORA)
                        </div>
                        <div style="font-size: 1.05rem; font-weight: 800; color: #ffffff; margin-top: 0.25rem;">
                            Galatasaray o Empate (1X) @ 1.30
                        </div>
                        <div style="font-size: 0.8rem; color: #cbd5e1; margin-top: 0.2rem;">
                            Osimhen en el infierno de Estambul. Con <strong>$5.00 USD</strong> cobras <strong>$6.50 USD</strong> (+$1.50 neto con 88% prob).
                        </div>
                    </div>
                    <div style="background: rgba(99, 102, 241, 0.12); border: 1px solid rgba(99, 102, 241, 0.35); border-radius: 12px; padding: 1rem 1.25rem;">
                        <div style="font-size: 0.78rem; font-weight: 800; color: #818cf8; text-transform: uppercase;">
                            🥈 OPCIÓN 2: LA COMBINADA DE RECONSTRUCCIÓN (CUOTA 1.87)
                        </div>
                        <div style="font-size: 1.05rem; font-weight: 800; color: #ffffff; margin-top: 0.25rem;">
                            Galatasaray 1X (1.30) + PSG 1X (1.18) + Técnico vs Mushuc Menos 3.5 (1.22)
                        </div>
                        <div style="font-size: 0.8rem; color: #cbd5e1; margin-top: 0.2rem;">
                            Cuota Total <strong>1.87</strong>. Con <strong>$4.00 USD</strong> cobras <strong>$7.48 USD</strong> (llevas tu saldo a $26.48 USD).
                        </div>
                    </div>
                </div>
            </div>

            <!-- GRID CON LAS 7 TARJETAS DE PARTIDOS -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 1.5rem; margin-bottom: 3rem;">

                <!-- PARTIDO 1: LIGAPRO ECUADOR -->
                <div style="background: var(--bg-card); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(234, 179, 8, 0.2); color: #fde047; border: 1px solid rgba(234, 179, 8, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇪🇨 LIGAPRO &bull; AMBATO
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 15:30 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            Técnico Univ. vs Mushuc Runa
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Estadio Bellavista:</strong> Clásico tungurahuense. Técnico urge de puntos para salir del fondo pero promedia menos de 1 gol por juego; Mushuc Runa de Paul Vélez es ordenado y prioriza el cero. Encuentro cerrado de altura.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Acero:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Menos de 2.5 / 3.0 Goles</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.45 - 1.55</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 2: SÜPER LIG TURQUÍA -->
                <div style="background: var(--bg-card); border: 2px solid rgba(239, 68, 68, 0.4); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇹🇷 SÜPER LIG &bull; CLÁSICO
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 13:30 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            Galatasaray vs Fenerbahçe
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>RAMS Park (Estambul):</strong> El Clásico Intercontinental. Galatasaray es líder invicto (19 pts) con Victor Osimhen y Mauro Icardi. Fenerbahçe llega 3º (16 pts). El RAMS Park es una caldera donde Galatasaray casi no cede puntos.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">La Fija de Oro:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Galatasaray o Empate (1X)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.30</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 3: LIGUE 1 FRANCIA -->
                <div style="background: var(--bg-card); border: 1px solid rgba(59, 130, 246, 0.35); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(59, 130, 246, 0.2); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇫🇷 LIGUE 1 &bull; CUMBRE
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 14:30 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            Paris Saint-Germain vs Lyon
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Parc des Princes:</strong> PSG de Luis Enrique suma 7 triunfos consecutivos (metió 4 goles al City y al Barça en Champions). Lyon llega arriba pero golpeado tras caer 0-3 con Hoffenheim. En París, el PSG tiene el control.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija Combinable:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">PSG o Empate (1X)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.18 - 1.25</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 4: LALIGA ESPAÑA -->
                <div style="background: var(--bg-card); border: 1px solid rgba(16, 185, 129, 0.35); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1px solid rgba(16, 185, 129, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇪🇸 LALIGA &bull; NERVIÓN
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 15:00 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            Sevilla FC vs CA Osasuna
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Sánchez-Pizjuán:</strong> Sevilla (6º, 14 pts) busca puestos europeos pero ha recibido goles en sus últimos partidos. Osasuna (12º) llega motivado con Ante Budimir en racha de gol. Duelo táctico con pocas concesiones.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Acero:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Menos de 3.5 Goles Totales</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.25</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 5: PRIMEIRA LIGA PORTUGAL -->
                <div style="background: var(--bg-card); border: 1px solid rgba(139, 92, 246, 0.35); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(139, 92, 246, 0.2); color: #c4b5fd; border: 1px solid rgba(139, 92, 246, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇵🇹 LIGA PORTUGAL &bull; AZORES
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 13:45 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            CD Santa Clara vs SL Benfica
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Estádio de São Miguel (Ponta Delgada):</strong> Salida de altísima complejidad para las Águilas. Santa Clara se mantiene invicto y con cerrojo de local. Benfica tiene la jerarquía pero rara vez golea en las islas.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Protección:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Benfica o Empate (X2)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.20 - 1.25</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 6: BRASILEIRÃO SÉRIE A -->
                <div style="background: var(--bg-card); border: 1px solid rgba(239, 68, 68, 0.35); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇧🇷 BRASILEIRÃO &bull; MARACANÁ
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 18:00 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            Flamengo vs Atlético Mineiro
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Estadio Maracaná:</strong> El Mengão (2º con 67 pts) necesita ganar sí o sí para pelear el liderato con Palmeiras tras su eliminación en Libertadores. Atlético Mineiro (6º) defiende puestos de copa pero sufre en Río.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Protección:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Flamengo o Empate (1X)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.20 - 1.24</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 7: MLS EL TRÁFICO -->
                <div style="background: var(--bg-card); border: 1px solid rgba(245, 158, 11, 0.35); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(245, 158, 11, 0.2); color: #fde047; border: 1px solid rgba(245, 158, 11, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇺🇸 MLS &bull; EL TRÁFICO
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 20:00 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            LAFC vs LA Galaxy
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>BMO Stadium (Los Ángeles):</strong> El derbi más espectacular de Norteamérica. Denis Bouanga y LAFC contra Joseph Paintsil del Galaxy. Espectáculo garantizado con transiciones vertiginosas y goles en ambas metas.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Goles:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Ambos Marcan / Más 2.5</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.42 - 1.50</span>
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
    c_new = c[:s_pos] + new_area1 + c[e_pos:]
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(c_new)
    print("✓ index.html actualizado con la Cartelera del Lunes 26/10.")

    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(c_new)
    print("✓ dashboard_pronosticos.html actualizado.")

    if os.path.exists(root_index_path):
        with open(root_index_path, "w", encoding="utf-8") as f:
            f.write(c_new)
        print("✓ ../index.html (raíz) actualizado.")
else:
    print(f"❌ Error buscando etiquetas: s_pos={s_pos}, e_pos={e_pos}")
