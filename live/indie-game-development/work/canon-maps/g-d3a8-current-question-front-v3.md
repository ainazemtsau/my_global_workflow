# g-d3a8 — Current Design Question Front v3

status: OWNER-APPROVED CARTOGRAPHY
approved_on: 2026-07-20
authority: routing, dependency and visual-work authority only; not Frame, not a paper answer, not canon, not image authority
governing_process: Canon Forge v3
supersedes_as_current_map:
  live/indie-game-development/work/canon-maps/
  g-d3a8-current-question-front-v2.md
owner_verdict: |
  «ну ок, я с тобой согласен с вариантом А, я в принципе утверждаю»

  «даже то, что сейчас есть по визуалу, это не канон, оно может
  измениться»

  «визуал газа отдельно проработать надо»

  «визуал мы не хотим тратить сильно много сил»

  «А так утверждаю вариант А, вот, но прими во внимание мои заметки.»

reconciled_on: 2026-07-21
reconciliation_verdict: |
  «ПРИНИМАЮ ПРОСТОЙ МАРШРУТ: один граф тем, один Canon Forge,
  формат ответа определяется типом вопроса; dashboard позже как
  представление тех же данных.»

## 1. Authority

Current authority order:

1. Current owner instruction.
2. Direction OS and active local plays.
3. Minimum Game Frame v2 — accepted whole-game Frame, not canon.
4. Gas Sphere extraction/custody Frame — accepted specialized Frame,
   not canon.
5. Current canon INDEX and its listed cards:
   - c-001 investigation readiness;
   - c-002 gas behavior jobs;
   - c-003 visual-development contract.
6. Historical questions, old maps, old StyleBible material, screenshots,
   generated images and previous answers — evidence only.

This map answers no gameplay- or visual-design question.

This is one graph of game topics and their sourced questions.
Dependencies decide what can be discussed now; `answer_shape` selects
the working format. A visual question stays in the same graph and uses
the same Canon Forge.

### Paper and visual completeness rule

The canon track designs the game as fully as currently possible through:

- text;
- diagrams;
- scenario descriptions;
- state and sequence plates;
- AI-generated scratch renders;
- candidate visual sets;
- owner-selected reference plates;
- gameplay mockups;
- paper UI, camera and environment hypotheses.

Lack of implementation, a greybox or playtest is not a blocker for this
design work.

`proof_later` means only that paper or images do not establish actual fun,
runtime legibility, real co-op behavior, production cost or market response.

Feasibility remains a design constraint. It does not become a reason to
stop paper work and wait for a product implementation.

### Current visual-authority reset

Current owner instruction establishes:

- no existing environment image or style document is current visual canon;
- old q-visual-style / StyleBible / screenshots are revisable historical
  reference material only;
- old gas visualization has no authority and must not be reused as a
  visual lock;
- the visual language of gas is unworked and must be designed separately;
- the visual language of the Sphere is unworked;
- the visual language of the player character is unworked;
- placeholders may appear in exploratory mockups only when explicitly
  marked as placeholders;
- minimalism, simplicity and low visual production cost are current owner
  constraints/preferences, not a frozen palette or exact style.

## 2. Post-c-002 reconciliation verdict

q-gas-behavior-jobs is RESOLVED / ADMITTED.

Current canon now supplies:

- movement/control as the minimum common behavior layer;
- Counter / Brake / Time;
- movement-job admission criteria;
- volume as strength;
- shell as general endurance;
- universal capture;
- no gas × shell compatibility;
- no mandatory N-player eligibility gate;
- movement-first, not movement-only.

This removes c-002 as a blocker from all downstream nodes.

It does not answer:

- gas visual language;
- Sphere visual language;
- exact read channels;
- exact physical gas laws;
- gas roster;
- reactions;
- damage;
- controls;
- capacity;
- economy;
- tools;
- artifacts;
- co-op composition;
- run structure;
- implementation.

V0 is RESOLVED / ADMITTED as c-003.

After the approved Canon Forge reconciliation is applied, V1 is the next
selected question.

## 3. Classification vocabulary

standing:

- settled_non_canon_frame
- canon_resolved
- ready_design
- historical_re_admission_required
- open_design
- proof_nonblocking
- implementation_downstream
- superseded_or_invalid

Required graph status:

- ready
- needs_preface
- blocked
- downstream
- proof_later
- unclear

`proof_later` does not block upstream paper design.

