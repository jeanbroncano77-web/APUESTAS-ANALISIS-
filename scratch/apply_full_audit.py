# -*- coding: utf-8 -*-
import os
import sys
import json
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(base_dir, ".."))

# 1. AUDITORÍA EXHAUSTIVA
audit_path = os.path.join(parent_dir, "sports_agents", "audit_history.json")
with open(audit_path, "r", encoding="utf-8") as f:
    audit_data = json.load(f)

# Filtrar para dejar solo hasta ID 109 y reemplazar viernes con las 5 fijas reales
audit_data["history"] = [h for h in audit_data["history"] if h["id"] < 110]

friday_all_fixtures = [
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
        "diagnostic": "FALLO REPORTADO: Instituto sorprendió 0-1 en Varela. Defensa generó escaso peligro (0.82 xG) y no pudo empatar tras la contra cordobesa.",
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
        "diagnostic": "ACIERTO: Boca ganó 1-0 en La Bombonera con gol de Milton Giménez (pase de Zenón). La Doble Oportunidad 1X salió verde.",
        "pnl": 15.0
    },
    {
        "id": 112,
        "match": "Cruzeiro (F) vs Liga de Quito (F)",
        "tournament": "Copa Conmebol Libertadores Femenina • Viernes 16/10/2026 • Final: 3 - 0",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Empate o Liga de Quito (X2) [Doble Oportunidad]",
        "odds": 1.42,
        "confidence": 74.2,
        "status": "loss",
        "diagnostic": "FALLO GRAVE DE CONTEXTO: Cruzeiro Femenino goleó 3-0 a Liga de Quito Femenina. El modelo proyectó erróneamente un X2 a LDU asumiendo factores masculinos/altura, ignorando la abrumadora superioridad física y técnica de los clubes brasileños femeninos.",
        "pnl": -100.0
    },
    {
        "id": 113,
        "match": "Atlético Tucumán vs Central Córdoba",
        "tournament": "Liga Profesional Argentina • Viernes 16/10/2026 • Final: 0 - 1",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Atlético Tucumán o Empate (1X) [Doble Oportunidad]",
        "odds": 1.30,
        "confidence": 76.5,
        "status": "loss",
        "diagnostic": "FALLO: Central Córdoba sorprendió 0-1 al Decano en el clásico norteño. Duelo trabado y caliente donde el local cayó en desesperación y no logró vulnerar el cerrojo ferroviario.",
        "pnl": -100.0
    },
    {
        "id": 114,
        "match": "Sarmiento vs Aldosivi",
        "tournament": "Liga Profesional Argentina • Viernes 16/10/2026 • Final: 0 - 0",
        "category_tag": "👑 La Fija (Goles Under)",
        "is_fija": True,
        "selection": "Menos de 4.5 goles totales",
        "odds": 1.12,
        "confidence": 94.5,
        "status": "win",
        "diagnostic": "ACIERTO: Empate 0-0 súper táctico y cerrado en Mar del Plata. La línea de seguridad de menos de 4.5 goles se cumplió con margen absoluto.",
        "pnl": 12.0
    }
]

audit_data["history"].extend(friday_all_fixtures)

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
    "active_streak": 0
}
audit_data["current_bankroll"] = round(audit_data["initial_bankroll"] + sum(h["pnl"] for h in audit_data["history"]), 2)
audit_data["total_profit"] = round(audit_data["current_bankroll"] - audit_data["initial_bankroll"], 2)

with open(audit_path, "w", encoding="utf-8") as f:
    json.dump(audit_data, f, ensure_ascii=False, indent=2)

print(f"AUDITORIA COMPLETA REGISTRADA:")
print(f"  Total Global: {wins_global} Wins / {losses_global} Losses = {win_rate_global}% ({total_global} total)")
print(f"  Total Fijas: {wins_fijas} Wins / {losses_fijas} Losses = {win_rate_fijas}% ({total_fijas} total)")

# 2. AUTOAPRENDIZAJE CICLO #92
feedback_path = os.path.join(parent_dir, "sports_agents", "autonomous_feedback_log.json")
with open(feedback_path, "r", encoding="utf-8") as f:
    feedback_data = json.load(f)

feedback_data["cycles_completed"] = 92
feedback_data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

new_calibration = {
    "cycle": 92,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "action": "Calibración Bayesiana Exhaustiva: Auditoría Completa de la Cartelera de Viernes (3 Fallos Reales)",
    "cause_of_error": "Auditoría integral revelada por el usuario: El viernes fallaron 3 de 5 fijas proyectadas en la cartelera (Defensa 0-1, Tucumán 0-1, y Cruzeiro F 3-0 LDU F). Causas: 1) Doble Oportunidades 1X en clásicos y ligas cerradas sin volumen ofensivo (xG < 1.1). 2) Error crítico de categoría al proyectar LDU Femenino frente a una potencia de Brasil en Libertadores.",
    "corrective_actions": [
        "1. Veto Definitivo a 1X frágiles en torneos de baja anotación: Queda PROHIBIDO recomendar como 'Fija' una Doble Oportunidad si el equipo tiene un promedio de gol menor a 1.2 o cuota superior a 1.22.",
        "2. Separación de Modelos Femenino vs Masculino: Obligatoriedad de factor 'brazilian_women_dominance' (multiplicador 1.65 a favor de clubes de Brasil en Conmebol Femenina). Veto a dar X2 al visitante no brasileño.",
        "3. Límite de Fijas Diarias: Máximo 2 Fijas auténticas por cartelera (confianza >= 94%), erradicando la inclusión forzada de partidos parejos como fijas sintéticas.",
        "4. Win Rate Transparente: Registradas las 11 derrotas en Fijas (86.6% Win Rate real) y 15 en Global (86.8% Win Rate real). Cero ocultamiento de resultados."
    ],
    "weights_adjusted": {
        "squad_offense_penalty": 0.90,
        "minimum_draw_floor": 30.0,
        "underdog_counterattack_penalty": 1.35,
        "home_advantage_dampener_low_scoring": 0.65,
        "fija_qualification_threshold": 92.0
    },
    "system_health": f"Calibrado con rigor honesto (Win Rate Fijas: {win_rate_fijas}% [{wins_fijas}/{total_fijas}] | Win Rate Global: {win_rate_global}% [{wins_global}/{total_global}] | Ciclo #92)"
}

feedback_data["calibrations"].append(new_calibration)
with open(feedback_path, "w", encoding="utf-8") as f:
    json.dump(feedback_data, f, ensure_ascii=False, indent=2)

print("Autoaprendizaje Ciclo #92 guardado.")
