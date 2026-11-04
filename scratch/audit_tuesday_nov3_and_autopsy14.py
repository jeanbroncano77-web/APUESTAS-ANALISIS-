# -*- coding: utf-8 -*-
"""
audit_tuesday_nov3_and_autopsy14.py
Auditoría completa del Martes 3 de Noviembre de 2026:
1. Villarreal 0 - 6 PSG (Champions League) -> WIN (+25.0)
2. Feyenoord 0 - 3 Inter de Milán (Champions League) -> WIN (+28.0)
3. Deportivo Pasto 2 - 0 Jaguares (Liga BetPlay) -> WIN (+48.0)
4. Manchester United 3 - 2 AS Roma (Champions League) -> WIN (+55.0)
5. FC Barcelona 3 - 0 Aston Villa (Ambos Marcan: Sí) -> LOSS (-$100.0) [AUTOPSIA #14]
6. Mushuc Runa 2 - 3 Manta FC (1X) -> LOSS (-$100.0) [Penal al minuto 90+9']

Genera Ciclo de Autoaprendizaje #129 / Autopsia #14:
- Diagnóstico del fallo de Ambos Marcan en Camp Nou (Aston Villa en cero)
- El penal al 90+9' en Echaleche
- El usuario NO apostó, por lo que su banca real sigue en $24.90 USD intacta
- Actualiza audit_history.json, autonomous_feedback_log.json y sincroniza index.html
"""

import os
import sys
import json
from datetime import datetime

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
audit_file = os.path.join(base_dir, "sports_agents", "audit_history.json")
feedback_file = os.path.join(base_dir, "sports_agents", "autonomous_feedback_log.json")

print("1. Cargando audit_history.json...")
with open(audit_file, "r", encoding="utf-8") as f:
    audit_db = json.load(f)

history = audit_db.get("history", [])
history = [p for p in history if p["id"] <= 181]

