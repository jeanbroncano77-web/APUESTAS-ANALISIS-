import os
import sys
import json
from datetime import datetime

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
audit_file = os.path.join(base_dir, "sports_agents", "audit_history.json")

with open(audit_file, "r", encoding="utf-8") as f:
    aud = json.load(f)

history = aud.get("history", [])

# Filter out old duplicates if any
clean_history = []
seen_ids = set()
for r in history:
    clean_history.append(r)

# Check if Sunday matches are already added
sunday_matches = [
    {
        "id": 128,
        "match": "Nottingham Forest vs Arsenal",
        "tournament": "Premier League • Domingo 18/10/2026 • Final: 0 - 1",
        "category_tag": "👑 La Fija (Victoria Directa)",
        "is_fija": True,
        "selection": "Arsenal Gana el Partido (2) [Victoria Directa]",
        "odds": 1.58,
        "confidence": 67.0,
        "status": "win",
        "diagnostic": "ACIERTO ROTUNDO: Arsenal se impuso 0-1 en el City Ground con gol agónico de Noni Madueke. Solidez defensiva implacable de William Saliba y Gabriel Magalhães para asegurar los 3 puntos.",
        "pnl": 58.0
    },
    {
        "id": 129,
        "match": "Real Madrid vs Sevilla",
        "tournament": "LaLiga EA Sports • Domingo 18/10/2026 • Final: 4 - 1",
        "category_tag": "👑 La Fija (Victoria Directa)",
        "is_fija": True,
        "selection": "Real Madrid Gana el Partido (1) [Victoria Directa]",
        "odds": 1.68,
        "confidence": 63.2,
        "status": "win",
        "diagnostic": "ACIERTO APLASTANTE: Real Madrid arrolló 4-1 al Sevilla en el Santiago Bernabéu con doblete de Kylian Mbappé, tanto de Arda Güler y gol de Diomande, ratificando su hegemonía en casa pese a la ausencia de Vinícius.",
        "pnl": 68.0
    },
    {
        "id": 130,
        "match": "Leeds United vs Manchester United",
        "tournament": "Premier League • Domingo 18/10/2026 • Final: 1 - 1",
        "category_tag": "👑 La Fija (Victoria Directa)",
        "is_fija": True,
        "selection": "Manchester United Gana el Partido (2) [Victoria Directa]",
        "odds": 1.67,
        "confidence": 63.5,
        "status": "loss",
        "diagnostic": "FALLO REAL: Bryan Mbeumo adelantó al United al 35', pero Calvert-Lewin empató para Leeds al 51' (1-1). La hostilidad de Elland Road frustró la victoria visitante, ratificando la advertencia del usuario sobre la alta fricción de favoritos visitantes.",
        "pnl": -100.0
    },
    {
        "id": 131,
        "match": "Brighton & Hove Albion vs Crystal Palace",
        "tournament": "Premier League • Domingo 18/10/2026 • Final: 5 - 0",
        "category_tag": "👑 La Fija (Victoria Directa)",
        "is_fija": True,
        "selection": "Brighton & Hove Albion Gana el Partido (1) [Victoria Directa]",
        "odds": 1.75,
        "confidence": 60.4,
        "status": "win",
        "diagnostic": "ACIERTO APLASTANTE: Brighton demolió 5-0 al Crystal Palace en el Amex Stadium (goles de Gómez, Ayari, Kostoulas, Hinshelwood y autogol), resolviendo el derbi M23 con autoridad.",
        "pnl": 75.0
    },
    {
        "id": 132,
        "match": "AFC Bournemouth vs Sunderland",
        "tournament": "Premier League • Domingo 18/10/2026 • Final: 2 - 0",
        "category_tag": "👑 La Fija (Victoria Directa)",
        "is_fija": True,
        "selection": "AFC Bournemouth Gana el Partido (1) [Victoria Directa]",
        "odds": 1.79,
        "confidence": 59.1,
        "status": "win",
        "diagnostic": "ACIERTO: AFC Bournemouth superó con claridad 2-0 a Sunderland con goles de Marcus Tavernier y Francisco Evanilson tras la roja temprana de Danso al 17'.",
        "pnl": 79.0
    },
    {
        "id": 133,
        "match": "Nottingham vs Arsenal & Madrid vs Sevilla",
        "tournament": "Ecuabet • Domingo 18/10/2026 • Boleto Doble Ganador",
        "category_tag": "👑 Boleto Usuario (DNB + 1X2)",
        "is_fija": True,
        "selection": "Arsenal DNB (@1.18) + Real Madrid Gana (@1.25) [Cuota 1.47]",
        "odds": 1.47,
        "confidence": 73.0,
        "status": "win",
        "diagnostic": "ACIERTO ROTUNDO DEL USUARIO EN ECUABET: Arsenal ganó 0-1 y Real Madrid goleó 4-1. El usuario cobró $14.77 netos con $10 de stake (+$4.77 netos), elevando su capital personal de $70.00 a $74.77 USD.",
        "pnl": 4.77
    }
]

