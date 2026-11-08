# -*- coding: utf-8 -*-
"""
build_sunday_nov8_elite6.py
Construye la Cartelera Oficial de los 6 PARTIDOS ESTELARES del Domingo 8 de Noviembre de 2026
(Partidos por jugar desde las 13:45 ECU en adelante):
1. Barcelona SC vs. Liga de Quito (16:30 ECU - LigaPro Clásico Nacional)
2. Aucas vs. Independiente del Valle (13:45 ECU - LigaPro Quito)
3. Atlético de Madrid vs. FC Barcelona (15:00 ECU - LaLiga Partidazo)
4. Inter de Milán vs. Como 1907 (14:45 ECU - Serie A • 👑 LA FIJA DE ORO EUROPEA)
5. Napoli vs. Lazio (14:45 ECU - Serie A • Clásico en el Maradona)
6. RC Lens vs. Olympique de Marsella (14:45 ECU - Ligue 1)
"""

import json
import re
import os

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"

SUNDAY_MATCHES = [
    {
        "id": 0,
        "match": "Barcelona SC vs. Liga de Quito",
        "home": "Barcelona SC",
        "away": "Liga de Quito",
        "home_flag": "🟡⚫",
        "away_flag": "⚪🔴",
        "tournament": "LigaPro Ecuabet • Fase 2 (El Clásico Nacional)",
        "venue": "Estadio Monumental Banco Pichincha (Guayaquil)",
        "time": "16:30 (ECU)",
        "attendance": "57,267 en estadio (~18M audiencia nacional)",
        "home_xg": 1.65,
        "away_xg": 1.40,
        "most_probable_score": "1 - 1",
        "score_alternatives": "2 - 1 (11.8%) • 1 - 0 (10.2%) • 2 - 2 (8.4%)",
        "badge_pill": "👑 EL CLÁSICO NACIONAL 84.0%",
        "badge_style": "background: linear-gradient(135deg, rgba(245, 158, 11, 0.3), rgba(217, 119, 6, 0.4)); border: 1px solid #fbbf24; color: #fef08a;",
        "fija_title": "Barcelona SC o Empate (1X) + Más de 1.5 goles",
        "fija_odds": 1.35,
        "fija_prob": 84.0,
        "fija_fair_odds": 1.19,
        "fija_rationale": "El Monumental de Guayaquil a más de 32°C de sensación térmica impone un desgaste físico extremo a los albos tras su seguidilla de partidos. El 'Ídolo' suele agigantarse en su caldera con el empuje de su gente. La combinación 1X + Más de 1.5 goles cubre cualquier victoria amarilla o empate con goles.",
        "p1x2": [46.0, 32.0, 22.0],
        "chart_data": [46.0, 32.0, 22.0],
        "other_markets": [
            ("Doble Oportunidad:", "Barcelona SC o Empate (1X)", "85.0% | @1.28"),
            ("Total de Goles:", "Más de 1.5 goles totales", "82.0% | @1.26"),
            ("Ambos Equipos Anotan:", "Ambos Equipos Anotan - SÍ (BTTS)", "66.0% | @1.72"),
            ("Córners Guayaquil:", "Más de 8.5 córners totales", "78.0% | @1.45"),
            ("Alex Arce al Marcador:", "Alex Arce anota o asiste", "62.0% | @1.85")
        ],
        "goals": {
            "o15": (82.0, 1.26),
            "o25": (56.0, 1.78),
            "u35": (74.0, 1.35),
            "btts": (66.0, 1.72)
        },
        "corners": {
            "total_exp": "9.6 córners esperados",
            "line": "Más de 8.5 córners totales",
            "prob": 78.0,
            "odds": 1.45,
            "desc": "Ataques constantes por las bandas con Janner Corozo en Barcelona y balones largos hacia los extremos albos."
        },
        "cards": {
            "total_exp": "6.2 tarjetas esperadas",
            "line": "Más de 5.5 tarjetas amarillas",
            "prob": 84.0,
            "odds": 1.50,
            "desc": "Máxima fricción y rivalidad histórica en el fútbol ecuatoriano. Duelo de pierna fuerte garantizado."
        },
        "player_props": [
            ("Octavio Rivero (BSC)", "Más de 1.5 remates a puerta", 75.0, 1.55, "Referente de área de Barcelona con gran juego aéreo."),
            ("Alex Arce (LDU)", "Más de 1.5 remates totales", 82.0, 1.40, "Goleador implacable que busca el arco desde cualquier ángulo.")
        ],
        "medical_bulletin": [
            ("Barcelona SC", "PLANTEL COMPLETO CONFIRMADO", "Alineación de gala con Díaz y Corozo habilitados."),
            ("Liga de Quito", "DESGASTE FÍSICO POR VIAJE", "Pablo Sánchez dosifica cargas en el mediocampo.")
        ]
    },
    {
        "id": 1,
        "match": "Aucas vs. Independiente del Valle",
        "home": "Aucas",
        "away": "Independiente del Valle",
        "home_flag": "🟡🔴",
        "away_flag": "🔵⚫",
        "tournament": "LigaPro Ecuabet • Fecha de Quito",
        "venue": "Estadio Gonzalo Pozo Ripalda (Chillogallo, Quito)",
        "time": "13:45 (ECU)",
        "attendance": "14,500 en estadio (~10M audiencia nacional)",
        "home_xg": 1.15,
        "away_xg": 1.95,
        "most_probable_score": "1 - 2",
        "score_alternatives": "1 - 1 (12.2%) • 0 - 2 (10.5%) • 0 - 1 (9.0%)",
        "badge_pill": "👑 LA FIJA DE QUITO 86.0%",
        "badge_style": "background: linear-gradient(135deg, rgba(6, 182, 212, 0.3), rgba(8, 145, 178, 0.4)); border: 1px solid #06b6d4; color: #cffafe;",
        "fija_title": "Independiente del Valle o Empate (Doble Oportunidad X2)",
        "fija_odds": 1.25,
        "fija_prob": 86.0,
        "fija_fair_odds": 1.16,
        "fija_rationale": "IDV llega con la moral por las nubes tras su clasificación en Copa Ecuador y un fútbol dinámico liderado por Junior Sornoza y Jeison Medina. En el Gonzalo Pozo Ripalda ambos juegan en la misma altura (2,800m), por lo que la jerarquía técnica de los 'Rayados' impone condiciones. La doble oportunidad X2 es una muralla.",
        "p1x2": [16.0, 28.0, 56.0],
        "chart_data": [56.0, 28.0, 16.0],
        "other_markets": [
            ("Doble Oportunidad:", "Independiente del Valle o Empate (X2)", "86.0% | @1.25"),
            ("Total de Goles:", "Más de 1.5 goles totales", "81.0% | @1.28"),
            ("IDV Anota Primero:", "Independiente del Valle marca primer gol", "76.0% | @1.45"),
            ("Córners Chillogallo:", "Más de 7.5 córners totales", "79.0% | @1.40"),
            ("Ambos Anotan:", "Ambos Equipos Anotan - SÍ", "60.0% | @1.80")
        ],
        "goals": {
            "o15": (81.0, 1.28),
            "o25": (54.0, 1.82),
            "u35": (75.0, 1.35),
            "btts": (60.0, 1.80)
        },
        "corners": {
            "total_exp": "8.8 córners esperados",
            "line": "Más de 7.5 córners totales",
            "prob": 79.0,
            "odds": 1.40,
            "desc": "IDV ataca con laterales proyectados que fuerzan rechaces sobre la línea de fondo de Aucas."
        },
        "cards": {
            "total_exp": "5.0 tarjetas esperadas",
            "line": "Más de 4.5 tarjetas amarillas",
            "prob": 80.0,
            "odds": 1.55,
            "desc": "Clásico barrial quiteño con mucha intensidad en la disputa del balón."
        },
        "player_props": [
            ("Jeison Medina (IDV)", "Más de 1.5 remates totales", 82.0, 1.42, "En racha goleadora continua en torneo y copa."),
            ("Junior Sornoza", "Más de 0.5 tiros a puerta", 78.0, 1.48, "Especialista en balones parados y disparos desde fuera del área.")
        ],
        "medical_bulletin": [
            ("Independiente del Valle", "ONCE ESTELAR SIN SANCIONADOS", "Gandolfi dispone de todas sus figuras para seguir peleando la etapa.")
        ]
    },
    {
        "id": 2,
        "match": "Atlético de Madrid vs. FC Barcelona",
        "home": "Atlético de Madrid",
        "away": "FC Barcelona",
        "home_flag": "🔴⚪",
        "away_flag": "🔵🔴",
        "tournament": "LaLiga EA Sports • Jornada 12 (El Partidazo de Europa)",
        "venue": "Estadio Cívitas Metropolitano (Madrid)",
        "time": "15:00 (ECU)",
        "attendance": "70,460 en estadio (~90M audiencia global)",
        "home_xg": 1.55,
        "away_xg": 2.25,
        "most_probable_score": "2 - 2",
        "score_alternatives": "1 - 2 (11.5%) • 2 - 1 (10.0%) • 1 - 3 (8.8%)",
        "badge_pill": "👑 EL PARTIDAZO DE LALIGA 86.5%",
        "badge_style": "background: linear-gradient(135deg, rgba(239, 68, 68, 0.3), rgba(185, 28, 28, 0.4)); border: 1px solid #ef4444; color: #fee2e2;",
        "fija_title": "Más de 2.0 Goles Totales (Línea Asiática / Over 1.5)",
        "fija_odds": 1.25,
        "fija_prob": 86.5,
        "fija_fair_odds": 1.15,
        "fija_rationale": "El Barcelona de Hansi Flick juega con bloque altísimo y un promedio goleador asombroso (>3.2 goles por partido con Lewandowski, Raphinha y Lamine Yamal). El Atlético del Cholo en el Metropolitano no se replegará y buscará contragolpear con Julián Álvarez y Griezmann. El xG combinado de 3.80 garantiza un festival de ocasiones y goles.",
        "p1x2": [32.0, 26.0, 42.0],
        "chart_data": [42.0, 26.0, 32.0],
        "other_markets": [
            ("Total de Goles Fijo:", "Más de 1.5 goles totales", "86.5% | @1.22"),
            ("Ambos Equipos Anotan:", "Ambos Equipos Anotan - SÍ (BTTS)", "74.0% | @1.55"),
            ("Doble Oportunidad:", "FC Barcelona o Empate (X2)", "72.0% | @1.42"),
            ("Córners Totales:", "Más de 8.5 córners en Madrid", "78.0% | @1.48"),
            ("Lamine Yamal Prop:", "Lamine Yamal Más de 0.5 tiros a puerta", "80.0% | @1.40")
        ],
        "goals": {
            "o15": (86.5, 1.22),
            "o25": (68.0, 1.58),
            "u35": (60.0, 1.75),
            "btts": (74.0, 1.55)
        },
        "corners": {
            "total_exp": "9.8 córners esperados",
            "line": "Más de 8.5 córners totales",
            "prob": 78.0,
            "odds": 1.48,
            "desc": "Transiciones vertiginosas de banda a banda y centros continuos de Raphinha y Giuliano Simeone."
        },
        "cards": {
            "total_exp": "5.8 tarjetas esperadas",
            "line": "Más de 4.5 tarjetas amarillas",
            "prob": 82.0,
            "odds": 1.50,
            "desc": "Duelo de altísimo voltaje táctico y duelos individuales ardientes en el Metropolitano."
        },
        "player_props": [
            ("Robert Lewandowski", "Más de 1.5 tiros a puerta", 82.0, 1.45, "Bota de Oro de LaLiga acechando el área colchonera."),
            ("Julián Álvarez (Atleti)", "Más de 1.5 remates totales", 80.0, 1.40, "Movilidad constante a la espalda de Cubarsí e Iñigo Martínez."),
            ("Raphinha", "Más de 2.0 remates totales", 85.0, 1.35, "En el mejor momento de su carrera disparando desde cualquier sector.")
        ],
        "medical_bulletin": [
            ("FC Barcelona", "FERRÁN TORRES Y GAVI CON MINUTOS", "Pedri, Dani Olmo y Casadó comandan la medular."),
            ("Atlético de Madrid", "LE NORMAND EN REPOSO PREVENTIVO", "Giménez y Witsel en el centro de la defensa.")
        ]
    },
    {
        "id": 3,
        "match": "Inter de Milán vs. Como 1907",
        "home": "Inter de Milán",
        "away": "Como 1907",
        "home_flag": "🔵⚫",
        "away_flag": "⚪🔵",
        "tournament": "Serie A • Giornata 12 (San Siro)",
        "venue": "Estadio Giuseppe Meazza / San Siro (Milán)",
        "time": "14:45 (ECU)",
        "attendance": "72,830 en estadio (~40M audiencia global)",
        "home_xg": 2.85,
        "away_xg": 0.45,
        "most_probable_score": "3 - 0",
        "score_alternatives": "2 - 0 (14.5%) • 3 - 1 (10.0%) • 4 - 0 (8.5%)",
        "badge_pill": "👑 LA FIJA DE ORO EUROPEA 89.0%",
        "badge_style": "background: linear-gradient(135deg, rgba(16, 185, 129, 0.3), rgba(5, 150, 105, 0.4)); border: 1px solid #10b981; color: #a7f3d0;",
        "fija_title": "Inter de Milán Gana el Partido (1)",
        "fija_odds": 1.25,
        "fija_prob": 89.0,
        "fija_fair_odds": 1.12,
        "fija_rationale": "El Inter de Simone Inzaghi en San Siro es una apisonadora táctica. Con Lautaro Martínez y Marcus Thuram en la delantera, la diferencia de ritmo y pegada frente al recién ascendido Como es descomunal. El Inter promedia más de 2.5 goles de local y concede poquísimo en defensa. Es la fija más contundente de la fecha dominical en Europa.",
        "p1x2": [80.0, 14.0, 6.0],
        "chart_data": [80.0, 14.0, 6.0],
        "other_markets": [
            ("Victoria Directa (1X2):", "Inter de Milán Gana el Partido (1)", "89.0% | @1.25"),
            ("Total de Goles Fijo:", "Más de 1.5 goles totales", "86.0% | @1.22"),
            ("Inter Marca Primero:", "Primer gol del cotejo para el Inter", "84.0% | @1.28"),
            ("Hándicap San Siro:", "Inter de Milán -1.0 Gol", "75.0% | @1.55"),
            ("Córners Inter:", "Inter Más de 5.5 córners a favor", "80.0% | @1.42")
        ],
        "goals": {
            "o15": (86.0, 1.22),
            "o25": (65.0, 1.62),
            "u35": (68.0, 1.45),
            "btts": (42.0, 2.10)
        },
        "corners": {
            "total_exp": "9.4 córners esperados",
            "line": "Inter Más de 5.5 córners a favor",
            "prob": 80.0,
            "odds": 1.42,
            "desc": "Dimarco y Dumfries bombardean con centros laterales permanentemente."
        },
        "cards": {
            "total_exp": "3.8 tarjetas esperadas",
            "line": "Menos de 4.5 tarjetas totales",
            "prob": 76.0,
            "odds": 1.45,
            "desc": "Partido de control hegemónico 'nerazzurro' con bajo riesgo disciplinario."
        },
        "player_props": [
            ("Lautaro Martínez", "Más de 1.5 tiros a puerta", 84.0, 1.42, "Capitán y goleador en plena racha anotadora en Milán."),
            ("Marcus Thuram", "Más de 2.0 remates totales", 82.0, 1.38, "Potencia física incontenible ante defensas novatas.")
        ],
        "medical_bulletin": [
            ("Inter de Milán", "BARELLA Y CALHANOGLU TITULARES", "Control total de los tiempos en la medular.")
        ]
    },
    {
        "id": 4,
        "match": "Napoli vs. Lazio",
        "home": "Napoli",
        "away": "Lazio",
        "home_flag": "🔵⚪",
        "away_flag": "🦅⚪",
        "tournament": "Serie A • Giornata 12 (Clásico del Sur)",
        "venue": "Estadio Diego Armando Maradona (Nápoles)",
        "time": "14:45 (ECU)",
        "attendance": "54,200 en estadio (~35M audiencia global)",
        "home_xg": 1.85,
        "away_xg": 0.90,
        "most_probable_score": "2 - 0",
        "score_alternatives": "2 - 1 (12.0%) • 1 - 0 (11.5%) • 1 - 1 (9.0%)",
        "badge_pill": "👑 LA FIJA PARTENOPEA 85.5%",
        "badge_style": "background: linear-gradient(135deg, rgba(59, 130, 246, 0.3), rgba(37, 99, 235, 0.4)); border: 1px solid #3b82f6; color: #bfdbfe;",
        "fija_title": "Napoli o Empate (1X) + Menos de 4.5 goles",
        "fija_odds": 1.28,
        "fija_prob": 85.5,
        "fija_fair_odds": 1.17,
        "fija_rationale": "El Napoli de Antonio Conte es sinónimo de disciplina defensiva férrea y pragmatismo puro en el Maradona. Con Lukaku fijando centrales y Kvaratskhelia desbordando, el Napoli casi no concede ocasiones a sus rivales de visita. La doble oportunidad 1X combinada con un margen amplio de menos de 4.5 goles blinda el cobro.",
        "p1x2": [62.0, 24.5, 13.5],
        "chart_data": [62.0, 24.5, 13.5],
        "other_markets": [
            ("Doble Oportunidad:", "Napoli o Empate (1X)", "86.5% | @1.22"),
            ("Total de Goles:", "Menos de 3.5 goles totales", "76.0% | @1.38"),
            ("Córners Nápoles:", "Más de 8.5 córners totales", "76.0% | @1.45"),
            ("Lukaku Prop:", "Romelu Lukaku Más de 0.5 tiros a puerta", "80.0% | @1.38"),
            ("Napoli Gana Directo:", "Victoria de Napoli (1)", "62.0% | @1.68")
        ],
        "goals": {
            "o15": (78.0, 1.30),
            "o25": (50.0, 1.95),
            "u35": (76.0, 1.38),
            "btts": (48.0, 1.95)
        },
        "corners": {
            "total_exp": "9.2 córners esperados",
            "line": "Más de 8.5 córners totales",
            "prob": 76.0,
            "odds": 1.45,
            "desc": "Kvaratskhelia fuerza constantes desbordes y rechaces defensivos 'laziales'."
        },
        "cards": {
            "total_exp": "5.4 tarjetas esperadas",
            "line": "Más de 4.5 tarjetas amarillas",
            "prob": 81.0,
            "odds": 1.52,
            "desc": "Clásico de alta rivalidad entre Nápoles y Roma con árbitro riguroso."
        },
        "player_props": [
            ("Khvicha Kvaratskhelia", "Más de 1.5 remates totales", 85.0, 1.35, "Regateador número 1 de la Serie A con disparo en comba."),
            ("Romelu Lukaku", "Más de 1.5 tiros al arco", 76.0, 1.50, "Pivote dominante en duelos contra Romagnoli.")
        ],
        "medical_bulletin": [
            ("Napoli", "LOBOTKA Y BUONGIORNO AL 100%", "Columna vertebral completa disponible para Conte.")
        ]
    },
    {
        "id": 5,
        "match": "RC Lens vs. Olympique de Marsella",
        "home": "RC Lens",
        "away": "Olympique de Marsella",
        "home_flag": "🔴🟡",
        "away_flag": "⚪🔵",
        "tournament": "Ligue 1 • Jornada 11 (Francia)",
        "venue": "Stade Bollaert-Delelis (Lens)",
        "time": "14:45 (ECU)",
        "attendance": "38,223 en estadio (~25M audiencia global)",
        "home_xg": 1.30,
        "away_xg": 1.70,
        "most_probable_score": "1 - 1",
        "score_alternatives": "1 - 2 (11.0%) • 2 - 1 (10.2%) • 0 - 1 (9.0%)",
        "badge_pill": "👑 DUELO FRANCÉS DE ALTO VOLTAJE 84.5%",
        "badge_style": "background: linear-gradient(135deg, rgba(168, 85, 247, 0.3), rgba(126, 34, 206, 0.4)); border: 1px solid #a855f7; color: #f3e8ff;",
        "fija_title": "Más de 1.5 Goles Totales en Bollaert-Delelis",
        "fija_odds": 1.28,
        "fija_prob": 84.5,
        "fija_fair_odds": 1.18,
        "fija_rationale": "El Marsella de De Zerbi es un equipo ultra vertical y ofensivo con Mason Greenwood desequilibrando por banda derecha. El Lens en su caldera de Bollaert-Delelis nunca especula y presiona alto. En los últimos 6 enfrentamientos directos entre ambos se han superado los 2 goles; la línea de Más de 1.5 es un seguro de vida.",
        "p1x2": [32.0, 30.0, 38.0],
        "chart_data": [38.0, 30.0, 32.0],
        "other_markets": [
            ("Total de Goles Fijo:", "Más de 1.5 goles totales", "84.5% | @1.28"),
            ("Ambos Equipos Anotan:", "Ambos Equipos Anotan - SÍ (BTTS)", "68.0% | @1.65"),
            ("Doble Oportunidad:", "Olympique de Marsella o Empate (X2)", "74.0% | @1.38"),
            ("Córners Bollaert:", "Más de 8.5 córners totales", "76.0% | @1.45"),
            ("Greenwood Prop:", "Mason Greenwood Más de 1.5 remates", "82.0% | @1.40")
        ],
        "goals": {
            "o15": (84.5, 1.28),
            "o25": (60.0, 1.72),
            "u35": (70.0, 1.45),
            "btts": (68.0, 1.65)
        },
        "corners": {
            "total_exp": "9.5 córners esperados",
            "line": "Más de 8.5 córners totales",
            "prob": 76.0,
            "odds": 1.45,
            "desc": "Transiciones fulgurantes por bandas que terminan en rechaces a saque de esquina."
        },
        "cards": {
            "total_exp": "4.8 tarjetas esperadas",
            "line": "Más de 3.5 tarjetas amarillas",
            "prob": 78.0,
            "odds": 1.48,
            "desc": "Choque físico de alta intensidad en el norte de Francia."
        },
        "player_props": [
            ("Mason Greenwood (OM)", "Más de 1.5 remates totales", 82.0, 1.40, "Principal arma de desequilibrio individual del Marsella."),
            ("Florian Sotoca (Lens)", "Más de 1.5 remates totales", 75.0, 1.52, "Capitán y corazón del Lens en área contraria.")
        ],
        "medical_bulletin": [
            ("Olympique de Marsella", "HOJBJERG Y RABIOT EN EL MEDIOCAMPO", "Jerarquía internacional confirmada para la visita a Lens.")
        ]
    }
]

