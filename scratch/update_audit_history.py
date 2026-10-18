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

# Ensure no duplicate Real Madrid vs Sevilla in audit (it's tomorrow's match!)
history = [r for r in history if r.get("match") != "Real Madrid vs Sevilla"]

# Ensure Barcelona pick is present as id 127
has_barca = any(r.get("match") == "FC Barcelona vs Sevilla" for r in history)
if not has_barca:
    barca_entry = {
        "id": 127,
        "match": "FC Barcelona vs Sevilla",
        "tournament": "LaLiga EA Sports • Domingo 20/10/2024 • Final: 5 - 1",
        "category_tag": "👑 La Fija (Gana + Goles / Combo)",
        "is_fija": True,
        "selection": "FC Barcelona Gana y Más de 1.5 Goles totales",
        "odds": 1.40,
        "confidence": 88.5,
        "status": "win",
        "diagnostic": "ACIERTO ROTUNDO (Pick de Usuario Ratificado): FC Barcelona goleó 5-1 al Sevilla en Montjuïc (doblete de Lewandowski, doblete de Pablo Torre y golazo de Pedri). Lectura impecable del usuario respaldando Barcelona Gana + Más 1.5 goles (+$20.00 netos).",
        "pnl": 20.0
    }
    history.append(barca_entry)

# Ensure sequential IDs and sorting
history.sort(key=lambda x: x["id"])
for idx, r in enumerate(history, 1):
    r["id"] = idx

# Compute exact metrics
total = len(history)
wins = sum(1 for r in history if r.get("status") == "win")
losses = sum(1 for r in history if r.get("status") == "loss")
win_rate = round((wins / total) * 100, 1)

fijas = [r for r in history if r.get("is_fija")]
fija_total = len(fijas)
fija_wins = sum(1 for r in fijas if r.get("status") == "win")
fija_losses = sum(1 for r in fijas if r.get("status") == "loss")
fija_win_rate = round((fija_wins / fija_total) * 100, 1)

total_profit = round(sum(r.get("pnl", 0.0) for r in history), 2)
initial_bankroll = 1000.0
current_bankroll = round(initial_bankroll + total_profit, 2)
roi_pct = round((total_profit / initial_bankroll) * 100, 1)

# Brier score calculation
brier_sum = sum((float(r.get("confidence", 75.0)) / 100.0 - (1.0 if r.get("status") == "win" else 0.0)) ** 2 for r in history)
brier_score = round(brier_sum / total, 4)

# Active streak
streak = 0
for r in reversed(history):
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

aud["history"] = history

with open(audit_file, "w", encoding="utf-8") as f_out:
    json.dump(aud, f_out, ensure_ascii=False, indent=2)

print(f"✓ audit_history.json actualizado con {total} pronósticos.")
print(f"  Win Rate Global: {win_rate}% ({wins}W / {losses}L)")
print(f"  Win Rate Fijas: {fija_win_rate}% ({fija_wins}W / {fija_losses}L)")
print(f"  Brier Score Real: {brier_score}")
print(f"  Bankroll: ${current_bankroll} (Profit: ${total_profit}, ROI: {roi_pct}%)")
print(f"  Racha Activa: {streak} aciertos")
