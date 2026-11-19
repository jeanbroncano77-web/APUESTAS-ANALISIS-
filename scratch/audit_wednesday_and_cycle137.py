import json

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"

# 1. ACTUALIZAR AUDIT_HISTORY.JSON
audit_path = f"{base_dir}/sports_agents/audit_history.json"
with open(audit_path, "r", encoding="utf-8") as f:
    audit = json.load(f)

# Limpiar posibles ejecuciones repetidas a partir de ID 236
audit["history"] = [h for h in audit["history"] if h.get("id") <= 235]

wednesday_picks = [
    {
        "id": 236,
        "date": "18/11/2026",
        "match": "Carlos Alcaraz vs Daniil Medvedev",
        "tournament": "Nitto ATP Finals 2026 • Grupo Ivan Lendl • Miércoles 18/11/2026 • Final: 2 - 0 (6-4, 6-4)",
        "category_tag": "👑 La Fija de Oro de Turín (Victoria Alcaraz 1)",
        "is_fija": True,
        "selection": "Carlos Alcaraz Gana el Partido (1)",
        "odds": 1.28,
        "confidence": 88.5,
        "status": "win",
        "diagnostic": "ACIERTO Y AUTORIDAD TOTAL EN TURÍN (2 - 0 Sets: 6-4, 6-4): Carlos Alcaraz desmanteló a Daniil Medvedev con un despliegue de ritmo, dejadas letales y solidez con su primer saque. Boleto sellado a semifinales y cobro impecable @1.28.",
        "pnl": 28.0,
        "bankroll_after": 3396.52
    },
    {
        "id": 237,
        "date": "18/11/2026",
        "match": "CD Alcoyano vs RCD Mallorca",
        "tournament": "Copa del Rey • Primera Ronda • Miércoles 18/11/2026 • Final: 0 - 2",
        "category_tag": "👑 La Fija de Oro Copera (Mallorca X2 + Menos 4.5)",
        "is_fija": True,
        "selection": "RCD Mallorca o Empate (X2) + Menos de 4.5 goles",
        "odds": 1.25,
        "confidence": 88.0,
        "status": "win",
        "diagnostic": "ACIERTO CON JERARQUÍA EN EL COLLAO (0 - 2): El RCD Mallorca impuso el peso de la Primera División con bloque compacto y goles de Larin y Dani Rodríguez. Doble oportunidad y control de goles cobrados sin sufrir.",
        "pnl": 25.0,
        "bankroll_after": 3421.52
    },
    {
        "id": 238,
        "date": "18/11/2026",
        "match": "CD Badajoz vs CD Tenerife",
        "tournament": "Copa del Rey • Primera Ronda • Miércoles 18/11/2026 • Final: 1 - 2",
        "category_tag": "Doble Oportunidad Visitante (Tenerife X2)",
        "is_fija": False,
        "selection": "CD Tenerife o Empate (X2)",
        "odds": 1.25,
        "confidence": 86.5,
        "status": "win",
        "diagnostic": "ACIERTO EN EL NUEVO VIVERO (1 - 2): Tenerife manejó los tiempos y selló el pase de ronda con tanto definitorio al 78'. Cobertura X2 resuelta.",
        "pnl": 25.0,
        "bankroll_after": 3446.52
    },
    {
        "id": 239,
        "date": "18/11/2026",
        "match": "Flavio Cobolli vs Frances Tiafoe",
        "tournament": "Nitto ATP Finals 2026 • Miércoles 18/11/2026 • Final: 1 - 2 Sets (4-6, 6-4, 4-6 | 30 Games)",
        "category_tag": "Total Games Over (Más de 20.5 Games)",
        "is_fija": False,
        "selection": "Más de 20.5 Games Totales",
        "odds": 1.26,
        "confidence": 85.5,
        "status": "win",
        "diagnostic": "ACIERTO OVER CON 30 GAMES TOTALES: Batalla titánica en tres sets entre Cobolli y Tiafoe. La línea de 20.5 games fue pulverizada desde el inicio del tercer set.",
        "pnl": 26.0,
        "bankroll_after": 3472.52
    },
    {
        "id": 240,
        "date": "18/11/2026",
        "match": "Nicaragua vs Montserrat",
        "tournament": "Concacaf Nations League • Play-In • Miércoles 18/11/2026 • Final: 3 - 0",
        "category_tag": "Victoria Local Directa (Nicaragua 1)",
        "is_fija": False,
        "selection": "Nicaragua Gana el Partido (1)",
        "odds": 1.25,
        "confidence": 87.0,
        "status": "win",
        "diagnostic": "ACIERTO Y FIESTA EN MANAGUA (3 - 0): Dominio absoluto de los Pinoleros ante una selección caribeña sin respuesta física ni táctica. Cobro resuelto en el primer tiempo.",
        "pnl": 25.0,
        "bankroll_after": 3497.52
    },
    {
        "id": 241,
        "date": "18/11/2026",
        "match": "Utebo FC vs CE Sabadell",
        "tournament": "Copa del Rey • Primera Ronda • Miércoles 18/11/2026 • Final: 1 - 1 (T.E. 1-2)",
        "category_tag": "Línea de Goles Under (Menos de 3.5 goles 90 min)",
        "is_fija": False,
        "selection": "Menos de 3.5 goles",
        "odds": 1.26,
        "confidence": 85.0,
        "status": "win",
        "diagnostic": "ACIERTO BAJO EL GUIÓN COPERO (1 - 1 en 90 min): Partido cerrado y táctico en césped artificial. Solo 2 goles en tiempo reglamentario, validando plenamente la línea Under 3.5.",
        "pnl": 26.0,
        "bankroll_after": 3523.52
    }
]

