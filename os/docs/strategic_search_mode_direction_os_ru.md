# Strategic Search Mode для Direction OS

**Тип документа:** исследовательско-проектный пакет для workflow-ассистента / maintenance-сессии  
**Дата:** 2026-06-11  
**Статус:** proposal, не patch; не применять напрямую без `os/MAINTENANCE.md`  
**Цель:** улучшить planning/intelligence layer Direction OS так, чтобы система не просто составляла аккуратные планы, а в рискованных направлениях работала как стратегический поисковый двигатель для solo owner + AI agents.

---

## 1. Executive summary

Direction OS уже силён в сессионной дисциплине, состоянии в git, delegation, evidence gates, scope control, rolling-wave planning, appetite, kill criteria и review через refutation. Его слабое место — не execution, а **стратегический поиск до выбора бета**.

Нужен не механизм вида “попроси модель предложить 5 вариантов и выбрать лучший”. Это поверхностно и не решает ключевую проблему LLM: модель легко выдаёт несколько красиво звучащих синонимов одного и того же плана, затем уверенно выбирает один из них. У LLM нет надёжного встроенного evaluator для стратегических идей. В рискованных направлениях вероятность сразу выбрать правильную траекторию низкая; правильная система должна ожидать ошибки и строить процесс так, чтобы после каждого короткого цикла уменьшалась неопределённость.

Предлагаемый механизм: **Strategic Search Mode**.

Коротко:

```text
Direction OS должен не угадывать лучший план сразу,
а искать стратегическое пространство через гипотезы, разные генотипы опций,
операторы поиска, быстрые probes, rollback boundaries, external evidence
и review update после каждого бета.
```

Strategic Search Mode включается не всегда. Он нужен для high-uncertainty / high-upside / competitive направлений, где обычная протоптанная дорожка почти наверняка проигрывает большим организациям. Для health/safety/legal/irreversible domains тот же OS должен переключаться в conservative evidence mode.

Главная формула режима:

```text
ambition
→ strategic search space
→ raw option population
→ synonym collapse + diversity filter
→ adversarial triage
→ first probe, not final plan
→ evidence from world
→ review updates search space
→ next probe / branch expansion / branch kill
```

---

## 2. Scope и границы

Этот документ не является готовым patch и не должен напрямую изменять `os/**`. Его нужно использовать как вход для будущих maintenance-сессий.

Перед реализацией workflow-ассистент должен прочитать авторитетные repo sources:

```text
AGENTS.md
os/KERNEL.md
os/MAINTENANCE.md
os/FRICTION.md
os/plays/map.md
os/plays/shape.md
os/plays/research.md
os/plays/review.md
os/plays/pulse.md
os/schema/packets.md
os/schema/direction-files.md
os/docs/REQUIREMENTS.md
os/docs/DESIGN.md
os/docs/RESEARCH_BASIS.md
```

`archive/**` использовать только как frozen legacy evidence, never authority.

Жёсткие ограничения, которые надо сохранить:

```text
- one session = one job;
- owner is arbiter;
- state in git;
- six state file types only;
- no new permanent planning bureaucracy;
- rolling-wave detail;
- appetite before tasks;
- kill criteria;
- evidence gates;
- research children inform, never decide or write state;
- small diffs;
- OS changes only through os/MAINTENANCE.md;
- one mechanism per maintenance session where possible.
```

---

## 3. Core diagnosis

### 3.1 What is missing

Current Direction OS can shape a bet once a node exists. It can cut scope, set appetite, define kill criteria, test riskiest assumptions and review by evidence. The missing piece is earlier:

```text
How does the system search the strategic option space before it commits appetite?
```

Without a structural search mechanism, a strong LLM tends to produce:

```text
- polished but average advice;
- generic startup/product/marketing patterns;
- five variants of the same conventional path;
- convincing narratives without real evidence channels;
- recommendations that are hard to distinguish from prose quality;
- premature convergence on the first plausible plan.
```

### 3.2 Why “give 5 options” is not enough

A list of options is not strategic diversity. Five options can be the same genotype with different surface phrasing.

Example of fake diversity:

```text
1. Build an MVP.
2. Build a prototype.
3. Build a vertical slice.
4. Build a demo.
5. Build a proof of concept.
```

These may differ in wording, but if they share the same target, mechanism, distribution channel, proof channel and main assumption, they are strategically identical.

The workflow needs an explicit definition of “different”. It also needs a way to choose the next test without pretending that the model can know the best final plan.

### 3.3 Correct target

The target is not:

```text
Pick the best plan.
```

The target is:

```text
Pick the next bounded probe that most improves the search trajectory:
- kills or strengthens a major assumption;
- exposes a real signal from the world;
- uses owner-specific edge or AI leverage;
- has acceptable downside and rollback;
- opens a better next branch if true;
- closes a costly branch if false.
```

---

## 4. Strategic Search Mode: core concept

Strategic Search Mode is a mode inside existing plays, not a new state layer and not a new permanent council.

It should be activated when one of these is true:

```text
- The direction is competitive, high-upside, high-uncertainty or creative.
- The owner explicitly asks for asymmetric/deep strategic search.
- The outside view says the conventional path is likely to lose.
- Review shows that ordinary execution is not producing progress.
- The next move is strategically consequential and not just routine execution.
```

It should not be activated when:

```text
- The work is routine execution.
- The path is known and low uncertainty.
- The domain is health/safety/legal/irreversible and requires conservative evidence.
- The bottleneck is doing already-selected work, not strategic search.
- The planning cost would exceed the appetite of the decision.
```

Core rule:

