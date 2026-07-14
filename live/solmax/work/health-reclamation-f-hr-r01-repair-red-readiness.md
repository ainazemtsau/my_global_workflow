# RED readiness — F-HR-R01 bounded repair

status: RED_READY
date: 2026-07-14
direction: solmax
node_task: g-operating-substrate-first-process-creator/t-4
review_class: fresh read-only full-packet semantic dry-run
product_mutation_in_this_preflight: none
direction_lifecycle_mutation_in_this_preflight: none
test_skeleton_count: 28
unresolved_cell_count: 0
inferred_cell_count: 0

## Disposition

The owner-approved repair is safe to dispatch as one bounded product executor
leg. The only candidate semantic targets are the Q2 projection rows OP-HR01
and KH-HR01. Direct evidence reconciliation is limited to the existing author
self-check and the current root closing report. Every other candidate,
architecture, history and lifecycle surface is protected.

This RED_READY disposition is valid only for the exact clean baseline below.
Any baseline drift, plan/spec amendment, newly discovered class sibling or need
for another changed path invalidates this record and returns the leg BLOCKED
before any product edit.

## Exact baseline and authority

- product worktree: C:/projects/solmax-operating-substrate
- branch: codex/health-reclamation-candidate-build
- base commit: b23eb0bb208a6b2344043ac472621093132dadc9
- base tree: 813384e85f1723bfdadc70d2f3c3f6c9a520a077
- working tree at preflight: clean
- product contract stamp: validation.config synced_contract_version 21
- Direction engineering contract: current 21
- owner-approved plan:
  C:/my_global_workflow_worktrees/solmax/live/solmax/work/health-reclamation-f-hr-r01-repair-plan-v1.md
- owner words:
  "A — исправляем только две классификации в правильном репозитории, сохраняя весь текущий прогрес"

Baseline blobs used by the dry-run:

| Surface | Blob at base |
|---|---|
| packs/health-reclamation/verification/scope-coverage.md | 23cc3ce81b809f90151194057c998d7c796e92b3 |
| docs/results/health-reclamation-v1-self-check.md | c6d3cfc5742bbaf7a89493fe38e4266e993a918b |
| RESULT.md | 52f1a76a891a172e04e0b9ed11be2a1e2eb3116b |
| docs/reviews/review-health-reclamation-v1.md | 41d1c21d38113a7ab44aafd64deef4e06278d3cd |
| packs/health-reclamation/policy.md | 452157116a04d65bfeedb736925439e8f9e5647f |
| packs/process-creator/procedures/02-discover-and-classify.md | 42beeeadc934f158de3c0956f90cd2fd654625d8 |

Authority used for semantic judgment:

1. the owner-approved bounded repair plan;
2. accepted Q2 card
   live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md;
3. product policy Primary normative ownership and current-run privacy/source
   distinctions;
4. Process Creator procedure 02 exact-one classification rule;
5. historical review 007 and aligned RESULT at b23eb0b.

Legacy Direction Health, Health AI, Health HQ and live/health were not read,
imported or used as authority. Saved health research and process intent were
not reopened; the repair does not need them.

## Frozen product diff boundary

Exactly three product paths may differ from the baseline:

1. packs/health-reclamation/verification/scope-coverage.md
   - semantic changes only to the stable rows OP-HR01 and KH-HR01;
   - every other row and section remains unchanged.
2. docs/results/health-reclamation-v1-self-check.md
   - only the directly affected Q2 atomic-ownership statement,
     REVIEW item 2 statement, duplicate-primary-owner sweep statement and the
     F-HR-R01 repair class/sweep record may change or be added;
   - F-A01 through F-A06 and all unrelated evidence remain unchanged.
3. RESULT.md
   - align the current repair handback, exact diff, gates, lifecycle boundary
     and later fresh-refutation route;
   - cite review 007 as immutable historical FAIL evidence, never as a repaired
     or passing review.

No new product file is allowed. In particular, the repair executor does not
edit or create a review artifact. The later fresh reviewer owns a distinct
review record after the repair commit exists.

## Complete obligation and test-skeleton packet

The Markdown substrate has no compiled-code mutation/property subject matter.
No row below is discharged as n/a: semantic properties and their deliberately
wrong shapes are explicit, while tools/selfcheck.py remains only the existing
wiring-gate negative control.

### R01 — exact dispatch baseline (property)

