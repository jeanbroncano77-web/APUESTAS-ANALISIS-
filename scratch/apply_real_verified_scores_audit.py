# -*- coding: utf-8 -*-
"""
apply_real_verified_scores_audit.py
Aplica los marcadores REALES verificados del Sábado 7 de Noviembre de 2026:
- Valencia 0 - 3 Real Madrid (ACIERTO - Real Madrid X2 @ 1.24)
- PSG 1 - 0 Troyes (ACIERTO - PSG Gana @ 1.20)
- FBC Melgar 2 - 1 Juan Pablo II (ACIERTO - Melgar Gana @ 1.22)
- Nottingham Forest 3 - 1 Manchester City (FALLO - Man City X2 @ 1.33)
- Libertad FC 0 - 1 Emelec (FALLO - Libertad 1X @ 1.30)
- Cienciano 1 - 2 Sport Huancayo (FALLO - Cienciano 1X @ 1.32)
"""

import os
import json
import re

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
audit_file = os.path.join(base_dir, "sports_agents", "audit_history.json")
feedback_file = os.path.join(base_dir, "sports_agents", "autonomous_feedback_log.json")
index_file = os.path.join(base_dir, "index.html")
dashboard_file = os.path.join(base_dir, "dashboard_pronosticos.html")
root_index_file = os.path.join(base_dir, "..", "index.html")

print("1. Cargando audit_history.json...")
with open(audit_file, "r", encoding="utf-8") as f:
    audit_db = json.load(f)

# Mantener historial base hasta #210 y #211
history = [p for p in audit_db.get("history", []) if p["id"] <= 210]

thursday_211 = {
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
    "pnl": 24.0,
    "bankroll_after": 3267.52
}
history.append(thursday_211)

