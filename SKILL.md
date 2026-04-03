---
name: yumfu
description: Multi-World MUD - Wuxia, Harry Potter, LOTR & more | 多世界MUD - 武侠/哈利波特/指环王等
homepage: https://github.com/yumyumtum/yumfu
metadata:
  {
    "openclaw":
      {
        "emoji": "🌍",
        "requires": { "bins": ["uv"], "env": ["GEMINI_API_KEY"] },
        "primaryEnv": "GEMINI_API_KEY"
      }
  }
---

# YumFu - Multi-World MUD 🌍

**Choose Your Adventure** | **选择你的冒险**

### ✅ **Available Now:**
- ⚔️ **Xiaoao Jianghu** (笑傲江湖) - Jin Yong wuxia classic
- ⚡ **Harry Potter** - Hogwarts, magic, wizarding duels
- 🐱 **Warrior Cats** - Clan life, forest territories, warrior code

### 🚧 **Coming Soon (Roadmap):**
- 🗡️ **Lord of the Rings** - Middle-earth, Fellowship
- 🐉 **Game of Thrones** - Westeros, power struggles
- 🐺 **The Witcher** - Monster hunting, Slavic folklore
- 📚 **More Jin Yong Novels** - 倚天屠龙记, 射雕英雄传, 天龙八部

---

## 🌐 Language & World Selection | 语言与世界选择

**First time?** Start with language selection:
```
/yumfu start
```

You'll see / 你会看到:
```
🌍 Welcome to YumFu! | 欢迎来到YumFu！

1. 中文 (Chinese) - 武侠世界
2. English - Fantasy Realms

Reply: /yumfu lang <1|2>
```

Then choose your world / 然后选择世界:

**中文 (Available Now):**
- **笑傲江湖** (Xiaoao Jianghu) - 华山派、武当、少林、江湖恩怨

**English (Available Now):**
- **Harry Potter** - Hogwarts houses, magic, wizarding adventures
- **Warrior Cats** - ThunderClan, RiverClan, forest territories

**Coming Soon:** LOTR, Game of Thrones, The Witcher, 倚天屠龙记, 射雕英雄传

---

## 🎮 核心特色 | Core Features

- ⚔️ **多人在线** - 在群聊中 @我 即可加入江湖
- 🤝 **组队冒险** - 最多5人组队，共享经验和战利品
- 💥 **PvP 切磋** - 友谊切磋或生死决斗
- 🌐 **共享世界** - 击杀 NPC、抢夺秘籍会影响所有玩家
- 🎨 **水墨风配图** - 每个场景自动生成水墨画风图片
- 📊 **实时排行榜** - 等级、善恶值、财富榜

---

## 触发指令

所有指令以 `/yumfu` 或 `/江湖` 开头

### 🌐 Language Support | 双语支持

**All commands support both English and Chinese aliases:**

| English | 中文 | Action |
|---------|------|--------|
| `/yumfu start` | `/yumfu 开始` | Start new game / 开始新游戏 |
| `/yumfu continue` | `/yumfu 继续` | Continue saved game / 继续游戏 |
| `/yumfu status` | `/yumfu 状态` | Show character stats / 显示状态 |
| `/yumfu help` | `/yumfu 帮助` | Show all commands / 显示帮助 |
| `/yumfu go <place>` | `/yumfu 去 <地点>` | Travel to location / 前往某地 |
| `/yumfu look` | `/yumfu 看` | Look around / 查看四周 |
| `/yumfu map` | `/yumfu 地图` | Show map / 显示地图 |
| `/yumfu fight <target>` | `/yumfu 战 <对手>` | Start combat / 发起战斗 |
| `/yumfu train <skill>` | `/yumfu 练 <功法>` | Train skill / 修炼武功 |

**Use the language that matches your selected world!**

---

### 游戏管理
- `/yumfu start` 或 `/yumfu 开始` — 开始新游戏（创建角色）
- `/yumfu continue` 或 `/yumfu 继续` — 继续已保存的游戏
- `/yumfu save` — 保存当前游戏状态
- `/yumfu status` 或 `/yumfu 状态` — 显示角色属性、物品、位置
- `/yumfu help` 或 `/yumfu 帮助` — 显示所有指令

