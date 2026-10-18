import os
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
audit_file = os.path.join(base_dir, "sports_agents", "audit_history.json")

with open(audit_file, "r", encoding="utf-8") as f:
    aud = json.load(f)

history = aud.get("history", [])

# Check if Barcelona is already there
has_barca = any("Barcelona" in r.get("match", "") for r in history)
print(f"Has Barcelona currently: {has_barca}")

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
        "diagnostic": "ACIERTO ROTUNDO: FC Barcelona goleó 5-1 al Sevilla en Montjuïc (dobletes de Robert Lewandowski y Pablo Torre, golazo de Pedri). Lectura certera del usuario apostando a la victoria con más de 1.5 goles (+$20.00 netos).",
        "pnl": 20.0
    }
    history.append(barca_entry)

# Compute true metrics
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

# Compute Brier score
brier_sum = 0.0
for r in history:
    p = float(r.get("confidence", 75.0)) / 100.0
    y = 1.0 if r.get("status") == "win" else 0.0
    brier_sum += (p - y) ** 2

brier_score = round(brier_sum / total, 4)

# Categories breakdown
cat_stats = {}
for r in history:
    tag = r.get("category_tag", "Otros")
    # Simplify category
    cat = "Otros"
    if "1X2" in tag or "Victoria Directa" in tag:
        cat = "Victoria Directa (1X2)"
    elif "Doble Oportunidad" in tag or "1X" in tag or "X2" in tag:
        cat = "Doble Oportunidad (1X/X2)"
    elif "Goles" in tag or "Over" in tag or "Under" in tag or "Más de" in tag or "Menos de" in tag:
        cat = "Líneas de Goles (Over/Under)"
    elif "Ambos Anotan" in tag or "BTTS" in tag:
        cat = "Ambos Equipos Anotan (BTTS)"
    elif "Tarjeta" in tag:
        cat = "Tarjetas & Disciplina"
    elif "Córner" in tag or "Corner" in tag:
        cat = "Córners Totales"
    elif "Remate" in tag or "Tiro" in tag or "Prop" in tag:
        cat = "Props de Jugador"
    elif "Combo" in tag or "Gana +" in tag:
        cat = "Combos Seguros (1X2 + Goles)"

    if cat not in cat_stats:
        cat_stats[cat] = {"total": 0, "wins": 0, "losses": 0, "profit": 0.0}
    cat_stats[cat]["total"] += 1
    if r.get("status") == "win":
        cat_stats[cat]["wins"] += 1
    else:
        cat_stats[cat]["losses"] += 1
    cat_stats[cat]["profit"] = round(cat_stats[cat]["profit"] + r.get("pnl", 0.0), 2)

for c, s in cat_stats.items():
    s["win_rate"] = round((s["wins"] / s["total"]) * 100, 1)

print(f"Total: {total}, Wins: {wins}, Losses: {losses}, Win Rate: {win_rate}%")
print(f"Fijas Total: {fija_total}, Fijas Wins: {fija_wins}, Fijas Win Rate: {fija_win_rate}%")
print(f"Bankroll: ${current_bankroll}, Profit: ${total_profit}, ROI: {roi_pct}%")
print(f"Global Brier Score: {brier_score}")
print("\nCategory Breakdown:")
for c, s in sorted(cat_stats.items(), key=lambda x: x[1]['total'], reverse=True):
    print(f" - {c}: {s['wins']}/{s['total']} ({s['win_rate']}%) | PnL: ${s['profit']:+.2f}")
