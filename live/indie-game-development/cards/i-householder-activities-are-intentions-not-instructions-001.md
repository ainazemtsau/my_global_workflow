---
id: i-householder-activities-are-intentions-not-instructions-001
_kind: issue
_pos: 23
level: execution
route: work
---

## issue
ПЕРЕНОС СЛОВАМИ ВЛАДЕЛЬЦА 2026-08-06: нынешняя пауза в профиле — только доказательство файлового профиля, а не модель жизни хозяина. Будущее занятие описывается НАМЕРЕНИЕМ («готовить в кухне»), исполняется фазами «путь → действие → завершение», его длительность считается ПОСЛЕ прибытия, и у него есть явная политика прерывания и возобновления.
## review_when
В `c-map-real-core-node-001` либо при первом явно принятом в демо занятии хозяина — читать как ВХОД от владельца, а не как пожелание ноги. Закрывается, когда первая реализованная способность несёт все четыре свойства, либо когда он сам их отменит. ЧЕТВЁРТОЕ СВОЙСТВО ПОДКРЕПЛЕНО ИЗМЕРЕНИЕМ REVIEW 2026-08-07 и стало самым срочным из четырёх: клауза карточки «новое событие может снова его отвлечь» опровергнута — во время активной реакции второй шум ДРУГОГО рода отвергается (`Householder.cs:1026-1044`, тест `ASecondDifferentNoiseIsRefused_AndEveryoneElseStillGetsThatTick`), а тест, названный этой клаузой (`ASecondNoiseDuringTheWayBackDistractsHimAgain`), свой случай проверить НЕ МОЖЕТ: его охрана требует `IsSafeToInterrupt`, который на каждом тике движения `false`. То есть явной политики прерывания/возобновления сегодня нет вовсе, а зелёный тест её наличие имитирует.
## evidence
Его слова Направлению в чате возврата 2026-08-06 (дословно в `t-host-3.checkpoint`); согласующийся §«Owner carry-forward — richer activities» в `ae9ce7b1:docs/results/c-exec-g-1d84-householder-profile-file-001.md`; разбор — history/2026-08-06-s-work-g-1d84-householder-profile-return-checkpoint-001.md.
END_OF_FILE: live/indie-game-development/cards/i-householder-activities-are-intentions-not-instructions-001.md
