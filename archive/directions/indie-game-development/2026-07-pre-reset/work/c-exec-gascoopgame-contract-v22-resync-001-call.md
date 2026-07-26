# CALL c-exec-gascoopgame-contract-v22-resync-001

to: executor
direction: indie-game-development
kind: engineering
repo: C:\projects\Unity\GasCoopGame_core
project: GasCoopGame
node: g-9c41
task: NearGas-L1-BUILD
phase: PRODUCT CONTRACT v21 -> v22 RE-SYNC ONLY
issued: 2026-07-14 (s-repair-near-gas-execute-003-v22-routing-001)
parent: s-repair-near-gas-execute-003-v22-routing-001

goal: |
  GasCoopGame's repo-local engineering contract truthfully enforces the executable Plan-to-RED handoff of Direction
  OS contract v22, so a later NearGas BUILD can be authorized only by reviewed immutable RED artifacts rather than
  prose testability claims.

context: |
  Direction OS contract v22 is published at
  C:\my_global_workflow_worktrees\indie-game-development origin/main@
  d18be6e779533932d59383834801dcb0ba850514. Read its v22 clauses first in:
  - os/engineering/CONTRACT_VERSION;
  - os/engineering/CONTOUR.md;
  - os/engineering/VALIDATION.md;
  - os/engineering/PROJECT_SETUP.md §Re-sync;
  - os/engineering/ESCAPE-CLASSES.md;
  - os/adapters/coding-agent.md, especially the executable RED handoff guard.

  Product authority is exact origin/main@86e7927f82c1e48a9d5ab7255ac8004dc12c10eb. Product `AGENTS.md` and
  `validation.config` currently stamp contract v21. Create a fresh branch
  `codex/c-exec-gascoopgame-contract-v22-resync-001` from that exact main only after a clean preflight proves the
  base and branch name are still available.

  The triggering NearGas evidence is a verified CHECKPOINT / NOT DELIVERED on
  `codex/c-exec-near-gas-core-authority-001-execute-003@86e7927f82c1e48a9d5ab7255ac8004dc12c10eb`:
  0 commits, 0 changed files, no independent RED commit and 0/29 tests. Binding fresh refutation found that
  AR-01/06/12/13 mix behavioral obligations with path/history/owner/review/gate evidence; F5 does not yet expose a
  complete all-result-fields plus pending-impulse comparison API; and the CsCheck 3.2.2 property text names seed,
  shrinking and 1,024 cases without a compile-ready invocation. The historical v21 29/29 review is planning history,
  not BUILD authority.

  Contract v22 is additive. Its required handoff is:
  PLAN or PLAN-AMEND -> separate fresh RED-FREEZE -> binding fresh artifact review -> fresh BUILD. Before RED-FREEZE,
  every atomic obligation is classified exactly once as `behavioral-red` or `evidence-only`, and every mixed row is
  split. Only `behavioral-red` rows enter the RED numerator and each names a test file/method plus an exact
  `fixture | call | observe | source | negative` recipe. Process order, structural review, owner verdicts and final
  gates are `evidence-only`; each names its real evidence venue and stays outside the test count.

  In RED-FREEZE the independent test-author writes the complete test/test-support patch once, commits it without
  production code and runs the repo-native compiler/test command. Existing-surface tests must compile, be discovered
  and fail on behavior. Compile-RED is legal only for a genuinely new frozen production surface and only when every
  diagnostic maps to an exact not-yet-built production symbol. A missing test-local fixture/helper, guessed framework
  API, process row posed as a test, partial suite or unexplained diagnostic is a PLAN gap and returns the complete gap
  list to PLAN-AMEND. The binding fresh reviewer then refutes the actual immutable RED commit, diff and runner output;
  it writes no tests. Only that artifact-backed verdict can open BUILD, whose CALL pins the reviewed RED commit and
  forbids editing or re-authoring it. An affected spec edit invalidates the RED artifact. No parser, regex scanner,
  schema compiler or conformance proxy may replace this semantic/artifact review.

  Mirror the Direction writer evidence guard in the product handback contract: a PLAN/PLAN-AMEND RESULT may route
  only to RED-FREEZE; RED-FREEZE may route only to binding fresh artifact review; BUILD may be opened only when the
  recorded evidence includes exact frozen-spec identity, the split/classification of every atomic obligation, one
  complete tests/test-support-only RED commit, the repo-native command and exact diagnostics, and zero unresolved
  helpers/framework guesses/partial-suite/process-row/unexplained-diagnostic gaps. A prose N/N, skeleton inventory,
  semantic dry-run or named-blocker-only GREEN must checkpoint without BUILD.

