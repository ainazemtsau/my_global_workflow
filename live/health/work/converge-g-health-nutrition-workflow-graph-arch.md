---
# Converge-Arch — g-health-nutrition-workflow-graph

> Produced by converge-arch session s-health-nutrition-workflow-converge-arch-001 on 2026-06-17.
> Assembly surface only; not a Direction OS state file.
> Scope: architecture/contract surface for the workflow graph overlay on g-health-nutrition-system.
> Authority: closed workflow WHAT in `live/health/work/converge-g-health-nutrition-workflow-graph.md`
> + existing nutrition W/NCA architecture as seed evidence only.
> Status: CLOSED ARCH, route to converge-verify.

## §READ / EVIDENCE

- E1 — Workflow graph WHAT is closed in `live/health/work/converge-g-health-nutrition-workflow-graph.md`
  with WG1-WG14 all answered.
- E2 — Existing nutrition module W1-W13 / NCA0-NCA9 / B1-B3 architecture remains valid seed evidence in
  `live/health/work/converge-g-health-nutrition-system.md` and
  `live/health/work/converge-g-health-nutrition-system-arch.md`; it does not prove WG1-WG14 coverage.
- E3 — Binding prior G5 says nutrition artifacts existed at health-ai commit
  `b421b94496c4c1f96b6173edd3c98fcc2f0b9fa4`, but the owner-facing startup UX was later rejected as
  missing an explicit workflow graph.
- E4 — Health AI already defines provider-independent roles, free-form owner input, writer packets,
  nutrition namespace boundaries, and operator-invoked nutrition seams.
- E5 — Product evidence shows active program/cycle/menu/grocery/fallback/LOG/review files, but no explicit
  canonical workflow graph or startup router artifact.
- E6 — Parallel child miner + strategic_search pre-pass returned two decisive gaps: no product-side router/
  current-state contract yet, and writer validation still names W/NCA/B acceptance rather than WG1-WG14.

## §BOUNDARIES

- This artifact defines contracts only. It does not start nutrition execution.
- No menu, recipe, grocery list, shopping instruction, daily plan, daily nutrition LOG, or food diary is produced.
- No product repo code or files are edited in this session.
- Health AI owner input remains free-form text/voice/photo; templates are internal parser/write targets only.
- Direction OS receives summary/decision/problem/CALL only; raw nutrition data remains in Health AI nutrition.
- g-health-core owns phase, week, day, weight_trend, adherence, biofeedback, PLAN-vs-LOG, procedure template,
  schema/versioning, and attach semantics. Nutrition consumes them and writes only nutrition-namespaced state.
- No app UI, server, database, runtime, cron, scheduler, background worker, external recipe service, or
  shopping-service dependency is introduced.

## §DECOMPOSITION

Subsystems for the workflow graph contract:

1. Workflow authority surface — the future product implementation must add a Health AI nutrition workflow graph
   contract, with one row per workflow state and explicit transition/block rules.
2. Current workflow cursor — the future product implementation must expose the current nutrition workflow state
   and the evidence used to resolve it, so startup is not hidden model judgment.
3. Operator router — an operator-invoked nutrition procedure resolves current state, validates drift, and returns
   one bounded task/question/action.
4. State-owned artifacts — program, cycle, week plan, day loop, review, and mutation each own only their allowed
   artifact class and next-state decision.
5. Writer handoff — any durable Health AI change must be one bounded file change or writer packet and must check
   WG1-WG14 in addition to W/NCA/B.
6. Block router — safety, missing material owner facts, workflow ambiguity, stale cursor, or forbidden scope route
   to conservative mode, one material clarifier, review, repair/writer packet, or Direction OS CALL as appropriate.

Sub-node decision:
- No new TREE child is proposed by this converge-arch session. The workflow graph is an overlay contract on
  g-health-nutrition-system; shape may later split product implementation tasks if converge-verify survives.

## §CONTRACTS

Status legend: all rows are `answered`.

### WGA0 — Workflow authority surface

status: answered