```text
In Strategic Search Mode, options are hypotheses, not plans.
A bet is a probe, not a scaled execution commitment.
Review updates the search space, not only task status.
```

---

## 5. The Strategic Genome

To prevent fake diversity, each strategic option must be represented as a compact strategic genome.

### 5.1 Genome fields

```text
option_id:
  stable short id within the session only, e.g. o-1

promise:
  What external result this option tries to create.

target:
  For whom / which segment / which situation.

pain_or_desire:
  What pain, desire, job-to-be-done, curiosity or pressure it exploits.

product_mechanism:
  How the option creates value or impact.

distribution_wedge:
  How it reaches people, resources, users, buyers, collaborators or evidence.

proof_channel:
  What observable signal from the world could validate or kill it.

owner_edge:
  What owner-specific skill, taste, asset, constraint, network, repo, habit,
  speed, weirdness or accumulated context makes this option non-generic.

AI_leverage:
  What AI agents make disproportionately cheaper, faster, broader or safer.

constraint_inversion:
  Which constraint becomes an advantage, if any.

external_analogy:
  A mechanism transferred from another domain, not a surface metaphor.

main_assumption:
  The single most important thing that must be true.

secondary_assumptions:
  1-3 important supporting assumptions.

time_to_signal:
  How soon the probe can produce useful evidence.

rollback_cost:
  How painful it is to abandon, undo or quarantine the result.

downside:
  What bad thing happens if this is wrong.

next_if_true:
  What branch opens if the signal is positive.

next_if_false:
  What branch dies, mutates or gets parked if the signal is negative.
```

### 5.2 Distinctness rule

Two options are not distinct unless they differ on at least three strategic genes, and at least one of the differing genes is one of:

```text
target
product_mechanism
distribution_wedge
proof_channel
main_assumption
```

Surface differences do not count. Different wording, tone, scale or artifact type does not count if the strategic mechanism is the same.

### 5.3 Synonym collapse

The session must explicitly collapse synonyms before presenting final option cards.

Example:

```text
raw options:
- MVP
- prototype
- vertical slice
- demo
- proof of concept

collapse:
- These collapse into one genotype if all rely on the same target,
  mechanism, proof channel and assumption.

survivor:
- o-1 product-first prototype probe
```

The collapse log is part of the result in Strategic Search Mode. It is important because it prevents a model from satisfying the “multiple options” requirement with paraphrases.

---

## 6. Search operators

The workflow should not merely ask for “creative ideas”. It should run search operators. Search operators force the model into different regions of the latent/search space.

### 6.1 Baseline extraction and deletion

First define the obvious path:

```text
What would a competent normal team with normal resources do?
```

Then temporarily prohibit reliance on that path:

```text
Generate options that do NOT depend on the baseline path working.
```

Purpose: the baseline becomes negative space. This prevents the default plan from silently dominating.

Output:

```text
baseline:
  conventional path:
  why it is attractive:
  why it likely loses for this owner:
  what parts may still be useful:
```

### 6.2 Constraint inversion

For each hard constraint, generate at least one option that wins because of that constraint.

Examples:

```text
little time:
  narrower promise, faster loop, public cadence, automation, decisive cuts

little money:
  proof-before-build, asset-light work, pre-sale, borrowed distribution

solo owner:
  taste coherence, no coordination tax, fast weird pivots, one clear voice

AI agents:
  cheap variation, parallel research, code/content burst with evaluator,
  automated consistency checks, many probes in one appetite

no audience:
  make audience-building itself an evidence probe, not a marketing chore

health or energy constraint:
  conservative pacing, no-ruin design, low-volatility cadence
```

Constraint inversion must not romanticize constraints. Some constraints are simply binding. The operator is valid only if it names how the constraint creates a real strategic mechanism.

### 6.3 Far analogy transfer

Mine mechanisms from other domains. The goal is not to copy examples, but to transfer causal structure.

Required format:

```text
source_domain:
  e.g. indie games, open-source, scientific tools, creator economy,
  security research, education, hardware, marketplaces, speedrunning,
  modding communities, newsletters, experimental art

source_case:
  what happened

mechanism:
  why it worked

transferable_structure:
  what maps to this direction

mismatch:
  why the analogy may fail

resulting_option:
  the adapted strategy genotype
```

This operator uses the LLM’s broad latent knowledge more effectively than asking for generic advice inside the current domain.

### 6.4 Small-team asymmetry

Ask:

```text
What can one fast owner + AI agents do that a larger company structurally avoids?
```

Potential asymmetries:

```text
- use an old/unfashionable idea that large teams ignore;
- combine weird domains without committee approval;
- maintain a sharper taste/personality coherence;
- move publicly before polish;
- build tiny artifacts that are not worth a company’s process overhead;
- serve a niche too small or strange for a large roadmap;
- run many small probes without needing interdepartmental alignment;
- drop work instantly when evidence says it is dead.
```

Important: this is not “small is always better”. It says where to search for plausible asymmetry.

### 6.5 AI leverage explosion

Ask:

```text
What becomes possible if generation, research, coding, refactoring,
variant production, documentation or analysis is 5-20x cheaper?
```

But AI leverage is valid only with an evaluator. Otherwise it becomes entropy generation.

Valid AI leverage examples:

```text
- generate 30 variants, but test them against a defined rubric and user signal;
- code fast, but inside architecture boundaries and with checks;
- research many analogies, but extract mechanisms and mismatch;
- create marketing/content variants, but measure real engagement;
- produce prototypes, but run playtests or acceptance checks.
```

Invalid AI leverage:

```text
- “AI will build it quickly” without rollback;
- “AI can make content” without distribution/proof channel;
- “AI can research the market” without source quality and direct evidence;
- “AI can evaluate the ideas” as the only judge.
```

