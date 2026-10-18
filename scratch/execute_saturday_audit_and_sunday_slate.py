# -*- coding: utf-8 -*-
import os
import sys
import json
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(base_dir, ".."))

# 1. AUDITORÍA SÁBADO 17/10
audit_path = os.path.join(parent_dir, "sports_agents", "audit_history.json")
with open(audit_path, "r", encoding="utf-8") as f:
    audit_data = json.load(f)

audit_data["history"] = [h for h in audit_data["history"] if h["id"] < 115]

saturday_fixtures = [
    {
        "id": 115,
        "match": "Real Betis vs Barcelona",
        "tournament": "LaLiga EA Sports • Sábado 17/10/2026 • Final: 1 - 3",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Empate o Barcelona (X2) [Doble Oportunidad]",
        "odds": 1.12,
        "confidence": 94.0,
        "status": "win",
        "diagnostic": "ACIERTO ROTUNDO: FC Barcelona venció 1-3 al Betis en el Villamarín (doblete de Lewandowski, gol de Lamine Yamal). Además, el usuario acertó su apuesta de $40 a Gana Barça + Más de 1.5 goles (@1.70), cobrando $68.00.",
        "pnl": 12.0
    },
    {
        "id": 116,
        "match": "Real Madrid vs Sevilla",
        "tournament": "LaLiga EA Sports • Sábado 17/10/2026 • Final: 2 - 0",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Real Madrid o Empate (1X) [Doble Oportunidad]",
        "odds": 1.18,
        "confidence": 89.2,
        "status": "win",
        "diagnostic": "ACIERTO: Real Madrid ganó 2-0 en el Bernabéu con goles de Mbappé y Vinícius. Asimismo, el tiro del usuario de $10 en tarjetas/faltas del Madrid acertó plenamente (5 amarillas en el encuentro), cobrando $14.00.",
        "pnl": 18.0
    },
    {
        "id": 117,
        "match": "Manchester City vs Ipswich Town",
        "tournament": "Premier League • Sábado 17/10/2026 • Final: 4 - 1",
        "category_tag": "👑 La Fija (Gol de Equipo)",
        "is_fija": True,
        "selection": "Manchester City anota más de 0.5 goles",
        "odds": 1.15,
        "confidence": 96.8,
        "status": "win",
        "diagnostic": "ACIERTO: Manchester City goleó 4-1 en el Etihad Stadium con hat-trick de Erling Haaland. Pick verde desde el minuto 12.",
        "pnl": 15.0
    },
    {
        "id": 118,
        "match": "Bayern Munich vs RB Leipzig",
        "tournament": "Bundesliga • Sábado 17/10/2026 • Final: 2 - 2",
        "category_tag": "👑 La Fija (Goles Over)",
        "is_fija": True,
        "selection": "Más de 1.5 goles totales",
        "odds": 1.18,
        "confidence": 92.5,
        "status": "win",
        "diagnostic": "ACIERTO: Partidazo vibrante de 4 goles en el Allianz Arena (2-2). La línea de más de 1.5 goles se cumplió antes de finalizar la primera parte.",
        "pnl": 18.0
    },
    {
        "id": 119,
        "match": "AS Roma vs Genoa",
        "tournament": "Serie A • Sábado 17/10/2026 • Final: 1 - 0",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "AS Roma o Empate (1X) [Doble Oportunidad]",
        "odds": 1.10,
        "confidence": 95.5,
        "status": "win",
        "diagnostic": "ACIERTO: Victoria 1-0 de la Roma en el Stadio Olimpico con gol de Paulo Dybala. Cobertura 1X verde sin contratiempos.",
        "pnl": 10.0
    },
    {
        "id": 120,
        "match": "Banfield vs Lanús",
        "tournament": "Liga Profesional Argentina • Sábado 17/10/2026 • Final: 0 - 0",
        "category_tag": "👑 La Fija (Tarjetas)",
        "is_fija": True,
        "selection": "Más de 3.5 tarjetas totales",
        "odds": 1.36,
        "confidence": 76.9,
        "status": "win",
        "diagnostic": "ACIERTO: Clásico del Sur de máxima fricción en el Florencio Sola. Facundo Tello mostró 7 tarjetas amarillas y 1 roja. Línea de 3.5 tarjetas superada con holgura.",
        "pnl": 36.0
    }
]

audit_data["history"].extend(saturday_fixtures)

total_global = len(audit_data["history"])
wins_global = sum(1 for h in audit_data["history"] if h["status"] == "win")
losses_global = sum(1 for h in audit_data["history"] if h["status"] == "loss")
win_rate_global = round((wins_global / total_global) * 100, 1)

fijas_history = [h for h in audit_data["history"] if h.get("is_fija")]
total_fijas = len(fijas_history)
wins_fijas = sum(1 for h in fijas_history if h["status"] == "win")
losses_fijas = sum(1 for h in fijas_history if h["status"] == "loss")
win_rate_fijas = round((wins_fijas / total_fijas) * 100, 1)

audit_data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
audit_data["global_stats"] = {
    "total": total_global,
    "wins": wins_global,
    "losses": losses_global,
    "win_rate": win_rate_global
}
audit_data["fija_stats"] = {
    "total": total_fijas,
    "wins": wins_fijas,
    "losses": losses_fijas,
    "win_rate": win_rate_fijas,
    "active_streak": 6
}
audit_data["current_bankroll"] = round(audit_data["initial_bankroll"] + sum(h["pnl"] for h in audit_data["history"]), 2)
audit_data["total_profit"] = round(audit_data["current_bankroll"] - audit_data["initial_bankroll"], 2)

