RESULT s-repair-launch-control-demo-control-room-unblock-001 (call: owner-goal-continuation-2026-07-22-demo-control-room-unblock)
direction: indie-game-development   track: launch-control   play: repair   node/task: g-b847/unblock-refit
outcome: |
  Единственное препятствие перед принятой перестройкой Launch Control больше не существует: отдельное изменение
  Direction OS реализовало ограниченный межтрековый запрос результата, а свежая проверка усилила его так, чтобы
  целевой трек сохранял право ACCEPT/COUNTER/BLOCK и всю власть над техническим способом.

  Тот же, а не второй, корень Demo Control Room теперь READY/default. Временно выбранный только на время блокировки
  Canon сохранён READY/non-default и может продолжаться владельцем независимо. Ни продуктовая работа, ни один
  чужой трек этим ремонтом не запущены; фактическая очередь теперь содержит четыре ready, два waiting, два blocked
  и один paused корень без новых решений владельца.
evidence: |
  Direction commits `587234f9` and `b6b76472` respectively install and harden the bounded outcome-request lifecycle.
  The binding rules are present in `os/schema/packets.md` and `os/adapters/coding-agent.md`: only the authorized
  requester's ordinary root may issue the auxiliary request; requester and target already occupy WIP; the target
  returns ACCEPT, COUNTER or BLOCKED with evidence, keeps its root and technical plan, and issues no successor.

  `live/indie-game-development/NOW.md` previously made Canon default explicitly only "while Demo Control Room refit
  is blocked". With that sole condition now false, the corrected state removes `unblock_when`, appends this receipt,
  selects the existing Demo Control Room map root and changes only the three stale selector notes. Every root id,
  track, scope, receipt, wait, pause and unrelated blocker is preserved.

  The owner accepted the researched replacement with the exact words `Так, окей, тогда принимаю план.` and gave
  implementation authority with `можешь автономно сейчас создать этот трек вот основу` and `желательно работай и
  позови меня только когда будем готовы`. He separately said Canon work may continue; therefore it remains READY but
  is no longer the conditional default. The regenerated owner panel mirrors the corrected counts and routing.
