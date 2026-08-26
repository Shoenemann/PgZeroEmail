# ZeroEmail Game Plan

## Campaign rules

The main campaign has seven levels and targets approximately 55-70 minutes for a first playthrough. Each level introduces a small set of shortcuts, gives the player a low-risk practice task, then asks for the same skills under a more natural objective. The assignments below are concrete and should be adjusted only after playtesting; every command in `spec/shortcuts.md` must remain covered.

Each level contains an inbox state, a story beat, a practical objective, a special feature, and a mastery check. Prompts may be visible during introduction and should recede during later exercises.

## Level 1: First Dispatch

- **Purpose:** Establish the fictional inbox, command feedback, undo, and the idea that shortcuts are learned through useful action.
- **Main task:** Find Marta's assignment, open the relevant thread, inspect it, and return to the inbox while clearing one harmless mistake.
- **Special features:** Guided onboarding, shortcut help overlay, searchable inbox, and a forgiving undo demonstration.
- **Story beat:** Sofia assigns Marta the Luce di San Vito investigation; Luca sends the first worrying note.
- **Unlocked:** `?`, `/`, `z`, `o` or `Enter`, `u`.
- **Exercised:** All five commands in a short inbox-and-thread loop.
- **Mastery check:** Complete the task with at least one intentional search and one successful undo.
- **Target time:** 7-9 minutes.

## Level 2: The Mailbox Map

- **Purpose:** Teach movement through conversations and mailbox destinations.
- **Main task:** Locate messages distributed across inbox, starred, snoozed, sent, drafts, all mail, and contacts, then assemble the initial timeline.
- **Special features:** Mailbox map, next/previous page navigation, and a clue board that records discovered message IDs.
- **Story beat:** Professor Rinaldi's archive note and a travel confirmation reveal the lantern moved before the exhibition.
- **Unlocked:** `j`, `k`, `n`, `p`, `gi`, `gs`, `gb`, `gt`, `gd`, `ga`, `gc`, `gk`, `gf`, `gl`, `gn`, `gp`.
- **Exercised:** Every navigation command through destination finding, conversation movement, search filters, labels, tasks, and pagination.
- **Mastery check:** Retrieve three clues from different destinations without opening the wrong thread twice.
- **Target time:** 8-10 minutes.

## Level 3: Correspondence Under Pressure

- **Purpose:** Teach composing and choosing the correct response mode.
- **Main task:** Contact Luca, reply to Giulia, reply all to a coordination thread, and forward a source message to Sofia.
- **Special features:** Compose validation, recipient-context hints during introduction, draft recovery, and a tone check that catches missing context rather than grammar.
- **Story beat:** Giulia asks Marta not to involve the family, while Nico sends an oddly specific clue from an alias.
- **Unlocked:** `c`, `d`, `r`, `a`, `f`, `R`, `A`, `F`.
- **Exercised:** Normal and new-window compose, reply, reply all, and forward variants.
- **Mastery check:** Send four messages with the correct recipients and conversation relationships, using no mouse action for the command itself.
- **Target time:** 8-10 minutes.

## Level 4: Triage at Monteluce

- **Purpose:** Teach rapid, reversible thread management under competing priorities.
- **Main task:** Process a crowded arrival inbox: archive routine mail, delete junk, report one suspicious sender, mute a noisy thread, apply or remove labels, star evidence, change read state, mark importance, and snooze a follow-up.
- **Special features:** Priority queue, action preview, undo window, and a non-punitive time-pressure meter.
- **Story beat:** A false trail points toward a courier, while Marta's family messages become harder to ignore.
- **Unlocked:** `e`, `#`, `!`, `m`, `y`, `s`, `Shift + i`, `Shift + u`, `_`, `+` or `=`, `-`, `b`.
- **Exercised:** Every thread action in a realistic triage order.
- **Mastery check:** Leave the inbox in the target state while preserving all story-critical evidence.
- **Target time:** 9-11 minutes.

## Level 5: The Evidence Sweep

- **Purpose:** Make batch operations and menus feel faster than one-message-at-a-time work.
- **Main task:** Select groups of messages by read state, star state, and type, then apply labels, move items, and operate the toolbar.
- **Special features:** Multi-select preview, label/move menus, focus indicator, and a side-quest-style evidence sorting challenge.
- **Story beat:** Marta discovers that Nico's alias appears in a batch of harmless messages, making the family connection undeniable.
- **Unlocked:** `x`, `*a`, `*n`, `*r`, `*u`, `*s`, `*t`, `.`, `v`, `l`, `,`.
- **Exercised:** Selection filters, more actions, move to, label as, and toolbar focus.
- **Mastery check:** Sort a mixed batch correctly without altering the protected story thread.
- **Target time:** 8-10 minutes.

## Level 6: Read the Whole Story

- **Purpose:** Teach conversation-level context and advanced archive/label navigation.
- **Main task:** Expand and collapse threads, remove labels while moving through evidence, and archive forward and backward through the remaining investigation.
- **Special features:** Conversation timeline, context warnings, and a reconstruction board showing how a partial message created the false accusation.
- **Story beat:** The complete thread reveals that Nico borrowed the replica lantern for a treasure hunt and that the case labels were swapped.
- **Unlocked:** `;`, `:`, `[`, `]`, `{`, `}`.
- **Exercised:** All conversation controls and advanced navigation shortcuts, plus remediation drills for earlier misses.
- **Mastery check:** Reconstruct the message order and reach the correct next thread using the appropriate archive or label command.
- **Target time:** 8-10 minutes.

## Level 7: The Bellafonte Finale

- **Purpose:** Integrate and assess the complete shortcut workflow without relying on prompts.
- **Main task:** Search, navigate, inspect, triage, select, communicate, and restore the final evidence trail to identify the artifact's location and prepare Marta's report.
- **Special features:** Mixed objective chain, optional hint budget, final shortcut reference, and a mastery report based on recall, correctness, recovery, and efficiency.
- **Story beat:** Nico confesses, the lantern is recovered, and Marta chooses a humane story that holds everyone accountable without inventing a conspiracy.
- **Unlocked:** No new commands; all commands are available.
- **Exercised:** The full list from `spec/shortcuts.md`, with at least one integrated use of every command and explicit practice for any command missed earlier.
- **Mastery check:** Complete the investigation and achieve a passing recall score. The player can replay missed command drills immediately.
- **Target time:** 10-12 minutes.

## Difficulty and pacing

The game should prefer clear objectives and recoverable mistakes over strict failure states. Time pressure is introduced only after the player has seen the relevant commands. Optional perfect-efficiency goals provide challenge without blocking the story. Playtesting must verify that multi-key commands, shifted symbols, and selection prefixes are discoverable and physically comfortable.
