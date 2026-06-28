# NOW — health

active_bet:
  status: none
  note: |
    No active bet after the training/activity v0 product/process work and its 2026-06-28 repair.
    Product/process evidence before repair: health-ai c1bf61e for t-1 and health-ai 8aa14f8 for t-2;
    owner release acceptance from t-3: "Запускаем". On 2026-06-28 the owner supplied a correction
    showing that 8aa14f8 falsely resolved x_training_activity to ACTIVE/DAY_LOOP on sample-only
    evidence. Bounded product repair health-ai 1fe41c2 supersedes that false launch route:
    training/activity now resolves to PROGRAM awaiting Deep Research, blocks proposal/ACTIVE/week/
    session until a suitable returned research conclusion plus owner approval exists, and keeps
    first real performed session unclaimed.

    Owner clarified on 2026-06-28 that Direction OS must not track Health AI projects/processes by
    default: "мы не трэкаем проекты если только я прямо не попрошу". Health AI may continue its
    nutrition/training work outside Direction OS. Direction OS will handle nutrition/training issues,
    returned conclusions, repairs or process-development decisions only when the owner explicitly
    brings them back.

tasks: []

open_calls: []

recurring:
  - id: r-health-ai-minor-fix-lane
    goal: >
      Keep a lightweight intake lane for minor Health AI UX/contract/prompt
      papercuts that do not justify a full direction bet.
    done_when: >
      Due minor Health AI issues are batched into a bounded repair/executor CALL
      or explicitly deferred/dropped; no raw health diary enters Direction OS.
    cadence: on_demand
    lens: ai-system-data-architecture
    last_done: 2026-06-28
    note: >
      Post-1338a35 bounded work was reconciled into this lane: menu workflow
      structure repair and owner_fact_delta/assumption hardening
      (7cd962a, 83dba88, 77a0ed), followed by fixed-menu/recipe support through
      health-ai 8246cec. On 2026-06-28 the lane handled the training/activity false
      launch-readiness repair in health-ai 1fe41c2: validation.config was re-synced to
      os-engineering-contract.v9, the training checker rejects the old ACTIVE/DAY_LOOP
      sample-launch state, and Health AI now blocks at PROGRAM awaiting Deep Research.
      The lane remains recurring/on-demand, not a second active bet. Authority, safety,
      provider-portability or owner-gate defects escalate to a bounded repair/executor
      CALL; cosmetic papercuts are batched, deferred or dropped.

decisions: []

next: |
  awaiting_owner_instruction

  Health AI continues outside Direction OS tracking. Do not poll, track, or propose execution-cycle
  tasks for nutrition/training unless the owner explicitly asks. If the owner brings a concrete
  returned training/activity research conclusion, problem, or process-development request, resolve
  that new message against current NOW.md and the relevant knowledge boundary.

END_OF_FILE: live/health/NOW.md
