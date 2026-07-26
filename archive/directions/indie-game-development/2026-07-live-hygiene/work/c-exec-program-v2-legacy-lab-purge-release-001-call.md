# CALL c-exec-program-v2-legacy-lab-purge-release-001

to: executor
direction: indie-game-development
track: program
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: legacy-lab-purge-release
issued: 2026-07-20 (s-work-program-v2-legacy-lab-purge-deliver-blocked-001)

goal: |
  The already validated legacy-lab cleanup candidate is published with exact remote readback, the V31 root is
  RELEASED, and WIN-U1 is free for feature work without changing the frozen cleanup candidate.

context: |
  This is the same-leg release continuation of `c-exec-program-v2-legacy-lab-purge-001`, not new cleanup work.
  Dispatch only after `unblock_when` is true. The product candidate is
  `72c7c8c6340064e6acb80358960518ebc433f820`, BUILD receipt
  `d58f54cdc30ce9411b98a1b917272db868c7626b`, validated/frozen handoff
  `c5c21c13a66744649fb5faf4c50ad5e76a6835b2`, and blocker-evidence commit
  `baf8513caa691a3fcbdebddde6b4feb6aa278108`. Candidate tree is
  `2541656dc3fa0597281115e0660bd534e9c1c0e8`.

  Fresh non-author G5 reported CONFIRMED / NO FINDINGS. Normal gates were GREEN at 1829/1829 and the
  standalone solution was GREEN at 1946/1946. The root is currently NOT RELEASED: local dev is clean at
  `baf8513c`; main, origin/main and origin/dev remain at
  `45b15623120f395b4295e43ac6cc5ed0c3aa108c`; no push or merge occurred; WIN-U1 is DRAINING with its
  closing lease preserved. Product evidence is recorded at
  `docs/results/c-exec-program-v2-legacy-lab-purge-001.md`.

  Deliver was RED solely because pre-existing
  `docs/reviews/review-c-exec-char-v2-source-router-repair-001.md` did not account for source commit
  `413149ce` after reviewed commit `8a0e33ec`. That defect existed on the audit base and belongs to the
  Character lineage. This continuation becomes runnable only when that external evidence is lawfully closed and
  `tools/check.ps1 -Deliver` can be GREEN on the preserved cleanup lineage.

boundaries: |
  Do not modify, rebuild, amend, rebase or expand the frozen cleanup candidate. Do not repair or rewrite the
  Character review/evidence lineage or gate authority in this root. Do not add feature work, Integration Lab,
  retained-scene consumers, migration/shim/framework code or new scope. Do not publish if Deliver is RED, remote
  refs have moved incompatibly, exact candidate/readback cannot be proven, or the V31 closing lease is not valid;
  return one exact ESCALATE blocker instead. Use the preserved V31 lifecycle and serialized Control route.

done_when: |
  1. The pre-existing Character review-evidence defect is closed outside this root and the unchanged preserved
     cleanup lineage passes the complete V31 Deliver gate.
  2. The released product tree contains exactly the validated cleanup candidate: all 24 approved tracked paths are
     absent, retained/KEEP hashes and the no-growth authority remain unchanged, and no extra product change rides it.
  3. Publication follows the installed V31 closing lifecycle; exact remote readback identifies the released SHA and
     tree, all required root/registry/dashboard mirrors agree, and the final product worktree is clean.
  4. WIN-U1 is released only after successful publication/readback; the returning HOME states whether feature work
     may resume and carries exact commands/results, refs, commits, manifest and lease disposition.

return: |
  One gated V31 REPORT/RELEASED HOME with exact publication/readback and slot-release evidence, or one genuine
  ESCALATE HOME naming the single blocker while preserving custody. No new feature CALL is created by the executor.

budget: <=0.25 focused day after unblock_when
surface: any
engineering_contract: 31

END_OF_FILE: live/indie-game-development/work/c-exec-program-v2-legacy-lab-purge-release-001-call.md
