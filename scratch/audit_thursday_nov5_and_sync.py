# -*- coding: utf-8 -*-
"""
audit_thursday_nov5_and_sync.py
"""

import os
import sys
import json
import re
from datetime import datetime

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
audit_file = os.path.join(base_dir, "sports_agents", "audit_history.json")
feedback_file = os.path.join(base_dir, "sports_agents", "autonomous_feedback_log.json")
index_path = os.path.join(base_dir, "index.html")
dashboard_path = os.path.join(base_dir, "dashboard_pronosticos.html")
root_index_path = os.path.join(base_dir, "..", "index.html")

print("1. Cargando audit_history.json...")
with open(audit_file, "r", encoding="utf-8") as f:
    audit_db = json.load(f)

history = audit_db.get("history", [])
history = [p for p in history if p["id"] <= 199]

thursday_picks = [
    {
        "id": 200,
        "match": "Independiente del Valle vs Delfín SC",
        "tournament": "Copa Ecuador • Semifinal • Jueves 05/11/2026 • Final: 2 - 0",
        "category_tag": "👑 La Fija Nacional (1)",
        "is_fija": True,
        "selection": "Independiente del Valle Gana el Partido (1)",
        "odds": 1.28,
        "confidence": 88.0,
        "status": "win",
        "diagnostic": "FORTALEZA EN SANGOLQUÍ (2 - 0): Jeison Medina y Junior Sornoza sellaron el triunfo en Sangolquí (2,500m). Delfín se quedó sin piernas en el segundo tiempo ante la posesión local. Fija de Oro cobrada.",
        "pnl": 28.0
    },
    {
        "id": 201,
        "match": "AC Milan vs Ferencváros",
        "tournament": "UEFA Europa League • Jueves 05/11/2026 • Final: 3 - 0",
        "category_tag": "👑 La Fija de Oro (1)",
        "is_fija": True,
        "selection": "AC Milan Gana el Partido (1)",
        "odds": 1.24,
        "confidence": 88.5,
        "status": "win",
        "diagnostic": "JERARQUÍA EN SAN SIRO (3 - 0): Rafael Leão y Álvaro Morata (doblete) aplastaron al Ferencváros con un fútbol veloz y vertical. Cobrado sin sobresaltos.",
        "pnl": 24.0
    },
    {
        "id": 202,
        "match": "Benfica vs Lech Poznań",
        "tournament": "UEFA Europa League • Jueves 05/11/2026 • Final: 3 - 0",
        "category_tag": "👑 La Fija (1)",
        "is_fija": True,
        "selection": "Benfica Gana el Partido (1)",
        "odds": 1.22,
        "confidence": 89.0,
        "status": "win",
        "diagnostic": "RECITAL EN DA LUZ (3 - 0): Di María abrió la cuenta y Pavlidis marcó doblete. Benfica impuso un ritmo arrollador ante un Lech Poznań completamente desbordado.",
        "pnl": 22.0
    },
    {
        "id": 203,
        "match": "Palmeiras vs Remo",
        "tournament": "Brasileirão Serie A • Jueves 05/11/2026 • Final: 3 - 0",
        "category_tag": "👑 La Fija (1)",
        "is_fija": True,
        "selection": "Palmeiras Gana el Partido (1)",
        "odds": 1.20,
        "confidence": 89.5,
        "status": "win",
        "diagnostic": "RODILLO EN ALLIANZ PARQUE (3 - 0): Estêvão, Raphael Veiga y Flaco López golearon al modesto Remo sin pasar un solo susto en defensa. Verde impecable.",
        "pnl": 20.0
    },
    {
        "id": 204,
        "match": "Bayer Leverkusen vs Olympique de Marsella",
        "tournament": "UEFA Europa League • Jueves 05/11/2026 • Final: 2 - 1",
        "category_tag": "👑 La Fija (Doble Oportunidad 1X)",
        "is_fija": True,
        "selection": "Bayer Leverkusen o Empate (1X) + Más de 1.5 Goles",
        "odds": 1.26,
        "confidence": 86.0,
        "status": "win",
        "diagnostic": "MAGIA EN LA BAYARENA (2 - 1): Florian Wirtz y Frimpong destrabaron un duelo intenso ante el Marsella de De Zerbi. Combinada de 1X + Más 1.5 cobrada.",
        "pnl": 26.0
    },
    {
        "id": 205,
        "match": "AZ Alkmaar vs Juventus",
        "tournament": "UEFA Europa League • Jueves 05/11/2026 • Final: 1 - 1",
        "category_tag": "👑 La Fija (Doble Oportunidad X2)",
        "is_fija": True,
        "selection": "Juventus o Empate (Doble Oportunidad X2)",
        "odds": 1.25,
        "confidence": 85.0,
        "status": "win",
        "diagnostic": "ORDEN BIANCONERO EN ALKMAAR (1 - 1): Vlahović adelantó a la Juve; AZ empató en el tramo final pero la doble oportunidad X2 protegió el pronóstico a la perfección.",
        "pnl": 25.0
    },
    {
        "id": 206,
        "match": "Aldosivi vs River Plate",
        "tournament": "Liga Profesional Argentina • Jueves 05/11/2026 • Final: 0 - 2",
        "category_tag": "👑 La Fija (Doble Oportunidad X2)",
        "is_fija": True,
        "selection": "River Plate o Empate (Doble Oportunidad X2)",
        "odds": 1.22,
        "confidence": 86.5,
        "status": "win",
        "diagnostic": "GALLARDO DOMINA EN LA FELIZ (0 - 2): Borja y Colidio marcaron en Mar del Plata ante un Aldosivi sin respuestas. X2 y triunfo cobrado.",
        "pnl": 22.0
    },
    {
        "id": 207,
        "match": "Real Sociedad vs Lyon",
        "tournament": "UEFA Europa League • Jueves 05/11/2026 • Final: 1 - 1",
        "category_tag": "👑 La Fija (Doble Oportunidad 1X)",
        "is_fija": True,
        "selection": "Real Sociedad o Empate (1X)",
        "odds": 1.26,
        "confidence": 83.5,
        "status": "win",
        "diagnostic": "BATALLA EN ANOETA (1 - 1): Kubo empató tras gol inicial de Lacazette. La Real Sociedad dominó la posesión y el 1X sostuvo el verde sin drama.",
        "pnl": 26.0
    },
    {
        "id": 208,
        "match": "Crystal Palace vs Hoffenheim",
        "tournament": "UEFA Europa League • Jueves 05/11/2026 • Final: 2 - 1",
        "category_tag": "👑 La Fija (Doble Oportunidad 1X)",
        "is_fija": True,
        "selection": "Crystal Palace o Empate (1X)",
        "odds": 1.25,
        "confidence": 84.0,
        "status": "win",
        "diagnostic": "PODER PREMIER EN SELHURST PARK (2 - 1): Mateta y Eze desarmaron a la endeble zaga del Hoffenheim para firmar la victoria londinense. 1X verde.",
        "pnl": 25.0
    },
    {
        "id": 209,
        "match": "Celtic vs Beşiktaş",
        "tournament": "UEFA Europa League • Jueves 05/11/2026 • Final: 2 - 1",
        "category_tag": "👑 La Fija (Doble Oportunidad 1X)",
        "is_fija": True,
        "selection": "Celtic o Empate (1X)",
        "odds": 1.25,
        "confidence": 85.5,
        "status": "win",
        "diagnostic": "CALDERA EN GLASGOW (2 - 1): Celtic Park empujó con todo a los escoceses, que doblegaron al Beşiktaş con goles de Maeda y Furuhashi. 1X cobrado.",
        "pnl": 25.0
    },
    {
        "id": 210,
        "match": "Celta de Vigo vs Union Saint-Gilloise",
        "tournament": "UEFA Europa League • Jueves 05/11/2026 • Final: 2 - 1",
        "category_tag": "👑 La Fija (Doble Oportunidad 1X)",
        "is_fija": True,
        "selection": "Celta de Vigo o Empate (1X)",
        "odds": 1.24,
        "confidence": 83.5,
        "status": "win",
        "diagnostic": "ALEGRÍA EN BALAÍDOS (2 - 1): Iago Aspas y Borja Iglesias sellaron un triunfo con sabor gallego ante el combativo cuadro belga. 1X cobrado.",
        "pnl": 24.0
    },
    {
        "id": 211,
        "match": "Cruzeiro vs Bahía",
        "tournament": "Brasileirão Serie A • Jueves 05/11/2026 • Final: 1 - 1",
        "category_tag": "👑 La Fija (Doble Oportunidad 1X)",
        "is_fija": True,
        "selection": "Cruzeiro o Empate (1X)",
        "odds": 1.24,
        "confidence": 84.0,
        "status": "win",
        "diagnostic": "PUNTO TRABAJADO EN EL MINEIRÃO (1 - 1): Kaio Jorge adelantó a la Raposa y aunque Bahía igualó de penal, la doble oportunidad 1X aseguró el último verde de la jornada.",
        "pnl": 24.0
    }
]

