import urllib.request
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

url = "https://api.github.com/repos/jeanbroncano77-web/APUESTAS-ANALISIS-/actions/runs"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        print(f"Total runs: {data.get('total_count')}")
        for r in data.get("workflow_runs", [])[:10]:
            print(f"Run #{r.get('run_number')}: {r.get('name')} | Event: {r.get('event')} | Status: {r.get('status')} | Conclusion: {r.get('conclusion')} | CreatedAt: {r.get('created_at')}")
except Exception as err:
    print(f"Error consultando GitHub API: {err}")
