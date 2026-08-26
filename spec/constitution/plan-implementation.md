# ZeroEmail Implementation Plan

The repository currently contains specifications only. Work proceeds in small, verifiable increments. The first milestone is a playable vertical slice; the second is the complete campaign; the third adds the remaining MVP extras and release polish.

## Milestone 0: Project contract

1. **Create the Python project skeleton.** Add the entry point, package directories, requirements file, README, tests directory, and asset directories. Document the supported Python version and the local launch command.
   - Depends on: nothing.
   - Deliverable: a blank Pygame Zero window launches locally.
   - Check: create a virtual environment, install dependencies, and run the documented command.

2. **Define code ownership and content conventions.** Add the initial data models and decide where level and message data live. Keep drawing, state mutation, and content separate.
   - Depends on: step 1.
   - Deliverable: importable models for messages, threads, folders, objectives, levels, and progress.
   - Check: unit tests construct a minimal inbox and level fixture.

## Milestone 1: Vertical slice

3. **Implement the shortcut registry.** Encode every command from `spec/shortcuts.md` with a stable identifier, notation, category, and learning metadata.
   - Depends on: step 2.
   - Deliverable: one canonical shortcut table.
   - Check: a validation test confirms the registry contains every source command and no duplicate identifier.

4. **Implement keyboard sequence recognition.** Support ordinary keys, shifted symbols, multi-key sequences, selection prefixes, and a short configurable timeout. Keep the parser independent of Pygame Zero.
   - Depends on: step 3.
   - Deliverable: parser that emits command identifiers or an unhandled-input result.
   - Check: unit tests cover `?`, `/`, `gi`, `*a`, `[`, `{`, shifted actions, incomplete sequences, and timeout behavior.

5. **Implement the inbox state engine.** Add deterministic threads, folders, labels, selection, read state, stars, importance, snooze, archive, delete, spam, mute, and undoable mutations.
   - Depends on: steps 2-4.
   - Deliverable: state transitions usable without rendering.
   - Check: tests verify each action and that `z` restores the previous state without losing unrelated changes.

6. **Render the inbox and conversation screens.** Add readable thread rows, message detail, focus state, status feedback, objective text, and keyboard-only navigation.
   - Depends on: step 5.
   - Deliverable: the player can view and operate a small fictional inbox.
   - Check: manually launch the game, open a thread, perform a command, observe feedback, and return to the list.

7. **Build Level 1 as a vertical slice.** Add the first story messages, tutorial prompts, objective evaluation, level completion, and shortcut learning state.
   - Depends on: steps 1-6.
   - Deliverable: First Dispatch is playable from the menu or entry point to its result screen.
   - Check: a new player can complete the level using the documented command prompts; a smoke fixture completes it without graphics assumptions.

## Milestone 2: Complete campaign

8. **Add progression and mastery tracking.** Record shortcut introduction, successful practice, recall, errors, recovery, and level results.
   - Depends on: step 7.
   - Deliverable: progress model and final assessment inputs.
   - Check: repeated command use updates statistics deterministically and a failed objective does not corrupt progress.

9. **Implement Levels 2-4.** Add navigation, communication, and triage content in the order defined in `plan-game.md`.
   - Depends on: step 8.
   - Deliverable: first half of the campaign with story transitions.
   - Check: content validation confirms every objective points to existing messages, folders, and commands.

10. **Implement Levels 5-6.** Add selection, menus, conversation controls, advanced navigation, and remediation drills.
    - Depends on: step 9.
    - Deliverable: all shortcut families are available in campaign play.
    - Check: integration tests cover batch operations, menu focus, expanded threads, and advanced archive/label movement.

11. **Implement Level 7 and the final assessment.** Create the integrated investigation, hint budget, recall scoring, completion report, and missed-shortcut drill links.
    - Depends on: steps 8-10.
    - Deliverable: complete seven-level campaign.
    - Check: a deterministic end-to-end fixture exercises every shortcut at least once and produces a passing result.

12. **Review narrative continuity.** Add all story-critical content and verify that character names, relationships, artifact details, and level beats match `plan-context.md`.
    - Depends on: steps 9-11.
    - Deliverable: coherent story from assignment to Bellafonte resolution.
    - Check: manual campaign pass confirms story mail is recoverable and filler mail cannot block progress.

## Milestone 3: MVP extras and release

13. **Add menu, pause, restart, settings, and shortcut reference.** Make navigation consistent across all screens.
    - Depends on: step 7; full integration after step 11.
    - Deliverable: complete navigation shell and contextual help.
    - Check: keyboard-only smoke pass from launch through pause, reference, restart, and quit.

14. **Add versioned local saves.** Save at safe checkpoints, load progress, migrate older schemas, and provide reset/recovery flows.
    - Depends on: step 8 and the navigation shell.
    - Deliverable: reliable resume behavior without external services.
    - Check: tests cover missing, valid, old-version, and corrupt save files.

15. **Add achievements and side quests.** Reuse the same inbox engine, shortcut registry, progression, and objective evaluator.
    - Depends on: steps 8, 11, and 14.
    - Deliverable: achievements, four initial side quests, replay, and practice mode.
    - Check: complete one side quest, unlock one achievement, replay a level, and confirm campaign state remains intact.

16. **Add assets, audio, accessibility, and presentation polish.** Include local assets, volume controls, high contrast, text sizing, reduced motion, focus indication, and non-audio feedback.
    - Depends on: stable screens and content.
    - Deliverable: polished, readable, keyboard-first experience.
    - Check: manual accessibility checklist at the smallest supported window size and with sound disabled.

17. **Package and document the release.** Finalize README setup, supported platforms, asset licensing notes, test commands, and an executable distribution path if practical.
    - Depends on: steps 13-16.
    - Deliverable: a fresh checkout can be installed and launched by following README instructions.
    - Check: test in a clean environment and run a complete campaign smoke pass.

## Cross-cutting rules

- Keep game state deterministic in tests and isolate real time behind a clock interface.
- Add or update focused tests with every state-changing feature.
- Validate content before launch so missing shortcuts, references, or objective targets fail clearly.
- Do not add real Gmail integration or network requirements.
- Prefer a small working slice over broad unfinished systems; each milestone must leave the repository runnable.
- Treat level shortcut assignments as provisional until playtesting, but require explicit coverage of every command before release.
