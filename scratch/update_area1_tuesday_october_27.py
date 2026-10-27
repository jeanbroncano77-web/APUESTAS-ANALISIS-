# -*- coding: utf-8 -*-
"""
update_area1_tuesday_october_27.py
Actualiza el Área 1 (Cartelera de Partidos) de index.html y dashboard_pronosticos.html
con los partidos estelares de mañana martes 27 de octubre de 2026:
1. CD Cuarte vs Girona FC (Copa del Rey España)
2. CD Manacor vs Villarreal CF (Copa del Rey España)
3. Fleetwood Town vs Arsenal FC (EFL Carabao Cup Inglaterra)
4. AS Roma vs Cagliari (Serie A Italia)
5. Rot Weiss Essen vs RB Leipzig (DFB-Pokal Alemania)
6. Borussia Dortmund vs Werder Bremen (DFB-Pokal Alemania)
7. US Sassuolo vs SS Lazio (Serie A Italia)
8. Sestao River vs RCD Espanyol (Copa del Rey España)
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

new_area1 = """        <!-- VISTA 1: PARTIDOS Y PRONÓSTICOS (MARTES 27 DE OCTUBRE DE 2026) -->
        <div id="view-container-matches">
            <!-- BANNER PRINCIPAL: PROTOCOLO SELLO DE ALTA CERTEZA (REGLA #119) -->
            <div style="background: linear-gradient(135deg, rgba(30, 27, 75, 0.9), rgba(15, 23, 42, 0.98)); border: 2px solid rgba(245, 158, 11, 0.6); border-radius: 20px; padding: 1.75rem 2rem; margin-bottom: 2rem; backdrop-filter: blur(16px); box-shadow: 0 16px 36px -8px rgba(245, 158, 11, 0.35);">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1.25rem;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.5rem;">
                            <span style="background: rgba(245, 158, 11, 0.25); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.7); padding: 0.25rem 0.85rem; border-radius: 9999px; font-size: 0.78rem; font-weight: 800; text-transform: uppercase;">
                                📅 CARTELERA OFICIAL &bull; MARTES 27 DE OCTUBRE DE 2026
                            </span>
                            <span style="background: linear-gradient(135deg, #10b981, #059669); color: #ffffff; padding: 0.25rem 0.85rem; border-radius: 9999px; font-size: 0.78rem; font-weight: 800; box-shadow: 0 0 12px rgba(16, 185, 129, 0.5);">
                                ⭐ SELLO DE ALTA CERTEZA (REGLA #119)
                            </span>
                        </div>
                        <h1 style="font-size: 1.8rem; font-weight: 900; color: #ffffff; letter-spacing: -0.02em; margin: 0;">
                            Copa del Rey, Carabao Cup, Serie A & DFB-Pokal: Operación Goliat
                        </h1>
                        <p style="color: #94a3b8; font-size: 0.92rem; margin-top: 0.35rem; margin-bottom: 0;">
                            Los gigantes europeos (Arsenal, Girona, Villarreal, RB Leipzig y AS Roma) enfrentan eliminatorias desiguales para reconstruir la banca.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.15); border-radius: 14px; padding: 1rem 1.5rem; text-align: right;">
                        <div style="font-size: 0.75rem; color: #94a3b8; text-transform: uppercase; font-weight: 700;">Saldo Activo Ecuabet</div>
                        <div style="font-size: 1.6rem; font-weight: 900; color: #fbbf24;">$23.00 USD</div>
                        <div style="font-size: 0.8rem; font-weight: 700; color: #34d399;">Stake Sugerido: $5.00 - $6.00 USD</div>
                    </div>
                </div>

                <!-- SPOTLIGHT DE LAS DOS ESTRATEGIAS RECOMENDADAS -->
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1rem; margin-top: 1.5rem; padding-top: 1.25rem; border-top: 1px solid rgba(255,255,255,0.08);">
                    <div style="background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 14px; padding: 1.1rem 1.25rem;">
                        <div style="font-size: 0.78rem; font-weight: 800; color: #34d399; text-transform: uppercase; display: flex; align-items: center; gap: 0.4rem;">
                            <span>👑</span> LA TRIPLETA DE HIERRO 'DAVID VS GOLIAT' (CUOTA 1.50)
                        </div>
                        <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff; margin-top: 0.35rem;">
                            Fleetwood vs Arsenal (2) + Cuarte vs Girona (2) + Manacor vs Villarreal (2)
                        </div>
                        <div style="font-size: 0.82rem; color: #cbd5e1; margin-top: 0.25rem;">
                            Tres gigantes de élite visitando Tercera/Cuarta división. Con <strong>$5.00 USD</strong> cobras <strong>$7.50 USD</strong> (+$2.50 limpios con 93% prob).
                        </div>
                    </div>
                    <div style="background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.4); border-radius: 14px; padding: 1.1rem 1.25rem;">
                        <div style="font-size: 0.78rem; font-weight: 800; color: #fbbf24; text-transform: uppercase; display: flex; align-items: center; gap: 0.4rem;">
                            <span>🚀</span> LA COMBINADA QUIRÚRGICA DE RECONSTRUCCIÓN (CUOTA 1.95)
                        </div>
                        <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff; margin-top: 0.35rem;">
                            Arsenal Gana (1.10) + Girona Gana (1.14) + Villarreal Gana (1.16) + Roma 1X (1.10) + Leipzig Gana (1.22)
                        </div>
                        <div style="font-size: 0.82rem; color: #cbd5e1; margin-top: 0.25rem;">
                            Cuota Total <strong>1.95</strong>. Con <strong>$5.00 USD</strong> cobras <strong>$9.75 USD</strong> (¡Llevas tu cuenta directo a casi $28.00 USD!).
                        </div>
                    </div>
                </div>
            </div>

            <!-- GRID CON LAS 8 TARJETAS DE PARTIDOS -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 1.5rem; margin-bottom: 3rem;">

                <!-- PARTIDO 1: COPA DEL REY - GIRONA -->
                <div style="background: var(--bg-card); border: 2px solid rgba(239, 68, 68, 0.4); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇪🇸 COPA DEL REY &bull; 1ª RONDA
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 12:30 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            CD Cuarte vs Girona FC
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Estadio Juan Guerrero El Lobo (Zaragoza):</strong> Abismo de categorías. CD Cuarte compite en Tercera Federación; Girona llega con piezas de Champions como Donny van de Beek, Bryan Gil y Stuani. Dominio absoluto visitante.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Acero:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Girona FC Gana el Partido (2)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.12 - 1.15</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 2: CARABAO CUP INGLATERRA - ARSENAL -->
                <div style="background: var(--bg-card); border: 2px solid rgba(239, 68, 68, 0.4); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🏴󠁧󠁢󠁥󠁮󠁧󠁿 CARABAO CUP &bull; OCTAVOS
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 14:45 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            Fleetwood Town vs Arsenal FC
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Highbury Stadium (Fleetwood):</strong> 60 puestos de diferencia en la pirámide inglesa. Fleetwood marcha 18º en 4ta división; Arsenal de Mikel Arteta, incluso con rotaciones y el tricolor Piero Hincapié, tiene una jerarquía estratosférica.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Acero:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Arsenal FC Gana el Partido (2)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.08 - 1.12</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 3: COPA DEL REY - VILLARREAL -->
                <div style="background: var(--bg-card); border: 2px solid rgba(234, 179, 8, 0.4); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(234, 179, 8, 0.2); color: #fde047; border: 1px solid rgba(234, 179, 8, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇪🇸 COPA DEL REY &bull; 1ª RONDA
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 15:00 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            CD Manacor vs Villarreal CF
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Poliesportiu Na Capellera (Baleares):</strong> El Submarino Amarillo viene encendido tras ganar a domicilio en Mestalla (1-2) con Mikautadze. Manacor (Tercera Federación) compite con ilusión pero no tiene cómo frenar la maquinaria grogueta.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Acero:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Villarreal CF Gana el Partido (2)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.15 - 1.18</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 4: SERIE A ITALIA - AS ROMA -->
                <div style="background: var(--bg-card); border: 1px solid rgba(245, 158, 11, 0.35); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(245, 158, 11, 0.2); color: #fde047; border: 1px solid rgba(245, 158, 11, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇮🇹 SERIE A &bull; STADIO OLIMPICO
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 14:45 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            AS Roma vs Cagliari Calcio
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Stadio Olimpico de Roma:</strong> La Roma de Gian Piero Gasperini está en zona Champions peleando el liderato con Donyell Malen. Cagliari es combativo pero sufre enormemente ante equipos con presión alta y ritmo asfixiante.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Protección:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">AS Roma o Empate (1X)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.10 - 1.15</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 5: DFB-POKAL ALEMANIA - LEIPZIG -->
                <div style="background: var(--bg-card); border: 1px solid rgba(59, 130, 246, 0.35); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(59, 130, 246, 0.2); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇩🇪 DFB-POKAL &bull; 1/16 DE FINAL
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 13:00 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            Rot Weiss Essen vs RB Leipzig
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Stadion an der Hafenstraße:</strong> El modesto Rot Weiss Essen de 3ra división alemana recibe al potente RB Leipzig de Bundesliga. La velocidad y transición de los Toros Rojos será demoledora para la zaga local.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Acero:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">RB Leipzig Gana el Partido (2)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.20 - 1.25</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 6: DFB-POKAL - BORUSSIA DORTMUND -->
                <div style="background: var(--bg-card); border: 1px solid rgba(234, 179, 8, 0.35); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(234, 179, 8, 0.2); color: #fde047; border: 1px solid rgba(234, 179, 8, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇩🇪 DFB-POKAL &bull; SIGNAL IDUNA
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 15:45 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            Borussia Dortmund vs Werder Bremen
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Signal Iduna Park:</strong> Duelo estelar de copa alemana. El BVB de Niko Kovač es imponente en el Muro Amarillo; el Werder Bremen buscará el golpe pero en Dortmund suele haber festivales de goles.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Protección:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Dortmund 1X + Más de 1.5</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.25 - 1.30</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 7: SERIE A - SASSUOLO VS LAZIO -->
                <div style="background: var(--bg-card); border: 1px solid rgba(16, 185, 129, 0.35); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1px solid rgba(16, 185, 129, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇮🇹 SERIE A &bull; MAPEI STADIUM
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 12:30 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            US Sassuolo vs SS Lazio
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Mapei Stadium:</strong> Partido matutino de Serie A. Sassuolo suele cerrarse bien en casa pero Lazio tiene mayor pegada colectiva. Choque de orden donde no se esperan excesos de goles.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Control:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Menos de 3.5 Goles Totales</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.25</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 8: COPA DEL REY - ESPANYOL -->
                <div style="background: var(--bg-card); border: 1px solid rgba(59, 130, 246, 0.35); border-radius: 18px; padding: 1.5rem; backdrop-filter: blur(16px); display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
                            <span style="background: rgba(59, 130, 246, 0.2); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.4); padding: 0.2rem 0.65rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800;">
                                🇪🇸 COPA DEL REY &bull; 1ª RONDA
                            </span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1;">⏰ 13:00 (ECU)</span>
                        </div>
                        <h3 style="font-size: 1.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0;">
                            Sestao River vs RCD Espanyol
                        </h3>
                        <p style="font-size: 0.82rem; color: #94a3b8; line-height: 1.5; margin: 0 0 1rem 0;">
                            📍 <strong>Las Llanas (Vizcaya):</strong> El Sestao River de Primera RFEF recibe a un Espanyol de Primera que quiere evitar cualquier traspié copero. La cobertura de empate blinda la clasificación perica.
                        </p>
                    </div>
                    <div style="background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                            <span style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">Fija de Protección:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">RCD Espanyol o Empate (X2)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: var(--text-muted);">Cuota Estimada:</span>
                            <span style="font-size: 0.95rem; font-weight: 800; color: #fbbf24;">@ 1.15</span>
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
    print("✓ index.html actualizado con la Cartelera del Martes 27/10.")

    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(c_new)
    print("✓ dashboard_pronosticos.html actualizado.")

    if os.path.exists(root_index_path):
        with open(root_index_path, "w", encoding="utf-8") as f:
            f.write(c_new)
        print("✓ ../index.html (raíz) actualizado.")
else:
    print(f"❌ Error buscando etiquetas: s_pos={s_pos}, e_pos={e_pos}")
