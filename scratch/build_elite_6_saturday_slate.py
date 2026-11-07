# -*- coding: utf-8 -*-
"""
build_elite_6_saturday_slate.py
Restaura con máxima calidad el sistema de los 6 PARTIDOS ESTELARES interactivos
con selector (.switcher-container) y vista detallada completa (.match-view #match-0 a #match-5),
auditoría médica, props de córners, tarjetas, remates, 1X2, goles y La Fija de Oro.
"""

import json
import re

# Los 6 Partidos Estelares de la Tarde/Noche del Sábado 7 de Noviembre
MATCHES_DATA = [
    {
        "id": 0,
        "match": "Valencia vs. Real Madrid",
        "home": "Valencia",
        "away": "Real Madrid",
        "home_flag": "🦇",
        "away_flag": "⚪",
        "tournament": "LaLiga EA Sports • Jornada 12 (Estelar)",
        "venue": "Estadio de Mestalla (Valencia)",
        "time": "15:00 (ECU)",
        "attendance": "49,430 en estadio (~50M audiencia global)",
        "home_xg": 0.85,
        "away_xg": 2.15,
        "most_probable_score": "1 - 2",
        "score_alternatives": "0 - 2 (11.4%) • 1 - 1 (10.8%) • 0 - 1 (9.2%)",
        "badge_pill": "👑 LA FIJA DE ORO DE LALIGA 87.0%",
        "badge_style": "background: linear-gradient(135deg, rgba(16, 185, 129, 0.3), rgba(5, 150, 105, 0.4)); border: 1px solid #10b981; color: #a7f3d0;",
        "fija_title": "Real Madrid o Empate (Doble Oportunidad X2)",
        "fija_odds": 1.24,
        "fija_prob": 87.0,
        "fija_fair_odds": 1.15,
        "fija_rationale": "Mestalla siempre genera un ambiente de alta fricción y hostilidad ante el Real Madrid. Sin embargo, la jerarquía en contragolpe con Vinícius, Mbappé y Bellingham es letal. La doble oportunidad X2 blinda completamente ante un empate 1-1 y garantiza el cobro.",
        "p1x2": [13.0, 26.0, 61.0], # 1, X, 2
        "chart_data": [61.0, 26.0, 13.0], # Madrid, Empate, Valencia
        "other_markets": [
            ("Doble Oportunidad:", "Real Madrid o Empate (X2)", "87.0% | @1.24"),
            ("Total de Goles:", "Más de 1.5 goles totales", "82.5% | @1.25"),
            ("Córners Totales:", "Más de 8.5 córners en Mestalla", "76.0% | @1.48"),
            ("Fricción Arbitral:", "Más de 4.5 tarjetas amarillas", "81.0% | @1.55"),
            ("Ambos Anotan (BTTS):", "Ambos Equipos Anotan - SÍ", "62.0% | @1.78")
        ],
        "goals": {
            "o15": (82.5, 1.25),
            "o25": (58.0, 1.72),
            "u35": (73.0, 1.37),
            "btts": (62.0, 1.78)
        },
        "corners": {
            "total_exp": "9.8 córners esperados",
            "line": "Más de 8.5 córners",
            "prob": 76.0,
            "odds": 1.48,
            "desc": "Valencia fuerza desbordes por bandas con Diego López y Gayà, mientras el Madrid promedia 6.2 córners a favor en salidas ligueras."
        },
        "cards": {
            "total_exp": "5.4 tarjetas esperadas",
            "line": "Más de 4.5 tarjetas amarillas",
            "prob": 81.0,
            "odds": 1.55,
            "desc": "Clásico de altísima tensión en Mestalla. Rigor arbitral estricto; historial reciente de roces constantes entre defensas 'chés' y atacantes blancos."
        },
        "player_props": [
            ("Vinícius Júnior", "Más de 1.5 tiros a puerta", 78.0, 1.45, "Extrema verticalidad atacando el carril de Thierry Correia."),
            ("Kylian Mbappé", "Más de 2.5 tiros totales", 84.0, 1.35, "Promedia 3.8 remates por partido buscando el arco rival."),
            ("Hugo Duro", "Más de 0.5 tiros a puerta", 65.0, 1.62, "Referencia ofensiva local que busca balones aéreos en el área.")
        ],
        "medical_bulletin": [
            ("Thibaut Courtois / Dani Carvajal", "BAJAS MÉDICAS CONFIRMADAS", "Recuperación de rotura de ligamentos en Carvajal. Lunin titular bajo los tres palos."),
            ("Mouctar Diakhaby (Valencia)", "BAJA EN DEFENSA CENTRAL", "Ausencia prolongada que obliga a Baraja a improvisar en la zaga.")
        ]
    },
    {
        "id": 1,
        "match": "Paris Saint-Germain vs. Troyes",
        "home": "Paris Saint-Germain",
        "away": "Troyes",
        "home_flag": "🔴🔵",
        "away_flag": "⚪🔵",
        "tournament": "Ligue 1 • Jornada de Fin de Semana (París)",
        "venue": "Parc des Princes (París)",
        "time": "15:05 (ECU)",
        "attendance": "47,926 en estadio (~30M audiencia global)",
        "home_xg": 3.10,
        "away_xg": 0.35,
        "most_probable_score": "3 - 0",
        "score_alternatives": "2 - 0 (14.2%) • 3 - 1 (10.5%) • 4 - 0 (8.9%)",
        "badge_pill": "👑 LA FIJA DE ORO MUNDIAL 90.0%",
        "badge_style": "background: linear-gradient(135deg, rgba(245, 158, 11, 0.3), rgba(217, 119, 6, 0.4)); border: 1px solid #fbbf24; color: #fef08a;",
        "fija_title": "PSG Gana el Partido (1)",
        "fija_odds": 1.20,
        "fija_prob": 90.0,
        "fija_fair_odds": 1.11,
        "fija_rationale": "El Parque de los Príncipes es un feudo inexpugnable. El equipo de Luis Enrique supera ampliamente en ritmo, posesión (>68%) y contundencia técnica al Troyes. Con Barcola, Dembélé y Vitinha en plenitud, el triunfo directo del PSG es el pilar de mayor certeza matemática de toda la jornada europea.",
        "p1x2": [82.0, 12.0, 6.0], # 1, X, 2
        "chart_data": [82.0, 12.0, 6.0],
        "other_markets": [
            ("Victoria Directa (1X2):", "PSG Gana el Partido (1)", "90.0% | @1.20"),
            ("Total de Goles Fijo:", "Más de 2.5 goles totales", "81.0% | @1.42"),
            ("PSG Anota Primero:", "Primer gol del cotejo anotado por PSG", "88.0% | @1.22"),
            ("Córners París:", "PSG Más de 5.5 córners a favor", "79.0% | @1.40"),
            ("Hándicap Asiático:", "PSG -1.5 Goles", "74.0% | @1.58")
        ],
        "goals": {
            "o15": (89.0, 1.15),
            "o25": (81.0, 1.42),
            "u35": (56.0, 1.95),
            "btts": (44.0, 2.10)
        },
        "corners": {
            "total_exp": "9.2 córners esperados",
            "line": "PSG Más de 5.5 córners a favor",
            "prob": 79.0,
            "odds": 1.40,
            "desc": "El asedio territorial constante del PSG en campo contrario fuerza numerosos rechaces sobre la línea de fondo visitante."
        },
        "cards": {
            "total_exp": "3.2 tarjetas esperadas",
            "line": "Menos de 4.5 tarjetas totales",
            "prob": 78.0,
            "odds": 1.42,
            "desc": "Partido de posesión hegemónica parisina con escasa fricción violenta y trámite fluido."
        },
        "player_props": [
            ("Bradley Barcola", "Más de 1.5 tiros al arco", 82.0, 1.48, "Desequilibrio puro en el uno contra uno por banda izquierda."),
            ("Ousmane Dembélé", "Más de 2.5 tiros totales", 86.0, 1.38, "Engancha hacia adentro con perfil ambidiestro buscando disparar."),
            ("Vitinha", "Más de 0.5 tiros al arco", 70.0, 1.65, "Llegada desde segunda línea y remate de media distancia.")
        ],
        "medical_bulletin": [
            ("Lucas Hernández / Presnel Kimpembe", "FASE FINAL DE READAPTACIÓN", "Plantilla profunda con Pacho y Marquinhos garantizando solidez en la zaga.")
        ]
    },
    {
        "id": 2,
        "match": "Libertad FC vs. Emelec",
        "home": "Libertad FC",
        "away": "Emelec",
        "home_flag": "🟠",
        "away_flag": "🔵",
        "tournament": "LigaPro Ecuabet • Fase 2 (Loja)",
        "venue": "Estadio Reina del Cisne (Loja, 2,100 msnm)",
        "time": "14:00 (ECU)",
        "attendance": "8,500 en estadio (~12M audiencia nacional)",
        "home_xg": 1.35,
        "away_xg": 1.10,
        "most_probable_score": "1 - 1",
        "score_alternatives": "1 - 0 (12.8%) • 2 - 1 (9.6%) • 0 - 0 (8.5%)",
        "badge_pill": "👑 LA FIJA NACIONAL DE LIGAPRO 84.5%",
        "badge_style": "background: linear-gradient(135deg, rgba(234, 88, 12, 0.3), rgba(194, 65, 12, 0.4)); border: 1px solid #f97316; color: #ffedd5;",
        "fija_title": "Libertad FC o Empate (Doble Oportunidad 1X)",
        "fija_odds": 1.30,
        "fija_prob": 84.5,
        "fija_fair_odds": 1.18,
        "fija_rationale": "En el Estadio Reina del Cisne a 2,100 metros de altitud, Libertad FC se juega la vida por la permanencia con intensidad física máxima. Emelec sufre en la generación ofensiva fuera de Guayaquil y sus transiciones en la sierra son lentas. La doble oportunidad 1X cubre el triunfo lojano y el empate.",
        "p1x2": [42.0, 42.5, 15.5],
        "chart_data": [42.0, 42.5, 15.5],
        "other_markets": [
            ("Doble Oportunidad:", "Libertad FC o Empate (1X)", "84.5% | @1.30"),
            ("Total de Goles:", "Menos de 2.5 goles totales", "72.0% | @1.55"),
            ("Ambos Anotan:", "NO Ambos Equipos Anotan", "64.0% | @1.68"),
            ("Córners Totales:", "Más de 7.5 córners en Loja", "75.0% | @1.42"),
            ("Primer Tiempo:", "Empate al Descanso (X)", "68.0% | @1.85")
        ],
        "goals": {
            "o15": (68.0, 1.45),
            "o25": (38.0, 2.30),
            "u25": (72.0, 1.55),
            "btts": (46.0, 2.05)
        },
        "corners": {
            "total_exp": "8.4 córners esperados",
            "line": "Más de 7.5 córners totales",
            "prob": 75.0,
            "odds": 1.42,
            "desc": "El balón rápido en la altura de Loja genera rebotes y tiros de esquina por despejes de los zagueros."
        },
        "cards": {
            "total_exp": "5.6 tarjetas esperadas",
            "line": "Más de 4.5 tarjetas amarillas",
            "prob": 82.0,
            "odds": 1.50,
            "desc": "Partido de pierna fuerte en el mediocampo por la urgencia de puntos de ambos equipos."
        },
        "player_props": [
            ("Diego Ávila (Libertad)", "Más de 1.5 tiros totales", 75.0, 1.52, "Principal ariete de Libertad buscando el arco en balones divididos."),
            ("Jaime Ayoví (Emelec)", "Más de 0.5 tiros a puerta", 68.0, 1.65, "Pivoteo constante y remate aéreo en balones detenidos.")
        ],
        "medical_bulletin": [
            ("Emelec", "DESGASTE FÍSICO POR VIAJE A LOJA", "Rotaciones tácticas de Leonel Álvarez en bandas para dosificar piernas.")
        ]
    },
    {
        "id": 3,
        "match": "FBC Melgar vs. Juan Pablo II",
        "home": "FBC Melgar",
        "away": "Juan Pablo II",
        "home_flag": "🔴⚫",
        "away_flag": "🟡⚪",
        "tournament": "Liga 1 Te Apuesto • Clausura (Arequipa)",
        "venue": "Estadio Monumental de la UNSA (Arequipa, 2,335 msnm)",
        "time": "18:00 (ECU)",
        "attendance": "18,200 en estadio (~10M audiencia nacional)",
        "home_xg": 2.60,
        "away_xg": 0.40,
        "most_probable_score": "3 - 0",
        "score_alternatives": "2 - 0 (15.5%) • 3 - 1 (11.0%) • 4 - 0 (9.2%)",
        "badge_pill": "👑 LA FIJA DE LA UNSA 89.0%",
        "badge_style": "background: linear-gradient(135deg, rgba(220, 38, 38, 0.3), rgba(185, 28, 28, 0.4)); border: 1px solid #ef4444; color: #fee2e2;",
        "fija_title": "FBC Melgar Gana el Partido (1)",
        "fija_odds": 1.22,
        "fija_prob": 89.0,
        "fija_fair_odds": 1.12,
        "fija_rationale": "El 'Dominó' es una máquina casi perfecta en el Monumental de la UNSA. Juan Pablo II es un equipo recién ascendido del llano que sufre asfixia en el segundo tiempo en los 2,335 metros de Arequipa. Con Bernardo Cuesta y Bordacahar, Melgar resolverá el partido con autoridad.",
        "p1x2": [78.0, 16.0, 6.0],
        "chart_data": [78.0, 16.0, 6.0],
        "other_markets": [
            ("Victoria Directa (1X2):", "FBC Melgar Gana el Partido (1)", "89.0% | @1.22"),
            ("Total de Goles Fijo:", "Más de 1.5 goles totales", "85.0% | @1.24"),
            ("Melgar Anota Primero:", "FBC Melgar marca el primer gol", "86.0% | @1.25"),
            ("Hándicap Arequipa:", "FBC Melgar -1.5 Goles", "71.0% | @1.65"),
            ("Córners Melgar:", "Melgar Más de 5.5 córners", "80.0% | @1.38")
        ],
        "goals": {
            "o15": (85.0, 1.24),
            "o25": (66.0, 1.62),
            "u35": (68.0, 1.45),
            "btts": (40.0, 2.15)
        },
        "corners": {
            "total_exp": "9.5 córners esperados",
            "line": "Melgar Más de 5.5 córners",
            "prob": 80.0,
            "odds": 1.38,
            "desc": "El asedio arequipeño por las bandas genera una avalancha de tiros de esquina locales."
        },
        "cards": {
            "total_exp": "4.2 tarjetas esperadas",
            "line": "Menos de 5.5 tarjetas totales",
            "prob": 74.0,
            "odds": 1.48,
            "desc": "Juan Pablo II se replegará cerca de su arco sin entrar en juego brusco deliberado."
        },
        "player_props": [
            ("Bernardo Cuesta", "Más de 1.5 tiros al arco", 80.0, 1.50, "Goleador histórico y emblema indiscutido de Melgar en la UNSA."),
            ("Cristian Bordacahar", "Más de 2.0 tiros totales", 78.0, 1.42, "Llegada constante por carril interior.")
        ],
        "medical_bulletin": [
            ("FBC Melgar", "PLANTEL COMPLETO SIN BAJAS DE PESO", "Marco Valencia dispone de su oncena estelar para consolidar el liderato.")
        ]
    },
    {
        "id": 4,
        "match": "Nottingham Forest vs. Manchester City",
        "home": "Nottingham Forest",
        "away": "Manchester City",
        "home_flag": "🔴🌲",
        "away_flag": "🔵⚪",
        "tournament": "Premier League • Matchday 11 (Inglaterra)",
        "venue": "The City Ground (Nottingham)",
        "time": "12:30 (ECU)",
        "attendance": "30,445 en estadio (~75M audiencia global)",
        "home_xg": 0.95,
        "away_xg": 2.20,
        "most_probable_score": "1 - 2",
        "score_alternatives": "0 - 2 (12.0%) • 1 - 3 (9.5%) • 1 - 1 (8.5%)",
        "badge_pill": "👑 LA FIJA DE PREMIER LEAGUE 86.5%",
        "badge_style": "background: linear-gradient(135deg, rgba(6, 182, 212, 0.3), rgba(8, 145, 178, 0.4)); border: 1px solid #06b6d4; color: #cffafe;",
        "fija_title": "Man City o Empate (X2) + Más de 1.5 goles",
        "fija_odds": 1.33,
        "fija_prob": 86.5,
        "fija_fair_odds": 1.16,
        "fija_rationale": "El City de Pep Guardiola necesita sumar de a tres para mantenerse en la cima de la Premier. Aunque The City Ground es una plaza combativa, la jerarquía de Haaland, Phil Foden y Kevin De Bruyne garantiza gol. La combinación X2 + Más de 1.5 goles cubre cualquier victoria 'citizen' o empate con goles.",
        "p1x2": [14.0, 24.5, 61.5],
        "chart_data": [61.5, 24.5, 14.0],
        "other_markets": [
            ("Doble Oportunidad Blindada:", "Man City o Empate (X2)", "88.0% | @1.22"),
            ("Total de Goles:", "Más de 1.5 goles totales", "84.0% | @1.26"),
            ("Córners Totales:", "Más de 9.5 córners en Nottingham", "75.0% | @1.52"),
            ("Haaland al Marcador:", "Erling Haaland anota en cualquier momento", "70.0% | @1.65"),
            ("Man City Córners:", "City Más de 5.5 córners", "78.0% | @1.42")
        ],
        "goals": {
            "o15": (84.0, 1.26),
            "o25": (62.0, 1.68),
            "u35": (70.0, 1.45),
            "btts": (58.0, 1.82)
        },
        "corners": {
            "total_exp": "10.2 córners esperados",
            "line": "Más de 9.5 córners totales",
            "prob": 75.0,
            "odds": 1.52,
            "desc": "El City genera permanente desborde por los costados con Doku y Savinho, elevando el conteo de tiros de esquina."
        },
        "cards": {
            "total_exp": "4.4 tarjetas esperadas",
            "line": "Más de 3.5 tarjetas amarillas",
            "prob": 76.0,
            "odds": 1.50,
            "desc": "El Forest apelará a cortar el circuito de pases de Rodri y Foden con faltas tácticas."
        },
        "player_props": [
            ("Erling Haaland", "Más de 1.5 tiros al arco", 84.0, 1.42, "Líder de goleo de la Premier League con hambre insaciable."),
            ("Chris Wood (Forest)", "Más de 0.5 tiros a puerta", 65.0, 1.68, "Juego aéreo letal en centros laterales."),
            ("Phil Foden", "Más de 2.0 tiros totales", 76.0, 1.48, "Remate de media distancia ante bloques bajos.")
        ],
        "medical_bulletin": [
            ("Rodri / Kevin De Bruyne", "GESTIÓN DE MINUTOS", "Guardiola dosifica cargas pero mantiene a sus mejores armas en el once de salida.")
        ]
    },
    {
        "id": 5,
        "match": "Cienciano vs. Sport Huancayo",
        "home": "Cienciano",
        "away": "Sport Huancayo",
        "home_flag": "🔴👑",
        "away_flag": "🔴🟢",
        "tournament": "Liga 1 Te Apuesto • Clausura (Cusco)",
        "venue": "Estadio Inca Garcilaso de la Vega (Cusco, 3,400 msnm)",
        "time": "20:30 (ECU)",
        "attendance": "22,000 en estadio (~11M audiencia nacional)",
        "home_xg": 1.85,
        "away_xg": 0.70,
        "most_probable_score": "2 - 0",
        "score_alternatives": "1 - 0 (14.0%) • 2 - 1 (10.2%) • 1 - 1 (9.0%)",
        "badge_pill": "👑 LA FIJA IMPERIAL DEL CUSCO 83.0%",
        "badge_style": "background: linear-gradient(135deg, rgba(168, 85, 247, 0.3), rgba(126, 34, 206, 0.4)); border: 1px solid #a855f7; color: #f3e8ff;",
        "fija_title": "Cienciano o Empate (1X) + Menos de 3.5 goles",
        "fija_odds": 1.32,
        "fija_prob": 83.0,
        "fija_fair_odds": 1.20,
        "fija_rationale": "A 3,400 metros sobre el nivel del mar en el Garcilaso de la Vega, Cienciano maneja el ritmo con posesión paciente y una zaga férrea. Aunque Sport Huancayo está habituado a la altura, su rendimiento nocturno de visita baja considerablemente. La combinación 1X + Menos de 3.5 goles es casi impenetrable.",
        "p1x2": [62.0, 26.0, 12.0],
        "chart_data": [62.0, 26.0, 12.0],
        "other_markets": [
            ("Doble Oportunidad:", "Cienciano o Empate (1X)", "86.0% | @1.24"),
            ("Total de Goles:", "Menos de 3.5 goles totales", "78.0% | @1.35"),
            ("Córners Cusco:", "Más de 8.5 córners totales", "76.0% | @1.45"),
            ("Cienciano Gana Directo:", "Victoria de Cienciano (1)", "62.0% | @1.62"),
            ("Ambos Anotan:", "NO Ambos Equipos Anotan", "65.0% | @1.65")
        ],
        "goals": {
            "o15": (72.0, 1.40),
            "o25": (45.0, 2.05),
            "u35": (78.0, 1.35),
            "btts": (44.0, 2.00)
        },
        "corners": {
            "total_exp": "9.4 córners esperados",
            "line": "Más de 8.5 córners totales",
            "prob": 76.0,
            "odds": 1.45,
            "desc": "El balón vuela veloz en el Cusco; los disparos lejanos son desviados al córner por los guardametas."
        },
        "cards": {
            "total_exp": "5.0 tarjetas esperadas",
            "line": "Más de 4.5 tarjetas amarillas",
            "prob": 79.0,
            "odds": 1.52,
            "desc": "Fricción tradicional entre clubes del sur y centro andino del Perú."
        },
        "player_props": [
            ("Carlos Garcés (Cienciano)", "Más de 1.5 tiros al arco", 76.0, 1.55, "Goleador del 'Papá' con gran capacidad de definición aérea."),
            ("Christian Cueva (Cienciano)", "Más de 0.5 tiros al arco", 70.0, 1.68, "Tiros libres y disparos colocados al borde del área.")
        ],
        "medical_bulletin": [
            ("Cienciano", "PLANTEL COMPLETO MOTIVADO", "El 'Papá' busca asegurar cupo internacional ante su hinchada en el Cusco.")
        ]
    }
]