- fixture: clean C:/projects/solmax-operating-substrate at the full base commit,
  base tree and contract stamp recorded above.
- call: read-only git rev-parse HEAD, git status --porcelain, base-tree
  comparison and validation.config stamp comparison before editing.
- observe: HEAD equals b23eb0bb208a6b2344043ac472621093132dadc9,
  status is empty, tree equals 813384e85f1723bfdadc70d2f3c3f6c9a520a077
  and both contract versions equal 21.
- source: approved repair plan Starting point; CALL 009 context; contract v21.
- negative: any different HEAD/tree, dirty path or contract mismatch blocks
  before the first edit.

### R02 — approved contour is complete (acceptance)

- fixture: owner-approved repair plan v1 and the exact owner words recorded
  above.
- call: compare every intended executor mutation and claim to Approved repair,
  What must remain unchanged and Done when.
- observe: the intended semantic delta is only the two Q2 projection
  corrections plus direct evidence/report reconciliation.
- source: health-reclamation-f-hr-r01-repair-plan-v1.md.
- negative: any need to change behavior, policy, routing, procedure, kernel,
  Process Creator semantics or another classification row blocks the leg.

### R03 — OP-HR01 process rule classification (acceptance)

- fixture: OP-HR01 at base, policy Primary normative ownership, and the Q2
  Process-pack declarations class.
- call: semantically restate the atomic claim as the Health rule that accepts
  only bounded current owner choices, then classify that rule.
- observe: the classified rule has exactly one primary class,
  process-pack declaration, and primary normative owner Health Reclamation
  pack.
- source: repair plan Approved repair item 1; policy lines 24-34; accepted Q2
  Architecture classes and Classification rule.
- negative: owner-profile concern, owner as the architecture-class owner, two
  primary classes, or an unclassified mixed claim fails.

### R04 — OP-HR01 current-input/source boundary (property)

- fixture: corrected OP-HR01 rule and policy definitions for current owner
  intent, private readiness disposition and current run context.
- call: trace goal, willingness, legitimate choice, language, cue and
  non-descriptive readiness disposition through source, variation owner,
  retention and cross-process reuse.
- observe: the owner remains the bounded current decision/input/source and
  legitimate variation owner; values expire with the run and do not become
  owner-wide profile truth.
- source: policy Primary normative ownership, Privacy and Information
  distinctions; accepted Q2 Owner-profile concerns.
- negative: persistence, automatic reuse across processes, profile promotion
  or pack invention of a current choice fails.

### R05 — KH-HR01 Health routing-rule classification (acceptance)

- fixture: KH-HR01 at base, policy Private readiness and legitimate action
  source, and the Q2 Process-pack declarations class.
- call: semantically restate the atomic claim as the Health rule that routes
  applicable medical/professional judgment to a qualified human, then classify
  that rule.
- observe: the routing rule has exactly one primary class,
  process-pack declaration, and primary normative owner Health Reclamation
  pack.
- source: repair plan Approved repair item 2; policy lines 140-166; accepted
  Q2 Architecture classes and Classification rule.
- negative: inherited human-authority application, a sixth class, kernel,
  owner-profile or double ownership fails.

### R06 — KH-HR01 qualified-human source/authority boundary (property)

- fixture: corrected KH-HR01 rule and policy authority/effect boundaries.
- call: trace who supplies, scopes, varies and authorizes the bounded judgment
  independently from who owns the Health routing rule.
- observe: the applicable qualified human remains the external source and
  authority holder for that judgment; the pack records dependency and bounds
  without acquiring medical authority.
- source: policy Primary normative ownership and Authority, safety, and
  effects; Process Creator procedure 02 steps 6-7.
- negative: treating the qualified human as an architecture class or allowing
  the pack/AI to issue, certify, broaden or override the judgment fails.

### R07 — exact-one accepted Q2 class (property)

- fixture: corrected OP-HR01 and KH-HR01 rows plus the accepted five-class Q2
  set.
- call: count primary architecture class assignments per corrected atomic row
  and compare each token to the accepted class set.
- observe: each row has exactly one accepted primary class and dependencies,
  source, variation owner and authority remain separate columns.
- source: accepted Q2 Unit of classification, Architecture classes and
  Classification rule; Process Creator procedure 02 steps 3-8.
- negative: zero, two or more classes, a sixth class, or a dependency encoded
  as normative ownership fails.

### R08 — no new shared architecture (property)