### 移动与探索
- `/yumfu go <地点>` 或 `/yumfu 去 <地点>` — 前往某地
- `/yumfu look` 或 `/yumfu 看` — 查看当前位置
- `/yumfu map` 或 `/yumfu 地图` — 显示已知地点

### 战斗
- `/yumfu fight <目标>` 或 `/yumfu 战 <对手>` — 发起战斗
- `/yumfu attack <招式>` 或 `/yumfu 攻 <招式>` — 战斗中使用特定招式
- `/yumfu defend` 或 `/yumfu 守` — 防御姿态
- `/yumfu flee` 或 `/yumfu 逃` — 尝试逃跑

### 修炼与技能
- `/yumfu train <功法>` 或 `/yumfu 练 <功法>` — 修炼武功
- `/yumfu meditate` 或 `/yumfu 打坐` — 恢复体力/内力，有机会顿悟
- `/yumfu skills` 或 `/yumfu 武功` — 列出已学武功和等级

### 社交
- `/yumfu talk <NPC>` 或 `/yumfu 对话 <人物>` — 与NPC对话
- `/yumfu join <门派>` 或 `/yumfu 拜入 <门派>` — 加入武林门派
- `/yumfu reputation` 或 `/yumfu 名望` — 查看各门派声望

### 物品
- `/yumfu inventory` 或 `/yumfu 背包` — 显示背包
- `/yumfu use <物品>` 或 `/yumfu 用 <物品>` — 使用物品
- `/yumfu buy <物品>` 或 `/yumfu 买 <物品>` — 从当前商店购买
- `/yumfu sell <物品>` 或 `/yumfu 卖 <物品>` — 向当前商店出售

---

## 🤝 多人指令（新增）

### 组队系统
- `/yumfu team create <队名>` — 创建队伍
- `/yumfu team invite @用户` — 邀请队友
- `/yumfu team join <队名>` — 加入队伍
- `/yumfu team leave` — 离队
- `/yumfu team status` — 查看队伍状态
- `/yumfu team list` — 列出所有队伍

### PvP 切磋
- `/yumfu duel @用户` — 友谊切磋（点到为止）
- `/yumfu duel @用户 --death-match` — 生死决斗（战至一方HP=0）
- `/yumfu watch` — 观战当前战斗

### 江湖信息
- `/yumfu world` — 查看世界状态（NPC位置、门派控制）
- `/yumfu events` — 查看今日江湖大事
- `/yumfu leaderboard` — 查看排行榜
- `/yumfu players` — 查看在线玩家

---

## 🌐 多人机制

### 共享世界
- **NPC 唯一性** - 洪七公只有一个，被杀后所有玩家都看到"已死"
- **秘籍争夺** - 九阴真经只有一本，先得者得，其他人需抢夺
- **门派战争** - 多人加入不同门派可攻城略地
- **世界事件** - 所有玩家行为记录到事件日志

### 组队机制
- **人数限制** - 最多5人
- **善恶限制** - 善恶值差>50 无法组队（正邪难两立）
- **门派限制** - 敌对门派无法组队
- **经验分配** - 按战斗贡献分配
- **战利品** - 队长分配或投骰

### PvP 机制

**友谊切磋**（默认）:
- HP 降至 20% 自动停止
- 不影响善恶值
- 胜者获得经验

**生死决斗**:
- 战至一方 HP = 0
- 败者掉落装备/秘籍
- 杀人者善恶值 -20
- 需要双方同意

### 相互影响

**1. NPC 击杀**
- 玩家A杀了洪七公 → 世界状态更新
- 玩家B去找洪七公 → "洪七公已被玩家A所杀"
- 江湖通缉：杀人者善恶值-50，各大门派追杀

**2. 门派争霸**
- 多个玩家加入不同门派
- 可攻占城市（如：魔教攻占洛阳）
- 影响所有玩家的任务和交易

**3. 秘籍争夺**
- 九阴真经只有一本（首先获得者拥有）
- 其他玩家想要？抢！或者拜师学习
- 可交易、可掉落

**4. 声望系统**
- **武林至尊榜** - 等级排行
- **善恶榜** - 善恶值排行
- **财富榜** - 银两排行
- 实时更新，所有玩家可见