## 4. Current dependency graph

accepted current Frames
  + c-001 investigation readiness
  + c-002 Counter / Brake / Time
     |
     +--> V0 minimal visual-development contract       [CANON RESOLVED /
     |                                                   c-003]
     |       |
     |       | owner-approved simple Forge format reconciliation
     |       v
     |     V1 gas + Sphere visual readability          [READY / NEXT CALL]
     |       |-----------------------------|
     |       v                             v
     |     F2 bounded bad-state scene      C1 later evidence
     |
     +--> D0 investigation pressure sources            [READY]
     |
     +--> F0 current floor-board read                  [READY /
     |                                                   NEW ADMISSION]
     |       |
     |       v
     |     F1 current floor loop                       [BLOCKED]
     |
     +--> E0 safe-return conversion                    [READY]
     |       |
     |       v
     |     T0 predictable tool roles                   [DOWNSTREAM]
     |
     +--> C0 4–8-player paper co-op composition        [READY]
     |       |
     |       v
     |     C1 actual co-op evidence                    [PROOF LATER,
     |                                                   NONBLOCKING]
     |
     +--> A0 artifact emergence                        [DOWNSTREAM]
             |
             v
           R0 complete finite-run spine                [DOWNSTREAM]
             |
             v
           I0 attendance/run continuity                [DOWNSTREAM]

E0 + A0 -> R0.
F0 + current Frames -> F1.
c-002 + V1 or another bounded concrete scene -> F2.
c-002 + E0 + recurring problems from floor/pressure work -> T0.
V1 + F1 + C0 -> C1 evidence route.

## 5. Nodes

### Q1 — Broad Sphere extraction and custody parent locks

plain_question:
  What broad physical activity turns nearby gameplay gas into a chosen
  growing Sphere and then into free physical cargo?
why_it_matters:
  The broad answer anchors all narrower questions and prevents a return to
  generic inventory or an unrelated extraction device.
answer_shape: loop_spine
status: downstream
standing: settled_non_canon_frame
dependency_type: implementation_downstream
depends_on: []
dependency_reason:
  The broad design direction exists in the accepted Sphere Frame. Only
  narrower design, visual and implementation questions remain.
blocks: []
do_not_solve_here:
  - exact controls
  - exact suction geometry
  - capacity
  - helper count
  - rupture
  - implementation
  - silent canon promotion of the whole Frame
needs_anchor: verbal_scene
confusion_traps:
  - treating the Frame as canon
  - reopening the whole extraction landscape
  - restoring an inventory item
  - restoring the old ring-fill mechanic by implication
forge_handoff:
  plain_question:
    No current broad extraction handoff.
  why_now:
    Reopen only if a later bounded question exposes a missing parent premise.
  must_decide:
    Only the newly exposed bounded gap.
  must_not_decide:
    A silent redesign of the accepted Sphere Frame.
  parent_locks:
    Active near-gas capture, visible transfer, player-chosen amount and free
    physical cargo remain accepted Frame direction.
  expected_answer_shape: loop_spine
  first_owner_question:
    Which exact parent premise is no longer sufficient?
  return_to_graph_if:
    A later visual or paper question cannot be stated without changing the
    broad extraction/custody direction.

### Q3-R — Gas behavior job grammar

plain_question:
  Which minimum physical differences must make gases produce different
  extraction, stopping and carrying decisions?
why_it_matters:
  It prevents universal capture from producing only decorative gas variety.
answer_shape: taxonomy
status: downstream
standing: canon_resolved
dependency_type: hard_prerequisite
depends_on: []
dependency_reason:
  The question completed Frame gate, Question gate, owner paper selection
  and separate owner canon admission.
blocks: []
do_not_solve_here:
  - redesign Counter / Brake / Time
  - gas roster
  - exact forces
  - reactions
  - damage
  - visual language
needs_anchor: verbal_scene
confusion_traps:
  - treating resolved as ready
  - treating movement-first as movement-only
  - inventing gas names from the taxonomy
  - assuming paper proves runtime readability
forge_handoff:
  plain_question:
    No current Forge handoff.
  why_now:
    The node is resolved and admitted.
  must_decide:
    Nothing unless a formal replacement is proposed later.
  must_not_decide:
    Extension or redesign inside downstream questions.
  parent_locks:
    c-002 in full.
  expected_answer_shape: taxonomy
  first_owner_question:
    What exact current evidence justifies proposing a replacement card?
  return_to_graph_if:
    A future bounded question exposes a direct contradiction with c-002
    rather than an ordinary open dimension.

