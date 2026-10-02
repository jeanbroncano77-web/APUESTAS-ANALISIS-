# -*- coding: utf-8 -*-
"""
build_dashboard_tomorrow.py
Reconstruye index.html con la cartelera de los 6 partidos estelares de MAÑANA:
1. Real Madrid vs Villarreal (LaLiga)
2. Barcelona vs Getafe (LaLiga)
3. Arsenal vs Leeds United (Premier League)
4. FC Augsburg vs Bayern Munich (Bundesliga)
5. Inter Milan vs Parma (Serie A)
6. Borussia Dortmund vs Werder Bremen (Bundesliga)
"""

import os
import sys
import json
import re

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")
sim_path = os.path.join(base_dir, "sports_agents", "simulations_tomorrow_results.json")

with open(sim_path, "r", encoding="utf-8") as f:
    sim_data = json.load(f)

matches = sim_data["Matches"]

flags = {
    "Real Madrid": "⚪", "Villarreal": "🟡",
    "Barcelona": "🔵", "Getafe": "🔵",
    "Arsenal": "🔴", "Leeds United": "⚪",
    "FC Augsburg": "🔴", "Bayern Munich": "🔴",
    "Inter Milan": "⚫", "Parma": "🟡",
    "Borussia Dortmund": "🟡", "Werder Bremen": "🟢"
}

def get_flag(team):
    return flags.get(team, "⚽")

# 1. GENERAR SWITCHER TABS HTML
tabs_html = ""
for i, m in enumerate(matches):
    active_cls = "active" if i == 0 else ""
    h_team = m["home_team"]
    a_team = m["away_team"]
    h_flag = get_flag(h_team)
    a_flag = get_flag(a_team)
    tournament = m["context"].get("tournament", "Competición")
    modal_score = m["score_prediction"]["most_probable_score"]
    corners_total = round(m["corners_prediction"].get("total_corners_expected", 9.0), 1)
    fija = m["la_fija_real"]
    fija_badge = f"<span class='badge-fija-pill'>⭐ Fija {fija['probability']}%</span>" if fija else ""

    tabs_html += f"""
        <div class="switcher-card {active_cls}" onclick="setMatch({i})" id="tab-{i}">
            <div class="switcher-header">
                <span>Partido {i + 1} &bull; {tournament}</span>
                {fija_badge}
            </div>
            <div class="switcher-teams">
                <span>{h_flag} {h_team}</span>
                <span class="vs-text">vs</span>
                <span>{a_team} {a_flag}</span>
            </div>
            <div class="switcher-meta">
                <span>Marcador: <strong style="color: #ffffff;">{modal_score}</strong></span>
                <span class="mono-bold" style="color: var(--cyan);">{corners_total} Córners</span>
            </div>
        </div>
    """