---

## 游戏设计

### 世界观
金庸、古龙经典武侠世界：
- 金庸、古龙小说中的经典地点
- 著名人物作为NPC（部分友善，部分敌对）
- 多条故事线和任务
- **共享世界状态** - 所有玩家影响同一个江湖

### 角色系统
- **属性**: 体力(HP)、内力(MP)、攻击、防御、速度、悟性
- **武功**: 向高手学习、寻找秘籍、打坐顿悟
- **门派**: 少林、武当、峨嵋、丐帮、明教、古墓派、华山、全真教、日月神教、独行侠(无门派)
- **善恶值**: 影响NPC互动、可接任务、结局、组队限制
- **等级**: 1-100，称号（无名小卒 → 江湖新秀 → 一流高手 → 绝世高手 → 武林至尊）

### 战斗系统
- 回合制，先手基于速度
- 每种武功有独特招式和效果
- 内力驱动特殊招式
- 装备影响属性
- Boss战需要策略
- **PvP 战斗** - 玩家间切磋/决斗

### 成长系统
- 修炼武功提升等级
- 寻找秘籍（九阴真经、九阳神功、独孤九剑等）
- 完成任务获得奖励
- 积累门派声望
- 解锁传世神兵
- **组队经验加成** - 组队战斗获得额外经验

---

## 技术实现

### 多人存档系统
```
memory/yumfu/
├── world-state.json          # 共享世界状态（NPC、秘籍、门派控制）
├── saves/
│   ├── xiaoao/               # 笑傲江湖存档目录
│   │   ├── user-123456789.json
│   │   └── user-2345678901.json
│   ├── harry-potter/         # Harry Potter存档目录
│   │   └── user-123456789.json
│   └── warrior-cats/         # Warrior Cats存档目录
│       └── user-123456789.json
├── teams/
│   └── team-华山论剑.json     # 临时队伍状态
└── events/
    └── 2026-04-01.json        # 今日江湖大事
```

**Note:** Each world uses a separate subfolder to prevent save conflicts.

### 世界状态（world-state.json）
```json
{
  "version": 1,
  "game_time": { "year": "南宋", "season": "春", "day": 1 },
  "npcs": {
    "洪七公": {
      "location": "洛阳",
      "hp": 1000,
      "status": "alive",
      "reputation": {
        "user-123456789": 50,
        "user-2345678901": -20
      },
      "killed_by": null
    }
  },
  "world_events": [...],
  "faction_control": { "洛阳": "丐帮" },
  "rare_items": {
    "九阴真经": { "owner": "user-123456789", "status": "owned" }
  },
  "leaderboards": {
    "level": [...],
    "morality": [...],
    "wealth": [...]
  }
}
```

### 玩家存档（user-{id}.json）
```json
{
  "version": 2,
  "user_id": "123456789",
  "language": "zh",
  "universe": "xiaoao",
  "character": { "name": "大红虾🦐", "level": 1, ... },
  "location": "洛阳城",
  "inventory": [...],
  "skills": [...],
  "quests": [...],
  "team_id": null,
  "in_combat_with": null
}
```

**Important:** Save path is `~/clawd/memory/yumfu/saves/{universe}/user-{id}.json`

### 💾 Save File Management (Agent Instructions)

**CRITICAL:** Persist game state after every significant action to prevent data loss!

#### When to Save:
1. **Training completion** - New skill learned
2. **Combat end** - HP/stats changed
3. **Quest milestone** - Progress updated
4. **Location change** - Player moved
5. **Inventory change** - Item gained/used
6. **Character creation** - First save

#### Save Workflow:
```python
# 1. Update character state in memory
character["hp"] = new_hp
character["location"] = new_location

# 2. Write to correct path
save_path = f"~/clawd/memory/yumfu/saves/{universe}/user-{user_id}.json"
with open(save_path, 'w') as f:
    json.dump(save_data, f, indent=2)

# 3. Verify write succeeded
if os.path.exists(save_path):
    print(f"✅ Game saved: {save_path}")
else:
    # Recovery: attempt backup path
    print(f"❌ Save failed! Attempting recovery...")
```