contract: |
  Health AI nutrition must add a concrete workflow authority surface before execution:
  `x_nutrition/workflow/graph.md` as the static state graph contract,
  `x_nutrition/state/current-workflow.md` as the current-state cursor/evidence surface, and
  `x_nutrition/procedures/workflow-router.md` as the operator-invoked router procedure.

acceptance: |
  Startup reads the workflow graph and current-state evidence before reading output-heavy nutrition artifacts.
  If either authority surface is missing, stale, or contradictory, startup blocks to a repair/writer packet or
  Direction OS CALL and produces no nutrition execution content.

rejects: |
  Prompt-only router; active-program-as-router; provider-continuation load order as router; Direction OS as raw
  workflow cursor; UI/runtime/scheduler as current authority.

### WGA1 — Startup/router operator contract (WG1)

status: answered

contract: |
  `workflow-router` is the first nutrition-facing operator step. It resolves current workflow state from
  `x_nutrition/state/current-workflow.md`, checks it against graph rules and current artifacts, then returns only:
  current state, one bounded next task/question, whether owner input is needed, and the next action or CALL.

acceptance: |
  A startup response is mechanically rejectable if it emits more than one current state, more than one bounded
  task/question, or any menu/recipe/grocery/shopping/daily-plan/LOG/review wall before the selected state
  authorizes that exact artifact class.

rejects: |
  "Here is the whole nutrition system"; startup dumping active program + first cycle + menu + grocery + recipes
  + LOG + review; startup deriving state silently from broad provider memory.

### WGA2 — State descriptor completeness (WG2)

status: answered

contract: |
  `x_nutrition/workflow/graph.md` must list each state with: purpose, inputs, owner-provided irreducible facts,
  AI-decided facts, allowed output artifact class, allowed next state(s), stop/block conditions, and review trigger.

acceptance: |
  Execution is blocked if any selected state lacks one of those fields. The graph may point to existing product
  files as seed/output families, but the graph row remains the authority for whether that file family may be used.

rejects: |
  Loose file inventory; relying on active artifacts alone; per-state prose without next/block rules.

### WGA3 — Canonical transition contract (WG3)

status: answered

contract: |
  The default transition path is STARTUP_ROUTER -> PROGRAM -> CYCLE -> WEEK_PLAN -> DAY_LOOP -> REVIEW ->
  MUTATION. MUTATION returns to DAY_LOOP, WEEK_PLAN, CYCLE, or PROGRAM by named mutation scope.

acceptance: |
  The router can name the only allowed next states from the graph. Any jump from STARTUP_ROUTER directly into
  multiple output artifacts is a contract failure unless the current state was already resolved to that one
  output-producing state.

rejects: |
  Hidden "AI decides next"; all-artifacts-at-once startup; mutation that regenerates the entire nutrition system.

### WGA4 — Program state contract (WG4)

status: answered

contract: |
  PROGRAM consumes core profile/phase/metrics and nutrition owner-fact/system-decision boundaries, then produces
  or updates only `x_nutrition/programs/*` or one writer packet for that program-level change.

acceptance: |
  PROGRAM may define objectives, success criteria, safety constraints, assumptions, behavioral review triggers,
  and mutation policy. It must not produce menu, recipe, grocery, daily plan, raw LOG, or review output in the
  same owner-facing step.

rejects: |
  Program artifact as startup router; program setup as full execution packet; asking expert variables as owner
  preferences.

### WGA5 — Cycle state contract (WG5)

status: answered

contract: |
  CYCLE consumes active program + core phase/week/day/metrics + known/pending owner facts, then produces or
  updates only `x_nutrition/cycles/*` or a writer packet for that cycle-level change.

acceptance: |
  CYCLE names objective, bounded execution loop, checkpoints/triggers, tracking precision policy, and conditions
  for continuation, rebuild, or brake. It names the next state, normally WEEK_PLAN, and does not start daily
  execution by itself.

rejects: |
  Permanent diet; cycle setup that also emits all week/day/review content as an owner-facing wall.

