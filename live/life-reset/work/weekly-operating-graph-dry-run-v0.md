# Weekly Operating Graph dry-run v0 — life-reset

Date prepared: 2026-06-19
Target real planning session: Sunday evening, 2026-06-21
Target real week: 2026-06-22 to 2026-06-28
Status: draft simulation for shaping, not an approved Weekly Contract

## 0. What this document is

This document is a detailed dry-run of how `life-reset` could build and operate
one real week as an active Weekly Operating Graph.

It is not the real plan yet. The real plan is accepted only in the Sunday
planning session, after the owner gives the real calendar, capacity, family
constraints, current state, and any latest source-direction updates.

This document answers:

- what information `life-reset` would collect;
- how it would import game / health / Solmax without taking ownership;
- what a Trello-like tracker / track-log could look like without choosing a
  permanent tool;
- what happens when new ideas appear mid-week;
- what happens when a source direction is blocked;
- what happens when something fails, slips, resets, or must be cut;
- how the week changes without silently expanding.

Important boundary:

`life-reset` is the week-construction and conflict-management layer. It is not
the source of truth for game tasks, health protocols, Solmax work, nutrition,
training, medical decisions, or psychiatric treatment.

## 1. The smallest useful weekly model

The weekly graph has five layers.

1. Sources
2. Candidate outcomes
3. Capacity and constraints
4. Selected slices
5. Weekly Contract

The mistake this prevents:

> A week becomes a list of things that feel important.

The intended behavior:

> A week becomes a graph of commitments, sources, capacity, dependencies,
> explicit cuts, and rules for changing the plan.

The v0 should be plain enough to run in a chat or Markdown document. It may look
like a Trello board, but no permanent Trello / repo / provider / tool choice is
made here.

## 2. Current source snapshots

These are the source snapshots used for this dry-run. They must be refreshed on
Sunday before a real contract is accepted.

### 2.1 Game direction: indie-game-development

Current root:

- Build, ship, and commercialize a Steam indie co-op game around gas + grid +
  expedition systems.
- Game direction has a fixed commercial pressure: Steam / Next Fest / money
  gates exist downstream.

Current spine:

- Active node: `g-9c41`.
- Wave 1 is closed and independently reviewed as `MET`.
- The stream / lock / Wave 1 proof is not the same as the whole node being done.
- The next major movement is Wave 2 shape.

Current next:

- `c-shape-wave2` is ready as the next shape call.
- But the Wave 2 contract set is blocked from being consumed into executor
  done_when until `c-converge-003` repairs two findings and a fresh re-verify is
  clean.

The two known Wave 2 contract blockers:

1. No coarse-tier network-replication contract.
2. Cross-layer feedback is not reconciled with the locked pure-sink Wave 1
   proofs.

Game direction imports into the week as:

- a primary progress lane;
- not as a detailed game production roadmap inside life-reset;
- not as permission for life-reset to rewrite game tasks.

What life-reset is allowed to ask about game:

- What is the next accepted CALL?
- Is it ready, blocked, queued, or done?
- What is the smallest slice this week can actually move?
- Does the game need owner decisions this week?
- Does the game create a capacity conflict with health, family, recovery, or
  life-reset setup?

What life-reset must not do:

- design the Wave 2 sim;
- choose game architecture;
- create game tasks not issued by the game direction;
- update game source state;
- turn game work into generic productivity tasks.

### 2.2 Health direction

Current active node:

- `g-health-core`

Current state:

- Tasks `t-1`, `t-2`, and `t-3` are done.
- Product evidence pre-pass is clean.
- Binding corrected G5 review is still pending.

Current next:

- `c-health-core-review-002`

Health imports into the week as:

- a source-direction review item;
- possible future next-bet decision if corrected G5 returns met;
- imported health floors / constraints only if already stated by health state or
  by the owner on Sunday.

What life-reset is allowed to ask about health:

- Does the corrected G5 review need a slot this week?
- Is there a health floor or constraint that affects capacity?
- Is there a decision pending after review?
- Is there any red-flag boundary that means life-reset should not intensify
  discipline?

What life-reset must not do:

- prescribe nutrition;
- prescribe training;
- track raw food, weight, sets, symptoms, or daily health data;
- make medical decisions;
- turn health into a life-reset diary.

### 2.3 Solmax / Zaratusta

Current active bet:

- `g-kernel` Wave 0, but held by owner.

Current state:

- Owner deferred Solmax/W0 on 2026-06-17.
- `t-2`, `t-3`, and converge-arch are held.

Life-reset import:

- Solmax is a cut for this week unless the owner explicitly resumes it in a
  separate proper session.

What life-reset does if Solmax desire appears mid-week:

- capture the desire;
- remind that Solmax is on owner hold;
- do not open W0 work inside the current week unless a competing commitment is
  explicitly removed and a valid next CALL is selected.

### 2.4 Life-reset itself

Current state:

- Direction framed.
- Top-level map approved.
- First shape target is `g-lr-weekly-operating-graph`.

This dry-run exists to shape the first limited bet:

- prepare the weekly graph format;
- show how it works on real adjacent data;
- then use it for real on Sunday evening.

## 3. Terms in simple language

### Weekly Operating Graph

The live structure of the week:

