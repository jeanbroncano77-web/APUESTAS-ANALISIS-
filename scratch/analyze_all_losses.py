import json
import sys
sys.stdout.reconfigure(encoding="utf-8")

with open("sports_agents/audit_history.json", "r", encoding="utf-8") as f:
    d = json.load(f)

history = d["history"]
print(f"Total registros: {len(history)}")

losses = [r for r in history if r["status"] == "loss"]
wins = [r for r in history if r["status"] == "win"]

print(f"Total Aciertos: {len(wins)}")
print(f"Total Fallos: {len(losses)}")
print("\n" + "="*80)
print("LISTA COMPLETA DE TODOS LOS FALLOS HISTÓRICOS (#1 a #96):")
print("="*80)

for l in losses:
    fija_str = "👑 LA FIJA" if l.get("is_fija") else "OPCIÓN SECUNDARIA"
    print(f"\nID: #{l['id']} | {fija_str}")
    print(f"Partido: {l['match']} ({l.get('tournament', 'N/A')})")
    print(f"Selección: {l.get('selection', 'N/A')} @{l.get('odds', 'N/A')} (Conf: {l.get('confidence', 'N/A')}%)")
    print(f"PnL: ${l.get('pnl', 'N/A')}")
    print(f"Diagnóstico: {l.get('diagnostic', 'Sin diagnóstico')}")

print("\n" + "="*80)
print("DISTRIBUCIÓN DE FALLOS POR MERCADO:")
print("="*80)
markets = {}
for l in losses:
    m = l.get('selection', '')
    if '[' in m and ']' in m:
        cat = m[m.find('[')+1:m.find(']')]
    else:
        cat = "Otro"
    markets[cat] = markets.get(cat, 0) + 1

for k, v in markets.items():
    print(f"- {k}: {v} fallos")
