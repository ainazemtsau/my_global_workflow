RESULT s-cartography-g-d3a8-current-question-front-001 (call: c-cartography-g-d3a8-current-question-front-001)
direction: indie-game-development
play: local/canon-cartography
node/task: g-d3a8 / current design-question front

outcome: |
  Существует owner-approved актуальная карта текущего design-question front
  для g-d3a8.

  Карта заменяет ошибочный ready-маршрут на абстрактный вопрос о разделении
  4–8 игроков следующим порядком:

  P0 — bounded Frame-v2 preface:
  - безопасно возвращённые разные газы дают общую устойчивую покупательную
    ценность для предсказуемых инструментов;
  - артефактная система обязательно существует и принципиально связана с
    газом и физическими условиями карты;
  - точные конвертация, валюта, цены, условия, частота, каталог и реализация
    остаются OPEN.

  Q1 — Simple Gas Extraction:
  - минимальное и очевидное действие добычи газа в растущий Пузырь;
  - видимое изменение газа и Пузыря во время забора;
  - решение игрока «где начать / сколько взять / когда остановиться»;
  - без преждевременного решения точной переноски, числа участников,
    scaling, полного roster, damage, экономики или implementation.

  Simple Suction Bubble зарегистрирован как owner-origin paper candidate:
  базовую добычу способен выполнить один игрок; Пузырь засасывает газ и
  растёт; игрок останавливает забор на выбранном объёме. Это не выбранный
  ответ, не Frame authority и не канон.

  Старые question-документы, старые карты и прежние frozen-ответы имеют
  статус historical evidence only. Они могут поставлять аргументы,
  гипотезы, vocabulary и failure evidence, но не ограничивают новый ответ
  и не получают current-canon authority автоматически.

  Отдельный co-op composition вопрос удалён из ready front. Кооператив
  остаётся общим design constraint при сравнении механик, а доказательство
  дополнительной ценности 4–8 игроков получает статус proof_later после
  появления конкретной sandbox-механики и representative greybox.

  Ни одного design-answer или OWNER-SELECTED PAPER ANSWER эта cartography
  не создаёт. Frame v2, TREE, CHARTER, canon, Sc-damage, product и
  implementation остаются неизменными.

evidence: |
  1. Финальный owner sign, дословно:

     «ПОПРАВКУ КАРТЫ УТВЕРЖДАЮ: старые question-документы
     используются только как historical evidence и не ограничивают
     новый ответ. Главный Q1 — Simple Gas Extraction: минимальное
     действие добычи газа в растущий Пузырь, видимое изменение во
     время забора и решение “сколько взять / когда остановиться”.
     Simple Suction Bubble с базовой добычей одним игроком —
     owner-origin кандидат, не выбранный ответ. Точные переноска,
     число людей и scaling — downstream. Маршрут P0 → Q1
     сохраняется.»

  2. Предшествующий owner sign карты, дословно:

     «КАРТУ УТВЕРЖДАЮ С ПРАВКОЙ: главный ready-вопрос —
     Interesting Gas Work Loop; добыча и доставка рассматриваются
     одной причинной связкой. Старый вопрос о наполнении Bubble
     становится частью этого вопроса. Точные газы используются
     только как неканонические test probes. Следующий маршрут:
     P0 → Q1.»

     Финальный verdict выше уточняет и supersedes слишком широкий
     Interesting Gas Work Loop: текущий Q1 ограничен самой добычей,
     а точная доставка вынесена downstream.

  3. Owner source для приоритета Q1 в этой сессии:
     - «главный риск – это то, что как мы интересно сделаем вот эту
       добычу, доставку газов»;
     - «мне больше сейчас пробел именно ... в том, как будет
       добываться»;
     - действие должно быть «явно и очевидно» и не должно становиться
       сложной процедурой.

  4. Owner source для authority старых документов:
     - «актуальные данные это canon forge v3»;
     - «старые документы, старый подход это не канон»;
     - старые материалы можно использовать как historical data, но
       новый свежий канон должен проходить действующий v3 route.

  5. Current authority:
     - live/indie-game-development/work/minimum-game-frame-v2.md
       SHA 680b93582249336d4ac31629574bed15bc5f2bed:
       FRAME READY, not canon; Bubble is the principal extraction
       DESIGN ANCHOR, while filling, control, capacity, stages and
       helpers remain OPEN.
     - gas_coop_game_canon/CORE.md
       SHA c2fe9c3dc156b91d1f684d490e04d9ea4c85f1b2:
       Bubble remains accepted concept direction; exact gas-to-Bubble
       action is explicitly still to be discussed.
     - gas_coop_game_canon/INDEX.md
       SHA f1e793c8a9ef94e47f8dd65f211c21a6cbcba47b:
       current card canon contains only c-001; old questions/maps are
       historical evidence.
     - live/indie-game-development/plays/canon-cartography.md
       SHA d6aec4d4627c66208164c42f0b6894671223a4d3:
       cartography owns question dependencies, readiness, routing and
       owner sign, but does not answer or freeze canon.
     - live/indie-game-development/NOW.md
       observed SHA 8a427aa65841fe77fd3f95fb03b97a5e4c775d4e:
       the stale ready route still names
       c-research-q-coop-interdependence-002 and therefore requires the
       bounded routing replacement below.

  6. Done-when coverage:
     - owner-readable bounded map: exact artifact below;
     - no more than 12 nodes: P0 + Q1–Q11;
     - each node carries source, plain question, why, answer shape,
       status, dependency, blocks, non-scope, anchor, confusion traps
       and forge handoff;
     - ready front is exactly P0 → Q1;
     - co-op composition has explicit proof_later disposition;
     - artifacts and common-value economy remain explicit;
     - owner approved the final corrected map verbatim;
     - no design answer or canon mutation occurred.