audit["history"].extend(wednesday_picks)

total_picks = len(audit["history"])
wins = sum(1 for h in audit["history"] if h["status"] == "win")
losses = sum(1 for h in audit["history"] if h["status"] == "loss")
win_rate = round((wins / total_picks) * 100, 1)

fijas_picks = [h for h in audit["history"] if h.get("is_fija", False)]
fijas_total = len(fijas_picks)
fijas_wins = sum(1 for h in fijas_picks if h["status"] == "win")
fijas_losses = sum(1 for h in fijas_picks if h["status"] == "loss")
fijas_win_rate = round((fijas_wins / fijas_total) * 100, 1)

audit["last_updated"] = "2026-11-18 21:15:00"
audit["current_bankroll"] = 3523.52
audit["bankroll"] = 3523.52
audit["total_profit"] = 2523.52
audit["roi_pct"] = 252.4

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
    "last_session_status": "INTACTO_SIN_APOSTAR_MARTES_Y_MIERCOLES"
}

with open(audit_path, "w", encoding="utf-8") as f:
    json.dump(audit, f, indent=2, ensure_ascii=False)

print(f"audit_history.json actualizado: Total {total_picks}, Wins {wins}, Losses {losses}, Win Rate {win_rate}%, Banca ${audit['current_bankroll']}")

# 2. ACTUALIZAR AUTONOMOUS_FEEDBACK_LOG.JSON (CICLO #137)
feedback_path = f"{base_dir}/sports_agents/autonomous_feedback_log.json"
with open(feedback_path, "r", encoding="utf-8") as f:
    fb = json.load(f)

# Limpiar si ya existe ciclo 137
fb["calibrations"] = [c for c in fb.get("calibrations", []) if c.get("cycle") != 137]

cycle_137 = {
    "cycle": 137,
    "timestamp": "2026-11-18 21:20:00",
    "action": "CALIBRACIÓN AUTÓNOMA CICLO #137: PLENO HISTÓRICO 6 DE 6 DEL MIÉRCOLES 18/11 (ALCARAZ 2-0, MALLORCA, TENERIFE, COBOLLI OVER 30 GAMES, NICARAGUA Y SABADELL UNDER), RACHA RÉCORD DE 9 VICTORIAS SEGUIDAS Y TRANSICIÓN A MUNDIAL SUB-17 & CHAMPIONS FEMENINA DEL JUEVES 19/11",
    "observations": [
        "[PLENO HISTÓRICO PERFECTO (6 DE 6)]: La jornada del miércoles 18/11 cerró con 100% de efectividad en los 6 pronósticos recomendados, elevando el balance institucional a $3,523.52 USD y la racha activa a 9 aciertos consecutivos.",
        "[DEMOLICIÓN DE ALCARAZ EN TURÍN (2-0)]: Carlos Alcaraz dominó a Medvedev con parciales de 6-4, 6-4, validando con holgura la Fija de Oro de Turín @1.28.",
        "[JERARQUÍA COPERA EN ESPAÑA]: RCD Mallorca (0-2 en El Collao) y CD Tenerife (1-2 en Badajoz) impusieron la solidez de categorías superiores. Utebo vs Sabadell (1-1 en 90') confirmó la tendencia de pocos goles en campos de césped artificial.",
        "[PRECISIÓN OVER EN TENIS INDOOR]: Cobolli y Tiafoe libraron una batalla de 30 games (4-6, 6-4, 4-6), pulverizando la línea de Más de 20.5 Games.",
        "[PRESERVACIÓN DE CAPITAL DEL USUARIO]: El usuario mantuvo su banca intacta en $24.90 USD ($20.00 de reserva inviolable y $4.90 de colchón para el jueves 19/11).",
        "[CALIBRACIÓN JUEVES 19/11 - MUNDIAL SUB-17 & UEFA CHAMPIONS FEMENINA]: Explotación de asimetría masiva de nivel en fútbol formativo juvenil (Ecuador Sub-17 vs Nueva Caledonia) y en fase de grupos europea femenina (FC Barcelona vs Servette, Bayern Múnich vs Austria Viena)."
    ],
    "adjustments": {
        "sub17_world_cup_talent_gap_weight": 1.35,
        "womens_champions_league_elite_spread": 1.30,
        "brazil_serie_a_home_field_factor": 1.22,
        "capital_preservation_rule": "ACTIVE_WALL_20_USD",
        "consecutive_win_streak": 9
    },
    "metrics_snapshot": {
        "total_picks": total_picks,
        "win_rate": win_rate,
        "fijas_win_rate": fijas_win_rate,
        "active_streak": 9,
        "banca_modelo": 3523.52,
        "user_bankroll": 24.90
    }
}

fb["calibrations"].append(cycle_137)
fb["cycles_completed"] = 137
fb["last_auto_audit"] = "2026-11-18 21:20:00"
fb["last_updated"] = "2026-11-18 21:20:00"

with open(feedback_path, "w", encoding="utf-8") as f:
    json.dump(fb, f, indent=2, ensure_ascii=False)

print(f"autonomous_feedback_log.json actualizado con Ciclo #137. Total ciclos: {fb['cycles_completed']}")
