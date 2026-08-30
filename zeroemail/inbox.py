from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class InboxState:
    folders: dict[str, list[str]] = field(default_factory=lambda: {
        "inbox": [],
        "starred": [],
        "snoozed": [],
        "sent": [],
        "drafts": [],
        "all-mail": [],
        "contacts": [],
    })
    selected: list[str] = field(default_factory=list)
    read: set[str] = field(default_factory=set)
    starred: set[str] = field(default_factory=set)
    labels: dict[str, list[str]] = field(default_factory=dict)
    history: list[dict] = field(default_factory=list)

    def add_thread(self, thread_id: str, folder: str = "inbox") -> None:
        self.folders.setdefault(folder, []).append(thread_id)
        self.history.append({"action": "add", "thread": thread_id, "folder": folder})

    def archive(self, thread_id: str) -> None:
        if thread_id in self.selected:
            self.selected.remove(thread_id)
        self.history.append({"action": "archive", "thread": thread_id})

    def undo(self) -> Optional[dict]:
        if not self.history:
            return None
        return self.history.pop()

    def star(self, thread_id: str) -> None:
        if thread_id in self.starred:
            self.starred.remove(thread_id)
        else:
            self.starred.add(thread_id)
        self.history.append({"action": "star", "thread": thread_id})

    def mark_read(self, thread_id: str, value: bool = True) -> None:
        if value:
            self.read.add(thread_id)
        else:
            self.read.discard(thread_id)
        self.history.append({"action": "read", "thread": thread_id, "value": value})

    def select(self, thread_id: str) -> None:
        if thread_id not in self.selected:
            self.selected.append(thread_id)
        self.history.append({"action": "select", "thread": thread_id})

    def clear_selection(self) -> None:
        self.selected.clear()
        self.history.append({"action": "clear_selection"})
