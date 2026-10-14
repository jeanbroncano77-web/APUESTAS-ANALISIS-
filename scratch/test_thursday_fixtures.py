# -*- coding: utf-8 -*-
import sys
import os
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.abspath("."))

from sports_agents import SportsDirectorAgent
director = SportsDirectorAgent()
fixtures = [
    ('Italia', 'Bélgica', 'DOBLE_OPORTUNIDAD'),
    ('Inglaterra', 'Finlandia', 'GOL_EQUIPO'),
    ('Israel', 'Francia', 'DOBLE_OPORTUNIDAD'),
    ('Macedonia del Norte', 'Albania', 'GOLES_UNDER'),
    ('Bosnia y Herzegovina', 'Turquía', 'GOL_EQUIPO'),
    ('Venezuela', 'Corea del Sur', 'DOBLE_OPORTUNIDAD')
]
for h, a, cat in fixtures:
    p = director.predict_fixture(h, a, preferred_market_category=cat)
    fija = p.get('la_fija_real', {})
    mkt = fija.get('market', 'N/A')
    sel = fija.get('selection', 'N/A')
    odds = fija.get('odds', 1.0)
    prob = fija.get('probability', 0.0)
    print(f"{h} vs {a}: [{mkt}] {sel} @{odds} ({prob}%)")
