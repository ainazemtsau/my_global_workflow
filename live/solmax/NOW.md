# NOW — solmax

project:
  name: Zaratusta
  product_repo: github.com/ainazemtsau/zaratusta

active_bet:
  status: none

repair_status: tree_reset_pending_evidence_audit

owner_directive: |
  The first preparatory Zaratusta phase should implement the functionality
  developed under LifeReset: a personal operating manager coordinating the
  owner's week/day rhythm, state, intake, planning, review and evolution.

  The latest LifeReset concept is a strong baseline, but it is not automatically
  accepted. Audit the concept, specification, implementation and prior workflow
  problems first. Then rebuild the Zaratusta TREE with the owner.

  After this phase is proven, continue toward the broader capabilities previously
  planned for Zaratusta.

blocked_reason: |
  The old g-kernel-first route and the previous LifeReset tree were created under
  incompatible sequencing assumptions. Previous implementation also suffered from
  requirement drift and parallel conflicting artifacts. No implementation resumes
  until evidence is audited and a fresh map is owner-approved.

owner_candidate_for_map:
  source_words: |
    "то что мы сейчас делаем это своеобразный подготовительный этап для Zaratusta"
  candidate: |
    First prove a coherent personal operating-manager capability derived from the
    latest LifeReset concept; then proceed toward the broader Zaratusta exocortex.

tasks: []
recurring: []
decisions: []
open_calls: []

preserved_evidence:
  - live/solmax/CHARTER.md
  - live/solmax/history/s-map-001.md
  - live/solmax/history/s-shape-001.md
  - live/life-reset/CHARTER.md
  - live/life-reset/LOG.md
  - live/life-reset/history/
  - live/life-reset/work/
  - github.com/ainazemtsau/life-reset-manager
  - github.com/ainazemtsau/zaratusta

next:
  id: c-zara-life-manager-map-evidence-001
  to: session
  direction: solmax
  play: research
  node: g-zara
  goal: |
    Produce fresh map evidence for rebuilding the Zaratusta tree by auditing the
    latest LifeReset concept and implementation as the candidate first preparatory
    Zaratusta capability.
  context: |
    Owner decisions:
    - The project is Zaratusta, not LifeReset.
    - Use github.com/ainazemtsau/zaratusta as the canonical product repository.
    - Begin with the functionality defined in the latest LifeReset concept.
    - Treat that concept as a strong baseline, not unquestionable authority.
    - After this phase is proven, continue toward the broader prior Zaratusta plan.

    Internal sources:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/LOG.md
    - live/solmax/history/s-map-001.md
    - live/life-reset/CHARTER.md
    - live/life-reset/LOG.md
    - live/life-reset/history/
    - live/life-reset/work/
    - github.com/ainazemtsau/life-reset-manager
    - github.com/ainazemtsau/zaratusta

    Reconstruct separately:
    1. what was conceptually sound;
    2. what failed because of planning/workflow/concurrency;
    3. what failed or remains unproven in specification or implementation;
    4. what is obsolete, contradictory or duplicated;
    5. what the first Zaratusta phase must prove before broader expansion.
  boundaries: |
    Do not modify state or repositories.
    Do not implement or migrate files.
    Do not accept the old LifeReset tree, old Zaratusta tree, SPEC or v1 merely
    because they exist.
    Do not collapse concept defects and execution defects into one category.
    Do not prescribe medical, psychiatric, nutrition or training treatment.
    If the existing Zaratusta root itself appears wrong, report the evidence and
    recommend a frame route; do not silently rewrite it.
  done_when: |
    Return one evidence report containing:

    - a dated chronology of the previous route and its failure points;
    - a requirement-to-implementation trace across the latest LifeReset concept,
      specifications and actual product files;
    - a `keep | change | investigate | drop` verdict for every load-bearing
      mechanism;
    - explicit separation of concept problems, specification problems,
      implementation problems and workflow/concurrency problems;
    - missing acceptance evidence and dangerous untested assumptions;
    - 2–3 external reference cases relevant to personal operating managers,
      durable agent state and evidence-gated self-improvement;
    - 3–6 candidate top-level Zaratusta outcomes for the subsequent map,
      including the owner candidate on equal footing;
    - the strongest argument against making the operating manager the first node;
    - a recommendation on whether map may proceed under the current root or must
      route to frame.
  return: |
    RESULT with sourced findings, confidence and limits; next =
    c-zara-remap-001 using play map.
  budget: one focused research session

END_OF_FILE: live/solmax/NOW.md
