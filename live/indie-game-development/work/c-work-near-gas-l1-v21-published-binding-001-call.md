CALL c-work-near-gas-l1-v21-published-binding-001
to: session
direction: indie-game-development
play: work
node: g-9c41  task: NearGas-L1-BUILD
goal: |
  Опубликованный NearGas L1 v21 planning authority получает связывающий Direction-вердикт: либо точный
  published packet принят как основание для будущего отдельного independent-RED execution leg, либо возвращён
  с полным опровержением. В обоих случаях L1 остаётся NOT DELIVERED.
context: |
  Авторитет состояния: live/indie-game-development/NOW.md.

  Product repo (read-only для этой сессии): C:\projects\Unity\GasCoopGame_core.
  Published product authority: origin/main@9dc4957548111c99980f7efbbb9e7adbda17332b.
  Integration merge: fed1073d53d5894946b8ad6e9ffd14d6c79ec69a.
  Frozen-packet source commit: 21acd415209dc4261aaa692c13cc56d0e6d9f59f.
  The merge has parents db69aba6847a47ce2544ad1314f3567b327805d7 and
  21acd415209dc4261aaa692c13cc56d0e6d9f59f; both fed1073d and 21acd415 are ancestors of published main.

  Exact published raw-Git-blob SHA-256 manifest:
  - ADR: ccc75150a7de90dd97363f1f3b7f595066cab8e907dfdb2d79ebc53d7495ea10
  - PLAN: bcc9de92f9e4ac0efddb6c066daa66319969599a10d67b2c73549cb44193b3e0
  - proposal: d44ac6df503e649a0bd3732dedeae7c56d18e6fe103ca6cd5d6be7d33c76c704
  - spec: 8419ba161de7787600fac6c20087df819c9c73e7f91f294b520c7075bb42b28e
  - tasks: ab32ed4a43b76d906d7ac75a1722e2a769121b184c65eb421c6c484e22710fe2
  - aggregate: 2f676a071731bd8ae6f787eb4aeb01fdc440e676d476ebc54956eba803ed3a0e

  Historical digest 52a47c52dc8202637c5aa665fc812f4d5d5254445671546a069020a5cc8971e1
  is working-tree-byte review chronology only. Before any remote push, line-ending normalization was detected;
  the five frozen files were not changed, and a fresh exact-blob semantic review returned 29/29 GREEN, zero gaps,
  with the manifest recomputed twice. That in-session review is evidence only, not this binding fresh session.

  Evidence pointers:
  - product docs/results/c-exec-near-gas-core-authority-001.md
  - product docs/gas-simulation/dashboard.html
  - live/indie-game-development/history/2026-07-14-s-exec-near-gas-core-authority-001-plan-amend-resync-002.md
  - live/indie-game-development/work/c-exec-near-gas-core-authority-001-plan-amend-resync-002-call.md
  Owner literal approval recorded in all five packet files: «Подтверждаю план.»
boundaries: |
  Это новая отдельная Direction-сессия и связывающий read-only review. Product repo, frozen packet, Direction
  TREE/CHARTER/canon и все внешние репозитории не мутировать. Не создавать RED, код или тесты; не запускать
  BUILD/tests/tools/check/review/mutation/Deliver/Unity/MCP; не делать product commit/merge/push.

  Owner approval, product commit/main publication и прежний in-session 29/29 pre-pass сами по себе не закрывают
  Direction gate. Подтвердить или опровергнуть claims first-hand в этой fresh session. Любые subagent-проходы
  считаются только pre-pass; binding verdict принадлежит самой fresh Direction-сессии.

  NearGas-L1-BUILD не переводить в done. До GREEN не снимать
  c-exec-near-gas-core-authority-001-plan-amend-resync-002 и не выпускать EXEC/BUILD. Этот CALL READY PARALLEL:
  сохранить c-review-poligon-m1-route-reset-001 как global PRIMARY/NOW.next и не менять unrelated calls/decisions.
done_when: |
  1. Fetch/readback подтверждает exact published main, ancestry, 12-path planning scope и неизменный five-file
     raw-blob manifest; более новый origin/main либо безопасно сохраняет эти blobs/ancestry, либо становится
     явно разобранным drift, а не молча принятой новой базой.
  2. Fresh reviewer независимо выводит полный набор 13 Acceptance Requirements + 12 unique NegativeControls +
     4 Properties и для каждой из 29 identities проверяет exact fixture | call | observe | source | negative
     recipe и concise executable test skeleton по точным published blobs.
  3. Есть отдельные dispositions для process integrity: owner-verdict sequence, approval-only edit, v21 contract
     stamp, no-crutch boundaries, historical 52a47... correction и final exact-blob 2f676... identity.
  4. Verdict GREEN допустим только при 29/29 PASS, zero unresolved/inferred cells и zero process gaps. Иначе RESULT
     возвращает полный дедуплицированный gap list, оставляет оба NearGas calls pending и не создаёт downstream CALL.
  5. При GREEN RESULT снимает planning-return call и этот binding call, оставляет L1 active/NOT DELIVERED и может
     создать complete future executor CALL: новая ветка от exact current published main, lane A/headless launch,
     новый independent spec-only RED первым, immutable packet/ledger, current v21, historical checkpoints preserved,
     no GasCoopGame_dev assignment, serial option A/deferred workers, full review/fresh-G5/Deliver contour.
return: |
  Полный Direction RESULT с binding-verdict GREEN|RED; exact published identity/ancestry; 29-row dispositions;
  process-integrity dispositions; complete gap list; explicit L1 NOT DELIVERED boundary; exact state_changes.
  При GREEN - один complete future independent-RED executor CALL. При RED - checkpoint без downstream CALL.
budget: one fresh Direction session
surface: codex

END_OF_FILE: live/indie-game-development/work/c-work-near-gas-l1-v21-published-binding-001-call.md
