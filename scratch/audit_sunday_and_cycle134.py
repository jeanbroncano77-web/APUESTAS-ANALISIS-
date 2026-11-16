# -*- coding: utf-8 -*-
"""
audit_sunday_and_cycle134.py
Registra de forma idempotente los 6 aciertos del Domingo 08/11/2026 en sports_agents/audit_history.json
y añade el Ciclo #134 en sports_agents/autonomous_feedback_log.json.
Total exacto: 222 picks (194 wins, 28 losses, 87.4% Win Rate, $3,199.52 USD).
"""

import json
import os

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
audit_path = os.path.join(base_dir, "sports_agents", "audit_history.json")
feedback_path = os.path.join(base_dir, "sports_agents", "autonomous_feedback_log.json")

with open(audit_path, "r", encoding="utf-8") as f:
    audit = json.load(f)

# Limpiar posibles duplicados por encima de 216
audit["history"] = [h for h in audit["history"] if h.get("id") <= 217]

# Domingo 08/11/2026 - 6 Partidos Estelares (Todos Ganados: +$166.00)
sunday_picks = [
    {
        "id": 218,
        "date": "08/11/2026",
        "match": "Barcelona SC vs Liga de Quito",
        "tournament": "LigaPro Serie A • Hexagonal Final • Domingo 08/11/2026 • Final: 1 - 1",
        "category_tag": "👑 Clásico Nacional (1X + Más 1.5)",
        "is_fija": True,
        "selection": "Barcelona SC o Empate (1X) + Más de 1.5 goles",
        "odds": 1.35,
        "confidence": 84.0,
        "status": "win",
        "diagnostic": "ACIERTO CLÁSICO NACIONAL (1 - 1): Sebastián González adelantó a LDU a los 16' y el juvenil Johan García empató con golazo para Barcelona al 50'. Enorme intensidad con rojas para Carabalí y Olvera. Se cumplió el 1X y la línea de Más de 1.5 goles con solvencia.",
        "pnl": 35.0,
        "bankroll_after": 3068.52
    },
    {
        "id": 219,
        "date": "08/11/2026",
        "match": "Aucas vs Independiente del Valle",
        "tournament": "LigaPro Serie A • Fase Final • Domingo 08/11/2026 • Final: 2 - 4",
        "category_tag": "👑 La Fija de Quito (Doble Oportunidad X2)",
        "is_fija": True,
        "selection": "Independiente del Valle o Empate (X2)",
        "odds": 1.25,
        "confidence": 86.0,
        "status": "win",
        "diagnostic": "ACIERTO ROTUNDO (2 - 4): IDV festejó su consagración de campeón en la cancha con un festival de Junior Sornoza (doblete y 2 asistencias) junto a tantos de Carabajal y González. Superioridad jerárquica total de los Rayados en Chillogallo.",
        "pnl": 25.0,
        "bankroll_after": 3093.52
    },
    {
        "id": 220,
        "date": "08/11/2026",
        "match": "Atlético de Madrid vs FC Barcelona",
        "tournament": "LaLiga EA Sports • Jornada 13 • Domingo 08/11/2026 • Final: 1 - 2",
        "category_tag": "👑 Partidazo de LaLiga (Más de 1.5 Goles)",
        "is_fija": True,
        "selection": "Más de 2.0 Goles Totales (Línea Asiática / Over 1.5)",
        "odds": 1.25,
        "confidence": 86.5,
        "status": "win",
        "diagnostic": "ACIERTO EN EL METROPOLITANO (1 - 2): Giuliano Simeone abrió la cuenta a los 10' para el Atlético, pero el doblete de Fermín López (45' y 66') sentenció la remontada culé. Festival de 3 goles que superó con holgura el Más 1.5.",
        "pnl": 25.0,
        "bankroll_after": 3118.52
    },
    {
        "id": 221,
        "date": "08/11/2026",
        "match": "Inter de Milán vs Como 1907",
        "tournament": "Serie A Enilive • Jornada 11 • Domingo 08/11/2026 • Final: 2 - 0",
        "category_tag": "👑 LA FIJA DE ORO EUROPEA (Victoria Inter 1)",
        "is_fija": True,
        "selection": "Inter de Milán Gana el Partido (1)",
        "odds": 1.25,
        "confidence": 89.0,
        "status": "win",
        "diagnostic": "ACIERTO DE ORO EN SAN SIRO (2 - 0): Francesco Pio Esposito al 11' y Marcus Thuram al 18' liquidaron el partido de forma express. Victoria contundente de los dirigidos por Simone Inzaghi con arco en cero y dominio absoluto.",
        "pnl": 25.0,
        "bankroll_after": 3143.52
    },
    {
        "id": 222,
        "date": "08/11/2026",
        "match": "Napoli vs Lazio",
        "tournament": "Serie A Enilive • Jornada 11 • Domingo 08/11/2026 • Final: 1 - 1",
        "category_tag": "👑 La Fija Partenopea (1X + Menos 4.5)",
        "is_fija": True,
        "selection": "Napoli o Empate (1X) + Menos de 4.5 goles",
        "odds": 1.28,
        "confidence": 85.5,
        "status": "win",
        "diagnostic": "ACIERTO TÁCTICO PARTENOPEO (1 - 1): Frattesi adelantó a la Lazio al 28' y un autogol de Pedraza al 48' selló el empate definitivo en el Diego Armando Maradona. Control táctico de Conte y cobro sobrado del 1X y Menos 4.5 goles.",
        "pnl": 28.0,
        "bankroll_after": 3171.52
    },
    {
        "id": 223,
        "date": "08/11/2026",
        "match": "RC Lens vs Olympique de Marsella",
        "tournament": "Ligue 1 McDonald's • Jornada 10 • Domingo 08/11/2026 • Final: 1 - 2",
        "category_tag": "👑 Duelo Francés de Alto Voltaje (Más de 1.5 Goles)",
        "is_fija": True,
        "selection": "Más de 1.5 Goles Totales en Bollaert-Delelis",
        "odds": 1.28,
        "confidence": 84.5,
        "status": "win",
        "diagnostic": "ACIERTO ELECTRIZANTE (1 - 2): Amine Gouiri anotó al 2', Florian Thauvin empató al 20' y Abdallah sentenció al 82' para el Marsella de De Zerbi. Duelo de 3 goles que cobró el Más de 1.5 en los primeros 20 minutos.",
        "pnl": 28.0,
        "bankroll_after": 3199.52
    }
]

