# -*- coding: utf-8 -*-
"""
scratch/integrate_autopsy10_and_riestra.py
1. Enriquecer Deportivo Riestra y Unión de Santa Fe en teams_database.json
2. Agregar contexto a matches_database.json
3. Reemplazar Macará vs IDV por Deportivo Riestra vs Unión de Santa Fe en official_calendar.json
4. Incorporar Autopsia #10 en sync_complete_dashboard_3areas.py
"""

import json
import os
import re

# 1. Enrich teams_database.json
teams_path = "sports_agents/teams_database.json"
with open(teams_path, "r", encoding="utf-8") as f:
    teams_db = json.load(f)

teams_db["Deportivo Riestra"] = {
    "fifa_rank": 58,
    "recent_form": ["L", "D", "W", "L", "D", "D", "L", "W"],
    "sequence": [
        {"goals_scored": 1, "goals_conceded": 0, "xg_for": 0.9, "xg_against": 1.0, "corners_for": 3, "corners_against": 5, "shots_total": 8, "shots_on_target": 3, "yellow_cards": 5, "red_cards": 0, "fouls": 18, "possession": 36},
        {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.6, "xg_against": 1.2, "corners_for": 2, "corners_against": 6, "shots_total": 6, "shots_on_target": 2, "yellow_cards": 4, "red_cards": 1, "fouls": 19, "possession": 38},
        {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.0, "xg_against": 1.1, "corners_for": 4, "corners_against": 4, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 16, "possession": 40},
        {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.7, "xg_against": 0.8, "corners_for": 3, "corners_against": 4, "shots_total": 7, "shots_on_target": 2, "yellow_cards": 4, "red_cards": 0, "fouls": 17, "possession": 39}
    ],
    "key_players": [
        {"name": "Jonathan Herrera", "position": "Delantero Centro", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 2.1, "goal_prob": 0.32},
        {"name": "Milton Céliz", "position": "Extremo / Capitán", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 3.2, "goal_prob": 0.22},
        {"name": "Braian Sánchez", "position": "Mediocentro Físico", "avg_shots_p90": 1.0, "avg_sot_p90": 0.3, "shot_creation_actions": 1.8, "goal_prob": 0.08}
    ]
}
teams_db["Riestra"] = teams_db["Deportivo Riestra"]

