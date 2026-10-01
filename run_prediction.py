"""
Script Principal de Ejecución de Pronósticos Deportivos con TimesFM
Ejecuta la suite multi-agente para España vs Croacia e Inglaterra vs Chequia,
imprime el reporte en consola y compila el Dashboard HTML interactivo.
"""

import json
import os
from sports_agents import SportsDirectorAgent


def generate_html_dashboard(data: dict, output_path: str):
    matches = data["matches"]
    
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SportsAI - Pronósticos TimesFM</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-primary: #07090e;
            --bg-card: rgba(18, 24, 38, 0.75);
            --bg-card-hover: rgba(26, 34, 52, 0.85);
            --border-glass: rgba(255, 255, 255, 0.08);
            --accent-blue: #3b82f6;
            --accent-cyan: #06b6d4;
            --accent-amber: #f59e0b;
            --accent-emerald: #10b981;
            --accent-rose: #f43f5e;
            --accent-purple: #8b5cf6;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-primary);
            color: var(--text-main);
            min-height: 100vh;
            background-image: 
                radial-gradient(circle at 15% 20%, rgba(59, 130, 246, 0.12) 0%, transparent 40%),
                radial-gradient(circle at 85% 70%, rgba(139, 92, 246, 0.12) 0%, transparent 40%);
            padding: 2.5rem 1.5rem;
        }}

        .container {{
            max-width: 1280px;
            margin: 0 auto;
        }}

        header {{
            text-align: center;
            margin-bottom: 2.5rem;
        }}

        .badge-model {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(59, 130, 246, 0.15);
            border: 1px solid rgba(59, 130, 246, 0.3);
            color: #60a5fa;
            padding: 0.35rem 1rem;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 1rem;
        }}

        h1 {{
            font-size: 2.75rem;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 0%, #94a3b8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            letter-spacing: -0.02em;
        }}

        .subtitle {{
            color: var(--text-muted);
            font-size: 1.1rem;
            max-width: 650px;
            margin: 0 auto;
        }}

        .tabs {{
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 2.5rem;
        }}

        .tab-btn {{
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            color: var(--text-muted);
            font-family: inherit;
            font-size: 1.05rem;
            font-weight: 600;
            padding: 0.85rem 1.85rem;
            border-radius: 14px;
            cursor: pointer;
            transition: all 0.25s ease;
            backdrop-filter: blur(12px);
        }}

        .tab-btn.active {{
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.25), rgba(139, 92, 246, 0.25));
            border-color: rgba(96, 165, 250, 0.5);
            color: #ffffff;
            box-shadow: 0 8px 24px -6px rgba(59, 130, 246, 0.3);
        }}

        .match-view {{
            display: none;
            animation: fadeIn 0.4s ease forwards;
        }}

        .match-view.active {{
            display: block;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(8px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* Hero Score Section */
        .hero-banner {{
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 24px;
            padding: 2.5rem 2rem;
            backdrop-filter: blur(16px);
            margin-bottom: 2rem;
            box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
            position: relative;
            overflow: hidden;
        }}

        .hero-banner::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--accent-blue), var(--accent-cyan), var(--accent-purple));
        }}

        .matchup-grid {{
            display: grid;
            grid-template-columns: 1fr auto 1fr;
            align-items: center;
            gap: 2rem;
            text-align: center;
        }}

        .team-title {{
            font-size: 2.2rem;
            font-weight: 800;
            letter-spacing: -0.01em;
        }}

        .team-meta {{
            color: var(--text-muted);
            font-size: 0.95rem;
            margin-top: 0.25rem;
        }}

        .score-box {{
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 1.25rem 2.25rem;
        }}

        .score-label {{
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--accent-cyan);
            font-weight: 700;
            margin-bottom: 0.25rem;
        }}

        .predicted-score {{
            font-size: 3.5rem;
            font-weight: 800;
            font-family: 'JetBrains Mono', monospace;
            color: #ffffff;
            line-height: 1;
        }}

        .score-confidence {{
            font-size: 0.85rem;
            color: var(--accent-emerald);
            margin-top: 0.4rem;
            font-weight: 600;
        }}

        /* Grid layout for analytics cards */
        .analytics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}

        .card {{
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            padding: 1.75rem;
            backdrop-filter: blur(12px);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}

        .card:hover {{
            border-color: rgba(255, 255, 255, 0.15);
            transform: translateY(-2px);
        }}

        .card-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.25rem;
            padding-bottom: 0.85rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        }}

        .card-title {{
            font-size: 1.2rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }}

        .card-badge {{
            font-size: 0.75rem;
            padding: 0.2rem 0.6rem;
            border-radius: 6px;
            font-weight: 600;
            background: rgba(255, 255, 255, 0.06);
            color: var(--text-muted);
        }}

        /* Probability Bars */
        .prob-bar-container {{
            margin-bottom: 1rem;
        }}

        .prob-bar-labels {{
            display: flex;
            justify-content: space-between;
            font-size: 0.9rem;
            margin-bottom: 0.35rem;
        }}

        .prob-bar-bg {{
            height: 10px;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 9999px;
            overflow: hidden;
        }}

        .prob-bar-fill {{
            height: 100%;
            border-radius: 9999px;
            transition: width 0.8s ease;
        }}

        /* Table styles */
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9rem;
        }}

        th {{
            text-align: left;
            padding: 0.6rem 0.5rem;
            color: var(--text-muted);
            font-weight: 600;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            font-size: 0.8rem;
            text-transform: uppercase;
        }}

        td {{
            padding: 0.75rem 0.5rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.04);
        }}

        tr:last-child td {{
            border-bottom: none;
        }}

        .stat-highlight {{
            font-family: 'JetBrains Mono', monospace;
            font-weight: 700;
            color: #ffffff;
        }}

        .tag-pill {{
            display: inline-block;
            padding: 0.2rem 0.5rem;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 600;
        }}

        .tag-yellow {{ background: rgba(245, 158, 11, 0.18); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }}
        .tag-red {{ background: rgba(244, 63, 94, 0.18); color: #fb7185; border: 1px solid rgba(244, 63, 94, 0.3); }}
        .tag-blue {{ background: rgba(59, 130, 246, 0.18); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }}

        footer {{
            text-align: center;
            margin-top: 3rem;
            color: var(--text-muted);
            font-size: 0.85rem;
            padding-top: 1.5rem;
            border-top: 1px solid var(--border-glass);
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="badge-model">⚡ Google TimesFM Foundation Model + Multi-Agent AI</div>
            <h1>Sistema Inteligente de Pronósticos de Fútbol</h1>
            <p class="subtitle">Análisis predictivo multivariado de series temporales, simulación Monte Carlo y proyección de marcadores, córners, tarjetas y figuras clave.</p>
        </header>

        <div class="tabs">
            <button class="tab-btn active" onclick="switchMatch(0)">🇪🇸 España vs Croacia 🇭🇷</button>
            <button class="tab-btn" onclick="switchMatch(1)">🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra vs Chequia 🇨🇿</button>
        </div>
    """

    for idx, match in enumerate(matches):
        active_class = "active" if idx == 0 else ""
        home = match["home_team"]
        away = match["away_team"]
        score_data = match["score_prediction"]
        corners = match["corners_prediction"]
        cards = match["cards_prediction"]
        props = match["player_props"]
        context = match["context"]

        html += f"""
        <div id="match-view-{idx}" class="match-view {active_class}">
            <!-- Hero Banner -->
            <div class="hero-banner">
                <div class="matchup-grid">
                    <div>
                        <div class="team-title">{home}</div>
                        <div class="team-meta">xG Esperado: <span class="stat-highlight">{match['projections']['expected_goals']['home']}</span></div>
                    </div>
                    <div>
                        <div class="score-box">
                            <div class="score-label">Marcador Más Probable</div>
                            <div class="predicted-score">{score_data['most_probable_score']}</div>
                            <div class="score-confidence">Confianza: {score_data['most_probable_prob_pct']}%</div>
                        </div>
                    </div>
                    <div>
                        <div class="team-title">{away}</div>
                        <div class="team-meta">xG Esperado: <span class="stat-highlight">{match['projections']['expected_goals']['away']}</span></div>
                    </div>
                </div>
            </div>

            <!-- Analytics Grid -->
            <div class="analytics-grid">
                <!-- Card 1: Probabilidad 1X2 y Marcadores Top -->
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">🎯 Marcador & Resultado 1X2</div>
                        <span class="card-badge">Monte Carlo 10k</span>
                    </div>

                    <div class="prob-bar-container">
                        <div class="prob-bar-labels">
                            <span>Victoria {home} (1)</span>
                            <span class="stat-highlight">{score_data['1x2_probabilities']['home_win_pct']}%</span>
                        </div>
                        <div class="prob-bar-bg">
                            <div class="prob-bar-fill" style="width: {score_data['1x2_probabilities']['home_win_pct']}%; background: var(--accent-emerald);"></div>
                        </div>
                    </div>

                    <div class="prob-bar-container">
                        <div class="prob-bar-labels">
                            <span>Empate (X)</span>
                            <span class="stat-highlight">{score_data['1x2_probabilities']['draw_pct']}%</span>
                        </div>
                        <div class="prob-bar-bg">
                            <div class="prob-bar-fill" style="width: {score_data['1x2_probabilities']['draw_pct']}%; background: var(--accent-amber);"></div>
                        </div>
                    </div>

                    <div class="prob-bar-container">
                        <div class="prob-bar-labels">
                            <span>Victoria {away} (2)</span>
                            <span class="stat-highlight">{score_data['1x2_probabilities']['away_win_pct']}%</span>
                        </div>
                        <div class="prob-bar-bg">
                            <div class="prob-bar-fill" style="width: {score_data['1x2_probabilities']['away_win_pct']}%; background: var(--accent-blue);"></div>
                        </div>
                    </div>

                    <div style="margin-top: 1.25rem;">
                        <div style="font-size: 0.85rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-bottom: 0.5rem;">Top 5 Marcadores Exactos</div>
                        <table>
                            <thead>
                                <tr>
                                    <th>Marcador</th>
                                    <th style="text-align: right;">Probabilidad</th>
                                </tr>
                            </thead>
                            <tbody>
        """
        for sc in score_data["top_5_scores"]:
            html += f"""
                                <tr>
                                    <td><strong style="color: #ffffff;">{sc['score']}</strong></td>
                                    <td style="text-align: right;" class="stat-highlight">{sc['probability_pct']}%</td>
                                </tr>
            """

        html += f"""
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Card 2: Esquinas / Córners -->
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">🚩 Córners (Esquinas)</div>
                        <span class="card-badge">TimesFM Cuantiles</span>
                    </div>

                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.25rem;">
                        <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-glass); border-radius: 14px; padding: 1rem; text-align: center;">
                            <div style="font-size: 0.8rem; color: var(--text-muted);">Córners {home}</div>
                            <div class="predicted-score" style="font-size: 2rem;">{corners['home_corners_expected']}</div>
                            <div style="font-size: 0.75rem; color: var(--accent-cyan);">Rango: {match['projections']['expected_corners']['home_quantiles']['p10']} - {match['projections']['expected_corners']['home_quantiles']['p90']}</div>
                        </div>
                        <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-glass); border-radius: 14px; padding: 1rem; text-align: center;">
                            <div style="font-size: 0.8rem; color: var(--text-muted);">Córners {away}</div>
                            <div class="predicted-score" style="font-size: 2rem;">{corners['away_corners_expected']}</div>
                            <div style="font-size: 0.75rem; color: var(--accent-cyan);">Rango: {match['projections']['expected_corners']['away_quantiles']['p10']} - {match['projections']['expected_corners']['away_quantiles']['p90']}</div>
                        </div>
                    </div>

                    <div style="background: rgba(59, 130, 246, 0.08); border: 1px solid rgba(59, 130, 246, 0.2); border-radius: 12px; padding: 0.85rem; text-align: center; margin-bottom: 1.25rem;">
                        <span style="color: #93c5fd; font-size: 0.9rem;">Total Esquinas Proyectadas:</span>
                        <strong style="color: #ffffff; font-size: 1.3rem; margin-left: 0.5rem;">{corners['total_corners_expected']}</strong>
                        <span style="font-size: 0.8rem; color: var(--text-muted); display: block; margin-top: 0.2rem;">Rango modal: {corners['most_likely_range']}</span>
                    </div>

                    <table>
                        <thead>
                            <tr>
                                <th>Línea de Córners</th>
                                <th style="text-align: right;">Prob. Over</th>
                                <th style="text-align: right;">Prob. Under</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Más de 8.5 Córners</td>
                                <td style="text-align: right;" class="stat-highlight">{corners['lines']['over_8_5_pct']}%</td>
                                <td style="text-align: right;" style="color: var(--text-muted);">{corners['lines']['under_8_5_pct']}%</td>
                            </tr>
                            <tr>
                                <td>Más de 9.5 Córners</td>
                                <td style="text-align: right;" class="stat-highlight">{corners['lines']['over_9_5_pct']}%</td>
                                <td style="text-align: right;" style="color: var(--text-muted);">{corners['lines']['under_9_5_pct']}%</td>
                            </tr>
                            <tr>
                                <td>Más de 10.5 Córners</td>
                                <td style="text-align: right;" class="stat-highlight">{corners['lines']['over_10_5_pct']}%</td>
                                <td style="text-align: right;" style="color: var(--text-muted);">{corners['lines']['under_10_5_pct']}%</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Card 3: Disciplina y Tarjetas -->
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">🟨 Tarjetas & Disciplina</div>
                        <span class="card-badge">Árbitro: {cards['referee']}</span>
                    </div>

                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.25rem;">
                        <div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.2); border-radius: 14px; padding: 1rem; text-align: center;">
                            <div style="font-size: 0.8rem; color: #fbbf24;">Amarillas {home}</div>
                            <div class="predicted-score" style="font-size: 2rem; color: #fbbf24;">{cards['home_yellow_cards']}</div>
                        </div>
                        <div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.2); border-radius: 14px; padding: 1rem; text-align: center;">
                            <div style="font-size: 0.8rem; color: #fbbf24;">Amarillas {away}</div>
                            <div class="predicted-score" style="font-size: 2rem; color: #fbbf24;">{cards['away_yellow_cards']}</div>
                        </div>
                    </div>

                    <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(244, 63, 94, 0.08); border: 1px solid rgba(244, 63, 94, 0.2); border-radius: 12px; padding: 0.85rem 1rem; margin-bottom: 1.25rem;">
                        <div>
                            <div style="font-weight: 700; color: #fda4af;">Riesgo de Tarjeta Roja</div>
                            <div style="font-size: 0.75rem; color: var(--text-muted);">Probabilidad de expulsión en 90 min</div>
                        </div>
                        <div class="tag-pill tag-red" style="font-size: 1rem; padding: 0.35rem 0.75rem;">
                            {cards['red_cards']['any_red_card_in_match_pct']}%
                        </div>
                    </div>

                    <table>
                        <thead>
                            <tr>
                                <th>Línea de Tarjetas Totales</th>
                                <th style="text-align: right;">Probabilidad</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Total Tarjetas Estimadas</td>
                                <td style="text-align: right;" class="stat-highlight">{cards['total_cards_expected']}</td>
                            </tr>
                            <tr>
                                <td>Más de 3.5 Tarjetas</td>
                                <td style="text-align: right;" class="stat-highlight">{cards['card_lines']['over_3_5_cards_pct']}%</td>
                            </tr>
                            <tr>
                                <td>Más de 4.5 Tarjetas</td>
                                <td style="text-align: right;" class="stat-highlight">{cards['card_lines']['over_4_5_cards_pct']}%</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Card 4: Tiros de Jugadores Clave -->
            <div class="card" style="margin-bottom: 2rem;">
                <div class="card-header">
                    <div class="card-title">👟 Aporte de Tiros de los Jugadores Más Importantes</div>
                    <span class="card-badge">Shots & Shots on Target (SoT)</span>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(450px, 1fr)); gap: 1.5rem;">
                    <div>
                        <h3 style="font-size: 1.1rem; color: var(--accent-cyan); margin-bottom: 0.75rem; font-weight: 700;">Figuras de {home}</h3>
                        <table>
                            <thead>
                                <tr>
                                    <th>Jugador</th>
                                    <th style="text-align: center;">Tiros Exp.</th>
                                    <th style="text-align: center;">Tiros Puerta</th>
                                    <th style="text-align: right;">+0.5 Tiros Arco</th>
                                    <th style="text-align: right;">Gol</th>
                                </tr>
                            </thead>
                            <tbody>
        """
        for p in props["home_key_players"]:
            html += f"""
                                <tr>
                                    <td><strong>{p['name']}</strong><br><small style="color: var(--text-muted);">{p['position']}</small></td>
                                    <td style="text-align: center;" class="stat-highlight">{p['expected_shots']}</td>
                                    <td style="text-align: center;"><span class="tag-pill tag-blue">{p['expected_sot']}</span></td>
                                    <td style="text-align: right;" class="stat-highlight">{p['prob_at_least_1_sot_pct']}%</td>
                                    <td style="text-align: right; color: var(--accent-emerald); font-weight: 600;">{p['goal_anytime_prob_pct']}%</td>
                                </tr>
            """
        html += f"""
                            </tbody>
                        </table>
                    </div>

                    <div>
                        <h3 style="font-size: 1.1rem; color: var(--accent-amber); margin-bottom: 0.75rem; font-weight: 700;">Figuras de {away}</h3>
                        <table>
                            <thead>
                                <tr>
                                    <th>Jugador</th>
                                    <th style="text-align: center;">Tiros Exp.</th>
                                    <th style="text-align: center;">Tiros Puerta</th>
                                    <th style="text-align: right;">+0.5 Tiros Arco</th>
                                    <th style="text-align: right;">Gol</th>
                                </tr>
                            </thead>
                            <tbody>
        """
        for p in props["away_key_players"]:
            html += f"""
                                <tr>
                                    <td><strong>{p['name']}</strong><br><small style="color: var(--text-muted);">{p['position']}</small></td>
                                    <td style="text-align: center;" class="stat-highlight">{p['expected_shots']}</td>
                                    <td style="text-align: center;"><span class="tag-pill tag-blue">{p['expected_sot']}</span></td>
                                    <td style="text-align: right;" class="stat-highlight">{p['prob_at_least_1_sot_pct']}%</td>
                                    <td style="text-align: right; color: var(--accent-emerald); font-weight: 600;">{p['goal_anytime_prob_pct']}%</td>
                                </tr>
            """
        html += f"""
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        """

    html += """
        <footer>
            Desarrollado con el ecosistema de Google DeepMind / Google Research TimesFM &middot; Arquitectura Multi-Agente Autónoma
        </footer>
    </div>

    <script>
        function switchMatch(index) {
            document.querySelectorAll('.tab-btn').forEach((btn, i) => {
                btn.classList.toggle('active', i === index);
            });
            document.querySelectorAll('.match-view').forEach((view, i) => {
                view.classList.toggle('active', i === index);
            });
        }
    </script>
