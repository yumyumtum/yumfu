#!/usr/bin/env python3
"""
YumFu Integration Test - Storybook Generation End-to-End

Tests the complete workflow:
1. Create mock session log
2. Generate HTML storybook
3. Convert to PDF
4. Verify output

Usage:
    uv run test_storybook_integration.py --user-id 1309815719 --universe warrior-cats
"""

import argparse
import subprocess
from pathlib import Path
import json
import shutil


def create_mock_session(user_id: str, universe: str) -> Path:
    """Create a mock session log for testing"""
    base_path = Path.home() / "clawd/memory/yumfu"
    session_dir = base_path / "sessions" / universe / f"user-{user_id}"
    session_dir.mkdir(parents=True, exist_ok=True)
    
    session_id = "test-20260403-001349"
    session_file = session_dir / f"session-{session_id}.jsonl"
    
    # Mock events
    events = [
        {
            "timestamp": "2026-04-03T00:13:49",
            "type": "turn",
            "player": "/yumfu start",
            "ai": "Welcome to ThunderClan! You are born as a tiny kit in the warm nursery.",
            "image": None
        },
        {
            "timestamp": "2026-04-03T00:15:23",
            "type": "turn",
            "player": "Tumpaw",
            "ai": "A fine name! Tumpaw it is. You grow quickly, and today is your apprentice ceremony!",
            "image": "tumpaw-ceremony-20260403.png"
        },
        {
            "timestamp": "2026-04-03T00:18:45",
            "type": "turn",
            "player": "/yumfu look",
            "ai": "You stand in ThunderClan camp. Firestar makes announcements from Highrock.",
            "image": "tumpaw-camp-20260403.png"
        },
        {
            "timestamp": "2026-04-03T00:22:10",
            "type": "turn",
            "player": "/yumfu train swimming",
            "ai": "Willowpelt leads you to the river border. Swimming is unusual for ThunderClan.",
            "image": None
        },
        {
            "timestamp": "2026-04-03T00:31:20",
            "type": "event",
            "content": "🏆 Achievement Unlocked: First Catch!",
            "image": None
        }
    ]
    
    with open(session_file, 'w', encoding='utf-8') as f:
        for event in events:
            f.write(json.dumps(event, ensure_ascii=False) + '\n')
    
    print(f"✅ Created mock session: {session_file}")
    return session_file


def test_storybook_generation(user_id: str, universe: str):
    """Test complete storybook generation"""
    print("\n🧪 YumFu Storybook Integration Test\n")
    
    # Step 1: Create mock session
    print("1️⃣ Creating mock session log...")
    session_file = create_mock_session(user_id, universe)
    
    # Step 2: Generate HTML
    print("\n2️⃣ Generating HTML storybook...")
    result = subprocess.run([
        "uv", "run",
        str(Path.home() / "clawd/skills/yumfu/scripts/generate_storybook_v3.py"),
        "--user-id", user_id,
        "--universe", universe,
        "--session-id", "test-20260403-001349"
    ], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ HTML generation failed:\n{result.stderr}")
        return False
    
    print(result.stdout)
    
    # Step 3: Verify output
    print("\n3️⃣ Verifying output...")
    base_path = Path.home() / "clawd/memory/yumfu/storybooks" / universe
    storybooks = sorted(base_path.glob(f"user-{user_id}-*"), key=lambda p: p.stat().st_mtime, reverse=True)
    
    if not storybooks:
        print("❌ No storybook found!")
        return False
    
    latest = storybooks[0]
    html_file = latest / "storybook.html"
    
    if not html_file.exists():
        print(f"❌ HTML file not found: {html_file}")
        return False
    
    print(f"✅ HTML generated: {html_file}")
    
    # Step 4: Check content
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = [
        ("Title present", "Tumpaw" in content),
        ("Player input present", "/yumfu start" in content),
        ("AI response present", "Welcome to ThunderClan" in content),
        ("Achievement present", "Achievement Unlocked" in content),
        ("Print button present", "Print to PDF" in content)
    ]
    
    print("\n4️⃣ Content validation:")
    all_passed = True
    for check_name, passed in checks:
        status = "✅" if passed else "❌"
        print(f"   {status} {check_name}")
        if not passed:
            all_passed = False
    
    # Summary
    print("\n" + "="*50)
    if all_passed:
        print("✅ All tests PASSED!")
        print(f"\n📖 Open storybook: file://{html_file}")
        print("💡 Convert to PDF: Open in browser and print")
    else:
        print("❌ Some tests FAILED")
    print("="*50)
    
    return all_passed


def main():
    parser = argparse.ArgumentParser(description="Test YumFu storybook generation")
    parser.add_argument("--user-id", default="1309815719", help="User ID")
    parser.add_argument("--universe", default="warrior-cats", help="Game universe")
    
    args = parser.parse_args()
    
    success = test_storybook_generation(args.user_id, args.universe)
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