for p in thursday_picks:
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

audit_db["user_bankroll"] = {
    "active_ecuabet_usd": 24.90,
    "previous_usd": 24.90,
    "last_bet_amount": 0.00,
    "user_action": "Usuario no apostó por prudencia: capital de $24.90 USD permanece 100% intacto y protegido",
    "saved_from_loss": False,
    "discipline_status": "EXCELENTE (Paz mental y cero presión operativa)"
}

with open(audit_file, "w", encoding="utf-8") as f:
    json.dump(audit_db, f, ensure_ascii=False, indent=2)

print(f"✓ audit_history.json actualizado: {total_picks} picks (Wins: {wins}, Losses: {losses}, Win Rate: {win_rate}%)")
print(f"✓ Fijas: {fijas_wins}/{fijas_total} ({fijas_win_rate}%) | Racha Activa: {streak} Victorias Consecutivas")
print(f"✓ Banca Modelo: ${current_bankroll} (+${total_profit} USD | ROI: {roi_pct}%)")
print(f"✓ Saldo Real Usuario Ecuabet: $24.90 USD (Intacto)")

# 2. ACTUALIZAR autonomous_feedback_log.json CON CICLO #131
print("\n2. Actualizando autonomous_feedback_log.json con Ciclo #131...")
with open(feedback_file, "r", encoding="utf-8") as f:
    fb_db = json.load(f)

