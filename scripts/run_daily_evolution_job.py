#!/usr/bin/env python3
import argparse
import json
import hashlib
from datetime import datetime
from pathlib import Path

WORLD_DIR = Path.home() / 'clawd' / 'skills' / 'yumfu' / 'worlds'
SAVE_DIR = Path.home() / 'clawd' / 'memory' / 'yumfu' / 'saves'
EVOLUTION_DIR = Path.home() / 'clawd' / 'memory' / 'yumfu' / 'evolution'


def load_json(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_world(universe: str):
    direct = WORLD_DIR / f'{universe}.json'
    nested = WORLD_DIR / universe / 'world.json'
    path = direct if direct.exists() else nested
    if not path.exists():
        raise FileNotFoundError(f'World config not found for {universe}')
    return load_json(path), path


def load_save(user_id: str, universe: str):
    path = SAVE_DIR / universe / f'user-{user_id}.json'
    if not path.exists():
        raise FileNotFoundError(f'Save not found: {path}')
    return load_json(path), path


def load_sidecar(user_id: str, universe: str):
    path = EVOLUTION_DIR / universe / f'user-{user_id}.json'
    if not path.exists():
        return {}, path
    try:
        return load_json(path), path
    except Exception:
        return {}, path


def pick_severity(key: str) -> str:
    n = int(hashlib.sha256(key.encode()).hexdigest(), 16) % 10
    if n == 0:
        return 'major'
    if n <= 3:
        return 'medium'
    return 'minor'


def clean_name(text: str | None, fallback: str) -> str:
    if not text:
        return fallback
    return str(text).strip()


def normalize_lang(value: str | None) -> str | None:
    if not value:
        return None
    v = str(value).strip().lower()
    if v in {'zh', 'zh-cn', 'zh-hans', 'zh-tw', 'zh-hant', 'cn', 'chinese', '中文'}:
        return 'zh'
    if v in {'en', 'en-us', 'en-gb', 'english'}:
        return 'en'
    return None


def build_route_payload(lang: str, hooks: list[str], meta: dict, location: str, fallback_target: str) -> tuple[list[dict], dict]:
    rumor_threads = meta.get('rumor_threads') or []
    npc_watchlist = meta.get('npc_watchlist') or []
    faction_movements = meta.get('faction_movements') or []
    item_threads = meta.get('item_threads') or []

    target_a = npc_watchlist[0] if npc_watchlist else fallback_target
    target_b = item_threads[0] if item_threads else (rumor_threads[0] if rumor_threads else fallback_target)
    pressure = faction_movements[0] if faction_movements else (rumor_threads[0] if rumor_threads else '')

    if lang == 'zh':
        routes = [
            {
                'label': '追当前最热的线',
                'why_now': pressure or '局势刚变，最早的痕迹还没冷掉',
                'target': target_a or location,
                'urgency': 'high',
            },
            {
                'label': '先摸实物/证据',
                'why_now': '先抓住能落到手里的东西，比继续听风声更稳',
                'target': target_b or fallback_target or location,
                'urgency': 'medium',
            },
        ]
        default_route = {
            'label': '默认沿主线继续试探',
            'why_now': '就算玩家暂时不选，这也是最自然、最不容易断档的推进方式',
            'target': target_a or fallback_target or location,
        }
    else:
        routes = [
            {
                'label': 'Pick up the hottest live thread',
                'why_now': pressure or 'the freshest traces are still available now',
                'target': target_a or location,
                'urgency': 'high',
            },
            {
                'label': 'Grab the concrete evidence first',
                'why_now': 'a tangible lead is easier to re-enter than more rumor alone',
                'target': target_b or fallback_target or location,
                'urgency': 'medium',
            },
        ]
        default_route = {
            'label': 'Default to the main pressure line',
            'why_now': 'if the player does nothing, this is the easiest natural continuation instead of a cold restart',
            'target': target_a or fallback_target or location,
        }

    return routes, default_route


def got_update(save: dict, world: dict, sidecar: dict) -> dict:
    character = save.get('character', {})
    name = clean_name(character.get('name'), 'the Dornish knight')
    location = clean_name(save.get('location'), 'the southern road')
    relationships = save.get('relationships', {})
    quest = (save.get('quests') or [{}])[0]
    intel = quest.get('intel', {})
    history = sidecar.get('history', [])
    severity = pick_severity(f"game-of-thrones:{name}:{location}:{len(history)}:{datetime.now().date().isoformat()}")

    first_destination = intel.get('first_destination', 'Planky Town')
    house = clean_name(character.get('house'), 'Martell')
    prince_name = 'Prince Doran'
    trust = relationships.get(prince_name, 0)
    lang = normalize_lang(save.get('language')) or 'en'

    if lang == 'zh':
        seeds = [
            {
                'summary': '码头上的红蜡信又动了一次。',
                'story_text': f"天色刚薄下来，关于{first_destination}的风声已经先一步传到你耳里：一条平底船明明没有公开卸出什么像样货物，岸边却有三个人为了那封深红封蜡的短讯争得过分厉害。缆绳吃水太深，不像只装盐货；而一旦有人瞥见马泰尔的颜色，码头工的声音就立刻低了下去。真正被人护着的，也许不是货，而是那封决定货该往哪走的信。若多兰亲王要你查的暗线确实埋在南岸，这里就是它第一次露出木头、绳索和证人的地方。你现在赶过去，还来得及在账本开封前抓到最早一手。你先盯信，先盯货，还是先盯拿信的人？",
                'hooks': [
                    '先盯那封红蜡信下一次换手。',
                    '先看货物在开账前会被挪去哪里。'
                ],
                'meta': {
                    'rumor_threads': ['码头红蜡信再度出现'],
                    'faction_movements': ['码头搬运线在高压下运作'],
                    'npc_watchlist': ['接信的人', '用假账的船主']
                },
                'image_prompt': 'Pre-dawn Planky Town docks in Dorne, flat-bottomed boat, suspicious dockhands arguing over a deep-red sealed note, covert supply-line tension, Game of Thrones dark fantasy oil painting style'
            },
            {
                'summary': '信使没到，但盯梢的人先到了。',
                'story_text': f"天还没彻底亮，{first_destination}的商贩之间已经开始低声谈论一个没到场的信使；可更要命的是，在同一批货登记之前，已有两拨生面孔先后在码头边打听它。多兰亲王提醒过你的那类事，往往不是看见了谁，而是谁明明该出现却没有出现。这条线没断，只是被人悄悄掰弯了。时机不对，面孔不对，大家对这个空缺的沉默更不对。若你现在下场，也许能在对方反应过来前，看清到底是谁在盯这条线。你是先混进人群里摸过去，还是先按住不动，等其中一个人自己露破绽？",
                'hooks': [
                    '先混进晨市里，把盯梢的人认出来。',
                    '先等第一个离开码头的人露出去向。'
                ],
                'meta': {
                    'rumor_threads': ['南线失踪信使'],
                    'faction_movements': ['货还没记账，观察者先到了'],
                    'npc_watchlist': ['码头盯梢人', '失踪信使']
                },
                'image_prompt': 'Morning crowd gathering at Planky Town docks, absent courier, two covert watchers scanning the shipment line, Dorne intrigue, Game of Thrones oil painting style'
            },
            {
                'summary': '补给线还在走，但谨慎得不对劲。',
                'story_text': f"南边那条线并没有停，这才是最危险的地方。天刚亮，车还是往{first_destination}去，船夫还是在骂，记账的人还是在湿木板上划着数字，可所有动作都带着一种不该有的谨慎。原本该急的人忽然不急了，原本该吵的人忽然安静了，甚至一小片干血色的红蜡痕都比早市更早出现在了码头木板上。这说明线已经被碰过，却还没被公开掐断。有人想让多兰的货继续走，只走到没人来得及惊慌、刀子却已经伸进去的位置。你若现在插手，面对的不是一条正常流动的货线，而是一条等着看谁先露头的暗流。你先试账本，先试搬运的人，还是先试那条船？",
                'hooks': [
                    '先查账本在墨迹未干前改过哪里。',
                    '先盯那个小心得过头的搬运人。'
                ],
                'meta': {
                    'rumor_threads': ['货线继续运行但账目受压'],
                    'faction_movements': ['补给路线在暗中受控'],
                    'npc_watchlist': ['账房', '过分谨慎的搬运人', '船主']
                },
                'image_prompt': 'Early morning Dorne supply wagons and dock ledgers at Planky Town, tense cautious workers, red wax fragment on wooden boards, covert sabotage mood, Game of Thrones oil painting style'
            }
        ]
    else:
        seeds = [
            {
                'summary': 'A red-sealed message has moved again at the docks.',
                'story_text': f"By the time dawn thins over the coast road, word reaches you that a flat-bottomed boat at {first_destination} unloaded nothing in public, yet three men argued over a deep-red sealed note beside the pier. The cargo ropes bit too deep for salt alone, and the dockhands went quiet the moment Martell colors came into view. Someone is moving goods under a false manifest, and someone else is more interested in the message than the cargo itself. If Doran’s hidden line truly runs through the southern coast, then this is not random dockside noise — it is the first place where the lie has touched wood, rope, and witnesses. You are close enough now to arrive before the morning ledgers settle. Do you shadow the note, the cargo, or the men holding it?",
                'hooks': [
                    'Follow the red-sealed note before it changes hands again.',
                    'Watch the cargo before anyone opens the books for the day.'
                ],
                'meta': {
                    'rumor_threads': ['red-sealed note at the docks'],
                    'faction_movements': ['dockside handlers behaving under pressure'],
                    'npc_watchlist': ['unknown note recipient', 'boat captain with false manifest']
                },
                'image_prompt': 'Pre-dawn Planky Town docks in Dorne, flat-bottomed boat, suspicious dockhands arguing over a deep-red sealed note, covert supply-line tension, Game of Thrones dark fantasy oil painting style'
            },
            {
                'summary': 'A courier failed to arrive, but the watchers did.',
                'story_text': f"Before full sunrise, a small knot of traders in {first_destination} begins whispering about a courier who never arrived, though two separate watchers appeared at the pier asking after the same shipment. That is the kind of absence Doran warned you about: the visible messenger matters less than the unseen hand expecting him. The route is still alive, which means whoever touched it did not shut it down — they bent it. The timing is wrong, the faces are wrong, and the silence around the missing courier is wrongest of all. If you move now, you may catch the people watching the line before they realize the line is watching them back. Do you press into the crowd as another traveler, or hold off until one of them breaks pattern?",
                'hooks': [
                    'Blend into the morning crowd and identify who came to watch the missing courier.',
                    'Wait for the first watcher to peel away from the pier.'
                ],
                'meta': {
                    'rumor_threads': ['missing courier on southern line'],
                    'faction_movements': ['unknown observers appear before cargo is logged'],
                    'npc_watchlist': ['silent watcher at the pier', 'missing courier']
                },
                'image_prompt': 'Morning crowd gathering at Planky Town docks, absent courier, two covert watchers scanning the shipment line, Dorne intrigue, Game of Thrones oil painting style'
            },
            {
                'summary': 'The supply line still moves, but under the wrong kind of caution.',
                'story_text': f"The southern line has not stopped. That is what makes it dangerous. By first light, the wagons still roll toward {first_destination}, the boatmen still curse, and the tally-men still scratch marks into wet ledgers — but everything carries the wrong kind of caution. Men who should be impatient are careful. Men who should be loud are quiet. And a wax fragment the color of dried blood has already reached the dockside boards ahead of the morning trade. That means the line is compromised, but not openly broken. Someone wants Doran’s supplies to keep moving just enough that nobody panics until the knife is already in too deep. If you step in now, you step into a flow that expects not a rider in Martell colors, but a fool who never learned to read silence. Which current do you test first: the manifests, the handlers, or the boat itself?",
                'hooks': [
                    'Check the manifests before the ink dries.',
                    'Watch which handler acts too carefully for an honest morning.'
                ],
                'meta': {
                    'rumor_threads': ['moving line, compromised books'],
                    'faction_movements': ['supply route operating under covert pressure'],
                    'npc_watchlist': ['ledger keeper', 'overcareful handler', 'boatmaster']
                },
                'image_prompt': 'Early morning Dorne supply wagons and dock ledgers at Planky Town, tense cautious workers, red wax fragment on wooden boards, covert sabotage mood, Game of Thrones oil painting style'
            }
        ]

    idx = int(hashlib.md5(f"{name}:{location}:{len(history)}:{trust}:{house}".encode()).hexdigest(), 16) % len(seeds)
    chosen = seeds[idx]
    chosen['severity'] = severity
    chosen['world_id'] = world.get('id', 'game-of-thrones')
    chosen['character_name'] = name
    chosen['location_context'] = location
    chosen['recap_text'] = build_recap(save, world, sidecar)
    chosen['image_prompt'] = chosen['image_prompt'] + ', visual continuity from the player\'s existing Doran/Martell covert route investigation, same ongoing arc, not a disconnected new scene'
    routes, default_route = build_route_payload(lang, chosen.get('hooks', []), chosen.get('meta', {}), location, first_destination)
    chosen['suggested_routes'] = routes
    chosen['default_route'] = default_route
    chosen['meta'].setdefault('world_detail_notes', [
        f'当前关键地点：{first_destination}' if lang == 'zh' else f'Current key place: {first_destination}',
        f'当前关键势力：{house}' if lang == 'zh' else f'Current key faction: {house}',
    ])
    chosen['meta'].setdefault('item_threads', ['红蜡信', '假账货单'] if lang == 'zh' else ['red-sealed note', 'false manifest'])
    return chosen


def lotr_update(save: dict, world: dict, sidecar: dict) -> dict:
    character = save.get('character', {})
    name = clean_name(character.get('name'), 'the wanderer')
    location = clean_name(save.get('location'), 'the wild road')
    role = clean_name(character.get('role'), 'traveler')
    house = clean_name(character.get('house'), 'the Shadow')
    inventory = save.get('inventory', []) or []
    quest = (save.get('quests') or [{}])[0]
    history = sidecar.get('history', [])
    severity = pick_severity(f"lotr:{name}:{location}:{role}:{len(history)}:{datetime.now().date().isoformat()}")

    notable_items = [item.get('name') for item in inventory[:4] if item.get('name')]
    item_a = notable_items[0] if notable_items else 'the broken stone under your boots'
    item_b = notable_items[1] if len(notable_items) > 1 else 'the sign that someone already tested this ground before you'
    quest_name = clean_name(quest.get('name'), 'the current line')

    seeds = [
        {
            'summary': 'The stone remembers the struggle, and someone else has begun reading it too.',
            'story_text': f"The pressure around {location} has changed from brute force to reading signs. What was broken in the last clash has not simply lain there: blood on iron, cracked white stone, and splintered staff-work have already started to sort the field into clues. Someone nearby now understands that this place is not merely a kill ground, but a hinge point in {quest_name}. A scavenger, watcher, or hidden servant has begun gathering what should have remained scattered. In Middle-earth, that matters. Whoever gathers the fragments first does not just learn what happened — they decide what story the next force believes. If you step back in now, you are not returning to a frozen battlefield. You are returning to a contested memory. Do you seize the fragments, follow the collector, or set a second trap and wait to see who comes for them?",
            'hooks': [
                'Gather the surviving fragments before another hand carries them off.',
                'Track whoever has started reading the battlefield for meaning.'
            ],
            'meta': {
                'rumor_threads': ['the battleground is already being quietly searched'],
                'faction_movements': ['a second layer of control is forming around the broken stair edge'],
                'npc_watchlist': ['the unseen collector', 'whoever responds to missing fragments'],
                'item_threads': [item_a, item_b],
            },
            'image_prompt': 'Broken white stair edge in Middle-earth, scattered war relics, black iron and pale shattered stone, unseen scavenger presence, tension after Gandalf clash, epic Tolkien oil painting style'
        },
        {
            'summary': 'The ring of pressure is no longer only steel; command itself is shifting.',
            'story_text': f"While you were away, the danger near {location} became more organized. What had been a vicious crush is beginning to harden into a command question: who owns the ground, who controls the next signal, and who gets to turn this wound in the stone into future authority? That matters more than one more corpse. In a place like this, fear is useful only until someone learns how to arrange it. Your rivals, allies, and watchers all understand that if {house} can turn this edge into a real base rather than a moment of blood, the whole line south changes. But that also means everyone with ambition now has reason to test your grip. Do you lock down the gate-keys and signal points, question the captains who grew quieter, or move first toward the next approach before another will claims the initiative?",
            'hooks': [
                'Lock down the signal points before command slips sideways.',
                'Question the suddenly disciplined captains before they regroup in private.'
            ],
            'meta': {
                'rumor_threads': ['the stone victory is turning into a command struggle'],
                'faction_movements': ['control of signals and gate authority is being quietly contested'],
                'npc_watchlist': ['the captain who grows too careful', 'the hand seeking the keys'],
                'item_threads': ['Signal Horn', item_a],
            },
            'image_prompt': 'Orc-held fortress edge in Middle-earth, signal horn, gate chains, captains under torchlight, command tension after siege victory, dark epic fantasy oil painting'
        },
        {
            'summary': 'A usable road is opening, but only if you read the burden correctly.',
            'story_text': f"Something important has changed in the road beyond {location}: what looked like a trapped edge is starting to become a route. That is dangerous in a different way. Once a battlefield turns into a road, every surviving object matters more — the horn that rallied, the shard that broke under pressure, the blood proof that a greater foe can be cut, the stores that keep a warband moving. In Middle-earth, roads do not merely connect places; they connect burdens. And right now, the burden around you is deciding whether this line becomes terror, logistics, or invitation. If you move too slowly, others will define the road for you. If you move too quickly, you may march your strength onto ground that has already been measured by unseen eyes. Do you scout the next road, fortify the current hold, or turn one captured proof into a threat the next enemy cannot ignore?",
            'hooks': [
                'Scout the next road before watchers turn it against you.',
                'Choose one captured proof and make it the center of the next threat.'
            ],
            'meta': {
                'rumor_threads': ['the battlefield is becoming a route rather than a ruin'],
                'faction_movements': ['the next march line is beginning to take shape'],
                'npc_watchlist': ['the first scout to return', 'the watcher measuring the road'],
                'item_threads': notable_items[:3] or [item_a],
            },
            'image_prompt': 'Harsh Middle-earth war road opening from shattered fortress edge, torches, black standards, relics of battle repurposed for the next march, Tolkien-style oil painting'
        },
    ]

    idx = int(hashlib.md5(f"lotr:{name}:{location}:{role}:{house}:{len(history)}".encode()).hexdigest(), 16) % len(seeds)
    chosen = seeds[idx]
    chosen['severity'] = severity
    chosen['world_id'] = world.get('id', 'lotr')
    chosen['character_name'] = name
    chosen['location_context'] = location
    chosen['recap_text'] = build_recap(save, world, sidecar)
    chosen['image_prompt'] = chosen['image_prompt'] + ' , visual continuity from the player\'s current LOTR campaign arc, not a disconnected new scene'
    routes, default_route = build_route_payload('en', chosen.get('hooks', []), chosen.get('meta', {}), location, quest_name)
    chosen['suggested_routes'] = routes
    chosen['default_route'] = default_route
    chosen['meta'].setdefault('world_detail_notes', [
        f'Current role: {role}',
        f'Current faction: {house}',
        f'Current quest line: {quest_name}',
    ])
    return chosen


def journey_to_west_update(save: dict, world: dict, sidecar: dict) -> dict:
    character = save.get('character', {})
    name = clean_name(character.get('name'), '未定名')
    location = clean_name(save.get('location'), '西行古道')
    quest = (save.get('quests') or [{}])[0]
    quest_name = clean_name(quest.get('name'), '西行第一步')
    flags = save.get('flags', {}) or {}
    history = sidecar.get('history', [])
    severity = pick_severity(f"jtw:{name}:{location}:{quest_name}:{len(history)}:{datetime.now().date().isoformat()}")

    pending_creation = bool(flags.get('character_creation_pending'))

    if pending_creation:
        seeds = [
            {
                'summary': '你还没选身份，可这片天地已经先朝你递来了第一张牌。',
                'story_text': f"{location} 的风这两天变得不一样了。古道上不只是一队行脚僧和驮盐的毛驴来回经过，连本该各守天命的几股势力，也像是在等谁先开口。道旁茶摊有人低声谈起五行山下又有金光浮起，路过的香客却说西梁方向最近夜里常有妖气逆风而上；更怪的是，一个挑担老者明明只是擦肩而过，却把“别急着选边，先看谁最先来试你”这句话留在了你耳边。你还未真正入局，但西游世界已经在试探你更像护经人、成妖者、天庭棋子，还是会把三界都搅浑的那类人。你若现在踏进去，第一步就不是空白，而是立场。",
                'hooks': ['先顺着五行山那道金光去看。', '先查是谁在古道上故意试你的口风。'],
                'meta': {
                    'rumor_threads': ['五行山下又有金光浮起', '西梁方向夜里妖气逆风而上'],
                    'faction_movements': ['各方势力都在等新入局者先表态'],
                    'npc_watchlist': ['挑担老者', '古道茶摊说书人'],
                    'item_threads': ['未曾启封的身份', '第一张立场牌'],
                },
                'image_prompt': 'Classic Journey to the West fairy-tale illustration, bright ancient road west of Tang border, distant golden glow near Five-Finger Mountain, mythic travelers and hidden destiny, no dark realism'
            },
            {
                'summary': '身份未定时，最先靠近你的往往不是朋友，而是机会。',
                'story_text': f"你还没有把自己的名字和身份钉在这条路上，这恰恰让机会先来了。{location} 附近今天多了两种完全不同的气息：一边是带着檀香与经卷味的清净路数，像是佛门护经线在悄悄试探；另一边却是妖风里夹着甜腻果香，像哪处山精已经把你也当成了可拉拢、可利用、也可吞掉的新棋子。西游世界从来不是等人准备好再开门，它只会在你犹豫时，把门一扇扇推到你面前。你若拖得太久，别人就会替你定义第一步。",
                'hooks': ['先接近佛门那条清净线。', '先摸清妖风背后是哪一路山精。'],
                'meta': {
                    'rumor_threads': ['佛门护经线在边界探路', '妖风携果香，像在招新棋子'],
                    'faction_movements': ['佛门与妖线都在边界轻轻试探'],
                    'npc_watchlist': ['边路僧人', '藏在果香后的山精'],
                    'item_threads': ['经卷气息', '果香妖风'],
                },
                'image_prompt': 'Bright classic Journey to the West illustration, Tang border ancient road, one side Buddhist incense scroll glow, another side sweet demon mist from hills, colorful mythic fork in destiny'
            },
        ]
    else:
        seeds = [
            {
                'summary': '路上的妖气不是乱起的，它像是在等某件东西露面。',
                'story_text': f"{location} 这一带的动静已经不再只是普通风声。近两日传出来的怪话都指向同一个意思：有人，或有妖，正在等一件能把{quest_name}往前推的东西露面。可能是一封法旨、一件法宝、一位护经人的名号，也可能只是某个不该出现在这里的脚印。西游里的局，最怕的不是妖怪明着拦路，而是它们先把‘该由谁出手’这件事算清了。若你现在回身接这条线，接到的就不只是下一段路，而是这条路背后谁在布局。",
                'hooks': ['先查最近被反复提到的那件“该露面的东西”。', '先盯最像提前埋伏的人或妖。'],
                'meta': {
                    'rumor_threads': ['有人在等关键物件或名号露面'],
                    'faction_movements': ['拦路一方开始提前布局，不再只是临时起意'],
                    'npc_watchlist': ['提前埋伏的探子', '最先提起关键物件的人'],
                    'item_threads': ['法旨', '法宝', '不该出现的脚印'],
                },
                'image_prompt': 'Classic colorful Journey to the West myth illustration, roadside shrine and demon signs, hidden artifact expectation, bright fairy-tale atmosphere, classic Chinese children\'s myth art'
            },
            {
                'summary': '真正往前推这条路的，也许不是法力，而是谁先看懂因果。',
                'story_text': f"你离开的这段时间，{location} 一带多了些看似不吓人的变化：求签的人忽然变多，路边小庙的香灰也厚得不正常，连讨水喝的行脚人都开始问起同一个方向。这种热闹，在西游里从来不只是热闹。它说明因果线正在往这里聚，说明接下来出现的人、妖、神、怪，未必最强，却一定最有来历。若你只是回来看一眼风景，就会错过谁才是这一难里真正该盯的核心。若你顺着这股因果去摸，下一步就不会只是‘继续赶路’，而是先挑哪一根线开刀。",
                'hooks': ['先查同一个方向为什么被反复问起。', '先摸清这股因果线最先会引来谁。'],
                'meta': {
                    'rumor_threads': ['同一方向被反复问起', '小庙香灰厚得异常'],
                    'faction_movements': ['新的因果线正在把不同势力往这里拉'],
                    'npc_watchlist': ['问路最多的人', '庙里最沉默的看香人'],
                    'item_threads': ['签筒', '香灰', '问路方向'],
                },
                'image_prompt': 'Journey to the West classic fairy-tale illustration, roadside shrine with thick incense ash, pilgrims and hidden immortals, colorful mythic causality gathering around a travel path'
            },
        ]

    idx = int(hashlib.md5(f"jtw:{name}:{location}:{quest_name}:{len(history)}:{pending_creation}".encode()).hexdigest(), 16) % len(seeds)
    chosen = seeds[idx]
    chosen['severity'] = severity
    chosen['world_id'] = world.get('id', 'journey-to-west')
    chosen['character_name'] = name
    chosen['location_context'] = location
    chosen['recap_text'] = build_recap(save, world, sidecar)
    chosen['image_prompt'] = chosen['image_prompt'] + ' , visual continuity from the player\'s current Journey to the West arc, not a disconnected standalone tableau'
    routes, default_route = build_route_payload('zh', chosen.get('hooks', []), chosen.get('meta', {}), location, quest_name)
    chosen['suggested_routes'] = routes
    chosen['default_route'] = default_route
    chosen['meta'].setdefault('world_detail_notes', [
        f'当前地点：{location}',
        f'当前主线：{quest_name}',
        '当前世界会先通过立场、因果与来历来定义危险，而不只是战力',
    ])
    return chosen


def sengoku_update(save: dict, world: dict, sidecar: dict) -> dict:
    character = save.get('character', {})
    name = clean_name(character.get('name'), '无名之辈')
    location = clean_name(save.get('location'), '城下町')
    role = clean_name(character.get('role'), '乱世之人')
    faction = clean_name(character.get('house'), '无主之势')
    history = sidecar.get('history', [])
    severity = pick_severity(f"sengoku:{name}:{location}:{role}:{len(history)}:{datetime.now().date().isoformat()}")

    seeds = [
        {
            'summary': '城里先传开的不是命令，而是风声。',
            'story_text': f"夜还没彻底退，{location}里先传开的不是官样命令，而是一阵更值钱的风声：昨夜有人悄悄问价，要买下一批新到港的火绳枪，却不肯留下主家名号。茶屋、仓场、花街和码头之间都有人在压着声量打听，像谁都知道要出事，却都想比别人晚一步露面。你现在的身份是{role}，站在{faction}这一边，可乱世里真正保命的从来不是名头，而是谁先抓住这阵风往哪边吹。只要你今晚抢先找到第一个放风的人，你就不只是听消息的人，而是能决定谁先拿到枪、谁先丢掉脑袋的人。你是先查火枪的去向，还是先查是谁故意放出这阵风？",
            'hooks': ['先追火枪去向。', '先查放风的人。'],
            'meta': {
                'rumor_threads': ['火绳枪暗中问价'],
                'faction_movements': ['多方势力同时试探军火流向'],
                'npc_watchlist': ['放风的茶屋耳目', '匿名军火买主']
            },
            'image_prompt': 'Torchlit Sengoku castle town before dawn, whispers spreading through tea houses and alleys, hidden gun deal rumors, banners, ash, lacquer armor, Japanese ukiyo-e woodblock print style, bold ink outlines, textured washi paper, flat layered colors'
        },
        {
            'summary': '花街里先有人开口，城门外才会死人。',
            'story_text': f"今夜{location}最先热起来的不是城门，而是花街。有人带着比银子更重的口风进了包间，说某位将领已经在私下募人，不是为了守城，是为了在下一场会盟之前先把不该活的人做掉。真正可怕的不是这句风声本身，而是说这句话的人明显不怕被听见——这说明放话的人不是傻，就是背后有人兜着。你这种{role}若只把它当闲话，就会错过把手伸进真正权力缝里的机会。若你先找对人，今夜你能收的就不只是消息，还可能是一条债、一把刀、或一个将来要为你卖命的人。你是先盯那个最会传话的女人，还是先查她背后的金主？",
            'hooks': ['先盯最会传话的人。', '先查出谁在背后付钱。'],
            'meta': {
                'rumor_threads': ['花街放出暗杀风声'],
                'faction_movements': ['有人在会盟前秘密募人'],
                'npc_watchlist': ['最会传话的花街女人', '出钱的幕后金主']
            },
            'image_prompt': 'Sengoku pleasure quarter at night, ambitious courtesan whispering fatal secrets behind lantern screens, armed retainers outside, Japanese ukiyo-e woodblock print style, bold ink outlines, textured washi paper, elegant but dangerous composition'
        },
        {
            'summary': '粮、枪和人情，今夜至少有一样要先断。',
            'story_text': f"{location}今夜的表面还算平静，可真正懂行的人都看得出来：粮、枪和人情三样东西里，至少有一样很快要先断。仓里的人突然开始惜米，带枪的人开始惜火药，原本逢人都点头的中间商也突然话少了一半。这种静不是平安，是有人已经提前闻到了血。你现在身在{faction}，又顶着{role}的身份，如果还等别人把局势讲明白，往往就只能替别人收残局。可若你趁现在先拿住一个关节，不管是仓、枪、还是人脉，等明天城里真正乱起来时，你就不是被卷进去的人，而是能收价的人。你先掐哪一处？",
            'hooks': ['先控制粮。', '先控制枪。', '先控制中间人。'],
            'meta': {
                'rumor_threads': ['仓、枪、人情同时收紧'],
                'faction_movements': ['多方为即将到来的乱局做准备'],
                'npc_watchlist': ['惜米的仓吏', '惜火药的枪头', '突然沉默的中间商']
            },
            'image_prompt': 'Sengoku storehouses and gun racks under lantern light, tense merchants and ashigaru sensing coming bloodshed, Japanese ukiyo-e woodblock print style, bold ink outlines, textured washi paper, smoke and red-black-indigo-gold palette'
        }
    ]

    idx = int(hashlib.md5(f"{name}:{location}:{role}:{faction}:{len(history)}".encode()).hexdigest(), 16) % len(seeds)
    chosen = seeds[idx]
    chosen['severity'] = severity
    chosen['world_id'] = world.get('id', 'sengoku')
    chosen['character_name'] = name
    chosen['location_context'] = location
    chosen['recap_text'] = build_recap(save, world, sidecar)
    chosen['image_prompt'] = chosen['image_prompt'] + ' , visual continuity from the player\'s current Sengoku campaign arc, not a cold standalone vignette'
    routes, default_route = build_route_payload('zh', chosen.get('hooks', []), chosen.get('meta', {}), location, faction)
    chosen['suggested_routes'] = routes
    chosen['default_route'] = default_route
    chosen['meta'].setdefault('world_detail_notes', [
        f'当前关键身份：{role}',
        f'当前关键势力：{faction}',
    ])
    chosen['meta'].setdefault('item_threads', ['火绳枪', '账册', '买主名单'])
    return chosen


def build_recap(save: dict, world: dict, sidecar: dict) -> str:
    character = save.get('character', {}) or {}
    quests = save.get('quests') or []
    first_quest = quests[0] if quests else {}
    name = clean_name(character.get('name'), 'you')
    world_id = clean_name(world.get('id'), '')
    world_name = clean_name(world.get('name_en') or world.get('name') or world.get('name_zh'), 'this world')
    location = clean_name(save.get('location'), 'the road ahead')
    house = clean_name(character.get('house'), '')
    role = clean_name(character.get('role'), '')
    last_summary = (sidecar.get('last_summary') or '').strip()
    quest_name = clean_name(first_quest.get('name'), '')

    if world_id == 'game-of-thrones':
        lang = normalize_lang(save.get('language')) or 'en'
        first_destination = clean_name((first_quest.get('intel') or {}).get('first_destination'), '南岸') if lang == 'zh' else clean_name((first_quest.get('intel') or {}).get('first_destination'), 'the southern coast')
        if lang == 'zh':
            parts = [
                f"你现在仍是{name}，而且已经深陷豪斯{house or 'Martell'}背后的那条南方暗线。",
                f"你一路走到这里，不是为了听流言，而是为了确认穿过{first_destination}的那条隐秘路线到底是真的，还是有人故意放出来的影子。",
            ]
            if last_summary and any('\u4e00' <= ch <= '\u9fff' for ch in last_summary):
                parts.append(f"上一次，局势是这样拧紧的：{last_summary}")
            return ''.join(p.strip() for p in parts if p.strip())

        parts = [
            f"You are {name}, already deep in a covert southern line tied to House {house or 'Martell'}.",
            f"You came this far to verify whether the hidden route through {first_destination} was real, not just whispered intrigue.",
        ]
        if last_summary:
            parts.append(f"Last time, the pressure showed itself like this: {last_summary}")
        return ' '.join(p.strip() for p in parts if p.strip())

    if world_id == 'lotr':
        parts = [
            f"You are {name}, still moving inside the same Middle-earth thread rather than starting a fresh adventure.",
            f"What matters now is the road around {location}: the company, the danger, and the burden you were already carrying have not gone away.",
        ]
        if quest_name:
            parts.append(f"The current line remains '{quest_name}', and today\'s sign matters because it presses on that same path.")
        if last_summary:
            parts.append(f"Last time, the world shifted like this: {last_summary}")
        return ' '.join(p.strip() for p in parts if p.strip())

    if world_id == 'sengoku':
        parts = [
            f"你不是刚踏进这座城的人，你已经在这条{faction_or_default(house)}的乱世线里站住了脚。",
            f"你现在以{role or '乱世之人'}的身份卡在 {location} 这一局里，今天的风声不是新故事，而是旧局势继续发酵。",
        ]
        if last_summary:
            parts.append(f"上一次局势是这样拧起来的：{last_summary}")
        return ''.join(p.strip() for p in parts if p.strip())

    parts = []
    if house and role:
        parts.append(f"You are {name}, moving through {world_name} as {role} aligned with {house}.")
    elif house:
        parts.append(f"You are {name}, moving through {world_name} under the banner of {house}.")
    elif role:
        parts.append(f"You are {name}, moving through {world_name} as {role}.")
    else:
        parts.append(f"You are {name}, already deep in the current thread at {location}.")

    if quest_name:
        parts.append(f"Your current line is still '{quest_name}', and the pressure around it has not gone still.")
    else:
        parts.append(f"You came here because the thread around {location} already mattered before today.")

    if last_summary:
        parts.append(f"Last time, the world shifted like this: {last_summary}")

    return ' '.join(p.strip() for p in parts if p.strip())


def faction_or_default(value: str) -> str:
    return value or '势力'


def generic_update(save: dict, world: dict, sidecar: dict) -> dict:
    character = save.get('character', {})
    name = clean_name(character.get('name'), 'the player')
    world_name = clean_name(world.get('name_en') or world.get('name') or world.get('name_zh'), 'the world')
    location = clean_name(save.get('location'), 'the road ahead')
    history = sidecar.get('history', [])
    severity = pick_severity(f"{world.get('id')}:{name}:{location}:{len(history)}")
    recap = build_recap(save, world, sidecar)
    result = {
        'summary': 'Something in the world shifted while you were away.',
        'recap_text': recap,
        'story_text': f"While you were away, the balance around {location} shifted just enough to matter. Rumors moved faster than people, small loyalties bent under pressure, and whatever was quiet yesterday is a little less quiet today. In {world_name}, that is how danger announces itself: not with a trumpet, but with one detail out of place. Something has changed near the thread you were already following, and if you step back in now, you can catch the world before the new shape hardens around you. Do you move toward the disturbance, question the nearest witness, or stay hidden long enough to see who reacts first?",
        'hooks': ['Step toward the disturbance before the trail cools.'],
        'meta': {
            'rumor_threads': ['a subtle change has spread through the area'],
            'faction_movements': ['local balance shifted while the player was away'],
            'npc_watchlist': ['whoever reacts first to the disturbance'],
            'item_threads': ['the detail that now feels out of place'],
            'world_detail_notes': [f'Current pressure point: {location}']
        },
        "image_prompt": f"{world_name}, continuity-aware evolving tension near {location}, visual callback to the player's current arc, one subtle but meaningful world shift, cinematic fantasy illustration",
        'severity': severity,
        'world_id': world.get('id'),
        'character_name': name,
        'location_context': location,
    }
    routes, default_route = build_route_payload('en', result.get('hooks', []), result.get('meta', {}), location, location)
    result['suggested_routes'] = routes
    result['default_route'] = default_route
    return result


def main():
    parser = argparse.ArgumentParser(description='Generate a safe, sidecar-friendly YumFu daily evolution update')
    parser.add_argument('--user-id', required=True)
    parser.add_argument('--universe', required=True)
    args = parser.parse_args()

    save, _ = load_save(args.user_id, args.universe)
    world, _ = load_world(args.universe)
    sidecar, _ = load_sidecar(args.user_id, args.universe)

    if args.universe == 'game-of-thrones':
        result = got_update(save, world, sidecar)
    elif args.universe == 'sengoku':
        result = sengoku_update(save, world, sidecar)
    elif args.universe == 'lotr':
        result = lotr_update(save, world, sidecar)
    elif args.universe == 'journey-to-west':
        result = journey_to_west_update(save, world, sidecar)
    else:
        result = generic_update(save, world, sidecar)

    print(json.dumps({'success': True, 'result': result}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
