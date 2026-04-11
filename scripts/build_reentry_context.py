#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path

LOAD_GAME = Path.home() / 'clawd' / 'skills' / 'yumfu' / 'scripts' / 'load_game.py'
LOAD_EVOLUTION = Path.home() / 'clawd' / 'skills' / 'yumfu' / 'scripts' / 'load_daily_evolution.py'


def main():
    parser = argparse.ArgumentParser(description='Build a concise YumFu re-entry context from save + daily evolution sidecar')
    parser.add_argument('--user-id', required=True)
    parser.add_argument('--universe', required=True)
    args = parser.parse_args()

    save_proc = subprocess.run([
        'python3', str(LOAD_GAME), '--user-id', args.user_id, '--universe', args.universe, '--quiet'
    ], capture_output=True, text=True)
    if save_proc.returncode != 0:
        print(save_proc.stderr.strip() or save_proc.stdout.strip(), file=sys.stderr)
        sys.exit(save_proc.returncode)

    save_payload = json.loads(save_proc.stdout)
    evo_proc = subprocess.run([
        'python3', str(LOAD_EVOLUTION), '--user-id', args.user_id, '--universe', args.universe
    ], capture_output=True, text=True)
    evo_payload = json.loads(evo_proc.stdout) if evo_proc.returncode == 0 and evo_proc.stdout.strip() else {'exists': False, 'data': None}

    save = save_payload.get('data') or {}
    evo = evo_payload.get('data') or {}
    hooks = evo.get('pending_hooks', [])[:3]

    result = {
        'success': True,
        'character_name': (save.get('character') or {}).get('name'),
        'location': save.get('location'),
        'active_quest': ((save.get('quests') or [{}])[0]).get('name'),
        'last_daily_summary': evo.get('last_summary'),
        'pending_hooks': hooks,
        'reentry_instruction': (
            'When the player returns, briefly pull them back into the scene using the latest daily evolution summary, '
            'then offer one easy natural next move. Do not dump lore or system bulletins.'
        )
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