</body>
</html>
    """
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Dashboard HTML generado exitosamente en: {output_path}")


def main():
    print("=================================================================")
    print(" INICIANDO SUITE DE INTELIGENCIA DEPORTIVA CON TIMESFM")
    print("=================================================================")
    director = SportsDirectorAgent()
    results = director.run_all()

    # Guardar JSON con todas las predicciones
    json_path = os.path.join(os.path.dirname(__file__), "predicciones_resultados.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"[OK] Archivo JSON de predicciones guardado en: {json_path}")

    # Generar Dashboard HTML interactivo
    html_path = os.path.join(os.path.dirname(__file__), "dashboard_pronosticos.html")
    generate_html_dashboard(results, html_path)

    # Imprimir resumen de consola
    for match in results["matches"]:
        print("\n-----------------------------------------------------------------")
        print(f" PARTIDO: {match['match']}")
        print("-----------------------------------------------------------------")
        sc = match["score_prediction"]
        print(f" -> Marcador Más Probable: {sc['most_probable_score']} ({sc['most_probable_prob_pct']}%)")
        print(f" -> 1X2: Local {sc['1x2_probabilities']['home_win_pct']}% | Empate {sc['1x2_probabilities']['draw_pct']}% | Visitante {sc['1x2_probabilities']['away_win_pct']}%")
        
        cn = match["corners_prediction"]
        print(f" -> Córners: {match['home_team']} {cn['home_corners_expected']} | {match['away_team']} {cn['away_corners_expected']} | Total: {cn['total_corners_expected']}")
        print(f" -> Líneas Córners: Over 8.5 ({cn['lines']['over_8_5_pct']}%) | Over 9.5 ({cn['lines']['over_9_5_pct']}%)")
        
        cd = match["cards_prediction"]
        print(f" -> Tarjetas: {match['home_team']} {cd['home_yellow_cards']} Amarillas | {match['away_team']} {cd['away_yellow_cards']} Amarillas | Total Exp: {cd['total_cards_expected']}")
        print(f" -> Prob. Tarjeta Roja en el partido: {cd['red_cards']['any_red_card_in_match_pct']}%")


if __name__ == "__main__":
    main()
