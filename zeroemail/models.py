from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Message:
    id: str
    subject: str
    sender: str
    body: str
    folder: str = "inbox"
    read: bool = False
    starred: bool = False
    important: bool = False
    labels: List[str] = field(default_factory=list)
    archived: bool = False
    deleted: bool = False
    muted: bool = False
    snoozed: bool = False


@dataclass
class Thread:
    id: str
    messages: List[Message]
    folder: str = "inbox"
    read: bool = False
    starred: bool = False
    labels: List[str] = field(default_factory=list)
    archived: bool = False
    deleted: bool = False
    muted: bool = False
    snoozed: bool = False


@dataclass
class Folder:
    id: str
    name: str
    threads: List[Thread] = field(default_factory=list)


@dataclass
class Objective:
    id: str
    description: str
    required_actions: List[str] = field(default_factory=list)
    complete: bool = False


@dataclass
class Level:
    id: str
    name: str
    folder: str = "inbox"
    threads: List[Thread] = field(default_factory=list)
    objectives: List[Objective] = field(default_factory=list)
    shortcuts: List[str] = field(default_factory=list)


@dataclass
class Progress:
    current_level: str = "level-1"
    learned_shortcuts: List[str] = field(default_factory=list)
    mastery: Dict[str, int] = field(default_factory=lambda: {"success": 0, "errors": 0})
    completed_levels: List[str] = field(default_factory=list)
    notes: Dict[str, Any] = field(default_factory=dict)


DEFAULT_FOLDER_IDS = ["inbox", "starred", "snoozed", "sent", "drafts", "all-mail", "contacts"]
