# NOW — solmax

active_bet:
  node: none
  note: |
    No active bet yet — the direction was just framed (foundation only). The goal tree
    (children of g-zara) is built next in a map session; the first bet (the Wave-0 RLK
    kernel) is shaped after that. Because the architecture is already designed (RLK +
    the wave plan), the map can be light — mostly ratifying the tree shape (the four
    extension axes + the waves) card-by-card — then straight to shaping Wave-0.

active_tasks: []

recurring: []

open_calls:
  - id: c-map-001
    status: ready
    note: |
      Map the goal tree for g-zara. Owner waived map_evidence (the two design workflows
      this session already supply the evidence). Candidate outcomes carried in next +
      RESULT.captures (history/s-frame-001.md).

decision_inbox: []

next: |
  CALL c-map-001
  to: session (map play)
  direction: solmax   node: g-zara
  goal: |
    Build the goal tree under g-zara — children as OUTCOMES only (no tasks), each with its
    one-line why, organized by the RLK architecture, the four extension axes, and the wave
    plan. Co-create card-by-card with the owner (G9). The map can be light: the architecture
    is already designed, so this is largely ratifying the tree shape and ordering.
  context: |
    - CHARTER.md (this direction) + TREE.md root g-zara.
    - Recommended architecture = "Solmax Registry-Ledger Kernel (RLK)" (design workflow
      wf_d1ea25b7): kernel owns ONLY 5 things — (1) Capability Registry (id -> {kind [open
      string], input/output schema, effect_tier, handler}); (2) append-only JSONL ledger
      with ledger-before-delivery + schema_version + reserved upcaster (= source of truth +
      audit + resume + Dream-Lab replay); (3) typed CALL/RESULT envelope + boundary
      validator; (4) effect-tier gate (0 silent / 1 reversible / 2 external-irreversible ->
      owner approval); (5) exactly two seams Engine + Store. Everything else (tools,
      channels, memory, processes, surfaces) = registry "kinds" added by register() with
      ~0 kernel diff. Acceptance test: "add the 20th capability = one register() + a handler
      file, 0-line kernel diff."
    - Engine = subscriptions not API: claude -p (forced JSON-Schema) = primary brain;
      codex exec = cross-vendor verifier/engineer; ChatGPT app = manual remote-MCP cockpit
      (NOT scriptable). ⚠️ ~$20/mo Agent-SDK credit cliff -> engine layer budgets +
      fails over. Clean API seam later (adapter swap behind the Engine port).
    - Build mode: background AI agents under owner review; decompose into small,
      agent-buildable, verifiable increments.
    - Candidate outcomes (frame captures, for the tree):
      * the RLK kernel (Wave 0 — registry + ledger + envelope + effect-tier gate + Engine
        & Store seam interfaces) + proof that a 3rd plug-in is a 0-line kernel diff;
      * Engine adapter (claude -p) + cost/credit handling + codex verifier (Wave 1);
      * first Channel (Telegram or in-app chat — freezes the channel contract) (Wave 1);
      * compile_context + the cognition loop as plug-in #1 (Wave 2);
      * Process kind + pluggable triggers (manual/schedule via cron-MCP/event) (Wave 2);
      * Memory kinds (episodic over the ledger; semantic/RAG; SQLite fold) (Wave 2);
      * Tools: whiteboard, kanban, app-connectors;
      * OS read-only capability (link to the workflow-OS repo, read-only);
      * big-vision capabilities as later plug-ins: Dream Lab (ledger replay at raised
        temperature), prediction-error learning, Reality-Alignment verifier, Environment
        Composer (Surface kind), omnichannel body (Wave 3+);
      * the four extension axes (tool/channel/memory/process) as the tree's organizing spine;
      * the wave plan W0 -> W3+ as map_order.
  done_when: |
    The goal tree exists under g-zara with children approved card-by-card by the owner;
    NOW points to the first shape (likely Wave-0: the RLK kernel + extension mechanism).
  boundaries: |
    Map creates OUTCOMES only — no tasks, no Wave-0 spec (that is shape). Keep the kernel
    tiny (KERNEL: "six file types, never more — wanting more structure is usually the wrong
    problem"). Never make the OS a write target. New ideas default to parked (G8).
  return: TREE.md children + map_order + next = a shape CALL on Wave-0.
  budget: one map session (light — architecture already decided).

END_OF_FILE: live/solmax/NOW.md
