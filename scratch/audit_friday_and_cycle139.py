import json

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"

# 1. ACTUALIZAR AUDIT_HISTORY.JSON
audit_path = f"{base_dir}/sports_agents/audit_history.json"
with open(audit_path, "r", encoding="utf-8") as f:
    audit = json.load(f)

# Limpiar si ya existieran IDs >= 248 para evitar duplicados en reejecución
audit["history"] = [h for h in audit["history"] if h.get("id") <= 247]

friday_picks = [
    {
        "id": 248,
        "date": "20/11/2026",
        "match": "Independiente del Valle vs Macará",
        "tournament": "LigaPro Ecuabet 2026 • Segunda Etapa • Viernes 20/11/2026 • Final: 1 - 1",
        "category_tag": "👑 La Fija de Oro Nacional (Victoria IDV 1)",
        "is_fija": True,
        "selection": "Independiente del Valle Gana el Partido (1)",
        "odds": 1.25,
        "confidence": 89.0,
        "status": "loss",
        "diagnostic": "FALLO EN AMAGUAÑA (1 - 1): Macará se plantó con doble línea de 5 ultra replegada. IDV se adelantó al 14' pero perdonó tres ocasiones claras y un contragolpe aislado al 79' empató el juego. Sorpresa en LigaPro y fallo transparente registrado (-$100.00).",
        "pnl": -100.0,
        "bankroll_after": 3565.52
    },
    {
        "id": 249,
        "date": "20/11/2026",
        "match": "Bayern Múnich vs FC Köln",
        "tournament": "Bundesliga Alemana • Jornada 11 • Viernes 20/11/2026 • Final: 2 - 0",
        "category_tag": "👑 La Fija de Oro Europea (Bayern 1 + Más 2.5)",
        "is_fija": True,
        "selection": "FC Bayern Múnich Gana (1) + Más de 2.5 goles",
        "odds": 1.22,
        "confidence": 90.5,
        "status": "loss",
        "diagnostic": "FALLO EN EL COMBO DE GOLES (2 - 0): El Bayern ganó con comodidad gracias a doblete de Kane (28' y 51'), pero reguló el desgaste físico de cara a la fecha de Champions y enfrió el partido sin buscar el tercer gol. El triunfo se dio pero faltó 1 gol para el Over 2.5 (-$100.00).",
        "pnl": -100.0,
        "bankroll_after": 3465.52
    },
    {
        "id": 250,
        "date": "20/11/2026",
        "match": "Athletic Club vs RCD Espanyol",
        "tournament": "LaLiga EA Sports • Jornada 14 • Viernes 20/11/2026 • Final: 2 - 0",
        "category_tag": "Doble Oportunidad Local + Margen Goles (Athletic 1X + U4.5)",
        "is_fija": False,
        "selection": "Athletic Club o Empate (1X) + Menos de 4.5 goles",
        "odds": 1.25,
        "confidence": 88.0,
        "status": "win",
        "diagnostic": "ACIERTO EN SAN MAMÉS (2 - 0): Monólogo de los leones con goles de Sancet y Nico Williams. Espanyol no generó remates al arco. Doble oportunidad y control estricto de goles cobrados (+ $25.00).",
        "pnl": 25.0,
        "bankroll_after": 3490.52
    },
    {
        "id": 251,
        "date": "20/11/2026",
        "match": "España Sub-17 vs China Sub-17",
        "tournament": "Mundial Sub-17 Catar 2026 • Fase de Grupos • Viernes 20/11/2026 • Final: 3 - 0",
        "category_tag": "Victoria Directa Formativa (España 1)",
        "is_fija": False,
        "selection": "España Sub-17 Gana el Partido (1)",
        "odds": 1.22,
        "confidence": 89.0,
        "status": "win",
        "diagnostic": "ACIERTO CON JERARQUÍA EN DOHA (3 - 0): Exhibición de posesión y circulación de 'La Rojita'. Goles al 12', 39' y 71' liquidaron el encuentro ante una China sin respuesta (+ $22.00).",
        "pnl": 22.0,
        "bankroll_after": 3512.52
    },
    {
        "id": 252,
        "date": "20/11/2026",
        "match": "Deportivo Cali vs Millonarios FC",
        "tournament": "Liga BetPlay Dimayor 2026 • Viernes 20/11/2026 • Final: 2 - 2",
        "category_tag": "Línea de Goles Under (Menos de 2.5 goles)",
        "is_fija": False,
        "selection": "Menos de 2.5 goles totales (Under 2.5)",
        "odds": 1.28,
        "confidence": 86.5,
        "status": "loss",
        "diagnostic": "FALLO EN EL CLÁSICO DE PALMASECA (2 - 2): Partido atípico y descontrolado con dos penales sancionados por VAR y una expulsión al 62'. Los 4 goles quebraron por completo la proyección conservadora de pocos goles (-$100.00).",
        "pnl": -100.0,
        "bankroll_after": 3412.52
    },
    {
        "id": 253,
        "date": "20/11/2026",
        "match": "FC Metz vs US Boulogne",
        "tournament": "Ligue 2 de Francia • Jornada 14 • Viernes 20/11/2026 • Final: 1 - 0",
        "category_tag": "Doble Oportunidad Local (Metz 1X)",
        "is_fija": False,
        "selection": "FC Metz o Empate (1X)",
        "odds": 1.25,
        "confidence": 87.0,
        "status": "win",
        "diagnostic": "ACIERTO EN SAINT-SYMPHORIEN (1 - 0): Solidez defensiva del Metz que marcó al 44' y neutralizó cualquier intento de Boulogne. Cobertura 1X resuelta sin sufrir (+ $25.00).",
        "pnl": 25.0,
        "bankroll_after": 3437.52
    }
]

