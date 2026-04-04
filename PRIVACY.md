# YumFu Privacy & Data Policy

## 📊 What Data Does YumFu Store?

YumFu is a **local-first** game. All your data stays on your machine unless you explicitly enable cloud features.

### ✅ Always Stored Locally

1. **Game Saves** (`~/clawd/memory/yumfu/saves/`)
   - Character stats, inventory, location
   - Quest progress, relationships, achievements
   - **Contains**: Game state only, no chat logs
   - **Purpose**: Resume your game across sessions

2. **Backup Saves** (`~/clawd/memory/yumfu/backups/`)
   - Automatic backups before overwriting saves
   - **Retention**: Manual cleanup (not auto-deleted)
   - **Purpose**: Recovery if save corrupts

3. **AI-Generated Images** (`~/.openclaw/media/outbound/yumfu/`)
   - Scene illustrations generated during gameplay
   - **Format**: PNG images (2K resolution)
   - **Purpose**: Visual storytelling

### ⚠️ Optional: Session Logging

**Session logs** record full gameplay conversations (your inputs + AI responses).

**Location**: `~/clawd/memory/yumfu/sessions/{universe}/user-{id}/`  
**Format**: JSONL (one turn per line)  
**Contains**: Player commands, AI narration, image filenames  
**Purpose**: Generate storybook PDFs of your adventures

**🔒 Privacy Control**:
```bash
# Disable session logging (recommended for privacy)
export YUMFU_NO_LOGGING=1

# Or delete logs manually
rm -rf ~/clawd/memory/yumfu/sessions/
```

**Note**: Session logging is **optional** for storybook generation. If you don't want PDFs of your gameplay, you don't need this feature.

---

## 🔑 External API Calls

YumFu makes **only one type** of external API call:

### Google Gemini API (Optional)

**Purpose**: Generate AI artwork for scenes  
**Endpoint**: `generativelanguage.googleapis.com`  
**Data sent**: Text prompts describing scenes (e.g., "forest with wolf")  
**Data received**: PNG images  
**Required**: No - game works in text-only mode without it

**How to disable**:
```bash
# Don't set GEMINI_API_KEY
unset GEMINI_API_KEY

# OR set text-only mode
export YUMFU_NO_IMAGES=1
```

**What's sent to Gemini**:
- Scene descriptions (e.g., "Winterfell courtyard at sunset")
- Art style specifications (e.g., "watercolor storybook style")
- **NOT sent**: Your character name, stats, or personal info

---

## 🚫 What YumFu NEVER Does

- ❌ Send your game saves to any server
- ❌ Send session logs anywhere (they stay local)
- ❌ Phone home or track usage
- ❌ Collect analytics or telemetry
- ❌ Share your data with third parties
- ❌ Require account creation or login
- ❌ Send your personal information to Gemini API

---

## 🛡️ Privacy Levels

Choose your comfort level:

### 🔒 **Maximum Privacy** (No external calls)
```bash
export YUMFU_NO_IMAGES=1
export YUMFU_NO_LOGGING=1
unset GEMINI_API_KEY
```
**What you get**: Text-only gameplay, local saves, no logs, zero network calls

### 🎨 **Balanced** (Images, no logging)
```bash
export GEMINI_API_KEY="your-key"
export YUMFU_NO_LOGGING=1
```
**What you get**: AI-generated images, local saves, no conversation logs

### 📚 **Full Features** (Images + storybooks)
```bash
export GEMINI_API_KEY="your-key"
# YUMFU_NO_LOGGING not set (logging enabled)
```
**What you get**: AI-generated images, storybook PDFs, full logs

---

## 📂 Data Locations Reference

```
~/clawd/memory/yumfu/
├── saves/                    # Game saves (ALWAYS created)
│   ├── xiaoao/
│   │   └── user-*.json
│   ├── harry-potter/
│   └── warrior-cats/
├── backups/                  # Save backups (ALWAYS created)
│   └── user-*-*.json
├── sessions/                 # Conversation logs (OPTIONAL)
│   ├── xiaoao/
│   │   └── user-*/
│   │       └── session-*.jsonl
│   └── harry-potter/
└── events/                   # World events (multiplayer only)
    └── YYYY-MM-DD.json

~/.openclaw/media/outbound/yumfu/
└── *.png                     # AI-generated images
```

---

## 🧹 Data Cleanup

### Delete Everything
```bash
rm -rf ~/clawd/memory/yumfu
rm -rf ~/.openclaw/media/outbound/yumfu
```

### Keep Saves, Delete Logs
```bash
rm -rf ~/clawd/memory/yumfu/sessions
rm -rf ~/clawd/memory/yumfu/backups
```

### Delete Old Images
```bash
find ~/.openclaw/media/outbound/yumfu -name "*.png" -mtime +30 -delete
```

---

## 🔍 Audit YumFu Yourself

### Check for Network Calls
```bash
cd ~/clawd/skills/yumfu
grep -r "http\|api\|endpoint" scripts/
```

**Expected results**:
- `generate_image.py`: Gemini API only
- No other network calls

### Review What Gets Logged
```bash
cat scripts/session_logger.py
```

**What it logs**: Player input + AI response + image filename  
**What it doesn't log**: API keys, system info, metadata

### Check GEMINI_API_KEY Usage
```bash
grep -r "GEMINI_API_KEY" scripts/
```

**Expected**: Only read from environment, never written to disk

---

## 📋 Privacy Checklist

Before installing YumFu, verify:

- [ ] I understand game saves are stored locally
- [ ] I know session logging is optional (`YUMFU_NO_LOGGING=1`)
- [ ] I know images are optional (`YUMFU_NO_IMAGES=1`)
- [ ] I reviewed where data is stored (see Data Locations)
- [ ] I know how to delete my data (see Data Cleanup)
- [ ] I understand Gemini API is the only external call
- [ ] I trust my GEMINI_API_KEY provider (Google)
- [ ] I reviewed the source code on GitHub

**Still unsure?** Read the full source:
- GitHub: https://github.com/yumyumtum/yumfu
- Security Policy: [SECURITY.md](SECURITY.md)

---

## 🤝 Trust but Verify

YumFu is **open source (GPLv3)** - you can and should read the code!

**Recommended review**:
1. `scripts/generate_image.py` - Image generation (Gemini API call)
2. `scripts/session_logger.py` - What gets logged
3. `scripts/save_game.py` - Where saves are written
4. `scripts/load_game.py` - How saves are read

**No code obfuscation, no compiled binaries, no surprises.**

---

**Questions?** Open a GitHub issue: https://github.com/yumyumtum/yumfu/issues

**Last Updated**: 2026-04-04  
**YumFu Version**: 1.0.1