- what sources feed the week;
- what outcomes are candidates;
- what dependencies exist;
- what capacity exists;
- what gets selected;
- what gets cut;
- what rule controls changes.

### Weekly Contract

The accepted commitment for the week.

It includes:

- selected outcomes;
- selected slices;
- maintenance floors;
- explicit cuts;
- capacity assumptions;
- success checks;
- change rule.

### Track-log / tracker

A working view of the week.

It can look like a Trello board, table, Markdown list, chat thread, or future
tool, but v0 does not select the permanent surface.

For this dry-run, the tracker is just a structured table.

### Slice

A bounded piece of a larger direction that can be moved this week.

Example:

- not "work on the game";
- but "complete `c-converge-003` repair and, if clean, run re-verify or prepare
  Wave 2 shape."

### Floor

Something that protects life or direction viability.

In v0, life-reset can import a floor, but it cannot invent a protocol.

Example:

- valid: "health direction says raw daily health data stays outside Direction OS";
- invalid: "life-reset prescribes meals / training."

### Cut

A thing intentionally not done this week.

A cut is not failure. It is a decision that protects the week.

## 4. Input checklist for Sunday

Sunday planning should start by collecting this input.

### 4.1 Calendar and availability

Owner gives:

- fixed appointments;
- family obligations;
- immovable errands;
- likely sleep / recovery constraints;
- any days that are low-capacity;
- any travel or interruption risk;
- desired focus windows;
- any hard external deadlines.

The graph records:

```yaml
capacity:
  week: 2026-06-22..2026-06-28
  hard_commitments: []
  focus_blocks_available: unknown_until_owner_input
  low_capacity_days: []
  protected_buffer: required
```

No plan is valid until this exists.

### 4.2 Source-direction refresh

Read or summarize:

- `live/indie-game-development/NOW.md`
- `live/health/NOW.md`
- `live/solmax/NOW.md`
- `live/life-reset/NOW.md`

For each source:

```yaml
source:
  direction:
  current_next:
  status: ready | blocked | active | held | awaiting_owner | done
  owner_decisions:
  risks:
  what_life_reset_can_import:
  what_life_reset_must_not_touch:
```

### 4.3 Owner state

Owner gives a plain statement:

- energy now;
- mood / stability at a practical level;
- biggest pressure;
- what would make the week feel successful;
- what would make it obviously too much;
- current temptation / avoidance / chaos risk if any.

This is not diagnosis. It is planning signal.

### 4.4 Backlog candidates

The owner may throw in ideas:

- books;
- canon ideas;
- spiritual practice;
- psychological conversation;
- dance / bike / VR;
- new tools;
- provider / repo / automation ideas;
- productivity fixes;
- family-related intentions.

Default behavior:

- capture;
- classify;
- do not automatically commit.

## 5. Candidate outcomes for the sample week

This is a dry-run using current state as of 2026-06-19.

### Candidate A: Game spine moves

Source:

- indie-game-development

Candidate outcome:

- The game direction is no longer blocked on the Wave 2 contract question, or
  the remaining blocker is named precisely.

Possible slices:

1. Run `c-converge-003` repair.
2. Run fresh converge-verify after repair.
3. If clean, shape Wave 2.
4. If still blocked, produce exact blocker and next route.

Risk:

- This can expand into deep game architecture work.

Life-reset rule:

- life-reset only allocates the week slot and tracks state; game direction owns
  the actual work.

### Candidate B: Health corrected review

Source:

- health

Candidate outcome:

- `g-health-core` has corrected binding G5 verdict: met / partially_met /
  not_met.

Possible slice:

- Run `c-health-core-review-002`.

Risk:

- If met, owner may want to immediately shape nutrition or training next.

Life-reset rule:

- if health review returns met, the next-bet decision is captured for weekly
  review or a separate health session; the current week does not automatically
  expand.

### Candidate C: Canon / creative track

Source:

- indie-game-development, `g-d3a8` canon track

Candidate outcome:

- One small canon action advances or one status report clarifies what is next.

Possible slices:

1. Run `canon-status` render-only.
2. Run one `canon-forge` question if all dependencies are ready.

Risk:

- Creative work can absorb the week because it feels alive.

Life-reset rule:

- optional only after primary selected outcomes fit;
- no second active game bet;
- no conflict with g-9c41 spine.

### Candidate D: Solmax

Source:

- solmax

Candidate outcome:

- none this week, because owner hold remains active.

Rule:

- cut.

### Candidate E: Life-reset v0 proves itself

Source:

- life-reset

Candidate outcome:

- One weekly graph and contract are accepted, used as the week reference, and
  reviewed at the end.

Risk:

- life-reset becomes another planning project.

Rule:

- one new improvement experiment max: the weekly graph itself.
- no daily runtime protocol in this bet.

## 6. Capacity model

The week should not start from ambition. It should start from capacity.

### 6.1 Capacity buckets

Use buckets, not exact fantasy-hours.

```yaml
capacity_buckets:
  deep_work:
    description: "hard creative/technical sessions"
    examples: ["game shape/converge", "code review", "hard planning"]
  admin_light:
    description: "low-cognitive work"
    examples: ["read state", "status pass", "small replies"]
  owner_decision:
    description: "owner attention for choosing/signing"
    examples: ["shape approval", "review verdict", "bet choice"]
  recovery_buffer:
    description: "unallocated slack"
  family_life:
    description: "fixed or desired family/personal commitments"
```