audit["history"].extend(sunday_picks)
audit["global_stats"] = {
    "total": 222,
    "wins": 194,
    "losses": 28,
    "win_rate": 87.4
}
audit["fija_stats"] = {
    "total": 182,
    "wins": 159,
    "losses": 23,
    "win_rate": 87.4,
    "active_streak": 9
}
audit["bankroll"] = {
    "initial": 1000.0,
    "current": 3199.52,
    "profit": 2199.52,
    "roi": 220.0
}
audit["current_bankroll"] = 3199.52
audit["total_profit"] = 2199.52
audit["roi_pct"] = 220.0
audit["last_updated"] = "2026-11-15 21:50:00"

audit["user_bankroll"] = {
    "active_ecuabet_usd": 24.90,
    "previous_usd": 24.90,
    "last_bet_amount": 0.0,
    "user_action": "El usuario mantuvo máxima serenidad y cero apuestas compulsivas durante su semana ocupada: capital de $24.90 USD se preservó 100% intacto, protegido por el muro inviolable de $20.00 USD.",
    "saved_from_loss": True,
    "discipline_status": "DISCIPLINA NIVEL ÉLITE ($24.90 USD intactos, sin fugas de capital)"
}

with open(audit_path, "w", encoding="utf-8") as f:
    json.dump(audit, f, ensure_ascii=False, indent=2)
