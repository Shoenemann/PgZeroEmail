# ZeroEmail Extra Features Plan

All features in this document are part of the intended MVP scope, but they are implemented after the core inbox loop and campaign vertical slice. Each feature must remain subordinate to readability, shortcut practice, and the main story.

## Main menu and navigation

The main menu offers New Campaign, Continue, Level Select after unlocking, Practice Shortcuts, Side Quests, Achievements, Settings, and Quit. Locked entries explain the unlock condition without exposing story spoilers. Every screen supports keyboard navigation, visible focus, Escape to go back, and a consistent confirmation pattern for destructive actions.

The pause menu offers Resume, Shortcut Reference, Restart Level, Settings, and Return to Menu. Restarting a level restores its initial deterministic state and does not erase already learned shortcuts. Returning to the menu autosaves progress after confirmation.

## Onboarding and help

The first launch includes a short interactive orientation to the inbox, conversation view, selection state, and command feedback. The `?` shortcut opens the context-sensitive shortcut reference. The reference can be filtered by workflow and shows locked, learned, practised, and mastered states.

Hints should be layered: first name the goal, then identify the relevant workflow, then reveal the exact command. Hints never consume progress. A reduced-hint setting is available for replay and assessment.

## Progression and saves

The player profile tracks campaign completion, shortcut state, level scores, best efficiency, story flags, side-quest completion, achievements, settings, and statistics such as successful uses and recoveries. Progress is saved at level start, objective completion, level completion, and menu exit.

There should be one primary local profile in the first version, with a clear reset-progress action protected by confirmation. Save data is versioned and corrupt data produces a recovery screen rather than a crash.

## Achievements

Achievements reward learning behaviors rather than grinding. Initial achievements include:

- **First Dispatch:** complete Level 1.
- **Full Keyboard:** use every shortcut at least once.
- **Context Matters:** inspect a complete conversation before acting in Level 6.
- **Undo Is a Feature:** recover from an incorrect action with `z`.
- **Inbox Cartographer:** visit every mailbox destination in Level 2.
- **Batch Processing:** complete the Level 5 sorting objective with a multi-selection.
- **No Loose Threads:** complete the finale without leaving a required story message unresolved.
- **Bellafonte Method:** pass the final mastery check with no hint usage.

Achievement feedback must be brief, dismissible, keyboard accessible, and never obscure an active objective.

## Side quests

Side quests are optional, replayable inbox stories that practise the same commands in comic situations. They unlock after the relevant campaign level and do not alter the canonical mystery. Proposed quests include:

- **The Great Espresso Procurement:** search, label, select, and archive a chaotic café order thread.
- **A Very Small Conference:** coordinate replies, forwards, drafts, and calendar-like task messages for a conference that keeps changing rooms.
- **The Case of the Missing Umbrella:** use conversation expansion, mute, snooze, and advanced archive navigation to trace an umbrella through three owners.
- **The Museum Gift Shop Incident:** practise batch selection and importance marking while preserving a story-critical receipt.

Each side quest has a clear objective, a bronze completion threshold, a silver efficiency threshold, and a gold no-hint threshold. Side quests should reuse the shortcut registry and state engine rather than create bespoke interaction rules.

## Practice and replay

Practice Shortcuts presents isolated drills grouped by workflow: search, navigation, communication, triage, selection, conversation control, and advanced movement. Drills use synthetic messages and can be restarted instantly. The player can practise any learned command, while unlearned commands remain discoverable through the campaign.

Level replay preserves story progress but records a separate best score. A “study mode” may display the command after a short delay; assessment mode removes command prompts and reports recall accuracy.

## Settings and accessibility

Settings include music volume, effects volume, text size, high-contrast palette, reduced motion, hint verbosity, keyboard layout notes, and reset-progress controls. Visual effects must not be the sole indication of selection, success, error, unread state, importance, or achievement.

The game must remain usable with keyboard-only input, provide a focus ring, avoid flashing, pause on window focus loss when possible, and offer readable timing feedback instead of relying on sound. Text should be concise, wrapped safely, and never depend on color alone.

## Audio and presentation

Audio supports confirmation, error, transition, and achievement events, with every sound independently disableable. The first playable slice may use placeholders. Final assets must be original or appropriately licensed and stored locally. Music should not compete with reading fictional emails.

A small number of page transitions and message reveals may animate, but reduced-motion mode disables or shortens them. The visual identity should suggest an annotated journalist's notebook and an Italian travel dossier without imitating Gmail branding.

## Completion and feedback

At campaign completion, the game shows the story outcome, shortcut mastery by workflow, successful and recovered actions, achievements, and recommended drills. The player can return to the inbox, replay Level 7, open Practice Shortcuts, or quit.

The game should not grade typing speed or spelling. Efficiency scores measure appropriate command choice, unnecessary actions, and recovery, while the core completion threshold measures correct task outcomes and shortcut recall.

## Delivery order

1. Main menu, pause, restart, and basic settings are added once the first level is playable.
2. Saves, progression, and shortcut reference are added before the full campaign is content-complete.
3. Achievements and side quests are added after the campaign state model stabilizes.
4. Audio, presentation polish, accessibility checks, and packaging are completed before release.

Each feature needs a focused smoke check and must not make the main campaign dependent on optional content.
