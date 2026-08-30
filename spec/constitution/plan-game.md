# ZeroEmail Game Plan

## Campaign rules

The main campaign has seven levels and targets approximately 55-70 minutes for a first playthrough. Each level introduces a small set of shortcuts, gives the player a low-risk practice task, then asks for the same skills under a more natural objective. The assignments below are concrete and should be adjusted only after playtesting; every command in `spec/shortcuts.md` must remain covered.

Each level contains a short context frame, a playable task, a feature hook, and a completion check. At a finer level, every level also includes a checklist of concrete actions to perform, but the instructions and feedback should come from Marta's internal dialogue rather than visible UI prompts. Sometimes the thoughts are brief and fast-paced (“now I do this…”), and sometimes they are longer reasoning lines based on email content or the player’s broader investigation plan. The dialogue is the primary guide for step-by-step progress, while the UI only supports the mechanical interaction. In addition, every shortcut introduced in a level should be exercised more than once during the task, with at least one straightforward use and one integrated use in a larger workflow.

## Level 1: First Dispatch

- **Purpose:** Establish the inbox as a working space, teach command feedback, and make undo feel like a safety net rather than a penalty.
- **Story beat:** Sofia assigns Marta the Luce di San Vito investigation; Luca sends the first worrying note, and Marta realizes the case may hinge on a single old message.
- **Shortcuts:** `?` (help), `/` (search), `z` (undo), `o`/`Enter` (open), `u` (back).
- **Main task:** Marta receives a short investigation checklist written in her own notes: search for “Luce di San Vito,” then “lantern,” then “Sofia,” then “Luca.” Each search is tied to a concrete objective, and the player must move through the inbox in a tight loop: search, open the result, read the contents, return to the thread list, then search again for the next clue. The game should include a harmless mistake such as opening the wrong thread or archiving a message by accident; the player then hears an internal line like “Oh no, I closed the wrong thing — undo,” and must recover before continuing. The final step is to find the older thread that contains the full name of the artifact and the date of the original note, then return to the inbox with the clue in hand.
- **Special features:** Guided onboarding, searchable inbox, one forgiving undo demonstration, a lightweight timer, and a replayable first-run challenge where the player tries to beat the record.
- **Level completion check:** Complete the checklist with at least two deliberate searches, two successful undos across separate mistakes, and at least two successful returns to the inbox while opening and reading the relevant clue threads before the final artifact note is accepted.
- **Target time:** 7-9 minutes.

## Level 2: The Mailbox Map

- **Purpose:** Teach movement across the broader Gmail map and make each destination feel like a deliberate place in the investigation.
- **Story beat:** Professor Rinaldi's archive note and a travel confirmation suggest the lantern was moved before the exhibition, and Marta begins to map the communication trail across multiple folders and conversations.
- **Shortcuts:** `j`/`k` (older/newer), `n`/`p` (next/prev message), `gi` (inbox), `gs` (starred), `gb` (snoozed), `gt` (sent), `gd` (drafts), `ga` (all mail), `gc` (contacts), `gk` (tasks), `gf` (filters), `gl` (labels), `gn`/`gp` (next/prev page).
- **Main task:** Marta must reconstruct the first part of the timeline by visiting several mail destinations and collecting message IDs from different places: the inbox for active mail, starred for important evidence, snoozed for deferred follow-ups, sent for outgoing messages, drafts for unfinished notes, all mail for archived history, contacts for names and aliases, and tasks or labels for remaining leads. The player has a checklist of clue locations, such as “find the old sent confirmation,” “check the starred note,” “open the archived thread,” and “return to a contact with the matching name.” The task should require both movement within a thread and movement across the mailbox, using `j`/`k` and `n`/`p` while reading, then `gi`/`gs`/`gb`/`gt`/`gd`/`ga`/`gc`/`gk`/`gf`/`gl` to jump to each destination and mark IDs on a clue board.
- **Special features:** Mailbox map overlay, clue board, page navigation with a visible section counter, and an optional score for how many destinations the player touched without opening the wrong thread twice.
- **Level completion check:** Gather at least five clues from four or more destinations, revisit at least two threads after reading them to confirm a detail, record the IDs correctly, and return to the inbox without losing the starting thread context.
- **Target time:** 8-10 minutes.

