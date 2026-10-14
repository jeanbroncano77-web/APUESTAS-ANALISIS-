import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('sports_agents/simulations_tomorrow_results.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print('TargetDay:', d.get('TargetDay'), 'TargetDate:', d.get('TargetDate'), 'TemporalLabel:', d.get('TemporalLabel'))
for m in d.get('Matches', []):
    fija = m.get('la_fija_real', {})
    print(f"Match: {m.get('match')} | Tournament: {m.get('context', {}).get('tournament')} | Fija: {fija.get('selection')} (@{fija.get('odds')})")
