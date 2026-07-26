# CALL c-exec-near-gas-l1b-surface-freeze-001

to: executor
direction: indie-game-development
track: core
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: L1B-Capture
issued: 2026-07-17 (s-work-near-gas-l1b-surface-freeze-dispatch-001)

goal: |
  NearGas L1B имеет замороженную, компилируемую внутреннюю поверхность наблюдения, на которой независимые
  поведенческие проверки могут доказать ровно пять принятых observation families без изменения поведения L1a.

context: |
  Это первый кодовый этап уже принятой L1B, а не новая задача и не расширение scope. Владелец принял PLAN точными
  словами «Принимаю PLAN» и 2026-07-17 разрешил продолжение: «можешь приступать к следующему шагу».

  Current product authority: contract v27; proven v23 compiled-carrier route remains active. Owner-approved PLAN:
  `openspec/changes/c-exec-near-gas-l1b-plan-001/PLAN.md`; proposal/tasks/delta spec in the same change;
  `docs/neargas-L1b-decisions.md`; ADR-E-0013. Exact frozen candidate `92331e300ab9ac38420d377184aa5dacd5184757`
  is published through product `main == dev == origin/main == origin/dev @ 2d995d69b503f73582e493c36c776a8b70f6bf66`.
  These SHAs are evidence, not a base, venue or branch pin. Re-read fresh root `AGENTS.md`, `validation.config`,
  canonical `docs/engineering/WORKTREE_REGISTRY.md` and current refs/worktrees before any write; product authority
  owns admission, venue, branch and serialized integration.

  Direction acceptance `live/indie-game-development/work/neargas-l1b-acceptance.md` freezes exactly five families:
  retry snapshot, fault injection, handler classification, sparse-kernel rows and test-side loopback trace. The
  frozen PLAN names every field, call site, rollback rule and disjoint ownership boundary. L1a remains DELIVERED;
  old v22 carrier is RETIRED/FORBIDDEN. Level LV0 is unrelated and remains pending owner verdict. Characters remain
  owner-paused.

  launch:
    lane: A / NearGas core, headless
    venue: current product registry assigns; Direction pins no path, branch or SHA
    machine: PC, no Unity Editor required except when current product authority explicitly says otherwise
    base: fresh current product authority; published 2d995d69 is evidence only
    conflict_surface: NearGas internal carrier files plus the exact no-op call sites frozen by the PLAN
    depends_on: owner-approved L1B PLAN published/released; no Level or character dependency
    merge_queue: product registry and integration queue serialize admission/publication
    gates: fresh non-author review is binding; model/provider identity never gates

boundaries: |
  This leg freezes only the internal compiler-green carrier and exact no-op connection sites. Do not implement
  recording, comparison, evaluator logic, fault throwing or any behavioral acceptance. Do not add or edit tests or
  test support. Do not open RED-FREEZE or BUILD from an unreviewed/unpublished candidate. No public API change,
  gameplay, Unity scene/asset/package work, runtime telemetry, networking, L2, C1, workers, S4, Level/DA/PGG or
  character work. No sixth family, generalized framework, legacy v22 reuse or workaround around current authority.
  Any need to change owner-approved PLAN semantics, exceed its source-line cap, touch an unadmitted/shared manifest,
  or use an unavailable required tool is STOP with the exact blocker.

done_when: |
  1. Current product registry legally admits one exact SURFACE-FREEZE venue before writes, with clean current-authority
     readback and no conflict with concurrent admitted work; lifecycle and serialized integration remain truthful.
  2. The committed carrier matches the frozen PLAN: one internal sealed one-shot operation context; field-preserving
     immutable carriers/read-only views for exactly four raw families; internal observed entry points only; public
     `ReplaceGeneration` and `Step` signatures and behavior remain unchanged.
  3. Exact no-op calls exist at snapshot entry/fault/exit, the two fixed pre-publication fault boundaries, the two
     actual handler invocation sites and the sparse-kernel row site. They record nothing, throw nothing and move no
     acceptance meaning into comments or documentation.
  4. The owner-approved decision page is contained or pinned and remains <=400 words; added production-source lines
     are <=400 by exact `git diff --numstat <parent>..<freeze>`; constructors preserve every field; every required
     Unity `.meta` sidecar is tracked in the same commit. Line 401 or any carrier gap is STOP+split, never a raised cap.
  5. Repo-native build, existing L1a tests and required surface/hygiene checks are GREEN. The handback names exact
     freeze commit+parent, Git manifest, source numstat, decision-page count, signatures, sidecars and command output.
     A separate fresh non-author review remains binding before RED; equal model provenance is legal under v27.

return: |
  Product SURFACE-FREEZE RESULT HOME: status; exact admission/lifecycle; freeze commit+parent and Git manifest;
  plain-language description of the added carrier and no-op sites; public-signature/behavior preservation evidence;
  production-source numstat; decision-page word count; sidecars; build/tests/hygiene commands and results; fresh
  review status or exact pending review CALL; every done_when disposition; preservation of Level/characters and cuts.
  No claim that L1B behavior, RED, BUILD or full L1B is complete.

budget: one focused half-day maximum; stop earlier on authority, conflict, cap, tool or frozen-PLAN mismatch
surface: product-repo Codex session

END_OF_FILE: live/indie-game-development/work/c-exec-near-gas-l1b-surface-freeze-001-call.md
