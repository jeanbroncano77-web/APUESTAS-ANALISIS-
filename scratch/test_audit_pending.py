import os
import sys
import json
from datetime import datetime, timedelta, timezone

current_dir = os.path.abspath("sports_agents")
audit_file = os.path.join(current_dir, "audit_history.json")
cal_file = os.path.join(current_dir, "official_calendar.json")

with open(audit_file, "r", encoding="utf-8") as f_aud:
    audit_db = json.load(f_aud)

with open(cal_file, "r", encoding="utf-8") as f_cal:
    cal_db = json.load(f_cal)

history = audit_db.get("history", [])
audited_matches_set = {r.get("match") for r in history}
print("Total audited so far:", len(history))
print("Audited set sample:", list(audited_matches_set)[:5])

# Current time
utc_now = datetime.now(timezone.utc)
lima_now = utc_now - timedelta(hours=5)
today_iso = lima_now.strftime("%Y-%m-%d")
print("today_iso:", today_iso, "lima_now.hour:", lima_now.hour)

for date_iso, cal_entry in sorted(cal_db.items()):
    condition = date_iso < today_iso or (date_iso == today_iso and lima_now.hour >= 18)
    if condition:
        fixtures = cal_entry.get("fixtures", [])
        for f in fixtures:
            m_key = f"{f[0]} vs {f[1]}"
            if m_key not in audited_matches_set:
                print(f"PENDING AUDIT: date={date_iso}, match={m_key}")
