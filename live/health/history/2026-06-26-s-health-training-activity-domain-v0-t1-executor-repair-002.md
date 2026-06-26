RESULT s-health-training-activity-domain-v0-t1-executor-repair-002 (call: c-health-training-activity-domain-v0-t1-executor-001)
direction: health   play: repair   node/task: g-health-training-activity-system/t-1

outcome: |
  Prior repair RESULT is superseded because it still failed writer G10:
  `play: repair` was declared, but `play_check` did not contain one line for each
  required step of `os/plays/repair.md`.

  Corrected durable state intent:
  - t-1 remains `active`.
  - t-1 gets an explicit blocker and unblock_when.
  - NOW.next is replaced with an outcome-only executor CALL.
  - The candidate patch remains context-only HOW input, not a goal or state claim.
  - No product implementation is claimed done until Health AI has commit/PR evidence,
    changed-HEAD check output, and an acceptance matrix.
  - `play_check` now maps explicitly to the five repair steps:
    Name contradiction, Reconstruct, Propose corrected state, Confirm, Friction.

evidence: |
  Writer rejection supplied by owner:
  - First rejection: state_changes was not mechanically exact; it did not say whether
    t-1 stays active or becomes blocked; it lacked exact unblock_when; it did not
    say how to replace NOW.next; next.goal violated CALL hygiene by starting with
    method wording "Apply or rework...".
  - Second rejection: the corrected RESULT declared `play: repair`, but `play_check`
    did not contain one line per `os/plays/repair.md` step. Required repair steps:
    Name contradiction, Reconstruct, Propose corrected state, Confirm, Friction.
  - Files were not changed and no commit was created.
  - Candidate patch SHA-256 remains intact and matches:
    f9d1fb677f5831d6f44fa5484d25a677add591dc8670b0ff4e20d8a54732c6ec.

  Corrective evidence in this RESULT:
  - t-1 status is explicitly `active`.
  - blocker and unblock_when are exact task-level fields.
  - NOW.next replacement is exact.
  - next.goal is outcome-only.
  - Patch is referenced only in next.context.
  - play_check has exactly one line for each of the five repair steps.

