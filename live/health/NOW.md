# NOW — health

active_bet:
  status: none
  note: >
    v1 nutrition approach RESET (2026-06-13). The chat-first "director + flat setup-gate" build
    did NOT work: it asked the owner expert questions it should research and decide (e.g. "how many
    meals per day"). Root cause is STRUCTURAL — no typed boundary between owner-only facts and
    system-decided expert variables. The node is reset to be re-derived from scratch via the
    converge play in a FRESH chat. Everything from v1 (architecture, evidence-base numbers, all
    prior decisions, the health-ai repo content) is DIRTY — input evidence only, never authority.

tasks: []

recurring: []

open_calls: []

decisions: []

next: |
  CALL c-health-nutrition-converge-001
  to: session
  direction: health
  play: converge
  node: g-health-nutrition-system
  goal: |
    The nutrition system node is converged from scratch into a closed, owner-signed WHAT spec for a
    professional, research-and-decide nutrition system — ready for shape.
  context: |
    RUN THIS IN A FRESH CHAT. Treat EVERYTHING as dirty: the current product repo
    github.com/ainazemtsau/health-ai (C:\projects\health-ai), the evidence-base numbers, the
    architecture (director + program-spine + domain-modules), and ALL prior decisions are INPUT
    EVIDENCE ONLY — re-derive and re-confirm with the owner; import nothing as born-closed;
    auto-fill no answers.

    Why the reset (the trouble): v1 asked the owner "how many meals per day?" — an expert decision
    the system must research and decide. Root cause: no typed boundary between owner-only facts and
    system-decided variables.

    Owner's bar: a super-professional health/nutrition agent that RESEARCHES and DECIDES everything
    expert (meals/day, timing, macros, food choice) and asks the owner ONLY irreducible personal
    facts (allergies, dislikes, budget, cooking-time, equipment) — minimal, skippable. Each process
    deeply worked out (not a shallow prompt). Chat-first, GitHub = single source of truth, owner
    never edits files. Extensible to training/water/etc. Must not become procrastination; tracking
    stays light. Guarded safety, non-prescriptive.

    A first-pass converge analysis (this chat, DIRTY input — do NOT treat as decided) is saved at
    live/health/work/converge-health-nutrition-input.md: the located defect, a disputed-term
    glossary, ~67 candidate WHAT questions tagged system-decides / owner-only / PLAN, and 5
    architecture options with a recommendation (Option E: typed personal-facts vs decided-variables
    split + generated plan artifact + per-process depth specs + thin router) + 7 high-risk
    architecture questions. Use it as a candidate set to refute and confirm — NOT as answers.

    Read: os/plays/converge.md, os/plays/converge-arch.md, os/plays/converge-verify.md,
    os/docs/converge-design.md, live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md,
    and the input doc above.
  boundaries: |
    Run the FULL converge process with its owner gates — do not skip the questions.
    Treat all prior state/decisions/data as dirty candidates; import nothing as authority; auto-fill nothing.
    Do not build or shape in this CALL; converge only (then converge-arch, converge-verify, then shape).
    Do not store raw daily data in Direction OS. No medical prescriptions.
  done_when: |
    converge produces work/converge-g-health-nutrition-system.md: triage, signed glossary, a closed
    cited §WHAT (forward+backward clean), the research-and-decide principle ratified, coverage
    complete; next = converge-arch (architecture incl. the personal-vs-decided boundary rule), then
    converge-verify, then shape.
  return: |
    RESULT with the converge spec surface, owner §SIGNOFFs, decisions_needed, and next CALL
    (converge-arch) or awaiting_decision.
  budget: converge movement (may span sessions; owner gates batched <=3)
  surface: fresh chat (Claude Code or ChatGPT/Claude project)

END_OF_FILE: live/health/NOW.md
