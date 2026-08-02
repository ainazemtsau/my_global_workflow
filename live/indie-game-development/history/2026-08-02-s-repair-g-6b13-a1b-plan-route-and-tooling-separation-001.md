# RESULT — s-repair-g-6b13-a1b-plan-route-and-tooling-separation-001

call: c-exec-rules-layer-and-single-walker-001
direction: indie-game-development
track: переноска
play: repair
node/task: g-6b13/a-1b
date: 2026-08-02

## outcome

PLAN and ADR-E-0019 are recorded as accepted by content, while a-1b remains blocked and no BUILD
authority exists. The Direction frontier now reflects the actual product line: the feature root waits
on separate task c-1b and its independent tooling child, which publishes the `ad42b2d8` fix outside
the feature diff. The
already approved host lane has a blocked root but cannot start while a-1b is the owner's sole current
task.

Hot routing is schema-shaped: two owner-approved tracks have a WIP limit and `for` targets; each has
one root; the carrying root has one acyclic same-track child; answered decisions and terminal CALLs
are no longer presented as live dispatch.

## evidence

- Owner verdict, exact: “PLAN и ADR-E-0019 по содержанию принимаю. BUILD пока не запускать:
  сначала исправить Direction-маршрут и отделить ad42b2d8 от задачи a-1b.” This accepts content and
  explicitly withholds BUILD.
- Product history in clean `GasCoopGame_win-u3`: `7c5fc5a6` freezes PLAN/spec/ADR on parent
  `c75015a8`; `ad42b2d8` is its child and changes only `tools/root-lifecycle-check.ps1`;
  `f7387751` is the child of `ad42b2d8` and adds PLAN receipts. U3 is clean, AVAILABLE, lease none.
- `ad42b2d8` is not in actual product main: fresh product `main`/`origin/main` are `c75015a8`, and
  `git branch -a --contains ad42b2d8` names only `slot/win-u3`. Thus it cannot truthfully be treated
  as either published tooling or feature work.
- Contract 35 authority in product `AGENTS.md` names the compiled route PLAN → PAIR-CANDIDATE →
  binding fresh PAIR-FREEZE → fresh BUILD; v30+ roots return HOME only at terminal REPORT or genuine
  ESCALATE. The old CALL text jumped from PLAN straight to BUILD and NOW marked it `ready`.
- Owner's earlier routing words are exact enough for the two structural facts retained here: “две я
  вижу точно” established two tracks; “Сейчас у меня в работе, ну только одна задача” and the stated
  intent to start parallel work after it passes justify a blocked, not runnable, host root.
- Fresh U2 evidence reverses the previous hot issue: U2 is clean and AVAILABLE at `c75015a8` with no
  lease. Only the missing named backup-ref remains; `e0000c5b` and `955e5e62` still resolve by SHA.

## state_changes

- `NOW.md`: a-1b `open → blocked`, with the exact owner checkpoint and unblock condition; create
  separate active task c-1b for the tooling publication, rather than counting it as a-1b feature
  work; set b-1 `open → blocked` until the owner-declared sequencing gate; set `track_wip_limit: 2`; add
  `label` and `for: g-6b13` to tracks `переноска` and `хозяин`.
- `NOW.md/open_calls`: keep `c-exec-rules-layer-and-single-walker-001` as the carrying root but set it
  to `waiting` on child `c-ctrl-publish-root-lifecycle-singleton-fix-001`; register that same-track
  child `ready` for separate task c-1b; register `c-work-host-walker-frontier-001` as the one host root `blocked` until a-1b
  has owner Play plus binding fresh G5 close evidence.
- Remove five terminal `done|dead` CALL rows from hot `open_calls`; their files, commits, LOG entries
  and history remain evidence. Replace five answered decision rows with `decisions: []`; their answers
  remain in bet/TREE/history and no owner choice is lost.
- Revise `work/c-exec-rules-layer-and-single-walker-001-call.md` to revision 3: record the owner's
  acceptance/hold, correct `lane` to `track`, prohibit automatic launch, and restore the v35 route
  through fresh PAIR-CANDIDATE/PAIR-FREEZE before BUILD and terminal HOME semantics.
