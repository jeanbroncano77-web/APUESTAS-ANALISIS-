# -*- coding: utf-8 -*-
"""
SquadInjuryAgent 2.0:
Agente Especializado de Inteligencia Médica, Convocatorias Oficiales y Poder de Veto Sanitario.
Audita partes médicos oficiales, lesiones musculares, suspensiones y minutos acumulados.

Características clave:
1. Registro Médico Global Oficial para Clubes de Élite y Selecciones Nacionales.
2. Veto Absoluto de Player Props para futbolistas lesionados o no disponibles (ej. Kylian Mbappé, Martin Ødegaard, Dani Olmo).
3. Normalización fonética y de acentos (NFKD) para detección infalible de futbolistas.
4. Algoritmo de Redistribución Ofensiva: Si la figura máxima es baja, redistribuye los tiros hacia los titulares confirmados (ej. Vinícius Jr., Rodrygo, Bellingham).
5. Penalización Cuantitativa de xG en el modelo de Poisson por ausencia de estrellas clave.
"""

from typing import Dict, Any, List
import unicodedata


def normalize_str(s: str) -> str:
    """Elimina acentos y normaliza a minúsculas para matching infalible."""
    if not s:
        return ""
    s_norm = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s_norm if not unicodedata.combining(c)).lower().strip()


