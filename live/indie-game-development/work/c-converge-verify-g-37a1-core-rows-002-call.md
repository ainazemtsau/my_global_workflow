CALL c-converge-verify-g-37a1-core-rows-002
to: session
direction: indie-game-development
play: converge-verify
node: g-37a1
verify_target: build
goal: |
  RERUN STEP 3, NARROWLY, ON WHAT THE REPAIR CHANGED — and on nothing else. The first run of step 3
  FAILED `work/converge-g-37a1-core-rows.md` with sixteen findings F1–F16
  (`history/2026-07-28-s-converge-verify-g-37a1-core-rows-001.md`). The repair leg
  `s-converge-g-37a1-core-rows-repair-001` resolved all sixteen inside the named sections and filled
  nothing else. Your job is to try to BREAK the repairs: did each one actually close its finding, and
  did any of them break something that was previously sound?
context: |
  THIS IS STILL STEP 3 OF THE OWNER'S OWN SIX-STEP ROUTE (`NOW.md` `d-post-verify-route-001`), which
  no leg may reorder without his words. Steps 1, 2 and 4 are COMPLETE. Step 5 — his ladder verdict —
  still waits on step 3 passing. This is not a seventh step: it is the same step 3, rerun on a
  repaired artifact, exactly as `os/plays/converge-verify.md` step 4 routes a build FAIL.

  READ, in this order:
  - `history/2026-07-28-s-converge-g-37a1-core-rows-repair-001.md` — the repair RESULT: what each of
    the sixteen findings resolved to, the two judgment calls it made, and what it deliberately did
    NOT fill.
  - `live/indie-game-development/work/converge-g-37a1-core-rows.md` — the target. Everything the
    repair touched is marked in place with its finding number and the date 2026-07-28.
  - `history/2026-07-28-s-converge-verify-g-37a1-core-rows-001.md` — the sixteen findings as
    originally stated, so you can check each repair against the charge it answers, PLUS the seven
    findings that were REFUTED in-leg and the four hazards recorded as CONFIRMATIONS.
  - `live/indie-game-development/TREE.md` `g-37a1` — the fifteen criteria, his verdict on exact text.
  - `live/indie-game-development/work/core-requirements-g-37a1.md` — the sixteen live lines, the
    NOT-core list and the settings register.

  Do NOT read `history/2026-07-28-s-converge-g-37a1-core-rows-001.md` (the original converge's
  reasoning) — the play forbids the verifier reading the deciding session's reasoning. The repair
  RESULT is a different thing and you must read it: it is the claim you are attacking.
boundaries: |
  NARROW SCOPE. Attack only what the repair changed, plus anything the repair may have broken
  elsewhere. In scope: §GLOSSARY (the two new terms «уровень» and «состояние захода», the
  re-marking of «вечная лаборатория» as PARTLY signed, the narrowing of «спорное число», the
  precision added to «заход»); §RULES in full (it went from eleven rules to fifteen and gained a
  three-part pass rule); §KNOBS in full (split into RIG knobs and LEVEL-AUTHORING inputs); §WHAT's
  criteria 11, 12 and 14 rows, its corrected coverage arithmetic and its two new blocks (the machine
  budget, the acceptance labour); §SEAM's withdrawn completeness claim and new seam 5; §SIGNOFF's
  corrected term count; and ROWS 1, 3, 5, 6, 9, 10, 12, 13, 14, 15, 16, 17.

  OUT OF SCOPE and not to be re-opened: §OWNER, §ORACLE and §BUILD-CLOSES-BETTER, which the repair
  did not touch; ROWS 2, 4, 8 and 11, which it did not touch; and ROW 7, retired in place with its
  number kept. The seven findings the first run REFUTED and the four it recorded as CONFIRMATIONS
  must not be re-raised — they are listed by name in its receipt.

  NOT REOPENABLE, on his exact words: passability is deleted; there are no sinks; the way up is made
  by the player; two gases now with liquid as headroom; breach behaviour is an EVENT whose form is a
  SETTING; there is NO value below in the core; death restarts the level in full; air refills ONLY
  at the base; the rig carries a level button, a start state and an immortality switch, all
  defaulting to off; the core has no completion condition; and the core is NOT graded on «весело».
  A finding against a CRITERION is out of scope — the card carries his `да` on exact text.

  THE SETTING RULE STILL GOVERNS: a question he turned into a knob is not an open question. No value
  is chosen anywhere in the repair for K1–K5, for air capacity, for the base's refill or for the step
  rate, and a finding that a row is incomplete because a value is unchosen is a false finding. The
  SAMPLE SIZES and PASS BARS the repair commits (six pairs at ROW 9, twelve frames at ROW 13,
  ten-plus-ten pairs at ROW 14, the bedrock/asked/absence split at §RULES) are acceptance-instrument
  parameters, not game knobs — attack whether they can fail a wrong build and pass a right one,
  never that a number was written down at all.

  Do not answer `d-air-counter-visibility-001`; it stays open. Do not manufacture an owner decision.
  Do not open a bet, a task or a track. Do not read `archive/**` or the product repository — every
  engineering fact is carried by an existing first-hand receipt of 2026-07-27 or 2026-07-28.