### 6.2 Capacity rule

No more than:

- 1 primary direction outcome;
- 1 secondary bounded outcome;
- 1 experiment;
- optional small activity only if it fits without stealing from the above.

For the sample week:

```yaml
selected_capacity_shape:
  primary: game spine
  secondary: health corrected review
  experiment: life-reset weekly graph v0
  optional: one canon status/forge only if capacity remains
  cut: Solmax/W0
```

### 6.3 Why not select everything

Because the current state already contains:

- game architecture / contract blocker;
- health review pending;
- life-reset pilot;
- possible canon pull;
- Solmax temptation;
- likely personal-life unknowns.

If all are selected, the week becomes a wish-list and loses evidence value.

## 7. Trello-like tracker v0

This is not a permanent Trello decision.

For v0, the tracker can be a Markdown board with lanes.

### 7.1 Lanes

```text
Inbox
Candidate
Selected This Week
Doing
Blocked
Done
Cut / Parked
Review Evidence
```

### 7.2 Card fields

Every card carries:

```yaml
id:
title:
source:
kind: direction_slice | floor | activity | idea | decision | blocker | evidence
status:
why_now:
done_when:
capacity_cost:
dependency:
owner_decision_needed:
source_of_truth:
life_reset_role:
cut_if:
evidence_to_capture:
```

### 7.3 Example cards at planning time

#### Card G1

```yaml
id: W25-G1
title: "Repair Wave 2 contracts for g-9c41"
source: indie-game-development
kind: direction_slice
status: candidate
why_now: "Wave 2 shape must not consume blocked contracts."
done_when: "c-converge-003 returned repaired contract set, or exact blocker remains."
capacity_cost: deep_work
dependency: "requires game direction session"
owner_decision_needed: possible
source_of_truth: "live/indie-game-development"
life_reset_role: "reserve slot, track state, do not design"
cut_if: "game owner chooses not to run Wave 2 route this week"
evidence_to_capture: "RESULT link / verdict summary only"
```

#### Card G2

```yaml
id: W25-G2
title: "Fresh re-verify Wave 2 contracts"
source: indie-game-development
kind: direction_slice
status: candidate
why_now: "Shape can consume contracts only after clean re-verify."
done_when: "converge-verify passed or blocks with named findings."
capacity_cost: deep_work
dependency: "after W25-G1"
owner_decision_needed: no unless blocked
source_of_truth: "live/indie-game-development"
life_reset_role: "track dependency"
cut_if: "W25-G1 does not close"
evidence_to_capture: "pass/block verdict"
```

#### Card G3

```yaml
id: W25-G3
title: "Shape Wave 2 of g-9c41"
source: indie-game-development
kind: direction_slice
status: candidate
why_now: "Wave 1 closed; Wave 2 is next if contracts are safe."
done_when: "Wave 2 bet approved or deferred with reason."
capacity_cost: deep_work + owner_decision
dependency: "contracts repaired and re-verified, unless shape explicitly does not bind them"
owner_decision_needed: yes
source_of_truth: "live/indie-game-development"
life_reset_role: "sequence, not author"
cut_if: "contract blocker remains"
evidence_to_capture: "approved bet / deferral"
```

#### Card H1

```yaml
id: W25-H1
title: "Corrected G5 review for health core"
source: health
kind: direction_slice
status: candidate
why_now: "g-health-core is partially_met pending corrected binding review."
done_when: "c-health-core-review-002 returns met / partially_met / not_met."
capacity_cost: deep_work or review_work
dependency: "fresh review session"
owner_decision_needed: maybe after verdict
source_of_truth: "live/health"
life_reset_role: "reserve slot, do not prescribe health actions"
cut_if: "game consumes all deep-work capacity and owner decides health waits"
evidence_to_capture: "verdict only"
```

#### L1

```yaml
id: W25-L1
title: "First real Weekly Contract accepted"
source: life-reset
kind: experiment
status: selected
why_now: "This is the first life-reset pilot."
done_when: "Week graph + contract accepted by owner with sources/capacity/cuts/change rule."
capacity_cost: owner_decision + planning
dependency: "Sunday planning"
owner_decision_needed: yes
source_of_truth: "live/life-reset"
life_reset_role: "primary"
cut_if: "Sunday planning cannot happen"
evidence_to_capture: "accepted contract"
```

#### S1

```yaml
id: W25-S1
title: "Solmax / W0"
source: solmax
kind: direction_slice
status: cut
why_now: "Owner hold remains active."
done_when: "Not touched this week."
capacity_cost: zero
dependency: none
owner_decision_needed: only in separate resume session
source_of_truth: "live/solmax"
life_reset_role: "protect cut"
cut_if: "always this week unless owner explicitly reopens and removes competing volume"
evidence_to_capture: "none"
```

#### I1

```yaml
id: W25-I1
title: "Idea inbox: new practices / books / tools"
source: owner
kind: idea
status: inbox
why_now: "Capture prevents loss without creating obligation."
done_when: "Classified as candidate / parked / routed / dropped."
capacity_cost: light
dependency: "weekly review or explicit swap rule"
owner_decision_needed: no immediately
source_of_truth: "life-reset backlog once built; for v0 a simple list"
life_reset_role: "capture and classify"
cut_if: "tries to become a current-week task without critical need"
evidence_to_capture: "one-line capture"
```

