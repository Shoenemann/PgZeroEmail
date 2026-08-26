# ZeroEmail Mission

## Purpose

ZeroEmail is a short, humorous, single-player PC game that teaches players to use Gmail keyboard shortcuts through meaningful practice. The player learns by acting inside a fictional inbox, not by memorizing an isolated reference sheet.

## Player promise

By the end of the main campaign, a player who already understands basic email can triage, navigate, search, communicate, and manage conversations quickly with the complete shortcut set in `spec/shortcuts.md`.

The player also follows a light international mystery involving a famous journalist, Italian friends and family, and a missing fictional cultural artifact. Story messages provide motivation and emotional continuity; quest messages provide safe opportunities to practise.

## Audience

The primary audience is a computer-literate Gmail user who wants to become faster and more confident with keyboard-driven email work. The game assumes that the player can understand an inbox, open a conversation, write messages, but does not assume knowledge of Gmail shortcuts.

## Experience principles

1. Every new shortcut is introduced in a useful situation.
2. The inbox is simple enough to read at a glance and rich enough to reward deliberate triage.
3. Story-critical messages are clearly authored and purposeful; filler messages can be funny without obscuring the task.
4. The campaign teaches, exercises, and later recalls shortcuts rather than relying on permanent prompts.
5. Errors are reversible where possible and explain the missed action without shaming the player.
6. The main story fits in approximately one hour across seven levels.
7. Accessibility and readable feedback are part of the core experience.

## Success criteria

- A new player can launch the game using documented local instructions.
- The player can complete the seven-level campaign without external Gmail access.
- Every shortcut listed in `spec/shortcuts.md` is introduced, practised, and exercised again in the finale.
- The player can inspect progress and review every learned shortcut.
- A manual playthrough can distinguish story-critical mail from quest and humour mail.
- The game remains playable with keyboard-only interaction and clear visual feedback.

## Non-goals

The first version will not connect to a real Gmail account, send real email, require an internet connection, support multiplayer, use private email data, or attempt to reproduce the full Gmail interface.

## Product shape

The repository will contain a small offline Pygame Zero game, built around deterministic fictional inbox data, explicit level definitions, a shortcut registry, lightweight progression tracking, and local save data. Optional systems are part of the intended MVP, but the playable campaign is implemented and verified before they are layered on.
