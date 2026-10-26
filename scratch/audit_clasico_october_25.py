# -*- coding: utf-8 -*-
"""
audit_clasico_october_25.py
Auditoría del Domingo 25 de Octubre de 2026:
- FC Barcelona 1 - 2 Real Madrid (El Clásico):
  - Fija Oficial del Modelo: Ambos Equipos Anotan: Sí @ 1.48 -> WIN (+48)
  - Boleto Personal Usuario Ecuabet: Barça 1X + Ambos Marcan @ 1.58 -> LOSS (-50) [Cayó al min 88 por Mbappé]
- Liverpool 2 - 0 Brighton & Hove Albion:
  - Fija Oficial: Liverpool o Empate (1X) @ 1.12 -> WIN (+12)

Actualiza audit_history.json y autonomous_feedback_log.json (Ciclo #118).
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
history = [p for p in history if p["id"] <= 166]

new_audits = [
    {
        "id": 167,
        "match": "FC Barcelona vs Real Madrid",
        "tournament": "LaLiga EA Sports • Domingo 25/10/2026 • Final: 1 - 2",
        "category_tag": "👑 La Fija Oficial (Ambos Marcan)",
        "is_fija": True,
        "selection": "Ambos Equipos Anotan: Sí (BTTS) [Mercado Neutral]",
        "odds": 1.48,
        "confidence": 78.5,
        "status": "win",
        "diagnostic": "VERDE ROTUNDO EN GOLES (1 - 2): Mbappé (41', 88') y Raphinha (61') cumplieron la ley histórica de que en El Clásico ambos perforan la red.",
        "pnl": 48.0
    },
    {
        "id": 168,
        "match": "Liverpool vs Brighton & Hove Albion",
        "tournament": "Premier League • Domingo 25/10/2026 • Final: 2 - 0",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Liverpool o Empate (1X) [Doble Oportunidad]",
        "odds": 1.12,
        "confidence": 91.5,
        "status": "win",
        "diagnostic": "SOLIDEZ TOTAL EN ANFIELD (2 - 0): Con autogol de Groß y tanto de Isak, Liverpool controló el partido de punta a punta cobrando el 1X.",
        "pnl": 12.0
    },
    {
        "id": 169,
        "match": "Boleto Personal Usuario Ecuabet (Barça 1X + Ambos Marcan)",
        "tournament": "Ecuabet • Domingo 25/10/2026 • Apuesta Personal Usuario",
        "category_tag": "👑 Boleto Usuario Ecuabet (Riesgo Alto)",
        "is_fija": True,
        "selection": "FC Barcelona o Empate (1X) + Ambos Equipos Marcan (Sí) [Cuota 1.58]",
        "odds": 1.58,
        "confidence": 68.0,
        "status": "loss",
        "diagnostic": "LA PUÑALADA DEL MINUTO 88 (1 - 2): Hasta el minuto 87 el partido marchaba 1-1 y el cupón estaba ganado. Un contragolpe letal de Mbappé a la espalda de la línea adelantada de Flick derribó el 1X sobre el cierre. Pérdida real de $50 USD del usuario.",
        "pnl": -50.0
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
audit_db["initial_bankroll"] = initial_bankroll
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

# 2. Actualizar autonomous_feedback_log.json con Ciclo #118
print("\n2. Actualizando autonomous_feedback_log.json con Ciclo #118...")
with open(feedback_file, "r", encoding="utf-8") as f:
    fb_db = json.load(f)

calibrations = fb_db.get("calibrations", [])

new_cycle = {
    "cycle": 118,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "action": "AUTOPSIA #13 (EL CLÁSICO: BARÇA 1-2 MADRID AL MINUTO 88 Y EL COSTO DEL ALL-IN EMOCIONAL)",
    "observations": [
        f"[RESUMEN DE LA JORNADA DOMINGO 25 OCTUBRE]: La Fija Oficial del Modelo 'Ambos Equipos Marcan (Sí)' (@1.48) y Liverpool 1X (@1.12) fueron ACIERTOS TOTALES (1-2 y 2-0).",
        "[AUTOPSIA DE FALLO CRÍTICO #13: EL BOLETO PERSONAL DEL USUARIO (-$50 USD)]: El usuario combinó Barça 1X + Ambos Marcan y arriesgó $50 USD (el 68.5% de su cuenta). Al minuto 87 el partido marchaba 1-1 (cobrado); pero al minuto 88, un contragolpe de Mbappé selló el 1-2 para el Real Madrid, derribando el 1X.",
        "[CONFIRMACIÓN DE LA ADVERTENCIA TÁCTICA]: En el análisis previo se advirtió textualmente: 'El único riesgo oculto es si Mbappé pica a la espalda de la línea adelantada de Flick y el Madrid clava un 1-2 al contragolpe; por eso el Ambos Marcan a secas era el tiro neutral perfecto'. La advertencia se cumplió con precisión quirúrgica.",
        "[LECCIÓN BRUTAL DE GESTIÓN DE BANCA]: El fallo no fue de lectura de goles (ambos marcaron, hubo 3 goles), sino de exposición excesiva de capital (All-In emocional). Saldo remanente real del usuario: $23.00 USD.",
        "[REGLA DE HIERRO #118 - PROTOCOLO DE RECONSTRUCCIÓN]: Queda estrictamente vetado arriesgar más del 15% - 20% del bankroll remanente en una sola jugada. El saldo de $23 USD se reconstruirá mediante micro-stakes disciplinados de $3 a $5 USD.",
        f"[MÉTRICAS OFICIALES CONSOLIDADAS]: Win Rate Global: {win_rate}% ({wins}/{total_picks}) | Win Rate Fijas: {fijas_win_rate}% ({fijas_wins}/{fijas_total}) | Banca Institucional: ${current_bankroll} (+{roi_pct}% ROI)."
    ],
    "system_health": f"Calibrado Integralmente (Win Rate Fijas: {fijas_win_rate}% [{fijas_wins}/{fijas_total}] | Win Rate Global: {win_rate}% [{wins}/{total_picks}] | Ciclo #118)"
}

calibrations.append(new_cycle)
fb_db["calibrations"] = calibrations
fb_db["cycles_completed"] = 118
fb_db["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(feedback_file, "w", encoding="utf-8") as f:
    json.dump(fb_db, f, ensure_ascii=False, indent=2)

print("✓ autonomous_feedback_log.json actualizado con Ciclo #118.")
