# health-core-kernel-review-evidence-gap

accepted: 2026-06-23
fact: >
  A kernel acceptance precondition is current-head evidence, not only a
  historical event. This gap was resolved on 2026-06-24: health-ai commit
  8246cec19672bdd7eaadb2fec070a247088b6749 restored the canonical
  acceptance/kernel/journey-proof.md package to current main, preserving the
  real historical SEED->PROPOSED->ACTIVE chain (f94351b -> 078d36d ->
  78bad5a), the original fresh refutation (9a0124a), and current operational
  continuity evidence through ACTIVE nutrition program/cycle/week-plan and
  DAY_LOOP. `tools/check_kernel_spine.py` now reports WA-K10 GREEN. Future
  clean-slate resets must either preserve/restore acceptance evidence packages
  in the same leg or explicitly downgrade the affected precondition to PENDING.
read_by:
  - play: review
    when: closing or auditing g-health-core kernel and follow-on kernel breadth bets
  - play: shape
    when: shaping training/activity or another second-domain attach on the Health AI kernel
  - play: repair
    when: reconciling Health AI evidence drift after clean-slate resets or product handoffs
reverified: 2026-06-24
resolved: 2026-06-24
source: s-health-core-kernel-wa-k10-evidence-repair-001

END_OF_FILE: live/health/knowledge/health-core-kernel-review-evidence-gap.md