boundaries: |
  This is the GasCoopGame v21 -> v22 §Re-sync only. Change only the minimum repo-local contract/process surfaces
  needed to mirror v22: root `AGENTS.md`, `validation.config`, OpenSpec planning guidance/templates,
  `docs/engineering/ESCAPE-CLASSES.md`, and the repo maintenance/friction record. A small re-sync RESULT artifact is
  allowed only if the product run contract requires one. Do not change tools or create a mechanical semantic checker.

  Do not amend, reformat or otherwise touch any file under
  `openspec/changes/c-exec-near-gas-core-authority-001/`, its ADR, ledger, Product RESULT, dashboard, production source
  or existing tests. Do not author RED tests or test support. Do not begin or implement NearGas BUILD. Do not run
  product build/test/Deliver commands, Unity or MCP in this contract-text leg. Validation is limited to read-only
  contract comparison, exact frozen-packet identity checks, `git diff --check` and non-build repository hygiene that
  cannot mutate product files. Do not merge or push.

  Preserve `C:\projects\Unity\GasCoopGame_dev` and every other worktree exactly as found. In particular, do not
  switch, clean, stage or edit the concurrent character worktree/branch. Stop on a moved product main, occupied target
  branch, overlapping contract-surface edit, unavailable authority file or any need to alter the NearGas packet.

  This CALL must return HOME before Direction issues anything else for NearGas. Do not create or propose the separate
  NearGas PLAN-AMEND CALL, RED-FREEZE CALL or BUILD CALL. Do not author the next Direction CALL.

done_when: |
  1. Preflight records exact product origin/main@86e7927f82c1e48a9d5ab7255ac8004dc12c10eb, a clean source worktree,
     unused target branch, current v21 stamp, and a preservation manifest for foreign worktrees.
  2. The root GasCoopGame run contract mirrors the four-session v22 boundary exactly: PLAN/PLAN-AMEND closes;
     independent RED-FREEZE authors and commits the full behavioral test/support artifact; binding fresh review
     refutes that artifact; only then may a fresh BUILD reuse it without edits.
  3. Repo-local planning/OpenSpec guidance requires every atomic obligation to be classified once as
     `behavioral-red` or `evidence-only`, requires mixed rows to split, keeps evidence-only rows out of the RED
     numerator, and gives each class the exact required recipe or real evidence venue.
  4. The repo-local handback/writer guard records the exact frozen spec, obligation classification, immutable
     tests/test-support-only RED commit, diff, repo-native command and exact diagnostics; it rejects prose N/N and
     every unresolved helper, guessed framework call, partial suite, process row or unexplained diagnostic.
  5. Existing-surface assertion-RED and the narrow genuinely-new-surface compile-RED exception are distinguished;
     affected spec edits invalidate RED; the BUILD handoff pins the reviewed commit and forbids test re-authoring.
  6. `docs/engineering/ESCAPE-CLASSES.md` gains the v22 evidence-class-integrity class and the witnessed NearGas
     0/29 case without weakening existing rows; no parser/scanner/conformance gate is introduced.
  7. `validation.config` stamps `synced_contract_version` exactly 22 and the maintenance/friction record identifies
     this v21 -> v22 §Re-sync and its evidence limit. No claim of feature delivery or executable NearGas readiness is
     made.
  8. Frozen NearGas packet/ADR/ledger/RESULT/dashboard, product source, tests and tools are byte-identical to base;
     the EXECUTE-003 branch/history and every foreign worktree are untouched. Exact before/after Git-blob identities
     are reported for the frozen packet.
  9. `git diff --check` and applicable non-build hygiene are green. Product build, tests, Deliver, Unity/MCP, RED,
     feature review, merge and push are explicitly recorded as NOT RUN / OUT OF SCOPE for this re-sync-only leg.
  10. The contract-only changes are committed on the dedicated branch and returned HOME as RE-SYNC COMPLETE /
      PRODUCT FEATURE NOT DELIVERED. No NearGas PLAN-AMEND, RED-FREEZE or BUILD CALL exists in the product return.

return: |
  Product CONTRACT-v22 RE-SYNC RESULT HOME with base/branch/commit; exact changed paths; v21 -> v22 clause map;
  synced_contract_version 22 evidence; frozen NearGas before/after blob identities; foreign-worktree preservation;
  `git diff --check` and non-build hygiene output; explicit NOT RUN list for product build/tests/Deliver/Unity/RED/
  feature review/merge/push; rollback command; and confirmation that no NearGas packet, tests, production, tools or
  downstream CALL changed. If any done_when item cannot be met, return CHECKPOINT / NOT DELIVERED with the exact
  blocker and no downstream CALL.

budget: one focused contract-text §Re-sync leg; checkpoint rather than expand scope
surface: any

END_OF_FILE: live/indie-game-development/work/c-exec-gascoopgame-contract-v22-resync-001-call.md