print(f"Total Matches configured: {len(MATCHES_DATA)}")

# 1. GENERAR SWITCHER HTML (.switcher-container con 6 .switcher-card)
switcher_html = '            <div class="switcher-container">\n'
for m in MATCHES_DATA:
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

# 2. GENERAR MATCH VIEWS HTML (#match-0 a #match-5)
views_html = ""
for m in MATCHES_DATA:
    active_cls = " active" if m["id"] == 0 else ""
    display_style = "display: block;" if m["id"] == 0 else "display: none;"
    
    # Sub-markets tags
    submarkets_html = ""
    for title, market, info in m["other_markets"]:
        submarkets_html += f'''                <span class="tag-pill tag-cyan" style="cursor: pointer; margin: 0.2rem; font-size: 0.76rem;" title="{title} {market} ({info})">
                    🎯 <strong>{title}</strong> {market} <span style="color: #ffffff;">({info})</span>
                </span>\n'''

    # Medical bulletin tags
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

    # Player props
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

print("Generated Views length:", len(views_html))

# 3. RECONSTRUIR AREA 1 EN index.html y dashboard_pronosticos.html
area1_full = f'''        <!-- ÁREA 1: CARTELERA DE LOS 6 PARTIDOS ESTELARES CON NAVEGADOR INTERACTIVO -->
        <section id="matches-section" style="margin-bottom: 3.5rem;">
            <div class="view-header">
                <div>
                    <div class="view-title">Cartelera de Élite: 6 Partidos Estelares</div>
                    <div class="view-desc">Simulaciones Monte Carlo (10,000 iteraciones), Poisson xG, SquadInjuryAgent y La Fija de Oro para la Tarde y Noche de hoy Sábado 7 de Noviembre</div>
                </div>
                <div style="display: flex; gap: 0.5rem;">
                    <button class="btn-subtle" onclick="window.print()">
                        <span>🖨️</span> Imprimir Reporte
                    </button>
                </div>
            </div>

            <!-- Switcher Tabs (0 a 5) -->
{switcher_html}
{views_html}
        </section>\n'''

