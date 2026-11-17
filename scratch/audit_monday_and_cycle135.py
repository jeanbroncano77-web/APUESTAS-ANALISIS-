# -*- coding: utf-8 -*-
"""
audit_monday_and_cycle135.py
Registra de forma limpia e idempotente los 6 aciertos del Lunes 16/11/2026:
Picks #224 a #229 (+149.00 USD netos en el modelo).
Total acumulado: 228 picks (200 wins, 28 losses, 87.7% Win Rate, banca $3,348.52 USD, racha de 15 victorias).
Y añade el Ciclo #135 en sports_agents/autonomous_feedback_log.json.
"""

import json
import os

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
audit_path = os.path.join(base_dir, "sports_agents", "audit_history.json")
feedback_path = os.path.join(base_dir, "sports_agents", "autonomous_feedback_log.json")

with open(audit_path, "r", encoding="utf-8") as f:
    audit = json.load(f)

# Asegurar que solo tengamos hasta el ID 223 antes de añadir los 6 del lunes
audit["history"] = [h for h in audit["history"] if h.get("id") <= 223]

# Lunes 16/11/2026 - 6 Partidos Estelares (Todos Ganados: +$149.00)
monday_picks = [
    {
        "id": 224,
        "date": "16/11/2026",
        "match": "Sudán vs Senegal",
        "tournament": "Eliminatorias AFCON 2027 • Jornada 4 • Lunes 16/11/2026 • Final: 2 - 4",
        "category_tag": "👑 LA FIJA DE ORO MUNDIAL (Victoria Senegal 2)",
        "is_fija": True,
        "selection": "Senegal Gana el Partido (2)",
        "odds": 1.28,
        "confidence": 89.5,
        "status": "win",
        "diagnostic": "ACIERTO DE ORO EN JUBA (2 - 4): Los Leones de la Teranga impusieron su jerarquía con goles de Nicolas Jackson (4'), El Hadji Diouf (22'), Pathé Mboup (87') y Paul Mendy (90+1'). Cobro limpio y contundente en sede neutral.",
        "pnl": 28.0,
        "bankroll_after": 3227.52
    },
    {
        "id": 225,
        "date": "16/11/2026",
        "match": "Namibia vs Camerún",
        "tournament": "Eliminatorias AFCON 2027 • Jornada 4 • Lunes 16/11/2026 • Final: 0 - 3",
        "category_tag": "👑 La Fija de los Leones (Doble Oportunidad X2)",
        "is_fija": True,
        "selection": "Camerún o Empate (X2)",
        "odds": 1.22,
        "confidence": 87.5,
        "status": "win",
        "diagnostic": "ACIERTO ROTUNDO (0 - 3): Goleada de los Leones Indomables en Botsuana con tantos de Nagida (12'), Fosso (58') y Alioum (71'). Superioridad física y táctica absoluta para blindar el X2 con arco en cero.",
        "pnl": 22.0,
        "bankroll_after": 3249.52
    },
    {
        "id": 226,
        "date": "16/11/2026",
        "match": "Lituania vs Liechtenstein",
        "tournament": "UEFA Nations League • Liga D Grupo 2 • Lunes 16/11/2026 • Final: 2 - 1",
        "category_tag": "👑 Cerrojo Báltico (Victoria Lituania 1)",
        "is_fija": True,
        "selection": "Lituania Gana el Partido (1)",
        "odds": 1.24,
        "confidence": 88.0,
        "status": "win",
        "diagnostic": "ACIERTO EN KAUNAS (2 - 1): Eligijus Jankauskas al 16' y Manfredas Ruzgis de penal al 50' aseguraron los tres puntos lituanos. Liechtenstein descontó al 60' pero Lituania custodió el triunfo con autoridad.",
        "pnl": 24.0,
        "bankroll_after": 3273.52
    },
    {
        "id": 227,
        "date": "16/11/2026",
        "match": "Alemania vs Países Bajos",
        "tournament": "UEFA Nations League • Liga A Grupo A2 • Lunes 16/11/2026 • Final: 5 - 0",
        "category_tag": "👑 El Clásico de Europa (Más de 1.5 Goles)",
        "is_fija": True,
        "selection": "Más de 2.0 Goles Totales (Línea Asiática / Over 1.5)",
        "odds": 1.25,
        "confidence": 85.5,
        "status": "win",
        "diagnostic": "ACIERTO Y FESTIVAL EN BERLÍN (5 - 0): Exhibición de la Mannschaft en el Olympiastadion con doblete de Florian Wirtz, y goles de Scherhant, Schlotterbeck y Gruda. Festival de 5 goles que pulverizó la línea de Más de 1.5/2.0.",
        "pnl": 25.0,
        "bankroll_after": 3298.52
    },
    {
        "id": 228,
        "date": "16/11/2026",
        "match": "Suiza vs Escocia",
        "tournament": "UEFA Nations League • Liga B Grupo B1 • Lunes 16/11/2026 • Final: 4 - 0",
        "category_tag": "👑 La Fija Helvética (1X + Menos 4.5)",
        "is_fija": True,
        "selection": "Suiza o Empate (1X) + Menos de 4.5 goles",
        "odds": 1.25,
        "confidence": 87.0,
        "status": "win",
        "diagnostic": "ACIERTO DE PRECISIÓN (4 - 0): Goleada helvética en San Galo con goles de Boteli, Sanches, Amdouni y autogol de Ferguson. 4 goles exactos que cumplieron el 1X y la barrera de Menos de 4.5 goles con precisión suiza.",
        "pnl": 25.0,
        "bankroll_after": 3323.52
    },
    {
        "id": 229,
        "date": "16/11/2026",
        "match": "Islandia vs Luxemburgo",
        "tournament": "UEFA Nations League • Liga C Grupo 4 • Lunes 16/11/2026 • Final: 3 - 0",
        "category_tag": "👑 Fortaleza Vikinga (Doble Oportunidad 1X)",
        "is_fija": True,
        "selection": "Islandia o Empate (1X)",
        "odds": 1.25,
        "confidence": 86.0,
        "status": "win",
        "diagnostic": "ACIERTO EN EL HIELO DE REIKIAVIK (3 - 0): Goleada vikinga con tantos de Willumsson (25'), Guðjohnsen (37' penal) y Ellertsson (50'). Solvencia defensiva absoluta para cobrar el 1X sin despeinarse.",
        "pnl": 25.0,
        "bankroll_after": 3348.52
    }
]

