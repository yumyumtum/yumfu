#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path.home() / 'clawd' / 'skills' / 'yumfu' / 'scripts'
LOAD = ROOT / 'load_game.py'
RUN = ROOT / 'run_daily_evolution_job.py'
REENTRY = ROOT / 'build_reentry_context.py'


def run_json(cmd: list[str]) -> dict:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f'command failed: {cmd}')
    return json.loads(proc.stdout)


def main():
    parser = argparse.ArgumentParser(description='Batch smoke test YumFu daily evolution outputs')
    parser.add_argument('--user-id', required=True)
    parser.add_argument('--universes', nargs='*', default=None)
    args = parser.parse_args()

    all_worlds = ['journey-to-west', 'xiaoao', 'lotr', 'game-of-thrones', 'harry-potter', 'warrior-cats', 'sengoku', 'yitian']
    universes = args.universes or all_worlds
    report = []

    for universe in universes:
        entry = {'universe': universe, 'save_exists': False, 'ok': False}
        try:
            save = run_json(['python3', str(LOAD), '--user-id', args.user_id, '--universe', universe, '--quiet'])
            if not save.get('exists') or not save.get('data'):
                entry['error'] = 'save_missing'
                report.append(entry)
                continue

            entry['save_exists'] = True
            evo = run_json(['python3', str(RUN), '--user-id', args.user_id, '--universe', universe])
            result = evo.get('result') or {}
            reentry = run_json(['python3', str(REENTRY), '--user-id', args.user_id, '--universe', universe])

            entry.update({
                'summary': result.get('summary'),
                'recap_text': result.get('recap_text'),
                'suggested_routes': result.get('suggested_routes'),
                'default_route': result.get('default_route'),
                'advancement_level': result.get('advancement_level'),
                'reentry_language': reentry.get('preferred_language'),
                'reentry_has_active_route': bool((reentry.get('active_route') or {}).get('label')),
            })

            problems = []
            if not result.get('summary'):
                problems.append('missing_summary')
            if not result.get('recap_text'):
                problems.append('missing_recap_text')
            if not isinstance(result.get('suggested_routes'), list) or not result.get('suggested_routes'):
                problems.append('missing_suggested_routes')
            if not isinstance(result.get('default_route'), dict) or not result.get('default_route'):
                problems.append('missing_default_route')
            if result.get('advancement_level') not in {'normal', 'major'}:
                problems.append('bad_advancement_level')

            entry['problems'] = problems
            entry['ok'] = not problems
        except Exception as e:
            entry['error'] = str(e)
        report.append(entry)

    ok = all(item.get('ok') or item.get('error') == 'save_missing' for item in report)
    print(json.dumps({'success': ok, 'report': report}, ensure_ascii=False, indent=2))
    if not ok:
        sys.exit(1)


if __name__ == '__main__':
    main()