- Add self-contained CALLs
  `work/c-ctrl-publish-root-lifecycle-singleton-fix-001-call.md` and
  `work/c-work-host-walker-frontier-001-call.md`.
- Replace stale issue `i-slot-u2-held-by-dead-lease-001` with the narrower
  `i-slot-u2-backup-ref-missing-after-cleanup-001`; refresh
  `i-slots-carry-old-contour-until-updated-001` from current slot evidence. Remove resolved
  `i-plan-and-adr-flow-back-on-for-building-001` and
  `i-gate-cut-not-merged-speedup-not-in-effect-001`: PLAN/ADR are now present and the gate cut is on
  main. Register `i-now-hot-file-over-ceiling-001` so the remaining 150-line hot-file violation has
  an explicit separate repair route rather than being hidden.
- Prepend this receipt to `LOG.md`; append one OS-hole observation to `os/FRICTION.md`. No CHARTER,
  TREE, knowledge, archive, or product-repository bytes are changed.

## captures

- `7c5fc5a6` and `f7387751` must remain exact accepted PLAN evidence; separation is by independent
  main publication plus incorporating current main, not by rewriting frozen history.
- U2 cleanup succeeded operationally, but the absent named backup-ref remains a recoverability choice
  for a later control leg; it does not block current work.
- NOW compaction is real debt and cannot be disguised as this route repair; Git/history permit a
  later lossless pointer-only compaction.

## decisions_needed

None.

## play_check

- 1 name the contradiction: done — owner withheld BUILD and requested separation, while NOW marked
  the mixed product root `ready` and its CALL jumped PLAN → BUILD.
- 2 reconstruct: done — reread fresh NOW/TREE/CHARTER/LOG/history, all roots/lanes/decisions/issues,
  product commit graph, slot registry, worktree cleanliness, and current product contract.
- 3 propose corrected state: done — every route change above has a one-line factual reason; no
  product progress or Direction close was invented, and removed hot rows retain evidence.
- 4 confirm (owner): done — content acceptance and BUILD hold cite the owner's exact current words;
  the WIP/two-lane and blocked-host facts cite his earlier exact words. No CHARTER/TREE semantic
  change and no lane is created or retired.
- 5 friction: done — recorded the writer-path hole that allowed a NOW-only, no-history repair to be
  born invalid and stale immediately; no OS rule is changed in this Direction leg.

## log

g-6b13/a-1b: PLAN и ADR приняты по содержанию; BUILD удержан, ad42b2d8 вынесен в отдельный tooling-child, две полосы получили законные корни и WIP=2

## next

CALL c-ctrl-publish-root-lifecycle-singleton-fix-001
to: executor
direction: indie-game-development
track: переноска
node: g-6b13
task: c-1b
parent: c-exec-rules-layer-and-single-walker-001
repo: ainazemtsau/GasCoopGame
kind: engineering
engineering_contract: 35
status: ready
goal: publish the reviewed singleton-frozen-entry fix independently on actual main and make U3's
feature diff contain no tooling change while preserving `7c5fc5a6` and `f7387751`
boundaries: no gameplay, Unity, PLAN rewrite, PAIR-CANDIDATE, PAIR-FREEZE, BUILD, VALIDATE, or
feature REPORT; on inability to preserve accepted commits, ESCALATE HOME
done_when: actual origin/main has the standalone fix with GREEN checks; U3 incorporates that main
without tools/validation/checker feature diff; touched slots are clean/released with exact evidence
return: HOME to parent with main/U3 SHAs, ancestry/scoped diff, checks and lease state; do not launch
the parent
budget: one control leg, no feature work
call_file: live/indie-game-development/work/c-ctrl-publish-root-lifecycle-singleton-fix-001-call.md

END_OF_FILE: live/indie-game-development/history/2026-08-02-s-repair-g-6b13-a1b-plan-route-and-tooling-separation-001.md
