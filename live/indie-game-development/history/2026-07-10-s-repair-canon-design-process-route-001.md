RESULT s-repair-canon-design-process-route-001 (call: owner-message-2026-07-10-canon-process-repair)
direction: indie-game-development   play: repair   node/task: g-d3a8/canon-process-repair

outcome: |
  Owner approved route «А»: the current Canon Forge v2 design-decision route is suspended pending
  an evidence-backed process redesign and one real pilot.

  core-0 gas states and core-1 bubble fill remain preserved, but are no longer active sequential
  canon questions. They are HOLD material for the pilot.

  Fixed foundations remain:
  - gas simulation;
  - reactions;
  - destructible/changeable space.

  Owner-liked concept material such as Bubble, three phases and sleeping-gas reconnaissance is
  classified as DESIGN ANCHOR:
  - not frozen canon;
  - not a fixed foundation;
  - not an ordinary discardable draft;
  - must not be lost or silently replaced;
  - may be revised, rejected or replaced only explicitly.

  No game-concept question was answered. No canon card was frozen. The full question graph will not
  be rebuilt until the new process passes one owner-evaluated pilot.

evidence: |
  - Owner confirmation in-session: «А».
  - Current Canon Forge v2 SESSION.md moves from framing directly into candidate answers and sparring;
    it has no mandatory pre-candidate dependency/readiness audit. Hidden prerequisites are handled
    only after the selected question proves unready.
  - Current NOW.md still exposes c-core-0-gas-states-001 as the ready canon route and core-1 as its
    downstream hold, showing a local queue reorder rather than a process-level correction.
  - history/2026-07-09-s-repair-canon-core-recovery-001.md and current NOW.md record the repeated
    failure pattern: accepted material was first demoted/lost, then over-protected; the first
    bubble-fill discussion then hit the missing gas-state prerequisite.
  - The owner-provided Indie Game Development.txt example records the owner-facing symptom:
    extensive prose, nested corrections and option menus without a sufficiently concrete and
    comparable decision experience.
  - INDEX.md remains empty; therefore no new Canon Forge v2 card must be revoked.