## 8. Sunday planning flow in detail

### Step 1: Open

Question:

> What week are we planning, and what is immovable?

Output:

```yaml
week:
  dates: 2026-06-22..2026-06-28
  planning_date: 2026-06-21 evening
  immovable_events: []
  known_low_capacity_windows: []
```

If the owner cannot give the calendar:

- do not fake precision;
- use conservative capacity;
- add a task: "calendar уточнить";
- keep the contract smaller.

### Step 2: Source refresh

Read current NOW files or accepted summaries.

Output:

```yaml
sources:
  indie_game_development:
    status: active
    next: "c-shape-wave2, but contract blocker path exists"
    week_candidate: "repair/reverify/shape sequence"
  health:
    status: active
    next: "c-health-core-review-002"
    week_candidate: "corrected review"
  solmax:
    status: held_by_owner
    week_candidate: "cut"
  life_reset:
    status: shaping first bet
    week_candidate: "first Weekly Contract v0"
```

### Step 3: Owner intention

Ask:

- If this week succeeds, what is visibly different?
- What would be too much?
- What are you likely to over-promise?
- What are you likely to avoid?

The answer is not accepted blindly. It is evidence for the graph.

Example possible owner answer:

> I want game momentum, health core closed, and not to collapse into chaos.

Graph interpretation:

- game gets primary lane;
- health review gets secondary lane;
- chaos prevention means cuts and buffer are mandatory;
- new ideas go to capture.

### Step 4: Candidate list

The graph lists candidates before selecting.

Example:

```yaml
candidates:
  - game_contract_repair
  - game_contract_reverify
  - game_wave2_shape
  - health_core_corrected_review
  - canon_status_or_one_forge
  - life_reset_weekly_graph_v0
  - solmax_resume
  - new_personal_practice
  - tool_surface_decision
```

### Step 5: Dependency graph

Important: candidates are not equal.

```text
game_contract_repair
  -> game_contract_reverify
    -> game_wave2_shape

health_core_corrected_review
  -> health_next_bet_decision (only if met)

life_reset_weekly_graph_v0
  -> weekly_review_evidence

solmax_resume
  -> blocked by owner hold
```

This prevents selecting `game_wave2_shape` as if it were independent when the
contract blocker is still live.

### Step 6: Capacity cut

Apply capacity rules.

For this dry-run:

```yaml
selected:
  primary:
    - game_contract_repair
    - game_contract_reverify_if_repair_clean
    - game_wave2_shape_if_reverify_clean
  secondary:
    - health_core_corrected_review
  experiment:
    - life_reset_weekly_graph_v0
  optional:
    - canon_status_only_or_one_small_forge
cut:
  - solmax_resume
  - permanent_tooling
  - daily_runtime_protocol
  - modules
  - full_backlog_system
  - nutrition_training_prescriptions
```

### Step 7: Contract drafting

The Weekly Contract is drafted in owner-facing plain language.

Example draft:

> This week is about moving the game spine honestly without pretending blocked
> contracts are ready, closing the health-core review verdict if capacity allows,
> and proving that life-reset can hold a week without expanding it.

### Step 8: Owner acceptance

The owner approves or changes the contract.

Approval should include:

- selected outcomes;
- cuts;
- change rule;
- acknowledgement that optional items are optional.

Without explicit acceptance, there is no contract.

## 9. Sample accepted Weekly Contract

This is a hypothetical output, not a real accepted contract.

```yaml
weekly_contract:
  id: lr-week-2026-06-22
  status: draft_example
  dates: 2026-06-22..2026-06-28

  primary_outcome:
    id: game-spine
    source: indie-game-development
    goal: |
      By the end of the week, g-9c41 Wave 2 is either legitimately ready to
      shape on clean contracts, shaped into an approved bet, or blocked with
      exact remaining findings.
    success_check:
      - c-converge-003 result exists OR owner explicitly chose a safe alternate route.
      - if repair closed, fresh converge-verify result exists.
      - if verify passed, c-shape-wave2 either ran or is ready with no hidden blocker.

  secondary_outcome:
    id: health-core-review
    source: health
    goal: |
      g-health-core has corrected binding G5 review verdict.
    success_check:
      - c-health-core-review-002 returns met / partially_met / not_met.
      - no nutrition/training module is shaped inside life-reset.

  experiment:
    id: life-reset-weekly-graph-v0
    source: life-reset
    goal: |
      The week is run from one accepted Weekly Contract with explicit sources,
      selected slices, cuts, and a change rule.
    success_check:
      - contract accepted Sunday.
      - midweek changes use the change rule.
      - weekly review can compare promised vs actual.

  optional:
    - id: canon-status
      rule: "Only if primary/secondary lanes do not consume the capacity."

  explicit_cuts:
    - Solmax/W0.
    - Daily runtime protocol.
    - Permanent provider/chat/repo/tool architecture.
    - Full backlog system.
    - Process/activity modules.
    - Nutrition/training/medical prescriptions.
    - Game production roadmap edits inside life-reset.

  change_rule: |
    A new current-week commitment requires:
    1. name the new fact;
    2. explain why it beats the accepted contract;
    3. remove or shrink a competing commitment of comparable size;
    4. record the change as an explicit contract mutation.
```

