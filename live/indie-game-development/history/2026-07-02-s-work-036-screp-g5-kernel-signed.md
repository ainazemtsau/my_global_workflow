# RESULT s-work-036 — Sc-rep binding G5 verdict + d-sparse-tick-kernel-001 SIGNED

- direction: indie-game-development / g-9c41
- session: s-work-036 (2026-07-02; owner in-chat; continuation of the 2026-07-02 review/repair thread)
- inputs: owner's «да» on d-sparse-tick-kernel-001 + the pasted verdict of the fresh-session G5 run on
  Sc-rep (GasCoopGame_dev @8db3ee1, refutation-only, no source edits, no merge).

## G5 verdict (binding, fresh session): COULD-NOT-REFUTE

Held under refutation attempts (evidence file:line in the owner-pasted report):
- dense→sparse conversion exact + atomic (scratch-then-swap; >4-type/drop/atomicity REDs);
- dominant STAMP + overlay folded CELL-KEYED (isolation / distinctness / cross-peer REDs distinguish);
- no-regression golden = the REAL post-Sc-weight baseline (ScWeightNoRegressionTests.GoldenChecksums), not
  rebaselined;
- zero-float / int-overflow scans cover the new files (40 each; planted -SelfTest controls trip);
- ZERO-LEGACY in the honest frame: VoxelField authority = SparseDominantNearGasField; dense remains only as
  per-tick scratch, and RESULT.md explicitly declares the sparse tick-kernel/performance NOT delivered
  (-Deliver red is the EXPECTED honest state until Sc-kernel);
- S1 review-repairs conform: destination back-pressure = d-roomfull-001 capacity law; temperature =
  long/saturating; ForcedFlow battery 66/66;
- runs: 1130/1130 full suite; focused batteries 73/73, 49/49, 25/25, 29/29; check.ps1 green;
  mutation artifact 74.17 ≥ 70 (read-only check, not re-run — the tool writes artifacts).

ONE finding, **P2 (test-gap, not a code defect):** the hashmap-substitution guard binds the cell RECORD, not
the FIELD authority storage — a private `Dictionary<int, SparseDominantCellRecord>` authority could pass.
**Disposition:** folded into the Sc-kernel draft CALL done_when #9 (work/c-exec-023-draft-call.md) — that
slice restructures exactly this hot path; no hotfix mid-gate (a fix is a change).

## Owner decision

**d-sparse-tick-kernel-001 = «да»** (owner, 2026-07-02, in-chat): slice Sc-kernel (active-front tick kernel)
inserted BEFORE Sc-reactions. NOW.decisions entry updated with the decision field.

## state_changes applied

1. NOW.md: current_truth + kill_by + Sc-rep status_note updated (G5 verdict + P2 disposition; wall CLOSED);
   next_slices Sc-kernel → SIGNED; decisions entry → decision recorded; next rewritten (owner-eye → merge →
   frame c-exec-023 → c-021 shape; visual W1a sign + W1b after merge; 4 decisions still pending).
2. work/c-exec-023-draft-call.md: banner conditions updated (sign ✅, G5 ✅, merge pending); NEW done_when #9 =
   field-level storage guard (the G5 P2).
3. LOG.md: entry appended.

## next

CALL: owner-eye on Sc-rep (confidence) → owner runs the merge block (dev→main --no-ff + push; dev2 NOT
merged) → fresh framing of c-exec-023 (owner present, standard hardening) → executor runs Sc-kernel.

END_OF_FILE: live/indie-game-development/history/2026-07-02-s-work-036-screp-g5-kernel-signed.md
