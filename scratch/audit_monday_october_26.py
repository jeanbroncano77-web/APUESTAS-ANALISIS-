# -*- coding: utf-8 -*-
"""
audit_monday_october_26.py
Auditoría del Lunes 26 de Octubre de 2026:
- Galatasaray 2 - 1 Fenerbahçe (Süper Lig): Doblete de Osimhen (29', 44') -> WIN (+30.0)
- PSG 2 - 0 Lyon (Ligue 1): Goles de Mayulu (72') y Godts (84') -> WIN (+18.0)
- Sevilla 2 - 0 Osasuna (LaLiga): Menos de 3.5 goles -> WIN (+25.0)
- Santa Clara 1 - 2 Benfica (Primeira Liga): X2 -> WIN (+22.0)

Actualiza audit_history.json y autonomous_feedback_log.json (Ciclo #119).
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
history = [p for p in history if p["id"] <= 169]

new_audits = [
    {
        "id": 170,
        "match": "Galatasaray vs Fenerbahçe",
        "tournament": "Süper Lig Turquía • Lunes 26/10/2026 • Final: 2 - 1",
        "category_tag": "👑 La Fija de Oro (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Galatasaray o Empate (1X) [Victoria Directa 2-1]",
        "odds": 1.30,
        "confidence": 88.0,
        "status": "win",
        "diagnostic": "EL INFIERNO DE ESTAMBUL (2 - 1): Doblete monumental de Victor Osimhen (29' y 44') para noquear al Fenerbahçe y sellar la Fija de Oro de forma inapelable.",
        "pnl": 30.0
    },
    {
        "id": 171,
        "match": "Paris Saint-Germain vs Olympique de Lyon",
        "tournament": "Ligue 1 Francia • Lunes 26/10/2026 • Final: 2 - 0",
        "category_tag": "👑 La Fija (Doble Oportunidad / Gana)",
        "is_fija": True,
        "selection": "PSG o Empate (1X) [Victoria Directa 2-0]",
        "odds": 1.18,
        "confidence": 89.5,
        "status": "win",
        "diagnostic": "LIDERATO EN SOLITARIO EN PARÍS (2 - 0): Con goles de Senny Mayulu (72') y Mika Godts (84'), el PSG dominó el tramo final y cobró sobrado.",
        "pnl": 18.0
    },
    {
        "id": 172,
        "match": "Sevilla FC vs CA Osasuna",
        "tournament": "LaLiga EA Sports • Lunes 26/10/2026 • Final: 2 - 0",
        "category_tag": "👑 La Fija (Total Goles)",
        "is_fija": True,
        "selection": "Total Goles: Menos de 3.5 Goles",
        "odds": 1.25,
        "confidence": 86.0,
        "status": "win",
        "diagnostic": "ORDEN EN NERVIÓN (2 - 0): Goles de Isaac Romero y Félix Correia en un partido controlado de 2 tantos, cobrando el Menos de 3.5 con holgura.",
        "pnl": 25.0
    },
    {
        "id": 173,
        "match": "CD Santa Clara vs SL Benfica",
        "tournament": "Liga Portugal • Lunes 26/10/2026 • Final: 1 - 2",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "SL Benfica o Empate (X2)",
        "odds": 1.22,
        "confidence": 85.0,
        "status": "win",
        "diagnostic": "REMONTADA EN LAS AZORES (1 - 2): Tras ir perdiendo 1-0 al descanso, las Águilas impusieron su jerarquía con dos goles en el complemento.",
        "pnl": 22.0
    }
]

for p in new_audits:
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

with open(audit_file, "w", encoding="utf-8") as f:
    json.dump(audit_db, f, ensure_ascii=False, indent=2)

print(f"✓ audit_history.json actualizado: {total_picks} picks (Wins: {wins}, Losses: {losses}, Win Rate: {win_rate}%)")
print(f"✓ Fijas: {fijas_wins}/{fijas_total} ({fijas_win_rate}%) | Racha Activa: {streak} | Banca: ${current_bankroll} (+${total_profit} USD, +{roi_pct}% ROI)")

# 2. Actualizar autonomous_feedback_log.json con Ciclo #119
print("\n2. Actualizando autonomous_feedback_log.json con Ciclo #119...")
with open(feedback_file, "r", encoding="utf-8") as f:
    fb_db = json.load(f)

calibrations = fb_db.get("calibrations", [])

new_cycle = {
    "cycle": 119,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "action": "PLENO TOTAL EN LUNES DE RECONSTRUCCIÓN: 4 DE 4 ACIERTOS (GALATASARAY, PSG, SEVILLA, BENFICA)",
    "observations": [
        f"[RESUMEN JORNADA LUNES 26 OCTUBRE]: Pleno absoluto de 4 victorias de 4 pronósticos auditados. Galatasaray derrotó 2-1 a Fenerbahçe con doblete de Osimhen, PSG batió 2-0 al Lyon para asumir liderato, Sevilla cumplió el Menos de 3.5 (2-0) y Benfica remontó en Azores (1-2).",
        "[CALIBRACIÓN PSICOLÓGICA DE USUARIO]: El usuario reportó 'Fear Of Missing Out' (FOMO) tras decidir abstenerse de apostar los $23 USD. Se valida la preservación del capital como un acto de madurez post-traumática, evitando el clásico error de revancha compulsiva.",
        "[NUEVO COMPROMISO DE INCENTIVO PROACTIVO]: El usuario solicitó formalmente mayor firmeza y convicción en las recomendaciones cuando la convergencia estadística supere el 88%. El modelo activará el protocolo 'SELLO DE ALTA CERTEZA' para marcar entradas donde la confianza sea indudable.",
        f"[MÉTRICAS OFICIALES CONSOLIDADAS]: Racha activa de 4 aciertos consecutivos. Win Rate Global: {win_rate}% ({wins}/{total_picks}) | Win Rate Fijas: {fijas_win_rate}% ({fijas_wins}/{fijas_total}) | Banca Institucional: ${current_bankroll} (+{roi_pct}% ROI) | Brier Score: {brier_score}."
    ],
    "system_health": f"Calibrado Integralmente (Racha Activa: 4 W | Win Rate Fijas: {fijas_win_rate}% [{fijas_wins}/{fijas_total}] | Ciclo #119)"
}

calibrations.append(new_cycle)
fb_db["calibrations"] = calibrations
fb_db["cycles_completed"] = 119
fb_db["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(feedback_file, "w", encoding="utf-8") as f:
    json.dump(fb_db, f, ensure_ascii=False, indent=2)

print("✓ autonomous_feedback_log.json actualizado con Ciclo #119.")