- fixture: corrected rows and the existing statement that no accepted reusable
  service semantic is introduced.
- call: compare the repair delta to every Q2 class and the existing no-service
  conclusion.
- observe: no invariant, reusable-service, owner-profile or implementation
  semantic is created or promoted; only two local pack-rule classifications
  are corrected.
- source: scope-coverage no-reusable-service paragraph; accepted Q2 promotion
  criteria; approved plan.
- negative: a new service contract, kernel guarantee, owner-profile entry,
  adapter rule or architecture class fails.

### R09 — exact changed-path allowlist (property)

- fixture: base commit and the three-path allowlist in Frozen product diff
  boundary.
- call: git diff --name-only from b23eb0b to the repair HEAD and compare as a
  set.
- observe: the set is exactly scope-coverage.md,
  health-reclamation-v1-self-check.md and root RESULT.md.
- source: approved repair item 3 and this readiness record.
- negative: any fourth path, missing required reconciliation path or new file
  fails and blocks commit.

### R10 — non-target hunks remain byte-preserved (property)

- fixture: base blobs for scope-coverage.md and the author self-check.
- call: inspect the complete textual diff, keyed by OP-HR01, KH-HR01 and the
  named self-check targets rather than by line number.
- observe: scope-coverage changes only OP-HR01/KH-HR01; self-check changes only
  the directly affected Q2 statements and F-HR-R01 class/sweep record.
- source: Frozen product diff boundary; review 007 Exact defect.
- negative: edits to HR-01..HR-17, K/PC/PP/AI rows, F-A01..F-A06 or unrelated
  prose fail.

### R11 — author self-check reconciliation (acceptance)

- fixture: base self-check Q2 atomic ownership row, REVIEW item 2 row,
  duplicate-primary-owner sweep row and author-findings table.
- call: reconcile those stable targets with the corrected projection and add
  the repair finding's author-only class/sweep evidence.
- observe: the report no longer asserts the old false mapping; it records
  F-HR-R01 as author-repaired and awaiting a new independent refutation, while
  every unrelated author conclusion is preserved.
- source: review 007 F-HR-R01 and Author findings and sibling sweeps; approved
  repair item 3.
- negative: structural PASS/admission language, deletion of prior author
  findings or an unrecorded repair sweep fails.

### R12 — current root RESULT reconciliation (acceptance)

- fixture: base RESULT.md, repaired diff and exact gate outputs at repair HEAD.
- call: align the current closing report fields outcome, evidence, assumptions,
  cuts, cost, manual-acceptance and next.
- observe: the report names base and repair commit, exact changed paths,
  F-HR-R01 author-repair evidence, preserved review 007 FAIL, all lifecycle
  limits, exact gates and return to Solmax for a separate fresh review.
- source: root AGENTS.md report contract; approved repair items 3-4.
- negative: stale claim that no repair occurred, fabricated fresh-review PASS,
  missing changed path/gate, or admission/activation claim fails.

### R13 — review 007 is immutable historical evidence (property)

- fixture: protected review blob
  41d1c21d38113a7ab44aafd64deef4e06278d3cd and its b23eb0b disposition.
- call: compare the review path blob at repair HEAD and inspect all new
  references to F-HR-R01.
- observe: the review blob is identical and still records OPEN/BLOCKING at its
  reviewed basis; new reports distinguish author repair from later binding
  verification.
- source: approved repair item 3; review 007 Finding F-HR-R01.
- negative: editing the review to fixed/PASS, erasing the finding or presenting
  it as review of the repaired commit fails.

### R14 — class-level sibling sweep and fix closure (acceptance)

- fixture: invariant/class token
  Q2 atomic-classification / evidence-integrity defect, the two known sites and
  the complete current projection.
- call: semantically sweep every projection row for process-specific current
  facts mislabeled owner-profile, non-five-class labels, mixed rule/source
  ownership and authority encoded as class.
- observe: only OP-HR01 and KH-HR01 require in-scope correction; the repair
  report records class, sites, dispositions and controls, with no other sibling.
- source: review 007 sibling sweep; engineering VALIDATION fix-class-closure;
  accepted Q2 rule.
- negative: a hollow "searched" statement, missing site, renamed class, or any
  newly found sibling outside the allowlist blocks rather than expands the
  diff.

### R15 — product ancestry and prior progress remain intact (property)

- fixture: preserved chain da9d95b -> e0f7db4 -> c184b36 -> b23eb0b and the
  repair commit to be created.