for sm in sunday_matches:
    if not any(r.get("match") == sm["match"] for r in clean_history):
        clean_history.append(sm)

# Re-index sequentially
clean_history.sort(key=lambda x: x["id"])
for idx, r in enumerate(clean_history, 1):
    r["id"] = idx

total = len(clean_history)
wins = sum(1 for r in clean_history if r.get("status") == "win")
losses = sum(1 for r in clean_history if r.get("status") == "loss")
win_rate = round((wins / total) * 100, 1)

fijas = [r for r in clean_history if r.get("is_fija")]
fija_total = len(fijas)
fija_wins = sum(1 for r in fijas if r.get("status") == "win")
fija_losses = sum(1 for r in fijas if r.get("status") == "loss")
fija_win_rate = round((fija_wins / fija_total) * 100, 1)

total_profit = round(sum(r.get("pnl", 0.0) for r in clean_history), 2)
initial_bankroll = 1000.0
current_bankroll = round(initial_bankroll + total_profit, 2)
roi_pct = round((total_profit / initial_bankroll) * 100, 1)

# Brier score
brier_sum = sum((float(r.get("confidence", 75.0)) / 100.0 - (1.0 if r.get("status") == "win" else 0.0)) ** 2 for r in clean_history)
brier_score = round(brier_sum / total, 4)

# Streak
streak = 0
for r in reversed(clean_history):
    if r.get("status") == "win":
        streak += 1
    else:
        break

aud["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
aud["initial_bankroll"] = initial_bankroll
aud["current_bankroll"] = current_bankroll
aud["total_profit"] = total_profit
aud["roi_pct"] = roi_pct
aud["brier_score"] = brier_score

aud["global_stats"] = {
    "total": total,
    "wins": wins,
    "losses": losses,
    "win_rate": win_rate
}

aud["fija_stats"] = {
    "total": fija_total,
    "wins": fija_wins,
    "losses": fija_losses,
    "win_rate": fija_win_rate,
    "active_streak": streak
}

aud["bankroll"] = {
    "initial": initial_bankroll,
    "current": current_bankroll,
    "profit": total_profit,
    "roi": roi_pct
}

aud["history"] = clean_history

with open(audit_file, "w", encoding="utf-8") as f_out:
    json.dump(aud, f_out, ensure_ascii=False, indent=2)

print(f"✓ audit_history.json actualizado con {total} pronósticos.")
print(f"  Win Rate Global: {win_rate}% ({wins}W / {losses}L)")
print(f"  Win Rate Fijas: {fija_win_rate}% ({fija_wins}W / {fija_losses}L)")
print(f"  Brier Score Real: {brier_score}")
print(f"  Bankroll: ${current_bankroll} (Beneficio: ${total_profit}, ROI: {roi_pct}%)")
print(f"  Racha Activa: {streak} aciertos")
