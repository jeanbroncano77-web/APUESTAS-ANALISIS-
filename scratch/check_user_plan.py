import sqlite3
import base64
import re

db_path = r"C:\Users\jeanb\AppData\Roaming\Antigravity IDE\User\globalStorage\state.vscdb"
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT value FROM ItemTable WHERE key = 'antigravityUnifiedStateSync.userStatus'")
val = c.fetchone()[0]
raw = base64.b64decode(val)

strings = re.findall(b"[\x20-\x7e]{4,}", raw)
for s in strings:
    t = s.decode("latin1")
    print(t)