### V0 — Minimal visual-development contract

plain_question:
  What minimum rules let us attach AI-generated images to design
  questions without accidentally treating placeholders, old screenshots
  or random generated details as canon?
why_it_matters:
  The admitted contract lets visual questions use generated material
  without granting authority to placeholders, historical screenshots or
  accidental details.
answer_shape: invariant
status: downstream
standing: canon_resolved
dependency_type: hard_prerequisite
depends_on:
  - current owner visual reset
  - current INDEX authority model
  - historical visual materials as evidence only
dependency_reason:
  The exact V0 artifact completed Gate F, Gate Q, owner paper selection
  and separate canon admission as c-003.
blocks: []
do_not_solve_here:
  - exact environment style
  - exact gas look
  - exact Sphere look
  - character design
  - camera design
  - UI design
  - actual image generation
  - product asset production
needs_anchor: none
confusion_traps:
  - old StyleBible treated as current canon
  - one generated image silently fixing many unrelated details
  - selected taste treated as final asset
  - placeholder character becoming character canon
  - low production cost collapsing into cheap-looking art
  - demanding a full art bible before any useful image
forge_handoff:
  plain_question:
    No current Forge handoff.
  why_now:
    V0 is resolved and admitted as c-003.
  must_decide:
    Nothing unless a formal replacement of c-003 is proposed.
  must_not_decide:
    Any actual appearance or silent extension of c-003.
  parent_locks:
    c-003 in full; old gas visuals remain invalid; only explicitly named
    properties can receive authority.
  expected_answer_shape: invariant
  first_owner_question:
    What exact current evidence justifies replacing c-003?
  return_to_graph_if:
    A future bounded question exposes a direct contradiction with c-003
    rather than an ordinary application of it.

### V1 — Gas and Sphere visual readability

plain_question:
  What should players see in the gas field and in the filled Sphere so they
  understand that this situation requires Counter, Brake or Time before the
  serious consequence has already happened?
why_it_matters:
  c-002 defines which decisions differ, but no valid visual language exists
  for reading those differences.
answer_shape: visual_plate
status: ready
standing: ready_design
dependency_type: visual_anchor
depends_on:
  - c-003
  - reconciled local/canon-forge
  - c-002
  - accepted Sphere Frame
dependency_reason:
  c-003 now defines visual authority and the reconciled single Forge
  provides the lawful format route. The actual visual answer remains
  fully open.
blocks:
  - gas visual language
  - Sphere visual language
  - visual sequence plates
  - field-legibility questions
  - bounded failure scenes
  - visual co-op scenarios
do_not_solve_here:
  - gas names or final roster
  - exact forces or cycles
  - final VFX implementation
  - renderer
  - final UI
  - character visual design
  - reactions
  - damage
needs_anchor: visual_plate
confusion_traps:
  - reusing invalid old gas imagery
  - different colour as the whole answer
  - decorative fog
  - one hero image instead of comparable gameplay situations
  - movement signal visible only after failure
  - placeholder character becoming binding
forge_handoff:
  plain_question:
    Which field, Sphere and motion signs make Counter, Brake and Time
    visually distinguishable before and during commitment?
  why_now:
    It is the next selected question after the applied reconciliation.
    It opens only through a fresh explicit owner-present CALL.
  must_decide:
    Visual information hierarchy across open gas, growing Sphere, closed
    cargo and near-loss-of-control sequence.
  must_not_decide:
    Final roster, renderer, controls, reactions, damage or implementation.
  parent_locks:
    c-002; c-003; universal Sphere; gas movement; volume as strength;
    shell as general endurance; no old gas image authority.
  expected_answer_shape: visual_plate
  first_owner_question:
    In one otherwise identical scene, what must change on screen so you can
    tell which physical obligation the gas creates?
  return_to_graph_if:
    A candidate depends on an undefined gas law, character foundation
    or visual-contract rule.

### D0 — Investigation pressure sources

plain_question:
  What can honestly change the world and force the team to act before it
  finishes investigating and consciously chooses its first valuable target?
why_it_matters:
  c-001 explicitly permits forced improvisation but leaves the source,
  cadence and rules of that pressure open.
