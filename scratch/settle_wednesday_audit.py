import json
import os

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
audit_file = os.path.join(base_dir, "sports_agents", "audit_history.json")
feedback_file = os.path.join(base_dir, "sports_agents", "autonomous_feedback_log.json")

# 1. ACTUALIZAR AUDIT_HISTORY CON MIÉRCOLES 14/10
with open(audit_file, "r", encoding="utf-8") as f:
    audit_data = json.load(f)

history = audit_data["history"]

# Truncar si existieran filas mayores a 96
history = history[:96]

wed_rows = [
    {
        "id": 97,
        "match": "Manchester City vs Paris Saint-Germain",
        "tournament": "UEFA Champions League &bull; Miércoles 14/10/2026 &bull; Final: 2 - 4",
        "category_tag": "👑 La Fija (95%+)",
        "is_fija": True,
        "selection": "Manchester City o Empate (1X) [Doble Oportunidad]",
        "odds": 1.14,
        "confidence": 95.0,
        "status": "loss",
        "diagnostic": "FALLO: Manchester City cayó 2-4 en el Etihad Stadium ante un PSG letal al contragolpe (Doué, Dembélé, Vitinha, Akliouche). Pese al doblete de Haaland, el repliegue defensivo citizen colapsó.",
        "pnl": -100.0
    },
    {
        "id": 98,
        "match": "AS Roma vs Real Madrid",
        "tournament": "UEFA Champions League &bull; Miércoles 14/10/2026 &bull; Final: 3 - 4",
        "category_tag": "👑 La Fija (95%+)",
        "is_fija": True,
        "selection": "Empate o Real Madrid (X2) [Doble Oportunidad]",
        "odds": 1.14,
        "confidence": 96.0,
        "status": "win",
        "diagnostic": "ACIERTO AGÓNICO: Real Madrid de José Mourinho remontó un 3-1 en contra para vencer 3-4 a la Roma en el Stadio Olimpico con gol heroico de Antonio Rüdiger. El escudo X2 cumplió.",
        "pnl": 14.0
    },
    {
        "id": 99,
        "match": "LASK vs Liverpool",
        "tournament": "UEFA Champions League &bull; Miércoles 14/10/2026 &bull; Final: 3 - 6",
        "category_tag": "👑 La Fija (95%+)",
        "is_fija": True,
        "selection": "Empate o Liverpool (X2) [Doble Oportunidad]",
        "odds": 1.14,
        "confidence": 95.0,
        "status": "win",
        "diagnostic": "ACIERTO: Festival goleador en Linz (3-6) con triplete de Bradley Barcola; el Liverpool aseguró la Doble Oportunidad X2 con comodidad.",
        "pnl": 14.0
    },
    {
        "id": 100,
        "match": "Bodø/Glimt vs Borussia Dortmund",
        "tournament": "UEFA Champions League &bull; Miércoles 14/10/2026 &bull; Final: 1 - 0",
        "category_tag": "👑 La Fija (95%+)",
        "is_fija": True,
        "selection": "Empate o Borussia Dortmund (X2) [Doble Oportunidad]",
        "odds": 1.14,
        "confidence": 96.8,
        "status": "loss",
        "diagnostic": "FALLO CATASTRÓFICO: Bodø/Glimt dio el gran golpe en Noruega al vencer 1-0 a Borussia Dortmund (gol de Sjøvold 52'). El césped sintético ártico y el clima polar volvieron a congelar al favorito alemán, ratificando la advertencia del usuario.",
        "pnl": -100.0
    },
    {
        "id": 101,
        "match": "Aston Villa vs Fenerbahçe",
        "tournament": "UEFA Champions League &bull; Miércoles 14/10/2026 &bull; Final: 6 - 0",
        "category_tag": "👑 La Fija (95%+)",
        "is_fija": True,
        "selection": "Aston Villa o Empate (1X) [Doble Oportunidad]",
        "odds": 1.14,
        "confidence": 96.8,
        "status": "win",
        "diagnostic": "ACIERTO ROTUNDO: Paliza histórica 6-0 de Unai Emery en Villa Park; el cerrojo de Doble Oportunidad 1X se cubrió con margen abrumador.",
        "pnl": 14.0
    },
    {
        "id": 102,
        "match": "Feyenoord vs Como",
        "tournament": "UEFA Champions League &bull; Miércoles 14/10/2026 &bull; Final: 3 - 2",
        "category_tag": "👑 La Fija (95%+)",
        "is_fija": True,
        "selection": "Feyenoord o Empate (1X) [Doble Oportunidad]",
        "odds": 1.14,
        "confidence": 96.8,
        "status": "win",
        "diagnostic": "ACIERTO: Feyenoord superó 3-2 al combativo Como en De Kuip, sellando la Doble Oportunidad 1X.",
        "pnl": 14.0
    }
]

history.extend(wed_rows)
audit_data["history"] = history

total_matches = len(history)
wins = sum(1 for r in history if r["status"] == "win")
losses = sum(1 for r in history if r["status"] == "loss")
global_wr = round((wins / total_matches) * 100, 1)