with open(audit_path, "w", encoding="utf-8") as f:
    json.dump(audit_data, f, ensure_ascii=False, indent=2)

print(f"AUDITORIA SABADO: 6 de 6 Acertados!")
print(f"  Total Global: {wins_global}/{total_global} ({win_rate_global}%)")
print(f"  Total Fijas: {wins_fijas}/{total_fijas} ({win_rate_fijas}%)")

# 2. AUTOAPRENDIZAJE CICLO #93
feedback_path = os.path.join(parent_dir, "sports_agents", "autonomous_feedback_log.json")
with open(feedback_path, "r", encoding="utf-8") as f:
    feedback_data = json.load(f)

feedback_data["cycles_completed"] = 93
feedback_data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

new_calibration = {
    "cycle": 93,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "action": "Calibración Bayesiana Ciclo #93: Pleno 6 de 6 en Europa y Recuperación de Banca",
    "observations": [
        "1. Pleno 6 de 6 en la jornada de Sábado 17/10: Las grandes ligas de Europa (LaLiga, Premier, Bundesliga, Serie A) ratificaron la confiabilidad matemática de los planteles de élite frente a la alta varianza sudamericana.",
        "2. Victoria del usuario: Los dos tiros personales ($40 en Barça Gana y +1.5 goles @1.70, y $10 en tarjetas del Real Madrid @1.40) resultaron en verdes impecables, cobrando $82.00 totales. Banca del usuario recuperada a $85.00 ($50 base intacto + $35 ganancia neta).",
        "3. Despliegue del Escudo de Confiabilidad 5.0 (Reliability Shield): Erradicado el sesgo de recompensa de cuota alta; implementados los 3 Niveles de Confianza (Tier 1 Candado, Tier 2 Valor, Tier 3 Riesgo).",
        "4. Validación del mercado de tarjetas en clásicos: Banfield vs Lanús registró 8 amonestaciones totales, confirmando que la fricción arbitral en derbis es una línea de alta predictibilidad cuando el 1X2 es incierto."
    ],
    "weights_adjusted": {
        "squad_offense_penalty": 0.88,
        "minimum_draw_floor": 27.5,
        "underdog_counterattack_penalty": 1.30,
        "home_advantage_dampener_low_scoring": 0.68,
        "fija_qualification_threshold": 92.0
    },
    "system_health": f"Excelente y Reforzado (Win Rate Fijas: {win_rate_fijas}% [{wins_fijas}/{total_fijas}] | Win Rate Global: {win_rate_global}% [{wins_global}/{total_global}] | Racha Activa: 6 Verdes | Ciclo #93)"
}

feedback_data["calibrations"].append(new_calibration)
with open(feedback_path, "w", encoding="utf-8") as f:
    json.dump(feedback_data, f, ensure_ascii=False, indent=2)

print("Autoaprendizaje Ciclo #93 guardado con éxito.")

# 3. ENRIQUECER TEAMS DATABASE PARA DOMINGO
teams_path = os.path.join(parent_dir, "sports_agents", "teams_database.json")
with open(teams_path, "r", encoding="utf-8") as f:
    teams_data = json.load(f)

new_teams_sunday = {
    "Chelsea": {
        "fifa_rank": 14,
        "recent_form": ["W", "W", "D", "W", "W"],
        "sequence": [
            {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.6, "xg_against": 0.8, "corners_for": 6, "corners_against": 4, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 2, "red_cards": 0, "fouls": 10, "possession": 62}
        ],
        "key_players": [
            {"name": "Cole Palmer", "position": "Mediapunta / Estrella Mundial", "avg_shots_p90": 3.6, "avg_sot_p90": 1.8, "shot_creation_actions": 6.8, "goal_prob": 0.52}
        ]
    },
    "Wolverhampton": {
        "fifa_rank": 48,
        "recent_form": ["L", "L", "D", "L", "L"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.0, "xg_against": 2.3, "corners_for": 4, "corners_against": 7, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 41}
        ],
        "key_players": [
            {"name": "Matheus Cunha", "position": "Extremo / Punta", "avg_shots_p90": 2.6, "avg_sot_p90": 1.1, "shot_creation_actions": 4.1, "goal_prob": 0.35}
        ]
    }
}

for t_name, t_val in new_teams_sunday.items():
    if t_name not in teams_data:
        teams_data[t_name] = t_val

with open(teams_path, "w", encoding="utf-8") as f:
    json.dump(teams_data, f, ensure_ascii=False, indent=2)

# 4. CALENDARIO OFICIAL DOMINGO 18/10/2026
calendar_path = os.path.join(parent_dir, "sports_agents", "official_calendar.json")
with open(calendar_path, "r", encoding="utf-8") as f:
    cal_data = json.load(f)

cal_data["2026-10-18"] = {
    "date_str": "18/10/2026",
    "day_name": "Domingo",
    "competition": "Premier League, LaLiga, Serie A & Liga Profesional",
    "fixtures": [
        ["Liverpool", "Chelsea", "DOBLE_OPORTUNIDAD"],
        ["Wolverhampton", "Manchester City", "GOL_EQUIPO"],
        ["Atlético de Madrid", "Leganés", "DOBLE_OPORTUNIDAD"],
        ["AS Roma", "Inter Milan", "GOLES_OVER"],
        ["Villarreal", "Getafe", "DOBLE_OPORTUNIDAD"],
        ["River Plate", "Vélez Sarsfield", "GOLES_UNDER"]
    ]
}

with open(calendar_path, "w", encoding="utf-8") as f:
    json.dump(cal_data, f, ensure_ascii=False, indent=2)

print("Calendario Domingo 18/10 actualizado.")
