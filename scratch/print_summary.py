import json

data = json.load(open("sports_agents/simulations_tomorrow_results.json", encoding="utf-8"))
print("Fecha objetivo:", data.get("TargetDay"), data.get("TargetDate"))
for i, m in enumerate(data.get("Matches", [])):
    fija = m.get("la_fija_real", {})
    score = m.get("score_prediction", {}).get("most_probable_score", "N/A")
    print(f"{i+1}. {m.get('match')}:")
    print(f"   -> Marcador Modal: {score}")
    print(f"   -> La Fija: {fija.get('selection')} (@{fija.get('odds')} | {fija.get('probability')}%)")
    print(f"   -> Justificación: {fija.get('rationale')}")