### 6.6 Failure inversion

Take premortem failures and turn them into search operators.

Examples:

```text
failure: nobody cares
→ option: first bet measures demand, not product quality

failure: scope eats project
→ option: absurdly narrow artifact with hard appetite and visible kill_by

failure: big companies can copy
→ option: choose moat through taste, community, process, speed or trust,
  not feature count

failure: AI codebase rots
→ option: build rollback/evaluator/architecture harness before feature burst

failure: owner loses energy
→ option: direction cadence uses small irreversible wins and low context switching
```

### 6.7 Evidence-channel-first search

Generate options by proof channel instead of by solution idea:

```text
What options can produce a useful signal through:
- direct user behavior;
- willingness to pay;
- retention / repeated use;
- inbound interest;
- expert rejection;
- benchmark/check output;
- manual owner test;
- public response;
- reduction in uncertainty;
- negative signal that safely kills a branch?
```

This operator is useful when plans are too narrative-heavy.

### 6.8 Rollback-first search

Generate options that are deliberately easy to abandon.

```text
What is the highest-upside thing we can try that is still cheap to reverse?
```

This is especially relevant for solo owner + AI agents, because AI can create a lot of artifact mass quickly. The system must prevent high-speed irreversible accumulation.

---

## 7. Option generation procedure

Strategic Search Mode should use this procedure inside `map`, `review`, or a bounded `research` child.

### Step 1 — Recite state and decision

Restate:

```text
- direction mission;
- relevant root/node goal;
- owner constraints;
- current state;
- known evidence;
- what decision this search must inform;
- what must not be decided here.
```

### Step 2 — Baseline

Name the obvious path and why it is insufficient.

```text
baseline path:
why normal teams choose it:
why it likely loses / is insufficient here:
what components may still be reused:
```

### Step 3 — Choose search axes

Pick 5-7 strategic genes that matter most for this direction.

Typical axes:

```text
target
pain_or_desire
product_mechanism
distribution_wedge
proof_channel
owner_edge
AI_leverage
constraint_inversion
external_analogy
risk_mode
```

### Step 4 — Generate raw population

Generate 8-12 raw options using multiple search operators:

```text
baseline deletion
constraint inversion
far analogy transfer
small-team asymmetry
AI leverage explosion
failure inversion
evidence-channel-first
rollback-first
```

This raw population is allowed to be messy. The point is coverage, not elegance.

### Step 5 — Collapse synonyms

Remove or merge options that do not differ by the distinctness rule.

Return a collapse log:

```text
collapsed:
  raw o-2, o-5, o-8 → survivor o-2
reason:
  same target, same product mechanism, same proof channel, same main assumption
```

### Step 6 — Refute survivors

For each survivor:

```text
strongest reason this fails:
most fragile assumption:
what outside view says:
what evidence would change the recommendation:
what would make this unsafe or not worth it:
```

### Step 7 — Choose first probe, not final plan

Recommendation is not “choose this strategy forever”. Recommendation is:

```text
First probe: <bounded bet candidate>
Why this probe: <learning value, upside, owner edge, rollback, time to signal>
What it decides: <branch expands / dies / mutates>
```

### Step 8 — Produce owner-facing option cards

Only after raw population, collapse and refutation, present 3-5 cards.

Card format:

```text
option_id:
goal:
done_when:
why:
strategic_genes:
main_assumption:
evidence_needed:
first_probe:
rollback/downside:
recommendation:
```

---

## 8. Selection logic: value of probe

Strategic Search Mode should not pretend to calculate exact expected value. Use coarse labels: `low`, `medium`, `high`.

### 8.1 Probe score factors

```text
learning_value:
  How much uncertainty this probe removes.

upside_if_true:
  What opens if the assumption is true.

owner_edge_fit:
  How strongly this uses owner-specific advantages or constraints.

AI_leverage:
  Whether AI agents create disproportionate speed, variation or checking ability.

time_to_signal:
  How fast a meaningful signal appears.

rollback_cost:
  How painful it is to undo or abandon.

downside:
  What harm or opportunity cost occurs if wrong.

outside_view_penalty:
  Whether comparable cases suggest this is unusually hard or commonly fails.
```

### 8.2 Decision rule

Prefer the probe that has:

```text
high learning_value
+ high upside_if_true
+ strong owner_edge_fit or AI_leverage
+ short time_to_signal
+ bounded downside
+ low rollback_cost
```

This is not a mathematical guarantee. It is a forcing function: it prevents selection by narrative attractiveness alone.

### 8.3 Recommendation format

```text
recommended_probe:
  <one probe>

why_not_best_plan:
  This is not selected as the final strategy. It is selected because it
  gives the strongest signal under appetite.

why_this_probe:
  learning_value:
  upside_if_true:
  edge_fit:
  time_to_signal:
  rollback:
  downside:

what_would_change_the_recommendation:
  <specific evidence or owner decision>
```

---

## 9. Bet as probe

In Strategic Search Mode, a shaped bet should be a probe.

Current Direction OS already has appetite, minimal solution, scope hammer, lens sweep, riskiest assumption and kill_by. Strategic Search Mode changes the interpretation:

```text
A bet is invalid if it mainly spends appetite executing an untested strategic path
without producing a decision-relevant signal.
```

### 9.1 Probe contract

Add conceptually to shape output:

```text
hypothesis:
  What must be true for this branch to deserve more appetite.

signal:
  What observable result will update us.

fastest_test:
  The smallest action that can produce that signal.

rollback:
  How we abandon, undo, quarantine or stop the path.

kill_by:
  Metric + threshold + date.

next_if_true:
  What branch opens.

next_if_false:
  What branch dies, mutates or gets parked.
```