### WGA6 — Week plan state contract (WG6)

status: answered

contract: |
  WEEK_PLAN consumes active cycle and may produce the exact plan artifact families needed for execution:
  `x_nutrition/menus/*`, `x_nutrition/recipes/*`, `x_nutrition/grocery/*`, `x_nutrition/fallbacks/*`, and
  related writer packets. It is the only normal state that may authorize menu/recipe/grocery/prep output.

acceptance: |
  WEEK_PLAN output is one bounded planning task at a time. If multiple artifacts must be created, the router
  sequences them through writer packets or follow-up states rather than printing an unbounded owner-facing wall.

rejects: |
  Startup producing week-plan content; week-plan artifacts treated as current authority without graph state.

### WGA7 — Day loop state contract (WG7)

status: answered

contract: |
  DAY_LOOP accepts messy owner text/voice/photo updates or near-term food questions and writes only
  `x_nutrition/logs/*` or a writer-compatible LOG packet, plus the bounded owner-facing decision needed now.

acceptance: |
  Owner never fills LOG templates or fixed checklists. LOG confidence and materiality decide whether the operator
  asks at most one clarifier. Raw daily nutrition data remains in Health AI nutrition only.

rejects: |
  Direction OS food diary; mandatory gram-level logging; owner-facing JSON/field templates.

### WGA8 — Review state contract (WG8)

status: answered

contract: |
  REVIEW consumes Health AI nutrition LOG summaries, owner feedback, and core metrics/phase/biofeedback/
  adherence, then emits exactly one decision class: hold, mutate, rebuild, update, refresh, brake, or
  non-diagnostic medical-check language.

acceptance: |
  REVIEW output either explicitly holds or names the mutation/rebuild/brake target and next graph state.
  It may update `x_nutrition/reviews/*` and may create exactly one mutation packet if artifact changes are needed.

rejects: |
  Passive review summary; exporting raw daily diary to Direction OS; review that silently changes artifacts.

### WGA9 — Mutation state contract (WG9)

status: answered

contract: |
  MUTATION applies or packets one bounded change to nutrition artifacts/rules/state after REVIEW or a material
  trigger. It names target artifact(s), reason, expected effect, and next review trigger.

acceptance: |
  If several unrelated changes are needed, MUTATION splits them into separate bounded tasks or CALLs. The
  current workflow cursor records the selected mutation scope and next state after the write is accepted.

rejects: |
  Regenerating the whole nutrition system; multi-artifact rewrite without a selected scope; mutation hidden inside
  a review summary.

### WGA10 — One-chat-one-task output contract (WG10)

status: answered

contract: |
  Every nutrition chat begins by stating one resolved workflow state and returns one bounded output/question/action.
  Extra needed outputs become sequenced states, writer packets, or a next CALL.

acceptance: |
  Owner-facing content remains compact: state, why it matters, what is blocked if anything, one output or question,
  and one recommended next action. File-heavy details belong in Health AI artifacts or writer packets.

rejects: |
  Scattershot multi-artifact answer; broad tutorial; "while I am here" nutrition execution.

### WGA11 — Owner-facts vs AI-decided facts contract (WG11)

status: answered

contract: |
  Every workflow state must distinguish irreducible owner facts from system-decided nutrition variables. The
  operator asks only material irreducible facts and decides expert variables from evidence, profile, phase,
  feedback, and review state.

acceptance: |
  Missing irreducible facts produce pending/reduced/default-safe state. No state asks the owner to choose meals/day,
  macro targets, deficit, timing, tracking precision, or review trigger policy as preferences.

rejects: |
  Expert-variable questionnaire; blocking execution on non-material owner facts; fabricated owner facts.

### WGA12 — Direction OS boundary contract (WG12)

status: answered

contract: |
  Direction OS may receive only summary, decision, problem, and next CALL. Raw food logs, photos, daily check-ins,
  and meal details stay under Health AI nutrition LOG/state.

acceptance: |
  A writer packet or RESULT is invalid if it asks to copy raw daily nutrition data into `live/health/NOW.md`,
  `LOG.md`, `TREE.md`, `knowledge/`, or history, except as summarized evidence.