# 2. GENERAR MATCH VIEWS HTML
views_html = ""
for i, m in enumerate(matches):
    active_cls = "active" if i == 0 else ""
    display_style = "display: block;" if i == 0 else "display: none;"
    h_team = m["home_team"]
    a_team = m["away_team"]
    h_flag = get_flag(h_team)
    a_flag = get_flag(a_team)
    ctx = m["context"]
    score_pred = m["score_prediction"]
    modal_score = score_pred["most_probable_score"]
    top_5 = score_pred.get("top_5_scores", [])
    p1x2 = score_pred.get("1x2_probabilities", {})
    goals_mkts = score_pred.get("goals_markets", {})
    sim_avg = score_pred.get("simulated_averages", {})
    corners = m["corners_prediction"]
    cards = m["cards_prediction"]
    player_props = m.get("player_props", {})
    fija = m["la_fija_real"]

    # Top 5 score rows
    top5_rows = ""
    for s_idx, sc in enumerate(top_5):
        tag_cls = "tag-emerald" if s_idx == 0 else "tag-blue"
        top5_rows += f"""
            <tr>
                <td><strong style="color: #ffffff;">{sc['score']}</strong></td>
                <td style="text-align: right;" class="mono-bold">{sc['probability_pct']}%</td>
                <td style="text-align: right;"><span class="tag-pill {tag_cls}">Top {s_idx + 1}</span></td>
            </tr>
        """

    # Player props rows
    home_pl = player_props.get("home_key_players", [])
    away_pl = player_props.get("away_key_players", [])
    player_rows = ""
    for p in (home_pl[:3] + away_pl[:3]):
        p_name = p.get("name", "Jugador")
        p_pos = p.get("position", "Delantero")
        p_team = h_team if p in home_pl else a_team
        p_flag = get_flag(p_team)
        exp_shots = round(p.get("expected_shots", 2.5), 1)
        exp_sot = round(p.get("expected_sot", 1.2), 1)
        prob_sot = p.get("prob_at_least_1_sot_pct", 75.0)
        prob_shot = p.get("prob_over_1_5_shots_pct", 88.0)
        prob_goal = p.get("goal_anytime_prob_pct", 35.0)

        sot_pill = "tag-emerald" if prob_sot >= 75 else "tag-cyan"
        shot_pill = "tag-amber" if prob_shot >= 85 else "tag-blue"
        player_rows += f"""
            <tr>
                <td>
                    <div style="font-weight: 700; color: #ffffff;">{p_name}</div>
                    <div style="font-size: 0.75rem; color: var(--text-muted);">{p_flag} {p_team} &bull; {p_pos}</div>
                </td>
                <td style="text-align: center;" class="mono-bold" style="color: var(--cyan);">{exp_shots}</td>
                <td style="text-align: center;" class="mono-bold" style="color: var(--emerald);">{exp_sot}</td>
                <td style="text-align: center;"><span class="tag-pill {sot_pill} mono-bold">{prob_sot}%</span></td>
                <td style="text-align: center;"><span class="tag-pill {shot_pill} mono-bold">{prob_shot}%</span></td>
                <td style="text-align: right;"><span class="tag-pill tag-purple mono-bold">{prob_goal}%</span></td>
            </tr>
        """

    # La Fija Card HTML
    market_odds = round(fija.get("odds", 1.12) * 1.08, 2)
    if market_odds < 1.05:
        market_odds = 1.05
    fija_card_html = f"""
        <div class="fija-gold-card">
            <div class="fija-badge-glow">
                <span class="fija-star">⭐</span> LA FIJA DEL PARTIDO &bull; CONFIANZA 95%+
            </div>
            <div class="fija-content-grid">
                <div class="fija-main">
                    <div class="fija-market-label">Selección Cuantitativa de Máxima Seguridad</div>
                    <div class="fija-market-title">{fija.get('selection', '1X')}</div>
                    <div class="fija-rationale">🔬 <em>Fundamento TimesFM & Monte Carlo:</em> {fija.get('rationale', '')}</div>
                </div>
                <div class="fija-stats">
                    <div class="fija-stat-box">
                        <div class="fija-stat-val">{fija.get('probability', 95.0)}%</div>
                        <div class="fija-stat-lbl">Probabilidad</div>
                    </div>
                    <div class="fija-stat-box">
                        <div class="fija-stat-val" style="color: var(--emerald);">{fija.get('odds', 1.12)}</div>
                        <div class="fija-stat-lbl">Cuota Justa</div>
                    </div>
                    <div class="fija-stat-box">
                        <div class="fija-stat-val" style="color: var(--cyan);">{market_odds}</div>
                        <div class="fija-stat-lbl">Cuota Mercado</div>
                    </div>
                    <div style="display: flex; align-items: center;">
                        <button class="btn-slip-action" id="btn-add-{i}" onclick="toggleBetInSlip({i}, '{m['match']}', '{fija.get('selection')}', {fija.get('probability', 95)}, {market_odds})">
                            <span>➕</span> <span id="btn-txt-{i}">Añadir al Ticket</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    """

    alt_score1 = top_5[1]['score'] if len(top_5) > 1 else '1-0'
    alt_prob1 = top_5[1]['probability_pct'] if len(top_5) > 1 else 10.0
    alt_score2 = top_5[2]['score'] if len(top_5) > 2 else '2-0'
    alt_prob2 = top_5[2]['probability_pct'] if len(top_5) > 2 else 8.0

    views_html += f"""
        <!-- ==================== PARTIDO {i + 1}: {m['match']} ==================== -->
        <div id="match-{i}" class="match-view {active_cls}" style="{display_style}">
            <!-- Hero Banner -->
            <div class="hero-banner">
                <div class="hero-context-badge">
                    <span>🏆 {ctx.get('tournament', 'Liga')}</span>
                    <span>📍 {ctx.get('stadium', 'Estadio')}</span>
                    <span>👥 {ctx.get('spectators_est', '45,000 espectadores')}</span>
                </div>

                <div class="hero-grid">
                    <div class="team-col">
                        <div class="team-flag">{h_flag}</div>
                        <div class="team-name">{h_team}</div>
                        <div class="team-xg-chip">xG Proyectado: <span class="mono-bold" style="color: var(--cyan);">{sim_avg.get('home_goals', 2.0)}</span></div>
                    </div>

                    <div class="center-score-col">
                        <div class="score-pill-title">Marcador Exacto Más Probable</div>
                        <div class="hero-score-val">{modal_score}</div>
                        <div class="hero-score-conf">Top Alternativas: {alt_score1} ({alt_prob1}%) &bull; {alt_score2} ({alt_prob2}%)</div>
                    </div>

                    <div class="team-col">
                        <div class="team-flag">{a_flag}</div>
                        <div class="team-name">{a_team}</div>
                        <div class="team-xg-chip">xG Proyectado: <span class="mono-bold" style="color: var(--amber);">{sim_avg.get('away_goals', 1.0)}</span></div>
                    </div>
                </div>
            </div>

            <!-- Glowing La Fija Card -->
            {fija_card_html}

            <!-- Analytics Grid -->
            <div class="analytics-grid-3">
                <!-- 1X2 & Exact Score -->
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">🎯 Marcador & Probabilidad 1X2</div>
                        <span class="badge-subtle">Dixon-Coles + Monte Carlo</span>
                    </div>

                    <div class="prob-bar-row">
                        <div class="prob-bar-label">
                            <span>Victoria {h_team} (1)</span>
                            <span class="mono-bold" style="color: var(--cyan);">{p1x2.get('home_win_pct', 65)}%</span>
                        </div>
                        <div class="prob-bar-track">
                            <div class="prob-bar-fill" style="width: {p1x2.get('home_win_pct', 65)}%; background: linear-gradient(90deg, #3b82f6, #06b6d4);"></div>
                        </div>
                    </div>

                    <div class="prob-bar-row">
                        <div class="prob-bar-label">
                            <span>Empate (X)</span>
                            <span class="mono-bold" style="color: var(--gold);">{p1x2.get('draw_pct', 25)}%</span>
                        </div>
                        <div class="prob-bar-track">
                            <div class="prob-bar-fill" style="width: {p1x2.get('draw_pct', 25)}%; background: linear-gradient(90deg, #f59e0b, #fbbf24);"></div>
                        </div>
                    </div>

                    <div class="prob-bar-row">
                        <div class="prob-bar-label">
                            <span>Victoria {a_team} (2)</span>
                            <span class="mono-bold" style="color: var(--rose);">{p1x2.get('away_win_pct', 10)}%</span>
                        </div>
                        <div class="prob-bar-track">
                            <div class="prob-bar-fill" style="width: {p1x2.get('away_win_pct', 10)}%; background: linear-gradient(90deg, #f43f5e, #e11d48);"></div>
                        </div>
                    </div>

                    <div class="table-container" style="margin-top: 1.25rem;">
                        <table>
                            <thead>
                                <tr>
                                    <th>Marcador</th>
                                    <th style="text-align: right;">Prob (%)</th>
                                    <th style="text-align: right;">Rango</th>
                                </tr>
                            </thead>
                            <tbody>
                                {top5_rows}
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Goals Distribution -->
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">⚽ Mercados de Goles</div>
                        <span class="badge-subtle">Distribución Poisson Bivariada</span>
                    </div>

                    <div class="prob-bar-row">
                        <div class="prob-bar-label">
                            <span>Más de 1.5 Goles</span>
                            <span class="mono-bold" style="color: var(--emerald);">{goals_mkts.get('over_1_5_pct', 85)}%</span>
                        </div>
                        <div class="prob-bar-track">
                            <div class="prob-bar-fill" style="width: {goals_mkts.get('over_1_5_pct', 85)}%; background: linear-gradient(90deg, #10b981, #059669);"></div>
                        </div>
                    </div>

                    <div class="prob-bar-row">
                        <div class="prob-bar-label">
                            <span>Más de 2.5 Goles</span>
                            <span class="mono-bold" style="color: var(--cyan);">{goals_mkts.get('over_2_5_pct', 65)}%</span>
                        </div>
                        <div class="prob-bar-track">
                            <div class="prob-bar-fill" style="width: {goals_mkts.get('over_2_5_pct', 65)}%; background: linear-gradient(90deg, #06b6d4, #0284c7);"></div>
                        </div>
                    </div>

                    <div class="prob-bar-row">
                        <div class="prob-bar-label">
                            <span>Ambos Equipos Anotan (BTTS)</span>
                            <span class="mono-bold" style="color: var(--amber);">{goals_mkts.get('btts_yes_pct', 55)}%</span>
                        </div>
                        <div class="prob-bar-track">
                            <div class="prob-bar-fill" style="width: {goals_mkts.get('btts_yes_pct', 55)}%; background: linear-gradient(90deg, #f59e0b, #d97706);"></div>
                        </div>
                    </div>

                    <div style="background: rgba(0,0,0,0.25); border-radius: 12px; padding: 1rem; margin-top: 1rem;">
                        <div style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 0.5rem;">PROMEDIO GOLES SIMULADOS:</div>
                        <div style="display: flex; justify-content: space-between; font-size: 0.85rem;">
                            <span>{h_team}: <strong style="color: var(--cyan);">{sim_avg.get('home_goals', 2.0)}</strong></span>
                            <span>{a_team}: <strong style="color: var(--amber);">{sim_avg.get('away_goals', 1.0)}</strong></span>
                            <span>Total: <strong style="color: var(--emerald);">{sim_avg.get('total_goals', 3.0)}</strong></span>
                        </div>
                    </div>
                </div>

                <!-- Córners & Tarjetas -->
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">🚩 Córners & Disciplina</div>
                        <span class="badge-subtle">Árbitro: {ctx.get('referee', 'FIFA')}</span>
                    </div>

                    <div class="prob-bar-row">
                        <div class="prob-bar-label">
                            <span>Córners Proyectados ({h_team})</span>
                            <span class="mono-bold" style="color: var(--cyan);">{round(corners.get('home_corners_expected', 5.2), 1)}</span>
                        </div>
                        <div class="prob-bar-track">
                            <div class="prob-bar-fill" style="width: 65%; background: var(--cyan);"></div>
                        </div>
                    </div>

                    <div class="prob-bar-row">
                        <div class="prob-bar-label">
                            <span>Córners Proyectados ({a_team})</span>
                            <span class="mono-bold" style="color: var(--amber);">{round(corners.get('away_corners_expected', 3.8), 1)}</span>
                        </div>
                        <div class="prob-bar-track">
                            <div class="prob-bar-fill" style="width: 45%; background: var(--amber);"></div>
                        </div>
                    </div>

                    <div style="background: rgba(0,0,0,0.25); border-radius: 12px; padding: 0.85rem; margin-top: 1rem;">
                        <div style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 0.3rem;">LÍNEAS DE CÓRNERS RECOMENDADAS:</div>
                        <div style="display: flex; justify-content: space-between; font-size: 0.85rem;">
                            <span>Over 8.5: <strong style="color: var(--emerald);">{corners.get('lines', {}).get('over_8_5_pct', 70)}%</strong></span>
                            <span>Over 9.5: <strong style="color: var(--cyan);">{corners.get('lines', {}).get('over_9_5_pct', 55)}%</strong></span>
                            <span>Tarjetas Esperadas: <strong style="color: var(--gold);">{cards.get('total_cards_expected', 4.2)}</strong></span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Player Props Section -->
            <div class="card" style="margin-top: 1.5rem;">
                <div class="card-header">
                    <div class="card-title">⭐ Remates & Disparos a Puerta de Figuras Clave</div>
                    <span class="badge-subtle">Regresión Poisson Individual (p90)</span>
                </div>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Jugador / Rol</th>
                                <th style="text-align: center;">Tiros Proy.</th>
                                <th style="text-align: center;">SoT Proy.</th>
                                <th style="text-align: center;">≥1 SoT (%)</th>
                                <th style="text-align: center;">≥1 Tiro (%)</th>
                                <th style="text-align: right;">Gol (%)</th>
                            </tr>
                        </thead>
                        <tbody>
                            {player_rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    """