tuesday_picks = [
    {
        "id": 182,
        "match": "Villarreal CF vs Paris Saint-Germain",
        "tournament": "UEFA Champions League • Martes 03/11/2026 • Final: 0 - 6",
        "category_tag": "👑 La Fija (Doble Oportunidad X2)",
        "is_fija": True,
        "selection": "PSG o Empate (X2) [Victoria 0-6]",
        "odds": 1.25,
        "confidence": 88.0,
        "status": "win",
        "diagnostic": "PASEO MONUMENTAL EN LA CERÁMICA (0 - 6): El PSG de Luis Enrique arrolló sin piedad a un Villarreal diezmado, cobrando el X2 y la victoria con baile histórico.",
        "pnl": 25.0
    },
    {
        "id": 183,
        "match": "Feyenoord vs Inter de Milán",
        "tournament": "UEFA Champions League • Martes 03/11/2026 • Final: 0 - 3",
        "category_tag": "👑 La Fija (Doble Oportunidad X2)",
        "is_fija": True,
        "selection": "Inter de Milán o Empate (X2) [Victoria 0-3]",
        "odds": 1.28,
        "confidence": 86.0,
        "status": "win",
        "diagnostic": "AUTORIDAD NERAZZURRA EN DE KUIP (0 - 3): Bisseck, Esposito y Zieliński liquidaron en Rotterdam para cobrar el X2 con holgura.",
        "pnl": 28.0
    },
    {
        "id": 184,
        "match": "Deportivo Pasto vs Jaguares de Córdoba",
        "tournament": "Liga BetPlay Colombia • Martes 03/11/2026 • Final: 2 - 0",
        "category_tag": "👑 La Fija (Total Goles)",
        "is_fija": True,
        "selection": "Total Goles: Menos de 2.5 Goles",
        "odds": 1.48,
        "confidence": 85.0,
        "status": "win",
        "diagnostic": "CERROJO EN NARIÑO (2 - 0): Pasto impuso su localía con goles de Serje y Méndez, manteniendo el marcador por debajo de 2.5 goles como se proyectó.",
        "pnl": 48.0
    },
    {
        "id": 185,
        "match": "Manchester United vs AS Roma",
        "tournament": "UEFA Champions League • Martes 03/11/2026 • Final: 3 - 2",
        "category_tag": "👑 La Fija (Ambos Marcan)",
        "is_fija": True,
        "selection": "Ambos Equipos Anotan: Sí (BTTS)",
        "odds": 1.55,
        "confidence": 84.0,
        "status": "win",
        "diagnostic": "FESTIVAL EN OLD TRAFFORD (3 - 2): Soulé y Malen marcaron para Roma; Bruno Fernandes y Cunha remontaron para el United. Ambos Marcan cobrado de sobra.",
        "pnl": 55.0
    },
    {
        "id": 186,
        "match": "FC Barcelona vs Aston Villa",
        "tournament": "UEFA Champions League • Martes 03/11/2026 • Final: 3 - 0",
        "category_tag": "👑 La Fija (Ambos Marcan)",
        "is_fija": True,
        "selection": "Ambos Equipos Anotan: Sí (BTTS) [Aston Villa se fue en blanco]",
        "odds": 1.50,
        "confidence": 82.0,
        "status": "loss",
        "diagnostic": "AUTOPSIA #14: TRAMPA DE FUERA DE JUEGO CULÉ (3 - 0). Aston Villa venía con 12 goles en Champions pero cayó 7 veces en fuera de juego ante la línea de Flick y Joan García atajó todo. Villa no marcó y falló el BTTS (aunque el 1X + Más 1.5 sí se cumplió).",
        "pnl": -100.0
    },
    {
        "id": 187,
        "match": "Mushuc Runa vs Manta FC",
        "tournament": "LigaPro Ecuador • Martes 03/11/2026 • Final: 2 - 3",
        "category_tag": "👑 La Fija (Doble Oportunidad 1X)",
        "is_fija": True,
        "selection": "Mushuc Runa o Empate (1X) [Penal rival en el 90+9']",
        "odds": 1.25,
        "confidence": 83.0,
        "status": "loss",
        "diagnostic": "DESENLACE AGÓNICO EN ECHALECHE (2 - 3): El Ponchito empataba 2-2 en el 95', pero un penal sancionado al minuto 90+9 convertido por Joaquín Vergés tumbó el 1X sobre la hora extrema.",
        "pnl": -100.0
    }
]

for p in tuesday_picks:
    history.append(p)

audit_db["history"] = history
total_picks = len(history)
wins = sum(1 for r in history if r.get("status") == "win")
losses = sum(1 for r in history if r.get("status") == "loss")
win_rate = round((wins / total_picks) * 100, 1)

fijas = [r for r in history if r.get("is_fija")]
fijas_total = len(fijas)
fijas_wins = sum(1 for r in fijas if r.get("status") == "win")
fijas_losses = sum(1 for r in fijas if r.get("status") == "loss")
fijas_win_rate = round((fijas_wins / fijas_total) * 100, 1)

streak = 0
for r in reversed(history):
    if r.get("status") == "win":
        streak += 1
    else:
        break

total_profit = round(sum(r.get("pnl", 0.0) for r in history), 2)
initial_bankroll = 1000.0
current_bankroll = round(initial_bankroll + total_profit, 2)
roi_pct = round((total_profit / initial_bankroll) * 100, 1)

brier_sum = sum((float(r.get("confidence", 75.0)) / 100.0 - (1.0 if r.get("status") == "win" else 0.0)) ** 2 for r in history)
brier_score = round(brier_sum / total_picks, 4)

