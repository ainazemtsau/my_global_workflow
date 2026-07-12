CALL c-exec-unity65-mac-revision-build-001
to: executor
direction: indie-game-development
node: g-9c41
repo: github.com/ainazemtsau/GasCoopGame
kind: engineering
phase: BUILD
issued: 2026-07-12 (c-exec-unity65-mac-revision-plan-001)
parent: c-exec-unity65-mac-revision-plan-001

goal: |
  Unity 6000.5.3f1 Mac migration is repaired and independently evidenced at one reviewed final tip:
  same-version peers preserve full-width FishNet scene handles, mixed protocol versions reject safely
  before scene-broadcast decoding, all close-check defects are closed, and the candidate is ready for
  Direction OS delivery review without claiming merge, push, or Windows completion.

context: |
  Owner approved the revised PLAN with actual words `A` on 2026-07-12.

  Product venue:
  `/Users/antoninozemcev/codex-windows/GasCoopGame_codex`
  branch `codex/unity-6.5-migration-plan`
  frozen PLAN commit `8a344e97da10da417d76c0a3e7534bec0a0f7c96`
  candidate parent `df1e5caec09556b781dad7fb703fbc5e1438f4e0`
  base `origin/main == origin/dev == a644e5db538d1102f726630d6a4ac2f3f1bdcf5a`
  change id `c-exec-unity65-mac-revision-001`
  approach `unity65-coordinated-wire-v2-repair-closeout`.

  Binding planning authority:
  - `openspec/changes/c-exec-unity65-mac-revision-001/PLAN.md`
  - `openspec/changes/c-exec-unity65-mac-revision-001/proposal.md`
  - `openspec/changes/c-exec-unity65-mac-revision-001/specs/toolchain/spec.md`
  - `openspec/changes/c-exec-unity65-mac-revision-001/tasks.md`
  - `docs/adr/ADR-E-0011-c-exec-unity65-mac-revision-001-version-gated-scene-handle-wire.md`

  Historical authority `c-exec-unity65-mac-001` and PLAN commit `7969f36` remain evidence and were not
  rewritten. The successor authority narrowly accepts the coordinated scene-handle `int -> ulong` wire
  change for same-version peers with mandatory mixed-version rejection before scene-broadcast decode.

  Required close-check evidence source:
  `/Users/antoninozemcev/codex-windows/my_global_workflow/live/indie-game-development/history/2026-07-11-s-work-unity65-mac-closecheck-001.md`.

  The checkout contains unrelated unstaged owner/editor changes in `.vscode/settings.json` and
  `Assets/GasCoopGame/Levels/GasLab/Flow/CoopSmallSGF.asset`. They are outside candidate evidence and
  must remain untouched, unstaged, uncleaned, and uncommitted.

  Contract v19 applies. PLAN and BUILD are separate sessions. This BUILD begins with a fresh independent
  test-author deriving RED acceptance tests and negative controls from only the frozen revised spec.
  The builder may not edit those tests, the spec, or the ledger. Existing builder-authored/modified
  migration tests are non-independent and require exact keep/replace/delete disposition.

boundaries: |
  Do not change game design, gas/core meaning, save data, scene content, visual direction, RenderGraph ABI,
  general networking semantics, authority, ordering, reliability, timing, supported peer topology, late join,
  matchmaking, or host migration.

  Do not add mixed-version compatibility, a dual codec, downgrade, translation, or fallback. The only accepted
  protocol change is the full-width scene-handle wire for same-version peers plus pre-decode protocol-version
  mismatch rejection.

  Do not edit the frozen revised PLAN/spec/ledger/ADR or the fresh independent acceptance/negative-control tests.
  Do not relabel existing builder-authored tests as independent. Do not use source scans or stale transcripts in
  place of real final-tip runs.

  Required unavailable tooling is a STOP. No machine-local shim, reduced-fidelity substitute, source-scan proxy,
  assumed waiver, or same-family relabelling is allowed. A structurally unavailable diff-relevant mutation target
  requires an explicit owner decision before proceeding.

  Windows execution, merge commits, pushes, and delivery claims are out of scope. Preserve the two unrelated
  dirty owner/editor files exactly.

done_when: |
  1. Fresh independent acceptance and negative-control tests derived only from the frozen revised spec first fail
     against the unrepaired candidate, then pass at the final tip; commit ancestry proves the builder never edited
     them. Every existing builder-authored or modified migration test has an exact keep/replace/delete disposition
     and none is counted as independent evidence.
  2. Real same-version FishNet host/client evidence roundtrips a scene handle above the 32-bit range exactly, while
     a mixed-protocol peer is deterministically rejected before scene-broadcast decoding with logs on both ends
     and an operator-visible incompatible-version/update-required outcome. No old-build compatibility is claimed,
     and regression evidence shows every other networking invariant unchanged.
  3. The Mac harness selects platform-native PowerShell correctly; telemetry JSON byte evidence proves the frozen
     UTF-8-without-BOM/LF/terminal-newline contract is checkout-EOL-independent; all related negative controls pass.
  4. Every changed package/lock entry is explained, and all 49 unique UAC serialization diagnostics have a
     class-by-class final-tip disposition. Any behavior-loss or unresolved diagnostic remains gating.
  5. After the last source fix, exact Unity 6000.5.3f1 completes a deleted-Library import with zero compile errors,
     discovers the named target tests, and records fresh EditMode/PlayMode, Odin, MCP, Dungeon Architect, FishNet,
     gas RenderGraph, headless, and portable-harness evidence. Zero discovered target tests, stale runs, and source
     scans do not pass.
  6. Mutation evidence attacks changed migration/protocol/tooling behavior. If that is structurally impossible,
     work stops for an explicit owner decision; mutation of unchanged CoarseSectorGraph.cs does not satisfy this row.
  7. Independent review at the final tip records reviewed ancestry, scope/site/disposition, refuted-register
     markers, and invariant-class plus complete sweep for every fixed finding. No in-scope finding remains open.
     A separate binding fresh-session G5 tries to refute the final tip; any explicitly required unavailable
     cross-family tooling causes STOP rather than substitution.
  8. `docs/results/c-exec-unity65-mac-revision-001.md` reconciles every BUILD promise and records exact Editor and
     package lock, exact rollback proof to the declared baseline, assumptions/cuts, test disposition map, final SHA,
     review/G5 evidence, and confirmation that Windows/merge/push did not start. Every frozen ledger row is passing
     and `tools/check.ps1 -Deliver` is green at that reviewed final tip.

return: |
  Return the final product commit and branch; exact changed-file summary; independent test-author and immutable-test
  ancestry; opened transcripts/artifacts for every done_when item; package and UAC disposition records; mutation,
  review, refuted-register, fix-class sweep, and binding fresh-session G5 evidence; closing-report path; exact
  rollback proof; all-passing ledger and `tools/check.ps1 -Deliver` output; assumptions/cuts; confirmation that
  dirty owner files, Windows, merge, and push were untouched. On any required unavailable tool or unresolved gate,
  return a checkpoint naming the blocker and leave delivery unclaimed.

budget: one focused BUILD/repair-closeout session; no merge, push, or Windows work

END_OF_FILE: live/indie-game-development/work/c-exec-unity65-mac-revision-build-001-call.md