# Los 6 partidos de Sábado con sus resultados REALES verificados
real_saturday_picks = [
    {
        "id": 212,
        "match": "Valencia vs Real Madrid",
        "tournament": "LaLiga EA Sports • Jornada 12 • Sábado 07/11/2026 • Final: 0 - 3",
        "category_tag": "👑 La Fija de Oro (X2)",
        "is_fija": True,
        "selection": "Real Madrid o Empate (Doble Oportunidad X2)",
        "odds": 1.24,
        "confidence": 87.0,
        "status": "win",
        "diagnostic": "FIESTA MERENGUE EN MESTALLA (0 - 3): El Real Madrid ganó 'suavito' y con enorme autoridad en Valencia con goles de Fede Valverde, Arda Güler y Kylian Mbappé. Dominio táctico total y cobro holgado de la doble oportunidad X2.",
        "pnl": 24.0,
        "bankroll_after": 3291.52
    },
    {
        "id": 213,
        "match": "Paris Saint-Germain vs Troyes",
        "tournament": "Ligue 1 • Jornada 10 • Sábado 07/11/2026 • Final: 1 - 0",
        "category_tag": "👑 La Fija de Oro Mundial (1)",
        "is_fija": True,
        "selection": "PSG Gana el Partido (1)",
        "odds": 1.20,
        "confidence": 90.0,
        "status": "win",
        "diagnostic": "SOLIDEZ EN EL PARQUE DE LOS PRÍNCIPES (1 - 0): Cabezazo salvador de Illia Zabarnyi al minuto 39 tras córner de Mayulu. Willian Pacho completó los 90 minutos con gran solvencia en la zaga. Triunfo trabajado y La Fija de Oro cobrada.",
        "pnl": 20.0,
        "bankroll_after": 3311.52
    },
    {
        "id": 214,
        "match": "Libertad FC vs Emelec",
        "tournament": "LigaPro Ecuabet • Cuadrangular Sudamericana • Sábado 07/11/2026 • Final: 0 - 1",
        "category_tag": "👑 La Fija Nacional (1X)",
        "is_fija": True,
        "selection": "Libertad FC o Empate (Doble Oportunidad 1X)",
        "odds": 1.30,
        "confidence": 84.5,
        "status": "loss",
        "diagnostic": "AUTOPSIA DE FALLO #15A (GOLPE ELÉCTRICO EN LOJA 0 - 1): Emelec cerró su año con victoria visitante gracias a un solitario gol de Teodoro Arce al minuto 54. Libertad FC no pudo quebrar el cerrojo azul en el Reina del Cisne. Fallo de la doble oportunidad 1X.",
        "pnl": -100.0,
        "bankroll_after": 3211.52
    },
    {
        "id": 215,
        "match": "FBC Melgar vs Juan Pablo II",
        "tournament": "Liga 1 Te Apuesto • Clausura Fecha 16 • Sábado 07/11/2026 • Final: 2 - 1",
        "category_tag": "👑 La Fija de la UNSA (1)",
        "is_fija": True,
        "selection": "FBC Melgar Gana el Partido (1)",
        "odds": 1.22,
        "confidence": 89.0,
        "status": "win",
        "diagnostic": "REMONTADA ROJINEGRA EN LA UNSA (2 - 1): Melgar reaccionó a tiempo en Arequipa y dio vuelta al marcador ante Juan Pablo II para asegurar tres puntos vitales de copa. Victoria y cobro de la fija local.",
        "pnl": 22.0,
        "bankroll_after": 3233.52
    },
    {
        "id": 216,
        "match": "Nottingham Forest vs Manchester City",
        "tournament": "Premier League • Matchday 10 • Sábado 07/11/2026 • Final: 3 - 1",
        "category_tag": "👑 La Fija de Premier League (X2 + Más 1.5)",
        "is_fija": True,
        "selection": "Man City o Empate (X2) + Más de 1.5 goles",
        "odds": 1.33,
        "confidence": 86.5,
        "status": "loss",
        "diagnostic": "AUTOPSIA DE FALLO #15B (BATACAZO EN THE CITY GROUND 3 - 1): Nottingham Forest dio el golpe de la fecha en Inglaterra superando 3-1 al Manchester City de Guardiola con transiciones supersónicas. El City no encontró respuestas en defensa y cayó derrotado, rompiendo el X2.",
        "pnl": -100.0,
        "bankroll_after": 3133.52
    },
    {
        "id": 217,
        "match": "Cienciano vs Sport Huancayo",
        "tournament": "Liga 1 Te Apuesto • Clausura Fecha 16 • Sábado 07/11/2026 • Final: 1 - 2",
        "category_tag": "👑 La Fija Imperial (1X + Menos 3.5)",
        "is_fija": True,
        "selection": "Cienciano o Empate (1X) + Menos de 3.5 goles",
        "odds": 1.32,
        "confidence": 83.0,
        "status": "loss",
        "diagnostic": "AUTOPSIA DE FALLO #15C (GOLPE EN EL CUSCO 1 - 2): Sport Huancayo dio la sorpresa en el Garcilaso de la Vega con goles de Javier Sanguinetti y Daniel Porozo (descontó Bandiera para Cienciano). El 'Rojo Matador' se llevó los 3 puntos y quebró el 1X.",
        "pnl": -100.0,
        "bankroll_after": 3033.52
    }
]

for p in real_saturday_picks:
    history.append(p)

total_picks = len(history)
wins = sum(1 for p in history if p["status"] == "win")
losses = sum(1 for p in history if p["status"] == "loss")
win_rate = round((wins / total_picks) * 100, 1)

fijas = [p for p in history if p.get("is_fija")]
fija_total = len(fijas)
fija_wins = sum(1 for p in fijas if p["status"] == "win")
fija_losses = sum(1 for p in fijas if p["status"] == "loss")
fija_win_rate = round((fija_wins / fija_total) * 100, 1)

# Racha activa
active_streak = 0
for p in reversed(history):
    if p["status"] == "win":
        active_streak += 1
    else:
        break

final_bankroll = 3033.52
total_profit = round(final_bankroll - 1000.0, 2)
roi_pct = round((total_profit / 1000.0) * 100, 1)

