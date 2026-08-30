from __future__ import annotations

from typing import Any

import pygame

from zeroemail.models import Level, Message, Objective, Thread


class ZeroEmailGame:
    def __init__(self) -> None:
        self.message = "ZeroEmail"
        self.level: Level | None = None
        self.current_matches: list[str] = []
        self.active_thread_id: str | None = None
        self.objective_complete = False
        self.history: list[dict[str, Any]] = []
        self.status_message = "Level 1 ready. Press ? for help."
        self._level_templates = self._build_levels()
        self.start_level("level-1")

    def _build_levels(self) -> dict[str, Level]:
        thread_1 = Thread(
            id="t-1",
            messages=[
                Message(
                    id="m-1",
                    subject="Luce di San Vito",
                    sender="sofia@example.com",
                    body="The archive note mentions the lantern from the Luce di San Vito project.",
                    folder="inbox",
                ),
            ],
            folder="inbox",
        )
        thread_2 = Thread(
            id="t-2",
            messages=[
                Message(
                    id="m-2",
                    subject="Sofia follow-up",
                    sender="luca@example.com",
                    body="Sofia asked me to check the family records before the exhibition.",
                    folder="inbox",
                ),
            ],
            folder="inbox",
        )

        level_1 = Level(
            id="level-1",
            name="First Dispatch",
            folder="inbox",
            threads=[thread_1, thread_2],
            objectives=[Objective(id="o-1", description="Find the key clue thread")],
            shortcuts=["?", "/", "z", "o", "u"],
        )
        return {"level-1": level_1}

    def start_level(self, level_id: str) -> Level:
        if level_id not in self._level_templates:
            raise ValueError(f"Unknown level: {level_id}")

        self.level = self._level_templates[level_id]
        self.current_matches = [thread.id for thread in self.level.threads]
        self.active_thread_id = None
        self.objective_complete = False
        self.history = []
        return self.level

    def search(self, query: str) -> bool:
        if self.level is None:
            return False

        q = (query or "").lower()
        matches = []
        for thread in self.level.threads:
            for message in thread.messages:
                haystack = " ".join(
                    [
                        message.subject.lower(),
                        message.body.lower(),
                        message.sender.lower(),
                    ]
                )
                if q in haystack:
                    matches.append(thread.id)
                    break

        self.current_matches = matches
        self.history.append({"action": "search", "query": q, "matches": matches})
        return bool(matches)

    def open_thread(self, thread_id: str) -> bool:
        if self.level is None:
            return False

        available = {thread.id for thread in self.level.threads}
        if thread_id not in available:
            return False

        self.active_thread_id = thread_id
        self.history.append({"action": "open_thread", "thread_id": thread_id})
        return True

    def record_mistake(self) -> None:
        self.active_thread_id = None
        self.history.append({"action": "mistake", "thread_id": None})

    def undo(self) -> bool:
        if not self.history:
            return False

        last = self.history.pop()
        if last["action"] in {"mistake", "open_thread"}:
            self.active_thread_id = None
            return True

        if last["action"] == "complete_objective":
            self.objective_complete = False
            return True

        return False

    def complete_objective(self) -> bool:
        self.objective_complete = True
        self.history.append({"action": "complete_objective"})
        return True

    def is_level_complete(self) -> bool:
        return self.level is not None and self.objective_complete

    def draw(self) -> None:
        surface = pygame.display.get_surface()
        if surface is None:
            return

        surface.fill((16, 20, 26))

        # Use Pygame's text rendering directly so the prototype works with the real runtime surface.
        font = pygame.font.SysFont(None, 36)
        title = font.render("ZeroEmail", True, (240, 240, 240))
        surface.blit(title, (30, 20))

        font_small = pygame.font.SysFont(None, 24)
        level_name = self.level.name if self.level else "No level"
        surface.blit(font_small.render(level_name, True, (170, 210, 255)), (30, 70))
        surface.blit(font_small.render(self.status_message, True, (220, 220, 220)), (30, 110))

        y = 160
        for thread in self.level.threads if self.level else []:
            label = f"{thread.id}: {thread.messages[0].subject}"
            color = (255, 220, 120) if thread.id == self.active_thread_id else (220, 220, 220)
            text = font_small.render(label, True, color)
            surface.blit(text, (30, y))
            y += 28

        if self.objective_complete:
            completed = font_small.render("Objective complete", True, (120, 255, 170))
            surface.blit(completed, (30, 340))

    def update(self) -> None:
        pass

    def handle_key(self, key: Any) -> None:
        if key is None:
            return

        key_name = str(key)
        if key_name == "?":
            self.status_message = "Help: / search, z undo, o open, u back"
        elif key_name == "/":
            self.status_message = "Search: Luce di San Vito"
        elif key_name == "z":
            self.status_message = "Undo last action."
            self.undo()
        elif key_name == "o":
            if self.level and self.level.threads:
                self.active_thread_id = self.level.threads[0].id
                self.status_message = "Opened thread t-1"
        elif key_name == "u":
            self.active_thread_id = None
            self.status_message = "Back to thread list"
        elif key_name == "RETURN":
            if self.level and self.level.threads:
                self.active_thread_id = self.level.threads[0].id
                self.status_message = "Opened thread t-1"
