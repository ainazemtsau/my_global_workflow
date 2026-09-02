---
id: c-exec-g-5a7c-a-flying-thing-knocks-the-mouse-down-1-001
_kind: call
_bet: g-5a7c
track: мышь становится телом
for: t-a-flying-thing-knocks-the-mouse-down-1
play: work
to: executor
status: done
issued: 2026-09-01
slot: WIN-U1
repo: C:\projects\Unity\GasCoopGame_win-u1
call: work/2026-09-01-call-a-flying-thing-knocks-the-mouse-down.md
basis: 19dff65e
description: Второй вызывающий AddImpulse — от контакта груза; приёмник уже стоит и им
  пользуется нить, работа в проводе и в сохранённом направлении вектора
_pos: 203
---

## журнал
2026-09-02 · статус выправлен направлением: карточка стояла ready при закрытой ноге. Работа закрыта 2026-09-01 на c97ee735 и записана в журнале ниже — ready держался ошибкой писаря, а не открытым нарядом. Приёмка задачи это НЕ закрывает: она остаётся INCONCLUSIVE и ждёт его пробы на уже построенном стенде мыши
2026-09-01 · закрыт: опубликовано c97ee735, аренда WIN-U1 освобождена штатно, слот AVAILABLE. Сверх наряда нога нашла и починила ранний невидимый контакт — capsule мыши шла со стандартным contactOffset 10 мм против настроенных 1 мм у груза — и добавила тест гарантированного промаха с измеряемым зазором 1 см. Обе мины наряда сняты точно: вектор не схлопнут, а чей импульс — говорит имя поля _impulseAppliedByCargoToOther
2026-09-01 · выдан с разрешением на освобождение висящей аренды t-the-mouse-has-a-body-1:BUILD, выданным явно и условно: направление проверило, что спасать нечего — в чекауте ноль изменений, slot/win-u1 равен main; отрицания в шапке сняты БЕЗ масок по путям, по правилу, заведённому часом раньше · history/2026-09-01-s-shape-g-5a7c-wave-11-001.md
END_OF_FILE: live/indie-game-development/cards/c-exec-g-5a7c-a-flying-thing-knocks-the-mouse-down-1-001.md
