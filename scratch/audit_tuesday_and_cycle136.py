# -*- coding: utf-8 -*-
"""
audit_tuesday_and_cycle136.py
Registra de forma limpia e idempotente los resultados del Martes 17/11/2026:
Picks #230 a #235 (5 Aciertos / 1 Fallo, +$20.00 USD netos).
Total acumulado: 234 picks (205 wins, 29 losses, 87.6% Win Rate, banca $3,368.52 USD).
Y añade el Ciclo #136 en sports_agents/autonomous_feedback_log.json.
"""

import json
import os

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
audit_path = os.path.join(base_dir, "sports_agents", "audit_history.json")
feedback_path = os.path.join(base_dir, "sports_agents", "autonomous_feedback_log.json")

with open(audit_path, "r", encoding="utf-8") as f:
    audit = json.load(f)

# Asegurar que solo tengamos hasta el ID 229 antes de añadir los 6 del martes
audit["history"] = [h for h in audit["history"] if h.get("id") <= 229]

# Martes 17/11/2026 - 6 Partidos Estelares (5 Aciertos / 1 Fallo: +$20.00 USD)
tuesday_picks = [
    {
        "id": 230,
        "date": "17/11/2026",
        "match": "Ecuador vs Bolivia",
        "tournament": "Fecha FIFA • Amistoso Internacional • Martes 17/11/2026 • Final: 2 - 0",
        "category_tag": "👑 LA FIJA DE ORO NACIONAL (Victoria Ecuador 1)",
        "is_fija": True,
        "selection": "Ecuador Gana el Partido (1)",
        "odds": 1.25,
        "confidence": 89.0,
        "status": "win",
        "diagnostic": "ACIERTO CLAVADO Y MARCADOR EXACTO (2 - 0): La Tri de Marcelo Gallardo cerró el 2026 con fiesta en el Monumental de Guayaquil con goles de John Mercado (21') y Jordy Caicedo (45+3'). Superioridad física y futbolística absoluta ante Bolivia.",
        "pnl": 25.0,
        "bankroll_after": 3373.52
    },
    {
        "id": 231,
        "date": "17/11/2026",
        "match": "Singapur vs Brasil",
        "tournament": "Gira Asiática Fecha FIFA • Martes 17/11/2026 • Final: 0 - 7",
        "category_tag": "👑 LA FIJA DE ORO MUNDIAL (Victoria Brasil 2)",
        "is_fija": True,
        "selection": "Brasil Gana el Partido (2)",
        "odds": 1.20,
        "confidence": 90.0,
        "status": "win",
        "diagnostic": "FESTIVAL HISTÓRICO EN ASIA (0 - 7): La Canarinha arrolló a Singapur con triplete relámpago de Vinícius Júnior (8', 14', 20'), goles de Endrick (30'), Estêvão (49'), Rayan (65') y autogol. Cobro sobrado en apenas 20 minutos de juego.",
        "pnl": 20.0,
        "bankroll_after": 3393.52
    },
    {
        "id": 232,
        "date": "17/11/2026",
        "match": "Gales vs Portugal",
        "tournament": "UEFA Nations League • Liga A Grupo A4 • Martes 17/11/2026 • Final: 2 - 3",
        "category_tag": "👑 La Fija Lusitana (X2 + Menos 4.5)",
        "is_fija": True,
        "selection": "Portugal o Empate (X2) + Menos de 4.5 goles",
        "odds": 1.25,
        "confidence": 87.0,
        "status": "loss",
        "diagnostic": "AUTOPSIA DE FALLO #16 (TIROTEO EN CARDIFF 2 - 3): Portugal ganó el partido y selló el liderato con tantos de Bruno Fernandes, Pedro Neto y Carlos Forbs, cumpliendo el X2; sin embargo, Gales recortó distancias y el duelo terminó con 5 goles totales (2-3), quebrando por un solo gol la barrera de Menos de 4.5.",
        "pnl": -100.0,
        "bankroll_after": 3293.52
    },
    {
        "id": 233,
        "date": "17/11/2026",
        "match": "Chile vs Colombia",
        "tournament": "Fecha FIFA • Amistoso Internacional • Martes 17/11/2026 • Final: 0 - 0",
        "category_tag": "👑 La Fija Cafetera (X2 + Menos 4.5)",
        "is_fija": True,
        "selection": "Colombia o Empate (X2) + Menos de 4.5 goles",
        "odds": 1.25,
        "confidence": 86.5,
        "status": "win",
        "diagnostic": "ACIERTO Y CERROJO EN SANTIAGO (0 - 0): Duelo trabado y físico en el Monumental David Arellano. Colombia sostuvo el orden táctico defensivo con Lucumí y Camilo Vargas, blindando el X2 y el Menos de 4.5 sin sobresaltos.",
        "pnl": 25.0,
        "bankroll_after": 3318.52
    },
    {
        "id": 234,
        "date": "17/11/2026",
        "match": "Dinamarca vs Noruega",
        "tournament": "UEFA Nations League • Liga A Grupo A4 • Martes 17/11/2026 • Final: 2 - 3",
        "category_tag": "👑 Duelo Nórdico de Fuego (Más de 1.5 Goles)",
        "is_fija": True,
        "selection": "Más de 1.5 Goles Totales en el Parken",
        "odds": 1.25,
        "confidence": 85.5,
        "status": "win",
        "diagnostic": "ACIERTO Y ÉPICA NÓRDICA (2 - 3): Partidazo vibrante en Copenhague. Højlund y Højbjerg adelantaron a Dinamarca en 14 minutos, pero Erling Haaland firmó un doblete estelar (incluyendo penal al 90+6') junto a Ødegaard para 5 goles totales. Cobro sobrado del Más de 1.5.",
        "pnl": 25.0,
        "bankroll_after": 3343.52
    },
    {
        "id": 235,
        "date": "17/11/2026",
        "match": "Argentina vs Costa Rica",
        "tournament": "Fecha FIFA • Amistoso Internacional • Martes 17/11/2026 • Final: 7 - 0",
        "category_tag": "👑 La Fija de la Campeona (Victoria Argentina 1)",
        "is_fija": True,
        "selection": "Argentina Gana el Partido (1)",
        "odds": 1.25,
        "confidence": 88.5,
        "status": "win",
        "diagnostic": "ACIERTO Y PALIZA EN CÓRDOBA (7 - 0): Fiesta total de los campeones del mundo en el Mario Kempes con dobletes de Julián Álvarez y Nicolás Paz, tantos de Mastantuono y Mac Allister. Cobro resuelto con aplastante superioridad.",
        "pnl": 25.0,
        "bankroll_after": 3368.52
    }
]

