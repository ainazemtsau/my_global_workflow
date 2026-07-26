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

END_OF_FILE: live/indie-game-development/work/c-research-canon-design-process-v3-001-call.md