state_changes: |
  live/indie-game-development/NOW.md:
    - SET `updated` to `2026-07-22 by s-repair-launch-control-demo-control-room-unblock-001`.
    - UPDATE existing root `c-map-launch-control-demo-control-room-refit-001`: status `blocked` -> `ready`; REMOVE
      `unblock_when`; APPEND this repair history receipt once; replace its note with READY/default same-track-refit
      wording that names completed maintenance and explicitly launches no product or foreign-track work.
    - SET `next.call` to existing ready root `c-map-launch-control-demo-control-room-refit-001`.
    - UPDATE only stale selector clauses in existing Canon, Grid and Gas root notes: Canon is READY/non-default and
      may continue independently; Grid and Gas remain READY/non-default; Demo Control Room refit is current default.
    - PRESERVE every track, root id, scope, status not named above, waiting dependency, blocker, pause, receipt,
      decision and WIP limit. Postcondition: ready 4, waiting 2, blocked 2, paused 1, decisions 0.
  live/indie-game-development/work/launch-control/c-map-launch-control-demo-control-room-refit-001-call.md:
    - REPLACE the dangling context reference to `unblock_when` with this repair receipt and the two authoritative OS
      rule sections; preserve goal, owner words, boundaries, done_when, budget and every other byte semantically.
  live/indie-game-development/work/board/dashboard.html:
    - REGENERATE mirrored Board/Journal routing: Demo Control Room READY/default; Canon READY/non-default; counts
      4/2/2/1/0; one current journal line explains the verified unblock and zero foreign launches. Preserve all
      unrelated cards, historical journal entries and five open findings.
  live/indie-game-development/LOG.md:
    - APPEND the `log` line once before its trailer.
  live/indie-game-development/history/2026-07-22-s-repair-launch-control-demo-control-room-unblock-001.md:
    - SAVE this full RESULT once with its exact END_OF_FILE trailer.
  live/indie-game-development/TREE.md, CHARTER.md, knowledge/, os/**, product repositories and every foreign-track
  plan/artifact: unchanged.
captures: []
decisions_needed: []
play_check:
  - 1 Name the contradiction: done — NOW still said the Demo Control Room waited for OS maintenance even though commits `587234f9` and `b6b76472` had completed and hardened that exact bounded capability.
  - 2 Reconstruct: done — fresh NOW, CALL, accepted transition RESULT, TREE, CHARTER, LOG tail, current git history, OS rules and owner-panel routing showed that Canon's default was explicitly conditional on the now-false blocker.
  - 3 Propose corrected state: done — the minimal diff makes the same root READY/default, removes only the consumed blocker and stale selector wording, refreshes its context/render and preserves every foreign root and plan.
  - 4 Confirm: done — owner said `Так, окей, тогда принимаю план.` and authorized autonomous foundation work with `можешь автономно сейчас создать этот трек вот основу ... желательно работай и позови меня только когда будем готовы`; these words cover the mechanical unblock and selector restoration, while his separate Canon allowance is preserved as READY/non-default.
  - 5 Friction: skipped — this was the planned one-time blocker; the OS hole was already fixed and freshly hardened, so no new or repeated friction remains to record.
log: 2026-07-22 · s-repair-launch-control-demo-control-room-unblock-001 · repair · launch-control · g-b847/unblock-refit: verified OS maintenance 587234f9 and fresh hardening b6b76472 satisfy the sole blocker; the same Demo Control Room map root is READY/default, Canon remains READY/non-default, and no foreign work was launched. → history/2026-07-22-s-repair-launch-control-demo-control-room-unblock-001.md
next: |
  CALL c-map-launch-control-demo-control-room-refit-001
  to: session
  direction: indie-game-development
  track: launch-control
  play: map
  node: g-b847
  issued: 2026-07-22 (s-work-launch-control-m1-superseded-by-demo-control-room-001)

  goal: |
    У направления есть одна принятая Demo Control Room, которая связывает
    качественное demo к выбранному Steam-окну с причинными продуктовыми
    результатами, проверяемым evidence, ограниченным вниманием владельца и
    ответственностью целевых треков без второй planning authority.

  context: |
    Read fresh:
    - `live/indie-game-development/CHARTER.md`
    - `live/indie-game-development/TREE.md`
    - `live/indie-game-development/NOW.md`
    - `live/indie-game-development/history/2026-07-22-s-work-launch-control-m1-superseded-by-demo-control-room-001.md`
    - `live/indie-game-development/history/2026-07-22-s-repair-launch-control-demo-control-room-unblock-001.md`
    - `os/schema/packets.md` (`Bounded cross-track outcome request`)
    - `os/adapters/coding-agent.md` (`bounded outcome-request exception`)

    The owner accepted the researched replacement with the exact words
    `Так, окей, тогда принимаю план.` He then authorized autonomous creation of
    the foundation and clarified that there must not be a second planning track.
    Reuse stable track identity `launch-control`; its owner-facing label is
    already `Demo Control Room`.

    Preserve the accepted Demo Contract, MUST/SHOULD/CUT, quality floor,
    truthful-claims boundary, conditional October route, February fallback and
    money gate. The old M1-first operating-plan model, 12-field Daily Command,
    premature binding min-spec choice and separate management dashboard are
    superseded, not inputs to restore.

  boundaries: |
    Do not create a second management track, new packet/state type, local play,
    dashboard, automation or recurring job. Do not mutate product repositories,
    Canon, Marketing or another track's plan; do not choose gameplay mechanics
    or another track's implementation. Preserve blocked, waiting, paused and
    already-running roots without relaunch.

    Demo Control Room may own priorities, external dates, outcome demand,
    evidence, cross-track collisions, cuts and replanning triggers. Each target
    track retains ACCEPT/COUNTER/BLOCK response, internal planning and all
    technical-how authority.

  done_when: |
    1. `g-b847` is one compact owner-approved outcome card for the sole Demo
       Control Room; the obsolete operating-plan/dashboard semantics are gone.
    2. The existing `launch-control` track identity is retained with no parallel
       management authority and one lawful bounded continuation.
    3. The accepted replacement makes causal product outcomes, evidence classes,
       external Steam routes, owner/integration constraints, WIP/refill rules and
       latest-safe cuts visible without inventing throughput or dates.
    4. The next bounded foundation outcome is ready, while Demo Contract,
       MUST/SHOULD/CUT, quality floor and truthful claims remain unchanged.
    5. Every target track keeps its technical planning/implementation authority;
       no product or foreign-track work is launched.

  return: |
    One map RESULT with the accepted replacement node, exact owner words,
    preserved boundaries and one bounded Demo Control Room foundation CALL.

  budget: one owner-present session
  surface: owner-present

END_OF_FILE: live/indie-game-development/history/2026-07-22-s-repair-launch-control-demo-control-room-unblock-001.md