## 10. What the week might look like day by day

This section is a simulation. The real week should not pre-fill every day before
the owner gives calendar and capacity.

### Sunday evening: planning

Actions:

1. Refresh source directions.
2. Collect calendar and capacity.
3. Build candidate list.
4. Cut down to selected outcomes.
5. Accept Weekly Contract.

Possible output:

```text
Selected:
- Game: repair/reverify/shape path.
- Health: corrected G5 review.
- Life-reset: run v0 contract.

Optional:
- Canon status only.

Cut:
- Solmax.
- tooling.
- daily runtime.
- modules.
```

Evidence saved:

- Weekly Contract.
- List of explicit cuts.
- Change rule.

### Monday: open primary lane

Possible focus:

- Start game-side `c-converge-003` repair.

Life-reset role:

- check that the task is still the primary lane;
- record whether it started, blocked, or returned;
- do not inspect or author the game contract details unless operating as the
  game direction session.

Tracker movement:

```text
W25-G1: Selected -> Doing
W25-G2: Candidate -> Blocked by W25-G1
W25-G3: Candidate -> Blocked by W25-G2
W25-H1: Selected, not started
```

If Monday goes well:

- `W25-G1` returns done or ready for re-verify.

If Monday fails:

- exact blocker is recorded;
- Tuesday plan does not pretend re-verify is available.

### Tuesday: follow dependency

Branch A, repair clean:

- Run fresh converge-verify.
- If it passes, Wave 2 shape becomes eligible.

Branch B, repair incomplete:

- Continue repair only if within capacity and not spiraling.
- Otherwise name the blocker and stop expansion.

Branch C, owner energy low:

- Move health review or admin/light work only if it does not break the primary
  outcome.

Tracker examples:

```text
Repair clean:
  W25-G1 -> Done
  W25-G2 -> Doing

Repair blocked:
  W25-G1 -> Blocked
  W25-G2 -> Blocked
  W25-G3 -> Blocked
```

Life-reset question:

> Are we still pursuing the accepted game outcome, or has the week found a real
> blocker?

If blocker:

- do not add canon to feel productive unless capacity allows after accepting the
  blocker.

### Wednesday: secondary lane or Wave 2 shape

If game verify passed:

- Shape Wave 2 may be the main Wednesday work.

If game is blocked:

- The week can shift to health corrected review, but only as an explicit
  mutation:

```yaml
contract_mutation:
  new_fact: "Game contracts are blocked after repair attempt."
  removed_or_shrunk: "Game Wave 2 shape this week."
  added_or_promoted: "Health corrected G5 review."
  accepted_by_owner: required
```

If game shape consumes owner decision bandwidth:

- health review may move to later.

### Thursday: health review or closure of game shape

Possible work:

- Run `c-health-core-review-002`.

Life-reset role:

- reserve the slot;
- ensure the review stays a review;
- prevent health from turning into nutrition/training shaping inside the same
  week unless accepted as a separate later direction decision.

Possible outcomes:

```text
health verdict = met:
  capture next-bet decision for health.
  do not auto-shape nutrition/training in life-reset.

health verdict = partially_met:
  record blocker gaps.
  do not pretend core is closed.

health verdict = not_met:
  record exact refutation.
  next health CALL follows health direction, not life-reset invention.
```

### Friday: buffer / evidence cleanup

The week needs a buffer day or buffer block.

Possible uses:

- finish game shape if nearly done;
- finish health review if started;
- collect evidence for weekly review;
- handle real-life disruptions;
- do nothing extra if the week is already full.

Important:

Friday should not automatically start a new large thing just because a task
finished early. Early finish is success, not permission to bloat.

### Saturday: optional / standalone / recovery

Possible uses:

- optional canon status;
- family/personal activity;
- light backlog classification;
- recovery / low-intensity day.

Rules:

- optional item does not become a moral debt;
- if the week is behind, Saturday is not automatically a punishment day;
- if the owner wants to use it for a hard push, the competing cost is named.

### Sunday: weekly review

Review asks:

1. What was promised?
2. What actually happened?
3. Where did drift occur?
4. What was cut correctly?
5. What was cut too timidly?
6. Which source directions changed?
7. What is the weakest link?
8. What changes next week?

Example review table:

```text
Promised:
- Game repair/reverify/shape path.
- Health corrected G5 review.
- Life-reset weekly graph v0.

Actual:
- Game repair done, reverify blocked on finding F2.
- Health review not run.
- Life-reset contract held; two new ideas captured, none added.

Decision:
- Next week primary remains game if owner accepts.
- Health review either scheduled first or parked with reason.
- Weekly graph v0 mutated: add clearer dependency lane.
```

## 11. How new ideas are handled

### 11.1 Default rule

New idea is not a command.

New idea becomes one of:

- drop;
- capture;
- candidate;
- current-week swap;
- route to another direction;
- research later;
- module candidate later.

### 11.2 Example: "I want to start dancing this week"

Classification:

```yaml
idea:
  title: "dance"
  value: "standalone activity, body/life energy"
  urgency: not_critical_unless_owner_says_so
  source: owner
  default: candidate_or_parked
```

Possible handling:

A. Park for weekly review.

- Good if week is already full.
- No moral debt.

