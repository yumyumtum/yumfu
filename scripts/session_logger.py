#!/usr/bin/env python3
"""
Session Logger for YumFu
Tracks gameplay conversations and events for storybook generation.

Usage:
    from scripts.session_logger import SessionLogger
    
    logger = SessionLogger(user_id, universe)
    logger.log_event("Tumpaw meets Firestar", image="tumpaw-firestar.png")
    logger.log_dialogue("Firestar", "Welcome, young apprentice!")
    logger.save()
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Optional


class SessionLogger:
    def __init__(self, user_id: str, universe: str, session_id: str = None):
        self.user_id = user_id
        self.universe = universe
        self.session_id = session_id or datetime.now().strftime("%Y%m%d-%H%M%S")
        
        # Paths
        self.base_path = Path.home() / "clawd/memory/yumfu"
        self.session_dir = self.base_path / "sessions" / universe / f"user-{user_id}"
        self.session_file = self.session_dir / f"session-{self.session_id}.jsonl"
        
        # Create directories
        self.session_dir.mkdir(parents=True, exist_ok=True)
        
        # Session data
        self.events = []
        self.start_time = datetime.now().isoformat()
        
    def log_event(self, event: str, image: Optional[str] = None, metadata: dict = None):
        """Log a story event"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "type": "event",
            "content": event,
            "image": image,
            "metadata": metadata or {}
        }
        self.events.append(entry)
        self._append_to_file(entry)
    
    def log_dialogue(self, speaker: str, text: str, image: Optional[str] = None):
        """Log character dialogue"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "type": "dialogue",
            "speaker": speaker,
            "content": text,
            "image": image
        }
        self.events.append(entry)
        self._append_to_file(entry)
    
    def log_choice(self, choice: str, options: list):
        """Log player choice"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "type": "choice",
            "chosen": choice,
            "options": options
        }
        self.events.append(entry)
        self._append_to_file(entry)
    
    def log_stat_change(self, stat: str, old_value, new_value):
        """Log attribute changes"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "type": "stat_change",
            "stat": stat,
            "old": old_value,
            "new": new_value,
            "change": new_value - old_value
        }
        self.events.append(entry)
        self._append_to_file(entry)
    
    def _append_to_file(self, entry: dict):
        """Append entry to JSONL file"""
        with open(self.session_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    
    def save(self):
        """Finalize session log"""
        summary = {
            "user_id": self.user_id,
            "universe": self.universe,
            "session_id": self.session_id,
            "start_time": self.start_time,
            "end_time": datetime.now().isoformat(),
            "event_count": len(self.events)
        }
        
        summary_file = self.session_dir / f"session-{self.session_id}-summary.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        return self.session_file


def get_current_session(user_id: str, universe: str) -> Optional[SessionLogger]:
    """Get or create current session logger"""
    # Check if there's an active session in the last 2 hours
    session_dir = Path.home() / "clawd/memory/yumfu/sessions" / universe / f"user-{user_id}"
    
    if not session_dir.exists():
        return SessionLogger(user_id, universe)
    
    # Find most recent session
    sessions = sorted(session_dir.glob("session-*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
    
    if not sessions:
        return SessionLogger(user_id, universe)
    
    # Check if most recent is still active (within 2 hours)
    latest = sessions[0]
    age_hours = (datetime.now().timestamp() - latest.stat().st_mtime) / 3600
    
    if age_hours < 2:
        # Resume existing session
        session_id = latest.stem.replace("session-", "")
        return SessionLogger(user_id, universe, session_id=session_id)
    else:
        # Start new session
        return SessionLogger(user_id, universe)
