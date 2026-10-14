import re

builder_code = open("sports_agents/build_dashboard_tomorrow.py", encoding="utf-8").read()

sunday_matches = ["Liverpool", "Manchester City", "Crystal Palace", "Elche", "Liga de Quito", "Lazio"]
for sm in sunday_matches:
    count = builder_code.count(sm)
    print(f"Match '{sm}' in build_dashboard_tomorrow.py: {count} times")

# Where does it appear?
for line_i, line in enumerate(builder_code.splitlines()):
    if any(sm in line for sm in sunday_matches):
        print(f"Line {line_i+1}: {line.strip()[:100]}")
