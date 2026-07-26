# CALL c-exec-gascoopgame-worktree-protocol-v2-001

to: executor
direction: indie-game-development
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: worktree-protocol-v2-install
issued: 2026-07-16 (s-repair-gascoopgame-worktree-routing-v2-001)
parent: s-repair-gascoopgame-worktree-routing-v2-001

goal: |
  У GasCoopGame есть одна недвусмысленная product-owned authority рабочих площадок, а каждый legacy checkout
  имеет lossless lifecycle disposition без зависимости от имени локальной папки.

context: |
  Владелец выбрал вариант A фактическим ответом «A». Audit и принятый Direction dispatch contract:
  live/indie-game-development/work/gascoopgame-worktree-protocol-v2.md.

  Current product authority: root AGENTS.md contract v26, его Worktree workflow и
  docs/gas-simulation/PROGRAM.md. Они уже разделяют integration-only branch, один persistent mutable workspace
  и shared-workspace sequencing, но не содержат complete registry/migration semantics для накопившихся checkout'ов.

  Direction KERNEL запрещает executor-CALL диктовать branches/paths/SHAs: executor обязан заново обнаружить
  fresh topology и владеть branch mechanics по product authority. Direction audit values — evidence bases, не
  freshness locks и не launch commands.

  NOW gate: CALL HELD, пока c-exec-char-v2-reaction-core-repair-002 не закрыт или явно не поставлен владельцем
  на паузу. Этот protocol install обязан вернуться HOME до первого product executor CALL ставки NearGas L1B.

boundaries: |
  Process/docs-only installation. Не менять game source, tests, assets, scenes, packages или Unity project data.
  Не delete/move/reset/clean/stash/rebase/merge ни один legacy checkout или его WIP; не выбирать `.meta` GUID;
  не удалять ignored/vendor/raw evidence; не запускать mutation и не менять L1a score/artifact. Не превращать
  локальный observed path/branch/SHA в Direction launch requirement. Не открывать cleanup execution в этой сессии.

done_when: |
  1. Product authority по fresh repo state однозначно называет один read-only integration branch и единственный
     persistent mutable Unity+MCP workspace; одновременно мутирует один product leg; clean ephemeral evidence
     checkout допустим только для fresh review/mutation evidence и не становится feature-worktree.
  2. Product-local registry задаёт состояния ACTIVE-EXCEPTION/FROZEN/FORENSIC/RETIRE-CANDIDATE, обязательные
     поля owner/CALL/editor/cleanliness/next-legal-action и fresh inventory всех обнаруженных checkout'ов.
  3. Registry/plan называет preservation proofs до любой уборки: incomplete Core snapshot, visual WIP, lab
     vendor/forensic content, PGG FAIL_STAGE evidence, divergent folder metas, canonical/stale raw mutation reports,
     clean exp/policy candidates и active character exception.
  4. Diff ограничен product protocol/docs; first-hand before/after status доказывает, что ни один legacy WIP,
     product source/asset/test, Unity lock/process, score или remote ref не изменён.
  5. Релевантные repo-native hygiene/checks зелёные; RESULT возвращает commit/diff/check evidence и отдельный
     proposed cleanup CALL, но сам cleanup не запускает.

return: |
  Product RESULT с commit/diff/check evidence, fresh registry и отдельным неисполненным cleanup handoff.

budget: one focused half-day maximum
surface: any

END_OF_FILE: live/indie-game-development/work/c-exec-gascoopgame-worktree-protocol-v2-001-call.md