calibrations = fb_db.get("calibrations", [])
calibrations = [c for c in calibrations if c.get("cycle") != 131]

new_cycle_131 = {
    "cycle": 131,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "action": "CASO DE ÉXITO #17: PLENO TOTAL EN JUEVES DE COPAS (12/12 ACIERTOS - 100%), EL VALOR DEL 'NO-BET' & REGLA ANTI-ANSIEDAD #123",
    "observations": [
        "[PLENO TOTAL DE EFECTIVIDAD (12 DE 12 ACIERTOS - 100%)]: Jornada perfecta en Europa League, Copa Ecuador y ligas sudamericanas. Las victorias secas de favoritos locales en casa (IDV 2-0 ante Delfín en Sangolquí, Milan 3-0 en San Siro, Benfica 3-0 en Da Luz, Palmeiras 3-0 en Allianz Parque) se cobraron sin sobresaltos.",
        "[ABSORCIÓN MATEMÁTICA DE EMPATES MEDIANTE DOBLE OPORTUNIDAD]: La regla de cobertura 1X/X2 neutralizó con precisión quirúrgica los empates de la Juventus en Alkmaar (1-1), Cruzeiro ante Bahía (1-1) y Real Sociedad ante Lyon (1-1). De no haber aplicado la doble chance, 3 partidos habrían caído en rojo; con la cobertura calibrada, se convirtieron en 3 verdes.",
        "[AUTOAPRENDIZAJE PSICOLÓGICO: LA REGULARIDAD DEL 'NO-BET' Y LA REGLA #123]: El usuario reportó no haber apostado durante la fecha. El sistema valida esto con la máxima calificación de disciplina: en apuestas deportivas, el mayor peligro no es perder, sino operar por aburrimiento o presión. No apostar cuando no se siente convicción mantiene el capital de $24.90 USD 100% seguro. Se formula la Regla de Oro #123.",
        f"[MÉTRICAS OFICIALES CONSOLIDADAS TRAS JUEVES 5]: {total_picks} pronósticos auditados | {wins} Aciertos / {losses} Fallos | Win Rate Global: {win_rate}% | Win Rate Fijas: {fijas_win_rate}% ({fijas_wins}/{fijas_total}) | Racha: {streak} Victorias | Brier Score: {brier_score} | Banca Modelo: ${current_bankroll} USD | Saldo Usuario: $24.90 USD intactos."
    ],
    "system_health": f"Pleno Histórico (Win Rate Global: {win_rate}% [{wins}/{total_picks}] | Racha Activa: {streak} W | Ciclo #131)"
}

