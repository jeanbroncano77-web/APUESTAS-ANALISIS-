import json
import os

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
audit_file = os.path.join(base_dir, "sports_agents", "audit_history.json")
feedback_file = os.path.join(base_dir, "sports_agents", "autonomous_feedback_log.json")

# 1. ACTUALIZAR AUDIT_HISTORY.JSON CON LOS RESULTADOS REALES DE CHAMPIONS
with open(audit_file, "r", encoding="utf-8") as f:
    audit_data = json.load(f)

history = audit_data["history"]

# Corregir Filas 91 a 96 (Martes 13/10 Champions League)
# 91: Arsenal vs Lille (3-0) -> WIN
history[90]["status"] = "win"
history[90]["diagnostic"] = "ACIERTO ROTUNDO: Arsenal superó 3-0 a Lille en el Emirates con autoridad absoluta de Saliba, Gabriel y Saka."
history[90]["pnl"] = 14.0

# 92: Inter Milan vs Club Brugge (3-4) -> FALLO
history[91]["status"] = "loss"
history[91]["diagnostic"] = "FALLO CATASTRÓFICO: Inter Milan cayó 3-4 en San Siro ante Club Brugge (hat-trick de Nicolò Tresoldi). El modelo subestimó la vulnerabilidad del repliegue defensivo y la letalidad belga al contraataque."
history[91]["pnl"] = -100.0

# 93: Galatasaray vs Barcelona (1-4) -> WIN
history[92]["status"] = "win"
history[92]["diagnostic"] = "ACIERTO X2 (Victoria 1-4 del Barça): El modelo sobreestimó el factor ambiental de la caldera de Estambul. El Barcelona de Flick aplastó 1-4 demostrando que la jerarquía y el pressing superaban el factor cancha."
history[92]["pnl"] = 14.0

# 94: Viking FK vs Bayern Munich (0-0) -> WIN
history[93]["status"] = "win"
history[93]["diagnostic"] = "ACIERTO TÉCNICO X2 (Empate 0-0): El césped y el frío en Stavanger frenaron el ataque bávaro, que no pudo romper el cerrojo del Viking. El X2 salvó el pick, pero evidenció la advertencia climática."
history[93]["pnl"] = 14.0

# 95: Atlético de Madrid vs Manchester United (2-0) -> WIN
history[94]["status"] = "win"
history[94]["diagnostic"] = "ACIERTO SÓLIDO: Atlético de Madrid impuso su cerrojo en el Metropolitano (2-0) ante un Manchester United inoperante en ataque."
history[94]["pnl"] = 14.0

# 96: Villarreal vs Napoli (1-0) -> FALLO
history[95]["status"] = "loss"
history[95]["diagnostic"] = "FALLO: Villarreal venció 1-0 en La Cerámica con gol en el tramo final. Napoli no tuvo contundencia en sus transiciones y cedió la victoria local."
history[95]["pnl"] = -100.0

# Recalcular métricas exactas
total_matches = len(history)
wins = sum(1 for r in history if r["status"] == "win")
losses = sum(1 for r in history if r["status"] == "loss")
global_wr = round((wins / total_matches) * 100, 1)

fijas = [r for r in history if r.get("is_fija")]
fijas_total = len(fijas)
fijas_wins = sum(1 for r in fijas if r["status"] == "win")
fijas_losses = sum(1 for r in fijas if r["status"] == "loss")
fijas_wr = round((fijas_wins / fijas_total) * 100, 1)

# Racha activa al final del día martes:
# El último partido (Row 96, Napoli) fue LOSS, así que la racha activa cayó a 0.
streak = 0
for r in reversed(history):
    if r["status"] == "win":
        streak += 1
    else:
        break

total_pnl = round(sum(r["pnl"] for r in history), 2)
initial_bankroll = 1000.0
current_bankroll = round(initial_bankroll + total_pnl, 2)
roi = round((total_pnl / initial_bankroll) * 100, 1)

audit_data["global_stats"] = {
    "total": total_matches,
    "wins": wins,
    "losses": losses,
    "win_rate": global_wr
}
audit_data["fija_stats"] = {
    "total": fijas_total,
    "wins": fijas_wins,
    "losses": fijas_losses,
    "win_rate": fijas_wr,
    "active_streak": streak
}
audit_data["bankroll"] = {
    "initial": initial_bankroll,
    "current": current_bankroll,
    "profit": total_pnl,
    "roi": roi
}

