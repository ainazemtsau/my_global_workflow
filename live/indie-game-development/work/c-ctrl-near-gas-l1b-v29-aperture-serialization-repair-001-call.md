# CALL c-ctrl-near-gas-l1b-v29-aperture-serialization-repair-001

to: executor
direction: indie-game-development
track: core
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: L1B-Capture
issued: 2026-07-19 (s-work-near-gas-l1b-v29-aperture-serialization-repair-route-001)
engineering_contract: 29

goal: |
  Losslessly preserve the external aperture evidence as PRESERVED-PAUSED and remove only its incomplete active-dev
  RESULT, so the serialized aperture blocker is actually clear for the later separate L1B
  HANDBACK-PENDING/integration-control stage.

context: |
  This is the same immutable L1B root `c-exec-near-gas-l1b-pair-candidate-001`, contract 29. Its final range
  `62db→75e0→4df→T=6fa101b4` remains REVIEW GREEN and is read-only here. The preceding aperture drain CALL returned
  BLOCKED at unchanged WIN-CTRL: authenticated `dev == origin/dev == 25afa4aa4585d40a304d233c0b3f24b4e6bf34b3` and
  `main == origin/main == 029279a7`. The reproduced gate
  `./pwsh.cmd tools/result-check.ps1 -Repo .` fails because active dev contains
  `docs/results/c-exec-structure-aperture-authority-v1-surface-freeze-001.md` as
  `SURFACE-FROZEN / REVIEW-GREEN / NOT DELIVERED`; publication to origin/dev does not clear the active-dev-versus-main
  comparison.

  Aperture carrier `3bbbc4c46c22bb39f6478413cd74d43fc5b555ef` and its existing review/result evidence are immutable
  Git objects. They must be preserved, not rebuilt or falsely marked DELIVERED. The prior CALL lacked authority to
  withdraw the incomplete active RESULT or to make the explicit PRESERVED-PAUSED lifecycle transition; this CALL
  grants only that control repair.

launch:
  lane: A / NearGas core / external serialized-dev control repair
  venue: WIN-CTRL admitted Target Local -> registry-resolved control venue
  target_local: resolve the exact project path, control lease, WIN-U4 preservation branch, and authorized artifact refs through WIN-CTRL; infer no path/ref here
  machine: PC
  base: authenticated dev/origin-dev `25afa4aa4585d40a304d233c0b3f24b4e6bf34b3` and main/origin-main `029279a7`
  conflict_surface: external aperture lifecycle, registry/dashboard mirrors, active RESULT visibility and preservation refs only; all L1B state is read-only
  depends_on: BLOCKED aperture drain HOME and immutable carrier `3bbbc4c46c22bb39f6478413cd74d43fc5b555ef`
  merge_queue: serialized; no L1B integration in this stage
  gates: engineering_contract 29; exact object/ref capture; WIN-U4 raw-byte preservation; actual result-check; normal check; non-force dev readback

authorized_scope: |
  1. Capture the exact carrier, refs, result blob/commit and review blob/commit identities; prove the registry-resolved
     WIN-U4 preservation branch keeps their raw bytes, is clean, and has no active lease before PRESERVED-PAUSED.
  2. Transition only `c-exec-structure-aperture-authority-v1-surface-freeze-001` from
     HANDBACK-PENDING/REVIEW-GREEN to PRESERVED-PAUSED; a future resume requires fresh admission.
  3. Remove or revert only the incomplete aperture RESULT from active dev, preserving it through named Git
     objects/refs/history. Reconcile only the exact aperture registry/dashboard lifecycle mirrors and retain review
     evidence only as lawfully applicable preserved evidence.
  4. Commit and push the authorized dev repair non-force after the required checks and exact readback.

boundaries: |
  Never mark the aperture result DELIVERED, rebuild aperture product work, discard its objects/refs/history, or
  substitute a new RESULT/review. Never reset, stash, clean, delete branches, force push, or alter main. Do not modify
  L1B source/tests/PLAN/spec/evidence/registry row/candidate `T`, transition L1B HBP, integrate T, choose final H,
  run mutation/Stryker, Deliver, or ask the owner. No unrelated dev delta or product design/work is authorized.

done_when: |
  1. HOME names the exact carrier/ref/result/review blob and commit identities, the WIN-U4 preservation branch and
     raw-byte proof, clean status, and no-lease proof.
  2. The aperture root is mechanically PRESERVED-PAUSED from HANDBACK-PENDING/REVIEW-GREEN; its retained evidence
     remains reachable in named Git objects/refs/history and any resume is fresh-admission only.
  3. Active dev changes only by the incomplete aperture RESULT's lawful removal/revert plus the exact required
     aperture registry/dashboard lifecycle mirrors; diff/readback proves zero L1B path, row, evidence or candidate delta.
  4. The actual `./pwsh.cmd tools/result-check.ps1 -Repo .` and normal check are GREEN on final dev; the repair is
     committed and pushed non-force with authenticated dev/origin-dev and main/origin-main readback.
  5. HOME returns exactly `APERTURE SERIALIZATION CLEARED — L1B HANDBACK-PENDING/INTEGRATION CONTROL ELIGIBLE`, or
     one complete blocker with current refs, preserved identities and the missing lawful authority. No integration,
     mutation, Deliver or final-H claim occurs here.

return: |
  Product APERTURE-PRESERVATION CONTROL-REPAIR HOME: WIN-CTRL Target Local/lease and U4 preservation proof; exact
  object/ref/blob identities; lifecycle transition; exact active-dev diff and zero-L1B proof; result-check/normal-check
  outputs; non-force push/readback; and only the exact eligibility phrase or one blocker. No successor CALL, owner
  relay, L1B integration, H selection, mutation or Deliver.

budget: one bounded WIN-CTRL serialized-control repair session
surface: Codex Desktop, WIN-CTRL registry-resolved Target Local

END_OF_FILE: live/indie-game-development/work/c-ctrl-near-gas-l1b-v29-aperture-serialization-repair-001-call.md
