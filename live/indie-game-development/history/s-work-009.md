# RESULT — s-work-009 (work / g-9c41 Wave 2 / t-2 close)

Session: apply + verify the returned c-exec-006 executor RESULT, complete the home-side OpenSpec lifecycle, and
close Wave-2 task t-2. Plain owner message ("T2 готова, Result сохранён — можем ли закрывать, всё ли формально
сделано по нашей инструкции и по OpenSpec"). Resolved against NOW (matches the active task t-2 / open call
c-exec-006) → `play: work`, CLOSE.

## outcome

Wave-2 **t-2 is CLOSED** (c-exec-006 delivered, verified, and formally finished). The coarse band solver now runs
on a real DA-shaped generated level with a controlled breach, per-room-capacity liveness, per-layer host+2-client
replication across the breach, a single field-sampling oracle, and clean 1-player parity — proven headlessly +
owner-eyeballed. The one outstanding formal step the executor handed back — **OpenSpec apply + archive** — is DONE.

- **Executor delivery (GasCoopGame, legs 1–8):** `check.ps1 -Deliver` GREEN — 372/372 headless, mutation 75.29% ≥ 70,
  deliverable-coverage 14 promises disposed. Owner eyeball PASSED («работает», 2026-06-18). Fresh-session G5 CLEAN
  (3 validators; 3 findings found + fixed: T28b CR1-reconstructed cross-peer oracle, BandForHeight `long` overflow,
  T5b GG4 source-survival-across-breach). On `main` @ `0327b9f` (build @ `bef6fd8` → `04f39ee`), pushed earlier.
- **deliverable-exists (v7) verified by hand:** the leg-8 owner-visible slice (composer + `DaTopologyProducer` +
  `GasDebugCoarseScene.unity` + run-artifact json) had been reported-done-not-built; the v7 coverage gate caught it,
  the rebuild closed it. I confirmed all 5 artifacts physically exist on disk — not trusted from the RESULT text.
- **OpenSpec apply + archive (home-side, DONE this session):** folded the 18 ADDED requirements of the c-exec-006
  change into the canonical `openspec/specs/sim-core/spec.md` (42→60 `### Requirement` blocks) with an Applied-from
  marker; canonical spec stays grep-clean of the dead cross-band prose; `git mv` the change folder to
  `openspec/changes/archive/`; flipped ledger T34 ☑. `check.ps1 -Deliver` re-run GREEN (strong-check + coverage now
  N/A-by-absence post-archive; build/tests untouched — markdown + folder move only). Committed `dev` @ `7987506`,
  merged `main` @ `ce79e10`. **UNPUSHED** (push owner-gated).
- **FishNet UDP wire:** env-deferred (`WSAENOBUFS` at the client socket bind, persists across an Editor restart — a
  host/OS condition, NOT a build defect). The spec's binding gate is headless + in-process loopback (which delivered
  the host→2-client slice identically over the LOCKed codec); the real-UDP axis is OWNER-RUN. Does not block closure.

## evidence

