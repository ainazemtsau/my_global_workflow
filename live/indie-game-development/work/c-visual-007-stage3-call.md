# CALL c-visual-007 — Stage 3: Одна жемчужина — RENDER-ONLY

> FIRE-READY 2026-07-07 (s-work-061). Third stage of gas-visual-plan-v2 after
> c-visual-006 closed. Stage 2 is DONE on GasCoopGame_dev_2 `dev2@6dbdddd`
> (gas passport + real two-type preview + real half-res path). Base for this
> leg is that delivered dev2 tip, not primary `NOW.next` and not c-exec-021.
>
> Contract note: GasCoopGame is behind OS engineering contract v19. FIRST
> product action is a narrow §Re-sync to v19: PLAN and BUILD are separate
> sessions, and the PLAN the owner approves is owner-readable. If the repo
> cannot §Re-sync cleanly before Stage 3 planning, STOP and return the blocker.

- direction: indie-game-development
- node: g-7e15 (VISUAL track)
- play: work (executor leg — GasCoopGame render layer; dev_2 only)
- repo: C:\projects\Unity\GasCoopGame_dev_2
- kind: engineering
- runs_in: a FRESH GasCoopGame_dev_2 PLAN session first, then a separate FRESH BUILD session after owner plan approval
- base: GasCoopGame_dev_2 `dev2@6dbdddd` from c-visual-006 close; verify clean/head before planning
- plan_source: live/indie-game-development/work/gas-visual-plan-v2-2026-07-02.md §Stage 3 only

## goal
One real gas reaches the "ближе к жемчужине" bar in motion: natural flow, light visibly passing through it, and LP1-LP5 individually re-confirmed on the Stage-2 ship-quality render path.

## context
- Stage 3 in `work/gas-visual-plan-v2-2026-07-02.md` is the authority for this leg: one hero gas, one lever at a time; the named debts are toon-band count, opacity ceiling, natural-jet fix, and LP1 re-test.
- Stage 2 closed on `dev2@6dbdddd`: base gas passport, 128B visual params layout, real dominant-type read, real half-res + bilateral upsample, and two-colour preview are available for Stage 3 to judge against.
- Stage 1 stand assets are the viewing surface: `GasRoomScene`, primary bookmark, Open Arena Jet, LP1 Proof camera/replay, fixed-seed restart, and `GoodSampleAsset` never-worse baseline.
- W1a left LP1 as candidate-pass: lamp-direction read while orbiting was weak. Stage 3 explicitly re-tests LP1 by moving/swapping the lamp; the through-light read must follow or the reservation stays recorded.
- The pre-agreed ceiling exit is `d-finer-grid-fork-001`: if the remaining gap is sub-cell silhouette, render polish stops honestly and the delta routes to that engine-side view-refinement fork later.

## Stage 3 scope from visual plan v2
1. Hero-polish one gas by owner-visible A/B levers only: two-tone directional ambient, HZD-style beer-powder dark edges, per-step analytic transmittance, HG tuning, and LUT-ramp promotion only if needed.
2. Close the two standing visual debts: owner-eye pick of toon-band count (1/2/3/4) and a signed opacity-ceiling number. The opacity number closes `owner-ack:esc-c-visual-003-opacity-ceiling-deferred-2026-06-30` and feeds LP5 sign-off.
3. Natural jet fix is not vague polish: kill the "plasticine capsule" read and make the jet feel like natural gas flow. Plan v2's starting approach is curl-noise advection plus two-phase flowmap blending; a blocked or substituted approach is a STOP + owner decision.
4. LP1 re-test row is mandatory: move/swap the lamp and show that the through-light read visibly follows from the primary bookmark.
5. Re-confirm LP1-LP5 individually. No aggregate "looks good" close.

## process discipline
- v19: PLAN and BUILD are separate sessions. The first session produces a detailed but simple owner-readable Stage 3 plan, names each technical decision and why, records cuts/deferred items, then STOPS after owner approval and hands off a build CALL. It writes no product code and authors/commissions no red tests.
- NEVER-WORSE: preserve `GoodSampleAsset`; every visible change is A/B against the current baseline from the primary bookmark; worse means discard the lever, not rebaseline downward.
- ONE GAS, ONE LEVER AT A TIME: state what the owner should see and why before each visual lever.
- PRIMARY BOOKMARK VERDICT: the primary preset is the verdict surface. Open-space pad/free orbit may inform notes but do not replace the signed verdict.
- UNCERTAINTY COMES HOME: if the jewel gap is actually grid silhouette, or the natural-jet approach needs sim truth, stop and return that finding.

## boundaries
- RENDER-ONLY (R13): ZERO `Core/**` edits; sim untouched; no c-exec-021, no Sc-reactions, no engine chemistry work, no c-exec-021 continuation.
- dev_2 only. Do not reset away `dev2@6dbdddd`; if Stage 2 is missing, dirty, or not recoverable, STOP. dev_2 -> main merge/push remains owner-gated.
- No Stage 4 work: no three archetypes, no danger ladder, no blind lineup, no frontier-blend multi-type character gate.
- No Stage 5/6 work: no flood perf spectacle, teammate readability, residue, sparse VFX accents, Feel/MMFeedbacks, or post-Steam-page world integration.
- No anomalous bespoke gases, no warning A-channel/hazard telegraph, no fake reaction/event data, and no render-side invention of sim outcomes.
- No self-written source-text scanner as behavior evidence. Render behavior is real Unity/live-MCP/PlayMode evidence plus owner-eye; wiring smoke may only prove existence.
- Required tool unavailable (Unity Editor/MCP/headless license) = STOP and ask the owner to launch/approve; no workaround or crutch.

## done_when
- §Re-sync to contract v19 is confirmed first: product run contract says PLAN and BUILD are separate sessions, owner-readable plan required, and `validation.config` stamps `synced_contract_version: 19`.
- The owner-approved PLAN is owner-readable and then stops before build; the BUILD starts in a fresh session from the frozen plan.
- One real gas, judged in motion on the Stage-2 half-res render path, reads closer to "жемчужина": natural flow, no plasticine-capsule jet read, light visibly passing through.
- Toon-band count is owner-picked (1/2/3/4) and recorded; opacity ceiling is signed as a number and the old deferred opacity-ceiling ack is closed.
- LP1, LP2, LP3, LP4, and LP5 each carry an individual disposition. LP1 specifically includes the lamp move/swap proof; if it still fails, the reservation is recorded honestly and the CALL returns that status, not a fake close.
- If the remaining visible gap is sub-cell silhouette, the RESULT says so and routes the delta to `d-finer-grid-fork-001`; no render crutch or silent scope stretch.
- `tools/check.ps1 -Deliver` GREEN; `tools/result-check.ps1 -Repo . -ChangeId c-visual-007` PASS; sim tests unchanged; `git diff Core/**` EMPTY; `docs/results/c-visual-007.md` exists and routes the RESULT home.

## return
- PLAN session return: owner-approved Stage 3 plan + frozen build handoff; c-visual-007 stays open.
- BUILD session return: RESULT home with outcome, evidence, owner-eye LP1-LP5 dispositions, check output, any cuts with owner-ack, and the next visual slice only after Stage 3 signs (Stage 4 = three characters + danger scale).

## budget & rigor
One owner-present PLAN session plus one focused BUILD session if the PLAN confirms the natural-jet fix fits. If the natural-jet fix is larger, the PLAN must split it as its own shaped sub-leg with appetite and checkpoint date before build, per visual plan v2.

parent: s-work-061

END_OF_FILE: live/indie-game-development/work/c-visual-007-stage3-call.md
