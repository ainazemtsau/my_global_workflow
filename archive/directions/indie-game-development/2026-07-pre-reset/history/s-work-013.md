# RESULT — s-work-013 (g-9c41 Wave 2): owner-approved scope CUT — t-3/XL2 deferred to Wave 3 (d-t3-defer-001); t-4 is the sole remaining leg

direction indie-game-development / bet g-9c41 / Wave 2 / play work (owner-approved scope decision applied; owner present).

## outcome

- The t-3 builder PLAN surfaced a **CALL-vs-ADR fork**: ADR-0005 + ADR-0007 Decision 5 say "temperature as a SEPARATE registered layer reading gas via the inter-layer read seam = the t-3 XL2 obligation", while the CALL (c-exec-007) frames t-3 as a NEW demonstrative layer with temperature left coupled.
- **Reconciled first-hand** (this session, against the ADRs + the VERIFIED §CONTRACTS): the ADR wording is **STALE**. converge-verify Finding F2 already caught exactly this and d-tempfeedback-001 resolved it — XL2 (verified contract) = a new demonstrative layer, gas byte-identical, no core edits = **what the CALL implements**; DECOUPLING temperature so gas reads it back = the temperature→gas FEEDBACK, which the owner **deferred** (post-g-d3a8). So the CALL was on the right side; the "fork" was largely already resolved.
- **Deep technical reason decoupling can't be free now:** temperature is an INPUT to the band-solver (per-band throttle, frozen in the LOCK). Decoupling forces gas to read temperature via the committed-revision seam = a 1-tick lag → different band-split → breaks the frozen band-solver goldens + reopens the LOCK (the only alternative — a live same-tick read — breaks determinism). So the builder's "option 2 = decouple now" is OFF the table (contradicts d-tempfeedback-001 + reopens the LOCK; it is Wave-3 / g-d3a8 work).
- **Owner decision = C** (presented A-refined vs C): DEFER t-3/XL2 to Wave 3; the demo proof was contrived; prove extensibility FOR-REAL in Wave 3 with the first genuine 2nd layer (the temperature decouple + feedback). Focus this wave on t-4 (the visible 08-31 artifact). t-2 already ships temperature as a replicated plane-6, so nothing is lost.

## evidence (first-hand reconciliation)

- ADR-0005 (GasCoopGame_dev/docs/adr/ADR-0005-coarse-band-solver.md:154): "Temperature as a SEPARATE registered layer reading gas via the inter-layer read seam is the t-3 XL2 obligation, NOT t-1." — the stale phrasing.
- ADR-0007 Decision 5 (lines 130-137): "Temperature stays an INDEPENDENT layer (... a SEPARATE registered layer is the t-3 XL2 obligation), readable ... on a committed revision ... temperature stays a pure SINK; ... temperature→gas FEEDBACK (d-tempfeedback-001, post-g-d3a8)." — carries BOTH the stale "separate-layer = t-3" note AND the feedback-deferral, unreconciled.
- work/converge-g-9c41.md §CONTRACTS: XL2 = "a new layer plugs in without core edits" (line 603); Finding F2 (lines 1018-1037) caught "XL2 byte-identical vs XL1 trajectory-changing feedback"; the repair (lines 1091-1098) DISSOLVED F2 via d-tempfeedback-001 — XL2 = byte-identical demonstrative layer, feedback deferred. This is the VERIFIED, shape-consumed contract → it supersedes the downstream ADR note.
- The builder was right to escalate (refused to silently choose when CALL ⟂ ADR); the only correction is the framing — the verified contract is the truth, the ADR note is stale.

## state_changes

- NOW.md active_bet.phase: appended the 2026-06-19 s-work-013 cut line.
- NOW.md done_when #5: reworded to NAME the XL2/extensibility deferral to Wave 3 (not a silent drop; t-2's plane-6 partially evidences extensibility).
- NOW.md wave_plan: Wave 2 = t-1/t-2/t-5 done → t-4 sole leg, t-3 cut; Wave 3 gains "extensibility FOR-REAL (temperature decouple + feedback, g-d3a8)".
- NOW.md cut_list.fresh_cut_this_wave: added the t-3/XL2 cut.
- NOW.md active_tasks: t-3 → dropped (re-homed Wave 3). (t-4 unchanged = active, sole leg; t-1/t-2/t-5 done.)
- NOW.md open_calls: c-exec-007 → cancelled.
- NOW.md decision_inbox: added d-t3-defer-001 (answered, owner «C», full reconciliation + options + consequences).
- NOW.md next: replaced — RUN c-exec-008 (t-4) as the sole Wave-2 leg; Wave-3 re-homed items; owner-run residuals; push owner-gated.
- LOG.md: appended the s-work-013 line.

## captures

- A downstream product-repo ADR forward-note (ADR-0005/0007 "separate-layer = t-3 obligation") drifted from the LATER verified converge §CONTRACTS; when a builder escalates a CALL-vs-ADR fork, reconcile to the VERIFIED contract (+ the owner decisions it folds), not to the stale ADR. Correct the ADR wording home-side so it stops re-surfacing.
- Note: the owner's earlier "Выбираем A" message was a CANON-thread choice (g-d3a8 biome, s-canon-011, concurrent session), NOT this t-3/t-4 thread — confirmed by the LOG; correctly not acted on here.

## decisions_needed

- none — owner decided C; the cut is applied. (Future: Wave-3 shape frames the real extensibility/feedback leg + the ADR-wording cleanup.)

## play_check

- "1 Recite — done: restated the t-3 fork (CALL vs ADR) + the owner's ask to discuss."
- "2 Owner inputs — engineering scope decision; owner present + decided «C»."
- "3 Do the work — reconciled the fork first-hand (ADRs + verified §CONTRACTS), presented A-refined vs C with a recommendation, applied the owner-approved cut."
- "4 Self-check — verified the ADR-stale claim against the committed contract; confirmed decoupling = deferred-feedback + LOCK-reopen (not a Wave-2 thing)."
- "5 Close — RESULT; next = run c-exec-008 (t-4) as the sole Wave-2 leg; Wave-2 review when it returns."
- "NOTE (scope-cut authority): this is an owner-approved Wave-2 DE-SCOPE (cut), not a goal-retarget — the multi-wave node g-9c41 goal + XL2 are intact, only re-timed to Wave 3; a full re-shape session is not warranted."

## log

work (g-9c41/Wave2, s-work-013): owner «C» — CUT t-3/XL2 → Wave 3 (d-t3-defer-001); reconciled the CALL-vs-ADR fork first-hand (ADR wording stale; decoupling = deferred feedback + LOCK-reopen, off the table); t-3 dropped, c-exec-007 cancelled, done_when/cut_list/wave_plan updated; t-4 (c-exec-008) is the sole Wave-2 leg.

## next

RUN c-exec-008 (t-4, render terminus + REAL Dungeon Architect) in GasCoopGame as the SOLE remaining Wave-2 leg — opens with a PLAN (owner present); binds the c-exec-010 DA→geometry-derived-id gate (+ a RED derive-mismatch test). When t-4 returns → review the Wave-2 node g-9c41, then roll to Wave 3 (which now carries the REAL extensibility = temperature decouple + feedback). Full CALL → history/s-work-010.md §c-exec-008 + the s-work-012 DA addendum. Home cleanup: correct the stale ADR-0005/0007 "separate-layer = t-3 obligation" wording.

END_OF_FILE: live/indie-game-development/history/s-work-013.md
