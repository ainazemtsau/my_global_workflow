RESULT s-health-core-kernel-wa-k10-evidence-repair-001 (call: c-health-core-kernel-wa-k10-evidence-repair-001)
direction: health   play: repair   node/task: g-health-core

outcome: |
  Current health-ai main has a current-head canonical WA-K10 evidence package
  again.

  Product commit 8246cec19672bdd7eaadb2fec070a247088b6749 restored
  acceptance/kernel/journey-proof.md. The proof records the real historical
  repo journey f94351b -> 078d36d -> 78bad5a as SEED -> PROPOSED -> ACTIVE
  with commit, diff and re-read evidence; preserves the original fresh
  refutation 9a0124a; and explicitly treats the current nutrition
  program/cycle/week-plan/DAY_LOOP files as continuity evidence, not as a
  substitute journey claim.

  `python tools/check_kernel_spine.py` now reports WA-K10 GREEN on committed
  HEAD. A fresh in-session validator pre-pass first refuted the uncommitted
  draft as non-durable, then re-ran after commit 8246cec and returned
  SURVIVES-PREPASS.

  Because the carried option-A approval authorized closure after current-head
  WA-K10 GREEN, g-health-core is closed done. NOW has no active bet and routes
  next to c-health-training-activity-shape-001.

evidence: |
  Product repo C:\projects\health-ai:
  - commit: 8246cec19672bdd7eaadb2fec070a247088b6749
    (`Restore kernel journey proof evidence`)
  - changed file: acceptance/kernel/journey-proof.md only
  - `git cat-file -e HEAD:acceptance/kernel/journey-proof.md`: succeeds
  - `python tools/check_kernel_spine.py`: PASS; WA-K10 GREEN
  - `git status --short --branch`: `## main...origin/main [ahead 1]`
  - historical journey: f94351b status SEED; 078d36d status PROPOSED;
    78bad5a status ACTIVE
  - original proof/refutation: 679dd8d + 9a0124a
  - clean-slate deletion that created the gap: 8e981ec
  - current continuity evidence: x_nutrition/runtime/state-machine.md ACTIVE,
    x_nutrition/runtime/cursor.md DAY_LOOP, x_nutrition/index.md ACTIVE
    program/cycle/week-plan/fixed-menu/recipe-book list

  Independent refutation:
  - pre-commit validator: REFUTED because the proof was untracked and therefore
    not HEAD evidence; substantive journey claim otherwise held
  - post-commit validator: SURVIVES-PREPASS against 8246cec; refuted holes 0,
    survived 1, inconclusive 0
  - note: this is an in-session OpenAI-family pre-pass, not a separate
    cross-family OS G5 session; no cross-family hard gate was requested for this
    repair CALL.

  Owner approval carried by the CALL:
  - D-health-core-kernel-review-close-003 option A authorizes: current-head
    evidence repair, require WA-K10 GREEN plus fresh refutation, then approve
    g-health-core active -> done and replace the stale nutrition dirty/blocked
    preamble with current partial-progress reality.
  - The owner dispatched the prepared option-A repair CALL and requested the
    prepared training/activity shape CALL in return.

state_changes: |
  live/health/TREE.md:
  - owner_approved: true
  - approval_evidence: >
      Carried from D-health-core-kernel-review-close-003 option A by the owner
      dispatching c-health-core-kernel-wa-k10-evidence-repair-001.
  - For node g-health-core:
      prepend a DONE 2026-06-24 note naming health-ai 8246cec, WA-K10 GREEN,
      and WA-K6/WA-K8 breadth as follow-on;
      status: active -> done.
  - For node g-health-nutrition-system:
      replace the stale dirty-prototype/blocked preamble with current partial
      progress: thin Health AI domain, ACTIVE program, ACTIVE cycle, ACTIVE
      week plan, ACTIVE fixed menu, ACTIVE recipe book, cursor DAY_LOOP /
      selected family x_nutrition_day_log; node remains parked and minor
      papercuts ride r-health-ai-minor-fix-lane.

  live/health/NOW.md:
  - Replace active_bet with status none and a note that health-ai 8246cec
    restored current-head WA-K10 GREEN and g-health-core is closed.
  - Replace tasks with [].
  - Replace open_calls with [].
  - Preserve r-health-ai-minor-fix-lane and update its note to include
    fixed-menu/recipe support through 8246cec.
  - Replace decisions with [].
  - Replace next with CALL c-health-training-activity-shape-001.

  live/health/knowledge/health-core-kernel-review-evidence-gap.md:
  - Replace the blocking gap fact with a resolved fact naming health-ai 8246cec,
    WA-K10 GREEN, the restored journey chain, original fresh refutation, and a
    warning that future clean-slate resets must preserve/restore evidence or
    downgrade the precondition to PENDING.
  - Add resolved: 2026-06-24 and source:
    s-health-core-kernel-wa-k10-evidence-repair-001.

  live/health/LOG.md:
  - Append the log line from this RESULT.

  live/health/history/2026-06-24-s-health-core-kernel-wa-k10-evidence-repair-001.md:
  - Add this full RESULT.