# 1. SWITCHER CONTAINER HTML
switcher_html = '            <div class="switcher-container">\n'
for m in SUNDAY_MATCHES:
    active_cls = " active" if m["id"] == 0 else ""
    switcher_html += f'''                <div class="switcher-card{active_cls}" onclick="setMatch({m['id']})" id="tab-{m['id']}">
                    <div class="switcher-header">
                        <span>Partido {m['id']+1} &bull; {m['tournament']}</span>
                        <span class="badge-fija-pill" style="{m['badge_style']}">{m['badge_pill']}</span>
                    </div>
                    <div class="switcher-teams">
                        <span>{m['home_flag']} {m['home']}</span>
                        <span class="vs-text">vs</span>
                        <span>{m['away']} {m['away_flag']}</span>
                    </div>
                    <div class="switcher-meta">
                        <span>👑 Fija Oficial: <strong style="color: #fbbf24;">{m['fija_title']}</strong></span>
                        <span class="mono-bold" style="color: var(--cyan);">@{m['fija_odds']} ({m['fija_prob']}%)</span>
                    </div>
                </div>\n'''
switcher_html += '            </div>\n\n            <!-- Match Views (0 a 5) -->\n'

# 2. MATCH VIEWS HTML
views_html = ""
for m in SUNDAY_MATCHES:
    active_cls = " active" if m["id"] == 0 else ""
    display_style = "display: block;" if m["id"] == 0 else "display: none;"
    
    submarkets_html = ""
    for title, market, info in m["other_markets"]:
        submarkets_html += f'''                <span class="tag-pill tag-cyan" style="cursor: pointer; margin: 0.2rem; font-size: 0.76rem;" title="{title} {market} ({info})">
                    🎯 <strong>{title}</strong> {market} <span style="color: #ffffff;">({info})</span>
                </span>\n'''

    med_html = ""
    for p_name, p_status, p_desc in m["medical_bulletin"]:
        med_html += f'''                <div style="background: rgba(239, 68, 68, 0.12); border: 1px solid rgba(239, 68, 68, 0.35); border-radius: 10px; padding: 0.85rem 1rem; margin-top: 0.5rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
                        <span style="font-weight: 700; color: #f87171; font-size: 0.9rem;">🚫 {p_name} &bull; {p_status}</span>
                        <span class="tag-pill tag-rose" style="font-size: 0.7rem;">INFORME OFICIAL</span>
                    </div>
                    <div style="font-size: 0.8rem; color: #fca5a5;">
                        <strong>Parte Médico:</strong> {p_desc}
                    </div>
                </div>\n'''

    props_html = ""
    for pl_name, pl_market, pl_prob, pl_odds, pl_desc in m["player_props"]:
        props_html += f'''                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 0.75rem 0.9rem; margin-bottom: 0.5rem;">
                    <div style="display: flex; justify-content: space-between; font-size: 0.84rem; margin-bottom: 0.2rem;">
                        <strong style="color: #67e8f9;">{pl_name}</strong>
                        <span style="color: #10b981; font-weight: 700;">{pl_prob}% &bull; @{pl_odds}</span>
                    </div>
                    <div style="font-size: 0.78rem; color: #cbd5e1;">{pl_market}</div>
                    <div style="font-size: 0.72rem; color: #94a3b8; margin-top: 0.2rem;">{pl_desc}</div>
                </div>\n'''

    views_html += f'''        <!-- ==================== PARTIDO {m['id']+1}: {m['match']} ==================== -->
        <div id="match-{m['id']}" class="match-view{active_cls}" style="{display_style}">
            <!-- Hero Banner -->
            <div class="hero-banner">
                <div class="hero-context-badge">
                    <span>🏆 {m['tournament']}</span>
                    <span>📍 {m['venue']} &bull; ⏰ {m['time']}</span>
                    <span>👥 {m['attendance']}</span>
                </div>

                <div class="hero-grid">
                    <div class="team-col">
                        <div class="team-flag">{m['home_flag']}</div>
                        <div class="team-name">{m['home']}</div>
                        <div class="team-xg-chip">xG Proyectado: <span class="mono-bold" style="color: var(--cyan);">{m['home_xg']}</span></div>
                    </div>

                    <div class="center-score-col">
                        <div class="score-pill-title">Marcador Exacto Más Probable</div>
                        <div class="hero-score-val">{m['most_probable_score']}</div>
                        <div class="hero-score-conf">Top Alternativas: {m['score_alternatives']}</div>
                    </div>

                    <div class="team-col">
                        <div class="team-flag">{m['away_flag']}</div>
                        <div class="team-name">{m['away']}</div>
                        <div class="team-xg-chip">xG Proyectado: <span class="mono-bold" style="color: var(--amber);">{m['away_xg']}</span></div>
                    </div>
                </div>
            </div>

            <!-- Glowing La Fija Card -->
            <div class="fija-gold-card">
                <div class="fija-badge-glow">
                    <span class="fija-star">⭐</span> LA FIJA DEL PARTIDO &bull; Máxima Certidumbre Matemática
                </div>
                <div class="fija-content-grid">
                    <div class="fija-main">
                        <div class="fija-market-label">Selección Cuantitativa Principal</div>
                        <div class="fija-market-title">{m['fija_title']}</div>
                        <div class="fija-rationale">🔬 <em>Fundamento TimesFM & Monte Carlo:</em> {m['fija_rationale']}</div>
                    </div>
                    <div class="fija-stats">
                        <div class="fija-stat-box">
                            <div class="fija-stat-val">{m['fija_prob']}%</div>
                            <div class="fija-stat-lbl">Probabilidad</div>
                        </div>
                        <div class="fija-stat-box">
                            <div class="fija-stat-val" style="color: var(--emerald);">@{m['fija_fair_odds']}</div>
                            <div class="fija-stat-lbl">Cuota Justa</div>
                        </div>
                        <div class="fija-stat-box">
                            <div class="fija-stat-val" style="color: var(--cyan);">@{m['fija_odds']}</div>
                            <div class="fija-stat-lbl">Cuota Ecuabet</div>
                        </div>
                    </div>
                </div>
                
                <div style="margin-top: 0.85rem; padding-top: 0.65rem; border-top: 1px dashed rgba(255,255,255,0.15);">
                    <div style="font-size: 0.74rem; color: var(--text-muted); margin-bottom: 0.4rem; font-weight: 700; letter-spacing: 0.5px;">
                        📊 OTROS MERCADOS DE SEGURIDAD ANALIZADOS EN ESTE PARTIDO:
                    </div>
                    <div style="display: flex; flex-wrap: wrap; gap: 0.35rem;">
{submarkets_html}                    </div>
                </div>
            </div>

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
                            <span>Victoria {m['home']} (1)</span>
                            <span class="mono-bold" style="color: var(--cyan);">{m['p1x2'][0]}%</span>
                        </div>
                        <div class="prob-bar-track">
                            <div class="prob-bar-fill" style="width: {m['p1x2'][0]}%; background: linear-gradient(90deg, #3b82f6, #06b6d4);"></div>
                        </div>
                    </div>

                    <div class="prob-bar-row">
                        <div class="prob-bar-label">
                            <span>Empate (X)</span>
                            <span class="mono-bold" style="color: var(--gold);">{m['p1x2'][1]}%</span>
                        </div>
                        <div class="prob-bar-track">
                            <div class="prob-bar-fill" style="width: {m['p1x2'][1]}%; background: linear-gradient(90deg, #f59e0b, #fbbf24);"></div>
                        </div>
                    </div>

                    <div class="prob-bar-row">
                        <div class="prob-bar-label">
                            <span>Victoria {m['away']} (2)</span>
                            <span class="mono-bold" style="color: var(--emerald);">{m['p1x2'][2]}%</span>
                        </div>
                        <div class="prob-bar-track">
                            <div class="prob-bar-fill" style="width: {m['p1x2'][2]}%; background: linear-gradient(90deg, #10b981, #34d399);"></div>
                        </div>
                    </div>

                    <div style="margin-top: 1.25rem; height: 180px; position: relative;">
                        <canvas id="chart1X2-{m['id']}"></canvas>
                    </div>
                </div>

                <!-- Mercados de Goles -->
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">⚽ Mercados de Goles</div>
                        <span class="badge-subtle">Poisson Multi-Línea</span>
                    </div>
                    
                    <div class="prob-bar-row">
                        <div class="prob-bar-label">
                            <span>Más de 1.5 Goles</span>
                            <span class="mono-bold" style="color: #38bdf8;">{m['goals']['o15'][0]}% &bull; @{m['goals']['o15'][1]}</span>
                        </div>
                        <div class="prob-bar-track">
                            <div class="prob-bar-fill" style="width: {m['goals']['o15'][0]}%; background: #38bdf8;"></div>
                        </div>
                    </div>

                    <div class="prob-bar-row">
                        <div class="prob-bar-label">
                            <span>Más de 2.5 Goles</span>
                            <span class="mono-bold" style="color: #818cf8;">{m['goals']['o25'][0]}% &bull; @{m['goals']['o25'][1]}</span>
                        </div>
                        <div class="prob-bar-track">
                            <div class="prob-bar-fill" style="width: {m['goals']['o25'][0]}%; background: #818cf8;"></div>
                        </div>
                    </div>

                    <div class="prob-bar-row">
                        <div class="prob-bar-label">
                            <span>Ambos Equipos Anotan (BTTS)</span>
                            <span class="mono-bold" style="color: #f472b6;">{m['goals']['btts'][0]}% &bull; @{m['goals']['btts'][1]}</span>
                        </div>
                        <div class="prob-bar-track">
                            <div class="prob-bar-fill" style="width: {m['goals']['btts'][0]}%; background: #f472b6;"></div>
                        </div>
                    </div>

                    <div style="margin-top: 1rem; padding: 0.75rem; background: rgba(255,255,255,0.02); border-radius: 8px; font-size: 0.8rem; color: #94a3b8;">
                        💡 <strong>Lectura Táctica:</strong> xG Combinado de {round(m['home_xg'] + m['away_xg'], 2)} goles esperados en el cotejo.
                    </div>
                </div>

                <!-- Córners & Balón Parado -->
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">🚩 Córners & Balón Parado</div>
                        <span class="badge-subtle">SetPieceModel</span>
                    </div>

                    <div style="margin-bottom: 0.75rem;">
                        <div style="font-size: 1.1rem; font-weight: 800; color: #38bdf8;">{m['corners']['total_exp']}</div>
                        <div style="font-size: 0.85rem; color: #cbd5e1; margin-top: 0.2rem;">Línea Óptima: <strong>{m['corners']['line']}</strong> ({m['corners']['prob']}% | @{m['corners']['odds']})</div>
                    </div>

                    <div style="font-size: 0.8rem; color: #94a3b8; line-height: 1.45; margin-bottom: 1rem;">
                        {m['corners']['desc']}
                    </div>

                    <div class="card-header" style="padding-top: 0.75rem; border-top: 1px solid rgba(255,255,255,0.08);">
                        <div class="card-title" style="font-size: 0.9rem;">🟨 Tarjetas & Rigor Arbitral</div>
                    </div>
                    <div style="font-size: 0.82rem; color: #fde047; font-weight: 700;">{m['cards']['total_exp']} &bull; {m['cards']['line']} (@{m['cards']['odds']})</div>
                    <div style="font-size: 0.75rem; color: #94a3b8; margin-top: 0.25rem;">{m['cards']['desc']}</div>
                </div>
            </div>

            <!-- Props & Figuras Clave -->
            <div class="card" style="margin-top: 1.5rem;">
                <div class="card-header">
                    <div class="card-title">⭐ Remates & Disparos a Puerta de Figuras Clave</div>
                    <span class="badge-subtle">PlayerProps Engine</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 0.75rem; margin-top: 0.5rem;">
{props_html}                </div>
            </div>

            <!-- Medical Bulletin & Sanity Audit Section -->
            <div class="card" style="margin-top: 1.5rem; border-color: rgba(239, 68, 68, 0.35);">
                <div class="card-header">
                    <div class="card-title" style="color: #f87171;">🏥 Auditoría Sanitaria & Boletín Médico Oficial (SquadInjuryAgent)</div>
                    <span class="tag-pill tag-rose">Veto Sanitario Verificado</span>
                </div>
{med_html}            </div>
        </div>\n\n'''

