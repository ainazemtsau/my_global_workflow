RESULT s-health-training-activity-tree-cleanup-001 (call: owner-message-2026-06-28-health-tree-cleanup)
direction: health   play: repair   node/task: g-health-training-activity-system

outcome: |
  Owner approved a minimal TREE cleanup for g-health-training-activity-system.

  The requested cleanup removes stale training/activity launch-readiness wording from TREE.md:
  - old/stale authority: health-ai @8aa14f8, ACTIVE reduced authority, current-week/what-today projections.
  - current authority: health-ai @1fe41c2, PROGRAM / research_request / awaiting_deep_research.
  - no ACTIVE real training program, current week, today brief, first real session, or body-execution claim exists until a suitable returned research conclusion plus owner approval exist.

  Owner also corrected the operating boundary:
  - Direction OS must not propose or track project/process execution cycles by default.
  - Health AI can work internally; nutrition/training problems are brought to Direction OS only when the owner explicitly asks.
  - Direction OS remains for process development, architecture, state repair, major decisions, and bounded issue routing, not routine project tracking.

evidence: |
  Owner approval and correction:
  - "давай отправим запрос на очистку TREE"
  - "мы не трэкаем проекты если только я прямо не попрошу"
  - "если с nutrition или training будут проблемы мы отдельно будем решать"

  State evidence:
  - live/health/TREE.md currently has stale g-health-training-activity-system prefix saying DONE 2026-06-27, health-ai @8aa14f8, ACTIVE reduced authority, current-week/what-today projections.
  - live/health/NOW.md says health-ai 1fe41c2 supersedes the false 8aa14f8 launch route; training/activity now resolves to PROGRAM awaiting Deep Research and blocks proposal/ACTIVE/week/session until a suitable returned research conclusion plus owner approval.
  - live/health/knowledge/health-training-activity-v0-release-boundary.md already records the repaired boundary: x_training_activity is not ACTIVE, Health AI resolves training/activity to PROGRAM awaiting Deep Research, and ACTIVE outputs require owner approval of a named proposed program.