answer_shape: scenario_grammar
status: ready
standing: ready_design
dependency_type: downstream
depends_on:
  - c-001
dependency_reason:
  The conscious transition rule is canon; the pressure families can now be
  designed on paper without waiting for implementation.
blocks:
  - investigation escalation grammar
  - some bounded bad-state questions
  - early-floor pacing design
do_not_solve_here:
  - universal timer
  - exact damage
  - death
  - reactions
  - implementation
  - tuning
needs_anchor: verbal_scene
confusion_traps:
  - random unavoidable accident
  - scripted scare
  - hidden timer
  - pressure that makes investigation meaningless
forge_handoff:
  plain_question:
    What readable world changes can take the choice away without cheating?
  why_now:
    c-001 leaves this exact dimension open.
  must_decide:
    Bounded pressure families, attribution and player response window.
  must_not_decide:
    Damage, full failure model, numbers or implementation.
  parent_locks:
    Investigation begins dangerous; conscious operation starts when a
    target is worth it; the world may force improvisation first.
  expected_answer_shape: scenario_grammar
  first_owner_question:
    What should players notice changing before they realise that the quiet
    investigation phase is over?
  return_to_graph_if:
    The answer requires a full damage, reaction or floor-generation system.

### F0 — Current floor-board read

plain_question:
  What must the crew understand about one floor or cluster to form a simple
  working plan, and what honestly remains unknown until contact with the
  world?
why_it_matters:
  Historical work found a potentially useful place/environment/condition/
  intel structure, but it has no current canon authority.
answer_shape: scenario_grammar
status: ready
standing: historical_re_admission_required
dependency_type: co_frame
depends_on:
  - Minimum Game Frame v2
  - c-001
  - accepted Sphere Frame
dependency_reason:
  The current Frame supplies incomplete-but-not-false investigation and a
  physical extraction objective. No implementation prerequisite exists.
blocks:
  - F1 current floor loop
  - floor opportunity grammar
  - floor-intel design
  - environment/condition composition
do_not_solve_here:
  - exact room taxonomy
  - exact condition roster
  - scanner UI
  - procedural generation
  - reactions
  - implementation
needs_anchor: diagram
confusion_traps:
  - silently importing old Simple Floor Read
  - numeric affix sheet
  - scanner solves the floor
  - full blindness
  - heavy planning phase
forge_handoff:
  plain_question:
    What simple information makes one floor an understandable situation
    rather than an abstract room list?
  why_now:
    It is a ready alternative after current Frame reconciliation, but not
    the owner-selected next route.
  must_decide:
    Current board/read grammar and exact treatment of historical findings.
  must_not_decide:
    Exact UI, room generator, condition roster or full loop.
  parent_locks:
    Information is incomplete but not deliberately false; meaningful gas
    target and route decisions matter.
  expected_answer_shape: scenario_grammar
  first_owner_question:
    What should the crew be able to say about the floor in one sentence
    before it enters?
  return_to_graph_if:
    Historical terminology cannot be translated into the current Sphere and
    c-002 design.

### F1 — Current floor loop

plain_question:
  What does the team repeatedly do inside one floor until it goes deeper,
  attempts safe return, retreats, abandons value or fails?
why_it_matters:
  A whole-game Frame exists, but the exact current local work loop is not
  admitted.
answer_shape: loop_spine
status: blocked
standing: historical_re_admission_required
dependency_type: hard_prerequisite
depends_on:
  - F0
  - accepted Sphere Frame
  - c-002
dependency_reason:
  The loop needs a current board/read substrate. Historical Simple Gas Work
  Loop wording cannot be imported directly.
blocks:
  - recurring gas-work problem set
  - some tool-role questions
  - bounded return-liability design
  - representative co-op scenarios
do_not_solve_here:
  - exact controls
  - tool catalogue
  - full economy
  - damage model
  - implementation
needs_anchor: diagram
confusion_traps:
  - one-loot floor
  - room-clear loop
  - vacuum-cleaner harvesting
  - vague verbs without changed stake
  - old floor-loop treated as already canon
forge_handoff:
  plain_question:
    Which repeated sequence turns floor information, gas work and return
    pressure into one understandable local game?
  why_now:
    After F0.
  must_decide:
    Repeated local causal spine and macrocycle handoffs.
  must_not_decide:
    Controls, full tools, economy, damage or implementation.
  parent_locks:
    Gas is regular value; chosen volume matters; world and return route can
    change; safe return banks value.
  expected_answer_shape: loop_spine
  first_owner_question:
    After the crew starts working one gas opportunity, what makes it choose
    another action instead of simply finishing and leaving?
  return_to_graph_if:
    The loop requires an undefined board, value or failure premise.