#### Error Recovery:
- If save fails: **Notify player immediately**
- Attempt backup save to `~/clawd/memory/yumfu/backups/`
- Log error to `~/clawd/memory/yumfu/save-errors.log`
- **Never silently fail** - player must know their progress may be lost

### 队伍状态（team-{name}.json）
```json
{
  "team_name": "华山论剑",
  "created": "2026-04-01T22:00:00",
  "leader": "user-123456789",
  "members": [
    { "user_id": "123456789", "name": "大红虾🦐", "hp": 90 },
    { "user_id": "2345678901", "name": "小龙虾", "hp": 100 }
  ],
  "exp_share": true,
  "loot_mode": "leader"
}
```

### 游戏引擎
Agent **就是**游戏引擎：
1. **识别玩家** - 从 Telegram ID 加载对应存档
2. **读取世界状态** - `world-state.json`
3. **处理玩家指令** - 修炼、战斗、组队、PvP
4. **生成武侠文风剧情** - 中文叙述
5. **计算结果** - 战斗/修炼/骰子系统
6. **更新世界状态** - 影响所有玩家
7. **记录事件** - 写入今日事件日志
8. **生成配图** - 水墨风场景图
9. **保存状态** - 更新玩家存档和世界状态

### 叙述风格

**Narrative style adapts to the world:**

#### 🇨🇳 **Chinese Worlds (Xiaoao Jianghu)**
- Use Chinese throughout
- Wuxia literary style (武侠文风)
- Show attributes: `[体力 -15] [内力 +5]`
- Combat descriptions with flair
- NPC dialogue matches personality

#### 🇬🇧 **English Worlds (Harry Potter, Warrior Cats)**
- Use English throughout
- Genre-appropriate style (magical/wilderness)
- Show attributes: `[HP -15] [Stamina +5]`
- Combat/action descriptions fitting the world
- NPC dialogue matches character voice

**Universal:**
- Blend narrative with game mechanics
- Combat writing has tension
- **Multiplayer interactions are immersive** - "You see 大红虾 sparring with 洪七公" / "You see Tumpaw training with Willowpelt"

### 骰子与随机
使用透明的随机系统：
```bash
# 百分比检定
shuf -i 1-100 -n 1

# D20检定
shuf -i 1-20 -n 1

# 战斗示例
攻击检定: 1d20+5 = 18 (成功!)
伤害: 2d10+3 = 16
```

### 战斗日志格式
```
⚔️ 大红虾 vs 小龙虾

[回合1] 大红虾使用【降龙十八掌】
[投骰] 攻击检定: 1d20+5 = 18 (命中!)
[投骰] 伤害: 2d10+3 = 16
💥 小龙虾未能闪避！
[体力] 小龙虾 100 → 84

[回合2] 小龙虾使用【玉女剑法】
...
```

---

## 场景配图 (Scene Illustration)

**🚨 CRITICAL RULE**: **Every significant story moment MUST generate an image automatically BEFORE narration.**

### ⚡ Agent Execution Order (MANDATORY)

When a trigger event occurs:
1. **FIRST**: Identify trigger type (location/NPC/combat/etc.)
2. **SECOND**: Generate image immediately (run script, DO NOT wait)
3. **THIRD**: Send image with message tool
4. **FOURTH**: Continue narration

**DO NOT** narrate first and generate later. **DO NOT** wait for user to ask "where's the picture?"

### When to Generate Images (AUTO-TRIGGER)

✅ **ALWAYS generate for:**
1. **New location arrival** - Player enters camp/dungeon/city
2. **Training completion** - After learning a new skill
3. **Combat start** - First round of any fight
4. **NPC encounter** - Meeting important characters (approaching Firestar = TRIGGER)
5. **Quest milestones** - Completing objectives
6. **Ceremony/ritual** - Apprentice ceremony, leader coronation, etc.
7. **Discovery** - Finding items, secrets, new areas

❌ **DO NOT generate for:**
- Menu screens / stat displays
- Info dumps / lore explanations (unless player explicitly explores a location)
- "What can I do?" meta questions
- Save/load operations

**Example Flow:**
```
User: "I want to talk to Firestar"
→ Agent: "This is NPC encounter trigger!"
→ IMMEDIATELY run generate_image.py
→ Send image + start dialogue
→ NOT: Start dialogue, then "oh wait, I should generate image"
```

