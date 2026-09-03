CALL c-solmax-zaratustra-v2-review-053
to: session
direction: solmax
play: review
node: g-zara-health-vertical
bet: bet-g-zara-health-vertical
status: ready

goal: |
  Закрыть активную ставку «Первый полезный Health-срез» честным вердиктом по
  плею review в свете решения владельца от 2026-09-03 о новом продукте
  Zaratustra v2, сохранить полезное как улики и передать направление на
  ревизию устава.

context: |
  Читать первым: `live/solmax/work/zaratustra-v2-plan-2026-09-03.md` —
  план перехода; раздел 0 несёт слова владельца, раздел 9 порядок ног.
  Карточки: `bet-g-zara-health-vertical`, `g-zara-health-vertical`, открытые
  `t-health-capabilities`, `t-health-executor`, `t-health-ui`, закрытые
  `cards/closed/t-health-*`.
  Продуктовый репозиторий `C:\projects\zaratusta-product`, ветка
  `feat/health-contracts`, HEAD `53a52cd` — только читать; в него больше не
  пишем.
  Рекомендуемый вердикт: obsolete — «a higher approved strategy change removed
  its purpose». Владелец 2026-09-03 решил, что Zaratustra это новый чистый
  продукт и преемник workflow, а Health-срез на Python-рантайме не нужен.
  Пороги ставки не сработали: порог 1 не сработал, три задачи остались
  открыты, дата разбора 13.09.2026 не наступила.
  Salvage как улики, без переноса структуры:
  `work/health-context-model-v1.md` (типизированный список контекста
  здоровья), `work/health-workflow-svod-dnya-v1.md` (граф свода дня), приём
  «одна команда проверки плюс selfcheck» из продуктового репозитория.

boundaries: |
  - Не строить продукт, не открывать converge, не выдавать задач старой
    ставке, не предлагать надстройку над workflow.
  - Не переписывать устав и карту в этой ноге: это следующие ноги, frame и
    затем map, по разделу 9 плана.
  - Вердикт произносит владелец: показать один экран (вердикт и основание, что
    сохраняем, что закрываем, следующий шаг) и остановиться до его слова.
  - Узлы 2–6 старой карты и ветку operating-substrate вердиктами не трогать:
    их судьба решается в map.
  - Один вопрос владельцу, не список.

done_when: |
  Владелец сказал вердикт своими словами и они процитированы; ставка закрыта
  по review: bet-карточка и открытые task-карточки закрыты, узел
  g-zara-health-vertical получил статус по вердикту, NOW.bet: null; salvage
  записан в RESULT; выдан один CALL на frame (ревизия устава по разделу 9
  плана) и передан через RESULT.next.

return: |
  RESULT по схеме: в outcome вердикт и его основание словами владельца; в
  state_changes закрытия и регистрация CALL на frame; в captures то, что
  уходит в map.

budget: one session