### F2 — First bounded recoverable bad state

plain_question:
  What first concrete loss-of-control state changes the world but still
  leaves the crew a meaningful response?
why_it_matters:
  General continuing-world failure is preserved, but exact failure,
  recovery, rupture and damage remain too broad.
answer_shape: scenario_grammar
status: blocked
standing: open_design
dependency_type: downstream
depends_on:
  - c-002
  - one concrete selected scene from V1, D0 or F1
dependency_reason:
  A useful bad-state question needs a named behavior, action and location.
  It does not need implementation, but it does need a bounded paper scene.
blocks:
  - recovery grammar
  - later damage-route readiness
  - specific failure visual plates
do_not_solve_here:
  - health
  - death
  - revive
  - full reaction table
  - numerical rupture threshold
  - Sc-damage release
  - implementation
needs_anchor: verbal_scene
confusion_traps:
  - every failure is rupture
  - gas-type shell damage
  - random disaster
  - lost value as the only consequence
forge_handoff:
  plain_question:
    What changed in the world, and what can the crew still do?
  why_now:
    After one bounded scene exists.
  must_decide:
    Attribution, continuing state and recovery opportunity.
  must_not_decide:
    Full damage, health, death, reaction or implementation systems.
  parent_locks:
    Failure changes the world; gas type alone does not rupture the Sphere.
  expected_answer_shape: scenario_grammar
  first_owner_question:
    What physical mistake should create a problem that is bad but still
    playable?
  return_to_graph_if:
    The answer depends on a reaction law, damage model or numerical
    threshold.

### E0 — Safe-return conversion

plain_question:
  Where does safely returned physical gas become durable run power, and
  which meaningful distinctions survive that conversion?
why_it_matters:
  It connects regular gas extraction to preparation and progression.
answer_shape: economy_model
status: ready
standing: ready_design
dependency_type: economy_downstream
depends_on:
  - safe-return boundary from Minimum Game Frame v2
  - accepted physical-return Sphere direction
dependency_reason:
  The current Frames already define a safely returned physical result.
  No implementation or gas-roster prerequisite is required for the bounded
  conversion question.
blocks:
  - T0 predictable tool roles
  - R0 complete run spine
  - later economy questions
do_not_solve_here:
  - prices
  - currency name
  - full progression
  - balance
  - exact shop
  - implementation
needs_anchor: diagram
confusion_traps:
  - physical gas becomes generic token too early
  - one gas becomes dominant grind currency
  - full economy before conversion boundary
forge_handoff:
  plain_question:
    After safe return, what exactly does the run keep?
  why_now:
    It is genuinely ready but not owner-selected as next.
  must_decide:
    Conversion boundary and retained distinctions.
  must_not_decide:
    Prices, full shop, progression numbers or balance.
  parent_locks:
    Only safe return banks value; returned gas supports preparation and
    run power.
  expected_answer_shape: economy_model
  first_owner_question:
    What remains meaningful about the returned gas besides one total amount?
  return_to_graph_if:
    The question requires the full run structure or a final gas roster.

### T0 — Predictable tool roles

plain_question:
  Which small set of predictable capabilities helps the crew handle
  recurring gas problems without automating or cancelling the interesting
  decision?
why_it_matters:
  Tools should answer known problems rather than define gameplay through a
  premature catalogue.
answer_shape: equipment_model
status: downstream
standing: open_design
dependency_type: downstream
depends_on:
  - c-002
  - E0
  - recurring problem set from F1 or D0
dependency_reason:
  c-002 supplies movement obligations, but tools also need a preparation
  route and recurring situations.
blocks:
  - tool feature questions
  - preparation grammar
  - part of R0
do_not_solve_here:
  - full catalogue
  - prices
  - permanent classes
  - exact input
  - implementation
needs_anchor: verbal_scene
confusion_traps:
  - universal gadget
  - tool list before problem
  - maintenance procedure as gameplay
  - tool role becomes class
