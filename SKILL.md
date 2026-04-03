---
name: yumfu
description: 武侠江湖 MUD - 多人在线武侠世界，PvP/组队/共享NPC，每步配水墨风配图
homepage: https://github.com/openclaw/openclaw
metadata:
  {
    "openclaw":
      {
        "emoji": "⚔️",
        "requires": { "bins": ["uv"], "env": ["GEMINI_API_KEY"] },
        "primaryEnv": "GEMINI_API_KEY"
      }
  }
---

# 武侠江湖 MUD (YumFu) ⚔️

**多人在线武侠世界** - 金庸、古龙小说宇宙，支持 PvP、组队、共享NPC、相互影响。

## 🎮 核心特色

- ⚔️ **多人在线** - 在群聊中 @我 即可加入江湖
- 🤝 **组队冒险** - 最多5人组队，共享经验和战利品
- 💥 **PvP 切磋** - 友谊切磋或生死决斗
- 🌐 **共享世界** - 击杀 NPC、抢夺秘籍会影响所有玩家
- 🎨 **水墨风配图** - 每个场景自动生成水墨画风图片
- 📊 **实时排行榜** - 等级、善恶值、财富榜

---

## 触发指令

所有指令以 `/yumfu` 或 `/江湖` 开头：

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
│   ├── user-123456789.json  # 玩家存档（按 Telegram ID）
│   ├── user-2345678901.json
│   └── ...
├── teams/
│   └── team-华山论剑.json     # 临时队伍状态
└── events/
    └── 2026-04-01.json        # 今日江湖大事
```

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
  "version": 1,
  "user_id": "123456789",
  "character": { "name": "大红虾🦐", "level": 1, ... },
  "location": "洛阳城",
  "inventory": [...],
  "skills": [...],
  "quests": [...],
  "team_id": null,
  "in_combat_with": null
}
```

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
- 所有输出使用中文，武侠文风
- 叙事与游戏机制结合
- 明确显示属性变化：`[体力 -15] [内力 +5]`
- 战斗描写要有张力
- NPC对话符合人物性格
- **多人互动要有代入感** - "你看到大红虾正在和洪七公切磋"

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

## 场景配图 (武侠图景)

**每个游戏回合必须生成配图**，使用 YumFu 内置的图片生成脚本（Gemini 图片生成）。

### 图片生成指令
```bash
uv run ~/clawd/skills/yumfu/scripts/generate_image.py \
  --prompt "<场景提示词>" \
  --filename "~/.openclaw/media/outbound/yumfu/$(date +%Y%m%d-%H%M%S)-<scene>.png" \
  --resolution 1K
```

**注意**：YumFu 使用专用脚本，不会自动发送图片，由游戏引擎控制发送时机。

### 固定艺术风格
**所有场景提示词必须以此风格前缀开头**：

```
Chinese wuxia ink wash painting style (水墨武侠风), dramatic cinematic composition, muted earth tones with selective vivid accents (red, gold), atmospheric fog and light rays, textured rice paper background,
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

## 初始化

### 首次游戏
1. 玩家在群聊中 `@我 /yumfu start`
2. 角色创建流程：姓名、门派、属性
3. 生成该玩家的存档 `user-{telegram_id}.json`
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
