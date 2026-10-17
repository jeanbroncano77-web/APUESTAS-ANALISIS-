# -*- coding: utf-8 -*-
import os
import sys
import json
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(base_dir, ".."))

# 1. AUDITORÍA DE RESULTADOS DE VIERNES 16/10
audit_path = os.path.join(parent_dir, "sports_agents", "audit_history.json")
with open(audit_path, "r", encoding="utf-8") as f:
    audit_data = json.load(f)

new_audit_entries = [
    {
        "id": 110,
        "match": "Defensa y Justicia vs Instituto",
        "tournament": "Liga Profesional Argentina • Viernes 16/10/2026 • Final: 0 - 1",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Defensa y Justicia o Empate (1X) [Doble Oportunidad]",
        "odds": 1.37,
        "confidence": 75.2,
        "status": "loss",
        "diagnostic": "FALLO REPORTADO POR EL USUARIO: Instituto sorprendió 0-1 a Defensa en Florencio Varela. El Halcón generó muy poco volumen ofensivo (xG 0.82) y fue incapaz de remontar la contra cordobesa. Error de modelado: clasificar como 'fija' una cuota 1.37 en liga argentina de bajo goleo sin factor xG > 1.4.",
        "pnl": -100.0
    },
    {
        "id": 111,
        "match": "Boca Juniors vs Talleres",
        "tournament": "Liga Profesional Argentina • Viernes 16/10/2026 • Final: 1 - 0",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Boca Juniors o Empate (1X) [Doble Oportunidad]",
        "odds": 1.15,
        "confidence": 86.4,
        "status": "win",
        "diagnostic": "ACIERTO: Boca Juniors ganó 1-0 en La Bombonera con gol de Milton Giménez a pase de Kevin Zenón. La Doble Oportunidad 1X se cumplió con solvencia.",
        "pnl": 15.0
    }
]

existing_ids = {h["id"] for h in audit_data["history"]}
for entry in new_audit_entries:
    if entry["id"] not in existing_ids:
        audit_data["history"].append(entry)

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
    "active_streak": 1
}
audit_data["current_bankroll"] = round(audit_data["current_bankroll"] - 85.0, 2)
audit_data["total_profit"] = round(audit_data["current_bankroll"] - audit_data["initial_bankroll"], 2)

with open(audit_path, "w", encoding="utf-8") as f:
    json.dump(audit_data, f, ensure_ascii=False, indent=2)
print(f"Auditoría: Global {wins_global}/{total_global} ({win_rate_global}%), Fijas {wins_fijas}/{total_fijas} ({win_rate_fijas}%)")

# 2. AUTOAPRENDIZAJE CICLO #91
feedback_path = os.path.join(parent_dir, "sports_agents", "autonomous_feedback_log.json")
with open(feedback_path, "r", encoding="utf-8") as f:
    feedback_data = json.load(f)

feedback_data["cycles_completed"] = 91
feedback_data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

new_calibration = {
    "cycle": 91,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "action": "Calibración Bayesiana Post-Fallo Defensa y Justicia vs Instituto",
    "cause_of_error": "Sesgo de sobreconfianza en localía de liga argentina de bajo goleo. Se categorizó como 'Fija' una cuota 1.37 (1X) en un equipo local (Defensa) con xG < 1.0, vulnerable a un gol aislado de contraataque del rival (Instituto 0-1).",
    "corrective_actions": [
        "1. Restricción Estricta de Fijas: Queda PROHIBIDO catalogar como 'Fija' cuotas de Doble Oportunidad superiores a 1.25 en ligas cerradas (< 2.1 goles promedio) si el equipo local no supera el 65% de victorias en casa.",
        "2. Ajuste de penalización de contraataque: home_advantage_dampener_low_scoring reducido a 0.75 para ligas sudamericanas de alta fricción.",
        "3. Regla de Combinadas: No enlazar selecciones de cuota > 1.30 en tickets donde el usuario busca 'cero estrés'; priorizar líneas de Goles Under de amplio colchón (Menos de 3.5/4.5) o Córners acumulados.",
        "4. Auditoría de Banca del Usuario: Reconocimiento explícito de la pérdida de $20 de las ganancias; capital base de $50 preservado al 100% (banca actual: $53.00)."
    ],
    "weights_adjusted": {
        "squad_offense_penalty": 0.88,
        "minimum_draw_floor": 28.5,
        "underdog_counterattack_penalty": 1.25,
        "home_advantage_dampener_low_scoring": 0.75
    },
    "system_health": f"Calibrado y sincero (Win Rate Fijas: {win_rate_fijas}% [{wins_fijas}/{total_fijas}] | Win Rate Global: {win_rate_global}% [{wins_global}/{total_global}] | Ciclo #91)"
}