### Image Generation Command
```bash
uv run ~/clawd/skills/yumfu/scripts/generate_image.py \
  --prompt "<scene prompt>" \
  --filename "~/.openclaw/media/outbound/yumfu/$(date +%Y%m%d-%H%M%S)-<scene>.png" \
  --resolution 2K
```

**Note**: Script does NOT auto-send. Use `message` tool with `media` parameter to send.

---

### Art Styles by World

**Each world has its own signature art style. ALWAYS include the style prefix in prompts.**

#### 🇨🇳 Xiaoao Jianghu (笑傲江湖)
```
Chinese wuxia ink wash painting style (水墨武侠风), dramatic cinematic composition, muted earth tones with selective vivid accents (red, gold), atmospheric fog and light rays, textured rice paper background,
```

#### 🧙 Harry Potter
```
Hogwarts watercolor illustration style, magical atmosphere, warm candlelight and moonlight, storybook composition, detailed wizarding world architecture, enchanted particle effects, painterly texture,
```

#### 🐱 Warrior Cats
```
Semi-realistic warrior cats art style, forest atmosphere with dappled sunlight, detailed cat anatomy and expressions, natural woodland setting, dramatic lighting through trees, storybook illustration quality,
```

### 场景类型与提示词模板

#### 🏞️ 探索 / 到达新地点
```
[风格前缀] wide establishing shot of <地点>, <时间>, <天气/氛围>, small figure of a lone swordsman in the scene, architectural details of <建筑>, <自然元素>
```

#### 👤 NPC遭遇 / 对话
```
[风格前缀] medium close-up portrait of <NPC描述>, <表情>, <特征>, <服饰细节>, <背景>, dramatic side lighting
```

#### ⚔️ 战斗（PvE / PvP）
```
[风格前缀] dynamic action shot, <角色> vs <敌人/玩家>, <正在使用的招式>, motion blur on weapon, debris/leaves flying, intense facial expressions, <环境>
```

**多人战斗**：
```
[风格前缀] chaotic multi-person combat, 3-5 martial artists in intense battle, various weapons and techniques, swirling energy effects, dramatic composition, <location>
```

#### 🧘 修炼 / 打坐
```
[风格前缀] serene composition, <角色> in <修炼姿势>, <地点>, mystical qi energy swirling around body as translucent wisps, soft golden light, tranquil atmosphere
```

#### 📜 剧情时刻 / 关键物品
```
[风格前缀] dramatic still life or vignette, <关键物品或象征>, <氛围光>, cinematic depth of field, <相关元素>
```

#### 🏪 商店 / 城镇室内
```
[风格前缀] warm interior scene, <商店/客栈描述>, lantern light, wooden beams, <NPC和物品>, cozy detailed atmosphere, period-accurate props
```

#### 🤝 组队场景（新增）
```
[风格前缀] group portrait, <team members> standing together in heroic formation, various weapons and martial arts stances, sense of camaraderie, <location background>
```

### 工作流程
1. 根据游戏动作判断场景类型
2. 使用风格前缀 + 场景模板组合提示词
3. 生成 1K 分辨率图片（快速）
4. 通过 `message` tool 发送图片（`media` 参数）
5. 图片自动归档到 `~/.openclaw/media/outbound/yumfu/`

### 规则
- 每回合一张图（不可跳过）
- 匹配该回合最戏剧性/有趣的时刻
- 战斗：展示动作，不是结果
- 对话：聚焦NPC面部/性格
- **多人场景**：包含所有相关玩家
- 文件名包含时间戳（唯一性）
- 图片发送后自动归档

---

## 🎮 世界特色系统 | World-Specific Features

Each world has unique progression systems designed for its target age group:

### ⚔️ **笑傲江湖 (Xiaoao Jianghu)** - 成人向 18+

**核心系统**:
- **装备品质**: 凡品 → 良品 → 宝器 → 神兵 (影响技能发挥)
- **武功境界**: 初窥门径 → 返璞归真 (6级，可自创招式)
- **道德系统**: 善恶值 -100~+100 (决定5种结局)
- **恋爱系统**: 3条情感线 (任盈盈/岳灵珊/仪琳)
- **制造系统**: 锻造武器 + 炼丹
- **7章节门槛**: 入门→危机→内斗→复仇→大战→传承→对决

