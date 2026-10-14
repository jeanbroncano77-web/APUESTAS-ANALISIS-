# -*- coding: utf-8 -*-
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open("scratch/dortmund_prediction_result.json", "r", encoding="utf-8") as f:
    pred = json.load(f)

print("Match:", pred.get("match"))
print("Fija Real:", pred.get("la_fija_real"))
print("All Fija Options:")
for opt in pred.get("all_fija_options", []):
    print(f" - {opt.get('category_code')}: {opt.get('selection')} @{opt.get('odds')} ({opt.get('probability')}%) | {opt.get('rationale')}")

print("\nScore Prediction:")
sp = pred.get("score_prediction", {})
print("1X2 Probs:", sp.get("1x2_probabilities"))
print("Top 5 Scores:", sp.get("top_5_scores"))
print("Simulated Averages:", sp.get("simulated_averages"))

print("\nPlayer Props:")
for p in pred.get("player_props", [])[:4]:
    print(f" - {p.get('player_name')} ({p.get('team')}): {p.get('market')} -> {p.get('selection')} @{p.get('odds')} ({p.get('probability_pct')}%)")

print("\nCorners Prediction:")
print(pred.get("corners_prediction"))

print("\nCards Prediction:")
print(pred.get("cards_prediction"))