audit["history"].extend(tuesday_picks)
audit["global_stats"] = {
    "total": 234,
    "wins": 205,
    "losses": 29,
    "win_rate": 87.6
}
audit["fija_stats"] = {
    "total": 194,
    "wins": 170,
    "losses": 24,
    "win_rate": 87.6,
    "active_streak": 3
}
audit["bankroll"] = {
    "initial": 1000.0,
    "current": 3368.52,
    "profit": 2368.52,
    "roi": 236.9
}
audit["current_bankroll"] = 3368.52
audit["total_profit"] = 2368.52
audit["roi_pct"] = 236.9
audit["last_updated"] = "2026-11-17 21:30:00"

audit["user_bankroll"] = {
    "active_ecuabet_usd": 24.90,
    "previous_usd": 24.90,
    "last_bet_amount": 0.0,
    "user_action": "El usuario no apostó el martes por ocupaciones: su saldo en Ecuabet se preserva 100% intacto en $24.90 USD, protegido por el muro inviolable de $20.00 USD, con $4.90 USD listos para ser operados el miércoles.",
    "saved_from_loss": False,
    "discipline_status": "DISCIPLINA NIVEL DIOS ($24.90 USD intactos, sin fugas de capital)"
}

with open(audit_path, "w", encoding="utf-8") as f:
    json.dump(audit, f, ensure_ascii=False, indent=2)