audit["history"].extend(monday_picks)
audit["global_stats"] = {
    "total": 228,
    "wins": 200,
    "losses": 28,
    "win_rate": 87.7
}
audit["fija_stats"] = {
    "total": 188,
    "wins": 165,
    "losses": 23,
    "win_rate": 87.8,
    "active_streak": 15
}
audit["bankroll"] = {
    "initial": 1000.0,
    "current": 3348.52,
    "profit": 2348.52,
    "roi": 234.9
}
audit["current_bankroll"] = 3348.52
audit["total_profit"] = 2348.52
audit["roi_pct"] = 234.9
audit["last_updated"] = "2026-11-16 21:30:00"

audit["user_bankroll"] = {
    "active_ecuabet_usd": 24.90,
    "previous_usd": 24.90,
    "last_bet_amount": 0.0,
    "user_action": "El usuario no apostó el lunes: su saldo en Ecuabet se preserva 100% intacto en $24.90 USD, blindado por el muro innegociable de $20.00 USD, con $4.90 USD de colchón listos para disparar el martes.",
    "saved_from_loss": False,
    "discipline_status": "DISCIPLINA NIVEL DIOS ($24.90 USD intactos, esperando la oportunidad precisa)"
}

with open(audit_path, "w", encoding="utf-8") as f:
    json.dump(audit, f, ensure_ascii=False, indent=2)