state_changes:
  live/health/TREE.md:
    update_owner_approved_evidence: |
      Add latest approval evidence:
      Owner approved a text-only cleanup for g-health-training-activity-system on 2026-06-28:
      "давай отправим запрос на очистку TREE". The cleanup replaces stale 8aa14f8/ACTIVE wording
      with the current 1fe41c2/PROGRAM-awaiting-research boundary; it does not restructure the node,
      reopen the bet, or claim body execution.
    replace_in_node:
      node_id: g-health-training-activity-system
      target_goal_prefix: |
        (DONE 2026-06-27 — training/activity v0 release accepted for personal Health AI use.
        Health AI @8aa14f8 has thin x_training_activity domain, ACTIVE reduced authority,
        current-week/what-today projections, normalized LOG/import/guided/status/review/handoff
        contour. First real performed session is not claimed; raw training/body execution data stay
        outside Direction OS.)
      replacement_goal_prefix: |
        (DONE 2026-06-27 at product/process review, with 2026-06-28 repair superseding launch-readiness semantics.
        Current authority is health-ai @1fe41c2: x_training_activity is PROGRAM awaiting Deep Research; no ACTIVE
        real training program, current week, today brief, or first real session is claimed until suitable returned
        research conclusion plus owner approval exist. Raw training/body execution data stay outside Direction OS.)
    preserve:
      - root.status: shaped
      - g-health-training-activity-system.status: done
      - g-health-training-activity-system.done_when
      - g-health-training-activity-system.why
      - all other nodes and statuses

  live/health/NOW.md:
    preserve:
      - active_bet.status: none
      - tasks: []
      - decisions: []
      - recurring[id=r-health-ai-minor-fix-lane]
      - raw-data boundary
    replace_open_calls_with: []
    replace_active_bet_note_with: |
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
    replace_next_with: |
      awaiting_owner_instruction

      Health AI continues outside Direction OS tracking. Do not poll, track, or propose execution-cycle
      tasks for nutrition/training unless the owner explicitly asks. If the owner brings a concrete
      returned training/activity research conclusion, problem, or process-development request, resolve
      that new message against current NOW.md and the relevant knowledge boundary.

  live/health/knowledge/:
    add_file:
      path: live/health/knowledge/health-direction-os-tracking-boundary.md
      content: |
        # health-direction-os-tracking-boundary

        accepted_decision: |
          On 2026-06-28 the owner clarified the operating boundary for health Direction OS:

          "мы не трэкаем проекты если только я прямо не попрошу"

          Direction OS must not propose, poll, or track Health AI project/process execution cycles by default.
          Health AI can run nutrition/training work internally. If nutrition or training has problems, the owner
          will bring those problems separately.

          Direction OS remains responsible for:
          - process development;
          - architecture and state repair;
          - major decisions;
          - bounded issue routing;
          - summary-level state only when explicitly requested.

          Direction OS must not create routine tracking/execution bets such as "7 days of logging/testing" unless
          the owner explicitly asks for that kind of tracking.

        evidence:
          - owner message 2026-06-28: "мы не трэкаем проекты если только я прямо не попрошу"
          - owner message 2026-06-28: "если с nutrition или training будут проблемы мы отдельно будем решать"

        read_by:
          - all health sessions before proposing next work
          - shape when drafting any new bet
          - guide when routing owner-operated work
          - repair when NOW contains project-tracking open calls not explicitly requested by the owner

        END_OF_FILE: live/health/knowledge/health-direction-os-tracking-boundary.md

  live/health/LOG.md:
    append: |
      2026-06-28 — health/g-health-training-activity-system repair: owner approved minimal TREE cleanup replacing stale 8aa14f8/ACTIVE training/activity wording with current 1fe41c2/PROGRAM-awaiting-Deep-Research boundary; owner also clarified that Direction OS must not track Health AI projects/processes unless explicitly asked, so Health AI continues outside OS tracking and NOW.next becomes awaiting_owner_instruction. → history/2026-06-28-s-health-training-activity-tree-cleanup-001.md

  live/health/history/:
    add: |
      live/health/history/2026-06-28-s-health-training-activity-tree-cleanup-001.md containing this RESULT.

captures: []

decisions_needed: []

play_check:
  - "1 Name the contradiction: done — TREE still says training/activity has 8aa14f8 ACTIVE reduced authority/current-week/what-today projections, while NOW and knowledge say 1fe41c2 superseded that and training/activity is PROGRAM awaiting Deep Research. A second contradiction is behavioral: NOW open_calls/next were tracking Health AI research, while the owner clarified: 'мы не трэкаем проекты если только я прямо не попрошу'."
  - "2 Reconstruct: done — current authority reconstructed from NOW, TREE, knowledge boundary and recent repair/state-validation history; owner approval and boundary correction taken from the current owner messages."
  - "3 Propose corrected state: done — proposed minimal TREE prefix replacement, NOW removal of default tracking open calls, NOW.next awaiting_owner_instruction, and a knowledge boundary to prevent future unsolicited tracking proposals."
  - "4 Confirm: done — owner explicitly approved cleanup with 'давай отправим запрос на очистку TREE' and explicitly set the tracking boundary with 'мы не трэкаем проекты если только я прямо не попрошу'."
  - "5 Friction: done — no os/FRICTION.md change in this health repair; the owner rule is captured as health knowledge. If the same unsolicited tracking behavior recurs across directions, escalate to OS maintenance/friction."

log: |
  health/g-health-training-activity-system repair: TREE cleanup approved; stale 8aa14f8/ACTIVE wording replaced with 1fe41c2/PROGRAM-awaiting-research boundary; Direction OS no longer tracks Health AI projects/processes unless owner explicitly asks.

next: |
  awaiting_owner_instruction

  Do not propose tracking/execution-cycle tasks. Do not poll Health AI research status. Health AI continues outside Direction OS tracking. When the owner explicitly brings a returned conclusion, problem, or process-development request, handle that concrete request only.

END_OF_FILE: live/health/history/2026-06-28-s-health-training-activity-tree-cleanup-001.md