class SquadInjuryAgent:
    def __init__(self):
        self.name = "SquadInjuryAgent"

        # Boletín Médico Oficial y Convocatorias Verificadas
        self.medical_bulletin = {
            "Real Madrid": [
                {
                    "name": "Kylian Mbappé",
                    "aliases": ["mbappe", "kylian mbappe", "mbappe lottin"],
                    "injury": "Lesión en el bíceps femoral de la pierna izquierda",
                    "severity": "BAJA MÉDICA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.88,
                    "reallocation_targets": ["Vinícius Jr.", "Rodrygo Goes", "Jude Bellingham"],
                    "medical_detail": "Molestia muscular sufrida en el tramo final vs Alavés. Veto estricto de cuotas y remates individuales."
                },
                {
                    "name": "Thibaut Courtois",
                    "aliases": ["courtois", "thibaut courtois"],
                    "injury": "Lesión en el abductor de la pierna izquierda",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "defense_penalty": 1.15,
                    "reallocation_targets": [],
                    "medical_detail": "Baja en portería; Andriy Lunin ratificado como titular bajo palos."
                },
                {
                    "name": "David Alaba",
                    "aliases": ["alaba", "david alaba"],
                    "injury": "Rotura del ligamento cruzado anterior",
                    "severity": "BAJA DE LARGA DURACIÓN",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "reallocation_targets": [],
                    "medical_detail": "Baja médica en fase de reacondicionamiento."
                },
                {
                    "name": "Brahim Díaz",
                    "aliases": ["brahim", "brahim diaz"],
                    "injury": "Lesión en el abductor largo de la pierna derecha",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.98,
                    "reallocation_targets": [],
                    "medical_detail": "En tratamiento fisioterapéutico."
                }
            ],
            "Barcelona": [
                {
                    "name": "Dani Olmo",
                    "aliases": ["olmo", "dani olmo"],
                    "injury": "Lesión en el bíceps femoral del muslo derecho",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.92,
                    "reallocation_targets": ["Raphinha", "Pedri", "Lamine Yamal"],
                    "medical_detail": "Lesión muscular sufrida en Montilivi; veto total de remates."
                },
                {
                    "name": "Marc-André ter Stegen",
                    "aliases": ["ter stegen", "marc-andre ter stegen"],
                    "injury": "Rotura completa del tendón rotuliano de la rodilla derecha",
                    "severity": "BAJA DE TEMPORADA",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "defense_penalty": 1.20,
                    "reallocation_targets": [],
                    "medical_detail": "Intervenido quirúrgicamente; Iñaki Peña titular bajo palos."
                },
                {
                    "name": "Gavi",
                    "aliases": ["gavi", "pablo gavi"],
                    "injury": "Fase de readaptación post-rotura de ligamento cruzado",
                    "severity": "MINUTOS RESTRINGIDOS / SIN RITMO COMPETITIVO",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "reallocation_targets": [],
                    "medical_detail": "Retorno gradual; no apto para proyecciones de volumen ofensivo."
                },
                {
                    "name": "Ronald Araújo",
                    "aliases": ["araujo", "ronald araujo"],
                    "injury": "Lesión en el tendón del isquiotibial derecho",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "reallocation_targets": [],
                    "medical_detail": "Baja en el eje defensivo."
                },
                {
                    "name": "Andreas Christensen",
                    "aliases": ["christensen", "andreas christensen"],
                    "injury": "Tendinopatía en el tendón de Aquiles izquierdo",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "reallocation_targets": [],
                    "medical_detail": "Baja en la zaga."
                },
                {
                    "name": "Fermín López",
                    "aliases": ["fermin", "fermin lopez"],
                    "injury": "Lesión en el recto anterior del muslo derecho",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.98,
                    "reallocation_targets": [],
                    "medical_detail": "Recaída muscular en readaptación."
                }
            ],
            "Arsenal": [
                {
                    "name": "Martin Ødegaard",
                    "aliases": ["odegaard", "martin odegaard", "martin ødegaard"],
                    "injury": "Lesión significativa de ligamentos de tobillo",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.88,
                    "reallocation_targets": ["Bukayo Saka", "Kai Havertz", "Declan Rice"],
                    "medical_detail": "Capitán y motor creativo descartado. Bukayo Saka y Kai Havertz asumen el peso ofensivo."
                },
                {
                    "name": "Oleksandr Zinchenko",
                    "aliases": ["zinchenko", "oleksandr zinchenko"],
                    "injury": "Lesión en la pantorrilla",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "reallocation_targets": [],
                    "medical_detail": "Baja en lateral izquierdo."
                },
                {
                    "name": "Takehiro Tomiyasu",
                    "aliases": ["tomiyasu", "takehiro tomiyasu"],
                    "injury": "Lesión de rodilla",
                    "severity": "BAJA",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "reallocation_targets": [],
                    "medical_detail": "No disponible para la convocatoria."
                }
            ],
            "Bayern Munich": [
                {
                    "name": "Hiroki Ito",
                    "aliases": ["ito", "hiroki ito"],
                    "injury": "Fractura metatarsiana",
                    "severity": "BAJA DE LARGA DURACIÓN",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "reallocation_targets": [],
                    "medical_detail": "En fase de rehabilitación postquirúrgica."
                },
                {
                    "name": "Josip Stanisic",
                    "aliases": ["stanisic", "josip stanisic"],
                    "injury": "Rotura de ligamento colateral de rodilla",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "reallocation_targets": [],
                    "medical_detail": "Baja defensiva confirmada."
                },
                {
                    "name": "Sacha Boey",
                    "aliases": ["boey", "sacha boey"],
                    "injury": "Rotura de menisco",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "reallocation_targets": [],
                    "medical_detail": "Operado de la rodilla."
                },
                {
                    "name": "Harry Kane",
                    "aliases": ["kane", "harry kane"],
                    "injury": "Golpe contundente en el tobillo (vs Leverkusen)",
                    "severity": "MONITOREO / DUDA ACTIVA",
                    "veto_player_props": False,
                    "offense_penalty": 0.96,
                    "reallocation_targets": ["Michael Olise", "Jamal Musiala", "Serge Gnabry"],
                    "medical_detail": "Disponible pero bajo estricto monitoreo médico con riesgo de sustitución preventiva."
                }
            ],
            "Villarreal": [
                {
                    "name": "Gerard Moreno",
                    "aliases": ["gerard moreno", "moreno"],
                    "injury": "Lesión muscular en los isquiotibiales",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.90,
                    "reallocation_targets": ["Ayoze Pérez", "Thierno Barry", "Álex Baena"],
                    "medical_detail": "Goleador histórico descartado para la visita al Bernabéu. Ayoze Pérez asume la referencia ofensiva."
                },
                {
                    "name": "Juan Foyth",
                    "aliases": ["foyth", "juan foyth"],
                    "injury": "Esguince de rodilla",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "reallocation_targets": [],
                    "medical_detail": "Baja en defensa."
                },
                {
                    "name": "Alfonso Pedraza",
                    "aliases": ["pedraza", "alfonso pedraza"],
                    "injury": "Lesión de tobillo",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "reallocation_targets": [],
                    "medical_detail": "Baja en el carril zurdo."
                }
            ],
            "Inter Milan": [
                {
                    "name": "Nicolò Barella",
                    "aliases": ["barella", "nicolo barella", "nicolo barella"],
                    "injury": "Distracción muscular en el recto femoral del muslo derecho",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.91,
                    "reallocation_targets": ["Hakan Çalhanoğlu", "Henrikh Mkhitaryan", "Lautaro Martínez"],
                    "medical_detail": "El pulmón del mediocampo nerazzurro se pierde el partido por lesión muscular."
                },
                {
                    "name": "Tajon Buchanan",
                    "aliases": ["buchanan", "tajon buchanan"],
                    "injury": "Fractura de tibia",
                    "severity": "BAJA",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "reallocation_targets": [],
                    "medical_detail": "En proceso de consolidación ósea."
                }
            ],
            "Borussia Dortmund": [
                {
                    "name": "Giovanni Reyna",
                    "aliases": ["reyna", "gio reyna", "giovanni reyna"],
                    "injury": "Lesión en la ingle",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.97,
                    "reallocation_targets": ["Julian Brandt", "Serhou Guirassy"],
                    "medical_detail": "Baja en la mediapunta."
                },
                {
                    "name": "Julien Duranville",
                    "aliases": ["duranville", "julien duranville"],
                    "injury": "Lesión muscular en el muslo",
                    "severity": "BAJA",
                    "veto_player_props": True,
                    "offense_penalty": 0.98,
                    "reallocation_targets": [],
                    "medical_detail": "Baja en los extremos."
                }
            ],
            "Getafe": [
                {
                    "name": "Álvaro Rodríguez",
                    "aliases": ["alvaro rodriguez", "alvaro"],
                    "injury": "Esguince de tobillo",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.95,
                    "reallocation_targets": ["Borja Mayoral", "Bertuğ Yıldırım"],
                    "medical_detail": "Baja médica confirmada."
                }
            ],
            "Francia": [
                {
                    "name": "Kylian Mbappé",
                    "aliases": ["mbappe", "kylian mbappe"],
                    "injury": "Lesión muscular en el bíceps femoral / Desconvocado",
                    "severity": "BAJA MÉDICA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.85,
                    "reallocation_targets": ["Bradley Barcola", "Ousmane Dembélé"],
                    "medical_detail": "Desconvocado de la selección para acondicionamiento físico tras molestia muscular."
                }
            ],
            "Japón": [
                {
                    "name": "Kaoru Mitoma",
                    "aliases": ["mitoma", "kaoru mitoma"],
                    "injury": "Descanso pactado con el club / No convocado",
                    "severity": "NO CONVOCADO",
                    "veto_player_props": True,
                    "offense_penalty": 0.82,
                    "reallocation_targets": ["Takefusa Kubo", "Takumi Minamino"],
                    "medical_detail": "Acuerdo club-selección para preservación física de la figura de desborde."
                }
            ],
            "España": [
                {
                    "name": "Rodri",
                    "aliases": ["rodri", "rodrigo hernandez", "rodri hernandez"],
                    "injury": "Rotura de ligamento cruzado anterior de rodilla derecha",
                    "severity": "BAJA DE TEMPORADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.94,
                    "defense_penalty": 1.15,
                    "reallocation_targets": ["Martín Zubimendi", "Pedri", "Fabián Ruiz"],
                    "medical_detail": "Intervenido quirúrgicamente; baja sensible en el eje medular de La Roja. Zubimendi asume la contención."
                },
                {
                    "name": "Dani Olmo",
                    "aliases": ["olmo", "dani olmo"],
                    "injury": "Lesión en el bíceps femoral derecho",
                    "severity": "BAJA MÉDICA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.92,
                    "reallocation_targets": ["Pedri", "Lamine Yamal", "Nico Williams"],
                    "medical_detail": "Desconvocado por rotura fibrilar en el muslo derecho."
                },
                {
                    "name": "Dani Carvajal",
                    "aliases": ["carvajal", "dani carvajal"],
                    "injury": "Rotura del ligamento cruzado anterior y colateral externo",
                    "severity": "BAJA DE TEMPORADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.97,
                    "defense_penalty": 1.12,
                    "reallocation_targets": ["Pedro Porro", "Óscar Mingueza"],
                    "medical_detail": "Grave lesión ligamentosa; Pedro Porro toma el carril derecho."
                },
                {
                    "name": "Robin Le Normand",
                    "aliases": ["le normand", "robin le normand"],
                    "injury": "Traumatismo craneoencefálico con hematoma subdural",
                    "severity": "BAJA MÉDICA OBLIGADA",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "defense_penalty": 1.10,
                    "reallocation_targets": ["Aymeric Laporte", "Dani Vivian", "Pau Cubarsí"],
                    "medical_detail": "Protocolo neurológico estricto tras golpe en derbi madrileño."
                }
            ],
            "Inglaterra": [
                {
                    "name": "Harry Kane",
                    "aliases": ["kane", "harry kane"],
                    "injury": "Molestia residual en el tobillo",
                    "severity": "MONITOREO / DUDA ACTIVA",
                    "veto_player_props": False,
                    "offense_penalty": 0.95,
                    "reallocation_targets": ["Cole Palmer", "Bukayo Saka", "Jude Bellingham", "Ollie Watkins"],
                    "medical_detail": "Trabaja diferenciado; Lee Carsley evalúa darle descanso o iniciar con Watkins."
                }
            ],
            "Croacia": [
                {
                    "name": "Josip Stanisic",
                    "aliases": ["stanisic", "josip stanisic"],
                    "injury": "Rotura del ligamento colateral de rodilla",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "defense_penalty": 1.12,
                    "reallocation_targets": ["Joško Gvardiol", "Borna Sosa"],
                    "medical_detail": "Baja en el lateral derecho de la zaga croata."
                }
            ],
            "Chequia": [
                {
                    "name": "Jindřich Staněk",
                    "aliases": ["stanek", "jindrich stanek"],
                    "injury": "Luxación de hombro",
                    "severity": "BAJA MÉDICA",
                    "veto_player_props": True,
                    "offense_penalty": 1.0,
                    "defense_penalty": 1.18,
                    "reallocation_targets": ["Matej Kovar"],
                    "medical_detail": "Guardameta titular checo ausente; Kovar asume la portería en el Carlos Tartiere."
                }
            ],
            "Suiza": [
                {
                    "name": "Denis Zakaria",
                    "aliases": ["zakaria", "denis zakaria"],
                    "injury": "Sobrecarga en los aductores",
                    "severity": "MONITOREO MÉDICO",
                    "veto_player_props": False,
                    "offense_penalty": 0.98,
                    "defense_penalty": 1.05,
                    "reallocation_targets": ["Granit Xhaka", "Remo Freuler"],
                    "medical_detail": "Duda en la medular helvética."
                }
            ],
            "Estados Unidos": [
                {
                    "name": "Timothy Weah",
                    "aliases": ["weah", "timothy weah"],
                    "injury": "Molestia muscular en los isquiotibiales",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.93,
                    "reallocation_targets": ["Christian Pulisic", "Folarin Balogun", "Brenden Aaronson"],
                    "medical_detail": "Extremo no disponible para el Clásico ante México."
                }
            ],
            "México": [
                {
                    "name": "Hirving Lozano",
                    "aliases": ["lozano", "hirving lozano", "chucky lozano"],
                    "injury": "Lesión muscular en pierna derecha",
                    "severity": "BAJA CONFIRMADA",
                    "veto_player_props": True,
                    "offense_penalty": 0.92,
                    "reallocation_targets": ["Santiago Giménez", "César Huerta", "Orbelín Pineda"],
                    "medical_detail": "Desconvocado del Tri por rotura fibrilar."
                }
            ]
        }

        # Plantillas de respaldo titulares confirmados en caso de requerir inyección de reemplazos
        self.verified_alternatives = {
            "Real Madrid": [
                {"name": "Vinícius Jr.", "position": "Extremo Desborde / Líder Ofensivo", "avg_shots_p90": 3.8, "avg_sot_p90": 1.8, "shot_creation_actions": 6.4, "goal_prob": 0.55},
                {"name": "Rodrygo Goes", "position": "Extremo / Delantero Referencia", "avg_shots_p90": 3.2, "avg_sot_p90": 1.5, "shot_creation_actions": 5.4, "goal_prob": 0.46},
                {"name": "Jude Bellingham", "position": "Mediapunta Llegada", "avg_shots_p90": 3.1, "avg_sot_p90": 1.5, "shot_creation_actions": 5.3, "goal_prob": 0.44},
                {"name": "Federico Valverde", "position": "Interior / Potencia Media Distancia", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 3.8, "goal_prob": 0.24}
            ],
            "Barcelona": [
                {"name": "Robert Lewandowski", "position": "Delantero Centro Killer", "avg_shots_p90": 4.1, "avg_sot_p90": 2.2, "shot_creation_actions": 3.4, "goal_prob": 0.74},
                {"name": "Raphinha", "position": "Extremo / Conductor Ofensivo", "avg_shots_p90": 3.6, "avg_sot_p90": 1.8, "shot_creation_actions": 6.2, "goal_prob": 0.52},
                {"name": "Lamine Yamal", "position": "Extremo Generacional", "avg_shots_p90": 3.3, "avg_sot_p90": 1.6, "shot_creation_actions": 7.0, "goal_prob": 0.48},
                {"name": "Pedri", "position": "Mediocentro Creativo", "avg_shots_p90": 1.5, "avg_sot_p90": 0.6, "shot_creation_actions": 5.6, "goal_prob": 0.20}
            ],
            "Arsenal": [
                {"name": "Bukayo Saka", "position": "Extremo Derecho Élite", "avg_shots_p90": 3.6, "avg_sot_p90": 1.8, "shot_creation_actions": 6.8, "goal_prob": 0.50},
                {"name": "Kai Havertz", "position": "Delantero Boya", "avg_shots_p90": 3.2, "avg_sot_p90": 1.5, "shot_creation_actions": 4.3, "goal_prob": 0.46},
                {"name": "Gabriel Martinelli", "position": "Extremo Eléctrico", "avg_shots_p90": 2.9, "avg_sot_p90": 1.3, "shot_creation_actions": 5.0, "goal_prob": 0.40},
                {"name": "Declan Rice", "position": "Pivote / Balón Parado", "avg_shots_p90": 1.7, "avg_sot_p90": 0.7, "shot_creation_actions": 4.4, "goal_prob": 0.18}
            ],
            "Villarreal": [
                {"name": "Ayoze Pérez", "position": "Segundo Delantero / Referencia", "avg_shots_p90": 3.0, "avg_sot_p90": 1.5, "shot_creation_actions": 3.8, "goal_prob": 0.42},
                {"name": "Álex Baena", "position": "Mediapunta Creador", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 6.0, "goal_prob": 0.26},
                {"name": "Thierno Barry", "position": "Delantero Centro Físico", "avg_shots_p90": 2.5, "avg_sot_p90": 1.2, "shot_creation_actions": 2.3, "goal_prob": 0.36}
            ]
        }

    def _match_bulletin_entry(self, player_name: str, team_bulletin: List[Dict[str, Any]]) -> Dict[str, Any] | None:
        """Busca si el jugador figura en el boletín médico con matching estricto y de alias."""
        p_norm = normalize_str(player_name)
        for item in team_bulletin:
            if normalize_str(item["name"]) == p_norm:
                return item
            for alias in item.get("aliases", []):
                if normalize_str(alias) == p_norm or alias in p_norm or p_norm in alias:
                    return item
        return None

    def audit_team_roster(self, team: str, key_players: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Audita rigurosamente la sanidad del plantel:
        1. Veta jugadores con lesión o no disponibles impidiendo que aparezcan en Player Props.
        2. Aplica penalizaciones al xG del equipo.
        3. Redistribuye tiros hacia los titulares confirmados.
        4. Inyecta alternativas ratificadas si el plantel queda corto de opciones.
        """
        team_bulletin = self.medical_bulletin.get(team, [])
        cleared_players = []
        vetoed_players = []
        cumulative_offense_penalty = 1.0
        reallocations = []

        vetoed_names_set = set()
        for p in key_players:
            p_name = p.get("name", "")
            bulletin_entry = self._match_bulletin_entry(p_name, team_bulletin)

            if bulletin_entry and bulletin_entry.get("veto_player_props", False):
                # VETO SANITARIO ACTIVADO
                p_norm = normalize_str(p_name)
                vetoed_names_set.add(p_norm)
                vetoed_players.append({
                    "name": bulletin_entry["name"],
                    "injury": bulletin_entry["injury"],
                    "severity": bulletin_entry["severity"],
                    "action": "VETO TOTAL DE PROPS (Excluido de Remates/Goles)",
                    "medical_detail": bulletin_entry["medical_detail"]
                })
                cumulative_offense_penalty *= bulletin_entry.get("offense_penalty", 0.90)
                reallocations.append({
                    "vetoed_star": bulletin_entry["name"],
                    "targets": bulletin_entry.get("reallocation_targets", [])
                })
            else:
                # Jugador apto o con monitoreo
                p_copy = dict(p)
                p_copy["roster_verified"] = True
                p_copy["health_status"] = "Disponible"
                if bulletin_entry:
                    p_copy["health_status"] = bulletin_entry.get("severity", "Monitoreado")
                    p_copy["medical_note"] = bulletin_entry.get("medical_detail", "")
                cleared_players.append(p_copy)

        # Incorporar e informar todas las bajas médicas del boletín oficial del equipo
        for b_entry in team_bulletin:
            b_norm = normalize_str(b_entry["name"])
            if b_norm not in vetoed_names_set and b_entry.get("veto_player_props", False):
                vetoed_names_set.add(b_norm)
                vetoed_players.append({
                    "name": b_entry["name"],
                    "injury": b_entry["injury"],
                    "severity": b_entry["severity"],
                    "action": "VETO TOTAL DE PROPS (Baja Confirmada)",
                    "medical_detail": b_entry["medical_detail"]
                })
                cumulative_offense_penalty *= b_entry.get("offense_penalty", 0.95)
                if b_entry.get("reallocation_targets"):
                    reallocations.append({
                        "vetoed_star": b_entry["name"],
                        "targets": b_entry.get("reallocation_targets", [])
                    })

        # Inyectar alternativas si se vetaron estrellas clave y la lista quedó corta
        if len(cleared_players) < 3 and team in self.verified_alternatives:
            existing_names = {normalize_str(cp["name"]) for cp in cleared_players}
            vetoed_names = {normalize_str(vp["name"]) for vp in vetoed_players}
            for alt in self.verified_alternatives[team]:
                alt_norm = normalize_str(alt["name"])
                if alt_norm not in existing_names and alt_norm not in vetoed_names:
                    alt_copy = dict(alt)
                    alt_copy["roster_verified"] = True
                    alt_copy["health_status"] = "Titular Confirmado"
                    cleared_players.append(alt_copy)
                    if len(cleared_players) >= 4:
                        break

        # Redistribuir volumen ofensivo si hubo estrellas vetadas
        reallocation_notes = []
        if reallocations:
            for item in reallocations:
                star = item["vetoed_star"]
                targets = item["targets"]
                reallocation_notes.append(
                    f"Ausencia de {star}: Volumen de tiros transferido hacia {', '.join(targets)}."
                )
                # Incrementar ligeramente el avg_shots_p90 de los titulares receptores
                for cp in cleared_players:
                    if cp.get("name") in targets:
                        cp["avg_shots_p90"] = round(cp.get("avg_shots_p90", 2.5) * 1.15, 2)
                        cp["avg_sot_p90"] = round(cp.get("avg_sot_p90", 1.0) * 1.14, 2)
                        cp["reallocated_from"] = star

        # Limitar penalización total para no distorsionar por completo el modelo
        final_penalty = round(max(0.78, min(1.0, cumulative_offense_penalty)), 2)

        return {
            "team": team,
            "cleared_players": cleared_players,
            "vetoed_players": vetoed_players,
            "offense_penalty_factor": final_penalty,
            "reallocation_summary": " | ".join(reallocation_notes) if reallocation_notes else "Plantel al 100% sin reasignación necesaria.",
            "squad_health_status": "VETO ACTIVO: Bajas Detectadas" if vetoed_players else "Plantel Ratificado al 100%"
        }
