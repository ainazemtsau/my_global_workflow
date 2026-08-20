# ПАСТА ДЛЯ WIN-U2 — ремонт сна A

CALL c-exec-g-5a7c-cargo-sleep-repair-1-002
to: executor
direction: indie-game-development
play: work
node: g-5a7c
task: t-cargo-sleep-1
repo: C:\projects\Unity\GasCoopGame_win-u2
kind: engineering
engineering_contract: 36
slot: WIN-U2
lease: c-exec-g-5a7c-cargo-sleep-repair-1-002:build
basis: 97ca2c98485f158d3367103b202000481e1e74d7
mode: ПРОБА
goal: |
  Ремонт сна A возвращает пик громкости приземления, делает две проверки тишины невакуумными
  и не позволяет живым настройкам оставить физический мир без владельца.
context: |
  Полный предшествующий контракт и происхождение находок:
  live/indie-game-development/work/2026-08-17-paste-cargo-sleep-repair-1.md.
  Автономный фоновый мандат:
  live/indie-game-development/work/2026-08-20-background-cargo-engineering-mandate.md.

  Нога A уже опубликована: candidate 34bd86f1d407389ec697c8b8f912739cbcd37f99,
  RESULT 87a015bd63c7d4a1081ddebc2db5656d4fb169f4, delivery close
  75b770df1d646eb93ff4cbbcc37be58234ac772c. Поздний ремонт -001 не начинался:
  repair candidate/RESULT/integration/delivery отсутствуют. Текущий опубликованный базис
  97ca2c98485f158d3367103b202000481e1e74d7 совпадает на origin/main и origin/dev.

  Три находки повторно подтверждены на этом базисе. CargoBodyContact.Record допускает замену
  первого support-begin более поздним сильным support-контактом, а SituationOf публикует
  SupportForce; существующий wall-vs-support тест не покрывает два support-begin. Два теста
  100-тактовой тишины зелены на старом поведении. CargoSleepThreshold/CargoContactOffset
  возвращают raw values, а takeover/регистрация тела происходят до потенциального throw без
  transactional rollback/finally.

  Product task 01a01df9-bcb2-7ac0-ab5c-64e8e8935378 уже дал claim ACK: WIN-U2 CLAIMED,
  lease c-exec-g-5a7c-cargo-sleep-repair-1-002:build, branch slot/win-u2, clean HEAD
  97ca2c98485f158d3367103b202000481e1e74d7. Unity ещё не запускался, feature-байты не писались.
boundaries: |
  Cargo B0 и его continuation неприкосновенны. Не делать B1, sparse delivery или item-state.
  Не делать beam, screenshots, scenes, art, householder behavior и не изобретать gameplay.
  Не трогать NetworkCargoPresentation.cs, snapshot/RPC/client/transport, девять Grid-authority
  путей, WorldSituationKind, число/значение _cargoGravity, ProjectSettings и чужие файлы хозяина.
  Сохранить попарный затвор, событийную природу громкости и единство источника Landed:
  point, target, vector и force берутся из одного победившего support-контакта. Стена не может
  одолжить силу опоре. Не писать reflection/string-name workaround, дублирующий механизм или
  временный костыль. Не трогать U4 и сохранённые screenshot bytes.

  Работать безопасно рядом с parallel dev. Исполнитель не сливает и не публикует main/dev;
  возвращает candidate/RESULT для отдельной свежей проверки и последующей integration flow.
  Полностью прочитать product AGENTS.md, docs/gas-simulation/PROGRAM.md, validation.config и
  обязательную validation authority до плана. Требуемый инструмент недоступен — честный STOP.
done_when: |
  1. ГРОМКОСТЬ ПРИЗЕМЛЕНИЯ СНОВА РАВНА ПИКУ SUPPORT-КОНТАКТА ЗА ОКНО И ДОКАЗАНА ФИЗИЧЕСКИ.
     Среди support-контактов окна выбирается максимальный по силе; point, target, vector и force
     Landed берутся только из него. Физическая регрессия создаёт два support-begin контакта,
     где поздний сильнее и побеждает; supportForce не подставляется руками. SituationOf/слух
     получает этот пик, а сильная стена не может одолжить ему силу или знак.
  2. ОБА ТЕСТА ТИШИНЫ НЕВАКУУМНЫ И ИМЕЮТ ДОЛГОВЕЧНЫЙ КРАСНЫЙ КОНТРОЛЬ.
     TenSleepingCargoProduceNoSituationsForOneHundredTicks и
     AuthoredSleepingListeningAlarmIsSilentForOneHundredTicks переписаны так, что каждый
     действительно падает на старом поведении f45b08d3 и проходит на repair candidate.
     Сохранены точные команды, имена тестов, counts и seeded/old-behavior negative-control
     evidence; тест, зелёный на старом поведении, удалён или снова переписан.
  3. ЖИВЫЕ РУЧКИ НЕ МОГУТ ЗАМОРОЗИТЬ МИР, А ВЛАДЕНИЕ СИМУЛЯЦИЕЙ ВОЗВРАЩАЕТСЯ ПРИ ЛЮБОМ ВЫХОДЕ.
     CargoSleepThreshold и CargoContactOffset clamp-ятся согласованно с соседними настройками.
     Физический шаг транзакционен: Physics.simulationMode и Physics.gravity восстанавливаются
     после успеха и после исключения, без утечки частичной регистрации/состояния. Проверки
     доказывают zero/invalid knobs и throwing path, включая отсутствие оставшегося Script mode.
return: |
  Candidate commit/ref с точным parent/basis и полный
  docs/results/c-exec-g-5a7c-cargo-sleep-repair-1-002.md. Первая строка — расписка о получении
  3/3 done_when. Для каждой строки: пути реализации и runnable evidence. Для каждого
  переписанного silence-теста: прямое утверждение и evidence, что он был подсажен на f45b08d3,
  упал с count, затем прошёл на candidate. Приложить negative controls, headless и обязательные
  Unity/EditMode outcomes, assumptions/cuts. Вернуть handoff в свежую независимую проверку без
  delivery claim и без публикации product main/dev.
budget: one focused half-day

END_OF_FILE: live/indie-game-development/work/2026-08-20-paste-cargo-sleep-repair-1-u2.md