**防速通机制**:
- 技能需师父认可才能学
- 装备影响技能威力（剑法必须用剑）
- 等级门槛锁定主线剧情
- 绝学需特殊条件（独孤九剑=Lv30+悟性80+风清扬）

---

### ⚡ **Harry Potter** - 青年向 13+

**核心系统**:
- **7学年制**: 不可跳年，每年4-6小时游戏时间
- **考试系统**: O.W.L.s (Year 5) + N.E.W.T.s (Year 7)，6级评分
- **友谊系统**: 5好友槽，关系分5级，解锁组队咒语
- **魁地奇**: 4位置可选，QTE小游戏
- **分院帽**: 7题性格测试决定学院（可请求）
- **学术**: 7必修课 + 5选修课，作业影响考试

**防速通机制**:
- 必须通过年终考试才能升年级
- 咒语分4层，需对应年级才能学
- 友谊等级解锁剧情任务
- 魔法物品需购买（隐形斗篷=传奇稀有）

---

### 🐱 **Warrior Cats** - 儿童向 8-12

**核心系统**:
- **7等级仪式链**: Kit → Apprentice → Warrior → Deputy → Leader (每级有仪式)
- **4季节系统**: 新叶/绿叶/落叶/寒叶 (影响猎物/疾病/战争)
- **导师制度**: 性格匹配，每日训练，关系4阶段
- **星族/黑森林**: 正邪双路线，梦境训练，预言引导
- **武士守则**: 14条规则，违反=流放/黑森林

**防速通机制**:
- 学徒必须学满7技能才能成为武士
- 需抓10只猎物 + 赢3场战斗 + 导师批准
- 副族长需先带过1个徒弟
- 族长需去月池接受九命加身

---

## 平台兼容性 | Platform Support

YumFu works across multiple AI platforms with varying feature sets:

### 🌟 **OpenClaw (Telegram, Discord, etc.)**
**Full multiplayer experience:**
- ✅ Multi-player (teams, PvP, shared world)
- ✅ AI-generated images (auto-sent)
- ✅ Persistent saves across sessions
- ✅ Group chat support
- ✅ User identification via platform ID

**Best for:** Group adventures, PvP, shared world events

---

### 🖥️ **Claude Code / Desktop AI**
**Single-player mode:**
- ✅ Full gameplay (exploration, combat, quests)
- ✅ AI-generated images (manual save/view)
- ✅ Persistent saves (local files)
- ❌ No multiplayer (PvP/teams disabled)
- ❌ No shared world state

**Best for:** Solo story-driven campaigns

---

### 💬 **Native Claude (Web/Mobile)**
**Text-only mode:**
- ✅ Basic gameplay (limited features)
- ✅ Manual save/load via copy-paste JSON
- ❌ No images
- ❌ No multiplayer
- ❌ No persistent saves (session-based)

**Best for:** Quick casual play, testing stories

---

## 初始化

### 首次游戏

**OpenClaw (Telegram/Discord):**
1. 玩家在群聊中 `@我 /yumfu start`
2. 角色创建流程：姓名、门派、属性
3. 生成该玩家的存档 `~/clawd/memory/yumfu/saves/{universe}/user-{platform_id}.json`
4. 显示开场剧情
5. 生成第一张场景图
6. 记录到世界事件

### 继续游戏
1. 玩家 `@我 /yumfu continue`
2. 读取 `user-{telegram_id}.json`
3. 读取 `world-state.json`（NPC状态、世界变化）
4. 显示当前状态 + 最新江湖大事
5. 等待玩家指令

### 多人交互
1. 玩家A `@我 /yumfu duel @玩家B`
2. 系统检查双方存档
3. 进入战斗流程
4. 更新双方存档
5. 记录到世界事件
6. 其他玩家可 `/yumfu events` 查看

---

## 最佳实践

