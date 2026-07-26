# RESULT — s-work-021 (work/triage · g-9c41/S1 · 2 Codex P2s from c-exec-015 STEP-0 routed home)

play: work (mid-leg triage of executor-routed findings)
direction: indie-game-development
node: g-9c41
task: S1 (c-exec-015, in flight — STEP-0 spike)
date: 2026-06-26

## outcome

Two P2 findings surfaced by Codex during the in-flight c-exec-015 STEP-0 build (and routed home by the build session
per the contract — not builder patches) are triaged and DECIDED. Both were verified FIRST-HAND in the dev code, not
taken from the report. Neither is a live correctness bug; both are real contract/ledger defects with a clear fix that
folds into STEP-0 (RED-first). The build session continues STEP-0 with the two decisions.

## evidence (first-hand, dev branch, GasCoopGame_dev)

- #1: `Assets/GasCoopGame/Core/Field/Voxel/VoxelFaceFlow.cs:66` — `biasMove = (int)((long)newBias[i] * faceConductivity[i]
  / kpEff)` with `kpEff = Kp*spf = 12*spf` (the GRADIENT's relaxation damper). So a non-zero bias below ~12 (full face)
  truncates to 0 → a weak kick/vent is a silent no-op. The builder's comments (lines 82-86, 99-102) show a bias-carry
  was DELIBERATELY rejected (it would move mass at zero gradient after the bias decays → breaks the Kp≥2*degree settle
  guarantee, ADR-0011 D3). So the no-carry choice is sound; the silent-no-op footgun is the real defect.
- #2: `tests/GasCoopGame.Core.Tests/Field/ForcedFlow/RW3ConservationAtomicityTests.cs:170-234` — Test-4 is ledgered as
  "throwing VoxelFaceFlow.Step leaves mass/bias/ttl unconsumed" but forces the throw on `SeedMass` (line 214), never on
  `Step`, and ASSERTS the checksum CHANGES (line 224). Step's overflow guard (line 139) is UNREACHABLE given
  MaxCellMass=1<<24 (max inflow ≈ 6×16.7M + 16.7M ≈ 117M ≪ int.MaxValue ~2.1B), and Step is atomic by construction (all
  locals validated before the single CommitStep, line 149). So it is a gap in the PROOF (honest-ledger defect), not a
  code defect.

## decisions (planner; verification = the leg's own RED tests + Step-0 oracle + fresh-session G5)

- **d-bias-quantum-001:** a non-zero bias on an open face MUST never silently no-op → preferred fix = a guaranteed
  signed ±1 floor (if bias≠0 ∧ conductivity>0 ∧ truncated biasMove==0 → ±1 in the bias direction, clamped by available
  mass) — parallel to the gradient's "a slit never seals to 0". NOT a bias-carry (the builder correctly rejected it).
  The build MAY instead reconsider whether the FORCING term should be kpEff-damped at all (likely root). Must preserve
  conservation + integer/in-checksum/loopback-determinism + still pass the Step-0 monotone-settle oracle (the ±1 acts
  only in the bounded, decaying forcing window). Independent test-author writes a RED test BEFORE the fix.
- **d-rw3-step-atomicity-ledger-001:** make the ledger honest — the independent test-author EITHER exercises a real
  throwing `Step` via a test seam (throw after bias/queue computed, before CommitStep; assert field byte-unchanged) OR
  renames the test to its true coverage (SeedMass atomicity) and discharges "Step atomicity" by a construction argument
  (overflow guard unreachable-by-construction + single CommitStep after validation), with the ledger row corrected. No
  silent overclaim.
- hygiene-red (untracked Unity files + `Assets/_Recovery`) = builder housekeeping (commit intended files + remove
  _Recovery + rerun `tools/check.ps1 -Deliver`); the leg is not gate-clean / cannot close until -Deliver is green.

## state_changes

- NOW.md decision_inbox: ADD d-bias-quantum-001 + d-rw3-step-atomicity-ledger-001 (both answered).
- NOW.md open_calls c-exec-015: status queued → in_flight (STEP-0; the 2 decided corrections + the hygiene note).
- NOW.md phase: prepend the s-work-021 entry. NOW.md next: RELAY block for the build session prepended.
- LOG.md: one line. (No CALL rewrite — these fold into the existing c-exec-015 STEP-0; the build session applies them
  RED-first.)

## captures

- The two decisions are STEP-0 corrections; they validate the choice to put the de-risk spike FIRST (the spike's oracle
  is exactly where #1 surfaces). No scope change to S1.

## decisions_needed

None blocking. Both findings decided (technical, planner-owned). The owner relays the decisions to the build session.

## play_check (play: work / mid-leg triage)

1. Recite — DONE: restated the 2 findings + the in-flight S1/c-exec-015 STEP-0 they belong to.
2. Owner inputs (owner) — N/A: technical triage; the fixes are machine artifacts, not owner-content. The owner relays.
3. Do the work — DONE: verified both first-hand in dev code; decided both; routed back as RED-first mandates.
4. Self-check — DONE: each decision traces to the actual code (line-cited); neither is a live bug; the fixes fold into
   STEP-0 and are gated by the leg's RED tests + oracle + G5.
5. Close — DONE: this RESULT; next = the build session continues STEP-0 with the 2 corrections.

## log

2026-06-26 — work/triage (g-9c41/S1, s-work-021): 2 Codex P2s from the in-flight c-exec-015 STEP-0 routed home + decided
(verified first-hand): d-bias-quantum-001 (weak bias must not silently no-op → ±1 floor, RED-first) + d-rw3-step-
atomicity-ledger-001 (RW3 Test-4 throws on SeedMass not Step → make the ledger honest; no live bug). Both fold into
STEP-0. next = build continues STEP-0.

## next

Relay the 2 decisions to the GasCoopGame_dev build session; it applies them RED-first within the in-flight c-exec-015
STEP-0, finishes the spike (oracle + decay + loopback hash + owner-eye), cleans hygiene, reruns -Deliver, then continues
to выброс/выдавливание/ветер/valve. RESULT applied home by a separate OS writer.

END_OF_FILE: live/indie-game-development/history/s-work-021.md