## Level 3: Correspondence Under Pressure

- **Purpose:** Teach the distinction between normal correspondence and strategic response modes, and make the player decide who should receive the message.
- **Story beat:** Giulia asks Marta not to involve the family, while Nico sends a clue from an alias, forcing Marta to choose the right write mode for each communication.
- **Shortcuts:** `c` (compose), `d` (new tab), `r` (reply), `a` (reply all), `f` (forward), `R`/`A`/`F` (new-window reply/reply-all/forward).
- **Main task:** Marta must send a series of targeted communications without using the mouse for the actual send action. The player first composes a direct message to Luca, then writes a careful reply to Giulia, then sends a reply-all to a coordination thread, and finally forwards a source email to Sofia. Several threads include identity cues: one is a one-to-one conversation, one is a group conversation where reply-all is required, and one is an evidence-sharing task where the message must be forwarded with its original content intact. The level should force the player to decide between `r` and `a`, then between `R` and `A`, and to understand that `d` and `F` are not different kinds of messages but different context-preserving workflows.
- **Special features:** Compose validation, recipient-context hints during onboarding, draft recovery, and a tone check that catches missing context rather than grammar.
- **Level completion check:** Send at least six correct messages across several threads, including at least two direct replies, two reply-all messages, and two forwards, while using both the normal and new-window variants at least once. The player must also recover or leave one draft in the correct state and complete the sequence without using the mouse for the actual compose action.
- **Target time:** 8-10 minutes.

## Level 4: Triage at Monteluce

- **Purpose:** Teach rapid, reversible thread management under competing priorities and make the inbox feel like a live queue rather than a static list.
- **Story beat:** A false trail points toward a courier, while Marta's family messages become harder to ignore, so the inbox must be sorted quickly without losing evidence.
- **Shortcuts:** `e` (archive), `#` (delete), `!` (spam), `m` (mute), `y` (remove label), `s` (star), `Shift + i`/`u` (read/unread), `_` (mark unread here), `+`/`=` (important), `-` (not important), `b` (snooze).
- **Main task:** Marta is asked to process a crowded arrival inbox in one focused sweep. The player must archive routine mail, delete obvious junk, report one suspicious sender as spam, mute a noisy thread, remove labels from old updates, star the real evidence, mark threads read or unread as needed, set importance on key messages, and snooze a follow-up that cannot be dealt with immediately. The task should be structured as a meaningful triage order: first clear the noise, then protect the evidence, then decide what needs follow-up. Every command has a role: `e` clears clutter, `#` and `!` handle junk and malicious mail, `m` reduces distraction, `y` and `s` reorganize and highlight, read-state commands flag what is active versus resolved, and `b` handles deferred work.
- **Special features:** Priority queue, action preview, undo window, and a non-punitive time-pressure meter that becomes more visible only after the player has seen the relevant commands.
- **Level completion check:** Process at least fifteen threads in a realistic triage order, using each action at least once in context and repeating the most common ones on a second pass. The inbox must end in the target state while preserving all story-critical evidence and without accidentally deleting or losing the key lead thread.
- **Target time:** 9-11 minutes.

## Level 5: The Evidence Sweep