teams_db["Unión de Santa Fe"] = {
    "fifa_rank": 48,
    "recent_form": ["D", "L", "W", "D", "L", "W", "D", "L"],
    "sequence": [
        {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.1, "xg_against": 1.2, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 48},
        {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.8, "xg_against": 1.3, "corners_for": 3, "corners_against": 5, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 4, "red_cards": 0, "fouls": 15, "possession": 45},
        {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.6, "xg_against": 0.7, "corners_for": 6, "corners_against": 3, "shots_total": 13, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 52},
        {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.9, "xg_against": 0.9, "corners_for": 4, "corners_against": 4, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 49}
    ],
    "key_players": [
        {"name": "Adrián Balboa", "position": "Delantero Centro", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 2.4, "goal_prob": 0.34},
        {"name": "Nicolás Orsini", "position": "Delantero / Segundo Punta", "avg_shots_p90": 2.1, "avg_sot_p90": 0.8, "shot_creation_actions": 2.2, "goal_prob": 0.28},
        {"name": "Mauro Pittón", "position": "Mediocampista Mixto", "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 3.8, "goal_prob": 0.15}
    ]
}
teams_db["Unión"] = teams_db["Unión de Santa Fe"]

with open(teams_path, "w", encoding="utf-8") as f:
    json.dump(teams_db, f, ensure_ascii=False, indent=2)
print("1. teams_database.json actualizado con Riestra y Unión.")

# 2. Update matches_database.json
matches_path = "sports_agents/matches_database.json"
try:
    with open(matches_path, "r", encoding="utf-8") as f:
        matches_db = json.load(f)
except Exception:
    matches_db = {}

matches_db["Deportivo Riestra vs Unión de Santa Fe"] = {
    "tournament": "Liga Profesional Argentina • Torneo Clausura (Fecha 13)",
    "stadium": "Estadio Guillermo Laza (Buenos Aires)",
    "spectators_est": "3,000 espectadores (19:15 Hora Ecuador / 21:15 Argentina)",
    "referee": "Andrés Merlos",
    "referee_avg_yellows": 5.4,
    "referee_avg_reds": 0.28,
    "intensity": "Extrema (Choque físico en campo de dimensiones reducidas; alta fricción y tendencia de tarjetas y Under)"
}

with open(matches_path, "w", encoding="utf-8") as f:
    json.dump(matches_db, f, ensure_ascii=False, indent=2)
print("2. matches_database.json actualizado con Deportivo Riestra vs Unión.")

# 3. Update official_calendar.json
cal_path = "sports_agents/official_calendar.json"
with open(cal_path, "r", encoding="utf-8") as f:
    cal_db = json.load(f)

cal_db["2026-10-19"] = {
    "date_str": "19/10/2026",
    "day_name": "Lunes",
    "competition": "Premier League, LaLiga EA Sports, Serie A, LigaPro & Liga Profesional Argentina",
    "fixtures": [
        ["Tottenham Hotspur", "Coventry City", "VICTORIA_DIRECTA"],
        ["Getafe", "Rayo Vallecano", "DOBLE_OPORTUNIDAD"],
        ["Monza", "Cagliari", "DOBLE_OPORTUNIDAD"],
        ["Parma", "Torino", "DOBLE_OPORTUNIDAD"],
        ["Mushuc Runa", "Orense SC", "DOBLE_OPORTUNIDAD"],
        ["Deportivo Riestra", "Unión de Santa Fe", "GOLES_UNDER"]
    ]
}

with open(cal_path, "w", encoding="utf-8") as f:
    json.dump(cal_db, f, ensure_ascii=False, indent=2)
print("3. official_calendar.json actualizado (Macará vs IDV reemplazado por Riestra vs Unión).")

# 4. Update sync_complete_dashboard_3areas.py with Autopsia #10
sync_script_path = "sports_agents/sync_complete_dashboard_3areas.py"
with open(sync_script_path, "r", encoding="utf-8") as f:
    sync_code = f.read()

autopsia10_html = """            <!-- AUTOPSIA #10: MACARÁ 1-0 INDEPENDIENTE DEL VALLE (LA TRAMPA DEL CAMPEÓN ANTICIPADO) -->
            <div class="autopsy-card" style="border: 2px solid rgba(239, 68, 68, 0.6); background: rgba(30, 27, 75, 0.7); box-shadow: 0 16px 36px -8px rgba(239, 68, 68, 0.35); margin-bottom: 2rem;">
                <div class="autopsy-header">
                    <div>
                        <div class="autopsy-match" style="color: #f87171; display: flex; align-items: center; gap: 0.5rem;">
                            <span>🚨 AUTOPSIA CLÍNICA #10 (CASO REAL LIGAPRO):</span>
                        </div>
                        <div style="font-size: 1.25rem; font-weight: 800; color: #ffffff; margin-top: 0.25rem;">
                            Macará 1-0 Independiente del Valle &bull; La Trampa Psicológica del "Campeón Anticipado" de Visita
                        </div>
                        <div style="font-size: 0.82rem; color: var(--text-muted); margin-top: 0.2rem;">
                            Componente: SportsPsychologyAgent &bull; MarketRealityAgent &bull; Factor 'championship_pressure_away_freeze'
                        </div>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 0.35rem;">
                        <span class="badge-status badge-loss" style="background: rgba(239, 68, 68, 0.25); border: 1px solid rgba(239, 68, 68, 0.6); color: #fca5a5; font-size: 0.85rem;">
                            ❌ TRASPIÉ DEL GIGANTE VISITANTE
                        </span>
                        <span class="badge-status badge-win" style="background: rgba(16, 185, 129, 0.25); border: 1px solid rgba(16, 185, 129, 0.6); color: #6ee7b7; font-size: 0.85rem;">
                            🛡️ REGLA ORO CONFIRMADA POR EL USUARIO
                        </span>
                    </div>
                </div>
                
                <div class="autopsy-split">
                    <div class="box-flaw" style="border-color: rgba(239, 68, 68, 0.4); background: rgba(239, 68, 68, 0.1);">
                        <div class="box-title-flaw">
                            <span>❌ Diagnóstico Táctico y Psicológico (¿Qué ocurrió en Ambato?)</span>
                        </div>
                        <div class="box-text">
                            <p><strong>1. La Presión de Coronarse de Visita:</strong> IDV llegaba a Ambato sabiendo que un triunfo los consagraba campeones nacionales. Esa urgencia generó precipitación y rigidez motriz, mientras Macará jugó con el orgullo herido de no permitir festejos ajenos en el Bellavista.</p>
                            <p style="margin-top: 0.5rem;"><strong>2. Varianza Brutal en Cancha:</strong> El arquero Rodrigo Rodríguez le atajó un penal a IDV, el VAR les anuló un gol milimétrico, y al 59' Agustín Campana marcó el 1-0 definitivo para Macará. ¡El favorito cayó estrepitosamente!</p>
                            <p style="margin-top: 0.5rem;"><strong>3. ¡Salvación del Usuario!:</strong> El usuario detectó a tiempo el resultado previo real, evitando caer en la trampa en la que cayeron miles de apostadores en Ecuador.</p>
                        </div>
                    </div>
                    
                    <div class="box-solution" style="border-color: rgba(16, 185, 129, 0.4); background: rgba(6, 78, 59, 0.2);">
                        <div class="box-title-solution">
                            <span>🛡️ Ley de Oro Implementada en FeedbackEngine 3.0</span>
                        </div>
                        <div class="box-text">
                            <p><strong>1. Veto Definitivo a Victoria Simple Visitante en Partidos de Título:</strong> Se prohíbe de raíz recomendar Victoria Directa (1X2) a un equipo que busca ser campeón fuera de casa sin cobertura de Doble Oportunidad o Empate No Válido.</p>
                            <p style="margin-top: 0.5rem;"><strong>2. Ponderación de Resistencia Local (1.40x):</strong> Los equipos locales que enfrentan a un candidato al título en estadios de altura multiplican su agresividad defensiva por 1.40x.</p>
                        </div>
                    </div>
                </div>
            </div>\n\n"""

# Insert Autopsia 10 right above Autopsia 9
if "<!-- AUTOPSIA #10:" not in sync_code:
    sync_code = sync_code.replace("<!-- AUTOPSIA #9: LEEDS UNITED", autopsia10_html + "            <!-- AUTOPSIA #9: LEEDS UNITED")
    with open(sync_script_path, "w", encoding="utf-8") as f:
        f.write(sync_code)
    print("4. sync_complete_dashboard_3areas.py enriquecido con Autopsia #10.")
else:
    print("4. Autopsia #10 ya presente en sync_complete_dashboard_3areas.py.")