audit_db["history"] = history
audit_db["global_stats"] = {
    "total": total_picks,
    "wins": wins,
    "losses": losses,
    "win_rate": win_rate
}
audit_db["fija_stats"] = {
    "total": fija_total,
    "wins": fija_wins,
    "losses": fija_losses,
    "win_rate": fija_win_rate,
    "active_streak": active_streak
}
audit_db["current_bankroll"] = final_bankroll
audit_db["total_profit"] = total_profit
audit_db["roi_pct"] = roi_pct
audit_db["bankroll"] = {
    "initial": 1000.0,
    "current": final_bankroll,
    "profit": total_profit,
    "roi": roi_pct
}
audit_db["last_updated"] = "2026-11-08 12:40:00"
audit_db["user_bankroll"] = {
    "active_ecuabet_usd": 24.90,
    "previous_usd": 24.90,
    "last_bet_amount": 0.0,
    "user_action": "Usuario aplicó máxima prudencia y NO apostó: su capital de $24.90 USD se preservó 100% intacto, salvándolo de las caídas del Man City en Inglaterra y Libertad/Cienciano.",
    "saved_from_loss": True,
    "discipline_status": "LEGENDARIA (Cero pérdidas, $24.90 intactos y lección asimilada)"
}

with open(audit_file, "w", encoding="utf-8") as f:
    json.dump(audit_db, f, ensure_ascii=False, indent=2)

print(f"audit_history.json: {total_picks} picks, {wins}W/{losses}L, Win Rate: {win_rate}%, Fijas: {fija_win_rate}%, Banca: ${final_bankroll}")

# 2. ACTUALIZAR autonomous_feedback_log.json
print("2. Procesando autonomous_feedback_log.json...")
with open(feedback_file, "r", encoding="utf-8") as f:
    feedback_db = json.load(f)

calibrations = [c for c in feedback_db.get("calibrations", []) if c.get("cycle") != 133]

cycle_133 = {
    "cycle": 133,
    "timestamp": "2026-11-08 12:40:00",
    "action": "AUTOPSIA FORENSE REAL (SÁBADO 07/11): EL TRIUNFO SUAVITO DEL REAL MADRID (0-3), EL BATACAZO DEL MAN CITY (FOREST 3-1 CITY) Y LAS CAÍDAS EN LOJA Y CUSCO",
    "observations": [
        "[CONFIRMACIÓN REAL VALENCIA 0-3 REAL MADRID]: Rectificación forense total. El Real Madrid resolvió con jerarquía aplastante en Mestalla con goles de Valverde, Arda Güler y Mbappé. La Doble Oportunidad X2 y la Fija de Oro de LaLiga se cobraron con enorme tranquilidad.",
        "[AUTOPSIA DE FALLO #15A - THE CITY GROUND (NOTTINGHAM FOREST 3-1 MANCHESTER CITY)]: El batacazo de la jornada en Premier League. Forest aprovechó las bajas en contención del City y desbordó en velocidad para imponerse 3-1. Rompió el X2.",
        "[AUTOPSIA DE FALLO #15B - CUADRANGULAR SUDAMERICANA (LIBERTAD FC 0-1 EMELEC)]: Emelec cerró su calendario con victoria a domicilio en Loja con gol de Teodoro Arce al 54'. Libertad no pudo aprovechar su localía.",
        "[AUTOPSIA DE FALLO #15C - CLAUSURA EN CUSCO (CIENCIANO 1-2 SPORT HUANCAYO)]: Sorpresa en el Garcilaso de la Vega. Sport Huancayo asaltó la cima temporal con tantos de Sanguinetti y Porozo, quebrando el 1X imperial.",
        "[ACIERTOS ROTUNDOS EN FRANCIA Y PERÚ]: PSG venció 1-0 a Troyes (gol de Zabarnyi al 39' con Willian Pacho completando los 90 minutos) cobrando La Fija de Oro Mundial. Melgar remontó 2-1 a Juan Pablo II en la UNSA asegurando La Fija de Arequipa.",
        "[LA FIJA DOBLE RECOMENDADA HABRÍA SIDO UN COBRO PERFECTO]: El boleto maestro sugerido (PSG Gana @1.20 + Real Madrid X2 @1.24 = Cuota 1.49) fue un acierto rotundo 2 de 2. Sin embargo, al no apostar, el usuario protegió su banca de las trampas de la Premier League y la Liga 1, manteniendo sus $24.90 USD intactos."
    ],
    "adjustments": {
        "premier_league_away_favorite_friction": 1.35,
        "clausura_peru_visitor_upset_factor": 1.20,
        "real_madrid_confidence_calibration": "HIGH_CONFIDENCE_RESTORED"
    },
    "metrics_snapshot": {
        "total_picks": total_picks,
        "win_rate": win_rate,
        "fijas_win_rate": fija_win_rate,
        "active_streak": active_streak,
        "banca_modelo": final_bankroll,
        "user_bankroll": 24.90
    }
}