- call: verify ancestry and compare the base-to-repair commit graph without
  rewriting, squashing or dropping prior commits.
- observe: b23eb0b is the direct or preserved ancestor of the repair commit and
  all earlier candidate/review history remains reachable.
- source: approved plan Starting point and What must remain unchanged.
- negative: reset, force rewrite, dropped commit or replacement from another
  repository fails.

### R16 — repository gates and report completeness (gate)

- fixture: committed or staged bounded repair candidate and aligned RESULT.md.
- call: run python tools/check.py, python tools/selfcheck.py and
  python tools/check.py --deliver at the repair HEAD.
- observe: all three exit zero; exact stdout is recorded in RESULT.md and the
  executor return.
- source: product AGENTS.md Commands and run contract; approved plan item 4.
- negative: any nonzero exit, omitted output, skipped gate or workaround is a
  block; no gate is allowed to judge Q2 meaning.

### R17 — Health behavior surfaces remain unchanged (property)

- fixture: base README.md, contract.md, policy.md, routing.md,
  continuation.md, procedures/01-08 and verification/scenarios.md.
- call: compare every listed blob/path from b23eb0b to repair HEAD.
- observe: every listed behavior/source/continuation artifact is unchanged.
- source: approved plan What must remain unchanged; review 007 HR-01..HR-17
  and S01..S16 preservation evidence.
- negative: any wording or behavior change in those surfaces fails even if a
  gate remains green.

### R18 — existing semantic evidence remains preserved (property)

- fixture: HR-01..HR-17 rows, S01..S16 scenarios and F-A01..F-A06 author
  findings at b23eb0b.
- call: compare all non-target rows and the historical review's dispositions
  against the repair HEAD.
- observe: the 17 behavior obligations, 16 scenarios and six prior fixes are
  unchanged; only the Q2 projection/report defect is repaired.
- source: review 007 Frozen plan and acceptance ledger, Adverse scenario
  refutation, and Author findings and sibling sweeps.
- negative: reopening, deleting, rewriting or claiming a new verdict for any
  preserved row fails.

### R19 — architecture, creator and tooling are frozen (property)

- fixture: kernel/, services/, adapters/, packs/process-creator/, tools/,
  AGENTS.md, validation.config and openspec/ at b23eb0b.
- call: compare path trees and the full base-to-repair name/status diff.
- observe: every listed surface is unchanged; contract stamp remains 21.
- source: approved plan What must remain unchanged; product Constitution.
- negative: kernel/creator semantic edits, service promotion, adapter changes,
  new checker/scanner, OpenSpec amendment or contract re-sync fails.

### R20 — owner intent, research and legacy sources stay outside the leg (property)

- fixture: the explicit source allowlist in this record and the product
  evidence at b23eb0b.
- call: record every source actually used by the executor and compare it to the
  allowlist before reporting completion.
- observe: no saved process description or health research is reopened or
  changed, and no Direction Health, Health AI, Health HQ or live/health source
  is used or cited as authority.
- source: owner instruction in CALL 009; approved plan Starting point and What
  must remain unchanged.
- negative: needing or using any excluded source blocks the leg; the executor
  must not ask the owner to repeat it.

### R21 — no personal health data (negative-control)

- fixture: the complete repair diff, report, commit message and executor return.
- call: semantic privacy read of every new line and reported input.
- observe: only architecture IDs, file paths, statuses and abstract boundaries
  appear; no owner-linked health fact, research detail or inferred health data
  appears.
- source: product policy Privacy, residency, and retention; product
  Constitution public-repo rule.
- negative: any symptom, diagnosis, metric, treatment, readiness reason or
  other personal health detail blocks completion and is not preserved.

### R22 — lifecycle separation and t-4 status are preserved (property)

- fixture: review 007 separated verdicts, product policy lifecycle boundary and
  live/solmax/NOW.md t-4 at preflight.
- call: compare every lifecycle claim in the repaired projection, self-check,
  RESULT and executor return; verify the product leg has no Direction diff.
- observe: review 007 remains historical structural FAIL; repaired candidate
  structural status is awaiting fresh refutation, never PASS; admission and
  activation are NOT_PERFORMED; useful-live, reliability and reuse remain not
  proven; t-4 remains active.
- source: approved plan What must remain unchanged and Done when; review 007.
- negative: task close, admission, activation, live/reuse promotion or
  Direction state edit fails.

