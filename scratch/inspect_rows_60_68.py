# -*- coding: utf-8 -*-
import os
import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

for i in range(60, 69):
    pat = rf'<tr class="audit-row[^"]*"[^>]*>[\s\S]*?<td class="col-id">#{i}</td>([\s\S]*?)</tr>'
    m = re.search(pat, html)
    if m:
        content = m.group(1)
        name = re.search(r'<div class="match-name">(.*?)</div>', content)
        sel = re.search(r'<div class="sel-text">(.*?)</div>', content)
        odds = re.search(r'<td class="col-odds">(.*?)</td>', content)
        conf = re.search(r'<td class="col-conf">(.*?)</td>', content)
        status = re.search(r'<span class="badge-status[^"]*">(.*?)</span>', content)
        pnl = re.search(r'<td class="col-pnl[^"]*">(.*?)</td>', content)
        print(f"#{i}: {name.group(1) if name else '?'} | {sel.group(1) if sel else '?'} | {odds.group(1) if odds else '?'} | {conf.group(1) if conf else '?'} | {status.group(1) if status else '?'} | {pnl.group(1) if pnl else '?'}")
    else:
        print(f"#{i}: NOT FOUND")