state_changes: |
  Apply the following exact Direction OS edits.

  1) File: live/health/NOW.md
     Section: tasks
     Target task: `id: t-1`

     Keep this existing field exactly as:
       status: active

     Add the following task-level fields immediately after the existing `evaluator: >`
     paragraph of task `t-1` and before the next task item `- id: t-2`.
     If fields named `blocker` or `unblock_when` already exist under task `t-1`,
     replace their full values with this exact text:

       blocker: >
         t-1 product implementation is not durably applied in ainazemtsau/health-ai:
         no Health AI commit or PR exists for the training/activity t-1 slice, no
         changed-HEAD check output exists, and current committed Health AI state has
         no x_training_activity thin-domain attach, dynamic evidence-backed program
         proposal path, current-week slice path, or today session brief path.
       unblock_when: >
         A code-assistant executor returns Health AI product evidence for t-1:
         commit or PR, changed files, `python tools/check_kernel_spine.py` output,
         and an acceptance matrix showing done_when items 1-10 satisfied or naming
         the first remaining blocker. Only after that evidence exists may a separate
         verifier try to refute t-1 for done.

  2) File: live/health/NOW.md
     Section: open_calls

     Leave this section exactly as:
       open_calls: []

     Do not add the continuation CALL to open_calls. The ready continuation is
     stored only in NOW.next.

  3) File: live/health/NOW.md
     Section: next

     Replace the entire existing `next: |` block with this exact block:

       next: |
         CALL c-health-training-activity-domain-v0-t1-executor-002
         to: executor
         direction: health
         node: g-health-training-activity-system
         task: t-1
         repo: ainazemtsau/health-ai
         kind: engineering
         goal: |
           Health AI has committed product evidence for the t-1 training/activity
           thin-domain v0 slice: x_training_activity is attached over the existing
           kernel, program creation is dynamic and evidence-backed, setup questions
           are material and irreducible, proposed training authority rides the
           existing gate, and ACTIVE authority can produce a current-week slice and
           today's session brief without duplicating kernel engine behavior.
         context: |
           Prior executor attempt produced no Health AI commit or PR. It prepared a
           context-only candidate patch:
           - path: /mnt/data/health_ai_training_activity_t1_candidate.patch
           - sha256: f9d1fb677f5831d6f44fa5484d25a677add591dc8670b0ff4e20d8a54732c6ec
           - status: HOW-only candidate input, not authority and not required if the
             executor finds a cleaner implementation.

           The executor must reload Health AI from committed repo state before making
           any product claim. The current known blocker is lack of durable product
           evidence: no commit/PR and no changed-HEAD check output exist for t-1.

           Preserve Direction OS and product acceptance already signed for this bet:
           - W1 thin training domain.
           - W2 canonical Health AI training authority.
           - W3 system-decided programming with only materially missing irreducible
             owner facts asked.
           - W4 session brief / "training today".
           - W7 mechanical safety brake.
           - W8 reduced/bad-week return.
           - W17 Direction OS boundary.
           - W18 D-kernel-1 registry-line control-plane decide-and-inform.
           - W20 setup-proven versus body-proven split.
           - TA-CA1, TA-CA2, TA-CA3 must be satisfied.
           - TA-CA8 and TA-CA9 must not be contradicted.
           - P1-P3/P8/P9/P10/P12 remain HOW/PLAN input, not Direction OS state.
         boundaries: |
           Do not modify Direction OS state.
           Do not store raw workout/activity/pulse/wearable data, native exports,
           screenshots, or daily session details in Direction OS.
           Do not build or require direct API integrations for Hevy, Strava, Apple
           Health, Apple Fitness, VR, or wearable tools.
           Do not build shared body-measurements protocol, dashboard/trend UI, or
           full WA-K8 proof in this task.
           Do not prescribe concrete workout programming in the Direction OS CALL;
           Health AI product behavior must create any program from evidence,
           owner/core facts, and current Health AI state.
           Do not duplicate kernel engine behavior: no second router, lifecycle,
           gate, writer barrier, job model, scheduler, server, database, background
           worker, or module-specific engine.
           Do not weaken W1-W20, TA-CA1..TA-CA12, setup/body evidence split,
           D-kernel-1, or the WA-K8 later-proof route.
           Do not start t-2 breadth work.
         done_when: |
           Product evidence shows:
           1. Training/activity attaches as a thin domain over the existing kernel:
              namespaced data, one registry-line control-plane attach, one
              state-machine instance, one cursor instance, one bounded procedure per
              term/stage as needed, and zero duplicated router/lifecycle/gate/writer/
              job model/scheduler/server/database/background worker.
           2. Health AI can create a training/activity program proposal from current
              owner/core facts and current external evidence. It does not use a
              hardcoded research template, fixed question script, fixed program
              template, fixed schedule, split, volume, intensity, vendor, or intake
              form. The system determines what evidence/deep-research pass is
              required for the artifact being created; for the training program this
              must include current evidence sufficient to justify the plan for the
              owner's profile, goals, constraints, safety, adherence, equipment and
              phase.
           3. Setup asks dynamically only for materially missing irreducible owner
              facts; it may ask freely when useful but does not block on nonessential
              answers, records defaults/assumptions as revisable where allowed, and
              never asks the owner to design expert variables. Exercise selection,
              split, volume, intensity, conditioning mix, progression, regression and
              deload logic are system-decided from evidence + owner profile + current
              phase + constraints + feedback.
           4. The proposed training authority can ride the existing
              SEED/PROPOSED/ACTIVE gate and is readable for owner approval; it records
              evidence/rationale, owner facts used, defaults/assumptions, safety
              constraints and extension points for arbitrary schedules, constraints,
              equipment, preferences and other material nuances.
           5. From ACTIVE authority, Health AI can generate a current-week
              training/activity slice and a readable "what today?" session brief for
              contexts such as home/gym/bike/VR/low-time/fatigue, without requiring
              the owner to read internal files.
           6. Session brief includes purpose, ordered work, planned effort,
              warm-up/prep, permitted substitutions, technique/safety cues, required
              result signals, reduced/bad-week branch and mechanical safety brake
              behavior.
           7. W1 thin training domain, W2 canonical Health AI training authority,
              W3 system-decided programming, W4 session brief, W7 mechanical safety
              brake, W8 reduced/bad-week return, W17 Direction OS boundary,
              W18 D-kernel-1, W20 setup/body evidence split are preserved.
           8. TA-CA1, TA-CA2 and TA-CA3 are satisfied; TA-CA8/TA-CA9 are not
              contradicted.
           9. P1-P3/P8/P9/P10/P12 remain PLAN/HOW input, not Direction OS state.
           10. Return includes commit/PR evidence, changed files, check output, and a
               blocker note before breadth work.
         return: |
           RESULT with:
           - outcome: what Health AI training/activity t-1 can now do;
           - evidence: commit/PR, changed files, `python tools/check_kernel_spine.py`
             output, and an acceptance matrix against done_when items 1-10;
           - explicit statement whether t-2 can proceed or which blocker must be
             repaired first.
         budget: one executor task, bounded to t-1 only

  4) File: live/health/LOG.md
     Append exactly one log line:

     2026-06-26 — health training/activity t-1 executor repair: prior RESULT was not applied; t-1 remains active with explicit blocker/unblock_when and corrected outcome-only continuation CALL; repair play_check now covers all five repair steps.

  5) File: live/health/history/
     Add a new history file:
       live/health/history/2026-06-26-s-health-training-activity-domain-v0-t1-executor-repair-002.md

     File content:
       this full RESULT block.

captures: []

decisions_needed: []