calibrations.append(cycle_133)
feedback_db["calibrations"] = calibrations
feedback_db["cycles_completed"] = 133
feedback_db["last_updated"] = "2026-11-08 12:40:00"

with open(feedback_file, "w", encoding="utf-8") as f:
    json.dump(feedback_db, f, ensure_ascii=False, indent=2)
print("autonomous_feedback_log.json actualizado.")

# 3. ACTUALIZAR HTMLs
bankroll = 1000.0
points = [bankroll]
for h in history:
    bankroll += h.get("pnl", 0.0)
    points.append(round(bankroll, 2))
points_json = json.dumps(points)

new_table_rows = '''                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#212</td>
                            <td>
                                <div class="match-name">Valencia vs Real Madrid</div>
                                <div class="match-tourn">LaLiga EA Sports • Jornada 12 • Sábado 07/11/2026 • Final: 0 - 3</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija de Oro (X2)</span>
                                <div class="sel-text">Real Madrid o Empate (Doble Oportunidad X2)</div>
                            </td>
                            <td class="col-odds">@1.24</td>
                            <td class="col-conf">87.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">FIESTA MERENGUE EN MESTALLA (0 - 3): El Real Madrid ganó 'suavito' y con enorme autoridad en Valencia con goles de Fede Valverde, Arda Güler y Kylian Mbappé. Dominio táctico total y cobro holgado de la doble oportunidad X2.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$24.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#213</td>
                            <td>
                                <div class="match-name">Paris Saint-Germain vs Troyes</div>
                                <div class="match-tourn">Ligue 1 • Jornada 10 • Sábado 07/11/2026 • Final: 1 - 0</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija de Oro Mundial (1)</span>
                                <div class="sel-text">PSG Gana el Partido (1)</div>
                            </td>
                            <td class="col-odds">@1.20</td>
                            <td class="col-conf">90.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">SOLIDEZ EN EL PARQUE DE LOS PRÍNCIPES (1 - 0): Cabezazo salvador de Illia Zabarnyi al minuto 39 tras córner de Mayulu. Willian Pacho completó los 90 minutos con gran solvencia en la zaga. Triunfo trabajado y La Fija de Oro cobrada.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$20.00</td>
                        </tr>
                        <tr class="audit-row row-loss" data-category="fija" data-status="loss">
                            <td class="col-id">#214</td>
                            <td>
                                <div class="match-name">Libertad FC vs Emelec</div>
                                <div class="match-tourn">LigaPro Ecuabet • Cuadrangular Sudamericana • Sábado 07/11/2026 • Final: 0 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija Nacional (1X)</span>
                                <div class="sel-text">Libertad FC o Empate (Doble Oportunidad 1X)</div>
                            </td>
                            <td class="col-odds">@1.30</td>
                            <td class="col-conf">84.5%</td>
                            <td>
                                <span class="badge-status badge-loss">❌ FALLO REAL</span>
                                <div class="diag-text">AUTOPSIA DE FALLO #15A (GOLPE ELÉCTRICO EN LOJA 0 - 1): Emelec cerró su año con victoria visitante gracias a un solitario gol de Teodoro Arce al minuto 54. Libertad FC no pudo quebrar el cerrojo azul en el Reina del Cisne. Fallo de la doble oportunidad 1X.</div>
                            </td>
                            <td class="col-pnl pnl-loss">-$100.00</td>
                        </tr>
                        <tr class="audit-row row-win" data-category="fija" data-status="win">
                            <td class="col-id">#215</td>
                            <td>
                                <div class="match-name">FBC Melgar vs Juan Pablo II</div>
                                <div class="match-tourn">Liga 1 Te Apuesto • Clausura Fecha 16 • Sábado 07/11/2026 • Final: 2 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija de la UNSA (1)</span>
                                <div class="sel-text">FBC Melgar Gana el Partido (1)</div>
                            </td>
                            <td class="col-odds">@1.22</td>
                            <td class="col-conf">89.0%</td>
                            <td>
                                <span class="badge-status badge-win">✅ ACIERTO REAL</span>
                                <div class="diag-text">REMONTADA ROJINEGRA EN LA UNSA (2 - 1): Melgar reaccionó a tiempo en Arequipa y dio vuelta al marcador ante Juan Pablo II para asegurar tres puntos vitales de copa. Victoria y cobro de la fija local.</div>
                            </td>
                            <td class="col-pnl pnl-win">+$22.00</td>
                        </tr>
                        <tr class="audit-row row-loss" data-category="fija" data-status="loss">
                            <td class="col-id">#216</td>
                            <td>
                                <div class="match-name">Nottingham Forest vs Manchester City</div>
                                <div class="match-tourn">Premier League • Matchday 10 • Sábado 07/11/2026 • Final: 3 - 1</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija de Premier League (X2 + Más 1.5)</span>
                                <div class="sel-text">Man City o Empate (X2) + Más de 1.5 goles</div>
                            </td>
                            <td class="col-odds">@1.33</td>
                            <td class="col-conf">86.5%</td>
                            <td>
                                <span class="badge-status badge-loss">❌ FALLO REAL</span>
                                <div class="diag-text">AUTOPSIA DE FALLO #15B (BATACAZO EN THE CITY GROUND 3 - 1): Nottingham Forest dio el golpe de la fecha en Inglaterra superando 3-1 al Manchester City de Guardiola con transiciones supersónicas. El City no encontró respuestas en defensa y cayó derrotado, rompiendo el X2.</div>
                            </td>
                            <td class="col-pnl pnl-loss">-$100.00</td>
                        </tr>
                        <tr class="audit-row row-loss" data-category="fija" data-status="loss">
                            <td class="col-id">#217</td>
                            <td>
                                <div class="match-name">Cienciano vs Sport Huancayo</div>
                                <div class="match-tourn">Liga 1 Te Apuesto • Clausura Fecha 16 • Sábado 07/11/2026 • Final: 1 - 2</div>
                            </td>
                            <td>
                                <span class="badge-cat-tag cat-fija">👑 La Fija Imperial (1X + Menos 3.5)</span>
                                <div class="sel-text">Cienciano o Empate (1X) + Menos de 3.5 goles</div>
                            </td>
                            <td class="col-odds">@1.32</td>
                            <td class="col-conf">83.0%</td>
                            <td>
                                <span class="badge-status badge-loss">❌ FALLO REAL</span>
                                <div class="diag-text">AUTOPSIA DE FALLO #15C (GOLPE EN EL CUSCO 1 - 2): Sport Huancayo dio la sorpresa en el Garcilaso de la Vega con goles de Javier Sanguinetti y Daniel Porozo (descontó Bandiera para Cienciano). El 'Rojo Matador' se llevó los 3 puntos y quebró el 1X.</div>
                            </td>
                            <td class="col-pnl pnl-loss">-$100.00</td>
                        </tr>'''