# Configuración de los 6 gráficos Chart.js
chart_configs_js = '''var chartConfigs = [
            { id: 'chart1X2-0', labels: ['Real Madrid (2)', 'Empate (X)', 'Valencia (1)'], data: [61.0, 26.0, 13.0] },
            { id: 'chart1X2-1', labels: ['PSG (1)', 'Empate (X)', 'Troyes (2)'], data: [82.0, 12.0, 6.0] },
            { id: 'chart1X2-2', labels: ['Libertad FC (1)', 'Empate (X)', 'Emelec (2)'], data: [42.0, 42.5, 15.5] },
            { id: 'chart1X2-3', labels: ['FBC Melgar (1)', 'Empate (X)', 'Juan Pablo II (2)'], data: [78.0, 16.0, 6.0] },
            { id: 'chart1X2-4', labels: ['Man City (2)', 'Empate (X)', 'Nottingham Forest (1)'], data: [61.5, 24.5, 14.0] },
            { id: 'chart1X2-5', labels: ['Cienciano (1)', 'Empate (X)', 'Sport Huancayo (2)'], data: [62.0, 26.0, 12.0] }
        ];'''

# allFijasData con los 6
all_fijas_js = '''var allFijasData = [
            { id: 1, match: 'Valencia vs Real Madrid', pick: 'Real Madrid o Empate (X2)', prob: 87.0, odds: 1.24 },
            { id: 2, match: 'PSG vs Troyes', pick: 'PSG Gana el Partido (1)', prob: 90.0, odds: 1.20 },
            { id: 3, match: 'Libertad FC vs Emelec', pick: 'Libertad FC o Empate (1X)', prob: 84.5, odds: 1.30 },
            { id: 4, match: 'FBC Melgar vs Juan Pablo II', pick: 'FBC Melgar Gana el Partido (1)', prob: 89.0, odds: 1.22 },
            { id: 5, match: 'Nottingham Forest vs Man City', pick: 'Man City o Empate (X2) + Más 1.5 goles', prob: 86.5, odds: 1.33 },
            { id: 6, match: 'Cienciano vs Sport Huancayo', pick: 'Cienciano o Empate (1X) + Menos 3.5 goles', prob: 83.0, odds: 1.32 }
        ];'''