captures:
  - check_kernel_spine.py can report overall PASS while WA-K10 is PENDING; future
    reviewers must read row statuses, not only process exit code.
  - Clean-slate resets that delete acceptance evidence can reopen a previously
    green precondition even when the underlying historical commits remain
    reproducible.

decisions_needed: []

play_check:
  - 1 Name the contradiction: done — current live state/material operation said
    kernel mostly works, but current health-ai HEAD lacked
    acceptance/kernel/journey-proof.md and WA-K10 was PENDING.
  - 2 Reconstruct: done — newest-first over NOW/TREE/LOG/history, health-ai
    commits, checker, historical journey commits, clean-slate deletion, and
    current nutrition artifacts.
  - 3 Propose corrected state: done — current-head proof restored in product;
    TREE/NOW/knowledge closure state prepared exactly around option A.
  - 4 Confirm: done — used the carried owner approval from
    D-health-core-kernel-review-close-003 option A; closure applied only after
    WA-K10 GREEN and post-commit validator SURVIVES-PREPASS.
  - 5 Friction: done — no OS rule change; recorded captures about checker exit
    status and clean-slate evidence lifecycle.

log: |
  2026-06-24 — health/g-health-core repair: current-head WA-K10 evidence repaired in health-ai @8246cec; acceptance/kernel/journey-proof.md restored, check_kernel_spine reports WA-K10 GREEN, fresh validator pre-pass survived; owner-approved option A closed g-health-core done and routed next to training/activity shape. → history/2026-06-24-s-health-core-kernel-wa-k10-evidence-repair-001.md

next: |
  CALL c-health-training-activity-shape-001
  to: session
  direction: health
  play: shape
  node: g-health-training-activity-system
  goal: |
    The next training/activity bet is small enough to execute and likely to
    improve real body outcomes.
  context: |
    g-health-core is closed done after current-head WA-K10 evidence repair.
    Product evidence:
    - health-ai commit 8246cec19672bdd7eaadb2fec070a247088b6749 restored
      acceptance/kernel/journey-proof.md.
    - `python tools/check_kernel_spine.py` reports WA-K10 GREEN.
    - Fresh in-session validator pre-pass post-commit returned
      SURVIVES-PREPASS for the WA-K10 proof package.

    Owner approval carried by the repair CALL:
    - D-health-core-kernel-review-close-003 option A: repair current-head
      WA-K10 evidence, then approve g-health-core active -> done and replace the
      stale g-health-nutrition-system dirty/blocked preamble with current
      ACTIVE-program/cycle/week-plan, DAY_LOOP partial-progress reality.
    - D-health-next-large-bet-003 prepared route: shape
      g-health-training-activity-system next.

    Current health-ai nutrition state has an ACTIVE program, cycle, week plan,
    fixed menu and recipe book with cursor DAY_LOOP. Minor Health AI papercuts
    remain in r-health-ai-minor-fix-lane rather than expanding this bet.
    Carry D-kernel-1 and the strongest WA-K8 second-domain test as explicit
    shape inputs, not automatic scope.
  boundaries: |
    Do not implement training. Do not author Health AI artifacts. Do not reopen
    kernel breadth by default. Keep raw workout/activity logs out of Direction OS.
  done_when: |
    An owner-approved training/activity bet has appetite, kill_by, real cut
    list, verdict for every CHARTER lens, a task testing the riskiest
    assumption first, no more than three active tasks, and a ready first CALL.
  return: |
    RESULT with owner-approved TREE/NOW state_changes and the next execution
    CALL.
  budget: one session

END_OF_FILE: live/health/history/2026-06-24-s-health-core-kernel-wa-k10-evidence-repair-001.md