- **Purpose:** Make batch operations feel faster than one-message-at-a-time work and connect selection actions to real investigation strategy.
- **Story beat:** Marta discovers that Nico's alias appears in a batch of harmless messages, making the family connection undeniable and forcing her to sort through many threads in one pass.
- **Shortcuts:** `x` (select), `*a`/`*n` (select/deselect all), `*r`/`*u` (read/unread), `*s`/`*t` (starred/unstarred), `.` (more actions), `v` (move to), `l` (label as), `,` (toolbar focus).
- **Main task:** Marta has to sort a mixed batch of messages by type and status: some are read, some unread, some starred, some not, and some belong to the protected story thread that must not be altered. The player begins by selecting the relevant group, then uses the selection shortcuts to target read/unread/starred content, opens the “more actions” menu for bulk operations, uses “move to” to relocate the batch, applies a label to the right set, and moves focus to the toolbar when needed. This task should be deliberately more than a toy drill: the player is deciding which conversations to organize, which to ignore, and which should remain untouched, with the protected thread as a visible danger point.
- **Special features:** Multi-select preview, label/move menus, focus indicator, and a side-quest-style evidence sorting challenge with a visible protected thread warning.
- **Level completion check:** Sort two mixed batches in sequence, selecting and acting on groups repeatedly with read/unread and starred/unstarred states, preserve the protected story thread at all times, and leave the result in the expected evidence state without accidental label or move errors.
- **Target time:** 8-10 minutes.

## Level 6: Read the Whole Story

- **Purpose:** Teach conversation-level context and advanced archive/label navigation, making the player manage a full thread rather than single messages.
- **Story beat:** The complete conversation reveals that Nico borrowed the replica lantern for a treasure hunt and that the case labels were swapped, so Marta must reconstruct the actual narrative from the thread itself.
- **Shortcuts:** `;`/`:` (expand/collapse all), `[`/`]` (remove label + next/prev), `{`/`}` (archive + next/prev).
- **Main task:** Marta must read the full story across several nested messages and then clear the case file by removing labels and archiving processed threads while moving through the investigation. The player expands the entire thread to reconstruct the chronology, collapses it when needed to reduce noise, removes labels while moving to the next or previous conversation, and archives a thread when it is processed. The task is about reading the complete narrative and keeping the workflow moving, so the player must decide whether to archive or relabel each clue thread and continue through the rest of the case without losing context.
- **Special features:** Conversation timeline, context warnings, and a reconstruction board that visually shows how a partial message created the false accusation.
- **Level completion check:** Reconstruct the message order across at least three nested threads, expand and collapse the same thread more than once, remove or archive labels in both directions across multiple conversations, and reach the correct next thread using the appropriate archive or label command without leaving the case in a broken state.
- **Target time:** 8-10 minutes.

## Level 7: The Bellafonte Finale

- **Purpose:** Integrate the full shortcut workflow and test recall, judgment, and recovery under realistic pressure.
- **Story beat:** Nico confesses, the lantern is recovered, and Marta chooses a humane story that holds everyone accountable without inventing a conspiracy.
- **Shortcuts:** Full set from `spec/shortcuts.md`; missed ones are replayed as drills before the final check.
- **Main task:** Marta must complete a full case sweep: search for the final lead, navigate across folders and threads, inspect the right history, triage the inbox, select and move evidence, compose or forward messages when needed, and restore the final evidence trail to identify the artifact's location and prepare her report. The player should be given a final checklist that follows Marta's internal reasoning rather than a static objective list, with short thoughts such as “first I search the alias,” “then I open the thread,” “I undo the bad action,” “now I move to the relevant folder,” “then I label the evidence,” and “finally I archive the old case files.” This is not a memorization challenge but a complete investigation workflow grounded in Marta's own thinking.
- **Special features:** Mixed objective chain, optional hint budget, final shortcut reference, and a mastery report based on recall, correctness, recovery, and efficiency.
- **Level completion check:** Complete the investigation in one continuous workflow, then repeat the key parts of the case sweep in a second pass to demonstrate mastery. The player must achieve a passing recall score, use every major shortcut family at least twice in context, and clear any missed shortcut drills before the final case report is accepted.
- **Target time:** 10-12 minutes.

## Difficulty and pacing

The game should prefer clear objectives and recoverable mistakes over strict failure states. Time pressure is introduced only after the player has seen the relevant commands. Optional perfect-efficiency goals provide challenge without blocking the story. Playtesting must verify that multi-key commands, shifted symbols, and selection prefixes are discoverable and physically comfortable.