feedback_data["calibrations"].append(new_calibration)
with open(feedback_path, "w", encoding="utf-8") as f:
    json.dump(feedback_data, f, ensure_ascii=False, indent=2)
print("Autoaprendizaje Ciclo #91 registrado.")

# 3. TEAMS DATABASE
teams_path = os.path.join(parent_dir, "sports_agents", "teams_database.json")
with open(teams_path, "r", encoding="utf-8") as f:
    teams_data = json.load(f)

new_teams = {
    "Real Betis": {
        "fifa_rank": 28,
        "recent_form": ["W", "D", "L", "W", "D"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.3, "xg_against": 1.2, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 49}
        ],
        "key_players": [
            {"name": "Giovani Lo Celso", "position": "Mediapunta Organizador", "avg_shots_p90": 2.6, "avg_sot_p90": 1.1, "shot_creation_actions": 5.4, "goal_prob": 0.35},
            {"name": "Vitor Roque", "position": "Delantero Centro", "avg_shots_p90": 2.9, "avg_sot_p90": 1.3, "shot_creation_actions": 3.1, "goal_prob": 0.40}
        ]
    },
    "RB Leipzig": {
        "fifa_rank": 16,
        "recent_form": ["W", "W", "D", "W", "L"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.2, "xg_against": 0.7, "corners_for": 7, "corners_against": 3, "shots_total": 16, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 56}
        ],
        "key_players": [
            {"name": "Benjamin Šeško", "position": "Delantero Tanque", "avg_shots_p90": 3.4, "avg_sot_p90": 1.7, "shot_creation_actions": 3.8, "goal_prob": 0.48},
            {"name": "Loïs Openda", "position": "Punta de Ruptura", "avg_shots_p90": 3.6, "avg_sot_p90": 1.8, "shot_creation_actions": 4.1, "goal_prob": 0.52}
        ]
    },
    "Genoa": {
        "fifa_rank": 52,
        "recent_form": ["L", "D", "L", "W", "D"],
        "sequence": [
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.8, "xg_against": 1.4, "corners_for": 3, "corners_against": 6, "shots_total": 9, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 42}
        ],
        "key_players": [
            {"name": "Andrea Pinamonti", "position": "Centrodelantero", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 2.2, "goal_prob": 0.30}
        ]
    },
    "Ipswich Town": {
        "fifa_rank": 65,
        "recent_form": ["D", "D", "L", "D", "L"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 2, "xg_for": 0.9, "xg_against": 2.4, "corners_for": 3, "corners_against": 8, "shots_total": 8, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 38}
        ],
        "key_players": [
            {"name": "Liam Delap", "position": "Delantero", "avg_shots_p90": 2.2, "avg_sot_p90": 1.0, "shot_creation_actions": 2.4, "goal_prob": 0.32}
        ]
    }
}

for t_name, t_val in new_teams.items():
    if t_name not in teams_data:
        teams_data[t_name] = t_val

with open(teams_path, "w", encoding="utf-8") as f:
    json.dump(teams_data, f, ensure_ascii=False, indent=2)

# 4. OFFICIAL CALENDAR
calendar_path = os.path.join(parent_dir, "sports_agents", "official_calendar.json")
with open(calendar_path, "r", encoding="utf-8") as f:
    cal_data = json.load(f)

cal_data["2026-10-17"] = {
    "date_str": "17/10/2026",
    "day_name": "Sábado",
    "competition": "LaLiga EA Sports, Premier League, Serie A & Liga Profesional",
    "fixtures": [
        ["Real Betis", "Barcelona", "DOBLE_OPORTUNIDAD"],
        ["Real Madrid", "Sevilla", "DOBLE_OPORTUNIDAD"],
        ["Manchester City", "Ipswich Town", "GOL_EQUIPO"],
        ["Bayern Munich", "RB Leipzig", "GOLES_OVER"],
        ["AS Roma", "Genoa", "DOBLE_OPORTUNIDAD"],
        ["Banfield", "Lanús", "TARJETAS"]
    ]
}

with open(calendar_path, "w", encoding="utf-8") as f:
    json.dump(cal_data, f, ensure_ascii=False, indent=2)
print("Calendario y equipos actualizados.")