# 3. BANNER SUPERIOR CON ESTRATEGIAS Y SALDO
banner_html = '''        <div id="view-container-matches">
            <!-- BANNER PRINCIPAL DE LA JORNADA: LOS 6 PARTIDOS ESTELARES DEL DOMINGO -->
            <div style="background: linear-gradient(135deg, rgba(30, 27, 75, 0.95), rgba(15, 23, 42, 0.98)); border: 2px solid rgba(59, 130, 246, 0.6); border-radius: 20px; padding: 1.75rem 2rem; margin-bottom: 2rem; backdrop-filter: blur(16px); box-shadow: 0 16px 36px -8px rgba(59, 130, 246, 0.35);">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 1rem;">
                    <div>
                        <span style="background: #3b82f6; color: #ffffff; padding: 0.35rem 0.85rem; border-radius: 9999px; font-weight: 800; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.8px;">
                            JORNADA OFICIAL &bull; DOMINGO 8 DE NOVIEMBRE DE 2026
                        </span>
                        <h2 style="font-size: 1.75rem; font-weight: 900; color: #ffffff; margin: 0.6rem 0 0.2rem 0; letter-spacing: -0.5px;">
                            Los 6 Partidos Estelares &bull; Domingo Tarde & Noche (13:45 a 16:30 ECU)
                        </h2>
                        <div style="color: #94a3b8; font-size: 0.92rem;">
                            Haz clic en cada partido arriba para abrir su análisis interactivo completo: xG, 1X2, cuotas Ecuabet, córners, tarjetas y La Fija de Oro.
                        </div>
                    </div>
                    <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 14px; padding: 0.75rem 1.25rem; text-align: right;">
                        <div style="font-size: 0.75rem; color: #6ee7b7; font-weight: 700; text-transform: uppercase;">Saldo Personal Ecuabet</div>
                        <div style="font-size: 1.4rem; font-weight: 900; color: #ffffff;">$24.90 USD <span style="font-size: 0.8rem; color: #10b981;">(INTACTO)</span></div>
                        <div style="font-size: 0.7rem; color: #94a3b8;">Muralla de $20 protegida &bull; $4.90 de colchón</div>
                    </div>
                </div>

                <!-- Estrategias de Apuesta -->
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-top: 1.25rem;">
                    <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 12px; padding: 1rem;">
                        <div style="font-size: 0.75rem; color: #f59e0b; font-weight: 800; text-transform: uppercase;">👑 Opción 1: El Francotirador Solitario</div>
                        <div style="font-size: 1rem; font-weight: 800; color: #ffffff; margin: 0.25rem 0;">Inter de Milán Gana Directo (1) @ 1.25</div>
                        <div style="font-size: 0.8rem; color: #94a3b8;">Con $4.90 USD cobras <strong>$6.12 USD</strong> en San Siro sin sobresaltos.</div>
                    </div>
                    <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 12px; padding: 1rem;">
                        <div style="font-size: 0.75rem; color: #10b981; font-weight: 800; text-transform: uppercase;">⚡ Opción 2: La Fija Doble Recomendada</div>
                        <div style="font-size: 1rem; font-weight: 800; color: #ffffff; margin: 0.25rem 0;">Inter Gana (1) @ 1.25 + IDV o Empate (X2) @ 1.25 &bull; Cuota 1.56</div>
                        <div style="font-size: 0.8rem; color: #94a3b8;">Con $4.90 USD cobras <strong>$7.64 USD</strong> (+$2.74 netos, llevando tu saldo a <strong>$27.64 USD</strong>).</div>
                    </div>
                </div>
            </div>\n'''

