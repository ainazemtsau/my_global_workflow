RESULT s-solmax-zaratustra-health-card-hygiene-repair-034 (call: none — owner instruction in chat 2026-08-14)
direction: solmax   play: repair
node: g-zara-health-vertical

outcome: |
  Two card-hygiene defects left by the shape leg 033 (commit de75d9ed) are gone, and
  nothing else changed. The node card's two head pointers now resolve to a card that
  exists, and the closed shape CALL now says what happened to it.

  1. `g-zara-health-vertical` head fields `appetite` and `kill_by` both ended with
     «полный текст в bet-g-zara-health-1». No such card exists — the bet card written
     by that same leg is `bet-g-zara-health-vertical`, and it must keep that name
     because `now set --field bet` validates a card named exactly `bet-<node-id>`
     (osctl.py:711, the FRICTION 033 itself recorded). So the pointer was the wrong
     half: the node card was corrected, not the bet card renamed.
  2. `cards/closed/c-solmax-zaratustra-health-shape-031.md` sat in `closed/` carrying
     `status: ready`. Corrected to `status: closed`, matching its two siblings in the
     same folder (`...converge-verify-030`, `...converge-repair-029`).

  Neither change touches meaning. The appetite text, the kill_by date and thresholds,
  the CALL's goal/context/boundaries and every journal line are byte-unchanged; only
  the referent of a pointer and one lifecycle field moved.

evidence: |
  - Defect 1, before: `live/solmax/cards/g-zara-health-vertical.md` lines 9-10 read
    `appetite: ... — полный текст в bet-g-zara-health-1` and
    `kill_by: ... — полный текст в bet-g-zara-health-1`.
    `grep -rn 'bet-g-zara-health-1' live/` returned exactly those two lines and no
    card by that id; `ls live/solmax/cards/` and `cards/closed/` hold exactly one bet
    card, `bet-g-zara-health-vertical.md` (`id: bet-g-zara-health-vertical`).
  - Defect 2, before: `cards/closed/c-solmax-zaratustra-health-shape-031.md` carried
    `status: ready`; `cards/closed/c-solmax-zaratustra-health-converge-verify-030.md`
    and `...converge-repair-029.md` both carry `status: closed`.
  - Cause of defect 2, re-derived first-hand rather than assumed: `cmd_card_close`
    sets the field only when `--status` is passed (`if a.status: head["status"] = ...`,
    osctl.py:797), so closing without it leaves the previous value. The doctor check
    at osctl.py:1143 flags a closed card whose status is not `done|dropped` ONLY for
    `_kind` in ("task", "node") — a `call` card is exempt, which is why nothing caught
    it. This is residue the tool tolerates, not a rule violation; it is corrected here
    for convention, and the tool gap is filed as FRICTION below.
  - Both defects were found by the writer leg that resolved RESULT 033 as a replay
    (history/2026-08-13-s-solmax-zaratustra-health-shape-033.md already saved, apply
    already committed as de75d9ed), reported to the owner, and fixed on his
    instruction in the same chat turn.
  - After: both head fields end `— полный текст в bet-g-zara-health-vertical`, which
    resolves; the closed CALL card reads `status: closed`. Values are 95 and 89
    characters, under the 120-character head limit (osctl.py:393).

state_changes: |
  - live/solmax/cards/g-zara-health-vertical.md: head field `appetite` — trailing
    referent `bet-g-zara-health-1` -> `bet-g-zara-health-vertical`. Rest of the value
    unchanged. Node-card hygiene trim, G9 mark below.
  - live/solmax/cards/g-zara-health-vertical.md: head field `kill_by` — same trailing
    referent corrected the same way. Rest of the value, including the date 13.09.2026
    and the five-threshold wording, unchanged.
  - live/solmax/cards/closed/c-solmax-zaratustra-health-shape-031.md: head field
    `status` ready -> closed, edited in place with `card set --closed` (the card stays
    closed; it is not reopened). No other field and no block touched.
  - Save this RESULT to
    history/2026-08-14-s-solmax-zaratustra-health-card-hygiene-repair-034.md and
    append the log line to the journal of g-zara-health-vertical. The closed CALL card
    receives no journal line: `osctl leg close` resolves `--id` through `live_only`
    (osctl.py:893) and refuses closed cards by design.
  - NOT changed: NOW.md, CHARTER.md, the bet card, all seven task cards, the open CALL
    card c-solmax-zaratustra-health-context-033, work/, knowledge/, the frozen WHAT,
    every history file including the 033 receipt, and every other direction. No card
    created, none closed, none reopened, no CALL issued, no status of live work moved.