This does not require a new state file. Some of it can live in `NOW.md` inside the active bet if adopted; richer rationale can live in `history/`.

### 9.2 AI acceleration and entropy

Solo owner + AI agents can generate large amounts of code, content, documents or designs quickly. That is power, but also entropy. A fast AI burst can create hidden structural debt, inconsistent artifacts, or wrong-path commitment faster than a human team would.

Therefore, before a large AI-amplified execution burst, shape should ask:

```text
What evaluator exists?
What rollback exists?
What architecture or boundary prevents artifact mass from becoming irreversible?
What signal says we should scale generation?
What signal says we should stop?
```

Valid AI-amplified bet:

```text
- bounded appetite;
- clear evaluator/check/proof channel;
- rollback or quarantine path;
- limited artifact surface;
- first signal before scaling;
- review by a fresh session.
```

Invalid AI-amplified bet:

```text
- “generate a lot quickly” without evaluator;
- “we can fix later” without rollback;
- broad code/content production before strategic signal;
- no kill_by;
- no branch consequence if false.
```

---

## 10. Review as search update

Current review checks evidence and updates the tree. In Strategic Search Mode it should also update the search space.

### 10.1 Search update fields

Review should extract:

```text
killed_assumptions:
  Which assumptions are now false enough to stop relying on.

strengthened_assumptions:
  Which assumptions now have better evidence.

strengthened_edges:
  Which owner/AI/constraint edges proved real.

weakened_edges:
  Which supposed edges were fake or weaker than expected.

surprising_signal:
  What happened that the prior search did not predict.

branch_to_drop:
  Which strategic branch should be dropped or parked.

branch_to_expand:
  Which branch deserves the next shape/map attention.

option_mutations:
  New option variants suggested by evidence.
```

### 10.2 Where to store this

No new state file.

```text
- Full search update: history/<session>.md inside RESULT.
- Durable learning: knowledge/ only if another play will actually read it.
- TREE.md: only outcome-level node changes with owner approval.
- NOW.md: only active bet / decisions / open-call dispatch frontier.
```

### 10.3 Review output consequence

Review should not only say:

```text
bet met / partially met / not met
```

It should say:

```text
What did this bet do to the search space?
- branch expanded;
- branch killed;
- assumption weakened;
- edge strengthened;
- next probe recommended;
- map needed because strategic topology changed.
```

---

## 11. Domain-risk calibration

Strategic Search Mode must not mean “risky everywhere”. The same OS should behave differently depending on downside, reversibility, externality and evidence.

### 11.1 Risk posture

Proposed coarse modes:

```text
routine:
  Known path, low uncertainty, low downside. Do not run Strategic Search Mode.

explore:
  Competitive/creative/high-upside, bounded downside, reversible. Weird bets allowed.

balanced:
  Material opportunity cost or reputation cost, but reversible. Require outside view
  and evidence-raising first probe.

conservative:
  Severe downside or costly reversibility. Require stronger evidence and refutation.

safety_critical:
  Health, legal, financial ruin, irreversible harm, harm to others, regulated actions.
  No wild bets. First move reduces risk/uncertainty.
```

### 11.2 Risk variables

Use coarse labels, not fake precision.

```text
downside:
  trivial | bounded | severe | ruin

reversibility:
  reversible | costly | irreversible_or_unknown

externality:
  owner_only | affects_known_others | public_or_systemic

evidence:
  model_inference | weak_external | good_comparable | strong_direct_or_guideline
```

### 11.3 Decision rule

```text
Explore mode is allowed only when downside is bounded and rollback exists.

Balanced mode requires outside view and a first probe that raises evidence.

Conservative mode requires selection refutation and safer fallback.

Safety-critical mode prohibits high-variance self-experiment or irreversible action
as the first move. First task should be evidence review, professional guidance,
safe measurement, or risk-reducing action.
```

### 11.4 Examples

Competitive indie/product direction:

```text
bounded downside + reversible + owner-only + weak evidence
→ explore mode
→ permit weird/high-variance probe if appetite, kill_by and rollback are clear
```

Health intervention:

```text
severe downside + possibly irreversible + medical uncertainty
→ safety_critical
→ no wild bet; first move evidence/professional check/safe measurement
```

Public launch with reputation risk:

```text
severe-ish downside + costly rollback + public externality + weak evidence
→ balanced/conservative
→ prefer private test, limited audience, or reversible signal before full launch
```

---

## 12. Preventing generic LLM output

Strategic Search Mode must include workflow-level anti-genericity checks.

### 12.1 Noun replacement test

```text
Replace owner/direction/product nouns with generic placeholders.
If the recommendation still reads as useful, it is too generic.
```

To pass, the recommendation must depend on at least three of:

```text
- current state fact;
- owner edge;
- hard constraint;
- external evidence or explicit evidence gap;
- specific assumption test;
- concrete rollback/downside;
- named distribution or proof channel;
- actual branch consequence.
```

### 12.2 Generic smell list

Reject or rewrite recommendations built mainly from:

```text
- build MVP;
- talk to users;
- do market research;
- create content;
- focus on niche;
- validate demand;
- improve quality;
- build community;
- make roadmap;
- use AI to automate;
- iterate quickly.
```

These are not banned as actions. They are banned as unanchored strategy. Each must specify:

```text
which target;
which mechanism;
which proof channel;
which owner edge;
which assumption;
which signal;
which rollback;
why now.
```

### 12.3 LLM role separation

Use LLM for:

```text
- generating raw options;
- analogical transfer;
- mutation;
- refutation;
- source retrieval;
- comparison against explicit criteria;
- drafting option cards.
```

Do not trust LLM alone for:

```text
- final strategy choice;
- market validation;
- medical/safety recommendation;
- proof that users care;
- proof that a plan is feasible;
- proof that code/content entropy is acceptable.
```

External evidence, owner decision, direct signals, tests, check output and review gates remain authoritative.

---

## 13. How this maps onto existing plays

### 13.1 `map`

Current role: build/revise goal tree with owner.

Strategic Search addition:

```text
Before final candidate cards in high-uncertainty competitive directions,
map runs search space expansion:
- baseline;
- axes;
- search operators;
- raw population;
- synonym collapse;
- survivor cards;
- recommendation of first branch/probe.
```

Map should not generate tasks. It only produces outcome-level nodes and next shape CALL.

### 13.2 `research`

Current role: answer one bounded question, write nothing directly.

Strategic Search addition:

```text
A parent may issue a strategic_search research CALL.
The child returns a population of strategic genotypes, collapse log,
refutations, evidence limits and recommended first probe.
The child does not decide strategy and does not write state.
```

This is the safest first implementation path because `research` already has the “child informs parent” contract.

### 13.3 `shape`

Current role: turn one node into active bet.

Strategic Search addition:

```text
In strategic_search mode, shape treats the bet as a probe.
It is invalid if it spends appetite without producing a decision-relevant signal.
It records hypothesis, signal, fastest_test, rollback, next_if_true and next_if_false.
```

### 13.4 `review`

Current role: close bet, verify, harvest, select next.

Strategic Search addition:

```text
Review updates the search space:
- assumptions killed/strengthened;
- edges killed/strengthened;
- surprising signals;
- branch to drop/expand;
- option mutations.
```

### 13.5 `pulse`

Pulse should not execute strategic search. It may only route:

```text
- direction appears idle because no strategic branch is credible;
- repeated generic planning friction;
- parked strategic captures now look urgent;
- maintenance suggestion if the Strategic Search mechanism creates friction.
```

---

## 14. CALL template for strategic search research

Use this as a parent-generated child call. It can be pasted into a research session.

```markdown
CALL <id>
to: research
direction: <direction-id>
play: research
node: <g-xxxx>
goal: |
  Produce a strategic search population for <node/direction decision>.
  The goal is not to choose a final plan. The goal is to find distinct strategic
  genotypes and recommend the first evidence-producing probe.
context: |
  Read: live/<direction>/CHARTER.md, TREE.md, NOW.md, relevant knowledge/,
  and any owner-named sources.
  Current decision: <what parent needs to decide>.
  Owner constraints/edges: <summary if known>.
boundaries: |
  Do not write state. Do not choose final strategy. Do not produce generic
  MVP/content/user-research advice unless anchored to a strategic genome.
  Treat archive/** as evidence only if explicitly referenced; never authority.
done_when: |
  Return: baseline path, search axes, 8-12 raw options, synonym collapse log,
  3-5 surviving strategic genotypes, refutation for each, evidence limits,
  and recommended first probe with rollback/downside/time-to-signal.
return: |
  Sections:
  1. Baseline path and why it is insufficient.
  2. Search axes used.
  3. Raw option population.
  4. Synonym collapse log.
  5. Survivor option cards with strategic genome.
  6. Refutation and evidence gaps for each survivor.
  7. Recommended first probe, not final plan.
  8. Confidence, limits, and what would change the answer.
budget: one session
parent: <parent-session-id>
```

---

## 15. RESULT shape for strategic search research

Expected return format:

```markdown
RESULT <session-id> (call: <call-id>)
direction: <direction-id>   play: research   node/task: <node>
outcome: |
  Strategic search population produced for <decision>. This is not a final
  strategy choice; it informs parent map/shape/review.
evidence: |
  Sources used, analogies, outside-view references, and explicit limits.
state_changes: |
  none; return-to-parent only.
captures:
  - <optional ideas that should be parked, not executed now>
decisions_needed: []
log: research strategic-search <node>: returned option genotypes and first-probe recommendation
next: |
  return-to-parent <parent-session-id>

findings:
  baseline:
    conventional_path:
    why_insufficient:
  search_axes:
    - <axis>
  raw_population:
    - id: o-raw-1
      summary:
      operator:
      genome:
  synonym_collapse:
    - collapsed: [o-raw-2, o-raw-5]
      survivor: o-2
      reason:
  survivors:
    - id: o-1
      option_card:
        goal:
        done_when:
        why:
        strategic_genes:
        main_assumption:
        evidence_needed:
        first_probe:
        rollback:
        downside:
        next_if_true:
        next_if_false:
      refutation:
        strongest_case_against:
        outside_view:
        what_would_change_recommendation:
  recommended_first_probe:
    option_id:
    why_probe_not_plan:
    learning_value:
    upside_if_true:
    owner_edge_fit:
    AI_leverage:
    time_to_signal:
    rollback_cost:
    downside:
  confidence_and_limits:
```

Note: current `RESULT` schema does not have a `findings` field. If strict schema compatibility is required, put `findings` inside `outcome` or `evidence` as structured markdown. Do not introduce a third packet type.

---

## 16. Patch-level sketches

These are sketches only. Apply only through `os/MAINTENANCE.md`, one problem per session.

### 16.1 Minimal first patch: `os/plays/research.md`

Reason: safest adoption path. It allows strategic search as a bounded child without changing state schema.