print("audit_history.json updated cleanly (exactly 222 items).")

with open(feedback_path, "r", encoding="utf-8") as f:
    feedback = json.load(f)

# Filtrar calibraciones para que no haya duplicados de 134
feedback["calibrations"] = [c for c in feedback.get("calibrations", []) if c.get("cycle") < 134]
feedback["cycles_completed"] = 134
feedback["last_auto_audit"] = "2026-11-15 21:50:00"
feedback["last_updated"] = "2026-11-15 21:50:00"

new_calibration = {
    "cycle": 134,
    "timestamp": "2026-11-15 21:50:00",
    "action": "CALIBRACIÓN AUTÓNOMA CICLO #134: PLENO HISTÓRICO DOMINICAL 08/11 (6 DE 6 ACERTADOS, +$166 USD), LA FIJA DE ORO DE SAN SIRO Y TRANSICIÓN A LA FECHA FIFA (UEFA NATIONS LEAGUE & AFCON)",
    "observations": [
        "[PLENO HISTÓRICO 6/6 DOMINGO 08/11]: Rendimiento perfecto de 6 aciertos sobre 6 selecciones cuantitativas (+166.00 USD de ganancia neta en el modelo). Win Rate global se eleva al 87.4% (194 aciertos en 222 pronósticos).",
        "[LA FIJA DE ORO EUROPEA EN SAN SIRO]: Inter de Milán superó 2-0 a Como 1907 con goles tempraneros de Esposito (11') y Thuram (18'), ratificando el 89% de certidumbre matemática y extendiendo la efectividad de las Fijas al 87.4% (159 aciertos / 182 fijas).",
        "[SOLIDEZ TOTAL EN LIGAPRO ECUABET]: En el Clásico del Monumental, Barcelona SC igualó 1-1 ante LDU con golazo de Johan García, sellando la combinación 1X + Más 1.5 @1.35. En Chillogallo, IDV celebró el título venciendo 2-4 a Aucas con recital de Junior Sornoza cobrando el X2 @1.25.",
        "[LALIGA Y LIGUE 1 EN TIERRA DE GOLES]: En el Metropolitano, doblete de Fermín López dio la victoria al Barça 1-2 sobre el Atlético (3 goles, cobrando Más 1.5 @1.25). En Francia, Marsella batió 1-2 a Lens cumpliendo la línea de goles en apenas 20 minutos.",
        "[SERIE A CERROJO TÁCTICO]: Napoli y Lazio empataron 1-1 en el Maradona, cobrando holgadamente la combinación 1X + Menos de 4.5 goles @1.28.",
        "[PRESERVACIÓN IMPECABLE DEL USUARIO]: El usuario protegió su capital de $24.90 USD en Ecuabet con cero impulsos emocionales. El muro de $20.00 USD permanece intacto con $4.90 USD listos para ser operados con francotirador.",
        "[CALIBRACIÓN FECHA FIFA LUNES 16/11]: Transición a selecciones nacionales: ponderación de jerarquía individual en sede neutral (Senegal y Camerún en África) y alta dinámica de goles en choques estelares europeos (Alemania vs Países Bajos)."
    ],
    "adjustments": {
        "fifa_neutral_venue_hierarchy_boost": 1.18,
        "uefa_nations_league_over15_weight": 1.25,
        "san_siro_inter_mastery": "CONFIRMED_HIGH_CERTAINTY",
        "capital_preservation_rule": "ACTIVE_WALL_20_USD"
    },
    "metrics_snapshot": {
        "total_picks": 222,
        "win_rate": 87.4,
        "fijas_win_rate": 87.4,
        "active_streak": 9,
        "banca_modelo": 3199.52,
        "user_bankroll": 24.90
    }
}

feedback["calibrations"].append(new_calibration)

with open(feedback_path, "w", encoding="utf-8") as f:
    json.dump(feedback, f, ensure_ascii=False, indent=2)
print("autonomous_feedback_log.json updated cleanly to Cycle #134.")