- **Closure verification (G10 deliverable reconciliation against the CALL's own done_when):** every t-2 done_when
  clause carries a disposition — IN1/IN2 (`CoarseTopologyIngestionTests` T10–T14) · liveness/back-pressure/GG4
  (`CoarseLivenessTests` T1–T8, T5/T5b) · breach GG1/GG2/GG3 (`CoarseBreachTests` T15–T20) · replication CR1/CR2/CR3
  (`CoarseBreachReplicationTests` T21–T25) · oracle OR1/OR3 (`Oracle/CoarseOracleTests` T26–T29 + T26b + T28b) ·
  parity (`CoarseParityAndAdditiveTests` T30) · planner spec actions (leg-1 T0a–T0c). Engine bullets 11–14 carry
  `exists:` existence proofs (verified on disk). No silent drop; no cut without owner-ack.
- **Gate:** `& C:\projects\Unity\GasCoopGame_dev\tools\check.ps1 -Deliver` → "OK: all gates green" (boundary 0/0;
  372/372; hygiene OK; RESULT fields present; strong-check + coverage N/A-by-absence).
- **OpenSpec apply integrity:** `grep -c "^### Requirement:" openspec/specs/sim-core/spec.md` = 60 (was 42, +18);
  `grep -niE "past a colder species|inverts past a cold light"` = 0 hits on dev AND main; `openspec/changes/` (non-
  archive) holds only `.gitkeep`; `archive/` now contains `c-exec-006-t2-real-level-breach-replication/`.
- **G5 (this session = independent refutation pass):** I am not the build session, so this is a second fresh look.
  I tried to break the claim — checked artifact existence, the merge SHAs, the un-applied canonical spec, the env
  deferral honesty, and the contract-version sync (repo v7 == os/engineering v7, no §Re-sync owed). The only real
  gap was the un-done OpenSpec apply+archive (now closed); the FishNet UDP block is a legitimately-deferred owner-run
  axis per the frozen spec. No hole survives.
- **Executor RESULT** saved verbatim → `history/2026-06-18-c-exec-006-t2-result.md`.

## state_changes

Applied to `live/indie-game-development/` this session (writer = this Codex-on-repo session, after this RESULT):
- `NOW.md` active_tasks t-2: `status: active` → `status: done` (full close note).
- `NOW.md` active_bet.phase: appended the t-2-CLOSED milestone line.
- `NOW.md` open_calls c-exec-006: `status: queued` → `status: done`.
- `NOW.md` decision_inbox: added `d-wave2-seq-001` (status `open`) — which Wave-2 leg leads (t-4/t-3/both), options +
  recommendation A (t-4 first).
- `NOW.md` next: replaced "open c-exec-006" with "frame + open the next Wave-2 leg (PLAN, owner present), owner picks
  t-3/t-4 sequencing at open" + carry-forward + owner-side non-gating items (push, FishNet UDP).
- `LOG.md`: appended the s-work-009 line.
- `history/2026-06-18-c-exec-006-t2-result.md`: saved the executor RESULT.
- `history/s-work-009.md`: this RESULT.
- TREE.md: UNTOUCHED (g-9c41 stays `active`, multi-wave; t-2 is not the last task — no node review triggered, G10
  task-play lifecycle).

GasCoopGame (product repo, separate): `dev` @ `7987506`, `main` @ `ce79e10` — OpenSpec apply+archive (planner
lifecycle action, not a builder edit). Local, unpushed.

## captures

- cap-1: **FishNet UDP `WSAENOBUFS` is a persistent host/OS condition** on this machine (survives an Editor restart) —
  loopback is the standing transport; real-UDP validation = owner-side network triage (non-paged-pool / VPN-LSP / AV
  UDP filtering) OR a two-process / non-loopback-NIC run. Non-gating (binding gate = headless + loopback). Re-surfaces
  for every FishNet PlayMode axis (t-3/t-4).
- cap-2: the **deliverable-exists v7 gate bit a SECOND time and worked** — leg-8's composer/scene were reported done by
  citing unrelated FishNet PlayMode tests, the contract-v7 coverage-check forced an existence proof, the rebuild
  closed it. Confirms the invariant earns its keep; no rule change indicated (it fired as designed).

## decisions_needed

- **d-wave2-seq-001 — which Wave-2 leg leads now t-2 is done?** t-3 (temperature-layer extensibility proof) and t-4
  (player-legible render terminus) are both unblocked and parallelizable.
  - (A, RECOMMENDED) t-4 first — first showable artifact off the real sim, breaks pre-mortem #2, feeds the fixed
    2026-08-31 page date; solver-agnostic so it doesn't wait on t-3. Bad: extensibility claim stays argued a bit longer.
  - (B) t-3 first — closes the seam-exercised half earliest. Bad: nothing visible, doesn't move the 08-31 clock.
  - (C) both in parallel (G1 ≤3 active). Bad: more orchestration load on a solo owner — only if running ahead.

## play_check (os/plays/work.md)

1. Recite — DONE: restated t-2 goal/done_when + the bet it serves (Wave-2 player-facing terminus); confirmed t-2 not
   obsolete (the returned RESULT delivers it).
2. Owner inputs (owner) — N/A→checked: t-2 is engineering, not owner-content (his food/voice/schedule); the one
   owner input this close needed — accept the delivery — was already given out-of-session (eyeball «работает»
   2026-06-18, recorded in the executor RESULT). No new owner drafting required.
3. Do the work — DONE: verified the executor RESULT against done_when (G10 reconciliation); confirmed leg-8 artifacts
   exist on disk; performed the home-side OpenSpec apply (18 reqs folded, grep-clean) + archive + T34; re-ran the
   deliver gate GREEN; committed GasCoopGame dev→main (local).
4. Self-check — DONE: each done_when clause maps to a named test or an existence artifact; gate GREEN; OpenSpec lifecycle
   complete (apply + archive, "archiving is part of done"); contract version synced; the only deferral (FishNet UDP) is
   a frozen-spec owner-run axis, not a gap.
5. Close — DONE: this RESULT; t-2 → done; next = frame the next Wave-2 leg; sequencing decision surfaced.

## log

2026-06-19 — work (g-9c41 / Wave 2 / t-2, s-work-009): closed t-2 — verified c-exec-006 (372/372, G5 clean, owner
eyeball, leg-8 artifacts exist) + completed the home-side OpenSpec apply+archive (canonical spec +18 reqs grep-clean,
folder archived, T34 ☑; GasCoopGame dev @7987506 / main @ce79e10, unpushed). FishNet UDP env-deferred (owner-run). Bet
rolls to t-3 ∥ t-4; owner picks sequencing (d-wave2-seq-001).

## next

CALL — frame + open the next Wave-2 executor leg.
- goal: the next Wave-2 outcome exists in GasCoopGame — either a player can SEE the real coarse sim in a stylized,
  debug-overlay-free render slice (t-4 terminus) OR a 3rd independent system-layer (temperature) is networked-
  consistent at coarse scale alongside gas (t-3 extensibility) — owner's sequencing pick at open (d-wave2-seq-001).
- context: t-2 closed; canonical `openspec/specs/sim-core/spec.md` now carries the applied t-2 requirements; the
  VERIFIED §CONTRACTS + ADR-0007 stand; build on GasCoopGame `dev` → `main` when green; t-4 reads the RN1 read-model
  (solver-agnostic), t-3 plugs in via the layer registry (XL2 byte-identical + barrier-table re-size SURFACED).
- boundaries: do NOT re-open the LOCK / C1–C22 / BS1–BS15; per-species temperature + the fine intra-room cloud shape +
  coarse↔fine handoff + d-returnfidelity-001 mid-transient bar = Wave 3, out of scope.
- done_when: the chosen leg's acceptance battery (independent test-author, RED-before/GREEN-after) passes headless +
  `check.ps1 -Deliver` GREEN + fresh-session G5 + owner acceptance, with deliverable-coverage closing each promise.
- return: an executor RESULT routed home (this OS owns the next CALL; the builder does not author it).
- budget: ≤ one focused executor leg (half-day human-equivalent); a 2× overrun stops and reports.

Owner-side, non-gating: PUSH GasCoopGame (`dev` @ 7987506 / `main` @ ce79e10) + this OS commit when ready; validate
the literal FishNet UDP wire once the host network is healthy.

END_OF_FILE: live/indie-game-development/history/s-work-009.md