```diff
 ## Notes
 
 - A research child never makes decisions for the parent and never touches state. It informs.
 - If the answer reveals work to do, that is a capture in the RESULT — the parent or shape triages it.
 - Respect the budget literally: better a partial answer on time than a perfect answer that burned the budget twice over.
+- A parent may request `strategic_search`: generate raw strategic options, collapse synonyms,
+  preserve distinct genotypes, refute survivors, and recommend a first evidence-producing probe.
+  The child still does not choose the parent strategy or write state.
```

This is small but does not by itself force parent plays to call it.

### 16.2 `os/plays/map.md`

```diff
+Strategic search mode: when the direction is high-uncertainty, competitive,
+or explicitly asks for asymmetric strategy, search before choosing.
+Name the baseline path; choose 5-7 strategic genes; generate raw options with
+baseline deletion, constraint inversion, far analogy, small-team asymmetry,
+AI leverage and failure inversion; collapse synonyms; present only distinct
+survivor cards. Two cards are distinct only if they differ on >=3 genes and
+main assumption.
+
 2. **Candidate cards** — propose 3–6 top-level outcomes. Each is presented as a separate card:
    - goal (an outcome in the world, not an activity)
    - done_when (verifiable)
    - **why — exactly how this node leads to the root's success criteria**
+   - strategic_genes — target/mechanism/distribution/proof/edge/AI_leverage as relevant
+   - main_assumption — what must be true
+   - evidence_needed — what signal would change the recommendation
+   - rollback/downside — why this is safe enough to explore
    - risk — what would kill or invalidate it
```

Potential issue: play budget. A maintenance session may need to compress existing wording.

### 16.3 `os/plays/shape.md`

```diff
+Strategic search mode: treat the bet as a probe, not a scaled execution plan.
+It is invalid if it spends appetite without a decision-relevant signal.
+State hypothesis, signal, fastest_test, rollback, next_if_true and next_if_false.
+
 6. **Riskiest assumption** — list the assumptions this bet rests on, ranked by kill-power.
```

Potential issue: `NOW.md` template may need room for probe fields. Prefer first storing rich detail in history; only add to NOW if proven useful.

### 16.4 `os/plays/review.md`

```diff
+In strategic_search mode, review also updates the search space: killed/strengthened
+assumptions, strengthened/weakened edges, surprising signals, branch_to_drop,
+branch_to_expand, and option mutations. Store rich detail in history; promote only
+durable learnings to knowledge/ when they have a read_by consumer.
+
 6. **Select next** — propose 2–3 candidate nodes for the next bet...
```

### 16.5 Optional schema patch: `os/schema/direction-files.md`

Only adopt if pilot proves these fields are read and useful.

```diff
 constraints:
   - <hard limits: time/week, money, health, values>
+
+risk_posture: <routine | explore | balanced | conservative | safety_critical>
+
+edges:
+  - <owner-specific advantage, constraint, asset, network, taste, repo, or AI leverage>
```

Risk: CHARTER grows and becomes self-mythology. If adopted, keep `edges` to 3-5 concrete items.

---

## 17. Pilot plan before OS changes

Do not change `os/**` first. Run manual pilots by including Strategic Search instructions in a CALL context.

### 17.1 Pilot cases

Use at least two cases:

```text
A. Competitive/reversible direction:
   high-upside, creative, startup-like, indie/product/market strategy.

B. Safety-sensitive direction:
   health, legal, irreversible personal risk, or other conservative domain.
```

### 17.2 Pilot sessions

```text
Session 1 — strategic_search research child
  Run the research CALL template.
  Output raw population, collapse log, survivor genotypes, refutations and first probe.

Session 2 — parent shape simulation
  Turn recommended first probe into a shaped bet.
  Check hypothesis, signal, fastest_test, rollback, kill_by, next_if_true/false.

Session 3 — adversarial review simulation
  Try to refute the probe.
  Decide whether the branch expands, mutates, parks or dies.
```

### 17.3 Pilot metrics

Track in session history, not a new file:

```text
real_diversity:
  Did survivors differ on >=3 strategic genes and main assumption?

specificity:
  Did options depend on owner/current-state facts?

decision_value:
  Did the mechanism change the recommended first bet/probe?

signal_quality:
  Would the first probe produce evidence or just activity?

rollback_quality:
  Is wrong-path cost bounded?

risk_calibration:
  Did competitive case become bolder while safety case became more conservative?

meta_cost:
  Did the process fit one session without becoming a planning attractor?
```

### 17.4 Adoption threshold

Adopt only if:

```text
- it changes the selected first probe or branch decision in at least one pilot;
- owner judges the options materially less generic;
- synonym collapse catches fake diversity;
- the mechanism fits within play budgets;
- no new state file is required;
- review can use the result later.
```

Kill or simplify if:

```text
- options remain generic;
- every session becomes strategic_search;
- the owner rejects the extra process as ceremony;
- probes do not produce evidence;
- review does not use the search update;
- planning time grows faster than execution value.
```

---

## 18. Maintenance sequencing

Do not apply all changes at once.

Recommended order:

```text
1. Add strategic_search allowance/return guidance to research.md.
   Smallest safe change; no state schema change.

2. Add a compact Strategic Search trigger to map.md and/or review.md.
   Parent sessions learn when to call strategic_search.

3. Add bet-as-probe language to shape.md.
   Ensures search output becomes evidence-producing bet, not prose.

4. Add search_update to review.md.
   Closes the loop so evidence changes future search.

5. Consider CHARTER risk_posture / edges only if pilots show they are repeatedly useful.
```

Each maintenance session should:

```text
- read os/MAINTENANCE.md;
- locate current rule/gap;
- design the smallest change;
- keep play <=600 words;
- avoid new state files;
- verify by walking through at least one competitive and one safety-sensitive scenario;
- log friction/fix as required.
```

---

## 19. Failure modes and countermeasures

### 19.1 Fake diversity

Failure:

```text
The model emits many options that are all the same strategic genotype.
```

Countermeasure:

```text
strategic genome + distinctness rule + synonym collapse log
```

### 19.2 LLM self-evaluation failure

Failure:

```text
The model selects the most elegant narrative rather than the best probe.
```

Countermeasure:

```text
choose probe by learning value, rollback, signal, downside and owner edge;
use external evidence and review, not model confidence
```

### 19.3 Overplanning attractor

Failure:

```text
Strategic Search Mode becomes a ritual that delays work.
```

Countermeasure:

```text
only activate under explicit triggers;
prefer research child with one-session budget;
first output is a probe, not a grand strategy;
kill if it does not change decisions
```

### 19.4 Risk leakage into safety domains

Failure:

```text
Bold startup logic contaminates health/legal/irreversible planning.
```

Countermeasure:

```text
risk posture: explore vs conservative vs safety_critical;
no wild self-experiment in safety-critical domains;
first move reduces risk or improves evidence
```

### 19.5 AI artifact entropy

Failure:

```text
AI agents generate a month of output in days, but the branch is wrong or structurally messy.
```

Countermeasure:

```text
no large AI burst without evaluator, rollback, architecture boundary and time-to-signal;
review by fresh session;
kill_by before scaling
```

### 19.6 Cargo-cult frameworks

Failure:

```text
The OS starts importing business-book frameworks and large matrices.
```

Countermeasure:

```text
operators and probes only;
coarse labels only;
no big scorecards;
no new state file;
remove mechanisms that do not change decisions
```

---

## 20. Evidence base and limits

This section distinguishes direct evidence, analogy and speculation.

### 20.1 Direct evidence: AI can homogenize creative output

Doshi and Hauser found that access to generative AI ideas can improve individual creative writing evaluations while making outputs more similar to one another. This supports the concern that unguided AI assistance may reduce collective diversity. [1]

Implication for Direction OS:

```text
Do not rely on “ask for ideas” alone. Add structural diversity filters.
```

### 20.2 Direct evidence: LLM idea generation has self-evaluation and diversity limits

A 2024 large-scale study with 100+ NLP researchers found LLM-generated research ideas were judged more novel than human expert ideas but slightly weaker on feasibility; the authors identified failures of LLM self-evaluation and lack of diversity as open problems. [2]

A 2025 follow-up execution study found an ideation-execution gap: LLM-generated ideas that looked strong at ideation stage degraded more after expert execution, with human ideas ranking higher on several post-execution metrics. [3]

Implication:

```text
Use LLM for generation/mutation/refutation, but force execution/evidence probes before commitment.
```

### 20.3 Direct evidence: AI ideation can increase fixation

A 2024 visual ideation experiment found AI image generator support led to higher fixation on an initial example; participants using AI produced fewer ideas with less variety and lower originality than baseline. [4]

Implication:

```text
Separate divergent search from convergent refinement. Do not let the first plausible artifact anchor the strategy.
```

### 20.4 Direct evidence: structured search + external knowledge can improve novelty/diversity in LLM ideas

Nova proposes iterative planning and search for external knowledge retrieval to improve LLM-generated scientific ideas; the paper reports substantially higher novelty/diversity, including 3.4x more unique novel ideas in its setting. [5]

Limit:

```text
Scientific idea generation is not the same as product/market strategy. Treat as evidence for process structure, not guaranteed strategy quality.
```

### 20.5 Strong analogy: Quality-Diversity / MAP-Elites

MAP-Elites and Quality-Diversity algorithms search for many high-performing but diverse solutions across user-defined dimensions instead of returning only one optimum. [6]

Implication:

```text
Direction OS should preserve strategically different genotypes and avoid early collapse.
```

Limit:

```text
Strategy lacks a clean numeric fitness function. Use probes and evidence channels as approximate evaluators.
```

### 20.6 Strong analogy: AlphaEvolve / FunSearch

AlphaEvolve uses LLMs inside an evolutionary loop with evaluators to improve algorithms; the key is not a single LLM answer but iterative generation plus feedback from evaluators. [7]

FunSearch similarly combines LLM-generated program candidates with automated evaluation and evolutionary search. [8]

Implication:

```text
For strategy, LLM-generated options must be passed through external/proxy evaluators: user behavior, market signal, tests, owner constraints, refutation and rollback.
```

### 20.7 Decision science: outside view and reference classes

Flyvbjerg’s reference class forecasting argues that project forecasts are distorted by optimism bias and strategic misrepresentation; actual outcomes from comparable reference classes help debias. [9]

Implication:

```text
Strategic options need outside-view notes. If outside view is hostile, the first probe must be especially cheap and evidence-producing.
```

### 20.8 Entrepreneurship: effectuation and affordable loss

Effectuation theory emphasizes starting from available means and limiting affordable loss under uncertainty rather than predicting the whole future. Startup research connects effectual logic with MVPs, customer involvement and technical debt tradeoffs. [10]

Implication:

```text
Explore mode should allow weird/high-variance bets only when loss is bounded and rollback exists.
```

### 20.9 Small-team asymmetry

Analysis of millions of papers, patents and software products found large teams tend to develop recent popular ideas while small teams are more associated with disruptive work drawing on older and less prevalent ideas. [11]

Implication:

```text
Smallness is not merely a disadvantage. Search should look for old, weird, neglected, niche or cross-domain mechanisms large teams avoid.
```