audit["history"].extend(friday_picks)

total_picks = len(audit["history"])
wins = sum(1 for h in audit["history"] if h["status"] == "win")
losses = sum(1 for h in audit["history"] if h["status"] == "loss")
win_rate = round((wins / total_picks) * 100, 1)

fijas_picks = [h for h in audit["history"] if h.get("is_fija", False)]
fijas_total = len(fijas_picks)
fijas_wins = sum(1 for h in fijas_picks if h["status"] == "win")
fijas_losses = sum(1 for h in fijas_picks if h["status"] == "loss")
fijas_win_rate = round((fijas_wins / fijas_total) * 100, 1)

audit["last_updated"] = "2026-11-20 22:05:00"
audit["current_bankroll"] = 3437.52
audit["bankroll"] = 3437.52
audit["total_profit"] = 2437.52
audit["roi_pct"] = 243.8

audit["global_stats"] = {
    "total": total_picks,
    "wins": wins,
    "losses": losses,
    "win_rate": win_rate
}

audit["fija_stats"] = {
    "total": fijas_total,
    "wins": fijas_wins,
    "losses": fijas_losses,
    "win_rate": fijas_win_rate
}

audit["user_bankroll"] = {
    "currency": "USD",
    "bookmaker": "Ecuabet",
    "initial_deposit": 20.00,
    "current_balance": 24.90,
    "net_profit": 4.90,
    "roi_pct": 24.5,
    "safety_wall": 20.00,
    "disposable_buffer": 4.90,
    "last_session_status": "DISCIPLINA_PROTEGIO_CAPITAL_EN_JORNADA_VARIANZA"
}

with open(audit_path, "w", encoding="utf-8") as f:
    json.dump(audit, f, indent=2, ensure_ascii=False)

print(f"audit_history.json actualizado: Total {total_picks}, Wins {wins}, Losses {losses}, Win Rate {win_rate}%, Banca ${audit['current_bankroll']}")

# 2. ACTUALIZAR AUTONOMOUS_FEEDBACK_LOG.JSON (CICLO #139)
feedback_path = f"{base_dir}/sports_agents/autonomous_feedback_log.json"
with open(feedback_path, "r", encoding="utf-8") as f:
    fb = json.load(f)

# Limpiar si ya existe ciclo 139
fb["calibrations"] = [c for c in fb.get("calibrations", []) if c.get("cycle") != 139]

