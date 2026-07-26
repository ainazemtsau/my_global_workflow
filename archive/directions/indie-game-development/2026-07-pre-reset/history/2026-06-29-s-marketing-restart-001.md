RESULT s-marketing-restart-001 (call: c-marketing-restart-001)
direction: indie-game-development   play: local/marketing-status + planning brief   node/task: g-2f8c/q-ai-pipeline
outcome: |
  Restart-brief маркетингового трека g-2f8c готов. q-ai-pipeline не заморожена.
  Вывод: первая следующая рабочая карточка должна быть q-capture-setup, а q-ai-pipeline — второй,
  уже в рамке real-build-first / AI-assisted polish / skeptic validation. Маркетинг остаётся
  параллельным к engine spine g-9c41 и не становится вторым active bet.
evidence: |
  Проверены правила KERNEL и packet schema.
  Прочитаны:
  - live/indie-game-development/plays/marketing-status.md
  - live/indie-game-development/plays/marketing-forge.md
  - live/indie-game-development/work/marketing/board.md
  - live/indie-game-development/work/marketing-track-design-2026-06-16.md
  - work/marketing/questions/q-foundation.md
  - work/marketing/questions/q-studio-identity.md
  - work/marketing/questions/q-ai-pipeline.md
  - work/marketing/questions/q-capture-setup.md
  - work/marketing/questions/q-channels.md
  - work/marketing/questions/q-money-path.md
  - work/marketing/questions/q-cadence.md
  - work/marketing/questions/q-marketing-assets-repo.md
  - work/marketing/questions/q-positioning-hook.md
  - work/marketing/handle-reservation-chinvat.md
  Done_when покрыт:
  1) текущее состояние маркетинга дано;
  2) протухания названы;
  3) actionable карточки названы;
  4) порядок первых задач рекомендован;
  5) следующий конкретный CALL подготовлен.
state_changes: []
captures:
  - q-capture-setup hygiene mismatch: board.md says open/actionable, but questions/q-capture-setup.md frontmatter still says blocked even though q-studio-identity is frozen.
  - q-foundation build-chain note is stale: old t-1/t-2/t-4 dependency should not drive current marketing sequencing; use current engine/visual context from owner checkpoint.
  - marketing-track-design still contains old public-AI prohibition; q-foundation supersedes it with flexible surface-aware AI policy, pending separate cleanup/tree-edit path.
  - q-ai-pipeline preliminary steer remains likely real-build-first, AI-assisted polish, skeptic validation; not decided/frozen.
decisions_needed: []
play_check:
  - 1 Load the graph: done — board + every marketing card read, plus marketing-track design and handle-reservation product.
  - 2 Compute: done — frozen/actionable/blocked/parallel recomputed; q-capture-setup contradiction flagged.
  - 3 Render: done — owner-facing restart brief rendered by frozen/actionable/blocked/drift/first tasks.
  - 4 Recommend: done — recommended q-capture-setup first, q-ai-pipeline second, q-channels third, q-money-path later.
  - Planning brief overlay: done — current state, stale items, actionable cards, order, and next CALL included.
log: "marketing restart (g-2f8c): status map rendered; q-capture-setup recommended as first restart card; q-ai-pipeline deferred to second, real-build-first frame; no state changes."
next: |
  CALL c-marketing-capture-setup-restart-001
  to: session
  direction: indie-game-development
  play: local/marketing-forge
  node: g-2f8c
  task: q-capture-setup

  goal: |
    Заморозить q-capture-setup как первый restart artifact маркетингового трека:
    практический capture substrate v0 для Chinvat — handles/account order, page/newsletter skeleton,
    owner-only vs delegable действия, и ясная зависимость финальной капсулы/ассетов от будущей q-ai-pipeline.

  context: |
    Read:
    - live/indie-game-development/work/marketing/board.md
    - live/indie-game-development/work/marketing/questions/q-capture-setup.md
    - live/indie-game-development/work/marketing/questions/q-foundation.md
    - live/indie-game-development/work/marketing/questions/q-studio-identity.md
    - live/indie-game-development/work/marketing/handle-reservation-chinvat.md
    - live/indie-game-development/plays/marketing-forge.md
    - live/indie-game-development/work/marketing-track-design-2026-06-16.md

    Current restart findings:
    - q-foundation is frozen: "мы никто", capture-first, real gameplay speaks, flexible AI policy.
    - q-studio-identity is frozen: studio name Chinvat, handle chinvat; it unblocks q-capture-setup.
    - Board says q-capture-setup is open/actionable, but the card frontmatter still says blocked;
      treat this as stale hygiene and include the appropriate correction in state_changes if the card is frozen.
    - Do not use q-foundation's old t-1/t-2/t-4 build-chain wording as current sequencing.
      Current owner checkpoint: engine is on character road; Sc-types done; Sc-weight next.
      Visual: gas-lab S1 done; S2 next = two-type character / heavy-light / scatter-glow.
    - q-ai-pipeline is still open and must not be frozen in this call.

  boundaries: |
    Do not freeze q-ai-pipeline.
    Do not invent game lore, world hook, or positioning line; q-positioning-hook waits for canon g-d3a8.
    Do not add dev scope or request new build work; only note what marketing will need from already-running tracks.
    Do not publish public posts or create external accounts as the session; owner executes external registrations.
    Do not touch NOW.md, TREE.md, CHARTER.md directly.
    Do not make a full go-to-market plan.

  done_when: |
    q-capture-setup is ready to freeze as an ARTIFACT with:
    - exact handle/account reservation order for chinvat, including owner-only vs delegable logistics;
    - minimal page/newsletter/capture skeleton and what can be prepared now;
    - explicit placeholder/dependency for capsule and visual assets via future q-ai-pipeline;
    - "do not post publicly until real gameplay clip/source material exists" guard;
    - rejected alternatives and owner voice-verdict recorded;
    - board/card hygiene handled in proposed state_changes;
    - NOW.md untouched.

  return: |
    marketing-forge RESULT: frozen q-capture-setup artifact or a checkpoint stopped at the first owner-required step,
    with clear evidence and no direct repo writes.

  budget: one chat, light research only unless service/tool choice needs current facts.

END_OF_FILE: live/indie-game-development/history/2026-06-29-s-marketing-restart-001.md