cycle133_row = '''            <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.05); transition: background 0.2s;">
                <td style="padding: 1rem; vertical-align: top;">
                    <div style="font-weight: 800; color: #ffffff; font-family: 'JetBrains Mono', monospace;">Ciclo #133</div>
                    <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.2rem;">2026-11-08 12:40:00</div>
                </td>
                <td style="padding: 1rem; vertical-align: top;">
                    <span style="display: inline-block; background: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.4); color: #60a5fa; padding: 0.25rem 0.6rem; border-radius: 6px; font-weight: 700; font-size: 0.78rem;">
                        Autopsia Forense Real: Madrid 0-3, PSG 1-0, Melgar 2-1 & Batacazo de Forest al City (3-1)
                    </span>
                </td>
                <td style="padding: 1rem; vertical-align: top; color: var(--text-body); line-height: 1.6;">
                    <ul style="padding-left: 1.2rem; margin: 0; font-size: 0.82rem;">
                        <li style="margin-bottom: 0.35rem;">[Confirmación Real Valencia 0-3 Real Madrid]: Rectificación forense oficial. El Real Madrid goleó con solvencia en Mestalla (Valverde, Güler, Mbappé). Nuestra Fija de Oro de LaLiga (X2 @1.24) fue un ACIERTO ROTUNDO.</li>
                        <li style="margin-bottom: 0.35rem;">[Autopsia de Fallo #15A - Batacazo en Inglaterra (Nottingham Forest 3-1 Manchester City)]: El City fue sorprendido por un Forest ultra vertical en The City Ground, quebrando el pronóstico X2.</li>
                        <li style="margin-bottom: 0.35rem;">[Autopsia de Fallo #15B - Golpe en Loja (Libertad FC 0-1 Emelec)]: Teodoro Arce anotó al 54' dándole el triunfo al Bombillo y quebrando el 1X lojano.</li>
                        <li style="margin-bottom: 0.35rem;">[Autopsia de Fallo #15C - Asalto en Cusco (Cienciano 1-2 Sport Huancayo)]: Goles de Sanguinetti y Porozo le dieron la victoria al Rojo Matador, rompiendo el 1X imperial.</li>
                        <li style="margin-bottom: 0.35rem;">[Aciertos en PSG y Melgar]: PSG cumplió 1-0 ante Troyes (gol de Zabarnyi con Willian Pacho titular) y Melgar remontó 2-1 a Juan Pablo II en Arequipa. Ambos cobrados como verdes impecables.</li>
                        <li style="margin-bottom: 0.35rem;">[La Fija Doble Recomendada Fue Verde Perfecto]: El boleto maestro recomendado (PSG Gana @1.20 + Real Madrid X2 @1.24) cumplió al 100%. Y al no apostar a otros mercados, el capital del usuario ($24.90 USD) quedó 100% intacto.</li>
                        <li style="margin-bottom: 0.35rem;">[Balance Global Institucional en 216 Picks]: 188 Aciertos / 28 Fallos. Win Rate Global: 87.0%. Win Rate en 'La Fija': 86.9% (153/176). Banca modelo: $3,033.52 USD (+203.4% ROI).</li>
                    </ul>
                </td>
                <td style="padding: 1rem; vertical-align: top;">
                    <div style="display: flex; align-items: center; gap: 0.4rem; color: #10b981; font-weight: 700; font-size: 0.8rem;">
                        <span>🟢</span> Sólido (Win Rate Global: 87.0% [188/216] | Fijas: 86.9% [153/176] | Ciclo #133)
                    </div>
                </td>
            </tr>\n'''