play_check:
  - 1 Name contradiction: done — contradiction named from owner report: prior RESULT declared `play: repair` but its `play_check` had four non-repair-specific lines instead of the five required repair play steps.
  - 2 Reconstruct: done — reconstructed current state from owner report: writer changed no files, no commit exists, candidate patch SHA remains intact, and the intended Direction OS repair is still unapplied.
  - 3 Propose corrected state: done — proposed mechanical state edits: keep t-1 `active`, add exact blocker/unblock_when, leave `open_calls: []`, replace `NOW.next` with an outcome-only executor CALL, append one LOG line, and add this history file.
  - 4 Confirm: done — no owner confirmation was required because this repair only corrects writer-rejected RESULT mechanics and preserves the previously requested outcome; owner explicitly requested a corrected RESULT/state_changes or repair RESULT.
  - 5 Friction: done — friction recorded in evidence/log: RESULT packets for repair must enumerate the exact five repair play steps; vague or ad hoc play_check labels are writer-rejected under G10.

log: >
  health training/activity t-1 executor repair: second G10 defect fixed; repair
  RESULT now includes exact five-step repair play_check and preserves exact
  t-1 blocker/unblock_when plus outcome-only NOW.next executor CALL.

next: |
  CALL c-health-training-activity-domain-v0-t1-executor-002
  to: executor
  direction: health
  node: g-health-training-activity-system
  task: t-1
  repo: ainazemtsau/health-ai
  kind: engineering
  goal: |
    Health AI has committed product evidence for the t-1 training/activity
    thin-domain v0 slice: x_training_activity is attached over the existing
    kernel, program creation is dynamic and evidence-backed, setup questions
    are material and irreducible, proposed training authority rides the
    existing gate, and ACTIVE authority can produce a current-week slice and
    today's session brief without duplicating kernel engine behavior.
  context: |
    Prior executor attempt produced no Health AI commit or PR. It prepared a
    context-only candidate patch:
    - path: /mnt/data/health_ai_training_activity_t1_candidate.patch
    - sha256: f9d1fb677f5831d6f44fa5484d25a677add591dc8670b0ff4e20d8a54732c6ec
    - status: HOW-only candidate input, not authority and not required if the
      executor finds a cleaner implementation.

    The executor must reload Health AI from committed repo state before making
    any product claim. The current known blocker is lack of durable product
    evidence: no commit/PR and no changed-HEAD check output exist for t-1.

    Preserve Direction OS and product acceptance already signed for this bet:
    W1, W2, W3, W4, W7, W8, W17, W18, W20; TA-CA1, TA-CA2, TA-CA3; do not
    contradict TA-CA8/TA-CA9; keep P1-P3/P8/P9/P10/P12 as HOW/PLAN input.
  boundaries: |
    Do not modify Direction OS state.
    Do not store raw workout/activity/pulse/wearable data, native exports,
    screenshots, or daily session details in Direction OS.
    Do not build or require direct API integrations for Hevy, Strava, Apple
    Health, Apple Fitness, VR, or wearable tools.
    Do not build shared body-measurements protocol, dashboard/trend UI, or full
    WA-K8 proof in this task.
    Do not prescribe concrete workout programming in the Direction OS CALL.
    Do not duplicate kernel engine behavior.
    Do not weaken W1-W20, TA-CA1..TA-CA12, setup/body evidence split,
    D-kernel-1, or the WA-K8 later-proof route.
    Do not start t-2 breadth work.
  done_when: |
    Product evidence shows:
    1. Training/activity attaches as a thin domain over the existing kernel.
    2. Health AI can create a training/activity program proposal from owner/core
       facts and current evidence without hardcoded research/question/program
       templates or fixed schedule/split/volume/intensity/vendor/intake form.
    3. Setup asks dynamically only for materially missing irreducible owner facts.
    4. Proposed training authority rides the existing SEED/PROPOSED/ACTIVE gate.
    5. From ACTIVE authority, Health AI can generate current-week slice and
       "what today?" brief.
    6. Session brief includes purpose, ordered work, effort, prep, substitutions,
       cues, result signals, reduced/bad-week branch and mechanical safety brake.
    7. W1/W2/W3/W4/W7/W8/W17/W18/W20 are preserved.
    8. TA-CA1, TA-CA2 and TA-CA3 are satisfied; TA-CA8/TA-CA9 are not contradicted.
    9. P1-P3/P8/P9/P10/P12 remain PLAN/HOW input, not Direction OS state.
    10. Return includes commit/PR evidence, changed files, check output, and
        blocker note before breadth work.
  return: |
    RESULT with outcome, commit/PR, changed files, `python tools/check_kernel_spine.py`
    output, acceptance matrix against done_when items 1-10, and explicit statement
    whether t-2 can proceed.
  budget: one executor task, bounded to t-1 only

END_OF_FILE: live/health/history/2026-06-26-s-health-training-activity-domain-v0-t1-executor-repair-002.md
