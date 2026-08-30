from __future__ import annotations

import time
from typing import List, Optional


class KeyboardParser:
    """Parses one-shot keys and multi-key Gmail shortcut sequences."""

    IMMEDIATE_SINGLE_KEYS = {"?": "help", "/": "search"}
    MULTI_KEY_LOOKUP = {
        "gi": "gi",
        "gs": "gs",
        "gb": "gb",
        "gt": "gt",
        "gd": "gd",
        "ga": "ga",
        "gc": "gc",
        "gk": "gk",
        "gf": "gf",
        "gl": "gl",
        "gn": "gn",
        "gp": "gp",
        "*a": "*a",
        "*n": "*n",
        "*r": "*r",
        "*u": "*u",
        "*s": "*s",
        "*t": "*t",
    }
    SINGLE_KEY_RETURNABLE = {"?", "/", "z", "o", "u", "j", "k", "n", "p", "c", "d", "r", "a", "f", "e", "#", "!", "m", "y", "s", "_", "+", "-", "b", "x", ".", "v", "l", ",", ";", ":", "[", "]", "{", "}"}

    def __init__(self, timeout_seconds: float = 0.25) -> None:
        self.timeout_seconds = timeout_seconds
        self._sequence: List[str] = []
        self._last_event = time.monotonic()

    def feed(self, key: str, shifted: bool = False) -> Optional[str]:
        if key is None:
            return None

        key_text = str(key).strip()
        if not key_text:
            return None

        if shifted:
            token = f"Shift + {key_text.lower()}"
            self._sequence = [token]
            self._last_event = time.monotonic()
            return token

        normalized = key_text.lower()
        if normalized in {"shift", "ctrl", "alt"}:
            return None

        if normalized in self.IMMEDIATE_SINGLE_KEYS:
            self.reset()
            return self.IMMEDIATE_SINGLE_KEYS[normalized]

        if not self._sequence:
            self._sequence.append(normalized)
            self._last_event = time.monotonic()
            return None

        self._sequence.append(normalized)
        self._last_event = time.monotonic()
        return None

    def get_result(self) -> Optional[str]:
        if not self._sequence:
            return None

        if len(self._sequence) == 1 and self._sequence[0].startswith("Shift + "):
            result = self._sequence[0]
            self.reset()
            return result

        current = "".join(self._sequence)
        if current in self.MULTI_KEY_LOOKUP:
            result = self.MULTI_KEY_LOOKUP[current]
            self.reset()
            return result

        if len(self._sequence) == 1 and self._sequence[0] in self.SINGLE_KEY_RETURNABLE:
            result = self._sequence[0]
            self.reset()
            return result

        if time.monotonic() - self._last_event > self.timeout_seconds:
            self.reset()
            return None

        return None

    def current_sequence(self) -> List[str]:
        return list(self._sequence)

    def reset(self) -> None:
        self._sequence.clear()
        self._last_event = time.monotonic()