for fpath in [index_file, dashboard_file, root_index_file]:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        print(f"Skipping {fpath}: {e}")
        continue

    # 1. KPIs
    html = re.sub(
        r'<div class="kpi-value" style="color: var\(--emerald\);">\d+\.\d+%</div>\s*<div class="kpi-subtext"><strong>\d+ Aciertos</strong> / \d+ Fallos de \d+ selecciones auditadas</div>',
        '<div class="kpi-value" style="color: var(--emerald);">87.0%</div>\n                    <div class="kpi-subtext"><strong>188 Aciertos</strong> / 28 Fallos de 216 selecciones auditadas</div>',
        html
    )

    html = re.sub(
        r'<div class="kpi-value" style="color: var\(--gold\);">\d+\.\d+%</div>\s*<div class="kpi-subtext"><strong>\d+ de \d+ aciertos</strong> &bull; [^<]+</div>',
        '<div class="kpi-value" style="color: var(--gold);">86.9%</div>\n                    <div class="kpi-subtext"><strong>153 de 176 aciertos</strong> &bull; Racha activa: Melgar, PSG & Real Madrid</div>',
        html
    )

    html = re.sub(
        r'<div class="kpi-value" style="color: var\(--cyan\);">\+\d+\.\d+%</div>\s*<div class="kpi-subtext"><strong>\+\$[\d,]+\.\d\d USD neto</strong> sobre banca inicial de \$1,000 USD</div>',
        '<div class="kpi-value" style="color: var(--cyan);">+203.4%</div>\n                    <div class="kpi-subtext"><strong>+$2,033.52 USD neto</strong> sobre banca inicial de $1,000 USD</div>',
        html
    )

    html = re.sub(
        r'<div class="kpi-value" style="color: #c084fc;">\$[\d,]+\.\d\d</div>\s*<div class="kpi-subtext"><strong>\+\$[\d,]+\.\d\d USD neto</strong> \(\+\d+\.\d+% ROI acumulado\)</div>',
        '<div class="kpi-value" style="color: #c084fc;">$3,033.52</div>\n                    <div class="kpi-subtext"><strong>+$2,033.52 USD neto</strong> (+203.4% ROI acumulado)</div>',
        html
    )

    html = re.sub(
        r'<span style="font-size: 0\.8rem; color: #10b981; font-weight: 700;">\+\$[\d,]+\.\d\d Ganancia Neta</span>',
        '<span style="font-size: 0.8rem; color: #10b981; font-weight: 700;">+$2,033.52 Ganancia Neta</span>',
        html
    )
    html = re.sub(
        r'<span style="font-size: 0\.8rem; color: var\(--gold\); font-weight: 700;">La Fija: \d+\.\d+% \(\d+/\d+\)</span>',
        '<span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">La Fija: 86.9% (153/176)</span>',
        html
    )

    # 2. Reemplazar filas de la tabla de auditoría si ya existían #212 a #217 o inyectar
    # Si ya existía #212, reemplazar desde #212 hasta el final de #217
    idx_212 = html.find('>#212</td>')
    if idx_212 != -1:
        # Encontrar el inicio de esa fila
        tr_start_212 = html.rfind('<tr', 0, idx_212)
        # Encontrar el fin de #217
        idx_217 = html.find('>#217</td>')
        if idx_217 != -1:
            tr_end_217 = html.find('</tr>', idx_217) + 5
            html = html[:tr_start_212] + new_table_rows.strip() + html[tr_end_217:]
            print(f"Replaced rows #212-#217 with REAL scores in {fpath}")
    else:
        # Inyectar después de #211
        idx_211 = html.find('>#211</td>')
        if idx_211 != -1:
            idx_tr_end = html.find('</tr>', idx_211) + 5
            html = html[:idx_tr_end] + '\n' + new_table_rows + html[idx_tr_end:]
            print(f"Injected rows #212-#217 into {fpath}")

    # 3. Ciclo #133 en la tabla de autoaprendizaje
    idx_c133 = html.find('Ciclo #133')
    if idx_c133 != -1:
        # Reemplazar la fila existente de Ciclo #133
        tr_start_c133 = html.rfind('<tr', 0, idx_c133)
        tr_end_c133 = html.find('</tr>', idx_c133) + 5
        html = html[:tr_start_c133] + cycle133_row.strip() + html[tr_end_c133:]
        print(f"Updated Ciclo #133 in {fpath}")
    else:
        # Inyectar arriba de Ciclo #132
        idx_c132 = html.find('Ciclo #132')
        if idx_c132 != -1:
            idx_tr_start = html.rfind('<tr', 0, idx_c132)
            html = html[:idx_tr_start] + cycle133_row + html[idx_tr_start:]
            print(f"Injected Ciclo #133 into {fpath}")

    # 4. rawPoints
    html = re.sub(
        r'var rawPoints = \[[^\]]+\];',
        f'var rawPoints = {points_json};',
        html
    )

    # 5. chart category
    html = re.sub(
        r'data:\s*\[\d+\.\d+,\s*100\.0,\s*90\.0,\s*75\.0,\s*75\.0\]',
        'data: [86.9, 100.0, 90.0, 75.0, 75.0]',
        html
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Saved {fpath} successfully.")

print("AUDITORÍA CON MARCADORES REALES VERIFICADOS APLICADA CON ÉXITO!")

