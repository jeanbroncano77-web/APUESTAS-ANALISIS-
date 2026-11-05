# -*- coding: utf-8 -*-
import json
from datetime import datetime

feedback_file = "sports_agents/autonomous_feedback_log.json"
with open(feedback_file, "r", encoding="utf-8") as f:
    fb_db = json.load(f)

calibrations = fb_db.get("calibrations", [])

new_cycle_130 = {
    "cycle": 130,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "action": "CASO DE ÉXITO #16: JORNADA DORADA EUROPEA Y SUDAMERICANA (11/12 ACIERTOS - 91.7%), AUTOPSIA #15 (PORTO 2-1 NÁPOLES) & REGLA ANTI-FOMO #122",
    "observations": [
        "[JORNADA DE ALTA EFECTIVIDAD (11 DE 12 ACIERTOS - 91.7%)]: Pleno en las fijas europeas de alta certeza (Real Madrid 0-3, Liverpool 1-2, City 1-2, Arsenal 0-2, PSV 2-1, Dortmund 2-1, Lens 1-0) y pleno sudamericano (Liga de Quito 2-0 en Casa Blanca, Flamengo 2-1, Paranaense 1-1, Botafogo 2-1). La cobertura de doble oportunidad (1X/X2) en equipos dominantes neutralizó los empates cerrados en Estambul y Curitiba.",
        "[AUTOPSIA DE FALLO #15 - PORTO 2-1 NÁPOLES]: El modelo asignó X2 al Nápoles confiando en el bloque bajo de Antonio Conte. Sin embargo, en el Estádio do Dragão, el Porto recurrió a la agresividad por bandas y balones detenidos (8 córners a favor), encontrando el gol de la victoria en el minuto 84. Regla derivada: en visitas a históricos portugueses que juegan al límite físico, el bloque bajo pasivo de visita es vulnerable si se cede la iniciativa total.",
        "[LECCIÓN DE AUTOAPRENDIZAJE Y PSICOLOGÍA OPERATIVA - REGLA DE ORO #122]: La duda o 'miedo' que sintió el usuario antes de la jornada no es una falla moral ni cobardía; es el escudo biológico contra la bancarrota que le impidió arriesgar $20 de sus $24.90. El sesgo de resultado ('ayer atinaste casi todo, me arrepiento de no meterle') es el principal disparador de bancarrota en apostadores novatos. Se ratifica la Regla #122: Jamás operar por FOMO (miedo a perderse ganancias) y mantener la preservación de capital por encima del ego.",
        "[MÉTRICAS OFICIALES CONSOLIDADAS TRAS JORNADA MIÉRCOLES 4]: 198 pronósticos auditados | 173 Aciertos / 25 Fallos | Win Rate Global: 87.4% | Win Rate Fijas: 87.3% (138/158) | Brier Score: 0.1191 | Banca Modelo: $2,976.52 USD | Saldo Real Usuario: $24.90 USD intactos."
    ],
    "system_health": "Calibrado de Precisión (Win Rate Global: 87.4% [173/198] | Win Rate Fijas: 87.3% [138/158] | Ciclo #130)"
}

calibrations.append(new_cycle_130)
fb_db["calibrations"] = calibrations
fb_db["cycles_completed"] = 130
fb_db["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(feedback_file, "w", encoding="utf-8") as f:
    json.dump(fb_db, f, ensure_ascii=False, indent=2)

print("✓ Ciclo 130 agregado preservando todos los ciclos históricos.")
