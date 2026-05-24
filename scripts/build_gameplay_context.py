#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

LOAD_GAME = Path.home() / 'clawd' / 'skills' / 'yumfu' / 'scripts' / 'load_game.py'
STORY_SPINE = Path.home() / 'clawd' / 'skills' / 'yumfu' / 'scripts' / 'story_spine_state.py'
WORLD_DIR = Path.home() / 'clawd' / 'skills' / 'yumfu' / 'worlds'


def run_json(cmd: list[str]) -> dict[str, Any]:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f'command failed ({proc.returncode})')
    return json.loads(proc.stdout)


def load_world(universe: str) -> dict[str, Any]:
    direct = WORLD_DIR / f'{universe}.json'
    nested = WORLD_DIR / universe / 'world.json'
    path = direct if direct.exists() else nested
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return {}


def summarize_recent_flags(flags: dict[str, Any]) -> list[str]:
    lines: list[str] = []
    if not isinstance(flags, dict):
        return lines
    for k, v in flags.items():
        if isinstance(v, bool) and v:
            lines.append(k)
        elif isinstance(v, (str, int, float)) and str(v).strip():
            lines.append(f'{k}: {v}')
        if len(lines) >= 6:
            break
    return lines


def _pick_list(value: Any, limit: int = 5) -> list[Any]:
    if not isinstance(value, list):
        return []
    return value[:limit]


def enrich_world_runtime(world: dict[str, Any]) -> dict[str, Any]:
    return {
        'main_questline': world.get('main_questline') or {},
        'key_figures': _pick_list(world.get('key_figures')),
        'city_and_region_hubs': _pick_list(world.get('city_and_region_hubs')),
        'relationship_webs': _pick_list(world.get('relationship_webs')),
        'major_items_and_artifacts': _pick_list(world.get('major_items_and_artifacts')),
        'mainline_stages': _pick_list(world.get('mainline_stages')),
        'subfaction_networks': _pick_list(world.get('subfaction_networks')),
        'quest_hubs': _pick_list(world.get('quest_hubs')),
        'city_subzones': _pick_list(world.get('city_subzones'), limit=4),
        'story_pressure_tracks': _pick_list(world.get('story_pressure_tracks')),
        'item_threads': _pick_list(world.get('item_threads')),
        'art_style': world.get('art_style'),
        'art_style_key': world.get('art_style_key'),
        'art_direction': world.get('art_direction') or {},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description='Build a normal-turn YumFu gameplay context with hidden story spine guidance')
    parser.add_argument('--user-id', required=True)
    parser.add_argument('--universe', required=True)
    parser.add_argument('--player-input', required=True)
    args = parser.parse_args()

    save_payload = run_json([
        'python3', str(LOAD_GAME), '--user-id', args.user_id, '--universe', args.universe, '--quiet'
    ])
    if not save_payload.get('exists') or not save_payload.get('data'):
        print(json.dumps({'success': False, 'error': 'save not found'}, ensure_ascii=False))
        sys.exit(1)

    spine_payload = run_json([
        'python3', str(STORY_SPINE), '--user-id', args.user_id, '--universe', args.universe
    ])

    save = save_payload['data']
    world = load_world(args.universe)
    spine = (spine_payload or {}).get('story_spine') or {}
    character = save.get('character') or {}
    quests = save.get('quests') or []
    active_quests = [q for q in quests if q.get('status') == 'active'][:3]

    result = {
        'success': True,
        'player': {
            'user_id': args.user_id,
            'name': character.get('name'),
            'role': character.get('role'),
            'house': character.get('house'),
            'level': character.get('level'),
            'location': save.get('location'),
            'inventory': save.get('inventory', [])[:12],
            'active_quests': active_quests,
            'relationship_keys': list((save.get('relationships') or {}).keys())[:10],
            'recent_flags': summarize_recent_flags(save.get('flags') or {}),
            'language': save.get('language') or world.get('default_language') or world.get('language') or 'en',
        },
        'world': {
            'id': world.get('id') or world.get('world_id') or args.universe,
            'name_zh': world.get('name_zh') or world.get('name'),
            'name_en': world.get('name_en') or world.get('name'),
            'genre': world.get('genre'),
            'description_zh': world.get('description_zh') or world.get('description'),
            'description_en': world.get('description_en') or world.get('description'),
            **enrich_world_runtime(world),
        },
        'story_spine': spine,
        'player_input': args.player_input,
        'hidden_turn_checks': {
            'must_answer_internally': [
                'what larger main line is this save currently inside?',
                'what concrete major task or pressure matters right now?',
                'does this turn sharpen, complicate, advance, or threaten that line?',
                'does the player leave this turn with a clear next move?'
            ],
            'must_not_leak': [
                'story spine',
                'default route',
                'active route',
                'pending hooks',
                'quest template',
                'prompt scaffolding',
                'backend checklist labels'
            ],
            'rendering_rule': 'Translate all backend structure into natural in-world scene pressure, NPC intent, consequences, and choices. Never show raw meta labels to the player.'
        },
        'agent_instruction': (
            'Use this context to write the next normal gameplay turn. Keep it in-world. '
            'Respect the current story spine, but never expose the spine/checklist directly. '
            'Use the enriched world structure when helpful: key figures for stronger NPC pressure, relationship webs for conflict framing, quest hubs/city subzones for specific scene placement, story pressure tracks for long tension, and item threads for recurring object-driven stakes. '
            'For image generation, always use the world-specific art style and art direction from this payload instead of falling back to a generic fantasy look. '
            'Normal gameplay turns should default to exactly one primary scene image before narration whenever image generation is available. '
            'If the player action is a detour, connect the detour back to the main line through consequences, pressure, discoveries, obligations, or opportunities. '
            'End with clear natural next moves or choices.'
        )
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