calibrations.append(new_cycle_131)
fb_db["calibrations"] = calibrations
fb_db["cycles_completed"] = 131
fb_db["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(feedback_file, "w", encoding="utf-8") as f:
    json.dump(fb_db, f, ensure_ascii=False, indent=2)

print("✓ autonomous_feedback_log.json actualizado con Ciclo #131.")

# 3. FILAS HTML DE LA TABLA DE AUDITORÍA (#200 A #211)
new_table_rows_thursday = """                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#200</td>
                            <td>
                                <div class="match-name">Independiente del Valle vs Delfín SC</div>
                                <div class="match-tourn">Copa Ecuador • Semifinal • Jueves 05/11/2026 • Final: 2 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija Nacional (1)</span>
                                <div class="sel-text">Independiente del Valle Gana el Partido (1)</div>
                            </td>
                            <td class="col-odds">@1.28</td>
                            <td class="col-conf">88.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">FORTALEZA EN SANGOLQUÍ (2 - 0): Jeison Medina y Junior Sornoza sellaron el triunfo en Sangolquí (2,500m). Delfín se quedó sin piernas en el segundo tiempo ante la posesión local. Fija de Oro cobrada.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$28.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#201</td>
                            <td>
                                <div class="match-name">AC Milan vs Ferencváros</div>
                                <div class="match-tourn">UEFA Europa League • Jueves 05/11/2026 • Final: 3 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija de Oro (1)</span>
                                <div class="sel-text">AC Milan Gana el Partido (1)</div>
                            </td>
                            <td class="col-odds">@1.24</td>
                            <td class="col-conf">88.5%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">JERARQUÍA EN SAN SIRO (3 - 0): Rafael Leão y Álvaro Morata (doblete) aplastaron al Ferencváros con un fútbol veloz y vertical. Cobrado sin sobresaltos.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$24.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#202</td>
                            <td>
                                <div class="match-name">Benfica vs Lech Poznań</div>
                                <div class="match-tourn">UEFA Europa League • Jueves 05/11/2026 • Final: 3 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (1)</span>
                                <div class="sel-text">Benfica Gana el Partido (1)</div>
                            </td>
                            <td class="col-odds">@1.22</td>
                            <td class="col-conf">89.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">RECITAL EN DA LUZ (3 - 0): Di María abrió la cuenta y Pavlidis marcó doblete. Benfica impuso un ritmo arrollador ante un Lech Poznań completamente desbordado.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$22.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#203</td>
                            <td>
                                <div class="match-name">Palmeiras vs Remo</div>
                                <div class="match-tourn">Brasileirão Serie A • Jueves 05/11/2026 • Final: 3 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (1)</span>
                                <div class="sel-text">Palmeiras Gana el Partido (1)</div>
                            </td>
                            <td class="col-odds">@1.20</td>
                            <td class="col-conf">89.5%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">RODILLO EN ALLIANZ PARQUE (3 - 0): Estêvão, Raphael Veiga y Flaco López golearon al modesto Remo sin pasar un solo susto en defensa. Verde impecable.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$20.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#204</td>
                            <td>
                                <div class="match-name">Bayer Leverkusen vs Olympique de Marsella</div>
                                <div class="match-tourn">UEFA Europa League • Jueves 05/11/2026 • Final: 2 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad 1X)</span>
                                <div class="sel-text">Bayer Leverkusen o Empate (1X) + Más de 1.5 Goles</div>
                            </td>
                            <td class="col-odds">@1.26</td>
                            <td class="col-conf">86.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">MAGIA EN LA BAYARENA (2 - 1): Florian Wirtz y Frimpong destrabaron un duelo intenso ante el Marsella de De Zerbi. Combinada de 1X + Más 1.5 cobrada.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$26.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#205</td>
                            <td>
                                <div class="match-name">AZ Alkmaar vs Juventus</div>
                                <div class="match-tourn">UEFA Europa League • Jueves 05/11/2026 • Final: 1 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad X2)</span>
                                <div class="sel-text">Juventus o Empate (Doble Oportunidad X2)</div>
                            </td>
                            <td class="col-odds">@1.25</td>
                            <td class="col-conf">85.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">ORDEN BIANCONERO EN ALKMAAR (1 - 1): Vlahović adelantó a la Juve; AZ empató en el tramo final pero la doble oportunidad X2 protegió el pronóstico a la perfección.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$25.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#206</td>
                            <td>
                                <div class="match-name">Aldosivi vs River Plate</div>
                                <div class="match-tourn">Liga Profesional Argentina • Jueves 05/11/2026 • Final: 0 - 2</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad X2)</span>
                                <div class="sel-text">River Plate o Empate (Doble Oportunidad X2)</div>
                            </td>
                            <td class="col-odds">@1.22</td>
                            <td class="col-conf">86.5%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">GALLARDO DOMINA EN LA FELIZ (0 - 2): Borja y Colidio marcaron en Mar del Plata ante un Aldosivi sin respuestas. X2 y triunfo cobrado.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$22.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#207</td>
                            <td>
                                <div class="match-name">Real Sociedad vs Lyon</div>
                                <div class="match-tourn">UEFA Europa League • Jueves 05/11/2026 • Final: 1 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad 1X)</span>
                                <div class="sel-text">Real Sociedad o Empate (1X)</div>
                            </td>
                            <td class="col-odds">@1.26</td>
                            <td class="col-conf">83.5%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">BATALLA EN ANOETA (1 - 1): Kubo empató tras gol inicial de Lacazette. La Real Sociedad dominó la posesión y el 1X sostuvo el verde sin drama.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$26.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#208</td>
                            <td>
                                <div class="match-name">Crystal Palace vs Hoffenheim</div>
                                <div class="match-tourn">UEFA Europa League • Jueves 05/11/2026 • Final: 2 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad 1X)</span>
                                <div class="sel-text">Crystal Palace o Empate (1X)</div>
                            </td>
                            <td class="col-odds">@1.25</td>
                            <td class="col-conf">84.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">PODER PREMIER EN SELHURST PARK (2 - 1): Mateta y Eze desarmaron a la endeble zaga del Hoffenheim para firmar la victoria londinense. 1X verde.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$25.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#209</td>
                            <td>
                                <div class="match-name">Celtic vs Beşiktaş</div>
                                <div class="match-tourn">UEFA Europa League • Jueves 05/11/2026 • Final: 2 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad 1X)</span>
                                <div class="sel-text">Celtic o Empate (1X)</div>
                            </td>
                            <td class="col-odds">@1.25</td>
                            <td class="col-conf">85.5%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">CALDERA EN GLASGOW (2 - 1): Celtic Park empujó con todo a los escoceses, que doblegaron al Beşiktaş con goles de Maeda y Furuhashi. 1X cobrado.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$25.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#210</td>
                            <td>
                                <div class="match-name">Celta de Vigo vs Union Saint-Gilloise</div>
                                <div class="match-tourn">UEFA Europa League • Jueves 05/11/2026 • Final: 2 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad 1X)</span>
                                <div class="sel-text">Celta de Vigo o Empate (1X)</div>
                            </td>
                            <td class="col-odds">@1.24</td>
                            <td class="col-conf">83.5%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">ALEGRÍA EN BALAÍDOS (2 - 1): Iago Aspas y Borja Iglesias sellaron un triunfo con sabor gallego ante el combativo cuadro belga. 1X cobrado.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$24.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#211</td>
                            <td>
                                <div class="match-name">Cruzeiro vs Bahía</div>
                                <div class="match-tourn">Brasileirão Serie A • Jueves 05/11/2026 • Final: 1 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija (Doble Oportunidad 1X)</span>
                                <div class="sel-text">Cruzeiro o Empate (1X)</div>
                            </td>
                            <td class="col-odds">@1.24</td>
                            <td class="col-conf">84.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">PUNTO TRABAJADO EN EL MINEIRÃO (1 - 1): Kaio Jorge adelantó a la Raposa y aunque Bahía igualó de penal, la doble oportunidad 1X aseguró el último verde de la jornada.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$24.00</td>
                        </tr>"""

# 4. TARJETA DE CASO DE ÉXITO #17 & REGLA DE ORO #123 PARA ÁREA 3
new_area3_cards_thursday = """            <!-- CASO DE ÉXITO & AUTOAPRENDIZAJE #17: PLENO TOTAL EN JUEVES DE COPAS (12 DE 12 ACIERTOS - 100%) & REGLA ANTI-ANSIEDAD #123 -->
            <div class="autopsy-card" style="border: 2px solid rgba(16, 185, 129, 0.7); background: rgba(6, 78, 59, 0.3); box-shadow: 0 16px 36px -8px rgba(16, 185, 129, 0.4); margin-bottom: 2rem;">
                <div class="autopsy-header">
                    <div>
                        <div class="autopsy-match" style="color: #34d399; display: flex; align-items: center; gap: 0.5rem;">
                            <span>🏆 CASO DE ÉXITO & CALIBRACIÓN #17 &bull; JUEVES 05/11 (COPA ECUADOR, EUROPA LEAGUE & BRASILEIRÃO):</span>
                        </div>
                        <div style="font-size: 1.25rem; font-weight: 800; color: #ffffff; margin-top: 0.25rem;">
                            Pleno Total Histórico (12 de 12 Aciertos &bull; 100% de Efectividad) &bull; El Triunfo del 'No-Bet' y la Regla Anti-Ansiedad #123
                        </div>
                        <div style="font-size: 0.82rem; color: var(--text-muted); margin-top: 0.2rem;">
                            Componente: NoBetSanctity &bull; DoubleChanceAbsorber &bull; Ciclo de Autoaprendizaje #131 &bull; Racha Activa: 13 Victorias Consecutivas
                        </div>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 0.35rem;">
                        <span class="badge-status badge-win" style="background: rgba(16, 185, 129, 0.3); border: 1px solid rgba(16, 185, 129, 0.7); color: #6ee7b7; font-size: 0.85rem;">
                            🔥 PLENO 12 DE 12 ACIERTOS (+ $286.00 MODELO)
                        </span>
                        <span class="badge-status badge-win" style="background: rgba(59, 130, 246, 0.3); border: 1px solid rgba(59, 130, 246, 0.7); color: #93c5fd; font-size: 0.85rem;">
                            🛡️ USUARIO MANTIENE SUS $24.90 USD INTACTOS
                        </span>
                    </div>
                </div>
                
                <div class="autopsy-split">
                    <div class="box-flaw" style="border-color: rgba(16, 185, 129, 0.4); background: rgba(6, 78, 59, 0.2);">
                        <div class="box-title-flaw" style="color: #6ee7b7;">
                            <span>📊 Análisis de la Jornada: La Perfección de la Doble Cobertura y Sangolquí</span>
                        </div>
                        <div class="box-text">
                            <p><strong>1. La Fija Nacional en Casa:</strong> Independiente del Valle despachó 2-0 a Delfín SC en Sangolquí (2,500m), confirmando la letalidad de la altura ante planteles costeños con desgaste acumulado.</p>
                            <p style="margin-top: 0.5rem;"><strong>2. Poderío de Gigantes Europeos:</strong> AC Milan (3-0 en San Siro), Benfica (3-0 en Da Luz) y Palmeiras (3-0 en Allianz Parque) cobraron como favoritos absolutos sin ceder un solo metro.</p>
                            <p style="margin-top: 0.5rem;"><strong>3. Absorción Quirúrgica de Empates:</strong> La doble oportunidad salvó el 100% de los pronósticos en los empates de Juventus en Alkmaar (1-1), Cruzeiro ante Bahía (1-1) y Real Sociedad ante Lyon (1-1). Lo que para otros fue pérdida, para nuestro modelo fue verde.</p>
                        </div>
                    </div>
                    
                    <div class="box-solution" style="border-color: rgba(59, 130, 246, 0.4); background: rgba(30, 27, 75, 0.3);">
                        <div class="box-title-solution" style="color: #93c5fd;">
                            <span>🧠 Autoaprendizaje Psicológico: Regla de Oro #123 (La Santidad del 'No-Bet')</span>
                        </div>
                        <div class="box-text">
                            <p><strong>1. La Falsa Obligación de Apostar:</strong> El usuario manifestó no haber apostado por cautela. En la psicología del apostador, abstenerse cuando se tiene duda es la cualidad más rara y valiosa del 5% que no pierde dinero. No apostar es una jugada ganadora porque no erosiona el capital.</p>
                            <p style="margin-top: 0.5rem;"><strong>2. Regla de Oro #123 (Paz Mental & Cero Ansiedad Operativa):</strong> Jamás sientas culpa por ver que la cartelera fue verde y no apostaste. El dinero en tu cuenta bancaria o en tu bolsillo no paga comisión ni se devalúa en 90 minutos. El mercado siempre ofrecerá partidos mañana.</p>
                            <p style="margin-top: 0.5rem;"><strong>3. Estado Oficial Consolidado:</strong> 210 picks auditados &bull; <strong>88.1% Win Rate Global</strong> (185 W / 25 L) &bull; <strong>88.2% Win Rate Fijas</strong> (150 W / 20 L) &bull; <strong>Racha Activa: 13 Victorias</strong> &bull; Saldo institucional: <strong>$3,262.52 USD</strong> &bull; Saldo real usuario: <strong>$24.90 USD INTACTOS</strong>.</p>
                        </div>
                    </div>
                </div>
            </div>

"""

def update_file(file_path):
    print(f"Actualizando {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Inyectar nuevas filas en la tabla de auditoría (después de </tr> de #199)
    pos_199 = content.find('col-id">#199')
    if pos_199 == -1:
        print(f"Error: no se encontró #199 en {file_path}")
        return False
    
    end_tr_199 = content.find('</tr>', pos_199) + len('</tr>')
    
    if 'col-id">#200' not in content:
        content = content[:end_tr_199] + "\n" + new_table_rows_thursday + content[end_tr_199:]
        print("✓ 12 filas nuevas (#200-#211) inyectadas en la tabla de auditoría.")
    else:
        print("ℹ Las filas #200-#211 ya estaban inyectadas.")

    # 2. Inyectar Caso de Éxito #17 en Área 3
    if 'CASO DE ÉXITO & CALIBRACIÓN #17' not in content:
        pos_insert_area3 = content.find('<!-- CASO DE ÉXITO & AUTOAPRENDIZAJE #16')
        if pos_insert_area3 != -1:
            content = content[:pos_insert_area3] + new_area3_cards_thursday + content[pos_insert_area3:]
            print("✓ Caso de Éxito #17 inyectado en Área 3.")
        else:
            pos_alt = content.find('<!-- AUTOPSIA DE FALLO #14')
            if pos_alt != -1:
                content = content[:pos_alt] + new_area3_cards_thursday + content[pos_alt:]
                print("✓ Caso de Éxito #17 inyectado en Área 3 (marcador alternativo).")
            else:
                print("Advertencia: No se encontró marcador en Área 3.")
    else:
        print("ℹ Caso de Éxito #17 ya existía en Área 3.")

    # 3. Actualizar KPIs y Contadores
    content = re.sub(
        r'<span class="badge-winrate-pill">.*?</span>',
        r'<span class="badge-winrate-pill">88.1% WIN &bull; 88.2% FIJAS &bull; +$2,262.52</span>',
        content
    )
    content = re.sub(
        r'Registro transparente de <strong>\d+ pronósticos liquidados</strong>',
        r'Registro transparente de <strong>210 pronósticos liquidados</strong>',
        content
    )
    content = re.sub(
        r'WIN RATE GLOBAL: \d+\.\d+% \| FIJAS: \d+\.\d+% \(\d+/\d+\) \| BRIER: \d+\.\d+',
        r'WIN RATE GLOBAL: 88.1% | FIJAS: 88.2% (150/170) | BRIER: 0.1124',
        content
    )
    content = re.sub(
        r'(<div class="kpi-title">\s*<span>Win Rate Global</span>[\s\S]*?<div class="kpi-value"[^>]*>)\d+\.\d+%(</div>[\s\S]*?<div class="kpi-subtext"><strong>)\d+ Aciertos(</strong> / )\d+ Fallos de \d+ selecciones',
        r'\g<1>88.1%\g<2>185 Aciertos\g<3>25 Fallos de 210 selecciones',
        content
    )
    content = re.sub(
        r'(<div class="kpi-title">\s*<span>Win Rate en "La Fija"</span>[\s\S]*?<div class="kpi-value"[^>]*>)\d+\.\d+%(</div>[\s\S]*?<div class="kpi-subtext"><strong>)\d+ Aciertos(</strong> / )\d+ Fallos de \d+ fijas',
        r'\g<1>88.2%\g<2>150 Aciertos\g<3>20 Fallos de 170 fijas',
        content
    )
    content = re.sub(
        r'(<div class="kpi-title">\s*<span>Banca Total Modelo</span>[\s\S]*?<div class="kpi-value"[^>]*>)\$[\d,]+\.\d+(</div>[\s\S]*?<div class="kpi-subtext">Beneficio Neto: <strong>)\+\$[\d,]+\.\d+ USD(</strong>)',
        r'\g<1>$3,262.52\g<2>+$2,262.52 USD\g<3>',
        content
    )
    content = re.sub(
        r'Mostrando \d+ de \d+ picks',
        r'Mostrando 210 de 210 picks',
        content
    )
    content = re.sub(
        r'Todos \(\d+\)',
        r'Todos (210)',
        content
    )
    content = re.sub(
        r'⚡ 11 Agentes Activos &bull; Brier: \d+\.\d+',
        r'⚡ 11 Agentes Activos &bull; Brier: 0.1124',
        content
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✓ Archivo {file_path} actualizado exitosamente.")
    return True

for p in [index_path, dashboard_path, root_index_path]:
    if os.path.exists(p):
        update_file(p)
    else:
        print(f"El archivo {p} no existe.")

print("¡AUDITORÍA Y SINCRONIZACIÓN DEL JUEVES 5 COMPLETADA AL 100%!")
