# -*- coding: utf-8 -*-
"""
update_area1_monday_october_26.py
Actualiza el Área 1 (Cartelera de Partidos) de index.html y dashboard_pronosticos.html
con los 7 partidos de mañana lunes 26 de octubre de 2026:
1. Técnico Universitario vs Mushuc Runa (LigaPro Ecuador)
2. Sevilla vs Osasuna (LaLiga)
3. PSG vs Lyon (Ligue 1)
4. Galatasaray vs Fenerbahçe (Süper Lig Turquía)
5. Santa Clara vs Benfica (Primeira Liga Portugal)
6. Flamengo vs Atlético Mineiro (Brasileirão)
7. LAFC vs LA Galaxy (MLS - El Tráfico)
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

cartelera_html = """            <!-- HEADER ÁREA 1: CARTELERA LUNES 26 DE OCTUBRE -->
            <div style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.15), rgba(99, 102, 241, 0.15)); border: 1px solid rgba(245, 158, 11, 0.4); border-radius: 1rem; padding: 1.5rem; margin-bottom: 2rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                    <div>
                        <span class="badge" style="background: rgba(245, 158, 11, 0.25); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.5); font-weight: 700; font-size: 0.85rem; padding: 0.35rem 0.85rem; border-radius: 9999px;">
                            📅 CARTELERA OFICIAL &bull; LUNES 26 DE OCTUBRE DE 2026
                        </span>
                        <h2 style="font-size: 1.6rem; font-weight: 900; color: #ffffff; margin-top: 0.5rem; letter-spacing: -0.02em;">
                            Plan de Reconstrucción de Banca: 7 Encuentros Quirúrgicos
                        </h2>
                        <p style="color: var(--text-muted); font-size: 0.95rem; margin-top: 0.25rem;">
                            LigaPro Tungurahua, Clásico de Turquía, PSG vs Lyon, Sevilla, Benfica en Azores, Maracaná y El Tráfico de Los Ángeles.
                        </p>
                    </div>
                    <div style="text-align: right; background: rgba(0,0,0,0.4); padding: 0.85rem 1.25rem; border-radius: 0.75rem; border: 1px solid rgba(255,255,255,0.1);">
                        <div style="font-size: 0.8rem; color: #94a3b8; text-transform: uppercase; font-weight: 700;">Gestión de Capital #118</div>
                        <div style="font-size: 1.25rem; font-weight: 900; color: #10b981;">Stake Sugerido: $3 - $5 USD</div>
                        <div style="font-size: 0.75rem; color: #fbbf24;">Saldo Activo Ecuabet: $23.00 USD</div>
                    </div>
                </div>
            </div>

            <!-- GRID DE PARTIDOS DE MAÑANA LUNES 26/10/2026 -->
            <div class="matches-grid">

                <!-- PARTIDO 1: LIGAPRO ECUADOR -->
                <div class="match-card" style="border: 1px solid rgba(245, 158, 11, 0.4); background: rgba(30, 41, 59, 0.7);">
                    <div class="match-header">
                        <span class="tournament-badge" style="background: rgba(234, 179, 8, 0.2); color: #fde047; border: 1px solid rgba(234, 179, 8, 0.4);">
                            🇪🇨 LIGAPRO ECUADOR &bull; FECHA CLAVE
                        </span>
                        <span class="match-time" style="color: #cbd5e1; font-weight: 700;">15:30 (ECU)</span>
                    </div>
                    <div class="match-teams" style="margin: 1.25rem 0;">
                        <div class="team" style="font-weight: 800; font-size: 1.15rem; color: #ffffff;">Técnico Universitario</div>
                        <div class="vs" style="color: var(--accent); font-weight: 900; font-size: 0.9rem;">VS</div>
                        <div class="team" style="font-weight: 800; font-size: 1.15rem; color: #ffffff;">Mushuc Runa SC</div>
                    </div>
                    <div style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4; margin-bottom: 1rem;">
                        <strong>📍 Estadio Bellavista de Ambato:</strong> Clásico provincial de Tungurahua. El Rodillo Rojo de Ismael Blanco urge de puntos de local, pero el Ponchito de Paul Vélez viene mejor parado en la acumulada. Duelo cerrado y físico.
                    </div>
                    <div class="picks-container" style="background: rgba(15, 23, 42, 0.8); border-radius: 0.75rem; padding: 1rem; border: 1px solid rgba(255,255,255,0.08);">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                            <span style="font-size: 0.85rem; color: #94a3b8; font-weight: 700;">👑 Fija de Protección:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Menos de 2.5 / 3.0 Goles</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.8rem; color: var(--text-muted);">Cuota Ecuabet Estimada:</span>
                            <span style="font-weight: 800; color: #fbbf24;">@ 1.42 - 1.55</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 2: SÜPER LIG TURQUÍA (CLÁSICO INTERCONTINENTAL) -->
                <div class="match-card" style="border: 2px solid rgba(239, 68, 68, 0.5); background: rgba(30, 41, 59, 0.7);">
                    <div class="match-header">
                        <span class="tournament-badge" style="background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4);">
                            🇹🇷 SÜPER LIG &bull; CLÁSICO INTERCONTINENTAL
                        </span>
                        <span class="match-time" style="color: #cbd5e1; font-weight: 700;">13:30 (ECU)</span>
                    </div>
                    <div class="match-teams" style="margin: 1.25rem 0;">
                        <div class="team" style="font-weight: 800; font-size: 1.15rem; color: #ffffff;">Galatasaray</div>
                        <div class="vs" style="color: var(--accent); font-weight: 900; font-size: 0.9rem;">VS</div>
                        <div class="team" style="font-weight: 800; font-size: 1.15rem; color: #ffffff;">Fenerbahçe</div>
                    </div>
                    <div style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4; margin-bottom: 1rem;">
                        <strong>📍 RAMS Park (Estambul):</strong> El duelo más caliente de Europa. Galatasaray líder (19 pts) con Victor Osimhen encendido, ante un Fenerbahçe tercero (16 pts). El infierno del RAMS Park inclina la balanza local.
                    </div>
                    <div class="picks-container" style="background: rgba(15, 23, 42, 0.8); border-radius: 0.75rem; padding: 1rem; border: 1px solid rgba(255,255,255,0.08);">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                            <span style="font-size: 0.85rem; color: #94a3b8; font-weight: 700;">👑 La Fija de Oro:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Galatasaray o Empate (1X)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.8rem; color: var(--text-muted);">Cuota Ecuabet Estimada:</span>
                            <span style="font-weight: 800; color: #fbbf24;">@ 1.30</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 3: LIGUE 1 FRANCIA -->
                <div class="match-card" style="border: 1px solid rgba(59, 130, 246, 0.4); background: rgba(30, 41, 59, 0.7);">
                    <div class="match-header">
                        <span class="tournament-badge" style="background: rgba(59, 130, 246, 0.2); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.4);">
                            🇫🇷 LIGUE 1 &bull; DUELO EN LA CUMBRE
                        </span>
                        <span class="match-time" style="color: #cbd5e1; font-weight: 700;">14:30 (ECU)</span>
                    </div>
                    <div class="match-teams" style="margin: 1.25rem 0;">
                        <div class="team" style="font-weight: 800; font-size: 1.15rem; color: #ffffff;">Paris Saint-Germain</div>
                        <div class="vs" style="color: var(--accent); font-weight: 900; font-size: 0.9rem;">VS</div>
                        <div class="team" style="font-weight: 800; font-size: 1.15rem; color: #ffffff;">Olympique de Lyon</div>
                    </div>
                    <div style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4; margin-bottom: 1rem;">
                        <strong>📍 Parc des Princes:</strong> PSG de Luis Enrique suma 7 victorias al hilo en todas las competiciones (4-2 a Man City y Barça en Champions), pero llega con desgaste. Lyon arriba peleando la punta pero cayó 0-3 con Hoffenheim.
                    </div>
                    <div class="picks-container" style="background: rgba(15, 23, 42, 0.8); border-radius: 0.75rem; padding: 1rem; border: 1px solid rgba(255,255,255,0.08);">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                            <span style="font-size: 0.85rem; color: #94a3b8; font-weight: 700;">👑 Fija de Protección:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">PSG o Empate (1X) + Más 1.5</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.8rem; color: var(--text-muted);">Cuota Ecuabet Estimada:</span>
                            <span style="font-weight: 800; color: #fbbf24;">@ 1.26 - 1.30</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 4: LALIGA ESPAÑA -->
                <div class="match-card" style="border: 1px solid rgba(16, 185, 129, 0.4); background: rgba(30, 41, 59, 0.7);">
                    <div class="match-header">
                        <span class="tournament-badge" style="background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1px solid rgba(16, 185, 129, 0.4);">
                            🇪🇸 LALIGA EA SPORTS &bull; JORNADA 10
                        </span>
                        <span class="match-time" style="color: #cbd5e1; font-weight: 700;">15:00 (ECU)</span>
                    </div>
                    <div class="match-teams" style="margin: 1.25rem 0;">
                        <div class="team" style="font-weight: 800; font-size: 1.15rem; color: #ffffff;">Sevilla FC</div>
                        <div class="vs" style="color: var(--accent); font-weight: 900; font-size: 0.9rem;">VS</div>
                        <div class="team" style="font-weight: 800; font-size: 1.15rem; color: #ffffff;">CA Osasuna</div>
                    </div>
                    <div style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4; margin-bottom: 1rem;">
                        <strong>📍 Ramón Sánchez-Pizjuán:</strong> Sevilla (6º con 14 pts) busca puestos de Champions pero tiene lagunas defensivas. Osasuna (12º con 11 pts) llega peligroso con Ante Budimir en racha de gol.
                    </div>
                    <div class="picks-container" style="background: rgba(15, 23, 42, 0.8); border-radius: 0.75rem; padding: 1rem; border: 1px solid rgba(255,255,255,0.08);">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                            <span style="font-size: 0.85rem; color: #94a3b8; font-weight: 700;">👑 Fija de Protección:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Menos de 3.5 Goles / 1X</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.8rem; color: var(--text-muted);">Cuota Ecuabet Estimada:</span>
                            <span style="font-weight: 800; color: #fbbf24;">@ 1.25 - 1.30</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 5: PRIMEIRA LIGA PORTUGAL -->
                <div class="match-card" style="border: 1px solid rgba(139, 92, 246, 0.4); background: rgba(30, 41, 59, 0.7);">
                    <div class="match-header">
                        <span class="tournament-badge" style="background: rgba(139, 92, 246, 0.2); color: #c4b5fd; border: 1px solid rgba(139, 92, 246, 0.4);">
                            🇵🇹 LIGA PORTUGAL &bull; ISLAS AZORES
                        </span>
                        <span class="match-time" style="color: #cbd5e1; font-weight: 700;">13:45 (ECU)</span>
                    </div>
                    <div class="match-teams" style="margin: 1.25rem 0;">
                        <div class="team" style="font-weight: 800; font-size: 1.15rem; color: #ffffff;">CD Santa Clara</div>
                        <div class="vs" style="color: var(--accent); font-weight: 900; font-size: 0.9rem;">VS</div>
                        <div class="team" style="font-weight: 800; font-size: 1.15rem; color: #ffffff;">SL Benfica</div>
                    </div>
                    <div style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4; margin-bottom: 1rem;">
                        <strong>📍 Estádio de São Miguel (Ponta Delgada):</strong> Salida trampa para las Águilas. Santa Clara llega invicto y rocoso en casa. Benfica tiene jerarquía de sobra pero suele sufrir marcadores cortos en las islas.
                    </div>
                    <div class="picks-container" style="background: rgba(15, 23, 42, 0.8); border-radius: 0.75rem; padding: 1rem; border: 1px solid rgba(255,255,255,0.08);">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                            <span style="font-size: 0.85rem; color: #94a3b8; font-weight: 700;">👑 Fija de Protección:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Benfica o Empate (X2)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.8rem; color: var(--text-muted);">Cuota Ecuabet Estimada:</span>
                            <span style="font-weight: 800; color: #fbbf24;">@ 1.20 - 1.24</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 6: BRASILEIRÃO SÉRIE A -->
                <div class="match-card" style="border: 1px solid rgba(239, 68, 68, 0.4); background: rgba(30, 41, 59, 0.7);">
                    <div class="match-header">
                        <span class="tournament-badge" style="background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4);">
                            🇧🇷 BRASILEIRÃO &bull; JORNADA 32
                        </span>
                        <span class="match-time" style="color: #cbd5e1; font-weight: 700;">18:00 (ECU)</span>
                    </div>
                    <div class="match-teams" style="margin: 1.25rem 0;">
                        <div class="team" style="font-weight: 800; font-size: 1.15rem; color: #ffffff;">Flamengo</div>
                        <div class="vs" style="color: var(--accent); font-weight: 900; font-size: 0.9rem;">VS</div>
                        <div class="team" style="font-weight: 800; font-size: 1.15rem; color: #ffffff;">Atlético Mineiro</div>
                    </div>
                    <div style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4; margin-bottom: 1rem;">
                        <strong>📍 Estadio Maracaná:</strong> El Mengão (2º con 67 pts) viene herido tras caer por penales en Libertadores ante Estudiantes. Necesita ganar sí o sí para pelear el título con Palmeiras ante un Galo (6º con 50 pts).
                    </div>
                    <div class="picks-container" style="background: rgba(15, 23, 42, 0.8); border-radius: 0.75rem; padding: 1rem; border: 1px solid rgba(255,255,255,0.08);">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                            <span style="font-size: 0.85rem; color: #94a3b8; font-weight: 700;">👑 Fija de Protección:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Flamengo o Empate (1X)</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.8rem; color: var(--text-muted);">Cuota Ecuabet Estimada:</span>
                            <span style="font-weight: 800; color: #fbbf24;">@ 1.20 - 1.25</span>
                        </div>
                    </div>
                </div>

                <!-- PARTIDO 7: MLS ESTADOS UNIDOS (EL TRÁFICO) -->
                <div class="match-card" style="border: 1px solid rgba(245, 158, 11, 0.4); background: rgba(30, 41, 59, 0.7);">
                    <div class="match-header">
                        <span class="tournament-badge" style="background: rgba(245, 158, 11, 0.2); color: #fde047; border: 1px solid rgba(245, 158, 11, 0.4);">
                            🇺🇸 MLS &bull; EL TRÁFICO DE LOS ÁNGELES
                        </span>
                        <span class="match-time" style="color: #cbd5e1; font-weight: 700;">20:00 (ECU)</span>
                    </div>
                    <div class="match-teams" style="margin: 1.25rem 0;">
                        <div class="team" style="font-weight: 800; font-size: 1.15rem; color: #ffffff;">Los Angeles FC</div>
                        <div class="vs" style="color: var(--accent); font-weight: 900; font-size: 0.9rem;">VS</div>
                        <div class="team" style="font-weight: 800; font-size: 1.15rem; color: #ffffff;">LA Galaxy</div>
                    </div>
                    <div style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4; margin-bottom: 1rem;">
                        <strong>📍 BMO Stadium (Los Angeles):</strong> El derbi más goleador de Norteamérica. Denis Bouanga lidera el ataque de LAFC ante los zarpazos de Joseph Paintsil. Partido de ida y vuelta donde los goles nunca faltan.
                    </div>
                    <div class="picks-container" style="background: rgba(15, 23, 42, 0.8); border-radius: 0.75rem; padding: 1rem; border: 1px solid rgba(255,255,255,0.08);">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                            <span style="font-size: 0.85rem; color: #94a3b8; font-weight: 700;">👑 Fija de Goles:</span>
                            <span style="font-size: 0.9rem; font-weight: 900; color: #10b981;">Ambos Marcan / Más 2.5</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.8rem; color: var(--text-muted);">Cuota Ecuabet Estimada:</span>
                            <span style="font-weight: 800; color: #fbbf24;">@ 1.40 - 1.50</span>
                        </div>
                    </div>
                </div>

            </div>"""

print("Actualizando Área 1 en index.html...")
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '<section class="dashboard-section" id="section-matches">'
end_marker = '</section>'

start_pos = content.find(start_marker)
if start_pos != -1:
    end_pos = content.find(end_marker, start_pos)
    if end_pos != -1:
        new_content = content[:start_pos + len(start_marker)] + "\n" + cartelera_html + "\n        " + content[end_pos:]
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✓ index.html actualizado con la Cartelera del Lunes 26/10.")

        with open(dashboard_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✓ dashboard_pronosticos.html actualizado con la Cartelera del Lunes 26/10.")

        if os.path.exists(root_index_path):
            with open(root_index_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("✓ ../index.html (raíz) actualizado.")
else:
    print("❌ No se encontró la etiqueta de inicio de sección.")