captures:
  - 'The 033 receipt in history/ keeps the old wording of these two pointers, as it
    must — a saved RESULT is the leg''s immutable record and is never edited to match
    later repairs. The correction lives in this leg''s receipt and in the card.'
  - 'An amended copy of RESULT 033 was pasted after the apply had already been
    committed; it differed from the saved receipt only in prose density plus one
    correction (task `kind` lives in the bet''s `## tasks` table, not in card heads —
    which matches what was actually applied). It was ruled a replay, no mutation, and
    the committed receipt was deliberately NOT overwritten.'

decisions_needed: []

owner_approved: |
  2026-08-14 — the owner authorized both edits with his exact words, in reply to a
  message that named each defect, its current wrong value and the correct one:
  «почини обе строки в ближайшей ноге».
  This is the G9 token for the node-card head-field change. It approves the exact
  artifact: the two pointer strings on g-zara-health-vertical and the status field on
  the closed shape-031 CALL card — nothing wider. No node-card semantics, no CHARTER
  line and no bet content were changed under it.

play_check:
  - 'step 1 name the contradiction: two lines. (a) The node card points at
    bet-g-zara-health-1, which does not exist; the bet is bet-g-zara-health-vertical.
    (b) A CALL card in closed/ carries status ready, which its own folder contradicts.'
  - 'step 2 reconstruct: newest-first. Commit de75d9ed (the 033 apply) introduced both
    values; the saved receipt history/2026-08-13-...-shape-033.md declares the head
    fields as "one-line pointers into the bet card", so the applied string missed the
    declared intent rather than expressing a different one. Artifacts outrank logs
    here: the bet card id on disk, the grep for the dangling id, the sibling closed
    cards and osctl.py:797/1143 were all read first-hand this leg. Inventory
    unchanged: one active bet (g-zara-health-vertical), seven tasks (one active, six
    open), one open CALL (c-solmax-zaratustra-health-context-033), no tracks, no
    pending decision, no open issue.'
  - 'step 3 propose corrected state: three field edits, one reason each, recorded in
    state_changes. Nothing removed, nothing retired, nothing superseded, no card
    closed or reopened — so the Removal boundary is not engaged at all. Under the play
    these are hygiene (dangling pointers, schema-shape), the class the play names as
    needing no owner permission; the G9 mark is carried anyway because the target is a
    node card.'
  - 'step 4 confirm (owner): the batched change was shown to him as the exact two
    defects with current and correct values before any write, and he answered «почини
    обе строки в ближайшей ноге». Applied only after those words. His "ближайшая нога"
    could not be honoured literally and he was told why: the standing frontier CALL is
    play work, and the adapter rejects node-card edits from work|guide, so the nearest
    LAWFUL carrier is this repair leg, run before that CALL is dispatched.'
  - 'step 5 friction: one line filed below. Not fixed here — repair does not edit os/**.'

friction:
  - 'osctl `card close` without `--status` silently leaves the card''s previous live
    status (here `ready`) on a card that has moved to closed/, and the `doctor` check
    that would catch it is scoped to `_kind` task|node (osctl.py:1143), so a closed
    `call` card can read `ready` indefinitely with nothing to flag it. Second
    occurrence of a status/location mismatch in this direction; if it recurs, it is a
    MAINTENANCE REQUEST for either a default status on close or widening the doctor
    check to call cards.'

log: - 2026-08-14 — гигиена карточек после ноги 033 по прямому указанию владельца «почини обе строки в ближайшей ноге»: указатели `appetite` и `kill_by` на карточке узла вели на несуществующий `bet-g-zara-health-1` и теперь ведут на реальный `bet-g-zara-health-vertical`, а закрытый наряд shape-031 получил `status: closed` вместо остатка `ready` от закрытия без `--status`; ни одного смыслового поля, ни одной живой карточки и ни одной квитанции не тронуто, причина остатка найдена в osctl.py:797/1143 и вынесена во FRICTION.

next: |
  return-to-owner — this repair issues no CALL. The direction's frontier is unchanged
  and still the pre-existing c-solmax-zaratustra-health-context-033 (session, play
  work, for t-health-context, status ready).
END_OF_FILE: live/solmax/history/2026-08-14-s-solmax-zaratustra-health-card-hygiene-repair-034.md
