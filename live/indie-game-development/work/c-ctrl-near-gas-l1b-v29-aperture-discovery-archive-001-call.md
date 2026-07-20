# CALL c-ctrl-near-gas-l1b-v29-aperture-discovery-archive-001

to: executor
direction: indie-game-development
track: core
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: L1B-Capture
issued: 2026-07-19 (s-work-near-gas-l1b-v29-aperture-discovery-archive-route-001)
engineering_contract: 29

goal: |
  Frozen aperture evidence is preserved outside active Deliver discovery and the retained L1B closing snapshot resumes
  lawful Deliver/publication, or one exact non-substitutable blocker.

context: |
  L1B explicit root validators are GREEN after evidence binding `01e0d793`. Retained canonical closing drafts are
  committed unchanged as clean local dev `b6bfc8fc9945e625c08a031c3a77b9e057be5129`; origin/dev is `01e0d793` and
  main/origin-main is `029279a7`. `./pwsh.cmd tools/check.ps1 -Deliver` fails only because frozen unrelated root
  `c-exec-structure-aperture-authority-v1-plan-001` is still enumerated as active and lacks a mutation record.

  That root was lawfully losslessly repaired to PRESERVED-PAUSED/no-successor: carrier `3bbbc4c...`; review/result
  commit `06b8a6e2`, review blob `00704214`, result blob `cdc17e5`; U4 clean detached `5af1d8db`, lease-free; repair
  commit `8d7d8f859232a8c585d6b3586d5cf9102451ed02` preserved objects and withdrew incomplete active RESULT. Owner
  authority closed the legacy cap route without successor; it must not be fabricated as DELIVERED or rebuilt.

launch:
  lane: A / NearGas core / serialized lifecycle-discovery control
  venue: WIN-CTRL admitted Target Local -> registry-resolved control venue holding retained L1B closing snapshot
  target_local: resolve exact clean control venue, lease, repository-authoritative archive/closure mechanism and retained snapshot custody through WIN-CTRL; infer no path/ref here
  machine: PC
  base: local dev `b6bfc8fc9945e625c08a031c3a77b9e057be5129`, origin/dev `01e0d793`, main/origin-main `029279a7`
  conflict_surface: aperture lifecycle/registry/result discovery metadata and Deliver discovery only
  depends_on: L1B root validators GREEN and proven aperture PRESERVED-PAUSED custody
  merge_queue: serialized control repair, then retained L1B closing snapshot resumes directly
  gates: engineering_contract 29; aperture lifecycle/result/discovery validators; preserved-object/U4 readback; result-check; normal check; no mutation exception; final Deliver on retained snapshot only after control GREEN

boundaries: |
  Fresh-read the repository-authoritative G0/Deliver discovery and archive/closure rules first. Use only their lawful
  mechanism to remove the named PRESERVED-PAUSED aperture root from active Deliver enumeration while preserving every
  frozen byte, Git object/ref/history and U4 custody. Do not create mutation evidence, grandfather/disable a gate,
  reinterpret product/spec, edit U4 or any product/candidate/test/PLAN byte, delete branches, or reset/stash/clean.
  Do not mark aperture DELIVERED or create a successor. If authority truly requires aperture mutation before any other
  root Deliver, stop and return that exact rule, validator output and non-substitutable blocker.

done_when: |
  1. HOME cites exact repository discovery/lifecycle authority and proves why the named no-successor PRESERVED-PAUSED
     root was active; it names the lawful archive/closure change that removes only it from G0 Deliver enumeration.
  2. Aperture lifecycle/result/discovery validators and actual result-check/normal check are GREEN, proving archived/
     preserved-not-delivered status. Carrier `3bbbc4c...`, commit/blobs, clean detached U4 `5af1d8db` and their refs/
     history are read back unchanged; no mutation or product byte is fabricated.
  3. Control-only commit/push/readback is exact and no L1B candidate, tests, behavior, mutation inputs/results or
     retained closing drafts change. If an unavoidable mutation rule exists, HOME returns it as the sole blocker.
  4. On GREEN, HOME includes `RETAINED L1B CLOSING SNAPSHOT RESUME AUTHORIZED`: clean `b6bfc8fc...` may immediately
     run full Deliver and non-force dev→main publication under the retained closing task, with no further Direction or
     owner relay. This control stage itself does not rerun mutation or publish L1B.

return: |
  Product APERTURE DISCOVERY ARCHIVE CONTROL HOME: authority/discovery finding; exact control diff/commit/refs;
  lifecycle/result/discovery validator outputs; frozen-object/U4 preservation readback; result/normal checks; and
  `RETAINED L1B CLOSING SNAPSHOT RESUME AUTHORIZED` or one non-substitutable blocker only.

budget: one bounded WIN-CTRL lifecycle/discovery control session
surface: Codex Desktop, WIN-CTRL registry-resolved Target Local

END_OF_FILE: live/indie-game-development/work/c-ctrl-near-gas-l1b-v29-aperture-discovery-archive-001-call.md
