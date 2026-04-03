#!/usr/bin/env python3
"""
Session Logger for YumFu - V2
Tracks COMPLETE gameplay conversations and events for storybook generation.

Usage:
    from scripts.session_logger import log_turn, get_current_session
    
    # At the start of each game turn
    log_turn(
        user_id="1309815719",
        universe="warrior-cats",
        player_input="/yumfu look",
        ai_response="You see the ThunderClan camp...",
        image_generated="tumpaw-camp-20260403.png"
    )
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
        
        # Session metadata
        self.start_time = datetime.now().isoformat()
        
    def log_turn(self, player_input: str, ai_response: str, image: Optional[str] = None):
        """
        Log a complete game turn (player action + AI response + optional image)
        
        Args:
            player_input: What the player typed (e.g., "/yumfu look")
            ai_response: The AI's narrative response
            image: Optional image filename if generated this turn
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "type": "turn",
            "player": player_input,
            "ai": ai_response,
            "image": image
        }
        self._append_to_file(entry)
    
    def log_event(self, event: str, image: Optional[str] = None, metadata: dict = None):
        """Log a story event (location change, achievement, etc.)"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "type": "event",
            "content": event,
            "image": image,
            "metadata": metadata or {}
        }
        self._append_to_file(entry)
    
    def log_dialogue(self, speaker: str, text: str, image: Optional[str] = None):
        """Log NPC dialogue"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "type": "dialogue",
            "speaker": speaker,
            "content": text,
            "image": image
        }
        self._append_to_file(entry)
    
    def log_image(self, filename: str, description: str = ""):
        """Log an image generation"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "type": "image",
            "filename": filename,
            "description": description
        }
        self._append_to_file(entry)
    
    def _append_to_file(self, entry: dict):
        """Append entry to JSONL file"""
        with open(self.session_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    
    def finalize(self):
        """Create session summary"""
        summary = {
            "user_id": self.user_id,
            "universe": self.universe,
            "session_id": self.session_id,
            "start_time": self.start_time,
            "end_time": datetime.now().isoformat()
        }
        
        summary_file = self.session_dir / f"session-{self.session_id}-summary.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        return self.session_file


def get_current_session(user_id: str, universe: str) -> SessionLogger:
    """
    Get or create current session logger.
    Sessions expire after 2 hours of inactivity.
    """
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


def log_turn(user_id: str, universe: str, player_input: str, ai_response: str, image: Optional[str] = None):
    """
    Convenience function to log a complete turn.
    Automatically manages sessions (creates/resumes).
    
    Example:
        log_turn(
            user_id="1309815719",
            universe="warrior-cats",
            player_input="/yumfu look",
            ai_response="You see the ThunderClan camp bustling with activity...",
            image_generated="tumpaw-camp-20260403.png"
        )
    """
    logger = get_current_session(user_id, universe)
    logger.log_turn(player_input, ai_response, image)
    return logger.session_file


def log_image_only(user_id: str, universe: str, filename: str, description: str = ""):
    """
    Log an image generation (when no dialogue happens in same turn)
    """
    logger = get_current_session(user_id, universe)
    logger.log_image(filename, description)
    return logger.session_file
