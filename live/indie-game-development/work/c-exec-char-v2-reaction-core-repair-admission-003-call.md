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
  BLOCKED / NOT DISPATCHABLE pending decision d-char-v2-repair-admission-route-001.

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
  Этот packet заблокирован и сам не разрешает registry push. Сначала нужны фактические слова владельца
  по d-char-v2-repair-admission-route-001 и отдельный Direction RESULT, который либо узко обновит boundaries и сделает CALL
  ready, либо оставит его blocked/paused. До этого не менять product repo.

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

budget: one focused continuation leg after the owner route verdict; stop if admission needs cleanup/topology redesign or scope expansion

END_OF_FILE: live/indie-game-development/work/c-exec-char-v2-reaction-core-repair-admission-003-call.md