state_changes: |
  1. Add the current owner-approved question-map artifact.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/work/canon-maps/
       g-d3a8-current-question-front-v1.md

     postcondition:
       Create the file with exactly the following content and one
       END_OF_FILE marker.

     artifact_content: |
       # g-d3a8 — Current Design Question Front v1

       status: OWNER-APPROVED CARTOGRAPHY
       approved_on: 2026-07-16
       authority: routing and dependency map only; not Frame, not a paper answer, not canon
       governing_process: Canon Forge v3
       owner_verdict: |
         «ПОПРАВКУ КАРТЫ УТВЕРЖДАЮ: старые question-документы
         используются только как historical evidence и не ограничивают
         новый ответ. Главный Q1 — Simple Gas Extraction: минимальное
         действие добычи газа в растущий Пузырь, видимое изменение во
         время забора и решение “сколько взять / когда остановиться”.
         Simple Suction Bubble с базовой добычей одним игроком —
         owner-origin кандидат, не выбранный ответ. Точные переноска,
         число людей и scaling — downstream. Маршрут P0 → Q1
         сохраняется.»

       ## 1. Authority and status

       Current authority order for this map:

       1. Current owner words.
       2. Direction OS and Canon Forge v3.
       3. Minimum Game Frame v2 — current owner-approved whole-game
          design basis, not canon.
       4. Current canon entrypoints and INDEX-listed cards.
       5. Historical questions, maps, frozen answers, research and old
          process material — evidence only.

       Old `questions/*.md`, prior question maps and earlier frozen
       answers do not constrain a new Canon Forge v3 paper answer.
       A useful old statement may re-enter only through a current sourced
       question, owner-selected paper answer and separate canon admission.

       This map answers no gameplay question.

       ## 2. Cluster diagnosis

       The previous ready route asked how 4–8 players should divide into
       temporary subgroups and roles before the concrete sandbox actions
       were defined.

       That route was premature:

       - it named no waiting implementation that required role composition;
       - its answer depended on still-open gas, extraction, cargo, route,
         tool and consequence mechanics;
       - it risked producing generic roles rather than a player-facing
         mechanic;
       - actual co-op value cannot be established before representative
         mechanics and later playable evidence.

       Current priority is the central concrete gap identified by the owner:

       > How does a player actually extract gas into a growing Bubble, and
       > why is the act of extraction more than holding a button and waiting?

       ## 3. Protected owner directions pending P0

       These are owner locks for the next Gate F discussion. They are not
       silently written into Frame v2 by this cartography.

       ### OL-1 — common returned-gas value

       Safely returned gas of different types feeds a common durable
       purchasing value through which the crew obtains predictable tools.

       OPEN:
       - exact conversion operation;
       - name and representation of value/currency;
       - exchange rates, prices and demand;
       - whether any gas retains exceptional non-fungible uses;
       - pressure-loop, quotas and balance.

       ### OL-2 — artifact line

       Artifacts necessarily exist as a game category and are connected to
       gas interacting with physical map conditions, objects or spatial
       states.

       OPEN:
       - exact generation grammar;
       - whether results are found, created, triggered or transformed;
       - required player action;
       - frequency, tiers, guarantees and catalogue;
       - persistence, ownership, loss and wipe exceptions.

       ## 4. Owner-origin Q1 candidate

       ### Simple Suction Bubble

       Candidate status: OWNER-ORIGIN INPUT ONLY.

       Baseline:
       - one player can perform basic extraction;
       - the player activates a Bubble near physical gas;
       - gas is visibly drawn into it;
       - the Bubble grows with the captured amount;
       - the player chooses when to stop;
       - a small Bubble remains individually manageable;
       - a larger voluntarily chosen Bubble may later require additional
         people to handle or transport.

       Not selected:
       - exact suction geometry;
       - pressure law;
       - control scheme;
       - number of carriers;
       - size/value scaling;
       - final carry behavior.

       ## 5. Dependency graph

       P0 → Q1

       Q1 → Q2
       Q1 → Q4
       Q1 → Q6

       Q2 → Q3
       Q2 → Q8

       Q3 → Q7
       Q3 → Q8

       Q4 → Q5

       Q6 → Q7
       Q6 → Q9

       Q8 → Q9

       Q1 + Q2 + Q3 + Q4 + Q5 → Q10 proof later

       Q9 → Q11 implementation downstream

       ## 6. Nodes

       ### P0 — Frame-v2 alignment preface

       source:
         Current owner directions OL-1 and OL-2 versus Frame-v2 sections
         3–4, where conversion remains OPEN and artifact origin remains an
         ARCHITECTURE HYPOTHESIS.
       plain_question:
         What exact minimal Frame-v2 wording preserves common returned-gas
         value and the mandatory artifact line without deciding their
         implementation?
       why_it_matters:
         Without this preface the new map can again lose or demote two
         owner-required systems.
       answer_shape: invariant
       status: needs_preface
       dependency_type: hard_prerequisite
       blocks:
         - Q1 current sourced route
         - all downstream questions that use economy or artifacts
       do_not_solve_here:
         - currency name
         - rates, prices, quotas or balance
         - exact artifact recipes, nodes or catalogue
         - canon admission
       needs_anchor: none
       confusion_traps:
         - importing the old seven-law research package wholesale
         - treating a map approval as an automatic Frame edit
         - promoting exact conversion or artifact origin details
       forge_handoff:
         plain_question:
           Do these two minimal owner directions make the current frame
           complete enough to proceed to Simple Gas Extraction?
         why_now:
           The owner explicitly says both systems will exist, while current
           Frame classification remains weaker.
         must_decide:
           Exact bounded Frame wording and FRAME READY / REVISED / BLOCKED.
         must_not_decide:
           Economy model, artifact mechanics, catalogue or canon.
         parent_locks:
           Gas is regular expedition value; safe return is the banking
           boundary; predictable tools and exceptional artifacts have
           different jobs.
         expected_answer_shape: invariant
         first_owner_question:
           Do these two short statements capture only what is guaranteed,
           while leaving the form open?
         return_to_graph_if:
           Either owner lock is disputed, requires a macro redesign or
           cannot be stated without choosing its detailed mechanic.

       ### Q1 — Simple Gas Extraction

       source:
         Frame-v2 Bubble extraction DESIGN ANCHOR; CORE owner direction;
         the owner's current priority and Simple Suction Bubble candidate.
       plain_question:
         When a player activates the Bubble near physical gas, what minimal
         obvious action transfers a chosen amount into a growing Bubble,
         what visibly changes during extraction, and what makes
         “where / how much / when to stop” a real decision?
       why_it_matters:
         This is the missing central player-facing action. Without it,
         gas types, carry, tools, artifacts and economy decorate an
         undefined extraction routine.
       answer_shape: scenario_grammar
       status: ready
       dependency_type: hard_prerequisite
       dependencies:
         - P0 must leave Gate F at FRAME READY
       blocks:
         - Q2 field readability
         - Q3 gas behavior jobs
         - Q4 Bubble custody and delivery
         - Q5 release and recovery
         - first representative extraction feature and greybox
       do_not_solve_here:
         - full delivery loop
         - exact carry controls
         - number of helpers
         - size/value formula or player-count scaling
         - full gas roster
         - final tools, UI, damage, networking or implementation
         - exact economy or artifacts
       needs_anchor: verbal_scene
       confusion_traps:
         - hold-to-fill with no changing decision
         - complexity rewarded merely for being unusual
         - fixing production controls or final tool art
         - treating the owner-origin candidate as already selected
         - forcing co-op into the basic action
       forge_handoff:
         plain_question:
           What exactly does the player do and see while a selected part of
           field gas becomes a growing Bubble?
         why_now:
           The owner names extraction as the largest missing concept and
           near-term feature-facing risk.
         must_decide:
           Start/stop action, extraction relation to field gas, visible
           change, chosen amount and one minimal source of changing judgment.
         must_not_decide:
           Full carry, exact carriers, scaling, roster, economy, damage,
           implementation or canon.
         parent_locks:
           Bubble remains the principal extraction anchor; base action must
           be obvious and simple; physical gas cannot become a generic
           pickup; paper does not certify fun.
         expected_answer_shape: scenario_grammar
         first_owner_question:
           In one room, what does the player press or do, what visibly moves
           or grows, and why might the player stop before taking everything?
         return_to_graph_if:
           The answer requires a full gas roster, exact delivery mechanics,
           a new engine subsystem or a disputed Frame premise.

       ### Q2 — Field readability and active conditions

       source:
         Frame-v2 local loop and OPEN signals/detectors; OL-2 artifact line.
       plain_question:
         What can players honestly perceive about the gas and relevant
         physical conditions before and during extraction?
       why_it_matters:
         Extraction choices and later artifact situations are unfair or
         arbitrary without readable physical causes.
       answer_shape: visual_plate
       status: downstream
       dependency_type: co_frame
       dependencies:
         - Q1 extraction grammar
       blocks:
         - Q3 gas jobs
         - Q8 artifact emergence
         - runtime readability criteria
       do_not_solve_here:
         - final VFX
         - complete scanner or UI
         - gas names or roster
       needs_anchor: visual_plate
       confusion_traps:
         - HUD numbers as the only truth
         - invisible unavoidable loss
         - pretending every detail is known at the door
       forge_handoff:
         plain_question:
           Which world signs make an extraction choice informed but not
           fully solved?
         why_now:
           Wake after Q1 identifies what must be read.
         must_decide:
           First-proof read channels and uncertainty boundary.
         must_not_decide:
           Final UI, full investigation system or roster.
         parent_locks:
           Information is incomplete but not false; consequences are
           attributable.
         expected_answer_shape: visual_plate
         first_owner_question:
           What can the player see, hear or measure before committing to
           suction?
         return_to_graph_if:
           A final renderer, complete UI or named gas catalogue is required.

       ### Q3 — Gas behavior jobs

       source:
         g-d3a8 current goal/done_when: each gas must have a gameplay job.
       plain_question:
         Which first behavior jobs are required to make the selected
         extraction grammar produce different decisions?
       why_it_matters:
         Gas types should be designed from gameplay needs rather than from
         names or decorative effects.
       answer_shape: taxonomy
       status: downstream
       dependency_type: downstream
       dependencies:
         - Q1
         - Q2
       blocks:
         - first meaningful gas set
         - Q7 tool roles
         - Q8 artifact grammar
       do_not_solve_here:
         - final roster
         - names, tuning or all reactions
       needs_anchor: verbal_scene
       confusion_traps:
         - cool-gas list before gameplay jobs
         - creature intelligence
         - chemistry table as the game
       forge_handoff:
         plain_question:
           Which distinct jobs must test the chosen extraction mechanic?
         why_now:
           Wake only after extraction says what variation matters.
         must_decide:
           A minimal job taxonomy and noncanonical probes.
         must_not_decide:
           Full catalogue, names, numbers or reaction matrix.
         parent_locks:
           Honest physical gas; each gas creates a decision, route, tool,
           consequence or pressure.
         expected_answer_shape: taxonomy
         first_owner_question:
           Which behavior would make the best extraction choice change?
         return_to_graph_if:
           The discussion becomes name-first or requires full content scope.

       ### Q4 — Bubble custody and delivery

       source:
         Frame-v2 Bubble anchor and OPEN control/capacity/helper dimensions.
       plain_question:
         After extraction ends, what simple physical responsibility makes
         the filled Bubble meaningful cargo rather than a generic item?
       why_it_matters:
         Q1 must hand a real state into delivery, but exact delivery should
         not be chosen before extraction is understood.
       answer_shape: loop_spine
       status: downstream
       dependency_type: downstream
       dependencies:
         - Q1
       blocks:
         - Q5 release/recovery
         - route pressure
         - carry greybox
       do_not_solve_here:
         - exact number of carriers
         - player-count scaling
         - full cargo inventory
         - final controls or balance
       needs_anchor: verbal_scene
       confusion_traps:
         - ordinary slow-walk cargo
         - hard N-body gates selected too early
         - identical work duplicated for co-op
       forge_handoff:
         plain_question:
           What must the player keep doing or account for after the Bubble
           has been filled?
         why_now:
           Wake after Q1 creates a concrete cargo state.
         must_decide:
           Custody obligation and route consequence.
         must_not_decide:
           Exact people count, scaling, controls or tuning.
         parent_locks:
           Bubble behavior depends on contained gas; larger voluntary stake
           may create more need for help.
         expected_answer_shape: loop_spine
         first_owner_question:
           What is different about returning with this Bubble rather than a
           normal crate?
         return_to_graph_if:
           The answer depends on exact player-count balance or full roster.

       ### Q5 — Release, failure and recovery

       source:
         Frame-v2 continuing world-state failure and OPEN damage/recovery.
       plain_question:
         What readable world change occurs when extraction or Bubble custody
         is interrupted, leaked, released or abandoned?
       why_it_matters:
         Failure must create a continuing situation, not only lose points or
         open a punishment screen.
       answer_shape: scenario_grammar
       status: downstream
       dependency_type: downstream
       dependencies:
         - Q1
         - Q4
       blocks:
         - later Sc-damage readiness
         - recovery and retreat grammar
       do_not_solve_here:
         - exact health, death or revive
         - full reaction table
         - Sc-damage release
       needs_anchor: verbal_scene
       confusion_traps:
         - invisible durability loss
         - gas vanishes on failure
         - random unavoidable disaster
       forge_handoff:
         plain_question:
           If extraction or custody goes wrong here, what changed and what
           can the player still do?
         why_now:
           Wake after Q1 and Q4 expose concrete failure sites.
         must_decide:
           Attribution, world consequence and recoverability boundary.
         must_not_decide:
           Exact damage/death/revive or tuning.
         parent_locks:
           Failure changes the world; deliberate release may be valid.
         expected_answer_shape: scenario_grammar
         first_owner_question:
           What is the first recoverable bad state?
         return_to_graph_if:
           The answer requires the unresolved damage model.

       ### Q6 — Common returned-gas conversion

       source:
         OL-1 and Frame-v2 safe-return/value direction.
       plain_question:
         How do safely returned different gases become one common purchasing
         value without making their field differences irrelevant?
       why_it_matters:
         This connects regular extraction to preparation and predictable
         tools while preserving gas-specific field play.
       answer_shape: economy_model
       status: downstream
       dependency_type: economy_downstream
       dependencies:
         - P0
         - Q1
       blocks:
         - Q7 tools
         - Q9 full run loop
       do_not_solve_here:
         - prices, rates, quotas or balance
         - complete progression
         - artifact economy
       needs_anchor: verbal_scene
       confusion_traps:
         - gas becomes a generic token in the field
         - one gas is always the best currency grind
         - economy dictates extraction before Q1
       forge_handoff:
         plain_question:
           Where exactly does physical gas stop being expedition custody and
           become common buying power?
         why_now:
           Wake after Q1 establishes what is safely returned.
         must_decide:
           Conversion boundary and retained distinctions.
         must_not_decide:
           Tuning, full shop or progression numbers.
         parent_locks:
           Safe return banks value; predictable tools use regular gas value.
         expected_answer_shape: economy_model
         first_owner_question:
           What survives conversion besides the common amount?
         return_to_graph_if:
           The model requires prices or full campaign structure.

       ### Q7 — Predictable tool roles

       source:
         Frame-v2 distinction between tools and artifacts.
       plain_question:
         Which minimal tool roles expand the selected gas work without
         automating or cancelling it?
       why_it_matters:
         Tools should provide known functions tied to real player actions,
         not become a catalogue before the loop exists.
       answer_shape: equipment_model
       status: downstream
       dependency_type: downstream
       dependencies:
         - Q3
         - Q6
       blocks:
         - first tool features
         - preparation grammar
       do_not_solve_here:
         - full loadout
         - prices or upgrades
         - production art
       needs_anchor: verbal_scene
       confusion_traps:
         - tool list before verbs
         - universal gadget solves every gas
         - mandatory servicing procedure
       forge_handoff:
         plain_question:
           What known capability does the crew buy because Q1–Q3 create a
           recurring need for it?
         why_now:
           Wake after jobs and common value exist.
         must_decide:
           Tool roles and trade-offs.
         must_not_decide:
           Full catalogue, economy tuning or implementation.
         parent_locks:
           Tools are predictable; base play remains simple.
         expected_answer_shape: equipment_model
         first_owner_question:
           Which recurring problem deserves the first reliable tool?
         return_to_graph_if:
           The tool cancels the interesting gas decision.

       ### Q8 — Artifact emergence grammar

       source:
         OL-2 and Frame-v2 artifact category.
       plain_question:
         How can gas interacting with a physical map condition create an
         artifact opportunity that players can perceive and act on?
       why_it_matters:
         This protects the mandatory artifact line as gameplay rather than
         decorative lore or a generic loot table.
       answer_shape: scenario_grammar
       status: downstream
       dependency_type: downstream
       dependencies:
         - P0
         - Q2
         - Q3
       blocks:
         - artifact feature questions
         - Q9 run-shaping role
       do_not_solve_here:
         - full recipe system
         - catalogue, frequency or tiers
         - specific persistent exceptions
       needs_anchor: verbal_scene
       confusion_traps:
         - chest drop unrelated to gas
         - hidden recipe with no readable cause
         - accepting old research examples as answers
       forge_handoff:
         plain_question:
           What visible physical situation tells players that an artifact
           can emerge here, and what choice do they have?
         why_now:
           Wake when field conditions and gas jobs are defined.
         must_decide:
           One emergence grammar and player decision.
         must_not_decide:
           Catalogue, rates, final recipes or balance.
         parent_locks:
           Artifacts exist, are exceptional, and connect to gas plus map
           conditions.
         expected_answer_shape: scenario_grammar
         first_owner_question:
           What does the crew see before the artifact exists?
         return_to_graph_if:
           The answer requires a complete roster or generic RNG.

       ### Q9 — Complete run loop

       source:
         Frame-v2 short finite run, safe return, full wipe and fast restart.
       plain_question:
         How do common returned-gas value, tools, artifact opportunities,
         depth, wipe and restart form one short finite run?
       why_it_matters:
         This connects field mechanics to the whole game without forcing
         campaign structure prematurely.
       answer_shape: loop_spine
       status: downstream
       dependency_type: downstream
       dependencies:
         - Q6
         - Q8
       blocks:
         - staging/depth structure
         - reset and progression questions
       do_not_solve_here:
         - exact prices or floor count
         - final objective content
         - full metaprogression
       needs_anchor: diagram
       confusion_traps:
         - meta compensates for weak field play
         - endless progression contradicts finite run
         - artifacts replace regular gas work
       forge_handoff:
         plain_question:
           What repeated sequence turns returned gas and occasional
           artifacts into a complete run with a real end?
         why_now:
           Wake only after regular value and artifact grammar exist.
         must_decide:
           Whole-run causal spine.
         must_not_decide:
           Tuning, content volume or implementation.
         parent_locks:
           Short difficult finite run; full wipe; fast meaningful restart.
         expected_answer_shape: loop_spine
         first_owner_question:
           What decision becomes possible after one successful return?
         return_to_graph_if:
           The answer depends on unchosen economy or artifact behavior.

       ### Q10 — 4–8-player value proof

       source:
         Mandatory eight-player owner requirement and Frame-v2 OPEN
         co-op-composition gap.
       plain_question:
         Do the selected sandbox mechanics create additional coupled
         decisions for 4, 6 and 8 players, or only increase throughput?
       why_it_matters:
         The game is co-op-first, but role composition cannot be designed
         meaningfully before concrete mechanics exist.
       answer_shape: proof
       status: proof_later
       dependency_type: proof_downstream
       dependencies:
         - Q1
         - Q2
         - Q3
         - Q4
         - Q5
         - representative greybox
       blocks:
         - later claims of actual 4–8-player value
       do_not_solve_here:
         - current extraction answer
         - permanent classes
         - forced roles
         - exact player-count balance
       needs_anchor: greybox
       confusion_traps:
         - “faster together” treated as sufficient
         - forcing every action to require a team
         - abstract role menu before sandbox
       forge_handoff:
         plain_question:
           What new decisions appear when extra players join the actual
           working sandbox?
         why_now:
           Not current; wake only after representative mechanics exist.
         must_decide:
           Evidence criteria for coupled decisions and self-organization.
         must_not_decide:
           New mechanics merely to pass an abstract co-op test.
         parent_locks:
           4–8 primary range; eight mandatory; solo not current target.
         expected_answer_shape: proof
         first_owner_question:
           What happened with eight that could not happen with four?
         return_to_graph_if:
           The proof exposes a missing mechanic prerequisite.
       current_blocks: none

       ### Q11 — Attendance, save ownership and session continuity

       source:
         Frame-v2 OPEN attendance continuity, join/leave, ownership and
         technical continuation.
       plain_question:
         How does a changing group continue the same run when attendance
         changes?
       why_it_matters:
         It is required for the product promise, but it should not dictate
         the central extraction mechanic prematurely.
       answer_shape: payload_model
       status: downstream
       dependency_type: implementation_downstream
       dependencies:
         - Q9
         - actual session/save implementation constraints
       blocks:
         - later continuity design and implementation
       do_not_solve_here:
         - networking architecture
         - host migration
         - lower-bound balance
       needs_anchor: diagram
       confusion_traps:
         - technical save choice silently becomes game law
         - solving late join while current scope excludes it
         - mixing continuity with Q10 co-op value
       forge_handoff:
         plain_question:
           Which run state belongs to the continuing group when yesterday's
           eight become today's five?
         why_now:
           Wake after whole-run state is defined and implementation needs it.
         must_decide:
           Product-level continuity ownership and permitted transitions.
         must_not_decide:
           Detailed networking architecture.
         parent_locks:
           Changing 4–8 group; same run may continue; exact technical model
           OPEN.
         expected_answer_shape: payload_model
         first_owner_question:
           What exactly must remain true when the roster changes?
         return_to_graph_if:
           The question requires an engineering architecture decision first.

       ## 7. Ready front

       Current ready route:

       1. P0 — owner-present bounded Gate F preface.
       2. Q1 — Simple Gas Extraction.

       No other node is automatically next. After Q1 the map is revisited
       against the concrete answer and actual implementation need.

       ## 8. Gap rule

       Return to this map when Canon Forge finds:

       - a hidden prerequisite;
       - an undefined entity;
       - a wrong answer shape;
       - a need for visual or playable evidence;
       - an answer that requires full roster/economy/delivery;
       - a contradiction with P0 or Frame v2;
       - owner judgment that the session is solving the wrong problem.

       Do not silently switch to another question.

       END_OF_FILE: live/indie-game-development/work/canon-maps/g-d3a8-current-question-front-v1.md

  2. Add the exact next CALL file.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/work/
       c-research-q-simple-gas-extraction-001-call.md

     operation:
       Create the file with exactly the complete CALL carried in `next`
       below, followed by:

       END_OF_FILE: live/indie-game-development/work/c-research-q-simple-gas-extraction-001-call.md

  3. Replace the stale g-d3a8 ready route in NOW.md.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/NOW.md

     observed_base_sha:
       8a427aa65841fe77fd3f95fb03b97a5e4c775d4e

     operations:
       a. Set the header marker to:
          updated: 2026-07-16 by s-cartography-g-d3a8-current-question-front-001

       b. Remove the complete open_calls entry with stable id:
          c-research-q-coop-interdependence-002

       c. Add in the same g-d3a8 parallel-routing position:

          - id: c-research-q-simple-gas-extraction-001
            to: session
            for: g-d3a8 / P0 Frame alignment + Q1 Simple Gas Extraction
            issued: 2026-07-16
            note: |
              READY PARALLEL / OWNER-PRESENT / PAPER-ONLY.
              Owner-approved current question map replaces the premature
              co-op-composition front. Route = P0 bounded Gate F alignment,
              then Q1 Simple Gas Extraction if the frame is READY:
              minimal obvious extraction into a growing Bubble, visible
              field/Bubble change and the choice “where / how much / when
              to stop”. Simple Suction Bubble is owner-origin input only,
              not selected. Old question documents are historical evidence
              only. Exact carry, helper count, scaling, roster, damage,
              economy, artifacts, networking and implementation remain
              outside Q1; co-op composition is proof_later; Sc-damage stays
              HELD. CALL:
              work/c-research-q-simple-gas-extraction-001-call.md.
              Map:
              work/canon-maps/g-d3a8-current-question-front-v1.md.

       d. Preserve unchanged after semantic rebase:
          - current bet and all tasks;
          - direction-level NOW.next;
          - every unrelated open call;
          - decisions and recurring;
          - c-shape-sc-damage-001 as HELD;
          - all engineering, visual, character, level and marketing routes.

  4. Append one LOG line.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/LOG.md

     observed_base_sha:
       24e1e331cd269c3376d870851ca7042e8b377bda

     append_before_end_marker: |
       2026-07-16 — local/canon-cartography close (g-d3a8/c-cartography-g-d3a8-current-question-front-001, s-cartography-g-d3a8-current-question-front-001): owner approved the corrected current question map — old question documents are historical evidence only; P0 preserves common returned-gas value and the mandatory artifact line without fixing their form; Q1 Simple Gas Extraction is the sole ready design question, with Simple Suction Bubble as owner-origin input rather than a selected answer; exact carry/helper count/scaling are downstream, co-op composition is proof_later, the stale co-op CALL is replaced by owner-present P0→Q1 Canon Forge, and Frame/TREE/CHARTER/canon/product/Sc-damage remain unchanged. → history/2026-07-16-s-cartography-g-d3a8-current-question-front-001.md

  5. Save this complete RESULT verbatim.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/history/
       2026-07-16-s-cartography-g-d3a8-current-question-front-001.md

     postcondition:
       File ends with exactly:

       END_OF_FILE: live/indie-game-development/history/2026-07-16-s-cartography-g-d3a8-current-question-front-001.md

  6. Explicit no-change surfaces.

     Do not modify:
       - live/indie-game-development/work/minimum-game-frame-v2.md;
       - live/indie-game-development/TREE.md;
       - live/indie-game-development/CHARTER.md;
       - gas_coop_game_canon/**;
       - product repositories or implementation;
       - damage, Sc-damage disposition, networking or balance;
       - old historical questions, maps, RESULTs or archives;
       - direction-level NOW.next.

captures:
  - |
    Current TREE g-d3a8 detail still contains the old co-op design-lane
    summary. This cartography did not present an exact TREE diff and
    therefore has no G9 authority to change it. A later bounded owner-present
    G9 cleanup may remove that stale detail; runnable authority meanwhile
    comes from NOW plus the current question-map artifact.
  - |
    Process finding: a question becoming unblocked does not make it current,
    high-priority or sufficiently answerable. Gate Q must name a concrete
    downstream need and surviving prerequisites.
  - |
    Old frozen question material under Canon Forge v3 should be treated as
    refutation and discovery evidence, not as invisible constraints on new
    paper answers.

decisions_needed: []

play_check:
  - |
    1 Frame cluster: done — the cluster is the current g-d3a8
    design-question front; cartography was required because the ready
    co-op-composition route lacked concrete priority and prerequisites,
    while central extraction and artifact/economy lines were missing from
    current routing.
  - |
    2 Inventory: done — current Frame v2, TREE, CHARTER, Canon Forge v3,
    current canon entrypoints/c-001, owner eight-player requirement, old
    maps/questions as historical evidence, preserved artifact and
    common-value directions, and owner corrections were classified without
    answering design.
  - |
    3 Plain questions: done — P0 and Q1–Q11 are stated as bounded
    owner-facing questions; Q1 is narrowed to Simple Gas Extraction rather
    than a broad Gas Work Loop.
  - |
    4 Classify graph: done — each node carries source, why, answer shape,
    status, dependency, blocks, non-scope, anchor, confusion traps and
    forge handoff; co-op composition is proof_later.
  - |
    5 Route: done — recommended and accepted route is exactly P0 → Q1;
    full carry, player count/scaling and co-op proof remain downstream,
    while old question documents provide evidence only.
  - |
    6 Owner sign: done — owner approved the final correction verbatim:
    «ПОПРАВКУ КАРТЫ УТВЕРЖДАЮ: старые question-документы используются
    только как historical evidence и не ограничивают новый ответ.
    Главный Q1 — Simple Gas Extraction: минимальное действие добычи газа
    в растущий Пузырь, видимое изменение во время забора и решение
    “сколько взять / когда остановиться”. Simple Suction Bubble с базовой
    добычей одним игроком — owner-origin кандидат, не выбранный ответ.
    Точные переноска, число людей и scaling — downstream. Маршрут
    P0 → Q1 сохраняется.»

log: |
  canon-cartography g-d3a8 current front approved: old question docs are
  historical only; P0 protects common gas value + artifact line; Q1 Simple
  Gas Extraction is sole ready question; Simple Suction Bubble remains a
  candidate; carry/scaling downstream and co-op proof_later.

next: |
  CALL c-research-q-simple-gas-extraction-001
  to: session
  direction: indie-game-development
  play: local/canon-forge
  node: g-d3a8
  surface: any
  parent: s-cartography-g-d3a8-current-question-front-001

  goal: |
    Under the owner-approved current question map, the bounded P0 Frame-v2
    alignment and Q1 Simple Gas Extraction issue reach either one
    OWNER-SELECTED PAPER ANSWER or an explicit FRAME / QUESTION / PAPER
    block, while canon admission remains separate.

  context: |
    Read current:
    - os/KERNEL.md
    - live/indie-game-development/NOW.md
    - live/indie-game-development/CHARTER.md
    - live/indie-game-development/TREE.md
    - live/indie-game-development/plays/canon-forge.md
    - live/indie-game-development/work/
      canon-process-v3-paper-only-pilot-brief.md
    - live/indie-game-development/work/minimum-game-frame-v2.md
    - live/indie-game-development/work/canon-maps/
      g-d3a8-current-question-front-v1.md
    - live/indie-game-development/knowledge/
      g9c41-players-8-owner-requirement.md
    - current gas_coop_game_canon:
      CONSTITUTION.md, CORE.md, INDEX.md, QUEUE.md, SESSION.md and c-001
    - history/
      2026-07-14-s-repair-minimum-game-frame-v2-001.md
    - history/
      2026-07-16-s-cartography-g-d3a8-current-question-front-001.md

    Current authority:
    - Canon Forge v3 is the sole current design-to-canon route.
    - Old questions, old maps and earlier frozen answers are historical
      evidence only. They may inform or refute candidates but do not
      constrain the new answer and are not current canon.
    - Current card canon contains c-001 only; c-001 does not answer
      extraction, Bubble behavior, co-op roles, economy or artifacts.
    - Frame v2 is FRAME READY but currently leaves returned-gas conversion
      OPEN and gas+condition artifact origin as an architecture hypothesis.

    P0 owner directions to reconcile at Gate F:
    1. Safely returned different gas types feed one common durable purchasing
       value for predictable tools; exact conversion, currency, rates,
       prices, demand and exceptions remain OPEN.
    2. Artifacts necessarily exist and are connected to gas interacting
       with physical map conditions, objects or spatial states; exact
       emergence grammar, actions, frequency, catalogue and persistence
       remain OPEN.

    Q1 current question:
    When a player activates the Bubble near physical gas, what minimal
    obvious action transfers a chosen amount into a growing Bubble, what
    visibly changes during extraction, and what makes the decisions
    “where / how much / when to stop” meaningful rather than
    hold-to-fill waiting?

    Owner-origin input — not selected:
    Simple Suction Bubble. One player can perform basic extraction; the
    Bubble visibly sucks in gas and grows; the player chooses when to stop.
    A larger voluntarily chosen Bubble may later require more people to
    handle, but exact carry, helper count and scaling are downstream.

    Design posture:
    The base action should be obvious and simple. Complexity or novelty is
    not a goal. Exact gases may be used only as noncanonical test probes.

    Co-op disposition:
    Do not reopen abstract temporary-role composition. Co-op may be a
    comparative benefit, but integrated 4–8-player value remains
    proof_later after concrete sandbox mechanics and greybox evidence.

  boundaries: |
    Owner-present and text only.
    Do not treat historical question documents as canon, parent locks or
    mandatory invariants.
    Do not alter canon in this CALL; any admission is a separate
    owner-present transition over the exact paper artifact.
    Do not decide the full delivery/carry loop, exact number of helpers,
    player-count scaling, complete gas roster, final tool, production
    controls/UI, damage, Sc-damage, networking, balance or implementation.
    Do not decide exact common-value economy or artifact mechanics beyond
    the bounded P0 Frame wording.
    Do not treat Simple Suction Bubble as selected.
    Do not make unusual complexity a positive criterion.
    Do not claim paper proves fun, runtime legibility or actual co-op.
    Preserve TREE, CHARTER and product unchanged.
    Sc-damage remains HELD.

  done_when: |
    1. P0 has one exact owner-readable bounded Frame proposal covering only:
       - common returned-gas purchasing value;
       - mandatory gas+physical-condition artifact line;
       with every detailed form explicitly OPEN.
    2. The owner gives a verbatim Gate F verdict:
       FRAME READY, FRAME REVISED or FRAME BLOCKED.
    3. The exact Q1 source, currentness, player decision, terms, blockers
       and non-scope are owner-readable, with a verbatim Gate Q verdict.
    4. If both gates pass, one shared extraction scene supports 2–3
       mechanically distinct, equally rendered, simple paper candidates,
       including Simple Suction Bubble as owner-origin input rather than an
       automatic winner.
    5. The session returns either:
       - one OWNER-SELECTED PAPER ANSWER for Simple Gas Extraction, naming
         every unverified dimension and the owner's verbatim verdict; or
       - an honest FRAME, QUESTION or PAPER block on the same issue.
    6. Exact carry, helper count, scaling, roster, damage, economy,
       artifact mechanics, networking and implementation remain undecided.
    7. Canon, TREE, CHARTER, product and Sc-damage remain unchanged.

  return: |
    Russian Gate F / Gate Q brief; bounded P0 Frame proposal; Q1 paper
    comparison or exact block; source/status matrix; unverified dimensions;
    verbatim owner verdicts; one RESULT.

  budget: one owner-present text-only session

END_OF_FILE: live/indie-game-development/history/2026-07-16-s-cartography-g-d3a8-current-question-front-001.md