rejects: |
  Direction OS as nutrition diary; external strategic workflow write-back of raw LOG contents.

### WGA13 — Seed artifact authority contract (WG13)

status: answered

contract: |
  Existing active program, first cycle, menu, grocery, fallback, LOG template, review template, and
  `first-setup-pending.md` are seeds/evidence until the workflow graph selects their state.

acceptance: |
  `first-setup-pending.md` and provider-continuation load order must be subordinated to `workflow-router`.
  They cannot authorize "use all generated artifacts" as startup UX until STARTUP_ROUTER has selected a
  single state and output family.

rejects: |
  Justifying the rejected startup wall by pointing to previously accepted artifacts; treating seed status as
  owner-facing workflow acceptance.

### WGA14 — Safety and block routing contract (WG14)

status: answered

contract: |
  The graph must define block routes for red flags, medical uncertainty, unsafe deterioration, material missing
  allergy/medical facts, stale or contradictory current workflow cursor, and workflow ambiguity.

acceptance: |
  Red flags route to conservative mode or non-diagnostic medical-check language. Material missing facts route to
  one clarifier or reduced mode. Workflow ambiguity routes to repair/writer packet or Direction OS CALL. Normal
  progression does not continue silently through a block.

rejects: |
  Silent continuation; many-question intake wall; medical diagnosis/prescription; training/activity scope expansion.

### WGA15 — Writer handoff / validation contract

status: answered

contract: |
  Nutrition writer handoff must be extended so any workflow-affecting write validates WG1-WG14 in addition to
  W1-W13, NCA0-NCA9, and B1-B3. Packets must name the resolved workflow state, target artifact family, source
  graph row(s), and boundary statement.

acceptance: |
  A writer rejects packets that preserve old nutrition acceptance rows but violate workflow graph obligations,
  especially startup/router, one-chat-one-task, seed artifact authority, Direction OS diary boundary, or block routing.

rejects: |
  Writer accepting old W/NCA/B surface while ignoring WG1-WG14; intention-only packets; partial multi-state writes.

## §ARCH DECISIONS

### Q1 — Router authority

| option | verdict | reason |
|---|---|---|
| Prompt-only router in SYSTEM/provider-continuation | rejected | Too easy to regress into hidden model judgment; the failure was workflow authority, not missing prose. |
| Active program as router | rejected | PROGRAM is a state artifact and cannot authorize startup/week/day/review content. |
| Procedure-only router | rejected as insufficient alone | Matches operator-invoked rule but has weak state memory and drift detection. |
| Explicit graph + current-state cursor + workflow-router procedure | picked | Mechanically checkable, provider-independent, nutrition-namespaced, and blocks stale/missing state before content output. |

signed_recommendation: |
  Pick explicit graph + current-state cursor + workflow-router procedure. This is a contract recommendation
  derived from owner-signed WHAT; no new owner preference is introduced because the pick only makes the signed
  one-chat-one-task workflow mechanically enforceable.

### Q2 — State contract shape

| option | verdict | reason |
|---|---|---|
| One loose graph paragraph | rejected | Does not mechanically prove WG2 fields per state. |
| Separate detailed state files now | rejected as premature HOW | Could create file sprawl before product PLAN decides implementation layout. |
| One graph file with one row per state and required fields | picked | Covers WG2 without embedding menus/recipes/log content or forcing per-state file layout. |

signed_recommendation: |
  Pick one graph file with required fields per state. PLAN may split into per-state files later if needed, but
  converge-arch requires only the behavioral contract.

### Q3 — Writer boundary

| option | verdict | reason |
|---|---|---|
| Old W/NCA/B writer validation only | rejected | It can pass old module acceptance while violating the new workflow overlay. |
| Direction OS stores workflow/raw data | rejected | Violates raw-data boundary and makes OS a diary. |
| Writer packet names workflow state and checks WG1-WG14 | picked | Keeps durable writes small, reviewable, and aligned with the new router contract. |