state_changes: |
  live/indie-game-development/NOW.md:

  1. Change the header to:
     updated: 2026-07-10 by s-repair-canon-design-process-route-001

  2. In open_calls, remove the entire entry:
     c-core-0-gas-states-001

  3. In open_calls, add:

     - id: c-research-canon-design-process-v3-001
       to: session
       for: g-d3a8 / evidence-backed canon design process v3
       issued: 2026-07-10
       call: work/c-research-canon-design-process-v3-001-call.md
       note: |
         READY research session after owner verdict «А». Canon Forge v2 is suspended as the active
         design-decision route. core-0 gas states and core-1 bubble fill are HOLD material for one
         future pilot, not active canon questions. Fixed foundations remain gas simulation,
         reactions and destructible/changeable space. Bubble, three phases, sleeping-gas recon and
         other owner-liked material are DESIGN ANCHORS: preserve them, but do not treat them as canon
         or immutable foundations. This CALL researches structurally different process options and
         returns a pilot-ready recommendation; it does not answer the concept, install a process or
         rebuild the full question graph.

  4. Replace only parallel_tracks entry g-d3a8.state with:

     state: |-
       PROCESS REPAIR ROUTED 2026-07-10
       (s-repair-canon-design-process-route-001; owner «А»). Canon Forge v2 is suspended as the
       active design-decision route: repeated sessions mixed design discovery with canon recording,
       lacked a dependency/readiness gate, and selected bubble-fill before gas-state semantics.
       core-0/core-1 are preserved as HOLD material for one pilot, not active sequential questions.
       Fixed foundations remain gas simulation, reactions and destructible/changeable space.
       Bubble, three phases, sleeping-gas reconnaissance and other owner-liked material are DESIGN
       ANCHORS — not canon, not foundations and not ordinary discardable drafts; preserve them and
       challenge/replace only explicitly. INDEX remains empty. Next design work =
       c-research-canon-design-process-v3-001. No full graph rebuild or concept verdict before one
       owner-evaluated pilot.

  5. Preserve every engine and visual line under NOW.next unchanged. Replace only the canon line:

     - CALL c-core-0-gas-states-001 → work/c-core-0-gas-states-call.md

     with:

     - CALL c-research-canon-design-process-v3-001 → work/c-research-canon-design-process-v3-001-call.md
       # CANON PROCESS: research process v3 + prepare one pilot; core-0/core-1 remain HOLD material

  6. decisions, bet, tasks, recurring and all non-g-d3a8 parallel tracks remain unchanged.

  live/indie-game-development/work/:

  Add c-research-canon-design-process-v3-001-call.md with exactly:

  CALL c-research-canon-design-process-v3-001
  to: session
  direction: indie-game-development
  play: research
  node: g-d3a8
  parent: s-repair-canon-design-process-route-001
  surface: any

  goal: |
    An evidence-backed recommendation exists for a game-design decision process that turns fixed
    foundations and owner-liked design anchors into decisions the owner can understand and evaluate,
    while keeping canon recording separate and preventing premature questions, idea loss,
    over-freezing and hard-to-judge prose.

  context: |
    Owner approved route «А» on 2026-07-10: perform a full process repair, then test it on one real
    decision bundle before rebuilding the full question graph.

    Fixed foundations:
    - gas simulation;
    - reactions;
    - destructible/changeable space.

    Owner-liked material has status DESIGN ANCHOR, not canon/foundation/ordinary draft:
    Bubble «неси, не лопни», three phases, sleeping-gas reconnaissance and related concept material
    must not be lost or silently replaced, but may be explicitly revised, rejected or superseded.

    Observed failure pattern:
    - Canon Forge v2 combines design discovery and canon recording;
    - candidate generation begins without a mandatory dependency/readiness audit;
    - a linear one-question queue selected bubble-fill before gas-state semantics;
    - prior repairs oscillated Bubble between parking/loss and excessive protection;
    - owner-facing outputs became long and difficult to evaluate as actual gameplay;
    - INDEX.md is empty: no new v2 canon card is frozen;
    - core-0 and core-1 are preserved as HOLD material for the future pilot.

    Read:
    - os/KERNEL.md
    - os/plays/research.md
    - live/indie-game-development/NOW.md
    - live/indie-game-development/plays/canon-forge.md
    - live/indie-game-development/history/s-process-canon-forge-v2-001.md
    - live/indie-game-development/history/2026-07-09-s-repair-canon-core-recovery-001.md
    - live/indie-game-development/knowledge/mechanic-lenses.md
    - live/indie-game-development/work/canon-maps/core-concept-rebuild-question-map-v0.1.md
      as revoked failure evidence only
    - canon repo:
      CONSTITUTION.md, CORE.md, INDEX.md, QUEUE.md, SESSION.md, START.md,
      templates/card.md
    - this parent RESULT, including the owner's current problem statement and verdict «А»

    Research authoritative or primary game-design and decision-process material where possible.
    Relevant fields include playcentric/iterative design, prototyping and playtesting, MDA,
    player intention and perceivable consequence, hypothesis-driven design, dependency/readiness
    framing, decision records, set-based exploration and methods for comparing alternatives without
    forcing premature convergence.

  boundaries: |
    Do not answer the game concept.
    Do not choose gas states, bubble-fill, Bubble-first or an alternative concept.
    Do not freeze, amend or edit canon.
    Do not rebuild the full question graph.
    Do not install a process or modify repository files.
    Do not treat DESIGN ANCHOR as immutable canon or as low-priority draft.
    Do not use the old core-0 question as permission to continue Canon Forge v2.
    Do not recommend more prose, more agents or more questions without a falsifiable mechanism.
    Do not equate a paper-clean mechanic with fun.

  done_when: |
    One sourced report contains:

    1. A causal diagnosis of the observed failures, separating:
       - question-selection/dependency failure;
       - design-exploration failure;
       - owner-facing comparison failure;
       - memory/status failure;
       - canon-recording failure.

    2. Explicit criteria for a replacement process:
       - questions are ready before options are generated;
       - owner-liked anchors are preserved without becoming immutable;
       - options are comparable through the same concrete scene/test;
       - conversation remains understandable and decision-oriented;
       - paper decisions, visual hypotheses and prototype hypotheses are distinguished;
       - canon is downstream of design maturity;
       - side ideas remain retrievable without hijacking the session.

    3. Two or three structurally different process architectures, not cosmetic variants.
       Each includes mechanism, strengths, failure modes, operational cost and the strongest
       refutation.

    4. A recommendation with uncertainty and conditions that would change it.

    5. A proposed status taxonomy including at minimum a precise DESIGN ANCHOR status and a
       distinction between paper decision, prototype hypothesis and frozen canon.

    6. A dependency/readiness representation that supports:
       - multiple prerequisites;
       - justified co-framing;
       - a small ready front;
       - explicit evidence mode;
       - return when a hidden prerequisite is found.

    7. A compact owner-facing session format that replaces long undifferentiated prose with
       concrete, equally rendered situations and explicit comparison criteria.

    8. A pilot-ready brief using core-0 gas-state semantics and core-1 bubble-fill only as source
       material. The pilot must test the process, not answer or freeze those design questions.

    9. Pilot pass/fail criteria. At minimum, the pilot fails if:
       - the owner still cannot explain what is being decided;
       - candidates depend on undefined entities;
       - options are prose variants rather than mechanical alternatives;
       - the session pressures a verdict without sufficient evidence;
       - the process loses or silently hardens a design anchor;
       - the output cannot name its next evidence requirement.

    Every external factual claim is cited. Established findings, inference and recommendation are
    clearly separated.

  return: |
    Russian owner-readable brief first, no more than 1,800 words:
    - diagnosis;
    - comparison of 2–3 architectures;
    - recommendation;
    - proposed status/dependency model;
    - exact pilot brief and kill criteria.

    Then RESULT with sources, confidence/limits, captures and
    next: return-to-parent s-repair-canon-design-process-route-001.

  budget: one session; up to 20 high-quality external sources

  live/indie-game-development/LOG.md:

  Append before END_OF_FILE:

  2026-07-10 — repair (g-d3a8/canon-process, s-repair-canon-design-process-route-001):
  owner chose «А»; suspended Canon Forge v2 as the active design route, held core-0/core-1
  for one pilot, classified liked concept material as design anchors, and opened evidence-backed
  process-v3 research before any full graph rebuild. →
  history/2026-07-10-s-repair-canon-design-process-route-001.md

  live/indie-game-development/history/:

  Add:
  history/2026-07-10-s-repair-canon-design-process-route-001.md
  containing this full RESULT.

  os/FRICTION.md:

  Append one line before END_OF_FILE:

  2026-07-10 indie-game-development repair: Canon Forge v2 mixed design discovery with canon
  recording and lacked a pre-candidate dependency/readiness gate; repeated repairs therefore
  oscillated owner-liked ideas between loss and over-freeze while a linear queue selected
  bubble-fill before gas-state semantics — owner approved full process research + one pilot
  before canon work resumes.

  Canon repository:
  - No files changed in this repair.
  - Treat its current START/SESSION/QUEUE route as suspended by the higher-authority NOW state.
  - Existing CORE/QUEUE content remains evidence and pilot material.
  - Exact replacement process files may be proposed only after research and owner review.
  - INDEX.md remains unchanged and empty.

  TREE.md:
  - unchanged.

  CHARTER.md:
  - unchanged.

