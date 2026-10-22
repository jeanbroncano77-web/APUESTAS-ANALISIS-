# -*- coding: utf-8 -*-
"""
settle_wednesday_audit_loss.py
Auditoría rigurosa y sin excusas de la jornada de Miércoles 21/10/2026:
- Real Madrid 4 - 1 RB Leipzig -> Real Madrid Gana @ 1.27 -> WIN (+27)
- Sporting CP 2 - 3 LASK Linz -> Sporting Gana @ 1.20 -> LOSS (-100) [FALLO FATAL]
- Aston Villa 3 - 1 Viking FK -> Aston Villa Gana @ 1.20 -> WIN (+20)
- Inter 1 - 0 Shakhtar -> Inter 1X @ 1.08 -> WIN (+8)
- Bayern 2 - 2 Arsenal -> Ambos Marcan @ 1.58 -> WIN (+58)
- Como 4 - 1 Manchester United -> Man United X2 @ 1.28 -> LOSS (-100) [Batacazo Como]
- Boleto Usuario Ecuabet (Madrid + Sporting) @ 1.52 -> LOSS (-100 institucional / -$10 real usuario)

Actualiza audit_history.json y autonomous_feedback_log.json (Ciclo #115).
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
existing_ids = {r["id"] for r in history}
last_id = max(existing_ids, default=148)

wednesday_audits = [
    {
        "id": last_id + 1,
        "match": "Real Madrid vs RB Leipzig",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 4 - 1",
        "category_tag": "👑 La Fija (Victoria Directa)",
        "is_fija": True,
        "selection": "Real Madrid Gana el Partido (1) [Victoria Directa]",
        "odds": 1.27,
        "confidence": 78.7,
        "status": "win",
        "diagnostic": "GOLEADA BLANCA EN EL BERNABÉU (4 - 1): Mbappé con doblete y Vinícius Jr. confirmaron la supremacía del Madrid en noche de Champions League.",
        "pnl": 27.0
    },
    {
        "id": last_id + 2,
        "match": "Sporting de Lisboa vs LASK",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 2 - 3",
        "category_tag": "👑 La Fija (Victoria Directa)",
        "is_fija": True,
        "selection": "Sporting de Lisboa Gana el Partido (1) [Victoria Directa]",
        "odds": 1.20,
        "confidence": 82.0,
        "status": "loss",
        "diagnostic": "BATACAZO HISTÓRICO Y ERROR CRÍTICO (2 - 3): LASK Linz (que pagaba cuota 12.00) sorprendió con un bloque reactivo y castigó la pasividad defensiva del Sporting en el José Alvalade. Fallo directo de complacencia que arruinó la combinada del usuario.",
        "pnl": -100.0
    },
    {
        "id": last_id + 3,
        "match": "Aston Villa vs Viking FK",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 3 - 1",
        "category_tag": "👑 La Fija (Victoria Directa)",
        "is_fija": True,
        "selection": "Aston Villa Gana el Partido (1) [Victoria Directa]",
        "odds": 1.20,
        "confidence": 83.3,
        "status": "win",
        "diagnostic": "TRIUNFO DE LOS VILLANOS (3 - 1): Unai Emery impuso condiciones en Villa Park; Viking descontó pero no pudo frenar la potencia de Watkins y Rogers.",
        "pnl": 20.0
    },
    {
        "id": last_id + 4,
        "match": "Inter Milan vs Shakhtar Donetsk",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 1 - 0",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Inter de Milán o Empate (1X) [Doble Oportunidad]",
        "odds": 1.08,
        "confidence": 93.4,
        "status": "win",
        "diagnostic": "VICTORIA SUFRIDA NERAZZURRA (1 - 0): Tal como anticipó el usuario, el Inter jugó con ansiedad por sus 0 puntos, pero un gol solitario de Lautaro bastó para asegurar el 1X.",
        "pnl": 8.0
    },
    {
        "id": last_id + 5,
        "match": "Bayern Munich vs Arsenal",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 2 - 2",
        "category_tag": "Ambos Equipos Anotan (BTTS)",
        "is_fija": False,
        "selection": "Ambos Equipos Anotan: Sí [BTTS]",
        "odds": 1.58,
        "confidence": 72.5,
        "status": "win",
        "diagnostic": "PARTIDAZO DE PODER A PODER (2 - 2): Harry Kane y Saka cumplieron con el pronóstico ofensivo del modelo en el Allianz Arena.",
        "pnl": 58.0
    },
    {
        "id": last_id + 6,
        "match": "Como vs Manchester United",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 4 - 1",
        "category_tag": "Doble Oportunidad",
        "is_fija": False,
        "selection": "Empate o Manchester United (X2) [Doble Oportunidad]",
        "odds": 1.28,
        "confidence": 77.5,
        "status": "loss",
        "diagnostic": "HUMILLACIÓN EN ITALIA (4 - 1): Cesc Fàbregas destrozó al Manchester United en el Giuseppe Sinigaglia. Nuevo colapso del United como visitante europeo.",
        "pnl": -100.0
    },
    {
        "id": last_id + 7,
        "match": "Boleto Doble de Oro Usuario (Real Madrid + Sporting Lisboa)",
        "tournament": "Ecuabet • Miércoles 21/10/2026 • Boleto Combinado Real del Usuario",
        "category_tag": "👑 Boleto Maestro Usuario Ecuabet",
        "is_fija": True,
        "selection": "Real Madrid Gana (@1.27) + Sporting Lisboa Gana (@1.20) [Cuota 1.52]",
        "odds": 1.52,
        "confidence": 84.5,
        "status": "loss",
        "diagnostic": "PÉRDIDA REAL DE $10.00 USD: Real Madrid cumplió aplastando 4-1, pero la insólita derrota del Sporting 2-3 ante LASK Linz echó abajo la combinada. La prudencia del usuario de apostar solo $10 evitó una pérdida mayor de $20 o $50.",
        "pnl": -100.0
    }
]

for p in wednesday_audits:
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

# 2. Actualizar autonomous_feedback_log.json con Ciclo #115
print("\n2. Actualizando autonomous_feedback_log.json con Ciclo #115...")
with open(feedback_file, "r", encoding="utf-8") as f:
    fb_db = json.load(f)

calibrations = fb_db.get("calibrations", [])

new_cycle = {
    "cycle": 115,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "action": "AUTOPSIA CRÍTICA #11: EL DESCALABRO DE LISBOA (SPORTING 2-3 LASK A CUOTA 1.20) & PÉRDIDA DE $10 USD DEL USUARIO",
    "observations": [
        "[RECONOCIMIENTO TOTAL DE PÉRDIDA REAL (-$10.00 USD)]: La combinada Real Madrid 4-1 + Sporting Lisboa 2-3 se perdió por culpa exclusiva de la derrota del Sporting en casa. El usuario tenía $83 USD y baja a $73 USD.",
        "[SALVACIÓN POR PRUDENCIA DEL USUARIO]: El usuario decidió con sabiduría apostar $10 en lugar de los $20 planeados originalmente ('aguanta soy gei mejor apostemos 10 nomas'). Esta gestión de riesgo evitó una pérdida de $20 y mantiene la banca en $73 USD (aún con balance positivo frente a los $70 iniciales).",
        "[AUTOPSIA TÁCTICA DEL FALLO EN SPORTING CP 2-3 LASK]: Sporting pagaba 1.20 frente a cuota 12.00 de LASK Linz. El modelo subestimó la fragilidad defensiva del Sporting ante transiciones verticales directas de equipos centroeuropeos.",
        "[LA DISPARIDAD DE JERARQUÍA EN CUOTAS BAJAS]: Real Madrid en el Bernabéu ratificó su 1.27 con un 4-1 contundente. Los equipos fuera del Top 4 europeo (como Sporting en Portugal) sufren descompresión y exceso de confianza cuando juegan como súper favoritos en Champions.",
        "[NUEVA REGLA MATEMÁTICA Y CALIBRACIÓN #115]: Se penaliza la selección de victorias directas de equipos de ligas secundarias europeas (Portugal, Países Bajos, Turquía) como Fijas si la cuota es menor a 1.25. En estos casos se exigirá cobertura DNB o Doble Oportunidad si el rival tiene juego físico directo.",
        f"[MÉTRICAS OFICIALES ACTUALIZADAS TRAS PÉRDIDA]: Win Rate Global ajustado a {win_rate}% ({wins}/{total_picks}) | Win Rate Fijas ajustado a {fijas_win_rate}% ({fijas_wins}/{fijas_total}) | Racha rota (reinicia a {streak}) | Brier Score: {brier_score}."
    ],
    "system_health": f"En Alerta / Calibrado Post-Fallo (Win Rate Fijas: {fijas_win_rate}% [{fijas_wins}/{fijas_total}] | Win Rate Global: {win_rate}% [{wins}/{total_picks}] | Ciclo #115)"
}

calibrations.append(new_cycle)
fb_db["calibrations"] = calibrations
fb_db["cycles_completed"] = 115
fb_db["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(feedback_file, "w", encoding="utf-8") as f:
    json.dump(fb_db, f, ensure_ascii=False, indent=2)

print("✓ autonomous_feedback_log.json actualizado con Ciclo #115.")