with open(audit_file, "w", encoding="utf-8") as f:
    json.dump(audit_data, f, indent=2, ensure_ascii=False)

print(f"Audit actualizado: Global {global_wr}% ({wins}/{total_matches}), Fijas {fijas_wr}% ({fijas_wins}/{fijas_total}), Racha {streak}, Bankroll ${current_bankroll}")

# 2. ACTUALIZAR AUTONOMOUS_FEEDBACK_LOG.JSON CON EL CICLO #81 REAL Y AUTOCRÍTICO
with open(feedback_file, "r", encoding="utf-8") as f:
    feedback_data = json.load(f)

feedback_data["calibrations"] = [c for c in feedback_data.get("calibrations", []) if c.get("cycle") != 81]

c81 = {
    "cycle": 81,
    "timestamp": "2026-10-13 21:40:00",
    "action": "Autocrítica Severa Champions League Martes 13/10 & Re-calibración Miércoles 14/10",
    "status": "CRITICAL_POST_MORTEM",
    "observations": [
        "[AUDITORÍA REAL MARTES 13/10 - 4/6 ACIERTOS / 2 FALLOS]: Inter Milan cayó 3-4 ante Club Brugge en San Siro y Villarreal superó 1-0 a Napoli en La Cerámica. Racha rota (cayó de 9 a 0).",
        "[FALLO CRÍTICO 1 - INTER MILAN 3-4 CLUB BRUGGE]: El modelo asignó 96.8% de confianza a la doble oportunidad del Inter, cayendo en la falacia de cuota ultra-baja (@1.07). No se ponderó la fatiga por calendario de Serie A ni la letalidad de las transiciones verticales del rival (hat-trick de Nicolò Tresoldi).",
        "[ERROR DE DISUASIÓN - BARCELONA 4-1 GALATASARAY]: El usuario planeaba apostar a la victoria directa del Barça (@1.28). El asistente/modelo sobreponderó la hostilidad del estadio turco y aconsejó retirarlo o cambiarlo por Bayern, quitándole al usuario una victoria clara que se selló 1-4 con goles de Cancelo, Fermín, Gordon y Adeyemi.",
        "[ADVERTENCIA CLIMÁTICA CONFIRMADA - VIKING 0-0 BAYERN]: El usuario advirtió sobre el frío y las condiciones en Noruega. Aunque el X2 se cobró, el Bayern fue incapaz de anotar en 90 minutos ante un rival noruego, demostrando que el clima y las canchas pesadas del norte sí afectan la efectividad ofensiva.",
        "[FALLO 2 - VILLARREAL 1-0 NAPOLI]: Napoli no logró generar peligro en España y concedió gol en el tramo final, perdiendo el X2.",
        "[AJUSTE SISTÉMICO URGENTE]: 1) Veto definitivo a catalogar cualquier cuota de 1.05-1.07 como 'búnker impenetrable'. 2) En Champions League, las rotaciones y la sobrecarga muscular son factores de riesgo primarios. 3) Jamás desaconsejar un equipo de élite en racha arrolladora únicamente por mito de estadio rival."
    ],
    "adjustments": {
        "fatigue_decay_champions": 0.22,
        "underdog_counterattack_boost": 0.28,
        "stadium_atmosphere_penalty_cap": 0.08,
        "weather_friction_multiplier": 0.18,
        "forbid_false_certainty_claims": True
    },
    "metrics_snapshot": {
        "global_win_rate": global_wr,
        "fijas_win_rate": fijas_wr,
        "total_audited": total_matches,
        "fijas_total": fijas_total,
        "fijas_wins": fijas_wins,
        "fijas_losses": fijas_losses,
        "pnl_usd": total_pnl,
        "bankroll_usd": current_bankroll,
        "active_streak": streak
    }
}

feedback_data["calibrations"].append(c81)
feedback_data["last_auto_audit"] = "2026-10-13 21:40:00"
feedback_data["last_updated"] = "2026-10-13 21:40:00"

with open(feedback_file, "w", encoding="utf-8") as f:
    json.dump(feedback_data, f, indent=2, ensure_ascii=False)

print("Feedback log actualizado con Ciclo #81 autocrítico.")