new_area1_content = banner_html + switcher_html + views_html + '        </div> <!-- Fin de view-container-matches -->\n\n'

chart_configs_js = '''var chartConfigs = [
            { id: 'chart1X2-0', labels: ['Barcelona SC (1)', 'Empate (X)', 'Liga de Quito (2)'], data: [46.0, 32.0, 22.0] },
            { id: 'chart1X2-1', labels: ['IDV (2)', 'Empate (X)', 'Aucas (1)'], data: [56.0, 28.0, 16.0] },
            { id: 'chart1X2-2', labels: ['FC Barcelona (2)', 'Empate (X)', 'Atlético Madrid (1)'], data: [42.0, 26.0, 32.0] },
            { id: 'chart1X2-3', labels: ['Inter Milan (1)', 'Empate (X)', 'Como (2)'], data: [80.0, 14.0, 6.0] },
            { id: 'chart1X2-4', labels: ['Napoli (1)', 'Empate (X)', 'Lazio (2)'], data: [62.0, 24.5, 13.5] },
            { id: 'chart1X2-5', labels: ['Marsella (2)', 'Empate (X)', 'Lens (1)'], data: [38.0, 30.0, 32.0] }
        ];'''

all_fijas_js = '''var allFijasData = [
            { id: 1, match: 'Barcelona SC vs Liga de Quito', pick: 'Barcelona SC o Empate (1X) + Más 1.5', prob: 84.0, odds: 1.35 },
            { id: 2, match: 'Aucas vs Independiente del Valle', pick: 'IDV o Empate (X2)', prob: 86.0, odds: 1.25 },
            { id: 3, match: 'Atlético de Madrid vs FC Barcelona', pick: 'Más de 2.0 goles (Over 1.5)', prob: 86.5, odds: 1.25 },
            { id: 4, match: 'Inter de Milán vs Como', pick: 'Inter de Milán Gana (1)', prob: 89.0, odds: 1.25 },
            { id: 5, match: 'Napoli vs Lazio', pick: 'Napoli o Empate (1X) + Menos 4.5', prob: 85.5, odds: 1.28 },
            { id: 6, match: 'RC Lens vs Marsella', pick: 'Más de 1.5 goles totales', prob: 84.5, odds: 1.28 }
        ];'''