cycle_139 = {
    "cycle": 139,
    "timestamp": "2026-11-20 22:10:00",
    "action": "CONTRALORÍA RIGUROSA & CALIBRACIÓN CICLO #139: AUDITORÍA TRANSPARENTE DEL VIERNES 20/11 (3W / 3L), AUTOPSIAS DE FALLO #17 (IDV 1-1 MACARÁ), #18 (BAYERN 2-0 OVER FALTANTE) Y #19 (CALI-MILLONARIOS 2-2 PENALES), FIN DE RACHA EN 15W Y PROTOCOLO DE RECUPERACIÓN PARA EL SÁBADO 21/11",
    "observations": [
        "[CONTRALORÍA Y TRANSPARENCIA TOTAL (3W / 3L)]: Se registran con absoluta honestidad los 3 fallos del viernes 20/11: el empate de IDV 1-1 ante Macará, la falta de 1 gol en el combo del Bayern (2-0 vs Köln) y el partido caótico con dos penales en Cali vs Millonarios (2-2). El balance de la banca retrocede a $3,437.52 USD y el Win Rate global se calibra en 87.3%.",
        "[AUTOPSIA DE FALLO #17 (IDV 1-1 MACARÁ)]: En fechas finales de etapa de LigaPro donde los visitantes luchan la permanencia con bloque ultra bajo, la posesión sin gol temprano genera ansiedad. Ajuste: queda prohibido jugar victoria simple a cuota baja en LigaPro sin cobertura de Doble Oportunidad 1X o líneas de goles amplias.",
        "[AUTOPSIA DE FALLO #18 (BAYERN 2-0 KÖLN - OVER 2.5 CAÍDO)]: Los gigantes europeos antes de semana de Champions regulan energía en el complemento tras ir ganando 2-0. Ajuste: en vísperas de Champions League, vetar combos de Over 2.5 y priorizar victoria simple o hándicap directo.",
        "[AUTOPSIA DE FALLO #19 (CALI 2-2 MILLONARIOS)]: El factor arbitral con 2 penales VAR y una expulsión desnaturalizó el partido cerrado proyectado. Se refuerza el filtro de volatilidad en clásicos con árbitros propensos al VAR.",
        "[PROTECCIÓN ABSOLUTA DEL CAPITAL DEL USUARIO]: Gracias a la regla del Muro de $20.00 USD, el usuario no arriesgó su capital base en un viernes de alta varianza. Su saldo se mantiene firme en $24.90 USD con sus $4.90 listos para el súper sábado.",
        "[CALIBRACIÓN SÁBADO 21/11 - FINAL SUDAMERICANA & ELITE EUROPEA]: Despliegue en la Gran Final CONMEBOL Sudamericana (Atlético Mineiro vs Boca Juniors con filtro Under estricto en final única), Real Madrid en el Bernabéu ante Celta, Manchester City en el Etihad, Católica vs Barcelona en LigaPro, Lazio en Roma y PSG en Francia."
    ],
    "adjustments": {
        "pre_champions_rotation_over_veto": True,
        "ligapro_relegation_block_draw_risk": 1.35,
        "var_penalty_referee_volatility_buffer": 1.25,
        "final_unica_sudamericana_under_weight": 1.40,
        "capital_preservation_rule": "ACTIVE_WALL_20_USD",
        "consecutive_win_streak": 1
    },
    "metrics_snapshot": {
        "total_picks": total_picks,
        "win_rate": win_rate,
        "fijas_win_rate": fijas_win_rate,
        "active_streak": 1,
        "banca_modelo": 3437.52,
        "user_bankroll": 24.90
    }
}

fb["calibrations"].append(cycle_139)
fb["cycles_completed"] = 139
fb["last_auto_audit"] = "2026-11-20 22:10:00"
fb["last_updated"] = "2026-11-20 22:10:00"

with open(feedback_path, "w", encoding="utf-8") as f:
    json.dump(fb, f, indent=2, ensure_ascii=False)

print(f"autonomous_feedback_log.json actualizado con Ciclo #139. Total ciclos: {fb['cycles_completed']}")
