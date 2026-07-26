RESULT
play: repair · direction: indie-game-development · node: g-9c41 · session: s-repair-canon-001
outcome: |
  CANON CONTEXT-HYGIENE repair (owner-directed). The owner caught two live architecture drifts while an S0
  planning chat explained the model: (a) determinism framed as needing «2 реальные машины» (he has one, and
  integer cross-CPU determinism is an established given), and (b) «каждый пир считает все 8 детальных пузырей»
  (the spec says ~1 bubble/peer, not N). A drift-sweep (wf_d11d864b, 11 agents, 16 invariants) CONFIRMED the
  root: the LOCKED decisions are sound and recorded verbatim; the drift is purely downstream — (1) vintage
  pre-2026-06-22 docs sitting in work/ next to the lock and read as authority, (2) lossy paraphrase-from-memory
  by chats over-generalizing one true fact onto its exception tier. Fix = ZERO-LEGACY applied to DOCS (the
  owner's own locked rule #6): archive the stale docs to a real place, add a tiny drift-guard, resolve the lone
  genuine canon gap. NO architecture decision changed.
evidence: drift-sweep wf_d11d864b (Extract/Check/Register over canon + 7 secondary docs + 2 pasted chat texts) +
  prior determinism-reconcile wf_94a1ce4b; first-hand reads of locked-slices / detail-authority-cost-model /
  dev-plan-graph / grid-vs-graph (verified the «~1 bubble/peer» and «integer=given» claims against the actual
  files; caught + discarded one synthesis-agent embellishment of NOW.md:201). Owner directive + owner answer on
  the re-flux gap.
state_changes: |
  - MOVED (git mv) 11 pre-2026-06-22 architecture docs from work/ → work/archive/:
    gas-model-design-full-2026-06-20, gas-model-research-result-2026-06-20, gas-model-discussion-brief-2026-06-20,
    aplus-replan-under-locked-arch-v1, aplus-wave-map-v1, aplus-breakdown-v1, research-g-9c41-core-architecture-2026-06-12(+ -v2),
    research-g-9c41-analytic-representations-2026-06-12, shape-g-9c41-approaches-2026-06-12, research-g-9c41-coarse-representation-2026-06-18.
  - CREATED work/archive/README.md (what/why; «история, не авторитет»; the active canon list; the one live carry =
    aplus-wave-map §4.2 risk-register R-*).
  - CREATED knowledge/g9c41-drift-guard.md — 5 пересказ-ловушек (8-пузырей / 2-машины / грид-vs-граф / деталь-в-одну-сторону /
    float-гард) + the OPEN A/B depth fork; mandatory READ-FIRST with locked-slices.
  - PATCHED active canon docs to drop dangling archive pointers + add the new read-first refs:
    dev-plan-graph (§1 ASCII «2 машинах»→«loopback/1 машина»; §4 read-first + archive pointers),
    gas-model-architecture-decision (provenance + §15 base-doc pointers → work/archive/),
    grid-vs-graph (Вход → archive + a ⚠️ re-flux CORRECTION BANNER: all «2 машины»/«2-машинный спайк» = loopback ONE machine + zero-float guard),
    detail-authority-cost-model (Вход → archive).
  - NOW.md: phase-note SINGLE-ENTRY list + decision-inbox durable-spec list + the S0 CALL mandatory-ingest list all
    re-pointed to the 6-doc clean canon (locked-slices + drift-guard READ-FIRST; aplus-replan dropped → archived);
    decision_inbox += d-reflux-gate-001 (answered).
  - LOG appended. (Applied + committed this session as its own writer.)
captures: |
  - work/archive/ now also still holds NON-architecture-current misc not touched this pass (converge-g-9c41(.|-arch),
    audit-tree-2026-06-12, c-exec-004-call, discussion-2026-06-14, maintenance-request-2026-06-12 stayed in work/ —
    Wave-2 contract history / other topics, NOT architecture-drift sources; archive them too only on explicit owner ask).
  - Moved docs keep their original END_OF_FILE: work/<name> trailer paths (cosmetic; they are frozen history now).
  - TREE #11 detail + NOW historical phase-notes still narrate the old doc paths (history, not the active reading path) —
    left as-is to avoid G9 scope on superseded narration.
  - The A/B depth fork (room-granular vs sub-room-form; the owner's «start detailed everywhere, add coarse later» idea)
    is a REAL open design decision, NOT drift — carried in drift-guard as OPEN, to be settled at the slice PLAN where it bites.
decisions_needed: []   # d-reflux-gate-001 answered by the owner this session; A/B fork is per-slice, not batched
play_check: |
  Trigger✓ (owner-directed context-hygiene repair, not a live-state contradiction) · Scope✓ (work/ doc hygiene +
  one answered decision; no TREE semantic change, no CHARTER) · Evidence✓ (drift-sweep + first-hand file reads) ·
  Owner-words✓ (re-flux: «две машины мы не делаем … нужен гард, который не пропустит float»; archive: «должно быть
  такое место для архивной документации») · No-decision-changed✓ (only relocation + one owner answer) · Apply✓
next: |
  No new CALL — S0 stands (NOW.next), now reading a CLEAN canon (6 docs, drift-guard READ-FIRST). The owner is
  verifying the cleanup (summary delivered this session) before starting S0 in a fresh chat. Open, owner-facing:
  the A/B depth fork (room-granular vs sub-room-form) — to be answered at the slice PLAN where it first bites, not now.
log: "s-repair-canon-001 g-9c41 (repair): canon context-hygiene — 11 pre-06-22 docs → work/archive/, NEW drift-guard READ-FIRST, d-reflux-gate-001 answered (no 2 machines; float-guard); active canon trimmed to 6 docs; decisions unchanged"
END_OF_FILE: live/indie-game-development/history/s-repair-canon-001.md