### 20.10 Safety domains: GRADE and precaution

GRADE provides a structured approach for assessing certainty of evidence and strength of healthcare recommendations. [12] The precautionary principle is relevant when uncertainty combines with serious or irreversible harm, though strong versions can become paralyzing. [13]

Implication:

```text
Safety-critical directions require conservative evidence gates. Do not import startup-style risk into health/legal/irreversible decisions.
```

---

## 21. What not to add

Do not add:

```text
- STRATEGY.md or any seventh state file;
- permanent multi-agent strategy council;
- large scoring matrices;
- generic “be creative/bold/specific” prompt language;
- a new default planning ceremony for all directions;
- synthetic user panels as evidence;
- full forecasting tournament;
- strategy work that bypasses owner approval for CHARTER/TREE changes;
- direct code/repo mutation instructions from parent OS beyond bounded executor CALLs;
- health/safety contrarian experiments.
```

Attractive but harmful pattern:

```text
“Let us add a robust strategy framework.”
```

Likely outcome:

```text
more meta-work, more fields, more fake precision, less execution.
```

Preferred pattern:

```text
one compact mode;
one bounded research child when needed;
one probe;
one review update;
kill if it does not change decisions.
```

---

## 22. Implementation recommendation

Recommended final design direction:

```text
Strategic Search Mode should become a compact optional mode across map/research/shape/review.
It should be invoked only for high-uncertainty, competitive or explicitly strategic decisions.
It should define options as strategic genotypes, force search operators, collapse synonyms,
refute survivors, choose first probes by learning value and rollback, and update the search
space after review.
```

Minimal adoption path:

```text
1. Add strategic_search child-return guidance to research.md.
2. Add trigger/call guidance to map.md and review.md.
3. Add bet-as-probe language to shape.md.
4. Add search_update language to review.md.
5. Pilot before adding schema fields such as risk_posture or edges.
```

Core invariant to preserve:

```text
The OS must never claim that the model has selected the best strategy.
It may only claim that, under current evidence and constraints, a bounded probe
is the best next move for reducing uncertainty or exploiting an asymmetry.
```

---

## 23. References

[1] Anil R. Doshi, Oliver P. Hauser. “Generative artificial intelligence enhances creativity but reduces the diversity of novel content.” arXiv:2312.00506. https://arxiv.org/abs/2312.00506

[2] Chenglei Si, Diyi Yang, Tatsunori Hashimoto. “Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers.” arXiv:2409.04109. https://arxiv.org/abs/2409.04109

[3] Chenglei Si, Tatsunori Hashimoto, Diyi Yang. “The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas.” arXiv:2506.20803. https://arxiv.org/abs/2506.20803

[4] Samangi Wadinambiarachchi et al. “The Effects of Generative AI on Design Fixation and Divergent Thinking.” arXiv:2403.11164. https://arxiv.org/abs/2403.11164

[5] Xiang Hu et al. “Nova: An Iterative Planning and Search Approach to Enhance Novelty and Diversity of LLM Generated Ideas.” arXiv:2410.14255. https://arxiv.org/abs/2410.14255

[6] Jean-Baptiste Mouret, Jeff Clune. “Illuminating search spaces by mapping elites.” arXiv:1504.04909. https://arxiv.org/abs/1504.04909

[7] Alexander Novikov et al. “AlphaEvolve: A coding agent for scientific and algorithmic discovery.” arXiv:2506.13131. https://arxiv.org/abs/2506.13131

[8] Bernardino Romera-Paredes et al. “Mathematical discoveries from program search with large language models.” Nature / FunSearch. Overview: https://deepmind.google/discover/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/

[9] Bent Flyvbjerg. “From Nobel Prize to Project Management: Getting Risks Right.” arXiv:1302.3642. https://arxiv.org/abs/1302.3642

[10] Effectuation and software startups: “An Effectual Approach to Software Startup Development.” arXiv:2103.07999. https://arxiv.org/abs/2103.07999

[11] Lingfei Wu, Dashun Wang, James A. Evans. “Large teams develop and small teams disrupt science and technology.” arXiv:1709.02445. https://arxiv.org/abs/1709.02445

[12] GRADE approach overview. https://www.gradeworkinggroup.org/ and https://en.wikipedia.org/wiki/GRADE_approach

[13] Precautionary principle overview and non-naive use under serious/irreversible harm. https://en.wikipedia.org/wiki/Precautionary_principle and Taleb et al., arXiv:1410.5787, https://arxiv.org/abs/1410.5787

---

## 24. Copy-paste maintenance request seed

Use this only when ready to run a real maintenance session.

```markdown
MAINTENANCE REQUEST
what: |
  Add a compact Strategic Search Mode mechanism to Direction OS so high-uncertainty,
  competitive directions can search strategic option space structurally instead of
  producing generic LLM plans. The mechanism should treat options as strategic genotypes,
  use search operators, collapse synonyms, refute survivors, recommend first probes rather
  than final plans, and update the search space in review.
where: |
  Start with the smallest safe change. Candidate files:
  os/plays/research.md for strategic_search child guidance;
  os/plays/map.md and os/plays/review.md for triggers and parent use;
  os/plays/shape.md for bet-as-probe;
  only later consider os/schema/direction-files.md for risk_posture/edges.
expected: |
  One compact mechanism, no new state file, no large planning bureaucracy, no generic
  “give 5 options” rule. Preserve Direction OS constraints: one session = one job,
  six state file types, rolling-wave detail, appetite before tasks, kill_by, evidence gates,
  owner as arbiter, and small diffs. Implement one minimal mechanism per maintenance session.
```

END_OF_DOCUMENT
