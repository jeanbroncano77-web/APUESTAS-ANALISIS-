import json

with open('sports_agents/audit_history.json', 'r', encoding='utf-8') as f:
    audit = json.load(f)

history = audit.get('history', [])
print("Total history items:", len(history))

bankroll = 1000.0
points = [bankroll]
wins = 0
losses = 0
fija_wins = 0
fija_losses = 0

for h in history:
    pnl = h.get('pnl', 0.0)
    status = h.get('status', 'win')
    bankroll += pnl
    points.append(round(bankroll, 2))
    if status == 'win':
        wins += 1
        if h.get('is_fija'): fija_wins += 1
    else:
        losses += 1
        if h.get('is_fija'): fija_losses += 1

print(f"Computed Final Bankroll: {bankroll:.2f}")
print(f"Wins: {wins}, Losses: {losses}, Total: {len(history)}, Win Rate: {wins/len(history)*100:.1f}%")
print(f"Fija Wins: {fija_wins}, Fija Losses: {fija_losses}, Fija Win Rate: {fija_wins/(fija_wins+fija_losses)*100:.1f}%")
print("Last 15 points:", points[-15:])

