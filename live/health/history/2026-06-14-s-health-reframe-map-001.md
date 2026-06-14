RESULT s-health-reframe-map-001 (call: c-health-reframe-map-001)
direction: health   play: map   node: g-health-core (whole-tree re-map)

outcome: |
  The health tree is re-mapped CORE-FIRST. Added g-health-core (a strong, provider-independent,
  self-extensible Markdown/YAML core: programs-as-plan + daily tracking + shared metrics/phases/review
  + NL/voice/photo input), to converge FIRST. g-health-ai-core (was done) is dropped/superseded — its
  artifacts become dirty input. g-health-nutrition-system and g-health-training-activity-system are
  reframed as MODULES attached to the core (converge second/third, with cross-module data exchange).
  starter-kit unchanged (done). Owner approved the whole tree in-session ("ok").

evidence: |
  Owner "ok" (G9) to the drafted tree. Build order: core -> nutrition -> training (core unblocks both).
  Recon research (work/health-core-recon-research.md) supplied the non-obvious path: model the
  LLM-managed health system on plain-text-accounting (Beancount: directives-vs-transactions) + flat-text
  program DSLs (Liftosaur / Wendler 5/3/1 anchor-and-percentage) — i.e. PLAN-vs-LOG + anchors-vs-derived
  as the spine, so an LLM resolves daily numbers from a few stored anchors instead of hand-writing days.

owner_approved: true
approval_evidence: >
  "ok" to the presented TREE re-map (this session).

state_changes: |
  TREE.md:
  - ADD g-health-core (status parked): goal/why/done_when as approved (provider-independent MD/YAML core;
    programs-as-plan; daily NL/voice/photo tracking; owner-fact-vs-decided-variable typed boundary +
    research-and-decide; shared metrics/phase/PLAN-vs-LOG/review; self-extensibility via workflow; modules
    attach without rewrite; Direction OS boundary preserved).
  - g-health-ai-core: status done -> dropped (compressed to a one-line superseded entry; artifacts = dirty input).
  - g-health-nutrition-system: goal reframed as a MODULE on g-health-core (parked).
  - g-health-training-activity-system: goal reframed as a MODULE on g-health-core, cross-module with nutrition (parked).
  - root + g-health-starter-kit: unchanged.
  NOW.md:
  - active_bet stays none; note updated to the core-first re-frame (supersede ai-core; product repo
    health-ai cleared + rebuilt in place at build time, history preserved, explicit confirmation before wipe).
  - next -> CALL c-health-core-converge-001 (play converge, node g-health-core), with the recon research +
    nutrition Define draft as input evidence.
  LOG.md: appended frame + map lines.
  history/: added 2026-06-14-s-health-reframe-charter-001.md and 2026-06-14-s-health-reframe-map-001.md.
  work/: added health-core-recon-research.md (recon synthesis, input evidence) and
    converge-nutrition-define-draft.md (UN-RATIFIED paused nutrition Define: triage + 16-term glossary +
    research-and-decide principle).

captures:
  - Many paused nutrition Define terms are now CORE concepts (the anchors/profile owner-fact-vs-decided
    boundary, deficit-as-outcome-gated-band, fallback-counts-toward-targets, review-must-mutate).
  - 10 open questions from recon for the core converge: protein reference weight; review autonomy level;
    template-vs-materialized days; cross-module coupling depth; food/exercise DB seeding; photo trust boundary;
    objective-recovery-metrics (deferred, marketing-dominated evidence); concurrent-write policy;
    decision-cadence policy; clarify-gate policy.

decisions_needed: []

play_check:
  - 1 Recite: done — mission/success unchanged; current tree restated; re-frame to core-first.
  - 2 Candidates & evidence (owner): done — owner candidate = core-first (R1–R13); recon research as evidence.
  - 3 Skeleton (owner): done — whole proposed map shown one-screen; owner reacted (forks F1–F4).
  - 4 Cards: done — g-health-core card elaborated (goal/why/done_when/edge/risk); modules reframed;
    non-obvious path seeded from one rare example (Beancount/Liftosaur flat-file analogy).
  - 5 Per-node verdict (owner): done — owner "ok" to core, ai-core drop, module reframes, starter-kit unchanged.
  - 6 Order (owner): done — core -> nutrition -> training confirmed (core unblocks both).
  - 7 Depth check: done — top level only (rolling wave G2); deeper splits deferred to shape.
  - 8 Lens sweep: done — weight-nutrition/strength/activity/adherence/medical-safety map to modules;
    ai-system-data-architecture is the core node itself; no uncovered lens.
  - 9 Close (owner): done — whole tree approved ("ok"); next = converge g-health-core.

log: "map: tree re-mapped core-first — +g-health-core, g-health-ai-core dropped (superseded), nutrition/training reframed as modules; next = converge g-health-core."

next: |
  CALL c-health-core-converge-001
  to: session
  direction: health
  play: converge
  node: g-health-core
  goal: |
    Converge g-health-core into a closed, owner-signed WHAT spec for a strong, provider-independent,
    self-extensible Markdown/YAML health core, ready for converge-arch then shape.
  context: |
    Fresh chat. Core-first re-frame approved 2026-06-14 (history 2026-06-14-s-health-reframe-charter-001 +
    -map-001). INPUT EVIDENCE (refute/confirm, import nothing as authority):
    work/health-core-recon-research.md (anchors/profile as the typed owner-fact-vs-decided fix; PLAN-vs-LOG;
    shared metrics trend-weight/biofeedback/adherence; phase as cross-module lever; value-type grammar;
    PARSE-vs-VALUES firewall + clarify-only-on-material-ambiguity; definition library by stable id;
    append-only dated logs; review = no-mutation reconciliation that proposes, owner ratifies;
    provider-independence via MD/YAML+git+AGENTS.md; YAML robust-edit discipline; +10 open questions) and
    work/converge-nutrition-define-draft.md (UN-RATIFIED triage + 16-term glossary + research-and-decide).
    CHARTER system-architecture constraint + TREE g-health-core done_when. Product repo health-ai is DIRTY
    (cleared + rebuilt in place at build time; history preserved; explicit confirmation before the wipe).
  boundaries: |
    Full converge with owner gates (batched <=3 across the converge set); import nothing as authority;
    auto-fill nothing. Converge only (then converge-arch, converge-verify, shape). No raw daily data in
    Direction OS; no medical prescriptions.
  done_when: |
    work/converge-g-health-core.md: triage, signed glossary, closed cited §WHAT (research-and-decide +
    owner-fact/decided-variable boundary ratified; provider-independence + NL-input + self-extensibility as
    acceptance properties; shared-concept ownership; PLAN-vs-LOG; review mechanism), coverage complete;
    next = converge-arch.
  return: |
    RESULT with the converge spec surface, owner §SIGNOFFs, decisions_needed, and next CALL (converge-arch)
    or awaiting_decision.
  budget: converge movement (may span sessions; owner gates batched <=3)
  surface: fresh chat (Claude Code or ChatGPT/Claude project)

END_OF_FILE: live/health/history/2026-06-14-s-health-reframe-map-001.md
