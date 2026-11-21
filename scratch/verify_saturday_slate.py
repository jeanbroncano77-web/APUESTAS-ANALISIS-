import json
from pathlib import Path

def main():
    # Verify audit_history
    with open('sports_agents/audit_history.json', 'r', encoding='utf-8') as f:
        ah = json.load(f)
    gs = ah['global_stats']
    assert gs['total'] == 252, f"Wrong total: {gs['total']}"
    assert gs['wins'] == 220, f"Wrong wins: {gs['wins']}"
    assert gs['losses'] == 32, f"Wrong losses: {gs['losses']}"
    assert gs['win_rate'] == 87.3, f"Wrong win rate: {gs['win_rate']}"
    assert ah['current_bankroll'] == 3437.52, f"Wrong bankroll: {ah['current_bankroll']}"

    # Verify feedback log
    with open('sports_agents/autonomous_feedback_log.json', 'r', encoding='utf-8') as f:
        fb = json.load(f)
    assert any(c.get('cycle') == 139 for c in fb['calibrations']), 'Cycle 139 missing in calibrations'

    # Verify simulations
    with open('sports_agents/simulations_tomorrow_results.json', 'r', encoding='utf-8') as f:
        st = json.load(f)
    assert st['TargetDate'] == '21/11/2026', f"Wrong target date: {st['TargetDate']}"
    assert len(st['Matches']) == 6, f"Expected 6 matches, got {len(st['Matches'])}"

    # Check HTML files
    for p in ['index.html', 'dashboard_pronosticos.html', '../index.html', '../dashboard_pronosticos.html']:
        txt = Path(p).read_text(encoding='utf-8')
        assert '87.3%' in txt, f"87.3% not in {p}"
        assert '$3,437.52' in txt or '3437.52' in txt, f"3437.52 not in {p}"
        assert 'Atlético Mineiro' in txt, f"Mineiro missing in {p}"
        assert 'Boca Juniors' in txt, f"Boca missing in {p}"
        assert 'match-5' in txt, f"match-5 missing in {p}"
        assert '139' in txt, f"Ciclo 139 not in {p}"

    print("ALL VERIFICATIONS PASSED 100% PERFECTLY!")

if __name__ == '__main__':
    main()