### 对于游戏设计者（Agent）
- 武侠文风要有韵味，但不能过于文绉绉
- 战斗要有策略性，不能只是数字游戏
- NPC性格要鲜明（郭靖憨厚、黄药师古怪、欧阳锋阴险）
- 善恶值要有明显后果（杀人过多会被正派追杀）
- 秘籍要难获得，但值得追求
- **多人互动要公平** - 不能偏袒某个玩家
- **世界状态要一致** - 所有玩家看到同一个NPC状态
- **PvP要平衡** - 等级差过大可以拒绝决斗

### 对于玩家
- 多与NPC对话，触发隐藏任务
- 善用打坐恢复和顿悟
- 装备和武功要配合（重剑配内功，轻功配暗器）
- 善恶值会影响剧情分支
- 存档多用几个槽位，避免后悔
- **组队时注意队友善恶值** - 正邪难两立
- **秘籍争夺要谨慎** - 可能树敌
- **PvP前评估实力** - 不要轻易生死决斗

---

## 触发规则

当玩家消息以下列任一开头时激活：
- `/yumfu`
- `/江湖`

**群聊支持**：
- 在群聊中使用 `@我 /yumfu <指令>` 即可触发
- 每个玩家独立存档
- 共享世界状态

---

**武侠江湖，等你来闯！邀上好友，共闯江湖！** ⚔️

---

## 📚 Storybook Feature

**NEW**: Every adventure is automatically recorded and can be turned into a beautiful PDF storybook!

### How It Works

**1. During Gameplay:**
- All dialogue, events, and choices are logged to `~/clawd/memory/yumfu/sessions/{universe}/user-{id}/`
- Images generated during play are tracked in the save file
- Session files use JSONL format (one event per line)

**2. Generate Storybook:**
```bash
# After finishing an adventure
uv run ~/clawd/skills/yumfu/scripts/generate_storybook.py \
  --user-id 1309815719 \
  --universe warrior-cats \
  --session-id 20260403-001349

# Or let it auto-detect from save file
uv run ~/clawd/skills/yumfu/scripts/generate_storybook.py \
  --user-id 1309815719 \
  --universe warrior-cats
```

**3. Output:**
```
~/clawd/memory/yumfu/storybooks/warrior-cats/user-1309815719-session-20260403/
├── story.md              # Markdown version
├── storybook.pdf         # Beautiful PDF with images
└── images/               # All session images
    ├── tumpaw-ceremony.png
    ├── tumpaw-firestar.png
    └── tumpaw-fishing.png
```

### Features

- ✅ **Auto-tracking** - No manual logging needed
- ✅ **Beautiful formatting** - Professional PDF layout
- ✅ **Image integration** - All AI-generated art included
- ✅ **Stats summary** - Final character stats and relationships
- ✅ **Achievements** - All unlocked achievements listed
- ✅ **Multi-language** - Works with Chinese and English worlds

### Example Storybook Structure

```markdown
# Tumpaw: A Warrior Cats Tale

**Universe:** Warrior Cats  
**Character:** Tumpaw  
**Rank:** Apprentice  
**Journey Date:** April 3, 2026

---

## 📖 The Story Begins

### Chapter 1
Born in ThunderClan nursery...

### Chapter 2
Became apprentice at 6 moons old...

## 🎨 Moments Captured

### Tumpaw Ceremony
![Ceremony](images/tumpaw-ceremony.png)

### Meeting Firestar
![Firestar](images/tumpaw-firestar.png)

## 🏆 Achievements Unlocked
- ✨ First Day as Apprentice
- ✨ Learned to Swim

## 📊 Final Stats
- **Hunting:** 13
- **Fighting:** 6
- **Swimming:** 15

## 💝 Bonds Formed
- **Willowpelt** (❤️ 35): Mentor, proud of progress
- **Firestar** (❤️ 30): Sees potential

---
*Generated by YumFu Storybook Generator*
```

### When to Generate

**Trigger storybook generation when:**
- Player reaches major milestone (becomes warrior, leader, etc.)
- Player explicitly requests (`/yumfu storybook`)
- Session ends (character dies, quest completed)
- Player hasn't played in 24+ hours (auto-archive)

### Agent Instructions

When player reaches an ending or requests storybook:
1. Call `generate_storybook.py` with user's ID and universe
2. Wait for PDF generation (10-30 seconds)
3. Send PDF to user via `message` tool with media parameter
4. Congratulate them on their adventure!

---
