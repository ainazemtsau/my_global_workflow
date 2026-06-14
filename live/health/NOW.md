# NOW — health

active_bet:
  status: none
  note: >
    CORE-FIRST RE-FRAME (2026-06-14). Owner redirected the whole direction: build a strong,
    structured, provider-independent CORE first (programs-as-plan + daily tracking + records +
    shared metrics/phases/review, Markdown/YAML in git, NL/voice/photo input, self-extensible
    via workflow), then nutrition and training as MODULES attached to it. The tree was re-mapped
    and CHARTER amended with a system-architecture constraint (owner approved, "ok").

    g-health-ai-core (was done) is SUPERSEDED/dropped — its artifacts (product repo health-ai,
    contract/skeleton v0) are dirty input, not authority. The product repo health-ai will be
    CLEARED and rebuilt in place at build time (same repo, git history preserves v1); the actual
    wipe needs explicit owner confirmation at that step.

    The prior nutrition converge is PAUSED; its Define output (triage + 16-term glossary +
    research-and-decide principle) is preserved DIRTY at work/converge-nutrition-define-draft.md,
    and a best-practice recon pass at work/health-core-recon-research.md — both are input evidence
    for the core converge, never authority. next = converge g-health-core from this evidence.

tasks: []

recurring: []

open_calls: []

decisions: []

next: |
  CALL c-health-core-converge-001
  to: session
  direction: health
  play: converge
  node: g-health-core
  goal: |
    Converge g-health-core into a closed, owner-signed WHAT spec for a strong, provider-independent,
    self-extensible Markdown/YAML health core (programs-as-plan + daily tracking + shared
    metrics/phases/review + NL/voice/photo input), ready for converge-arch then shape.
  context: |
    RUN IN A FRESH CHAT. Core-first re-frame approved 2026-06-14
    (history/2026-06-14-s-health-reframe-charter-001.md + -map-001.md).

    INPUT EVIDENCE (refute/confirm — import NOTHING as authority, auto-fill nothing):
    - work/health-core-recon-research.md — best-practice recon (MacroFactor, Cronometer, USDA FDC,
      Hevy/Liftosaur, Wendler 5/3/1, Beancount, Obsidian, peer-reviewed protein/trend/autoregulation):
      anchors/profile file as the typed owner-fact-vs-decided-variable fix; PLAN-vs-LOG split;
      shared metrics (trend weight / biofeedback / adherence); phase as the cross-module lever;
      a value-type grammar; PARSE-vs-VALUES firewall + clarify-only-on-material-ambiguity;
      definition library by stable id; append-only dated logs; review = no-mutation reconciliation
      that PROPOSES (owner ratifies); provider-independence via MD/YAML+git+AGENTS.md; YAML
      robust-edit discipline; + 10 open questions for the converge.
    - work/converge-nutrition-define-draft.md — UN-RATIFIED paused nutrition Define: triage +
      16-term glossary + research-and-decide principle. Many terms are now CORE concepts (the
      anchors split, deficit-as-outcome-gated-band, fallback-counts-toward-targets, review-must-mutate).
      Re-derive at the core level; do not import as answered.
    - CHARTER.md (the system-architecture constraint) and TREE.md (g-health-core done_when).
    - DIRTY: product repo health-ai (will be cleared + rebuilt in place at build time; explicit
      owner confirmation before the wipe).
  boundaries: |
    Full converge with owner gates (batched <=3 across the converge set). Import nothing as authority;
    auto-fill nothing. Converge only (then converge-arch for contracts+architecture, then
    converge-verify, then shape). No raw daily data in Direction OS. No medical prescriptions.
  done_when: |
    work/converge-g-health-core.md: triage, signed glossary, closed cited §WHAT (research-and-decide
    principle + the owner-fact/decided-variable boundary ratified; provider-independence + NL/voice/photo
    input + self-extensibility as acceptance properties; shared-concept ownership; PLAN-vs-LOG; review
    mechanism), coverage complete; next = converge-arch.
  return: |
    RESULT with the converge spec surface, owner §SIGNOFFs, decisions_needed, and next CALL
    (converge-arch) or awaiting_decision.
  budget: converge movement (may span sessions; owner gates batched <=3)
  surface: fresh chat (Claude Code or ChatGPT/Claude project)

END_OF_FILE: live/health/NOW.md
