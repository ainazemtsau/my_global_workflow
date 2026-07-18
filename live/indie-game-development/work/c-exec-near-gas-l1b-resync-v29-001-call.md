# CALL c-exec-near-gas-l1b-resync-v29-001

to: executor
direction: indie-game-development
track: contract-sync
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: L1B-Capture
issued: 2026-07-18 (s-work-near-gas-l1b-resync-v29-dispatch-001)
engineering_contract: re-sync:29

goal: |
  GasCoopGame dev enforces engineering contract v29, including the applicable v28 HOME authority and the
  hot-safe v29 pin/pair route, while every pre-v29 NearGas artifact and lineage remains unchanged and no product
  feature work occurs.

context: |
  Exact owner authority for this launch:
  «Запускай v29 rescue-route для NearGas L1B. Разрешаю самостоятельно создать и координировать Local-задачи в
  indie-game-development, GasCoopGame_dev и GasCoopGame_win-u3, пересылать CALL/HOME до окончательного результата.
  Сначала hot-safe product re-sync v27→v29 через WIN-CTRL; затем закрыть legacy cap-route без successor и открыть
  новый root engineering_contract: 29. Новый root без изменений принимает frozen PLAN/decision/spec
  c-exec-near-gas-l1b-plan-001; без нового owner interview и без 400-line cap. Качество и независимые gates не снижать».

  Launch authority is the current product root AGENTS.md owner-direct rule. The owner explicitly selected WIN-CTRL;
  therefore this task runs only in `C:\projects\Unity\GasCoopGame_dev`, Codex target Local, on its current `dev`
  branch. Fresh-read actual bytes before any edit and preserve them. Direction does not authorize any other checkout.

  launch:
    lane: control / engineering-contract re-sync only
    venue: owner-selected WIN-CTRL / C:\projects\Unity\GasCoopGame_dev / current branch dev / Target Local
    machine: PC
    base: fresh current WIN-CTRL dev state at task start; observed 2026-07-18 HEAD 06b8a6e26cd562fb4650e15552f42794fd2cf291 is evidence only, never a reset target
    conflict_surface: product control-plane authority only; no feature, frozen-plan, NearGas source, RED or candidate bytes
    depends_on: product stamp v27 plus Direction tags engineering-contract-v28 and engineering-contract-v29
    merge_queue: n/a — stay on dev; do not merge to main or push in this bounded re-sync
    gates: pre-upgrade v27 run contract; repo-native control-plane seeded misses/checks; fresh independent read-only review of the exact re-sync diff

  Fresh readback at dispatch found `validation.config: synced_contract_version = 27`,
  `obligation_inventory_version = 27`, `obligation_ceiling = 239`, and
  `obligation_inventory_source = 64736ecf6071e7ecd26f7e73e87e126b8cbfa0ad`. WIN-CTRL was on `dev`, clean,
  ahead of `origin/dev` by 7, at 06b8a6e26cd562fb4650e15552f42794fd2cf291. These are dispatch evidence;
  re-read them and STOP on incompatible fresh state rather than overwriting it.

  Exact Direction authority sources are the immutable my_global_workflow tags:
  - v27 base: `engineering-contract-v27^{commit}` = 64736ecf6071e7ecd26f7e73e87e126b8cbfa0ad;
  - applicable v28 delta: `engineering-contract-v28^{commit}` = 9d6e182bad4938a1ec8c23a2dcba5031df8303fc;
  - terminal v29 authority: `engineering-contract-v29^{commit}` = 8d2f0866c3e4a9c2f4a41eb60d8fef22584a0a1c.
  The authoritative current texts are `os/engineering/{CONTOUR,VALIDATION,PROJECT_SETUP,OBLIGATION_INVENTORY}.md`,
  `os/engineering/profiles/unity.md`, `os/engineering/CONTRACT_VERSION`, `os/schema/packets.md`, and the Role-1
  engineering pin guard in `os/adapters/coding-agent.md` at the v29 tag. Use their exact v27→v28 and v28→v29
  deltas; do not reconstruct retired v22/v23 migrations by memory.

  Applicable v28 outcome: every engineering stage returns the current CALL's HOME handback even at a fresh-stage
  boundary; it names eligibility or the blocker only, never authors or asks for a successor; Direction alone issues
  successors. Inventory X41(v27) is replaced by X41(v28), with total obligation ceiling still 239.

  Terminal v29 outcome for newly pinned compiled legs: root CALLs carry an integer contract pin and same-leg
  successors inherit it; pre-v29 unmarked calls plus their `legacy:<origin-call-id>` successors retain their recorded
  route across Re-sync; `re-sync:29` changes repo authority only. PLAN hands to one separate PAIR-CANDIDATE job, then
  binding fresh PAIR-FREEZE refutation, then fresh BUILD. A fresh contract-author independent from BUILD/validation
  may stabilize permitted non-behavioral public carrier gaps and immutable RED in that one bounded candidate job.
  Final evidence pins exact carrier commit/manifest followed by exact RED commit/manifest; real signatures,
  field-preserving value/data construction, trivial reachability, build+hygiene/Unity sidecars after the last carrier
  edit, and real compile/discovery/behavioral-failure evidence remain required. The owner-approved decision page stays
  <=400 words, but there is no production-source line cap. Behavioral/out-of-plan changes return a blocker. Fresh
  refutation freezes the public contract and RED; BUILD implements internal HOW and edits neither. No independent
  author, immutable RED, fresh refutation, mutation, NegativeControl, property, review, Deliver or G5 gate is reduced.
  Inventory replaces X33a/X33b(v28) with X33a/X33b(v29), applies the current reworded G33/X07-X09/X18/
  X34a-X34b/X75-X76/E06-E07/E09-E12/E15/U20a-U20b rows, and remains N=239.

  Frozen legacy authority includes the entire committed
  `openspec/changes/c-exec-near-gas-l1b-plan-001/**` PLAN/decision/spec set, carrier chain through `de1cc87c`, prior
  RED `0d0cea14`, their reviews/results/ADR/registry records, and all current NearGas production/test bytes. Re-sync
  does not reinterpret, migrate, rebase, edit, archive or retire them. The existing Direction cap-reconciliation CALL
  remains a pre-v29 legacy snapshot until a later Direction transaction consumes this HOME.

