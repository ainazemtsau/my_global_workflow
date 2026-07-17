CALL c-exec-char-v2-reaction-core-repair-admission-003
to: executor
direction: indie-game-development
track: characters
repo: ainazemtsau/GasCoopGame
kind: engineering
node: g-6d4e
parent: c-exec-char-v2-body-rig-ragdoll-build-001

goal: |
  В2 Leg 1 имеет честное, готовое к отдельной binding-проверке закрытие полного класса
  «незагейтованный посев»: readiness возникает только из законного provenance, а inner-state во время
  реакции не влияет на авторитетную позу или ручательство о ней.

context: |
  READY after the owner verdict recorded in
  history/2026-07-17-s-work-char-v2-repair-reservation-authorized-001.md. The owner's exact words were
  «Тогда разрешать пройть запись.» in reply to the A/B/C route question. In that immediate context this
  authorizes option A only: one service registry-reservation record may be committed, pushed to the current
  origin/dev tip and confirmed by fresh readback. This is admission plumbing, not publication of the repair.

  repair-002 закончился evidence-checkpoint до первой product-записи:
  history/2026-07-17-s-work-char-v2-reaction-core-repair-002-admission-blocked-001.md.
  Current product authority требует committed+pushed+fresh-read-back registry reservation на current
  origin/dev tip; локальная или uncommitted row не admission. Исходный CALL запрещал любой push,
  поэтому product diff/commit/candidate/gates/review остались нулевыми. Saved ACTIVE-EXCEPTION WIP сохранён
  content-addressed capsule + archival refs и не владеет slot/mutation authority.

  Полный invariant не меняется: pose законна, только если она sampled while reactions were Normal или
  received as restPose through GetUp; без такой pose wrapper not ready. Lawful Origin остаётся valid;
  value sniffing запрещён.

  Read current product AGENTS.md and canonical registry first; they alone assign venue, branch/path/SHA, Editor
  identity and lifecycle. Direction evidence:
  - knowledge/g6d4e-char-v2-leg1-reaction-core.md
  - work/c-plan-characters-002-plan.md
  - work/gascoopgame-worktree-protocol-v2.md
  - history/2026-07-17-s-work-characters-resume-a1.md

boundaries: |
  До source/test mutation разрешена ровно одна внешняя service mutation: создать одну reservation-запись
  в canonical product registry, сделать registry-only commit, push этого commit в current origin/dev и fresh
  fetch/readback точного reservation state. Никакой другой push этим CALL не разрешён. Если current product
  authority не может оформить admission в этих пределах без cleanup, topology redesign, дополнительных service
  commits/pushes или иной мутации, STOP с evidence. После подтверждённого admission локальные repair diff/commit,
  gates и read-only review разрешены только в пределах goal/done_when; candidate остаётся unpushed.

  Preserve frozen authoritative-body seam and confirmed reaction/state-machine behavior. Do not add movement or
  authority source, fix DF-13, build rig/ragdoll/locomotion, touch gas/network/core, clean legacy worktrees,
  integrate/publish candidate branches or open Leg 2. Saved work is evidence input, never launch authority.

done_when: |
  1. Full provenance invariant holds for both hostile orderings and construction over an already-reacting body;
     lawful Normal sampling and lawful Origin still work.
  2. Recorded pre-fix evidence fails and distinguishes the candidate; a suite green on both is not proof.
  3. Current product-native build/test/delivery gates are green and the frozen character seam is evidenced unchanged.
  4. F3/S8 is corrected or explicitly routed without a false self-healing claim; DF-13 and the known throw/stray-GetUp
     latent boundaries are named honestly.
  5. A fresh read-only product review attempts to refute the repaired invariant and records class+sweep evidence under
     current model-neutral rules.
  6. The product RESULT reconciles every item above and returns exact evidence pointers without merging, pushing the
     candidate, opening Leg 2 or declaring Direction close.

return: |
  Product RESULT plus exact commit/diff, gate and review evidence. Return to Direction as a checkpoint; Direction
  opens a separate fresh binding-G5 successor under the same parent before the body-rig root can become ready.

budget: one focused continuation leg; stop if admission needs cleanup/topology redesign or scope expansion

END_OF_FILE: live/indie-game-development/work/c-exec-char-v2-reaction-core-repair-admission-003-call.md