### R23 — no process execution or effect (negative-control)

- fixture: complete executor action log, product diff and reports.
- call: classify every action as repository-local repair, gate or report work.
- observe: no Health Reclamation admission, activation, intervention, live run,
  monitoring, message, booking, purchase, scheduling, device action or other
  external effect occurs.
- source: CALL 009 boundaries; product policy Authority, safety, and effects.
- negative: any attempted or claimed process/effect action blocks and cannot be
  normalized into repair evidence.

### R24 — green wiring never becomes semantic proof (property)

- fixture: three gate outputs and repaired author evidence.
- call: inspect every conclusion that cites a gate or file presence.
- observe: gates support wiring/report completeness only; semantic correction
  remains author evidence pending a new fresh-session refutation.
- source: product AGENTS.md Constitution item 3; review 007 Gates, limits and
  return route.
- negative: "gate PASS therefore structurally admissible/fixed/admitted" fails.

### R25 — later fresh-refutation handoff is complete (handoff)

- fixture: repair commit, exact diff, class+sweep record, gate outputs,
  preserved review 007 and current RESULT.
- call: build the return route to Solmax without authoring the downstream
  Direction CALL.
- observe: the handoff names the repair commit and asks a distinct fresh
  read-only reviewer to refute both corrected rows, all preservation
  properties, sibling sweep and lifecycle separation before any disposition.
- source: approved repair item 4 and Done when; KERNEL G5.
- negative: no repair commit, missing evidence pointer or a route directly to
  admission/activation fails.

### R26 — repair author and fresh reviewer remain separate (negative-control)

- fixture: repair executor identity, product diff and docs/reviews tree.
- call: compare authorship/session identity and review-file changes.
- observe: the repair executor creates no new review artifact, leaves review
  007 untouched and makes no binding fresh-refutation claim.
- source: product run contract; approved plan item 4; direction-os fresh G5
  rule.
- negative: self-authored new review, edited historical review or same-session
  binding verdict fails.

### R27 — any contour drift fails before mutation (negative-control)

- fixture: exact baseline, plan, allowlist and 28-row packet.
- call: recheck them immediately before build and again before commit.
- observe: no drift exists; otherwise the executor returns one precise blocker
  with no partial commit or scope expansion.
- source: contract v21 amendment rule; approved plan stop condition.
- negative: silent rebase, inferred requirement, extra file, new sibling,
  changed plan/spec or partial apply fails.

### R28 — executor return is fully reconciled (acceptance)

- fixture: R01-R27 and the final product HEAD.
- call: give every row one explicit MET or BLOCKED disposition and attach the
  named evidence; count blank, inferred, unresolved and n/a cells.
- observe: RED repair handback is legal only with 28 explicit dispositions,
  zero blank/inferred/unresolved/n/a cells and the complete evidence requested
  by the executor CALL.
- source: contract v21 Plan-to-RED readiness; CALL 009 done_when and return.
- negative: any missing row/evidence, compressed "all passed", inferred fact or
  unresolved cell blocks the handoff.

## Done-when reconciliation

| Required contour | Skeletons | Disposition |
|---|---|---|
| both Q2 corrections | R03-R08 | complete |
| diff containment | R09-R10, R17-R19 | complete |
| preservation of semantics and history | R13, R15, R17-R24 | complete |
| legacy-Health exclusion and privacy | R20-R21 | complete |
| lifecycle separation and t-4 active | R22-R24 | complete |
| direct evidence/report reconciliation | R11-R14 | complete |
| sibling sweep and fix-class closure | R14 | complete |
| repository gates | R16, R24 | complete |
| later fresh-refutation handoff | R25-R26 | complete |
| base/amendment fail-fast | R01-R02, R27 | complete |
| zero ambiguity and exact return | R28 | complete |

## Final count

- acceptance/property/negative/gate/handoff skeletons: 28
- skeletons with fixture: 28
- skeletons with call: 28
- skeletons with observe: 28
- skeletons with source: 28
- skeletons with negative: 28
- unresolved cells: 0
- inferred cells: 0
- product edits performed by this preflight: 0
- lifecycle actions performed by this preflight: 0
- executor CALL:
  live/solmax/work/calls/c-solmax-operating-substrate-first-process-creator-t4-health-reclamation-f-hr-r01-bounded-repair-010.md

END_OF_FILE: live/solmax/work/health-reclamation-f-hr-r01-repair-red-readiness.md
