#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path

WORLD_PATH = Path.home() / 'clawd' / 'skills' / 'yumfu' / 'worlds' / 'sengoku.json'
LOAD_GAME = Path.home() / 'clawd' / 'skills' / 'yumfu' / 'scripts' / 'load_game.py'


def load_world():
    return json.loads(WORLD_PATH.read_text(encoding='utf-8'))


def main():
    parser = argparse.ArgumentParser(description='Render the first playable opening scene for Sengoku Chaos')
    parser.add_argument('--user-id', required=True)
    args = parser.parse_args()

    proc = subprocess.run([
        'python3', str(LOAD_GAME), '--user-id', args.user_id, '--universe', 'sengoku', '--quiet'
    ], capture_output=True, text=True)
    if proc.returncode != 0:
        print(proc.stderr.strip() or proc.stdout.strip(), file=sys.stderr)
        sys.exit(proc.returncode)

    payload = json.loads(proc.stdout)
    save = payload.get('data') or {}
    world = load_world()
    character = save.get('character', {})
    quest = (save.get('quests') or [{}])[0]
    intel = quest.get('intel', {})
    role = character.get('role', '乱世之人')
    faction = character.get('house', '无主之势')
    name = character.get('name', '无名之辈')
    scenario = save.get('location', '乱世开局')
    hook = intel.get('scenario_hook', '今夜有事要发生。')

    npc_sets = {
        '京都夜火': ['戴斗笠的密探', '被火光照红脸的町奉行手下', '知道密信去向的花街女使'],
        '安土酒宴': ['笑得最慢的宿将', '给主人斟酒却不抬眼的侍女', '袖中藏信的年轻使番'],
        '大坂粮乱': ['掌仓老吏', '抢米的足轻', '借机抬价的商人'],
        '堺港火枪交易': ['南蛮火枪商', '压价的大名使者', '假装路过的忍者耳目'],
        '甲斐骑阵点兵': ['老骑将', '想夺你位置的同僚', '沉默记名的军法官'],
        '对马海书': ['持海书的译官', '不肯报真名的海商', '盯着码头不说话的朝鲜来客']
    }
    npcs = npc_sets.get(scenario, ['沉默的看客', '藏刀的使者', '比你更先听到风声的人'])

    role_openers = {
        '足轻头': '你不是席上最尊贵的人，却可能是今夜第一个见血、也第一个立功的人。',
        '浪人头目': '你没正经俸禄，只有刀、脸和一群半饥半忠的手下。谁出得起价，你就替谁把局面切开。',
        '忍者头领': '别人看见的是火和酒，你看见的是谁在借火遮脸、借酒藏话。',
        '火器技师': '别人争的是面子，你争的是谁手里有枪、谁手里有药、谁会在第一响之前先死。',
        '花魁/名妓势力主': '别人以为你卖的是笑和眼波，只有你知道，真正值钱的是谁在你面前卸下戒心。',
        '南蛮异乡客': '别人看你像外人，可乱世里最不被本地规矩绑住的，往往最先闻到钱味和血味。'
    }

    text = (
        f"{hook}\n\n"
        f"你叫{name}，身份是【{role}】，目前站在【{faction}】这一边。"
        f"{role_openers.get(role, '你已经站进了这盘会吃人的局。')}\n\n"
        f"今夜真正值得你盯的人有三个：\n"
        + "\n".join(f"- {n}" for n in npcs) +
        f"\n\n这不是介绍世界观的时候，而是你得立刻决定第一步的时候。"
    )

    choices = [
        f"先接近：{npcs[0]}",
        f"先盯住：{npcs[1]}",
        f"先试探：{npcs[2]}",
        '按你自己的路子先开口或先动手'
    ]

    print(json.dumps({
        'success': True,
        'text': text,
        'npcs': npcs,
        'choices': choices,
        'image_prompt': f"Sengoku Chaos first playable scene, {scenario}, {hook}, protagonist {name}, role {role}, faction {faction}, three dangerous figures in one room, cinematic samurai war painting, torchlight, intrigue, lacquer armor, smoke and tension"
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
