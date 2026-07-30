# RESULT s-repair-g-37a1-gas-rest-launch-state-001

call: owner-pasted intermediate product handback for `c-exec-g-37a1-gas-rest-amend-001`
direction: indie-game-development · track: t-sim · play: repair · node/task: g-37a1/t-6
date: 2026-07-30

## outcome

Hot state теперь совпадает с проверяемой реальностью запуска: действующий инженерный root
`c-exec-g-37a1-gas-rest-amend-001` зарегистрирован как `running`, а не повторно dispatchable
`ready`. Его id, полоса, задача, CALL-файл, metadata и смысл сохранены без изменений.

Это только launch bookkeeping и защита от повторного запуска. Продуктовая пара не признана
принятой: квитанции `04-pair-candidate.json` нет, binding PAIR-FREEZE не проведён, t-6 остаётся
active. По маршруту engineering_contract 31 промежуточная pair eligibility не закрывает root и не
создаёт Direction-successor; существующий root остаётся открытым до gated REPORT либо genuine
ESCALATE.

## evidence

- Владелец увидел точную дельту и разрешил её словами: «Записывай эту дельту».
- Product repo `C:/projects/Unity/GasCoopGame_win-u4`, прочитан только на чтение: branch
  `slot/win-u4`, HEAD `943832ba42254d430738927e79712cf299adb60d`.
- Разрешимый launch receipt:
  `docs/measurements/root-receipts/c-exec-g-37a1-gas-rest-and-checksum-001/03-plan-amend.json`,
  commit `6a775462208f29348d766e9fc5671886ec48d74b`, SHA-256
  `76298234dc295cba2ed0fa97e1e8e82256a332f620cec2245a506a8f3a11f4e3`; receipt фиксирует
  `state: ACTIVE`, `stage: PLAN`, `engineering_contract: 31`, новый `plan_freeze_commit`
  `cd9bad22e1de2d686bb1ab60911ab687b6018e75` и eligibility для свежего PAIR-CANDIDATE.
- Точная последующая родословная существует:
  `cd9bad22e1de2d686bb1ab60911ab687b6018e75` →
  `24f1eb8bf42b1421868ec02e6ddf26b579528c01` →
  `943832ba42254d430738927e79712cf299adb60d`. Это доказательство запуска и наличия кандидата, не
  доказательство принятия пары.
- `docs/measurements/root-receipts/c-exec-g-37a1-gas-rest-and-checksum-001/04-pair-candidate.json`
  отсутствует на свежем HEAD; отдельная binding PAIR-FREEZE-сессия ещё не оставила доказательства.
- `os/schema/packets.md`, `os/adapters/runtime.md` и writer contract одинаково требуют для v30/v31:
  один root остаётся зарегистрированным через внутренние стадии; pair eligibility не выпускает
  Direction CALL и не закрывает задачу.
- Перед применением перечитаны свежие `NOW.md`, `TREE.md`, `CHARTER.md`, LOG tail, Git, play
  `repair` и writer contract. Текущее направление сохраняет один active bet, WIP=5, пять полос,
  по одному root на полосу, pending decisions отсутствуют, forecast остаётся `no_basis`.
- В current `knowledge/` owner panel не объявлен; регенерация не требуется. Product repo не
  изменялся.

## state_changes

```text
live/indie-game-development/NOW.md:
  updated -> s-repair-g-37a1-gas-rest-launch-state-001
  open_calls.c-exec-g-37a1-gas-rest-amend-001.status: ready -> running
  open_calls.c-exec-g-37a1-gas-rest-amend-001.started: + точный product receipt 03, его commit и
    SHA-256
  open_calls.c-exec-g-37a1-gas-rest-amend-001: id, track, to, for, issued, call, note и смысл
    сохранены
  tasks/tracks/issues/forecast/recurring/decisions и все остальные open_calls сохранены без
    изменений; t-6 остаётся active; ни один CALL не закрыт и не создан

live/indie-game-development/LOG.md: prepend одна строка с этим session-id
live/indie-game-development/history/2026-07-30-s-repair-g-37a1-gas-rest-launch-state-001.md:
  создать этот полный RESULT
```

## captures

[]

## decisions_needed

[]

## play_check

- 1 name the contradiction: done — NOW держал root `ready`, хотя точная продуктовая квитанция и
  два последующих коммита доказывают, что он уже запущен.
- 2 reconstruct: done — newest-first по NOW/TREE/CHARTER/LOG/history/Git и product artifacts;
  подтверждены active bet, все задачи, пять полос и их roots, issues, `no_basis`, отсутствие
  решений и recurring work.
- 3 propose corrected state: done — предложены только `ready → running`, проверяемый `started`,
  LOG/history; прогресс, task status, pair verdict, forecast и соседние полосы не изобретались.
- 4 confirm (owner): done — один batched diff показан целиком; точные слова владельца:
  «Записывай эту дельту».
- 5 friction: skipped — это единично пропущенный launch-bookkeeping; действующие schema/runtime
  уже предписывают receipt и duplicate-launch guard, повторного OS-дефекта не установлено.

## log

продуктовый root уже запущен; open call переведён ready → running по точной квитанции 03, при этом
PAIR-CANDIDATE не принят, t-6 не закрыта и Direction-successor не создан

## next

return-to-owner. `c-exec-g-37a1-gas-rest-amend-001` остаётся `running` и не предлагается к
повторному dispatch. Следующие внутренние продуктовые переходы не являются Direction CALL:
сначала должна появиться committed `04-pair-candidate.json`, затем отдельная свежая PAIR-FREEZE
проверяет точную пару и получает требуемую подпись величины веса.

END_OF_FILE: live/indie-game-development/history/2026-07-30-s-repair-g-37a1-gas-rest-launch-state-001.md