forge_handoff:
  plain_question:
    Which recurring problem should become more controllable without
    disappearing?
  why_now:
    After E0 and at least one recurring problem source.
  must_decide:
    Minimal tool roles and trade-offs.
  must_not_decide:
    Full catalogue, prices, upgrades, controls or implementation.
  parent_locks:
    Tools are predictable; base play remains simple; movement jobs remain
    meaningful.
  expected_answer_shape: equipment_model
  first_owner_question:
    What problem should a prepared crew handle better but never completely
    delete?
  return_to_graph_if:
    A proposed tool cancels the gas decision or requires an undefined
    economy.

### A0 — Artifact emergence

plain_question:
  What readable physical situation gives the crew an exceptional artifact
  opportunity rather than an ordinary guaranteed reward?
why_it_matters:
  Artifacts are accepted as rare run-shaping exceptions, but their origin
  remains open.
answer_shape: scenario_grammar
status: downstream
standing: open_design
dependency_type: downstream
depends_on:
  - F0
  - V1
dependency_reason:
  Artifact emergence needs a current readable board and visual/physical
  causality. It does not need implementation.
blocks:
  - artifact feature questions
  - artifact role in R0
do_not_solve_here:
  - complete catalogue
  - frequency
  - tiers
  - persistence
  - named artifacts
  - implementation
needs_anchor: visual_plate
confusion_traps:
  - random chest
  - old gas-plus-condition example treated as law
  - hidden recipe
  - artifact on every floor
forge_handoff:
  plain_question:
    What does the crew see and do before an artifact opportunity exists?
  why_now:
    After current floor read and visual causality.
  must_decide:
    One emergence grammar or explicit rejection of a physical-emergence
    route.
  must_not_decide:
    Catalogue, rates, persistence, balance or implementation.
  parent_locks:
    Artifacts are rare, desirable and run-shaping; exact origin is open.
  expected_answer_shape: scenario_grammar
  first_owner_question:
    Which visible world change should make the crew realise that an
    exceptional opportunity has appeared?
  return_to_graph_if:
    The answer requires a full roster or run structure.

### R0 — Complete finite-run spine

plain_question:
  How do safe return, preparation, repeated expeditions, artifacts, depth,
  end-state and full wipe form one short finite run?
why_it_matters:
  The whole-game Frame defines direction but not the exact causal sequence.
answer_shape: loop_spine
status: downstream
standing: open_design
dependency_type: downstream
depends_on:
  - E0
  - A0
dependency_reason:
  Regular returned value and exceptional artifact value need selected roles
  before the complete run can be specified.
blocks:
  - staging/depth structure
  - reset and persistence questions
  - I0 continuity
do_not_solve_here:
  - exact prices
  - exact floor count
  - final content volume
  - implementation
needs_anchor: diagram
confusion_traps:
  - endless progression
  - metagame replaces weak field play
  - artifacts replace regular gas
  - premature campaign architecture
forge_handoff:
  plain_question:
    What repeated causal sequence gives the run a real beginning, escalation
    and end?
  why_now:
    After E0 and A0.
  must_decide:
    Whole-run causal spine.
  must_not_decide:
    Final tuning, content volume or technical save architecture.
  parent_locks:
    Run is short, difficult and finite; full wipe ends it; restart returns
    quickly to meaningful decisions.
  expected_answer_shape: loop_spine
  first_owner_question:
    What new decision becomes available after the first successful return?
  return_to_graph_if:
    Conversion or artifact role is still undefined.

### C0 — Paper design of 4–8-player cooperation

plain_question:
  Which simultaneous responsibilities and coupled decisions make four to
  eight players meaningfully different from several people performing the
  same solo task faster?
why_it_matters:
  Co-op-first must be designed explicitly on paper even though actual
  player behavior remains unverified.
answer_shape: scenario_grammar
status: ready
standing: ready_design
dependency_type: downstream
depends_on:
  - mandatory 4–8-player owner requirement
  - accepted Sphere Frame
  - c-002
dependency_reason:
  Enough physical structure exists to design temporary responsibilities,
  parallel work and reunion pressure without waiting for a greybox.
blocks:
  - detailed co-op scenario grammar
  - lower-bound hypotheses
  - C1 evidence criteria
do_not_solve_here:
  - permanent classes
  - fixed N-player gates
  - exact player-count balance
  - networking
  - implementation
needs_anchor: verbal_scene
confusion_traps:
  - faster together counted as enough
  - every Sphere requires a crowd
  - role menu
  - proof status used to avoid paper design