# Actualizar simulations_tomorrow_results.json
sim_results = {
    "GeneratedAt": "07/11/2026 12:00",
    "TargetDay": "Sábado (Tarde & Noche)",
    "TargetDate": "07/11/2026",
    "TemporalLabel": "Sábado 07/11 Tarde y Noche (6 Partidos Estelares)",
    "ActiveBankroll": 3267.52,
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
        } for m in MATCHES_DATA
    ]
}

with open('sports_agents/simulations_tomorrow_results.json', 'w', encoding='utf-8') as f:
    json.dump(sim_results, f, ensure_ascii=False, indent=2)
print("Updated sports_agents/simulations_tomorrow_results.json")

# Inyectar en archivos HTML
files_to_update = ['index.html', 'dashboard_pronosticos.html', '../index.html']

for fpath in files_to_update:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Skipping {fpath}: {e}")
        continue

    # Reemplazar Área 1
    # Área 1 empieza en <!-- ÁREA 1 o <section id="matches-section" o id="cartelera-section"
    # y termina antes de <!-- VISTA 2 o id="audit-section"
    pattern = r'<!-- ÁREA 1:.*?-->\s*<section.*?</section>'
    m_search = re.search(pattern, html, re.DOTALL)
    if not m_search:
        # probar otro patrón
        pattern = r'<section id="(?:matches|cartelera)-section".*?</section>'
        m_search = re.search(pattern, html, re.DOTALL)
    
    if m_search:
        html = html[:m_search.start()] + area1_full + html[m_search.end():]
        print(f"Replaced Area 1 in {fpath}")
    else:
        print(f"Could not find Area 1 pattern in {fpath}")

    # Reemplazar chartConfigs
    html = re.sub(r'var chartConfigs = \[.*?\];', chart_configs_js, html, flags=re.DOTALL)
    
    # Reemplazar allFijasData
    html = re.sub(r'var allFijasData = \[.*?\];', all_fijas_js, html, flags=re.DOTALL)

    # Actualizar título y botones de cabecera a 6 Partidos
    html = re.sub(
        r'<title>.*?</title>',
        '<title>SportsAI Analytics &middot; 6 Partidos Estelares &bull; Sábado 07/11 &bull; Win Rate & Autoaprendizaje</title>',
        html
    )
    html = re.sub(
        r'Motor Predictivo Multi-Agente &bull; \d+ Partidos Estelares &bull; [^<]+',
        'Motor Predictivo Multi-Agente &bull; 6 Partidos Estelares &bull; Sábado 07/11 (Tarde & Noche)',
        html
    )
    html = re.sub(
        r'⚽ Partidos &amp; Pronósticos \(\d+\)|⚽ Partidos & Pronósticos \(\d+\)',
        '⚽ Partidos & Pronósticos (6)',
        html
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Saved {fpath} successfully.")

print("COMPLETED ELITE 6 BUILD!")
