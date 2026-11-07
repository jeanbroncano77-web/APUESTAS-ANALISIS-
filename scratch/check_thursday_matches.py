# -*- coding: utf-8 -*-
import json

with open('sports_agents/simulations_tomorrow_results.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print('Day:', d.get('TargetDay'), d.get('TargetDate'))
print('Total matches:', len(d.get('Matches', [])))
for i, m in enumerate(d.get('Matches', [])):
    h = m.get('home_team')
    a = m.get('away_team')
    fija = m.get('la_fija_real', {})
    score = m.get('score_prediction', {}).get('most_probable_score', '')
    sel = fija.get('selection')
    odds = fija.get('odds')
    prob = fija.get('probability')
    print(f"{i+1}. {h} vs {a} | Score: {score} | Fija: {sel} @{odds} ({prob}%)")