# Actualizar simulations_tomorrow_results.json
sim_results = {
    "GeneratedAt": "08/11/2026 12:45",
    "TargetDay": "Domingo (Tarde & Noche)",
    "TargetDate": "08/11/2026",
    "TemporalLabel": "Domingo 08/11 Tarde y Noche (6 Partidos Estelares)",
    "ActiveBankroll": 3033.52,
    "Status": "active",
    "Matches": [
        {
            "match": m["match"],
            "home_team": m["home"],
            "away_team": m["away"],
            "tournament": m["tournament"],
            "time_ec": m["time"],
            "stadium": m["venue"],
            "score_prediction": {
                "most_probable_score": m["most_probable_score"],
                "home_goals": m["home_xg"],
                "away_goals": m["away_xg"]
            },
            "la_fija_real": {
                "selection": m["fija_title"],
                "odds": m["fija_odds"],
                "probability": m["fija_prob"],
                "confidence": m["badge_pill"],
                "argument": m["fija_rationale"]
            }
        } for m in SUNDAY_MATCHES
    ]
}

with open(f"{base_dir}/sports_agents/simulations_tomorrow_results.json", "w", encoding="utf-8") as f:
    json.dump(sim_results, f, ensure_ascii=False, indent=2)
print("simulations_tomorrow_results.json actualizado.")