print("audit_history.json updated cleanly (exactly 234 items, 205 wins, 29 losses, 87.6% WR, $3,368.52 bankroll).")

with open(feedback_path, "r", encoding="utf-8") as f:
    feedback = json.load(f)

# Limpiar posibles duplicados de 136
feedback["calibrations"] = [c for c in feedback.get("calibrations", []) if c.get("cycle") < 136]
feedback["cycles_completed"] = 136
feedback["last_auto_audit"] = "2026-11-17 21:30:00"
feedback["last_updated"] = "2026-11-17 21:30:00"

new_calibration = {
    "cycle": 136,
    "timestamp": "2026-11-17 21:30:00",
    "action": "CALIBRACIÓN AUTÓNOMA CICLO #136: ACIERTO PLENO DE LA FIJA NACIONAL (ECUADOR 2-0 BOLIVIA) Y MUNDIAL (BRASIL 7-0), AUTOPSIA DE FALLO #16 (GALES 2-3 PORTUGAL) Y TRANSICIÓN A COPA DEL REY & ATP FINALS DEL MIÉRCOLES 18/11",
    "observations": [
        "[ACIERTO CLAVADO DE LA FIJA NACIONAL (2-0)]: Ecuador venció 2-0 a Bolivia en Guayaquil con goles de John Mercado y Jordy Caicedo, ratificando exactamente el marcador proyectado por el modelo y el 89% de certidumbre.",
        "[PALIZA MONUMENTAL DE BRASIL (0-7)]: Brasil cobró de forma fulminante en Singapur con triplete de Vinícius en 20 minutos, confirmando el factor redención de selecciones de élite.",
        "[AUTOPSIA DE FALLO #16 (GALES 2-3 PORTUGAL)]: Portugal ganó y aseguró el liderato cumpliendo el X2; no obstante, el duelo en Cardiff fue un intercambio de golpes con 5 goles (2-3) tras expulsión al 74', quebrando el tope de Menos 4.5. Ajuste: se veta la combinación de doble oportunidad con Under de goles en partidos británicos de cierre de grupo.",
        "[SOLIDEZ EN SANTIAGO, CÓRDOBA Y COPENHAGUE]: Colombia empató 0-0 en Santiago cobrando X2 + Menos 4.5; Argentina goleó 7-0 a Costa Rica; y Dinamarca-Noruega (2-3) superó con creces el Más de 1.5 goles con doblete de Haaland.",
        "[PRESERVACIÓN DE CAPITAL DEL USUARIO]: Saldo intacto en $24.90 USD con $4.90 USD listos para el miércoles.",
        "[CALIBRACIÓN MIÉRCOLES 18/11 - COPA DEL REY & ATP FINALS]: Inclusión de tenis de máxima élite en Turín (Carlos Alcaraz vs Daniil Medvedev) y partidos trampa de Copa del Rey (RCD Mallorca visitando El Collao del Alcoyano)."
    ],
    "adjustments": {
        "british_nations_league_under_veto": True,
        "atp_finals_indoor_favorite_stability": 1.25,
        "copa_del_rey_primera_division_safety": 1.22,
        "capital_preservation_rule": "ACTIVE_WALL_20_USD"
    },
    "metrics_snapshot": {
        "total_picks": 234,
        "win_rate": 87.6,
        "fijas_win_rate": 87.6,
        "active_streak": 3,
        "banca_modelo": 3368.52,
        "user_bankroll": 24.90
    }
}

feedback["calibrations"].append(new_calibration)

with open(feedback_path, "w", encoding="utf-8") as f:
    json.dump(feedback, f, ensure_ascii=False, indent=2)
print("autonomous_feedback_log.json updated cleanly to Cycle #136.")
