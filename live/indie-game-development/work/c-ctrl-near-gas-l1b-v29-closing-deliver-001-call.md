# CALL c-ctrl-near-gas-l1b-v29-closing-deliver-001

to: executor
direction: indie-game-development
track: core
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: L1B-Capture
issued: 2026-07-19 (s-work-near-gas-l1b-v29-closing-deliver-route-001)
engineering_contract: 29

goal: |
  Close the immutable L1B implementation root with verbatim canonical evidence, validated Deliver and RELEASED
  dev/main publication, or return one exact blocker.

context: |
  Same root `c-exec-near-gas-l1b-pair-candidate-001`, contract 29. FINAL-H REVIEW/MUTATION is GREEN. Clean final-H
  checkout is `H=dev=origin/dev=bf76fa68183f186190a2d6221a241a0b48b975e1`; main/origin-main is
  `029279a7a03af5869f32ddbb8b93aa49f2c6183f`. Only reviewer-owned untracked evidence exists:
  `docs/reviews/review-c-exec-near-gas-l1b-pair-candidate-001.md` and
  `docs/measurements/mutation-c-exec-near-gas-l1b-pair-candidate-001.json`.

  Exact review blob is `8eaaa8051980db29a3ef983f2113b4c88d1a654c`; mutation JSON blob is
  `9ad8b74608b704227eae2ece88106a26c0562466`. Review binds
  `Reviewed-commit=Mutation-reviewed-commit=H`, names canonical mutation artifact blob `9ad8...`, has Builder-model/
  Reviewer-model, Rounds 1, nonempty Findings, and one in-scope `class:l1b-source-identity-retry-exit-loopback-drift`
  finding refuted with KERNEL-G5. Mutation JSON v2 binds this implementation changeId to H with score 75.18 (floor 70
  passed), killed 1294, timeout 208, survived 273, noCoverage 223, valid 1998; reviewer-authoritative scope is three
  Core files, `I=B=029279a7`, concurrency 16 adaptive. Core 0/0, full 1915/1915, standard check 1813/1813 plus
  hygiene/self-tests/scans are GREEN. No candidate or mutation-input delta exists.

launch:
  lane: A / NearGas core / serialized closing evidence and Deliver
  venue: WIN-CTRL admitted Target Local -> registry-resolved closing-control venue
  target_local: resolve exact clean control path, lease, publication strategy and authorized refs through WIN-CTRL; infer no path/ref here
  machine: PC
  base: authenticated final H `bf76fa68183f186190a2d6221a241a0b48b975e1` with only the two named reviewer evidence files untracked
  conflict_surface: canonical review/mutation/result evidence, exact root lifecycle/registry/dashboard mirrors, Deliver and serialized dev/main refs only
  depends_on: FINAL-H REVIEW/MUTATION GREEN, ACTIVE root binding and exact H custody
  merge_queue: serialized final close; no concurrent candidate or mutation work
  gates: engineering_contract 29; verbatim evidence hashes; root review/mutation/result/fix-class/refuted/root-binding validators; check.ps1 -Deliver; non-force dev/main readback and RELEASED lifecycle proof

boundaries: |
  Stage and commit the two supplied reviewer evidence files verbatim; do not modify mutation inputs. Create only the
  canonical root RESULT `docs/results/result-c-exec-near-gas-l1b-pair-candidate-001.md` with the repo-required seven
  sections/status, plus exact lifecycle registry/dashboard mirrors and gate-produced closing evidence if required. Do
  not edit any candidate/carrier/RED/BUILD/T blob, reopen design, run mutation again unless the evidence is mechanically
  stale, or make unrelated changes. Preserve U3 branch/worktree. No force push, reset, stash, clean or destructive
  branch operation. A stale-evidence diagnosis, validator failure, Deliver failure or publication conflict is a blocker.

done_when: |
  1. HOME proves canonical review and mutation JSON bytes/hashes exactly match `8eaaa805...` and `9ad8b746...` before
     their evidence commit; mutation inputs still have zero post-H delta. The canonical root RESULT is complete with
     required seven sections/status and every required lifecycle mirror is named.
  2. Explicit root review, mutation, result, fix-class, refuted and root-binding validators are GREEN. Required
     closing evidence is accounted for exactly, including guarded evidence commits and the refuted KERNEL-G5 finding.
  3. `./pwsh.cmd tools/check.ps1 -Deliver` is GREEN on closing HEAD; its scope proves no post-H mutation-input delta.
     Any mutation rerun occurs only after a mechanically demonstrated stale-evidence condition and is recorded.
  4. Closing commits are non-force pushed to dev; dev is merged into main using the repo-authorized strategy, both refs
     are non-force pushed and exact local/origin dev/main readback proves the delivered root. Root lifecycle becomes
     RELEASED with final required lifecycle evidence and final gate/readback rerun.
  5. HOME returns `DELIVERED/RELEASED` with exact evidence, closing, dev and main commits/refs, or one complete blocker.

return: |
  Product L1B CLOSING CONTROL HOME: Target Local/lease; verbatim evidence hashes/blobs and root RESULT identity;
  validator/Deliver outputs; all closing commits; authenticated dev/main/origin refs; RELEASED registry/dashboard
  readback; U3 preservation and zero candidate/mutation-input delta proof; and DELIVERED/RELEASED or one blocker only.

budget: one bounded WIN-CTRL final evidence/Deliver/publication control session
surface: Codex Desktop, WIN-CTRL registry-resolved Target Local

END_OF_FILE: live/indie-game-development/work/c-ctrl-near-gas-l1b-v29-closing-deliver-001-call.md
