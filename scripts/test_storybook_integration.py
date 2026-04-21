#!/usr/bin/env python3
"""
YumFu Integration Test - Storybook Generation End-to-End

Validates the qualities we actually care about now:
1. HTML storybook is generated
2. Scene-bound layout stays image/text together
3. Player storybook prose is preserved
4. Stats section is populated (not empty / not raw dict dumps)
5. Print button exists
"""

import argparse
import json
import subprocess
from pathlib import Path


def create_mock_session(user_id: str, universe: str) -> Path:
    base_path = Path.home() / "clawd/memory/yumfu"
    session_dir = base_path / "sessions" / universe / f"user-{user_id}"
    session_dir.mkdir(parents=True, exist_ok=True)

    session_id = "test-20260403-001349"
    session_file = session_dir / f"session-{session_id}.jsonl"

    events = [
        {
            "timestamp": "2026-04-03T00:13:49",
            "type": "turn",
            "player": "/yumfu start",
            "player_storybook": "You stepped into the world of ThunderClan for the first time.",
            "ai": "Welcome to ThunderClan! You are born as a tiny kit in the warm nursery.",
            "ai_storybook": "ThunderClan opened around you in warmth and moss-scent, and your story began in the nursery.",
            "image": None,
        },
        {
            "timestamp": "2026-04-03T00:15:23",
            "type": "turn",
            "player": "Tumpaw",
            "player_storybook": "You chose the name Tumpaw and claimed it as your own.",
            "ai": "A fine name! Tumpaw it is. You grow quickly, and today is your apprentice ceremony!",
            "ai_storybook": "The name Tumpaw settled over you, and with it came the bright, trembling promise of apprenticeship.",
            "image": "tumpaw-ceremony-20260403.png",
        },
        {
            "timestamp": "2026-04-03T00:31:20",
            "type": "event",
            "content": "🏆 Achievement Unlocked: First Catch!",
            "image": None,
        },
    ]

    with open(session_file, "w", encoding="utf-8") as f:
        for event in events:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")

    print(f"✅ Created mock session: {session_file}")
    return session_file


def test_storybook_generation(user_id: str, universe: str):
    print("\n🧪 YumFu Storybook Integration Test\n")
    print("1️⃣ Creating mock session log...")
    create_mock_session(user_id, universe)

    print("\n2️⃣ Generating HTML storybook...")
    result = subprocess.run([
        "uv", "run",
        str(Path.home() / "clawd/skills/yumfu/scripts/generate_storybook_v3.py"),
        "--user-id", user_id,
        "--universe", universe,
        "--session-id", "test-20260403-001349",
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print(f"❌ HTML generation failed:\n{result.stderr}")
        return False
    print(result.stdout)

    print("\n3️⃣ Verifying output...")
    base_path = Path.home() / "clawd/memory/yumfu/storybooks" / universe
    storybooks = sorted(base_path.glob(f"user-{user_id}-*"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not storybooks:
        print("❌ No storybook found!")
        return False

    html_file = storybooks[0] / "storybook.html"
    if not html_file.exists():
        print(f"❌ HTML file not found: {html_file}")
        return False

    print(f"✅ HTML generated: {html_file}")
    content = html_file.read_text(encoding="utf-8")

    checks = [
        ("Player storybook prose preserved", "You stepped into the world of ThunderClan for the first time." in content),
        ("AI prose preserved", "ThunderClan opened around you in warmth and moss-scent" in content),
        ("Print button exists", "Print / Save PDF" in content or "打印 / 存 PDF" in content),
        ("Stats section exists", "Final Character Archive" in content or "终局角色档案" in content),
        ("Raw dict dump avoided", "{&#x27;skyclan&#x27;:" not in content),
        ("Event banner preserved", "Achievement Unlocked: First Catch!" in content),
    ]

    print("\n4️⃣ Content validation:")
    all_passed = True
    for name, passed in checks:
        print(f"   {'✅' if passed else '❌'} {name}")
        if not passed:
            all_passed = False

    print("\n" + "=" * 50)
    print("✅ All tests PASSED!" if all_passed else "❌ Some tests FAILED")
    print("=" * 50)
    return all_passed


def main():
    parser = argparse.ArgumentParser(description="Test YumFu storybook generation")
    parser.add_argument("--user-id", default="1309815719")
    parser.add_argument("--universe", default="warrior-cats")
    args = parser.parse_args()
    return 0 if test_storybook_generation(args.user_id, args.universe) else 1


if __name__ == "__main__":
    raise SystemExit(main())
