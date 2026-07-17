CALL c-exec-char-v2-reaction-core-repair-002
to: executor
direction: indie-game-development
track: characters
repo: ainazemtsau/GasCoopGame
kind: engineering
node: g-6d4e
parent: c-exec-char-v2-body-rig-ragdoll-build-001

goal: |
  В2 Leg 1 имеет честное, готовое к отдельной binding-проверке закрытие полного класса
  «незагейтованный посев»: источник сообщает готовность позы только при законном provenance,
  а состояние inner во время реакции не может влиять на авторитетную позу или ручательство о ней.

context: |
  Read current product AGENTS.md and the canonical worktree registry first; they alone assign
  admitted venue, branch/path/SHA, editor identity and integration lifecycle.

  Direction evidence and accepted scope:
  - live/indie-game-development/knowledge/g6d4e-char-v2-leg1-reaction-core.md
  - live/indie-game-development/work/c-plan-characters-002-plan.md
  - live/indie-game-development/work/gascoopgame-worktree-protocol-v2.md
  - live/indie-game-development/history/2026-07-17-s-work-characters-resume-a1.md

  The complete invariant is provenance-based: readiness is valid only after a pose was sampled
  while reactions were Normal or received as the rest pose through GetUp. With no such pose the
  wrapper is not ready. A lawful pose at Origin remains valid; value sniffing is forbidden.

  The saved product work is an ACTIVE-EXCEPTION input, not launch authority. The product protocol
  decides whether it can be admitted/preserved/reused or whether the leg must stop. The owner chose
  the narrow repair option A; this does not authorize Leg 2, merge, push or cleanup.

boundaries: |
  Preserve the frozen authoritative-body seam and the already confirmed reaction/state-machine
  behavior. Do not add a new movement or authority source, fix DF-13, build rig/ragdoll/locomotion,
  touch gas/network/core behavior, clean legacy worktrees, or integrate/publish product branches.
  Do not treat a historical path, branch, SHA, dirty file or model family as authority or a gate.
  If current product admission cannot preserve the saved work losslessly, stop with evidence.

done_when: |
  1. The full provenance invariant holds for both hostile orderings and construction over an
     already-reacting body, while lawful Normal-state sampling and a lawful Origin pose still work.
  2. Recorded pre-fix evidence distinguishes the failing state from the candidate; a suite that is
     green on both is not accepted as proof.
  3. The current product-native build/test/delivery gates required for this admitted leg are green,
     and the frozen character seam is evidenced unchanged.
  4. The previously refuted F3/S8 disposition is corrected or explicitly routed without a false
     self-healing claim; DF-13 and the known throw/stray-GetUp latent boundaries are named honestly.
  5. A fresh read-only product review attempts to refute the repaired invariant and records
     class+sweep evidence under current model-neutral review rules.
  6. The product RESULT reconciles every item above and returns exact evidence pointers without
     merging, pushing, opening Leg 2 or declaring Direction close.

return: |
  Product RESULT plus exact commit/diff, gate and review evidence. Return to Direction as a
  checkpoint; Direction must open a separate fresh binding-G5 successor under the same parent
  before the body-rig root can become ready.

budget: one focused continuation leg; stop if admission requires cleanup/topology redesign or the repair expands beyond the bounded invariant class

END_OF_FILE: live/indie-game-development/work/c-exec-char-v2-reaction-core-repair-002-call.md
