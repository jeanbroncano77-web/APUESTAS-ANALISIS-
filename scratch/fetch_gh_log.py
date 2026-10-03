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
req = urllib.request.Request(
    'https://api.github.com/repos/jeanbroncano77-web/APUESTAS-ANALISIS-/actions/jobs/111099333874/logs',
    headers={'Authorization': f'token {token}', 'User-Agent': 'SportsAI'}
)
res = opener.open(req)
log_text = res.read().decode('utf-8', errors='ignore')
print(log_text[-2500:])