forge_handoff:
  plain_question:
    What can additional players do simultaneously that changes the team's
    decision rather than only its speed?
  why_now:
    It is genuinely ready but not selected as the next route.
  must_decide:
    Paper grammar of temporary responsibilities, split/reunion pressure and
    coupled decisions across 4–8 players.
  must_not_decide:
    Final balance, networking, implementation or claim of proven fun.
  parent_locks:
    Eight-player support is mandatory; solo is not current target; roles
    arise from hands and situation; no mandatory eligibility gate.
  expected_answer_shape: scenario_grammar
  first_owner_question:
    What important situation should four players handle differently from
    eight?
  return_to_graph_if:
    The paper grammar requires an undefined floor loop or failure model.

### C1 — Actual co-op and readability evidence

plain_question:
  Do real players actually read the situation, communicate, divide
  responsibility and gain new coupled decisions from the designed systems?
why_it_matters:
  Paper and images can specify the intended experience but cannot establish
  observed player behavior.
answer_shape: proof
status: proof_later
standing: proof_nonblocking
dependency_type: proof_downstream
depends_on:
  - V1
  - F1
  - C0
  - representative playable scenario
dependency_reason:
  Actual behavioral evidence requires a playable situation, but this
  dependency does not block any upstream paper-design question.
blocks:
  - empirical claims of fun
  - empirical claims of runtime readability
  - empirical claims of actual additional 4–8-player value
do_not_solve_here:
  - new mechanics added only to pass a test
  - paper substitute for observation
  - implementation architecture
needs_anchor: greybox
confusion_traps:
  - proof_later treated as design_later
  - confidence treated as evidence
  - throughput treated as cooperation
forge_handoff:
  plain_question:
    No current paper Forge handoff.
  why_now:
    Only when a representative playable situation exists.
  must_decide:
    Evidence criteria and observed verdict.
  must_not_decide:
    Upstream design by postponement.
  parent_locks:
    Paper design should already be complete enough to state falsifiable
    intended behavior.
  expected_answer_shape: proof
  first_owner_question:
    What did additional players actually decide or coordinate that fewer
    players could not reproduce?
  return_to_graph_if:
    Evidence exposes a missing design prerequisite.

### I0 — Attendance and run continuity

plain_question:
  What run state belongs to the continuing group when yesterday's eight
  players become today's five?
why_it_matters:
  Changing attendance is part of the player promise and needs a coherent
  paper state model before technical implementation.
answer_shape: payload_model
status: downstream
standing: implementation_downstream
dependency_type: implementation_downstream
depends_on:
  - R0
dependency_reason:
  The run state must first be defined. Its paper ownership rules can then be
  designed before exact storage/network architecture.
blocks:
  - save ownership design
  - roster-change transitions
  - later continuity implementation
do_not_solve_here:
  - networking architecture
  - host migration
  - storage format
  - late join if excluded elsewhere
needs_anchor: diagram
confusion_traps:
  - technical storage choice becomes game law
  - implementation dependency blocks paper state design
  - continuity confused with co-op value
forge_handoff:
  plain_question:
    What exactly do today's five inherit from yesterday's eight?
  why_now:
    After R0 defines the run state.
  must_decide:
    Paper ownership and permitted state transitions.
  must_not_decide:
    Detailed network or storage architecture.
  parent_locks:
    A changing 4–8-player group may continue the same run.
  expected_answer_shape: payload_model
  first_owner_question:
    Which parts of the run belong to the group rather than individual
    attendees?
  return_to_graph_if:
    The complete run state is still undefined.

## 6. Superseded, invalid and parked routes

1. Former separate Frame-v2 preface:
   superseded. Current Frames provide enough basis for bounded questions.

2. Broad extraction and custody questions:
   settled at non-canon Frame altitude; exact design children remain open.

3. Gas-specific Sphere eligibility or gas-type shell damage:
   parked behind future evidence and not a current design requirement.

4. Old gas visual:
   invalid. It provides no style, silhouette, material, motion or VFX lock.

5. Old q-visual-style and StyleBible:
   historical reference only. Their internal `frozen` labels do not create
   current authority under the current INDEX and owner instruction.

6. Old exact ring-fill Bubble:
   superseded by accepted active near-gas Sphere capture.

7. Old gas roster, radiation, reaction, damage and state-window examples:
   examples only or conflicting historical material. No current authority.

