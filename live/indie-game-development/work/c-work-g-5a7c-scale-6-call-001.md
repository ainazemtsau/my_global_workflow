# CALL — c-work-g-5a7c-scale-6-call-001

to: session
play: work
direction: indie-game-development
node: g-5a7c
task: t-scale-6
issued: 2026-08-09 by s-work-g-5a7c-scale-4-close-001
status: ready

## goal

Существует готовый к отправке наряд исполнителю на `t-scale-6`: четверо могут держать один груз,
усилие складывается по рукам с потолком на руку, а разница «один / вдвоём» видна по сети.

## context

- `t-scale-4` закрыта повторным прогоном владельца. Product commit `e7dc8f5b`, полный RESULT-tip
  `d9518538`; Direction-разбор — `history/2026-08-09-s-work-g-5a7c-scale-4-close-001.md`.
- Product disposition честная: `d9518538` опубликован в `origin/slot/win-u1`, WIN-U1 освобождён,
  но `dev/main` этим закрытием не объявлены обновлёнными. Перед executor CALL заново перемерить
  lawful basis, публикацию, owner-selected slot и contract pin; SHA здесь не freshness-lock.
- Сейчас `_cargoMaxHolders: 2`; существующий `CargoHaul` уже суммирует держателей и имеет потолок
  усилия на руку. Task требует четверых, видимую сетевую разницу и возврат к владельцу, если чисел
  под текстуру «лёгкий один может тащить, средний двое» честно не находится.
- Архитектурная находка зарегистрирована отдельно как
  `i-world-situations-need-extensible-reaction-architecture-001`; это не скрытый scope `t-scale-6`.
- Каждая строка наряда проверяет происхождение и перемеряет grounds до отправки.

## boundaries

- Не заводить личную мощность хвата и классы груза: это `t-scale-7`.
- Не добавлять разные размеры/массы/ценность, прокачку, магазин, бросок или UI.
- Не строить общую situation/event bus и не расширять реакцию хозяина.
- Не переоткрывать lifecycle/Y/тишину/преграду `t-scale-4`, телекинезные `1.28 / 0.8 / 1.6`,
  наклон, delivery или пороги `60 / 150 / 400` без нового слова владельца.
- Числа ПРОБЫ не замораживать тестами. Если ступень не выводится — вопрос владельцу с вариантами и
  рекомендацией, не самостоятельный выбор.
- Направление не выбирает слот само: нужен один WIN-U1..WIN-U4, названный владельцем, и свежий
  selector readback.

## done_when

Наряд лежит в `work/` и зарегистрирован executor call card: слот, lawful basis и pin перемерены;
происхождение строк проверено; «четверо / сумма / потолок на руку / сеть» сведено с текущими
байтами; границы `t-scale-7` и architecture issue сохранены; маршрут вопроса при отсутствии чисел
записан прямо. Product handback возвращается HOME и сам Direction-задачу не закрывает.

## return

RESULT session-work с зарегистрированным engineering CALL либо один полный blocker/owner decision.

## budget

Одна нога на наряд. Без product BUILD, Control merge и исправления architecture issue.

END_OF_FILE: live/indie-game-development/work/c-work-g-5a7c-scale-6-call-001.md