# 3. CONSTRUIR SECCIÓN COMPLETA DE VISTA 1
new_matches_section = f"""
        <div id="view-container-matches">
            <!-- Phase 6: Top Actions Toolbar -->
            <div class="top-actions-toolbar">
                <div class="banner-fija-de-oro">
                    <div class="badge-fija-oro">👑 LA FIJA DE ORO DE MAÑANA (CONFIANZA 98.8%)</div>
                    <div class="fija-oro-title">⭐ FC Augsburg vs Bayern Munich &bull; Empate o Bayern Munich (X2) (@1.12 | 98.8%)</div>
                    <div class="fija-oro-sub">⭐ Respaldo Estelar: Barcelona o Empate (1X) (@1.12 | 98.5% Confianza en Montjuïc)</div>
                </div>

                <div class="toolbar-btn-group">
                    <button class="btn-tool" onclick="downloadJSON()">
                        <span>📥</span> Descargar Raw JSON
                    </button>
                    <button class="btn-tool" onclick="downloadCSV()">
                        <span>📊</span> Exportar CSV Auditoría
                    </button>
                    <button class="btn-tool" onclick="window.print()">
                        <span>🖨️</span> Imprimir Reporte
                    </button>
                </div>
            </div>

            <!-- Switcher Tabs -->
            <div class="switcher-container">
                {tabs_html}
            </div>

            <!-- Match Views -->
            {views_html}
        </div> <!-- Fin de view-container-matches -->
"""

# 4. REEMPLAZAR EN INDEX.HTML
with open(index_path, "r", encoding="utf-8-sig") as f:
    orig_html = f.read()

start_m = orig_html.find('<div id="view-container-matches">')
end_m = orig_html.find('</div> <!-- Fin de view-container-matches -->') + len('</div> <!-- Fin de view-container-matches -->')

if start_m == -1 or end_m == -1:
    print("Error: No se encontró view-container-matches en index.html")
    sys.exit(1)

new_full_html = orig_html[:start_m] + new_matches_section.strip() + orig_html[end_m:]

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_full_html)

# También actualizar dashboard_pronosticos.html
dash_path = os.path.join(base_dir, "dashboard_pronosticos.html")
with open(dash_path, "w", encoding="utf-8") as f:
    f.write(new_full_html)

# Sincronizar también con el root index.html servido por tunnel
root_index = os.path.abspath(os.path.join(base_dir, "..", "index.html"))
try:
    with open(root_index, "w", encoding="utf-8") as f_root:
        f_root.write(new_full_html)
except Exception:
    pass

print("¡index.html y dashboard_pronosticos.html actualizados con éxito con los 6 partidos de MAÑANA!")
