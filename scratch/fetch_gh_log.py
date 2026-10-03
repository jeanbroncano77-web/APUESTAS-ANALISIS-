import subprocess
import urllib.request
import json

p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
out, _ = p.communicate('protocol=https\nhost=github.com\n')
token = dict(l.split('=', 1) for l in out.splitlines() if '=' in l).get('password')

class NoAuthRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, hdrs, newurl):
        r = super().redirect_request(req, fp, code, msg, hdrs, newurl)
        if r and 'Authorization' in r.headers:
            del r.headers['Authorization']
        return r

opener = urllib.request.build_opener(NoAuthRedirect)

# Get latest run
req_runs = urllib.request.Request(
    'https://api.github.com/repos/jeanbroncano77-web/APUESTAS-ANALISIS-/actions/runs?per_page=1',
    headers={'Authorization': f'token {token}', 'User-Agent': 'SportsAI'}
)
runs = json.loads(urllib.request.urlopen(req_runs).read())
latest_run = runs['workflow_runs'][0]
print(f"Run ID: {latest_run['id']} - Status: {latest_run['status']} - Conclusion: {latest_run['conclusion']}")

req_jobs = urllib.request.Request(
    f"https://api.github.com/repos/jeanbroncano77-web/APUESTAS-ANALISIS-/actions/runs/{latest_run['id']}/jobs",
    headers={'Authorization': f'token {token}', 'User-Agent': 'SportsAI'}
)
jobs = json.loads(urllib.request.urlopen(req_jobs).read())
for job in jobs['jobs']:
    print(f"Job: {job['name']} ({job['conclusion']})")
    for s in job.get('steps', []):
        print(f"  - {s['name']}: {s.get('conclusion')}")
    
    # Fetch log
    req_log = urllib.request.Request(
        f"https://api.github.com/repos/jeanbroncano77-web/APUESTAS-ANALISIS-/actions/jobs/{job['id']}/logs",
        headers={'Authorization': f'token {token}', 'User-Agent': 'SportsAI'}
    )
    try:
        res = opener.open(req_log)
        content = res.read().decode('utf-8', errors='ignore')
        print("\n--- JOB LOG LAST 2500 CHARACTERS ---")
        print(content[-2500:])
    except Exception as e:
        print(f"Error fetching logs: {e}")