B. Add as a tiny standalone activity.

- Only if capacity exists.
- Example: one bounded session, not a full process.

C. Promote later to module.

- Only after process/activity modules node is shaped later.

Not allowed in v0:

- create full dance module;
- build tracking system;
- make it compete silently with game/health.

### 11.3 Example: "I have a spiritual practice idea"

Classification:

```yaml
idea:
  title: "spiritual practice"
  value: "spirit/transcendence lens"
  risk: "can become bypass or scope expansion"
  default: capture
```

Handling:

- capture the idea;
- maybe ask what real action it should produce;
- do not start a module in the weekly graph v0;
- revisit in review or later process/activity module shaping.

### 11.4 Example: "I want to resume Solmax"

Classification:

```yaml
idea:
  title: "resume Solmax"
  source: solmax
  current_state: held_by_owner
  default: cut
```

Handling:

- remind: Solmax/W0 is held;
- capture the desire;
- if owner insists, require explicit mutation:
  - what new fact changed?
  - what current selected commitment is removed?
  - does Solmax have a valid next route?
  - is this a separate session?

Most likely v0 answer:

- not this week.

### 11.5 Example: "Let's pick the permanent tool"

Classification:

```yaml
idea:
  title: "permanent tool architecture"
  default: cut
  reason: "boundary explicitly forbids selecting permanent provider/chat/repo/tool architecture"
```

Handling:

- use plain Markdown/chat for v0;
- capture tool friction;
- choose tooling only after real use proves need.

## 12. How blockers are handled

### 12.1 Blocker types

```yaml
blocker_types:
  source_blocker: "direction itself says next is blocked"
  capacity_blocker: "not enough time/energy/attention"
  decision_blocker: "owner decision needed"
  evidence_blocker: "done_when cannot be proven"
  boundary_blocker: "would violate scope/source-of-truth"
  drift_blocker: "owner state makes plan unrealistic"
```

### 12.2 Game contract blocker

If `c-converge-003` cannot close:

- `game_wave2_shape` stays blocked;
- do not turn blocked shape into vague game work;
- record exact finding;
- week may still succeed if it names the blocker and avoids false progress.

Possible mutation:

```yaml
mutation:
  new_fact: "Wave 2 contract repair did not close."
  consequence: "Wave 2 shape cannot honestly consume contracts."
  replacement_options:
    - "Continue contract repair within remaining appetite."
    - "Switch secondary lane to health review."
    - "Stop primary lane and preserve evidence for next week."
  recommended: "Switch only if repair is truly blocked or over budget."
```

### 12.3 Health review blocker

If corrected G5 review cannot run:

- keep health core status unresolved;
- do not shape nutrition/training;
- carry exact review blocker.

### 12.4 Capacity blocker

If the owner is overloaded:

- reduce week, do not add discipline theater;
- pick one next true action;
- keep cuts explicit.

Example:

```yaml
capacity_mutation:
  new_fact: "Owner has 50% expected capacity."
  remove:
    - optional canon
    - health review if game is primary and urgent
  keep:
    - one game dependency action
    - life-reset contract review
```

## 13. Reset behavior

Reset means "rebuild the operating stance from current reality."

It does not mean "erase the week" or "punish the owner."

### 13.1 Daily reset

Daily reset is not a full daily runtime protocol in v0.

It is a simple question:

> Given the Weekly Contract and today's real capacity, what is the next honest
> move?

Fields:

```yaml
day_reset:
  date:
  contract_items_remaining:
  real_capacity_today:
  blockers:
  next_honest_move:
  cut_today:
  evidence_to_save:
```

Example:

```yaml
day_reset:
  date: 2026-06-25
  contract_items_remaining:
    - game reverify
    - health review
  real_capacity_today: "low"
  blockers:
    - "sleep poor / attention low" # practical signal, not medical diagnosis
  next_honest_move: "Run light source refresh, defer hard shape."
  cut_today:
    - "no canon"
  evidence_to_save:
    - "capacity lower than planned"
```

### 13.2 Midweek reset

Triggered by:

- major blocker;
- unexpected family obligation;
- serious capacity drop;
- source direction changes;
- owner wants to add a large new commitment.

Midweek reset uses the change rule:

```yaml
midweek_reset:
  trigger:
  new_fact:
  contract_impact:
  keep:
  remove:
  add:
  owner_acceptance:
```

Example:

```yaml
midweek_reset:
  trigger: "game repair remains blocked"
  new_fact: "F1/F2 repair did not close after one focused attempt."
  contract_impact: "Wave 2 shape cannot be selected this week."
  keep:
    - "record exact blocker"
    - "health corrected review"
  remove:
    - "game Wave 2 shape"
  add:
    - "one short blocker handoff"
  owner_acceptance: required
```

### 13.3 Full week reset

Only if the contract became invalid.

Examples:

- major family emergency;
- owner explicitly rejects the plan;
- source direction state changed enough that selected outcomes are false;
- clinical/safety risk appears and discipline should not be intensified.

Full reset output:

- current week contract killed or simplified;
- no moral debt;
- next small contract.

## 14. Drift patterns and responses

### Drift 1: private engineering tunnel

Signal:

- game consumes all attention;
- no player-facing or review pressure;
- health/life supports disappear.

Response:

- life-reset does not stop the game by default;
- it names the risk;
- preserves health review/floors if already selected;
- ensures game work still follows its own evidence gates.

### Drift 2: planning becomes the work

Signal:

- many templates;
- no actual source-direction movement;
- tool decisions;
- perfect board design.

Response:

- cut tooling;
- keep one Markdown tracker;
- run a real source-direction action.

### Drift 3: new idea flood

Signal:

- owner adds books, practices, tools, modules, spiritual ideas, social activities
  mid-week.

Response:

- capture all;
- select none by default;
- weekly review triages.

### Drift 4: guilt-based expansion

Signal:

- "I should also do health, canon, Solmax, daily routine, backlog, training,
  book, prayer, everything."

Response:

- return to capacity;
- one primary, one secondary, one experiment;
- cuts are success.

### Drift 5: avoidance disguised as support work

Signal:

- optional canon/status/tooling appears exactly when game contract repair is
  hard.

Response:

- ask whether the primary blocker has a next honest action;
- if yes, do it first;
- if no, explicitly mutate contract.

## 15. How evidence is saved

Life-reset stores only weekly-level evidence.

### 15.1 Evidence life-reset may save

- accepted Weekly Contract;
- source summaries;
- explicit cuts;
- midweek mutations;
- blocker summaries;
- review verdicts;
- owner acceptance;
- weak-link decisions.

### 15.2 Evidence life-reset must not save

- raw health daily logs;
- raw nutrition / training data;
- game implementation details;
- game production task state;
- full chat transcript as source of truth;
- clinical/private material beyond what is needed for safe planning.

### 15.3 Example evidence summary

```yaml
week_evidence:
  promised:
    - game contract repair/reverify path
    - health corrected review
    - life-reset weekly graph v0
  actual:
    - game repair done, reverify blocked on one finding
    - health review done: met
    - life-reset held cuts
  drift:
    - two new tool ideas captured, not added
  decisions:
    - next week starts with game reverify before Wave 2 shape
    - health next-bet decision postponed to Sunday review
  cuts_that_held:
    - Solmax
    - permanent tooling
    - daily runtime
```

## 16. Variant weeks

The same weekly graph should handle different outcomes.

### Variant A: Game-first week succeeds

Flow:

1. Repair contracts.
2. Re-verify clean.
3. Shape Wave 2.
4. Health review either runs in a secondary slot or moves to next week.

End state:

- game Wave 2 bet approved or ready;
- life-reset proves it can protect primary focus;
- health review maybe pending but intentionally cut.

Risk:

- health gets delayed again.

Review question:

- Was delaying health a conscious cut or silent drift?

### Variant B: Game blocker persists

Flow:

1. Repair attempt fails or remains blocked.
2. Wave 2 shape is cut.
3. Health review becomes the next honest outcome.

End state:

- exact game blocker preserved;
- health review closed;
- week still successful because it did not fake progress.

Risk:

- owner feels blocked and starts random work.

Review question:

- Did the graph help convert frustration into an explicit route?

### Variant C: Health review becomes primary

Trigger:

- owner chooses body/system health as more important this week;
- game can wait without immediate harm.

Flow:

1. Health corrected G5 review.
2. If met, choose next health bet later.
3. Game only gets a small source refresh.

Boundary:

- life-reset still does not prescribe nutrition/training.

Risk:

- game loses momentum during a commercial-pressure direction.

Review question:

- Was this a real priority choice or avoidance of game complexity?

### Variant D: Low-capacity week

Trigger:

- real calendar / family / energy reduces capacity.

Flow:

1. Select only one source-direction action.
2. Keep life-reset experiment small.
3. Cut optional and secondary items.

Contract:

```yaml
selected:
  - one game repair attempt OR health review
  - weekly graph v0
cut:
  - everything else
```

Success:

- honest week, not heroic week.

### Variant E: New idea week

Trigger:

- owner brings many attractive new ideas.

Flow:

1. Capture all.
2. Pick at most one tiny standalone activity if capacity exists.
3. Do not create modules.
4. Review backlog Sunday.

Success:

- ideas not lost;
- week not hijacked.

## 17. What changes over the week

### 17.1 Card statuses change

Example:

```text
Sunday:
  W25-G1 selected
  W25-G2 candidate blocked by G1
  W25-G3 candidate blocked by G2
  W25-H1 selected
  W25-S1 cut

Monday:
  W25-G1 doing

Tuesday:
  W25-G1 done
  W25-G2 doing

Wednesday:
  W25-G2 blocked
  W25-G3 cut this week
  W25-H1 doing

Thursday:
  W25-H1 done

Sunday review:
  primary outcome partially met
  secondary outcome met
  next week starts from exact game blocker
```

### 17.2 Contract can mutate

Mutation is explicit:

```yaml
mutation:
  date:
  previous_commitment:
  new_fact:
  removed:
  added:
  reason:
  owner_accepted:
```

No silent mutation.

### 17.3 Backlog changes

Backlog v0 has simple statuses:

```yaml
backlog_statuses:
  inbox: "captured, not judged"
  candidate: "might be selected later"
  parked: "not now"
  routed: "belongs to another direction"
  dropped: "not worth keeping"
```

Example:

```yaml
backlog:
  - idea: "Trello permanent board"
    status: parked
    reason: "tooling not proven by v0"
  - idea: "dance activity"
    status: candidate
    reason: "possible standalone activity later"
  - idea: "Solmax resume"
    status: routed
    reason: "requires separate Solmax resume session"
```

## 18. Review at the end

Weekly Review should be able to judge the system, not just the owner.

### 18.1 Review prompts

1. Did the contract distinguish outcomes from wish-list items?
2. Did source directions keep ownership?
3. Were cuts real?
4. Did new ideas stay captured without hijacking the week?
5. Did the tracker reduce chaos or add bureaucracy?
6. Did we know what to do when a blocker appeared?
7. Did the owner feel helped or controlled?
8. What one thing should change next week?

### 18.2 Review decisions

Allowed decisions:

- hold;
- mutate;
- kill;
- route;
- research;
- simplify.

Example:

```yaml
review_decision:
  verdict: mutate
  reason: "Dependency lane was useful, but daily reset was too vague."
  change_next_week: "Add one daily next-honest-move line, not a full daily runtime."
```

## 19. Lens sweep for this dry-run

### Weekly execution

Needs work.

Task:

- prepare and run the Sunday Weekly Contract.

Reason:

- this is the core lens of the node.

### Daily discipline

Needed only lightly.

Verdict:

- not a full task in v0.

Reason:

- daily runtime is a separate node; v0 only includes minimal daily reset sketch.

### Cross-direction integration

Needs work.

Task:

- import game / health / Solmax summaries without taking ownership.

### Improvement and learning

Needs light work.

Task:

- capture new ideas as backlog candidates, not commitments.

### Spirit and transcendence

Not needed as a task in this bet.

Reason:

- spiritual ideas can be captured, but no module/practice is shaped in weekly
  graph v0.

### Inner work and disclosure

Not needed as a task in this bet.

Reason:

- owner state can inform capacity, but no psychological process is prescribed or
  shaped here.

### Fatherhood and example

Not needed as a separate task.

Reason:

- family/time constraints can enter capacity and cuts; no separate fatherhood
  module in v0.

### System quality

Needs work.

Task:

- keep the graph Markdown/simple and portable; avoid permanent tooling.

### Safety

Needs work as a boundary.

Task:

- do not intensify discipline when the right move is reduce, route, or seek
  appropriate support.

## 20. Real cuts for the first bet

These cuts should be in the actual shaped bet.

1. No real operation before Sunday planning.
2. No daily runtime protocol.
3. No process/activity modules.
4. No permanent tool / provider / repo architecture.
5. No Solmax/W0.
6. No nutrition/training/medical prescriptions.
7. No game production tasks authored by life-reset.
8. No full backlog system.
9. No automation.
10. No attempt to plan more than one week.

## 21. Riskiest assumptions

### Assumption 1

The weekly graph can stay small enough that it helps rather than becoming
planning bureaucracy.

Test:

- Sunday planning produces an accepted contract without expanding into a full
  tool/system design.

### Assumption 2

Source-direction imports can be useful without duplicating ownership.

Test:

- game / health / Solmax summaries influence the week, but life-reset does not
  rewrite their tasks or raw data.

### Assumption 3

The owner will accept explicit cuts as a feature, not as loss.

Test:

- Solmax, permanent tooling, daily runtime, and optional ideas stay cut unless a
  real mutation removes competing volume.

### Assumption 4

A single Markdown-style tracker is enough for the first week.

Test:

- board/table can represent selected, blocked, done, cut, and evidence without
  tool choice.

## 22. Suggested first active bet from this dry-run

This is the shape candidate implied by the document.

```yaml
active_bet_candidate:
  node: g-lr-weekly-operating-graph
  appetite: "until Sunday 2026-06-21 evening planning + one real weekly contract"
  goal: |
    A minimal Weekly Operating Graph v0 is prepared, dry-run against current
    game/health/Solmax state, and used in the Sunday planning session to accept
    the real Weekly Contract for 2026-06-22..2026-06-28.
  done_when:
    - dry-run document exists;
    - Sunday input checklist is used;
    - real Weekly Contract is accepted with sources, capacity, selected slices,
      explicit cuts, and change rule;
    - next work CALL is ready for running the first selected weekly slice.
  kill_by:
    date: 2026-06-21
    threshold: |
      If the Sunday session cannot produce a minimal accepted Weekly Contract
      without selecting permanent tooling, daily runtime, modules, or source-
      direction ownership, kill/review and simplify.
```

## 23. What the next real Sunday session should ask

1. What fixed commitments exist from 2026-06-22 to 2026-06-28?
2. How many deep-work blocks are realistically available?
3. Is game still the primary source direction this week?
4. Should health corrected review be selected this week or consciously cut?
5. Is Solmax still held?
6. What one thing would make the week feel alive but not overloaded?
7. Which optional ideas should be captured and not selected?
8. What explicit cuts do you accept?
9. What is the rule for changing the week?
10. Do you accept the Weekly Contract?

## 24. The key owner-facing rule

The week is not a prison and not a wish-list.

It is a contract with a mutation rule.

If reality changes, the week changes honestly:

- name the new fact;
- cut something real;
- update the contract;
- preserve evidence.

If nothing real changed, new ideas wait.

END_OF_FILE: live/life-reset/work/weekly-operating-graph-dry-run-v0.md