boundaries: |
  This is a bounded no-feature contract install. Do not change `Assets/**`, gameplay/product behavior, NearGas source,
  product tests or test-support for a feature, frozen OpenSpec PLAN/decision/spec/tasks, candidate/RED artifacts,
  reviews/results/ADR belonging to active legacy legs, registry lifecycle of those legs, scenes, packages or project
  settings. Dedicated control-plane contract/check documentation, config, scripts and seeded-miss tests may change only
  where required to make v28+v29 authority true and verifiable.

  Stay on the existing WIN-CTRL `dev` branch. Do not create, switch, rename, reset or delete a branch; do not checkout,
  stash, clean, rebase, merge, push, force, discard, overwrite or normalize unrelated tracked/untracked bytes. Do not
  touch WIN-U3 or any other workspace from this CALL. Do not merge to main. A fresh-state collision or inability to
  preserve bytes is a STOP with exact evidence.

  Do not perform PLAN, PLAN-AMEND, SURFACE-FREEZE, RED-FREEZE, PAIR-CANDIDATE, PAIR-FREEZE, BUILD, mutation, gameplay
  review or L1B G5. Do not create or propose the new v29 NearGas feature root, a legacy feature successor, or any
  successor CALL. Do not modify the 400-word decision-page limit; remove only the retired 400 production-source-line
  cap for v29-pinned legs. Do not apply v29 evidence retroactively to the legacy cap route.

done_when: |
  1. Fresh pre-state evidence records WIN-CTRL path, Target Local, current branch `dev`, exact HEAD/status and product
     stamp/inventory v27; all existing tracked and untracked bytes are preserved outside the declared control-plane diff.
  2. The applicable v28 HOME rule is installed in product run authority: every stage returns its current HOME,
     successors belong only to Direction, X41(v27) is replaced by X41(v28), and obligation count remains 239.
  3. Product run authority and validation/config surfaces enforce the v29 engineering pin semantics, legacy snapshot
     preservation, bounded `re-sync:29`, and compiled PLAN→PAIR-CANDIDATE→fresh PAIR-FREEZE refutation→BUILD route.
  4. The v29 pair contract retains the <=400-word owner-approved decision page and every existing independent quality
     gate, but contains no production-source line cap; a seeded/readback check proves retired cap wording cannot govern
     a new `engineering_contract: 29` root while remaining available to pre-v29 legacy lineages.
  5. The exact v29 obligation inventory disposition is recorded: X33a/X33b(v28) replaced by v29, all named reworded rows
     present, `obligation_inventory_version: 29`, `obligation_ceiling: 239`,
     `obligation_inventory_source: 8d2f0866c3e4a9c2f4a41eb60d8fef22584a0a1c`, and `synced_contract_version: 29`.
  6. Repo-native targeted control-plane tests/seeded misses and the full applicable one-command check are GREEN, then a
     fresh independent read-only review of the exact committed re-sync diff finds no unresolved in-scope issue or the
     task returns the complete blocker; no quality or independence gate is waived.
  7. Git evidence proves no diff under `openspec/changes/c-exec-near-gas-l1b-plan-001/**`, NearGas product/test paths,
     carrier/RED artifacts or unrelated dirty state; no feature work, branch action, reset/stash/clean, merge or push
     occurred. The bounded re-sync is committed on the existing local `dev` branch with a descriptive commit.
  8. HOME dispositions all preceding seven bullets and returns exact commits/manifests/check outputs/review evidence plus one
     eligibility statement: Direction may close this re-sync call, close legacy
     `c-exec-near-gas-l1b-surface-cap-reconcile-001` without successor under the quoted owner authority, and only then
     issue a new root pinned `engineering_contract: 29` that accepts frozen `c-exec-near-gas-l1b-plan-001` unchanged,
     without a new owner interview and without a production-source line cap. Product authors no successor CALL.

return: |
  Product RE-SYNC v29 RESULT HOME: status GREEN or exact blocker; CALL id and `engineering_contract: re-sync:29`;
  owner-selected WIN-CTRL/GasCoopGame_dev/Target Local/current-dev proof; pre/post HEAD, status and complete control-plane
  manifest; exact v28 HOME/X41 disposition; exact v29 pin/legacy/pair/no-source-line-cap/inventory disposition;
  final validation.config stamp/provenance; targeted seeded-miss and full-check outputs; fresh independent review
  artifact and finding dispositions; commit id; byte-preservation proof for frozen PLAN/decision/spec, legacy
  cap/carrier/RED and unrelated state; explicit no-feature/no-branch-action/no-merge/no-push cuts; assumptions/cost;
  dispositions for done_when 1-8; and the exact Direction eligibility statement from bullet 8. No successor CALL.

budget: one bounded control-plane re-sync leg; <= one focused half-day; STOP on fresh-state collision, gate regression or scope expansion
surface: Codex Desktop, owner-selected WIN-CTRL project with Target Local

END_OF_FILE: live/indie-game-development/work/c-exec-near-gas-l1b-resync-v29-001-call.md
