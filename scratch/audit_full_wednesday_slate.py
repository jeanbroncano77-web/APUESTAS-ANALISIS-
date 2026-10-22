# -*- coding: utf-8 -*-
"""
audit_full_wednesday_slate.py
Liquida y audita absolutamente TODOS los partidos y fijas de la cartelera del Miércoles 21/10/2026:
1. Real Madrid 4 - 1 RB Leipzig -> Real Madrid Gana @ 1.27 -> WIN
2. Sporting CP 2 - 3 LASK Linz -> Sporting Gana @ 1.20 -> LOSS [FALLO #1]
3. Aston Villa 3 - 1 Viking FK -> Aston Villa Gana @ 1.20 -> WIN
4. Inter Milan 1 - 0 Shakhtar Donetsk -> Inter 1X @ 1.08 -> WIN
5. Bayern Munich 2 - 2 Arsenal -> Ambos Marcan @ 1.58 -> WIN
6. Como 4 - 1 Manchester United -> Man United X2 @ 1.28 -> LOSS [FALLO #2]
7. Real Betis 1 - 0 Feyenoord -> Real Betis 1X @ 1.30 -> WIN
8. Club Brujas 3 - 0 RC Lens -> Club Brujas 1X @ 1.25 -> WIN
9. LOSC Lille 2 - 4 Galatasaray -> Más de 2.5 / BTTS @ 1.65 -> WIN
10. Boleto Maestro Ecuabet Usuario (Madrid + Sporting) @ 1.52 -> LOSS (-$10 real)

Calcula el Win Rate global y de la jornada completa, actualizando audit_history.json
y autonomous_feedback_log.json (Ciclo #116 - "Ponte Venus").
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

# Limpiar posibles duplicados de miércoles si existieran arriba de 149
history = [p for p in history if p["id"] <= 149]

wednesday_all_picks = [
    {
        "id": 150,
        "match": "Real Madrid vs RB Leipzig",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 4 - 1",
        "category_tag": "👑 La Fija (Victoria Directa)",
        "is_fija": True,
        "selection": "Real Madrid Gana el Partido (1) [Victoria Directa]",
        "odds": 1.27,
        "confidence": 78.7,
        "status": "win",
        "diagnostic": "FIESTA BLANCA EN EL BERNABÉU (4 - 1): Mbappé con doblete y Vinícius Jr. confirmaron la supremacía del Madrid en noche de Champions League.",
        "pnl": 27.0
    },
    {
        "id": 151,
        "match": "Sporting de Lisboa vs LASK Linz",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 2 - 3",
        "category_tag": "👑 La Fija (Victoria Directa)",
        "is_fija": True,
        "selection": "Sporting de Lisboa Gana el Partido (1) [Victoria Directa]",
        "odds": 1.20,
        "confidence": 82.0,
        "status": "loss",
        "diagnostic": "BATACAZO HISTÓRICO Y ERROR CRÍTICO (2 - 3): LASK Linz (que pagaba cuota 12.00) sorprendió con transiciones letales y castigó la pasividad defensiva del Sporting en el José Alvalade. Fallo directo de complacencia que arruinó la combinada del usuario.",
        "pnl": -100.0
    },
    {
        "id": 152,
        "match": "Aston Villa vs Viking FK",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 3 - 1",
        "category_tag": "👑 La Fija (Victoria Directa)",
        "is_fija": True,
        "selection": "Aston Villa Gana el Partido (1) [Victoria Directa]",
        "odds": 1.20,
        "confidence": 83.3,
        "status": "win",
        "diagnostic": "TRIUNFO DE LOS VILLANOS (3 - 1): Unai Emery impuso condiciones en Villa Park; Viking descontó pero no pudo frenar la potencia física de Watkins y Rogers.",
        "pnl": 20.0
    },
    {
        "id": 153,
        "match": "Inter Milan vs Shakhtar Donetsk",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 1 - 0",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Inter de Milán o Empate (1X) [Doble Oportunidad]",
        "odds": 1.08,
        "confidence": 93.4,
        "status": "win",
        "diagnostic": "VICTORIA SUFRIDA NERAZZURRA (1 - 0): Tal como anticipó el usuario, el Inter jugó con ansiedad por sus 0 puntos, pero Lautaro Martínez anotó el gol decisivo en San Siro.",
        "pnl": 8.0
    },
    {
        "id": 154,
        "match": "Bayern Munich vs Arsenal",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 2 - 2",
        "category_tag": "Ambos Equipos Anotan (BTTS)",
        "is_fija": False,
        "selection": "Ambos Equipos Anotan: Sí [BTTS]",
        "odds": 1.58,
        "confidence": 72.5,
        "status": "win",
        "diagnostic": "PARTIDAZO DE PODER A PODER (2 - 2): Harry Kane y Saka cumplieron con el pronóstico ofensivo del modelo en el Allianz Arena en un choque eléctrico.",
        "pnl": 58.0
    },
    {
        "id": 155,
        "match": "Como vs Manchester United",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 4 - 1",
        "category_tag": "Doble Oportunidad",
        "is_fija": False,
        "selection": "Empate o Manchester United (X2) [Doble Oportunidad]",
        "odds": 1.28,
        "confidence": 77.5,
        "status": "loss",
        "diagnostic": "HUMILLACIÓN EN ITALIA (4 - 1): Cesc Fàbregas destrozó tácticamente al Manchester United en el Giuseppe Sinigaglia. Nuevo colapso del United como visitante europeo.",
        "pnl": -100.0
    },
    {
        "id": 156,
        "match": "Real Betis vs Feyenoord",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 1 - 0",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Real Betis o Empate (1X) [Doble Oportunidad]",
        "odds": 1.30,
        "confidence": 79.0,
        "status": "win",
        "diagnostic": "MAGIA DE ISCO EN EL VILLAMARÍN (1 - 0): Real Betis dominó el trámite ante Feyenoord y aseguró la victoria con gol de Isco al minuto 68.",
        "pnl": 30.0
    },
    {
        "id": 157,
        "match": "Club Brujas vs RC Lens",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 3 - 0",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Club Brujas o Empate (1X) [Doble Oportunidad]",
        "odds": 1.25,
        "confidence": 81.5,
        "status": "win",
        "diagnostic": "AUTORIDAD BELGA (3 - 0): Brujas confirmó su momento dulce en Champions pasando por encima del RC Lens francés en el Estadio Jan Breydel.",
        "pnl": 25.0
    },
    {
        "id": 158,
        "match": "LOSC Lille vs Galatasaray",
        "tournament": "UEFA Champions League • Miércoles 21/10/2026 • Final: 2 - 4",
        "category_tag": "Goles Más de 2.5 & BTTS",
        "is_fija": False,
        "selection": "Ambos Equipos Anotan: Sí [BTTS]",
        "odds": 1.65,
        "confidence": 75.0,
        "status": "win",
        "diagnostic": "FESTIVAL DE 6 GOLES (2 - 4): Galatasaray sorprendió a Lille en Francia en un duelo frenético de ida y vuelta que cumplió con holgura el pronóstico de goles.",
        "pnl": 65.0
    },
    {
        "id": 159,
        "match": "Boleto Doble de Oro Usuario Ecuabet (Real Madrid + Sporting)",
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

for p in wednesday_all_picks:
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

# Estadísticas de la jornada de Miércoles 21/10
wed_singles = [p for p in wednesday_all_picks if p["id"] < 159]
wed_wins = sum(1 for p in wed_singles if p["status"] == "win")
wed_losses = sum(1 for p in wed_singles if p["status"] == "loss")
wed_win_rate = round((wed_wins / len(wed_singles)) * 100, 1)

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
print(f"✓ Jornada Miércoles 21/10 (9 partidos): {wed_wins} Aciertos / {wed_losses} Fallos ({wed_win_rate}% Win Rate)")

# 2. Actualizar autonomous_feedback_log.json con Ciclo #116 ("Ponte Venus")
print("\n2. Actualizando autonomous_feedback_log.json con Ciclo #116 ('Ponte Venus')...")
with open(feedback_file, "r", encoding="utf-8") as f:
    fb_db = json.load(f)

calibrations = fb_db.get("calibrations", [])

new_cycle = {
    "cycle": 116,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "action": "AUTOAPRENDIZAJE INTEGRAL 'PONTE VENUS' (AUDITORÍA TOTAL DE LOS 9 PARTIDOS DE CHAMPIONS MIÉRCOLES 21/10)",
    "observations": [
        f"[BALANCE COMPLETO DE LA CARTELERA DEL MIÉRCOLES (9 PARTIDOS)]: {wed_wins} Aciertos y {wed_losses} Fallos ({wed_win_rate}% de efectividad en la jornada). Salieron 7 de 9 pronósticos individuales.",
        "[LOS 7 ACIERTOS INDIVIDUALES DE LA JORNADA]: 1) Real Madrid 4-1 Leipzig (Gana Real Madrid @1.27); 2) Aston Villa 3-1 Viking (Gana Villa @1.20); 3) Inter 1-0 Shakhtar (Inter 1X @1.08); 4) Bayern 2-2 Arsenal (Ambos Marcan @1.58); 5) Betis 1-0 Feyenoord (Betis 1X @1.30); 6) Brujas 3-0 Lens (Brujas 1X @1.25); 7) Lille 2-4 Galatasaray (BTTS @1.65).",
        "[LOS 2 ÚNICOS FALLOS DE LA JORNADA]: 1) Sporting CP 2-3 LASK (Fallo Crítico: Sporting a cuota 1.20 cayó de local ante LASK a cuota 12.00); 2) Como 4-1 Manchester United (Fallo Secundario: Man United colapsó de visita ante el equipo de Fàbregas).",
        "[LA TRAGEDIA DE LA COMBINADA Y LA PARADOJA DEL PARLEY]: De 9 partidos salieron 7. Si en la combinada del usuario se hubiera mantenido a Aston Villa (3-1), Inter (1-0), o Bayern Ambos Marcan (2-2), el boleto habría sido verde. Pero el fútbol castiga en las combinadas: un solo tropiezo (Sporting 2-3) tumba todo el boleto.",
        "[LECCIÓN Y NUEVA REGLA MATEMÁTICA 'PONTE VENUS' #116]: 1) Prohibición de cuotas < 1.25 en victoria directa de equipos portugueses o de ligas intermedias (Portugal, Países Bajos, Bélgica) en Champions League; 2) Blindaje obligatorio con DNB o Doble Oportunidad si el rival centroeuropeo juega a la contra; 3) El usuario salvó capital reduciendo a $10, dejando la banca en $73 USD.",
        f"[MÉTRICAS OFICIALES GENERALES]: Win Rate Global: {win_rate}% ({wins}/{total_picks}) | Win Rate Fijas: {fijas_win_rate}% ({fijas_wins}/{fijas_total}) | Brier Score: {brier_score}."
    ],
    "system_health": f"Calibración Exhaustiva 'Ponte Venus' (Win Rate Fijas: {fijas_win_rate}% [{fijas_wins}/{fijas_total}] | Win Rate Global: {win_rate}% [{wins}/{total_picks}] | Ciclo #116)"
}

calibrations.append(new_cycle)
fb_db["calibrations"] = calibrations
fb_db["cycles_completed"] = 116
fb_db["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(feedback_file, "w", encoding="utf-8") as f:
    json.dump(fb_db, f, ensure_ascii=False, indent=2)

print("✓ autonomous_feedback_log.json actualizado con Ciclo #116 ('Ponte Venus').")
