# ZeroEmail Tech Stack

## Runtime

- **Language:** Python 3.11 or newer, with the exact supported version recorded when the project is initialized.
- **Game framework:** Pygame Zero (`pgzero`) for the window, draw loop, event handling, sprites, and audio.
- **Operating model:** Offline, single-player, desktop game. No account, server, network request, or real Gmail integration.
- **Standard library:** Prefer `dataclasses`, `enum`, `json`, `pathlib`, `typing`, and `unittest` before adding dependencies.

## Proposed structure

```text
zeroemail.py              # Pygame Zero entry point and lifecycle wiring
zeroemail/
  models.py                # Messages, threads, folders, levels, player progress
  shortcut_registry.py     # Canonical shortcut definitions and learning metadata
  input.py                 # Key-sequence recognition and command dispatch
  inbox.py                 # Deterministic inbox state and message actions
  levels.py                # Level data, objectives, unlocks, and mastery checks
  story.py                 # Story-critical content and narrative progression
  screens.py               # Menu, inbox, conversation, pause, results, settings
  persistence.py           # Versioned local JSON save data
  achievements.py          # Achievement definitions and unlock evaluation
  content/                 # Level, message, and character data
assets/
  images/
  sounds/
tests/                     # Focused unit and smoke tests
requirements.txt           # Runtime dependency pin or compatible range
README.md                  # Installation and run instructions
```

The final module names may change during the vertical slice, but ownership boundaries should remain explicit: game state must not be hidden inside drawing code, and shortcut meanings must have one canonical registry.

## Input and shortcut model

The game must support single keys, shifted symbols, and multi-key sequences such as `gi`, `*a`, `[`, and `{`. Input handling should distinguish a command sequence from ordinary text entry, provide a short sequence timeout, and expose a testable parser independent of Pygame Zero.

Shortcut definitions should include the displayed notation, command identifier, level introduction, description, whether the command changes state, and whether it is eligible for mastery scoring. The complete source list is `spec/shortcuts.md`; no command should be silently invented or omitted.

## Content and assets

Level content should be data-driven where practical so messages, objectives, and shortcut assignments can be reviewed without editing rendering logic. Initial art can use simple original shapes, typography, and locally stored assets. Audio is optional during the first vertical slice and must be original, licensed, or replaced by silence during development.

## Persistence

Save data should be local JSON under an application-specific user data directory, not in the repository and not beside source files by default. The save format must include a schema version and tolerate a missing or older file. A save contains campaign progress, learned shortcuts, mastery statistics, achievements, settings, and side-quest status. Corrupt data must fail gracefully with a recoverable reset path.

## Testing and quality

- Unit-test shortcut parsing, sequence timing, command dispatch, inbox mutations, undo, progression, mastery scoring, and save migration.
- Add a smoke test for launching the main state and completing a minimal level fixture.
- Keep level content validation separate from rendering tests: verify that every shortcut is assigned and every objective references valid content.
- Use deterministic fixtures and avoid timing-dependent tests where a fake clock is sufficient.
- Run formatting and static checks once tooling is selected; do not add a formatter solely to reformat unrelated files.

## Accessibility and UX constraints

Keyboard-only play is required. Important states must have readable contrast, a non-color-only signal, clear focus indication, adjustable text size where feasible, and feedback that does not depend on sound. The game should support pause, reduced or disabled animation, volume controls, and a shortcut reference screen.

## Run and packaging policy

The repository must provide a short `README.md` with virtual-environment setup, dependency installation, and the command to launch the game. The first supported path is a developer checkout running Python locally; a later packaging step may create a platform-specific executable. Any packaging tool must preserve offline operation and include required assets.
