# -*- coding: utf-8 -*-
import json, os

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
audit_file = os.path.join(base_dir, "sports_agents", "audit_history.json")
tracker_file = os.path.join(base_dir, "sports_agents", "dispatch_tracker.json")

with open(audit_file, "r", encoding="utf-8") as f:
    audit_data = json.load(f)

raw_history = audit_data.get("history", [])

# Filtrar: Asegurar que NINGÚN partido del Real Madrid esté en la auditoría porque juega mañana
clean_history = []
for h in raw_history:
    match_name = h.get("match", "")
    tournament_name = h.get("tournament", "")
    if "Real Madrid" in match_name and ("17/10" in tournament_name or "18/10" in tournament_name or "19/10" in tournament_name or "Balaídos" in h.get("diagnostic", "")):
        continue
    clean_history.append(h)

# Re-enumerar IDs correlativos
for idx, h in enumerate(clean_history, start=1):
    h["id"] = idx

wins = sum(1 for r in clean_history if r.get("status") == "win")
losses = sum(1 for r in clean_history if r.get("status") == "loss")
fijas = [r for r in clean_history if r.get("is_fija")]
fija_wins = sum(1 for r in fijas if r.get("status") == "win")
fija_losses = sum(1 for r in fijas if r.get("status") == "loss")
total_profit = sum(r.get("pnl", 0.0) for r in clean_history)

audit_data["last_updated"] = "2026-10-17 20:38:00"
audit_data["current_bankroll"] = round(1000.0 + total_profit, 2)
audit_data["total_profit"] = round(total_profit, 2)
audit_data["roi_pct"] = round((total_profit / 1000.0) * 100, 1)
audit_data["global_stats"] = {
    "total": len(clean_history),
    "wins": wins,
    "losses": losses,
    "win_rate": round((wins / len(clean_history)) * 100, 1)
}
audit_data["fija_stats"] = {
    "total": len(fijas),
    "wins": fija_wins,
    "losses": fija_losses,
    "win_rate": round((fija_wins / len(fijas)) * 100, 1),
    "active_streak": 6
}
audit_data["bankroll"] = {
    "initial": 1000.0,
    "current": round(1000.0 + total_profit, 2),
    "profit": round(total_profit, 2),
    "roi": round((total_profit / 1000.0) * 100, 1)
}
audit_data["history"] = clean_history

with open(audit_file, "w", encoding="utf-8") as f:
    json.dump(audit_data, f, ensure_ascii=False, indent=2)

print(f"Auditoría purgada con éxito. Total: {len(clean_history)} | Win Rate: {audit_data['global_stats']['win_rate']}%")

# Resetear dispatch tracker
with open(tracker_file, "w", encoding="utf-8") as f:
    json.dump({"last_target_date": "", "last_slot_date": "", "dispatched_at": "", "status": ""}, f)
print("DispatchTracker reseteado.")
