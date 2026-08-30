from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Sequence


@dataclass(frozen=True)
class Shortcut:
    id: str
    notation: str
    category: str
    description: str
    level: int
    learns: str | None = None


SOURCE_SHORTCUTS = [
    ("help", "?", "general", "Open shortcut help", 1),
    ("search", "/", "general", "Search mail", 1),
    ("undo", "z", "general", "Undo last action", 1),
    ("open", "o", "general", "Open conversation", 1),
    ("back", "u", "general", "Back to thread list", 1),
    ("older", "j", "navigation", "Older conversation", 2),
    ("newer", "k", "navigation", "Newer conversation", 2),
    ("next_message", "n", "navigation", "Next message in conversation", 2),
    ("prev_message", "p", "navigation", "Previous message in conversation", 2),
    ("inbox", "gi", "navigation", "Go to inbox", 2),
    ("starred", "gs", "navigation", "Go to starred", 2),
    ("snoozed", "gb", "navigation", "Go to snoozed", 2),
    ("sent", "gt", "navigation", "Go to sent", 2),
    ("drafts", "gd", "navigation", "Go to drafts", 2),
    ("all_mail", "ga", "navigation", "Go to all mail", 2),
    ("contacts", "gc", "navigation", "Go to contacts", 2),
    ("tasks", "gk", "navigation", "Go to tasks", 2),
    ("filters", "gf", "navigation", "Go to search filters", 2),
    ("labels", "gl", "navigation", "Go to labels", 2),
    ("next_page", "gn", "navigation", "Next page", 2),
    ("prev_page", "gp", "navigation", "Previous page", 2),
    ("compose", "c", "compose", "Compose", 3),
    ("compose_tab", "d", "compose", "Compose in a new tab", 3),
    ("reply", "r", "compose", "Reply", 3),
    ("reply_all", "a", "compose", "Reply all", 3),
    ("forward", "f", "compose", "Forward", 3),
    ("reply_new_window", "R", "compose", "Reply in a new window", 3),
    ("reply_all_new_window", "A", "compose", "Reply all in a new window", 3),
    ("forward_new_window", "F", "compose", "Forward in a new window", 3),
    ("archive", "e", "thread_actions", "Archive", 4),
    ("delete", "#", "thread_actions", "Delete", 4),
    ("spam", "!", "thread_actions", "Report spam", 4),
    ("mute", "m", "thread_actions", "Mute conversation", 4),
    ("remove_label", "y", "thread_actions", "Remove label", 4),
    ("star", "s", "thread_actions", "Toggle star", 4),
    ("mark_read", "Shift + i", "thread_actions", "Mark as read", 4),
    ("mark_unread", "Shift + u", "thread_actions", "Mark as unread", 4),
    ("mark_unread_here", "_", "thread_actions", "Mark unread from here", 4),
    ("important", "+", "thread_actions", "Mark as important", 4),
    ("not_important", "-", "thread_actions", "Mark as not important", 4),
    ("snooze", "b", "thread_actions", "Snooze", 4),
    ("select", "x", "selection", "Select conversation", 5),
    ("select_all", "*a", "selection", "Select all", 5),
    ("deselect_all", "*n", "selection", "Deselect all", 5),
    ("select_read", "*r", "selection", "Select read", 5),
    ("select_unread", "*u", "selection", "Select unread", 5),
    ("select_starred", "*s", "selection", "Select starred", 5),
    ("select_unstarred", "*t", "selection", "Select unstarred", 5),
    ("more_actions", ".", "menus", "Open more actions menu", 5),
    ("move_to", "v", "menus", "Open move to menu", 5),
    ("label_as", "l", "menus", "Open label as menu", 5),
    ("toolbar_focus", ",", "menus", "Move focus to toolbar", 5),
    ("expand_all", ";", "conversation", "Expand all", 6),
    ("collapse_all", ":", "conversation", "Collapse all", 6),
    ("remove_label_next", "[", "advanced_navigation", "Remove label and go to next", 6),
    ("remove_label_prev", "]", "advanced_navigation", "Remove label and go to previous", 6),
    ("archive_next", "{", "advanced_navigation", "Archive and go to next", 6),
    ("archive_prev", "}", "advanced_navigation", "Archive and go to previous", 6),
]

SHORTCUTS = [
    Shortcut(id=shortcut_id, notation=notation, category=category, description=description, level=level)
    for shortcut_id, notation, category, description, level in SOURCE_SHORTCUTS
]


def validate_registry(source_commands: Sequence[tuple[str, str, str, str, int]]) -> list[str]:
    seen_ids: set[str] = set()
    seen_notations: set[str] = set()
    missing: list[str] = []

    for shortcut_id, notation, _, _, _ in source_commands:
        if shortcut_id in seen_ids:
            missing.append(f"duplicate-id:{shortcut_id}")
        seen_ids.add(shortcut_id)

        if notation in seen_notations:
            missing.append(f"duplicate-notation:{notation}")
        seen_notations.add(notation)

    return missing


def get_shortcut_by_notation(notation: str) -> Shortcut | None:
    for shortcut in SHORTCUTS:
        if shortcut.notation == notation:
            return shortcut
    return None


def get_shortcuts_for_level(level_number: int) -> list[Shortcut]:
    return [shortcut for shortcut in SHORTCUTS if shortcut.level == level_number]
