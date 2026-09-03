CALL c-solmax-zaratustra-v2-map-055
to: session
direction: solmax
play: map
node: g-solmax
status: ready

goal: |
  Перевыпустить дерево целей solmax под ревизованный устав: семь целей = волны
  0-6 плана перехода, все parked; вынести явный вердикт каждому старому узлу;
  записать в карту правило «спека любой цели это CORE.md, converge не
  запускается».

context: |
  Читать первым: `live/solmax/work/zaratustra-v2-plan-2026-09-03.md` —
  §8 волны (состав и колонка «Проверка владельца, пять минут»),
  §9.3 состав этой ноги, §10 покрытие требований, §11 чего не делать,
  §12 решения по умолчанию.
  Устав после ревизии 2026-09-03: `live/solmax/CHARTER.md`. Три критерия
  успеха, преемник workflow, два репозитория, строго индивидуальное
  использование, ветка operating-substrate закрыта как маршрут.
  Итог предыдущей ноги: `live/solmax/history/2026-09-03-s-solmax-zaratustra-v2-frame-054.md`
  и запись его слова «да» в `cards/owner_approved.md`.
  Состояние дерева: `cards/tree_validity.md` —
  `umbrella_placement_superseded_tree_awaiting_map`.
  Цена закрытия при нарезке: `live/solmax/knowledge/light-close-throughput-measured.md`.

  Семь целей это волны 0-6 из §8 плана: 0 ядро текстом, 1 программа-скелет,
  2 первый эксперт (разработка самой Zaratustra), 3 здоровье, 4 поверхности и
  модели, 5 самоисправление и обновление, 6 переезд. У каждой цели в карточке:
  что появляется по §8, и сценарий пятиминутной проверки владельца из той же
  строки таблицы — как строка done_when, а не как пожелание.

  Правило направления, записать в карту явно: спека любой цели это CORE.md;
  converge для целей не запускается — триаж trivial, строка
  `converge OFF — because CORE.md is the spec` копируется в play_check ноги
  shape. Основание — §11 плана: четыре узла с тяжёлым разбором дали ноль строк
  продукта.

boundaries: |
  - Судьба старых узлов решается здесь и только здесь, каждому явный вердикт с
    причиной: `g-zara`, `g-zara-daily-owner-use`,
    `g-zara-extensible-areas-workflows`, `g-zara-governed-improvement`,
    `g-zara-model-qualification-routing`, `g-zara-trusted-context-state`,
    `g-zara-health-vertical` (parked его словом 2026-09-03 — статус не менять
    без нового слова), `g-operating-substrate`,
    `g-operating-substrate-first-process-creator`.
  - Карточка `tree_validity` перевыпускается под новую карту.
  - Ставку не открывать и задач не создавать: активация волны 0 это `shape`.
  - Жёсток порядок только первых трёх волн (§8); состав волн 3-6 меняем по ходу.
  - Не изобретать содержание волн сверх §8 плана; живое слово владельца старше
    плана, план старше догадок.
  - Дерево меняется только его явным словом (G9): без слова — чекпойнт и новый
    наряд на ту же работу, а не запись.
  - Продукт не строить; в `C:\projects\zaratusta-product` не писать.

done_when: |
  Семь узлов волн 0-6 заведены в `cards/` с goal / done_when / why / status /
  _parent / _pos, все `parked`; у каждого узла строка done_when с его
  пятиминутной проверкой; правило «CORE.md это спека, converge OFF» записано в
  карту так, что нога shape его прочитает; каждый из девяти старых узлов имеет
  явный вердикт с причиной; `tree_validity` перевыпущен; владелец одобрил
  дерево своими словами и они процитированы в RESULT; в state_changes отметка
  owner_approved с его словами; выдан один наряд на `shape` волны 0 и передан
  через RESULT.next.

return: |
  RESULT по схеме: в outcome дерево семи волн и слово владельца; в
  state_changes карточки семи узлов, вердикты девяти старых узлов, перевыпуск
  tree_validity, отметка owner_approved и регистрация наряда на shape.

budget: one session

END_OF_FILE: live/solmax/work/calls/c-solmax-zaratustra-v2-map-055.md
