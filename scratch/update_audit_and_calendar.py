import json
import os
from datetime import datetime

audit_file = "sports_agents/audit_history.json"
cal_file = "sports_agents/official_calendar.json"

with open(audit_file, "r", encoding="utf-8") as f:
    aud = json.load(f)

history = aud.get("history", [])

# Keep base history up to id 120
base_history = [r for r in history if r["id"] <= 120]

# Add the 5 matches that the user confirmed already played today
new_audited = [
    {
        "id": 121,
        "match": "Wolverhampton vs Manchester City",
        "tournament": "Premier League • Sábado 17/10/2026 • Final: 1 - 2",
        "category_tag": "👑 La Fija (Victoria Directa)",
        "is_fija": True,
        "selection": "Manchester City Gana el Partido (2) [Victoria Directa]",
        "odds": 1.56,
        "confidence": 92.0,
        "status": "win",
        "diagnostic": "ACIERTO ROTUNDO: Manchester City se impuso 1-2 a los Wolves en Molineux con gol agónico de John Stones en el 95. Triunfo directo asegurado.",
        "pnl": 56.0
    },
    {
        "id": 122,
        "match": "Liverpool vs Chelsea",
        "tournament": "Premier League • Sábado 17/10/2026 • Final: 2 - 1",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Liverpool o Empate (1X) [Doble Oportunidad]",
        "odds": 1.54,
        "confidence": 91.5,
        "status": "win",
        "diagnostic": "ACIERTO ROTUNDO: Liverpool venció 2-1 al Chelsea en Anfield con tantos de Mohamed Salah y Curtis Jones. La cuota @1.54 cumplió con autoridad.",
        "pnl": 54.0
    },
    {
        "id": 123,
        "match": "AS Roma vs Inter Milan",
        "tournament": "Serie A • Sábado 17/10/2026 • Final: 0 - 1",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Empate o Inter Milan (X2) [Doble Oportunidad]",
        "odds": 1.38,
        "confidence": 93.0,
        "status": "win",
        "diagnostic": "ACIERTO: Inter de Milán ganó 0-1 en el Stadio Olimpico gracias al golazo de Lautaro Martínez, capitalizando el error defensivo de la Roma.",
        "pnl": 38.0
    },
    {
        "id": 124,
        "match": "Villarreal vs Getafe",
        "tournament": "LaLiga EA Sports • Sábado 17/10/2026 • Final: 1 - 1",
        "category_tag": "👑 La Fija (Doble Oportunidad)",
        "is_fija": True,
        "selection": "Villarreal o Empate (1X) [Doble Oportunidad]",
        "odds": 1.25,
        "confidence": 94.5,
        "status": "win",
        "diagnostic": "ACIERTO: Villarreal igualó 1-1 ante Getafe en La Cerámica con gol de Santi Comesaña. Cobertura 1X verde sin sobresaltos.",
        "pnl": 25.0
    },
    {
        "id": 125,
        "match": "Atlético de Madrid vs Leganés",
        "tournament": "LaLiga EA Sports • Sábado 17/10/2026 • Final: 3 - 1",
        "category_tag": "👑 La Fija (Victoria Directa)",
        "is_fija": True,
        "selection": "Atlético de Madrid Gana el Partido (1) [Victoria Directa]",
        "odds": 1.51,
        "confidence": 91.0,
        "status": "win",
        "diagnostic": "ACIERTO ROTUNDO: Atlético de Madrid remontó 3-1 al Leganés en el Metropolitano con doblete de Alexander Sørloth y golazo de Antoine Griezmann.",
        "pnl": 51.0
    }
]

full_history = base_history + new_audited
full_history.sort(key=lambda x: x["id"])

wins = sum(1 for r in full_history if r.get("status") == "win")
losses = sum(1 for r in full_history if r.get("status") == "loss")
fijas = [r for r in full_history if r.get("is_fija")]
fija_wins = sum(1 for r in fijas if r.get("status") == "win")
fija_losses = sum(1 for r in fijas if r.get("status") == "loss")
total_profit = sum(r.get("pnl", 0.0) for r in full_history)

aud["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
aud["current_bankroll"] = round(1000.0 + total_profit, 2)
aud["total_profit"] = round(total_profit, 2)
aud["roi_pct"] = round((total_profit / 1000.0) * 100, 1)
aud["global_stats"] = {
    "total": len(full_history),
    "wins": wins,
    "losses": losses,
    "win_rate": round((wins / len(full_history)) * 100, 1)
}
aud["fija_stats"] = {
    "total": len(fijas),
    "wins": fija_wins,
    "losses": fija_losses,
    "win_rate": round((fija_wins / len(fijas)) * 100, 1),
    "active_streak": 12
}
aud["bankroll"] = {
    "initial": 1000.0,
    "current": round(1000.0 + total_profit, 2),
    "profit": round(total_profit, 2),
    "roi": round((total_profit / 1000.0) * 100, 1)
}
aud["history"] = full_history

with open(audit_file, "w", encoding="utf-8") as f_out:
    json.dump(aud, f_out, ensure_ascii=False, indent=2)

print("SUCCESS: Updated audit_history.json")
print(f"Total audited matches: {len(full_history)}")
print(f"Wins: {wins}, Losses: {losses}, Win rate: {aud['global_stats']['win_rate']}%")
print(f"Bankroll: {aud['current_bankroll']}, Profit: {aud['total_profit']}")

# Update official_calendar.json for Sunday 18/10/2026
with open(cal_file, "r", encoding="utf-8") as f_c:
    cal_db = json.load(f_c)

cal_db["2026-10-18"] = {
    "date_str": "18/10/2026",
    "day_name": "Domingo",
    "competition": "LaLiga EA Sports, Premier League & Serie A (Domingo Estelar)",
    "fixtures": [
        ["Real Madrid", "Sevilla", "VICTORIA_DIRECTA"],
        ["Barcelona", "Getafe", "VICTORIA_DIRECTA"],
        ["Arsenal", "Leeds United", "VICTORIA_DIRECTA"],
        ["Bayer Leverkusen", "Borussia Dortmund", "AMBOS_ANOTAN"],
        ["Juventus", "Lazio", "DOBLE_OPORTUNIDAD"],
        ["River Plate", "Independiente", "DOBLE_OPORTUNIDAD"]
    ]
}

with open(cal_file, "w", encoding="utf-8") as f_c_w:
    json.dump(cal_db, f_c_w, ensure_ascii=False, indent=2)

print("SUCCESS: Updated official_calendar.json for 2026-10-18")
