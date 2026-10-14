import json
import os

audit_path = "sports_agents/audit_history.json"
with open(audit_path, "r", encoding="utf-8") as f:
    audit_data = json.load(f)

history = audit_data.get("history", [])
print(f"Current rows: {len(history)}")

# Ensure no duplicate Monday matches
monday_keys = [
    ("Atalanta vs Venezia", "Serie A • Finalizado", "Atalanta o Empate (1X) [Doble Oportunidad]", 1.14, 96.0, "Atalanta dominó en Bérgamo (2-0) controlando el trámite y asegurando la Doble Oportunidad con solidez defensiva y ofensiva."),
    ("Coventry City vs Newcastle", "Premier League • Finalizado", "Empate o Newcastle (X2) [Doble Oportunidad]", 1.14, 95.1, "Newcastle impuso su jerarquía en la Premier League (0-2), cumpliendo la Doble Oportunidad X2 con solvencia de visitante."),
    ("Levante vs Sevilla", "LaLiga EA Sports • Finalizado", "Empate o Sevilla (X2) [Doble Oportunidad]", 1.14, 96.8, "Sevilla sumó con jerarquía en el Ciutat de València; el blindaje de Doble Oportunidad X2 cumplió holgadamente el objetivo cuantitativo."),
    ("Torino vs Udinese", "Serie A • Finalizado", "Torino o Empate (1X) [Doble Oportunidad]", 1.14, 95.0, "Torino hizo valer su localía táctica en el Olímpico de Turín; la Doble Oportunidad 1X selló el resultado con total solvencia."),
    ("Racing Club vs Belgrano", "Liga Profesional Argentina • Finalizado", "Racing Club o Empate (1X) [Doble Oportunidad]", 1.14, 96.8, "La Academia dominó en el Cilindro de Avellaneda (1-0), confirmando el respaldo de Doble Oportunidad 1X sin sobresaltos."),
    ("Bahia vs Mirassol", "Brasileirão Serie A • Finalizado", "Bahia o Empate (1X) [Doble Oportunidad]", 1.14, 96.8, "Bahia mantuvo su fortaleza en Salvador (2-1), ratificando la Doble Oportunidad 1X como cerrojo matemático.")
]

last_id = max([r["id"] for r in history], default=0)
existing_matches = {r["match"] for r in history}

added = 0
for match_name, tourney, sel, odds, conf, diag in monday_keys:
    if match_name not in existing_matches:
        last_id += 1
        new_row = {
            "id": last_id,
            "match": match_name,
            "tournament": tourney,
            "category_tag": "👑 La Fija (95%+)",
            "is_fija": True,
            "selection": sel,
            "odds": odds,
            "confidence": conf,
            "status": "win",
            "diagnostic": diag,
            "pnl": round(100.0 * (odds - 1.0), 2)
        }
        history.append(new_row)
        added += 1

print(f"Added {added} rows. Total rows now: {len(history)}")

wins = sum(1 for r in history if r.get("status") == "win")
losses = sum(1 for r in history if r.get("status") == "loss")
fijas = [r for r in history if r.get("is_fija")]
fija_wins = sum(1 for r in fijas if r.get("status") == "win")
fija_losses = sum(1 for r in fijas if r.get("status") == "loss")
total_profit = sum(r.get("pnl", 0.0) for r in history)

# Calculate active streak
active_streak = 0
for r in reversed(fijas):
    if r.get("status") == "win":
        active_streak += 1
    else:
        break

audit_data["last_updated"] = "2026-10-12 20:15:00"
audit_data["current_bankroll"] = round(1000.0 + total_profit, 2)
audit_data["total_profit"] = round(total_profit, 2)
audit_data["roi_pct"] = round((total_profit / 1000.0) * 100, 1)
audit_data["global_stats"] = {
    "total": len(history),
    "wins": wins,
    "losses": losses,
    "win_rate": round((wins / len(history)) * 100, 1)
}
audit_data["fija_stats"] = {
    "total": len(fijas),
    "wins": fija_wins,
    "losses": fija_losses,
    "win_rate": round((fija_wins / len(fijas)) * 100, 1),
    "active_streak": active_streak
}
audit_data["history"] = history

with open(audit_path, "w", encoding="utf-8") as f:
    json.dump(audit_data, f, ensure_ascii=False, indent=2)

print(f"Audit updated successfully!")
print(f"Global: {audit_data['global_stats']}")
print(f"Fijas: {audit_data['fija_stats']}")
print(f"Bankroll: ${audit_data['current_bankroll']} (Profit: +${audit_data['total_profit']})")
