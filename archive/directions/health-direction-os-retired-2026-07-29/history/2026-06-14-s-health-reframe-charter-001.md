RESULT s-health-reframe-charter-001 (call: owner-message-2026-06-14-reframe-core-first)
direction: health   play: frame (charter revision)   node: g-health-root

outcome: |
  CHARTER amended for the core-first re-frame. A new "Системная архитектура Health AI System"
  constraint codifies: provider-independence (plain Markdown/YAML in git, managed by any LLM —
  ChatGPT/Claude/Claude Code/Codex — via AGENTS.md + CLAUDE.md(->AGENTS.md) + a portable
  system-prompt for project instructions; numbers-in-files/arithmetic-in-formulas; no proprietary
  memory/runtime); owner interface = NL/voice/photo + research-and-decide; self-extensibility
  (new global procedures via workflow; new domain = 1 folder + 1 registry line); core-first with
  nutrition/training as modules sharing metrics/phases. Mission and success_criteria are UNCHANGED.
  Routed as frame because map may not edit CHARTER.

evidence: |
  Owner approved in-session, exact word: "ok" — to the drafted CHARTER amendment + tree re-map.
  Requirements R1–R12 confirmed (R6 with the AGENTS.md/CLAUDE.md/system-prompt addition); R13
  (self-extensibility via workflow) added; F1–F4 resolved (F1 = supersede g-health-ai-core +
  wipe-and-rebuild the product repo in place; F2/F3/F4 per recommendation).

owner_approved: true
approval_evidence: >
  "ok" to the presented draft (CHARTER constraint + TREE re-map), this session, after the owner
  confirmed R1–R13 and F1–F4.

state_changes: |
  CHARTER.md:
  - constraints: appended one item "Системная архитектура Health AI System (принято 2026-06-14,
    core-first re-frame)": provider-independence (MD/YAML+git; AGENTS.md + CLAUDE.md(->AGENTS.md) +
    portable system-prompt; numbers in files / arithmetic in documented formulas; no proprietary
    memory/runtime); owner interface NL/voice/photo + research-and-decide; self-extensibility (new
    procedures via workflow; new domain = folder + registry line); core-first, nutrition/training
    as modules sharing metrics/phases.
  - mission, success_criteria, lenses, owner_edges, risk_posture, pre_mortem, product_repos: UNCHANGED.

captures:
  - Product repo health-ai is DIRTY; cleared and rebuilt IN PLACE at build time (repo kept, git
    history preserves v1), with explicit owner confirmation before the wipe.

decisions_needed: []

play_check:
  - 1 Interview (owner): N/A in revision — owner supplied the requirements directly (R1–R13, this chat).
  - 2 Homework (outside view): done — recon research (work/health-core-recon-research.md) informed the amendment.
  - 3 Charter draft + approval (owner): done — amendment presented; owner "ok" (G9).
  - 4 Pre-mortem: N/A — existing pre-mortem holds; the re-frame adds no new failure mode requiring a charter change.
  - 5 Root node: unchanged.
  - 6 Close (owner): done — owner_approved; next = map.

log: "frame: CHARTER amended for core-first (system-architecture constraint: provider-independence, NL+research-and-decide, self-extensibility, core-first modules); mission/success unchanged; owner ok."

next: |
  CALL c-health-reframe-map-001
  to: session
  direction: health
  play: map
  goal: Re-map the tree core-first (add g-health-core, supersede g-health-ai-core, reframe modules).
  budget: one map movement (owner already approved the draft).
  surface: this session (continues immediately as writer).

END_OF_FILE: live/health/history/2026-06-14-s-health-reframe-charter-001.md
