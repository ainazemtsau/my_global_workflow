# Play: day

Purpose: be the owner's daily strategic adviser without creating a second plan. The chat derives a complete current view, helps adapt it, and records nothing until the owner explicitly says to save.

Reads: CHARTER.md, TREE.md, NOW.md, recent LOG.md, due issue evidence, and knowledge entries whose `read_by` names day/current planning.
Writes after explicit save only: NOW.md, LOG.md, and issued CALL artifacts. It never writes CHARTER.md or TREE.md.

## Steps

1. **Refresh reality** — reread fresh Git. Resolve the global target and hard dates, roadmap, active objective if any, future objectives, current tasks/lanes, unresolved issues/decisions, recent outcomes, and the stored direction forecast. Follow evidence pointers only where they can change today's advice; never bulk-load history.
2. **Derived brief** — explain in plain Russian what changed since the previous working day, where the direction stands, what is or is not on plan, the important evidence and problems, and the current chance of the dated target. `no_basis` is an honest forecast. Do not expose ids, packet/status labels, empty fields, or a fixed questionnaire.
3. **Advise** — recommend one focus for today and 0..N collision-free starts. Every non-recurring start must serve the active bet; without a bet, recommend the correct planning route instead of launching legacy work. Name why this is the best move, what is deliberately not being done, and which event would change the advice.
4. **Discuss** — answer, challenge assumptions, compare alternatives and revise the proposed day plan in chat. This remains read-only. Conversation memory may support the discussion but never overrides freshly read state.
5. **Save boundary (owner)** — only exact owner words such as `сохрани`, `запиши` or `запускай` authorize the agreed delta. Cite those words in `play_check`. Save only explicit issue/forecast/decision or launch-state changes, bounded CALLs inside the active objective, or — when `bet: null` — one untracked planning/review/repair CALL. Mission → frame; roadmap → map; objective activation → KERNEL §2 readiness router; objective stop/change → review; state contradiction → repair; OS defect → maintenance. Issue no foreign strategic change.
6. **Close** — a saved leg emits one RESULT, then writer apply/commit. A later owner turn may start another fresh day leg in this physical chat. `закрываем день` ends the chat; unsaved discussion stays unsaved.

## Done when

The owner has a truthful, detailed operating view and a recommended next move; no state changed without explicit save words, and any saved delta is owned by the correct play.

## Notes

- The dashboard is the chat response, derived each time; no daily file or HTML mirror is created.
- Forecast is not task-completion percent and never rises by ritual.
- An urgent unrelated problem enters the issue register; it does not silently become today's second objective.

END_OF_FILE: os/plays/day.md