captures:
  - Design Forge + Canon Ledger is a candidate architecture for the research comparison, not an adopted solution.
  - A dependency-aware decision bundle is a candidate unit of discussion, not yet a process rule.
  - The owner-provided long Canon Forge output should be used as a negative owner-facing-format test during the pilot.

decisions_needed: []

play_check:
  - 1 Name the contradiction: done — NOW and Canon Forge v2 route core-0 as the next design session, while the owner says the process itself repeatedly failed and asked for research/rebuild rather than another question answer.
  - 2 Reconstruct: done — process files, NOW, recovery history and the owner-provided failed output show premature-question selection, discovery/recording conflation, binary status oscillation and owner-facing comparison failure.
  - 3 Propose corrected state: done — suspend v2 design work, hold core-0/core-1, preserve only the three fixed foundations, classify liked material as design anchors and open bounded process-v3 research before a pilot.
  - 4 Confirm: done — owner verdict cited verbatim: «А».
  - 5 Friction: done — repeated process-level defect is added to os/FRICTION.md; no OS rule is changed in this session.

log: |
  repair g-d3a8/canon-process: owner chose «А»; old forge route suspended, anchors preserved without canon freeze, process-v3 research opened before one pilot.

next: |
  CALL c-research-canon-design-process-v3-001 →
  live/indie-game-development/work/c-research-canon-design-process-v3-001-call.md

END_OF_FILE: live/indie-game-development/history/2026-07-10-s-repair-canon-design-process-route-001.md
