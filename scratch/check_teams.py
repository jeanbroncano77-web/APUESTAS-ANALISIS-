# -*- coding: utf-8 -*-
import os
import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open("sports_agents/data_scout_agent.py", "r", encoding="utf-8") as f:
    text = f.read()

teams_in_scout = re.findall(r'"([A-Za-z\s\(\)\.\'\-]+)":\s*\{\s*"fifa_rank"', text)
print("Teams in DataScoutAgent:", teams_in_scout)

matches_in_scout = re.findall(r'\(\s*"([^"]+)"\s*,\s*"([^"]+)"\s*\):', text)
print("\nMatches in DataScoutAgent:")
for m in matches_in_scout:
    print(" -", m[0], "vs", m[1])
