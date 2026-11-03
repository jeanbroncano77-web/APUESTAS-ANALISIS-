# -*- coding: utf-8 -*-
"""
audit_full_recap_and_sync_nov3.py
Recopilación completa de partidos del 27 de octubre al 3 de noviembre de 2026:
1. AS Roma 4 - 2 Cagliari (Serie A - Cuota de Oro 1.38) -> WIN (Usuario cobró $6.90 con $5.00 reales)
2. CD Cuarte 0 - 2 Girona FC (Copa del Rey - Cuota 1.15) -> WIN
3. CD Manacor 0 - 5 Villarreal CF (Copa del Rey - Cuota 1.16) -> WIN
4. Rot-Weiss Essen 1 - 2 RB Leipzig (DFB-Pokal - Cuota 1.22) -> WIN
5. Borussia Dortmund 3 - 2 Werder Bremen (DFB-Pokal - Cuota 1.28) -> WIN
6. Racing Santander 0 - 3 Real Madrid (LaLiga - Cuota 1.25) -> WIN
7. Independiente del Valle 2 - 0 Liga de Quito (LigaPro - Cuota 1.24) -> WIN
8. Macará 3 - 0 Barcelona SC (LigaPro - Cuota 1.48) -> WIN

Registra el Ciclo de Autoaprendizaje #127 / Caso de Éxito #15:
- La salvada histórica del veto a la cuota 1.07 de Arsenal (Fleetwood 1-1 Arsenal, eliminado en penales)
- El cobro con la Roma (4-2)
- La racha activa de 12 victorias consecutivas
- Sincroniza las 3 Áreas de index.html y dashboard_pronosticos.html
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
# Conservar hasta id 173
history = [p for p in history if p["id"] <= 173]

new_picks = [
    {
        "id": 174,
        "match": "AS Roma vs Cagliari Calcio",
        "tournament": "Serie A Italia • Martes 27/10/2026 • Final: 4 - 2",
        "category_tag": "👑 La Fija de Oro (Sello de Certeza #119)",
        "is_fija": True,
        "selection": "AS Roma Gana el Partido (1) [Cuota de Oro]",
        "odds": 1.38,
        "confidence": 88.0,
        "status": "win",
        "diagnostic": "FIESTA GOLEADORA EN EL OLÍMPICO (4 - 2): Dybala y Dovbyk destrozaron la lenta zaga de Cagliari. El usuario apostó $5.00 USD reales y cobró $6.90 USD (+$1.90 netos en Ecuabet).",
        "pnl": 38.0
    },
    {
        "id": 175,
        "match": "CD Cuarte vs Girona FC",
        "tournament": "Copa del Rey España • Martes 27/10/2026 • Final: 0 - 2",
        "category_tag": "👑 La Fija (Copa del Rey)",
        "is_fija": True,
        "selection": "Girona FC Gana el Partido (2)",
        "odds": 1.15,
        "confidence": 90.0,
        "status": "win",
        "diagnostic": "JERARQUÍA EN ZARAGOZA (0 - 2): Abel Ruiz y Pyshchur resolvieron sin despeinarse ante un rival de 5ta categoría.",
        "pnl": 15.0
    },
    {
        "id": 176,
        "match": "CD Manacor vs Villarreal CF",
        "tournament": "Copa del Rey España • Martes 27/10/2026 • Final: 0 - 5",
        "category_tag": "👑 La Fija (Copa del Rey)",
        "is_fija": True,
        "selection": "Villarreal CF Gana el Partido (2)",
        "odds": 1.16,
        "confidence": 92.0,
        "status": "win",
        "diagnostic": "FESTIVAL GROGUET EN BALEARES (0 - 5): Cinco goles (Diatta, Pépé, Cardona) para certificar el abismo de categorías.",
        "pnl": 16.0
    },
    {
        "id": 177,
        "match": "Rot-Weiss Essen vs RB Leipzig",
        "tournament": "DFB-Pokal Alemania • Martes 27/10/2026 • Final: 1 - 2",
        "category_tag": "👑 La Fija (DFB-Pokal)",
        "is_fija": True,
        "selection": "RB Leipzig Gana el Partido (2)",
        "odds": 1.22,
        "confidence": 86.0,
        "status": "win",
        "diagnostic": "REMONTADA DE LOS TOROS ROJOS (1 - 2): Doblete salvador de Baumgartner (78' y 82') para avanzar a octavos y cobrar el verde.",
        "pnl": 22.0
    },
    {
        "id": 178,
        "match": "Borussia Dortmund vs Werder Bremen",
        "tournament": "DFB-Pokal Alemania • Martes 27/10/2026 • Final: 3 - 2",
        "category_tag": "👑 La Fija (DFB-Pokal)",
        "is_fija": True,
        "selection": "Dortmund 1X + Más de 1.5 Goles",
        "odds": 1.28,
        "confidence": 85.0,
        "status": "win",
        "diagnostic": "PARTIDAZO EN EL SIGNAL IDUNA (3 - 2): Guirassy y Sabitzer sellaron la victoria en tiempo reglamentario cobrando el 1X y el over con creces.",
        "pnl": 28.0
    },
    {
        "id": 179,
        "match": "Racing de Santander vs Real Madrid",
        "tournament": "LaLiga EA Sports • Domingo 01/11/2026 • Final: 0 - 3",
        "category_tag": "👑 La Fija (LaLiga EA Sports)",
        "is_fija": True,
        "selection": "Real Madrid Gana el Partido (2)",
        "odds": 1.25,
        "confidence": 88.0,
        "status": "win",
        "diagnostic": "AUTORIDAD EN EL SARDINERO (0 - 3): Goles de Mbappé, Bellingham y Diomandé para asegurar el triunfo con total solvencia.",
        "pnl": 25.0
    },
    {
        "id": 180,
        "match": "Independiente del Valle vs Liga de Quito",
        "tournament": "LigaPro Ecuador • Domingo 01/11/2026 • Final: 2 - 0",
        "category_tag": "👑 La Fija (LigaPro Ecuador)",
        "is_fija": True,
        "selection": "Independiente del Valle o Empate (1X) [Victoria 2-0]",
        "odds": 1.24,
        "confidence": 87.0,
        "status": "win",
        "diagnostic": "CLÁSICO CAPITALINO EN CHILLO JIJÓN (2 - 0): IDV anuló por completo a Liga y se llevó el clásico asegurando el 1X con autoridad.",
        "pnl": 24.0
    },
    {
        "id": 181,
        "match": "Macará vs Barcelona SC",
        "tournament": "LigaPro Ecuador • Sábado 31/10/2026 • Final: 3 - 0",
        "category_tag": "🛡️ Táctico / Doble Oportunidad",
        "is_fija": True,
        "selection": "Macará o Empate (1X) [Victoria 3-0]",
        "odds": 1.48,
        "confidence": 82.0,
        "status": "win",
        "diagnostic": "LECCIÓN EN AMBATO (3 - 0): Macará volvió a hacer pesar el Bellavista goleando a un Barcelona desarticulado.",
        "pnl": 48.0
    }
]

for p in new_picks:
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

# Guardar saldo real del usuario
audit_db["user_bankroll"] = {
    "active_ecuabet_usd": 24.90,
    "previous_usd": 23.00,
    "last_bet_amount": 5.00,
    "last_payout": 6.90,
    "net_gain": 1.90,
    "winning_ticket": "AS Roma Gana @ 1.38 (AS Roma 4-2 Cagliari)"
}

with open(audit_file, "w", encoding="utf-8") as f:
    json.dump(audit_db, f, ensure_ascii=False, indent=2)

print(f"✓ audit_history.json actualizado: {total_picks} picks (Wins: {wins}, Losses: {losses}, Win Rate: {win_rate}%)")
print(f"✓ Fijas: {fijas_wins}/{fijas_total} ({fijas_win_rate}%) | Racha Activa: {streak} consecutivas!")
print(f"✓ Saldo Real Usuario en Ecuabet: $24.90 USD (+$1.90 ganados con AS Roma)")

# 2. Actualizar autonomous_feedback_log.json con Ciclo #127 / Caso de Éxito #15
print("\n2. Actualizando autonomous_feedback_log.json con Ciclo #127...")
with open(feedback_file, "r", encoding="utf-8") as f:
    fb_db = json.load(f)

calibrations = fb_db.get("calibrations", [])

new_cycle = {
    "cycle": 127,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "action": "CASO DE ÉXITO #15: EL VETO SALVADOR A ARSENAL (1.07 TRAMPA) Y EL COBRO MAESTRO DE LA AS ROMA (4-2)",
    "observations": [
        "[LA SALVADA HISTÓRICA DEL VETO A LA CUOTA 1.07]: El usuario capturó en vivo una combinada con Fleetwood Town vs Arsenal @ 1.07. El agente intervino con urgencia extrema: 'Meter 3 partidos para ganar una miseria de 1.25 es la trampa más sucia de las casas de apuestas... borra a Arsenal y vete por la Roma'. El resultado real fue una bomba mundial: ¡Fleetwood (4ta división) empató 1-1 con el Arsenal y lo eliminó en penales (5-3)! De haber apostado al Arsenal a 1.07, el usuario habría perdido su dinero. El veto estricto salvó la cuenta.",
        "[EL TRIUNFO DE LA AS ROMA (4 - 2 CAGLIARI)]: El usuario confió en el análisis táctico (la velocidad de Dybala y Dovbyk destrozando el giro lento de Yerry Mina). La Roma arrolló 4-2 en el Olímpico, el usuario cobró su cuota de oro 1.38 con $5.00 reales ganando $6.90 USD (+$1.90 netos), y su saldo real en Ecuabet subió a $24.90 USD.",
        f"[RACHA ACTIVA DE 12 VICTORIAS CONSECUTIVAS]: Pleno total desde el 26 de octubre al 3 de noviembre de 2026 (Galatasaray 2-1, PSG 2-0, Sevilla 2-0, Benfica 2-1, Roma 4-2, Girona 2-0, Villarreal 5-0, Leipzig 2-1, Dortmund 3-2, Madrid 3-0, IDV 2-0, Macará 3-0).",
        f"[MÉTRICAS OFICIALES CONSOLIDADAS]: Win Rate Global: {win_rate}% ({wins}/{total_picks}) | Win Rate Fijas: {fijas_win_rate}% ({fijas_wins}/{fijas_total}) | Racha: {streak} W | Brier Score: {brier_score}."
    ],
    "system_health": f"Calibrado Integralmente (Racha Activa: {streak} W | Win Rate Fijas: {fijas_win_rate}% [{fijas_wins}/{fijas_total}] | Ciclo #127)"
}

calibrations.append(new_cycle)
fb_db["calibrations"] = calibrations
fb_db["cycles_completed"] = 127
fb_db["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(feedback_file, "w", encoding="utf-8") as f:
    json.dump(fb_db, f, ensure_ascii=False, indent=2)

print("✓ autonomous_feedback_log.json actualizado con Ciclo #127.")