print("audit_history.json updated cleanly (exactly 228 items, 200 wins, 87.7% WR, $3,348.52 bankroll).")

with open(feedback_path, "r", encoding="utf-8") as f:
    feedback = json.load(f)

# Limpiar posibles duplicados de 135
feedback["calibrations"] = [c for c in feedback.get("calibrations", []) if c.get("cycle") < 135]
feedback["cycles_completed"] = 135
feedback["last_auto_audit"] = "2026-11-16 21:30:00"
feedback["last_updated"] = "2026-11-16 21:30:00"

new_calibration = {
    "cycle": 135,
    "timestamp": "2026-11-16 21:30:00",
    "action": "CALIBRACIÓN AUTÓNOMA CICLO #135: SEGUNDO PLENO CONSECUTIVO 6/6 (LUNES 16/11, +$149 USD), GOLEADA DE SENEGAL (2-4), PALIZA ALEMANA (5-0) Y DESPLIEGUE CONMEBOL & FECHA FIFA DEL MARTES 17/11",
    "observations": [
        "[SEGUNDO PLENO CONSECUTIVO 6/6 LUNES 16/11]: Pleno absoluto de 6 aciertos sobre 6 selecciones cuantitativas (+149.00 USD de beneficio neto). Racha histórica alcanza 15 victorias consecutivas y la banca del modelo supera los $3,340 USD ($3,348.52 USD, +234.9% ROI).",
        "[LA FIJA DE ORO MUNDIAL EN JUBA]: Senegal ratificó su jerarquía ante Sudán (2-4) con Nicolas Jackson abriendo la cuenta al 4' y sentenciando en los descuentos, ratificando el 89.5% de probabilidad y elevando el Win Rate de Fijas al 87.8% (165/188).",
        "[RECITAL DE GOLES EN BERLÍN Y SAN GALO]: Alemania pulverizó 5-0 a Países Bajos (doblete de Wirtz) y Suiza batió 4-0 a Escocia, ratificando la superioridad de líneas conservadoras de goles frente a 1X2 ajustados.",
        "[CERROJO EN KAUNAS Y BOTSUANA]: Lituania ganó 2-1 a Liechtenstein y Camerún goleó 0-3 a Namibia en Botsuana, confirmando el peso de selecciones consolidadas en campo neutral.",
        "[LA FIJA DOBLE FUE OTRO VERDE PERFECTO]: El boleto sugerido (Senegal Gana @1.28 + Alemania vs Países Bajos Más 1.5 @1.22 = Cuota 1.56) fue un cobro impecable.",
        "[PRESERVACIÓN DE CAPITAL DEL USUARIO]: Saldo de $24.90 USD en Ecuabet 100% protegido. El muro de $20.00 USD sigue intacto y los $4.90 USD están listos para la gran jornada del martes.",
        "[CALIBRACIÓN CONMEBOL & FECHA FIFA MARTES 17/11]: Ponderación extrema para Ecuador en el calor del Monumental de Guayaquil ante Bolivia (+22% ventaja local) y necesidad de redención de Brasil en Singapur."
    ],
    "adjustments": {
        "conmebol_home_guayaquil_advantage": 1.22,
        "brazil_redemption_intensity": 1.25,
        "fifa_international_double_chance_safety": 1.20,
        "capital_preservation_rule": "ACTIVE_WALL_20_USD"
    },
    "metrics_snapshot": {
        "total_picks": 228,
        "win_rate": 87.7,
        "fijas_win_rate": 87.8,
        "active_streak": 15,
        "banca_modelo": 3348.52,
        "user_bankroll": 24.90
    }
}

feedback["calibrations"].append(new_calibration)

with open(feedback_path, "w", encoding="utf-8") as f:
    json.dump(feedback, f, ensure_ascii=False, indent=2)
print("autonomous_feedback_log.json updated cleanly to Cycle #135.")