signed_recommendation: |
  Pick WG-aware writer handoff. Workflow graph evidence rides product implementation context only; shape/executor
  done_when must not make this architecture-on-paper itself the success proof.

### Q4 — Block routing

| option | verdict | reason |
|---|---|---|
| Best-effort continue through ambiguity | rejected | Recreates "AI somehow decides." |
| Ask a full intake questionnaire | rejected | Violates owner-free-form boundary and one-chat-one-task. |
| Explicit block table with one material clarifier / reduced mode / repair / CALL | picked | Handles safety and workflow ambiguity without content walls or hidden continuation. |

signed_recommendation: |
  Pick explicit block routes. Safety blocks and workflow ambiguity are first-class router outcomes, not exceptions
  handled ad hoc inside content generation.

## §WG1-WG14 COVERAGE

| WG | mapped contract obligations | status |
|---|---|---|
| WG1 startup/router | WGA0, WGA1, WGA10, WGA13: graph + cursor + router first; compact startup output only. | answered |
| WG2 state graph completeness | WGA2: graph row per state with required fields; missing field blocks execution. | answered |
| WG3 transition path | WGA3: canonical path and mutation return scopes. | answered |
| WG4 program | WGA4: program-level artifact only; consumes core, no execution wall. | answered |
| WG5 cycle | WGA5: cycle-level artifact only; bounded loop, next state. | answered |
| WG6 week plan | WGA6: only WEEK_PLAN authorizes menu/recipe/grocery/prep artifact families. | answered |
| WG7 day loop | WGA7: free-form owner input parsed internally to Health AI LOG/writer packet. | answered |
| WG8 review | WGA8: one explicit decision class with target/next state. | answered |
| WG9 mutation | WGA9: one bounded change; split unrelated changes. | answered |
| WG10 one-chat-one-task | WGA10 and WGA15: state + one output/question/action; writer rejects multi-state packets. | answered |
| WG11 owner facts / AI decisions | WGA11: irreducible owner facts only; expert variables system-decided. | answered |
| WG12 Direction OS boundary | WGA12 and WGA15: summary/decision/problem/CALL only upward. | answered |
| WG13 seed authority | WGA13: artifacts and first-setup state are seeds until selected by graph. | answered |
| WG14 safety/block | WGA14: explicit routes for safety, material facts, stale cursor, ambiguity, forbidden scope. | answered |

Rows explicitly rejected as HOW/currently out of contract:
- Storage layout beyond the named contract surfaces, per-state file split, exact field serialization, prompt wording,
  schedule timing, background automation, UI, app, service, and shopping/recipe integration details.
- Nutrition content generation itself: menus, recipes, grocery lists, shopping instructions, daily plans, food logs.

## §OPEN / DEFERRED CHECK

open rows: 0
deferred rows: 0
blocker rows: 0
owner decisions needed: 0

contract_coverage: every WG1-WG14 row maps to at least one WGA contract row.
arch_open: 0
arch_in_context_only: PASS — this paper architecture must ride future shape/executor context only; it is not copied
into done_when as binding implementation evidence.

## §SIGNOFF

§SIGNOFF — DECLARE:
  Workflow graph contracts WGA0-WGA15 are closed on paper for converge-verify.

§SIGNOFF — ARCHITECT:
  High-risk architecture questions Q1-Q4 have refuted options and signed recommendations. No owner decision batch is
  needed in this session because no new nutrition behavior or owner preference is chosen; the recommendations only
  mechanize the owner-signed workflow WHAT.

## §ROUTE

Next: converge-verify.

Reason:
- WG1-WG14 all map to concrete Health AI state/procedure/file/operator obligations.
- Hidden old-surface gaps are closed: router/current-state surface, first-setup seed subordination, WG-aware writer
  validation, block routing, and review-trigger-not-schedule boundary.
- Verification must now try to refute this architecture closure before shape/executor work.

END_OF_FILE: live/health/work/converge-g-health-nutrition-workflow-graph-arch.md