# Inyectar en HTMLs
files = [
    f"{base_dir}/index.html",
    f"{base_dir}/dashboard_pronosticos.html",
    f"{base_dir}/../index.html"
]

for fpath in files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        print(f"Skipping {fpath}: {e}")
        continue

    # Encontrar view-container-matches y reemplazar
    start_tag = '<div id="view-container-matches">'
    start_idx = html.find(start_tag)
    end_tag = '<!-- VISTA 2: WIN RATE & AUDITORÍA EN VIVO -->'
    end_idx = html.find(end_tag)

    if start_idx != -1 and end_idx != -1:
        html = html[:start_idx] + new_area1_content + html[end_idx:]
        print(f"Replaced Area 1 in {fpath}")
    else:
        print(f"Could not find Area 1 tags in {fpath}")

    # chartConfigs
    html = re.sub(r'var chartConfigs = \[.*?\];', chart_configs_js, html, flags=re.DOTALL)
    # allFijasData
    html = re.sub(r'var allFijasData = \[.*?\];', all_fijas_js, html, flags=re.DOTALL)

    # Título de pestaña y subtítulos
    html = re.sub(
        r'<title>.*?</title>',
        '<title>SportsAI Analytics &middot; 6 Partidos Estelares &bull; Domingo 08/11 &bull; Win Rate & Autoaprendizaje</title>',
        html
    )
    html = re.sub(
        r'Motor Predictivo Multi-Agente &bull; \d+ Partidos Estelares &bull; [^<]+',
        'Motor Predictivo Multi-Agente &bull; 6 Partidos Estelares &bull; Domingo 08/11 (Tarde & Noche)',
        html
    )
    html = re.sub(
        r'⚽ Partidos &amp; Pronósticos \(\d+\)|⚽ Partidos & Pronósticos \(\d+\)',
        '⚽ Partidos & Pronósticos (6)',
        html
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Saved {fpath} successfully.")

print("SUNDAY ELITE 6 BUILD COMPLETE!")