fijas = [r for r in history if r.get("is_fija")]
fijas_total = len(fijas)
fijas_wins = sum(1 for r in fijas if r["status"] == "win")
fijas_losses = sum(1 for r in fijas if r["status"] == "loss")
fijas_wr = round((fijas_wins / fijas_total) * 100, 1)

# Racha activa al final del miércoles:
streak = 0
for r in reversed(history):
    if r["status"] == "win":
        streak += 1
    else:
        break

total_pnl = round(sum(r["pnl"] for r in history), 2)
initial_bankroll = 1000.0
current_bankroll = round(initial_bankroll + total_pnl, 2)
roi = round((total_pnl / initial_bankroll) * 100, 1)

audit_data["global_stats"] = {
    "total": total_matches,
    "wins": wins,
    "losses": losses,
    "win_rate": global_wr
}
audit_data["fija_stats"] = {
    "total": fijas_total,
    "wins": fijas_wins,
    "losses": fijas_losses,
    "win_rate": fijas_wr,
    "active_streak": streak
}
audit_data["bankroll"] = {
    "initial": initial_bankroll,
    "current": current_bankroll,
    "profit": total_pnl,
    "roi": roi
}

with open(audit_file, "w", encoding="utf-8") as f:
    json.dump(audit_data, f, indent=2, ensure_ascii=False)

print(f"Audit Miércoles liquidado: Global {global_wr}% ({wins}/{total_matches}), Fijas {fijas_wr}% ({fijas_wins}/{fijas_total}), Racha {streak}, Bankroll ${current_bankroll}")

# 2. ACTUALIZAR FEEDBACK LOG CON CICLO #82
with open(feedback_file, "r", encoding="utf-8") as f:
    feedback_data = json.load(f)

feedback_data["cycles_completed"] = 82
feedback_data["last_updated"] = "2026-10-14 22:00:00"

c82 = {
    "cycle": 82,
    "timestamp": "2026-10-14 22:00:00",
    "action": "Auditoría Real Miércoles 14/10 Champions League & Calibración Jueves 15/10 Europa/Conference League",
    "status": "CRITICAL_POST_MORTEM_WEDNESDAY",
    "observations": [
        "[AUDITORÍA REAL MIÉRCOLES 14/10 - 4/6 ACIERTOS / 2 FALLOS]: Ganaron Roma-Madrid (3-4), LASK-Liverpool (3-6), Aston Villa-Fenerbahçe (6-0) y Feyenoord-Como (3-2). Cayeron Man City (2-4 vs PSG) y Borussia Dortmund (0-1 en Noruega ante Bodø/Glimt). Racha activa: 2 aciertos.",
        "[FALLO 1 - LA TRAMPA NÓRDICA CONFIRMADA (BODØ/GLIMT 1-0 DORTMUND)]: El usuario advirtió repetidamente sobre el frío y las canchas de Noruega. El modelo cometió el error garrafal de poner a Dortmund X2 como 'Fija de Oro'. En el círculo polar ártico y sobre césped sintético, Bodø/Glimt anuló al Dortmund y ganó 1-0. VETO PERMANENTE a poner Fijas de Oro en visitas al norte de Europa en césped artificial.",
        "[FALLO 2 - MANCHESTER CITY 2-4 PSG]: El usuario desconfió del City y prefirió sacarlo del boleto. El PSG desnudó las debilidades en transición rápida del City y se puso 0-3 en el primer tiempo. El modelo sobreponderó el mito de la localía en el Etihad.",
        "[ÉXITO DEL USUARIO - RECUPERACIÓN DE $50 A ~$70]: El usuario apostó con cabeza $35 a cuota @1.51 con Aston Villa 1X (goleó 6-0) y Real Madrid X2 (remontó 3-4 de la mano de Mourinho y gol de Rüdiger), guardando $15 de reserva y logrando su primer escalón de recuperación verde con ~$70 de saldo.",
        "[CARTELERA JUEVES 15/10 UEFA EUROPA LEAGUE & CONFERENCE LEAGUE]: 6 choques modelados (Benfica vs Celtic, Salzburg vs Milan, Celta vs Juventus, Poznań vs Leverkusen, Lyon vs Crystal Palace, Hajduk vs Ajax). Fija de Oro otorgada al Benfica en el Estádio da Luz (1X)."
    ],
    "adjustments": {
        "nordic_synthetic_pitch_ban": True,
        "away_fav_european_penalty": 0.25,
        "home_fortress_strict_threshold": 0.82
    },
    "metrics_snapshot": {
        "global_win_rate": global_wr,
        "fijas_win_rate": fijas_wr,
        "total_audited": total_matches,
        "fijas_total": fijas_total,
        "fijas_wins": fijas_wins,
        "fijas_losses": fijas_losses,
        "pnl_usd": total_pnl,
        "bankroll_usd": current_bankroll,
        "active_streak": streak
    }
}

feedback_data["calibrations"].append(c82)
if len(feedback_data["calibrations"]) > 50:
    feedback_data["calibrations"] = feedback_data["calibrations"][-50:]

with open(feedback_file, "w", encoding="utf-8") as f:
    json.dump(feedback_data, f, indent=2, ensure_ascii=False)

print("autonomous_feedback_log.json actualizado con Ciclo #82.")