done_when: |
  1. Each of the sixteen repairs is checked against the finding it answers: does it CLOSE the charge,
     or restate it? Name any that does not.
  2. The two judgment calls the repair made are attacked directly, because they are the two places it
     could be wrong in a way nothing else catches.
     (a) **F11 — late-join STRUCK rather than raised with the owner.** The repair removed snapshot
     join from ROW 16 on the ground that no owner text contains it, that three of his own standing
     rules decide it, and that raising it would manufacture a decision. Attack that: is there owner
     text that requires it, and does striking it break any row, criterion or line?
     (b) **F2 — the build must ship AT LEAST TWO authored levels.** The repair derived this from
     criterion 12's «загрузка другого уровня» plus his «другой». Attack the derivation, and attack
     whether it smuggles a requirement into a set that may not gain one.
  3. Nothing the repair changed broke something previously sound. Specifically re-check: ROW 4 and
     ROW 11, which the first run called the best-formed things in the file and which the repair did
     not touch but now sit next to changed neighbours; the signed «the mark tells SIZE, not KIND»
     distinction, which ROW 13's repaired deck must now honour rather than violate; and whether the
     §KNOBS split leaves any row citing a knob that has moved out from under it.
  4. What the repair deliberately did NOT fill is confirmed as still named and still not filled:
     §ORACLE class 8 (no row states which single measurement would show the model wrong); the machine
     budget's PRICE (F15's price half); the acceptance labour's PRICE and owner (F16); the PRE-BUILD
     stretch, routed to `shape`'s appetite and `kill_by`; and criterion 11's co-op ordering clause,
     which is held by nothing and is routed to `shape` as a constraint on the bet. A finding that
     these are unfilled is a CONFIRMATION, not a defect — they are outside a converge's authority.
  5. `§SIGNOFF: converge-verify passed @ 2026-07-28` written on PASS, or named sections returned on
     FAIL.
return: |
  One `converge-verify` RESULT. On PASS: the signoff line, step 3 marked COMPLETE in
  `d-post-verify-route-001`, and the frontier handed to step 5 — the owner's ladder verdict
  (`i-engine-fit-decision-ladder`), which is an OWNER step and must be presented to him as a brief
  with options and a recommendation, never decided by a leg. On FAIL: the named sections returned to
  `converge` by one bounded CALL, exactly as the first run did.

  **TWO-STRIKES IS LIVE FOR THIS TARGET.** If a finding here repeats a finding of
  `s-converge-verify-g-37a1-core-rows-001` against the same section — the same charge, not merely
  the same section — that is the second failed correction round on one point (`os/KERNEL.md` §2), and
  the RESULT checkpoints and says so rather than issuing a third repair CALL into the same loop.
budget: one session, no owner.
surface: a FRESH chat, separate from the repair leg, from the first verification and from the
  session that wrote the rows.

disposition: |
  DISCHARGED 2026-07-28 by `s-converge-verify-g-37a1-core-rows-002`. **FAIL**, and no `§SIGNOFF` was
  written — but a different FAIL from the first. **All sixteen repairs CLOSE their charges**; not one
  was merely restated. **Both judgment calls this CALL named as the things to attack hardest
  SURVIVED:** ROW 16's late-join strike was verified first-hand against `CHARTER.md`, `TREE.md` and
  the seventeen lines (zero hits for any join clause) and gained a derivation the file lacks —
  criterion 9's full restart plus ROW 16's «both dig in the same section» entail a session-wide
  reload, so ROW 4's open multiplayer mechanism cannot re-import snapshot join; and F2's
  second-authored-level derivation holds and does not smuggle, because it makes an approved clause
  satisfiable rather than adding an obligation, which is the same discriminator that struck
  late-join. **Eight findings R1–R8 stand**, six against text the repair itself wrote (§KNOBS' split
  leaves base placement in both tables against his own settings register; §RULES' new Part 1 is
  all-or-nothing on an uncontrolled stimulus; its wrong-rule FAIL has no scope; ROW 15's row-level
  rule omits two of three scored halves; ROW 9(a) scores a two-part judgment as one binary; §WHAT's
  criterion-11 routing strengthens his clause into a bet-granularity rule and §WHAT's labour count
  omits ROW 5) and two against roll-ups this CALL's predecessor forbade the repair to touch, which
  is a scope defect of a section-scoped repair CALL rather than a repair failure. Every one is a
  one-to-three-sentence fix and none needs the owner. **KERNEL two-strikes NOT fired**, adjudicated
  in the open, with its boundary named for the next run. The four deliberately-unfilled items are
  CONFIRMED still named and still unfilled. Receipt:
  `history/2026-07-28-s-converge-verify-g-37a1-core-rows-002.md`. Successor:
  `c-converge-g-37a1-core-rows-repair-002`, with scope widened by exactly three lines in §ORACLE and
  §BUILD-CLOSES-BETTER. Step 5 still waits on step 3 by the owner's own route.

END_OF_FILE: live/indie-game-development/work/c-converge-verify-g-37a1-core-rows-002-call.md