audit_db["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
audit_db["current_bankroll"] = current_bankroll
audit_db["total_profit"] = total_profit
audit_db["roi_pct"] = roi_pct
audit_db["brier_score"] = brier_score

audit_db["global_stats"] = {
    "total": total_picks,
    "wins": wins,
    "losses": losses,
    "win_rate": win_rate
}

audit_db["fija_stats"] = {
    "total": fijas_total,
    "wins": fijas_wins,
    "losses": fijas_losses,
    "win_rate": fijas_win_rate,
    "active_streak": streak
}

audit_db["bankroll"] = {
    "initial": initial_bankroll,
    "current": current_bankroll,
    "profit": total_profit,
    "roi": roi_pct
}

# Saldo del usuario permanece intacto en $24.90 USD porque NO apostó
audit_db["user_bankroll"] = {
    "active_ecuabet_usd": 24.90,
    "previous_usd": 24.90,
    "last_bet_amount": 0.00,
    "user_action": "Usuario decidió no apostar preservando el 100% de su capital de $24.90 USD",
    "saved_from_loss": True
}

with open(audit_file, "w", encoding="utf-8") as f:
    json.dump(audit_db, f, ensure_ascii=False, indent=2)

print(f"✓ audit_history.json actualizado: {total_picks} picks (Wins: {wins}, Losses: {losses}, Win Rate: {win_rate}%)")
print(f"✓ Fijas: {fijas_wins}/{fijas_total} ({fijas_win_rate}%) | Banca Modelo: ${current_bankroll}")
print(f"✓ Saldo Real Usuario Ecuabet: $24.90 USD (Intacto)")

# 2. Actualizar autonomous_feedback_log.json con Ciclo #129 / Autopsia #14
print("\n2. Actualizando autonomous_feedback_log.json con Ciclo #129...")
with open(feedback_file, "r", encoding="utf-8") as f:
    fb_db = json.load(f)

calibrations = fb_db.get("calibrations", [])

new_cycle = {
    "cycle": 129,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "action": "AUTOPSIA DE FALLO #14: EL CERROJO DE HANSI FLICK (BARÇA 3-0 ASTON VILLA) Y EL PENAL AL 90+9' EN ECHALECHE",
    "observations": [
        "[AUTOPSIA DE FALLO #14 - LA FALACIA DEL AMBOS MARCAN]: En Barça 3-0 Aston Villa, el modelo proyectó 'Ambos Marcan' basándose en los 12 goles previos del Villa y las bajas defensivas culés. Sin embargo, la sincronización milimétrica de la trampa de fuera de juego de Hansi Flick (7 offsides al Villa) y la soberbia actuación de Joan García dejaron a Unai Emery en cero. Lección crítica: En casa de gigantes con línea alta agresiva, el 'Ambos Marcan' es frágil si el rival cae repetidamente en fuera de juego. El mercado seguro era '1X + Más de 1.5' (cobrado 3-0).",
        "[PRESERVACIÓN TOTAL DE BANCA DE USUARIO]: El usuario no ejecutó la apuesta de Ambos Marcan, evitando la pérdida y salvaguardando sus $24.90 USD intactos en Ecuabet. Se reconoce el acierto intuitivo del usuario al detectar el riesgo.",
        "[ANÁLISIS DEL DESENLACE EN ECHALECHE (2-3)]: Mushuc Runa empataba 2-2 en el minuto 95, pero un penal sancionado en el minuto 90+9 liquidó el 1X. En el hexagonal de descenso de LigaPro con tiempos añadidos > 8 minutos, la volatilidad en el cierre exige cobertura DNB o mercado de goles en lugar de doble oportunidad ajustada.",
        f"[MÉTRICAS OFICIALES CONSOLIDADAS]: {total_picks} pronósticos auditados | {wins} Aciertos / {losses} Fallos | Win Rate Global: {win_rate}% | Win Rate Fijas: {fijas_win_rate}% ({fijas_wins}/{fijas_total}) | Brier Score: {brier_score}."
    ],
    "system_health": f"Calibrado Forense (Win Rate Fijas: {fijas_win_rate}% [{fijas_wins}/{fijas_total}] | Ciclo #129)"
}

calibrations.append(new_cycle)
fb_db["calibrations"] = calibrations
fb_db["cycles_completed"] = 129
fb_db["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(feedback_file, "w", encoding="utf-8") as f:
    json.dump(fb_db, f, ensure_ascii=False, indent=2)

print("✓ autonomous_feedback_log.json actualizado con Ciclo #129.")
