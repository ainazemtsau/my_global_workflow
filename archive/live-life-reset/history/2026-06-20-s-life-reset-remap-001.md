RESULT s-life-reset-remap-001 (call: c-life-reset-remap-001)
direction: life-reset   play: map   node/task: g-life-reset-root

outcome: |
  The remap session did not produce a new tree. Co-creating with the owner
  revealed the current CHARTER root is too narrow: life-reset is not a weekly
  tracker and not a set of isolated programs, but a STRICT, SELF-IMPROVING
  personal operating MANAGER (weekly+daily rhythm) as the spine, into which
  directions, programs and a backlog plug. Because map cannot edit CHARTER.md,
  the session routes to FRAME. The full captured vision (R1–R31 + two operating
  models) is saved durably; the TREE stays invalid until the root is re-framed
  (owner-approved) and a fresh map rebuilds the tree on it.

evidence: |
  Owner co-creation in-session (key words):
  - "наш workflow не трекает недели, он строит процессы программы ... и уже в
    них проходит всё"; "это же должно всё объединено быть".
  - "всё это курирует ... недельный ритм ... task/time/personal менеджер ...
    использует лучшие практики ... чтобы планы достигались".
  - strict personality: "очень жёсткий, очень прямолинейный, направленный
    только на эффективность"; "он ни разу не должен прогибаться"; dance/discount
    examples; "лучше где-то перекритиковать, чем недокритиковать".
  - self-improving process: "сам вот этот процесс ... определял ... делает
    research ... возможно этот процесс перестроил ... если неделю пошло что-то
    не так ... запустился цикл, который сделает новый research и улучшит ...
    сам процесс".
  - week refinement: directions "может читать, но ... не вся информация";
    "сначала ... минимум, что должно быть сделано", routine floors "уборка ...
    должна делать", wishes only after, через фильтр.
  - route approval: "давай тогда закрывать мап, как ты написал ... команда Go".
  Captured artifact: live/life-reset/work/life-reset-manager-vision-capture-v1.md

state_changes: |
  NEW work/: live/life-reset/work/life-reset-manager-vision-capture-v1.md
    — the durable capture (R1–R31, hub model, operating-state loop, week
    composition, three guardrail flags, open research questions).

  NOW.md:
    - active_bet: keep status none; set repair_status: root_being_reframed;
      replace note to explain the manager-as-spine finding and the route to
      frame; keep TREE invalid until re-frame.
    - preserved_evidence: add the capture artifact and this session's history.
    - open_calls: remove c-life-reset-remap-001 (its RESULT = this); add
      c-life-reset-frame-manager-root-001.
    - next: replace with CALL c-life-reset-frame-manager-root-001 (play: frame).

  LOG.md: append the 2026-06-20 map→frame line.

  history/: this file.

  CHARTER.md / TREE.md: unchanged (root change happens in frame, with G9
  approval — not here).

captures:
  - The manager is framed as a "personality" (mentor / manager / owner's
    reflection) over a distributed process of cycles/blocks — owner-facing tone,
    not literal autonomy.
  - Open design questions for the research leg: week-graph structure; balance
    minimum/routine-floors/wishes; safe self-rewriting of process rules;
    encoding a non-caving prioritization policy; "math precision" = heuristic +
    evidence, not literal optimization.

decisions_needed: []

play_check:
  - "1 Recite: done — restated mission, current invalid-tree state and the drift
    diagnosis (weekly node tunneled into whole-runtime work) before any building."
  - "2 Candidates & evidence (owner): done — owner waived listing candidate
    nodes and instead delivered his own system model; the 2026-06-19
    map_evidence plus the accumulated runtime/dry-run artifacts were mined. His
    words: \"наш workflow не трекает недели, он строит процессы программы\" and
    the strict-manager spec. This revealed the charter root is too narrow."
  - "3 Skeleton (owner): skipped — routed to frame before skeleton; per the map
    play note, map does not edit CHARTER.md and the root itself must change first."
  - "4 Cards: skipped — no tree built; root re-frame precedes the tree."
  - "5 Per-node verdict (owner): skipped — no cards."
  - "6 Order (owner): skipped — no tree."
  - "7 Depth check: skipped — no tree."
  - "8 Lens sweep: skipped — belongs to the map that follows the re-frame."
  - "9 Close (owner): done as a ROUTE approval, not a tree approval — owner:
    \"давай тогда закрывать мап ... команда Go\"."

log: "map→frame: owner co-created the real scope (strict, self-improving personal manager as spine; week = minimum + routine floors + wishes via filter); current charter root too narrow → routed to frame; full vision captured (R1–R31); next c-life-reset-frame-manager-root-001."

next: |
  CALL c-life-reset-frame-manager-root-001
  to: session
  direction: life-reset
  play: frame
  node: g-life-reset-root
  goal: |
    life-reset has an owner-approved revised root (mission, success criteria,
    principles/constraints, lenses) that encodes the real scope: a strict,
    self-improving personal operating manager as the spine — not a weekly
    tracker and not isolated programs.
  context: |
    Read, in this order:
    - os/KERNEL.md
    - os/plays/frame.md
    - live/life-reset/CHARTER.md (current root to revise)
    - live/life-reset/NOW.md
    - live/life-reset/work/life-reset-manager-vision-capture-v1.md  (R1–R31 + models — primary input)
    - live/life-reset/history/2026-06-20-s-life-reset-remap-001.md

    The revised root must newly encode:
    - manager-as-spine: one coordinating personal manager (weekly+daily rhythm)
      into which directions + programs + backlog plug; the week is the manager's
      pulse, not a contract artifact (R8, R27–R29).
    - strict personality (R1–R7, R30–R31): efficiency-first, non-caving,
      aggressive/critical-by-default in any program (especially where work
      stalls), "better to over-criticize than under-criticize"; interrupt the
      accepted plan only for real impact on current goals/directions or a hard
      newly-discovered due date; on rest/play do not moralize but seek synergy —
      while still allowing genuine recovery.
    - self-improving process (R13–R17): self-defining intake that researches the
      owner's work-style and can rewrite its own instructions; a week-gone-wrong
      triggers a re-research/improve cycle on the process itself.
    - portability/state/writer (R18–R22) and the v1 goal + expansion (R23–R24).
  boundaries: |
    Present the revised root one artifact at a time; nothing enters CHARTER.md
    without explicit owner approval (G9).
    Do not build the tree (that is the following map).
    Do not run the implementation research inside frame.
    Keep success criteria measurable and PROTECT the "run one real cycle before
    more architecture" gate (charter pre_mortem #11) and the guardrails: process
    self-rule-changes pass an explicit gate/review and the manager cannot
    silently disable the owner's override path; "math precision" = heuristic +
    evidence.
    Do not store raw health/game/Solmax data; keep source-direction boundaries.
    Do not prescribe nutrition/training/medical/psychiatric treatment.
  done_when: |
    CHARTER.md root (mission, success_criteria, principles, lenses) is owner-
    approved and reflects R1–R31; NOW.next is a map CALL to rebuild the tree on
    the revised root.
  return: |
    RESULT with the owner-approved revised charter root, state_changes, evidence
    and next map CALL.
  budget: one frame session

END_OF_FILE: live/life-reset/history/2026-06-20-s-life-reset-remap-001.md