8. Exact controls, UI, camera, VFX and visual implementation:
   not current questions, but they may be designed later on paper after
   their parent design/visual questions. They do not need to wait for
   product implementation.

## 7. Historical floor/core reconciliation

| Finding | Current disposition |
|---|---|
| Real but incomplete floor read | Compatible background; exact law remains open |
| Shown condition exists; details uncertain | Compatible background and future floor-intel material |
| Progressive field understanding | Current open read/loop material |
| Place + environment + active conditions + intel | New bounded paper/admission route required |
| Active condition as world cause, not numeric affix | Compatible direction; new admission required |
| Repeated gas/value work | Broadly preserved by current Frame |
| Greed / return / deeper decisions | Broadly preserved by current Frame |
| Exact Simple Gas Work Loop | Historical only; new admission route required |
| Temporary co-op roles | Current open paper-design material |
| Actual anti-solo / 4–8 value | Playable evidence later; does not block paper design |
| Local return liability | Current open pressure/failure material |
| Base prepares; field creates stake | Downstream economy/progression material |
| Raw volume never valuable | Conflicting if absolute; exact value formula remains open |
| Bubble/Sphere as central cargo anchor | Preserved by current Frame |
| Exact old ring placement | Superseded |
| Named gas examples / radiation / damage palette | Examples without authority |
| Old environment visual material | Revisable historical reference |
| Old gas visualization | Invalid |
| Minimal low-cost visual direction | Owner constraint/preference, not canon |

## 8. Stale prose outside this map

### TREE.md

Current g-d3a8 detail still states:

- c-001 is the current card;
- an older eight-player consistency repair is READY FIRST;
- an older abstract co-op research route is READY PARALLEL.

These lines are stale routing prose after c-002 and this cartography.

This map does not edit TREE.

Any TREE correction requires a separate exact G9 artifact shown to and
approved by the owner.

### Old visual files

q-visual-style and StyleBible retain old internal frozen labels.

Current INDEX and current owner instruction make them historical/open
material only.

This map does not rewrite those files.

### CORE.md

CORE preserves important owner direction:

- Sphere/Bubble centrality;
- gas behavior affects cargo;
- simple physical action;
- gas remains the visible star.

Exact old ring-fill, named gas examples and damage palette are not current
canon and must be read through current Frames and c-002.

## 9. Current owner-selected route

Exactly one current canon-track root after this reconciliation
transaction:

V1 &mdash; visual readability of Counter / Brake / Time across open gas,
growing Sphere, closed cargo and near-loss-of-control sequence.

The fresh V1 CALL uses the owner-selected simple route:

- one graph, not a second visual Forge;
- one Canon Forge, not a parallel visual authority;
- answer format follows the question;
- c-003 permits controlled visual research in a visual question;
- owner selection, canon admission and evidence remain distinct.

V0 is resolved as the minimal operating contract for visual work. It did
not select a final look, roster, reactions, damage, controls, renderer,
production assets or empirical claims.

<!-- Superseded pre-reconciliation route (non-authoritative historical
     record):
Exactly one current canon-track root:

V0 — minimal visual-development contract.

Why now:

- owner explicitly approved visual-by-default paper work;
- existing visual authority has been reset;
- old gas visual is invalid;
- future images need controlled status and intentional-lock rules;
- current Canon Forge remains text-only and cannot silently generate
  authoritative plates.

The contract question does not decide the look of the game.

After V0, the intended first substantive visual question is:

V1 — visual readability of Counter / Brake / Time across open gas,
growing Sphere, closed cargo and near-loss-of-control sequence.

-->

Other genuinely ready but not selected questions:

- D0 investigation pressure sources;
- F0 current floor-board read;
- E0 safe-return conversion;
- C0 paper design of 4–8-player cooperation.

None is opened automatically.

## 10. Gap rule

Return to cartography rather than inventing a substitute when Forge finds:

- an image-authority rule that cannot be stated independently of exact art;
- a visual question that silently fixes gas roster, reactions or damage;
- dependence on invalid old gas imagery;
- a hidden prerequisite in character, camera, environment or Sphere design;
- a wrong answer shape;
- an undefined entity;
- a contradiction with current Frames, c-002 or c-003;
- a process conflict with one graph / one Forge / answer-format-follows-
  question route;
- owner judgment that the session is solving the wrong question.

END_OF_FILE: live/indie-game-development/work/canon-maps/g-d3a8-current-question-front-v3.md
