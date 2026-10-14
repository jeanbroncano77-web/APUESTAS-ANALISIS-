import json

with open("sports_agents/autonomous_feedback_log.json", encoding="utf-8") as f:
    fb = json.load(f)

print("Cycles completed:", fb.get("cycles_completed"))
print("Last updated:", fb.get("last_updated"))
calibs = fb.get("calibrations", [])
print(f"Total calibrations: {len(calibs)}")
if calibs:
    print("Latest calibration:")
    print(json.dumps(calibs[-1], indent=2, ensure_ascii=False))
