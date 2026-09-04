# CALL: закрыть Wave 5 и открыть минимальный Steam Store Presence

CALL c-review-g-5a7c-wave-5-steam-minimum-001

to: session
direction: indie-game-development
play: review
node: g-5a7c
for: bet-g-5a7c-wave-5

## goal

Закрыть пятую волну одним честным verdict и оставить один одобренный владельцем маршрут
successor-волны, внешний результат которой — **минимальный Steam Store Presence, принятый Valve**.
Результат включает не только пять скриншотов, но также публичное имя, логотип и обязательные
графические экспорты, тексты/метаданные, обязательный трейлер, фактический checklist конкретного
App, Store Beta preview и отправку Store Presence на ревью.

Сам `review` не создаёт задачи и не пишет developer contract. После owner-readable brief он
останавливается за точными словами владельца; только затем выдаёт отдельный `shape` CALL.

## почему это review, а не прямой наряд разработчику

`bet-g-5a7c-wave-5` утверждён как волна пяти скриншотов и прямо вырезает необходимость ловить
настоящую сессию с четырьмя живыми игроками. Теперь владелец добавил обязательный трейлер,
четырёхпользовательскую удалённую съёмку, сетевой rehearsal и Store Presence целиком. Это меняет
внешний outcome, cut list и зависимости. `day` не имеет права молча переписать волну; сначала её
закрывает свежий `review`, затем successor нарезает `shape`.

## слова владельца — не пересказывать как вывод

- «ВАЖНО что нужно еще и трейлер и тут стоит учитывать что уже добавлен хозяин».
- «это должно записываться с бесплатными анимациями».
- «у нас есть плагин Feel я думаю мы можем добавить какие нить эффекты типа дрожание камеры когда
  идет хозяин».
- Ролик предполагается снимать вчетвером; друзьям должно быть легко подключиться, а необходимость
  `tailnet, radmin etc` должна быть известна и проверена до съёмки.
- «важно что должно включать все факты и действия которые нужно сделать название логотипы все что
  нужно МИНИМАЛЬНО что бы пройти ревью».
- Save boundary: «запускай».

Эти слова разрешают маршрут и задают границу. Они **не** являются verdict пятой волны, выбором
публичного названия, согласием купить лицензию или одобрением придуманного shot list.

## fresh reality, которую надо перемерить в начале ноги

### Direction OS @ `24c66006`

- Активен `bet-g-5a7c-wave-5`; его deadline/appetite — 2026-08-20.
- `t-photoset-1` active; `t-frames-1` waiting.
- `i-steam-appid`: публичное название, base AppID и Steam page не начаты; evidence говорит об одном
  App credit, но реальный Steamworks landing page надо открыть заново.
- `i-steam-demo-gates-unverified` относится к более широкому Next Fest/demo route. Эта нога не
  расширяет Store Presence в demo/build review.
- Background cargo work не принадлежит Wave 5 и не поглощается этим review.

В начале свежего review выполнить fresh Git + `osctl context` и развести **все** живые task/call
Wave 5 по актуальному списку, не только названные выше.

### Product `C:\projects\Unity\GasCoopGame_dev` @ `dev 97ca2c98485f158d3367103b202000481e1e74d7`

На момент выдачи наряда рабочее дерево чистое; это mutable authority, поэтому SHA и строки ниже
перемерить:

- FishNet `4.7.2` + Tugboat; lobby уже умеет Host/Join по введённому IP.
- `NetworkConnectionSettings.asset`: default `127.0.0.1`, UDP `7770`.
- Build Settings: `Lobby.unity` → `IntegratedHouse.unity`. `PhotoSet_LivingRoom.unity` в `dev` пока
  отсутствует.
- Feel импортирован, включая camera-shake feedbacks, но поиск в `Assets/TunnelCrew/**` не нашёл
  подключённого shake для приближения/шага хозяина.
- В `PresentationSettings.asset` тело хозяина всё ещё
  `Bodies/Prefabs/Kenney_CharacterA.prefab`, а не Anton homeowner.
- Файлы `homeowner.fbx` и бесплатные Mixamo clips idle/walk/run/look лежат в
  `Assets/TunnelCrew/Art/Bodies/Sources/Anton/**`, но наличие source-файлов не равно их интеграции
  в игрового хозяина.

### юридический gate, который нельзя спрятать ради срока

`Assets/TunnelCrew/Art/Bodies/Sources/Anton/SOURCE.md` говорит:

- Mixamo-анимации бесплатны/royalty-free для коммерческой игры.
- Геометрия/одежда/волосы Anton homeowner получены через Human Generator из стороннего репака;
  коммерческая лицензия **не подтверждена**.
- До покупки коммерческой лицензии Human Generator эта геометрия не должна попадать во внешний
  билд, публичный скриншот или трейлер.

Текущий `Kenney_CharacterA` имеет сохранённую лицензию CC0 и уже подключён как законный бесплатный
fallback. Review обязан показать владельцу ровно два законных минимальных пути:

1. купить/доказать коммерческую лицензию Human Generator и затем использовать Anton homeowner;
2. сохранить дедлайн без покупки — использовать Kenney CC0 либо другую геометрию с проверенной
   коммерческой лицензией, не выдавая её за финальный арт.

**Рекомендация review по умолчанию:** путь 2 для минимального срочного Store Presence; путь 1 только
по точному слову владельца. Не использовать нелицензированную модель «только в ролике».

## официальная база Valve — verified baseline, не замена checklist App

1. [Store Presence review](https://partner.steamgames.com/doc/store/review_process?language=english):
   обычно 3–5 рабочих дней; подавать минимум за 7 рабочих дней. На странице только launch-content;
   незавершённое удалено либо явно обозначено; capsule title/logo читаем; screenshots — только
   gameplay; description подробное, связное, без внешних ссылок.
2. [Store Page: Building and Editing](https://partner.steamgames.com/doc/store/page?language=english):
   фактическая власть — checklist справа на landing page конкретного App и секции со `*` во всех
   tabs; до публикации проверить Store Beta Mode; готовое уходит через Publish/Prepare for
   Publishing. Публичное имя после pre-release review не меняют обычным редактированием.
3. [Graphical Assets Overview](https://partner.steamgames.com/doc/store/assets?l=english):
   обязательные размеры store, icon и library assets.
4. [Store Graphical Assets](https://partner.steamgames.com/doc/store/assets/standard):
   минимум пять gameplay screenshots, 1920×1080 или больше, 16:9.
5. [Graphical Asset Rules](https://partner.steamgames.com/doc/store/assets/rules):
   в base capsules только artwork, название и официальный subtitle; logo/name читаемы; Library
   Hero без слов; Library Logo — только логотип на прозрачном фоне.
6. [Trailers](https://partner.steamgames.com/doc/store/trailer):
   trailer обязателен в release process; gameplay должен объяснить игру меньше чем за 10 секунд и
   без звука; 1920×1080, 30/29.97 или 60/59.94 fps, 5,000+ Kbps, H.264 + AAC предпочтительны.
7. [Coming Soon](https://partner.steamgames.com/doc/store/coming_soon):
   закончить Store Presence checklist, Mark as ready for review, отправить минимум за 7 рабочих
   дней; approved page можно обновлять после выхода в Coming Soon.
8. [Release Process](https://partner.steamgames.com/doc/store/releasing):
   Store Presence и Game Build — два разных checklist; Store Presence подаётся раньше build review.
9. [October 2026 Next Fest](https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/2026october):
   registration deadline — 2026-08-31 11:59 PM PDT; фестиваль 19–26 октября.

Если документация и реальный App checklist расходятся, записать расхождение и следовать более
конкретному checklist/ответу Valve. Не объявлять неизвестную строку выполненной.

## минимальная матрица результата — ни одной строки не потерять

Review строит одну owner-readable таблицу:

`area | official/actual requirement | current artifact/evidence | status ready/missing/unknown |
missing action | who acts | owner word needed | pass evidence`.

### A. App и публичная идентичность

- Steam Direct App credit/создание App проверены в реальном Steamworks, создан base AppID.
- Утверждено **точное публичное название**: spelling, регистр, пробелы, допустимый официальный
  subtitle. Не использовать рабочее название по догадке.
- Проверены developer/publisher display name, release-date display, Early Access yes/no и другие
  identity/release rows — только те, которые реально требует UI.
- Сделан master logo/wordmark: редактируемый source + transparent PNG. Он читается в самом маленьком
  размере и совпадает с title App.
- На каждое внешнее asset/font/music/animation/model есть source + license evidence; никакого
  watermark, fan art или контента без коммерческих прав.

### B. Фактический checklist страницы и тексты

Открыть `Edit Store Page` и пройти все tabs/секции с `*`. Минимум проверить и записать:

- short description и detailed/About description;
- supported languages;
- categories/features и заявленный player count/co-op только по реально работающему launch scope;
- genres/tags, если их требует конкретный UI/checklist;
- system requirements;
- content/mature-content survey и возрастные строки, которые реально показывает App;
- developer/publisher identity, release date/Coming Soon display;
- legal/copyright fields и любые обязательные notices, если UI их показывает;
- ни одной внешней ссылки в description;
- ни одного кадра, trailer shot или обещания функции, которой нет в доступном launch content.

Не заполнять отсутствующий факт красивым текстом. `unknown` превращается в один точный owner question
или в проверку продукта.

### C. Обязательный графический пакет

Сделать из одного key-art/master logo и проверить точные pixels/format:

| asset | обязательный минимум |
|---|---:|
| Header Capsule | 920×430 |
| Small Capsule | 462×174 |
| Main Capsule | 1232×706 |
| Vertical Capsule | 748×896 |
| Shortcut Icon | 256×256, ICO или PNG |
| App Icon | 184×184, JPG |
| Library Capsule | 600×900 |
| Library Hero | 3840×1240, PNG, **без текста** |
| Library Logo | 1280 px wide и/или 720 px tall, PNG, transparent |
| Library Header Capsule | 920×430 |

Base capsules: только artwork + читаемое game name/logo + официальный subtitle, если утверждён.
Никаких awards, review scores, скидок, дат, «wishlist now», feature bullets и лишнего текста.

### D. Gameplay screenshots

- Не меньше пяти; 1920×1080 или больше, 16:9.
- Только настоящий кадр игры/движка; без concept art, pre-rendered cinematic still, marketing copy,
  awards и письменного описания.
- Постановка допустима только если она честно показывает реальную игру и launch-content.
- Каждый кадр показывает разные читаемые действия/ценность, а не пять вариантов одного угла.
- Минимум четыре кадра отметить suitable for all ages, если содержание это честно позволяет:
  это рекомендация для видимости, не придуманная замена actual review gate.
- `t-frames-1` нельзя закрыть без файлов, загрузки в App, preview и слова владельца «не стыдно»,
  если эта строка остаётся в done_when актуальной волны.

### E. Trailer

Минимальный deliverable:

- один gameplay-first trailer, целевой хронометраж **45–55 секунд**;
- 1920×1080, 60 fps (30 fps допустим только если source стабилен), H.264 MP4, AAC stereo,
  bitrate не ниже 5,000 Kbps;
- смысл считывается без звука; первая механика/угроза видна до 10-й секунды;
- без кинематографического intro, длинных logos и feature cards; title/logo end card — 2–3 секунды;
- custom poster не делать по умолчанию: Steam сгенерирует его. Если генерация плохая, взять
  **кадр из самого видео** 1920×1080 JPG/PNG;
- аудио не является gate: gameplay audio допустим; новая музыка/SFX только с доказанной
  коммерческой лицензией.

Кандидат shot list для owner verdict — сохранить простым и снять одной сессией:

| время | что реально записываем | что доказывает |
|---|---|---|
| 0–7 c | четыре маленьких игрока уже вместе двигают/удерживают крупный узнаваемый loot | co-op hook и масштаб |
| 7–16 c | два угла телекинеза/переноса, видимый beam/status, без постановочного текста | основная механика |
| 16–25 c | хозяин входит/идёт рядом; шаг или proximity запускает лёгкий Feel camera shake | угроза читается без слов |
| 25–35 c | игроки бросают/теряют предмет, прячутся либо расходятся, хозяин реагирует на шум | stealth pressure |
| 35–47 c | короткая погоня/хаос и совместное спасение loot | payoff четырёх игроков |
| 47–52 c | чистый game title/logo на key art | запоминание названия |

Каждая строка снимается только если это реально работает в capture build. Если конкретного действия
нет, review/shape заменяет shot на существующее действие, а не просит разработчика подделать
feature ради ролика.

### F. Preview, submit и evidence

- В Store Beta Mode проверены desktop layout, mobile-ish narrow view где доступно, readability
  small capsule, порядок screenshots и trailer first.
- Actual landing-page checklist зелёный; каждая `*` section заполнена.
- Нажат `Prepare for Publishing`/Publish для накопленных изменений, затем `Mark as ready for
  review`/submit Store Presence.
- Сохранены: AppID, timestamp, checklist screenshot до submit, preview URL/screenshot, confirmation
  submit, список файлов и их hashes/размеры.
- Если Valve возвращает замечания, каждая строка становится отдельной evidence-backed correction;
  не расширять scope превентивно.

## что сознательно НЕ входит в минимальный Store Presence

- Page Background 1438×810 — optional: Steam может сгенерировать его из screenshot.
- Event/announcement assets — только если реально создаётся event/announcement.
- Bundle art, artwork overrides, accolades, broadcast, community cosmetics, trading cards,
  achievements, Points Shop, soundtrack/DLC, localization variants графики.
- Game Build review, demo review, depot/upload, Steamworks SDK integration и October demo gates.
- Steam Lobby/Relay/NAT punch, приглашения Steam и внутриигровая интеграция VPN.
- Больше пяти screenshots, второй trailer, bespoke character animation, cinematic camera system,
  озвучка, новая музыка.

Если actual App checklist помечает любую из этих строк обязательной именно для App, она возвращается
в матрицу с screenshot evidence; иначе не делать.

## минимальный технический capture contract для последующего shape

Это **не задача review**, а точная граница для successor shape и будущего developer CALL.

### Capture build

- Один Windows x64 ZIP из одного verified commit: `.exe` + `*_Data` + `UnityPlayer.dll` и всё, что
  реально выдаёт Unity build. Друзьям Unity-проект, Git, Unity Hub и редактор не отправляются.
- Одна и та же сборка у host + трёх clients; checksum/version показывается в handoff.
- Lobby Host/Join работает по введённому адресу; capture scene доступна из этой сборки и содержит
  только launch-representative gameplay.
- Anton homeowner интегрируется только после legal verdict; иначе остаётся Kenney CC0/approved
  fallback. Уже лежащие Mixamo idle/walk/run/look переиспользуются; bespoke animation запрещена.
- Feel: один малый, отключаемый camera shake от подтверждённого proximity/footstep хозяина; intensity
  ограничена, чтобы не портить motion readability. Никаких новых framework.

### Удалённый rehearsal и съёмка

Default route — [Radmin VPN](https://www.radmin-vpn.com/): официальный сайт описывает бесплатную
виртуальную LAN для Windows 7–11. Не ставить одновременно Tailscale/Radmin «на всякий случай».

1. За день/минимум за несколько часов до съёмки host создаёт Radmin network и передаёт имя/пароль
   друзьям вне репозитория.
2. Все четверо устанавливают только Radmin VPN и распаковывают один Windows build.
3. Host разрешает игре/UDP 7770 во входящем Windows Firewall для нужного сетевого профиля и запускает
   `Host`.
4. Три клиента вводят **Radmin IPv4 host**, не `127.0.0.1` и не публичный IP, затем `Join`.
5. Rehearsal считается зелёным только если все четыре игрока одновременно видят один session,
   двигаются, удерживают loot, видят хозяина и проходят 10 минут без disconnect/desync.
6. Фиксируются screenshot четырёх connected clients, build hash, host Radmin IPv4, фактический порт
   и ошибки. Пароль сети в evidence не сохраняется.
7. Только оператор записи ставит [OBS Studio](https://obsproject.com/kb/quick-start-guide); друзьям
   OBS не нужен. Перед основной сессией записать двухминутный тест Game Capture и проверить
   1920×1080, fps, отсутствие dropped frames и читаемость тёмных сцен.
8. Если Radmin rehearsal красный, не чинить сеть в день съёмки и не интегрировать новый transport:
   shape обязан заранее назвать один fallback rehearsal. Steam networking остаётся вне scope.

## boundaries

- Свежий физический чат обязателен: этот day-чат сформировал маршрут и не судит собственную волну.
- Product repo read-only; review не внедряет Feel, не собирает build, не снимает и не загружает.
- Ни одной новой task/track: их создаёт только downstream `shape`.
- Store Presence/Coming Soon only. Game Build/demo/Next Fest implementation не прятать внутрь.
- Actual Steamworks App checklist сильнее обобщённой памятки.
- Не выводить owner choices: title, legal route, developer/publisher identity, release date mode,
  Early Access и unsupported languages/features требуют его точных слов только если реально
  незакрыты.
- Страница, screenshots и trailer обещают только доступный launch-content.
- Нелицензированная Anton geometry не выходит наружу.

## done_when

1. Один честный verdict `bet-g-5a7c-wave-5` (`met | partial | killed | obsolete`) против его
   forecast/against/kill_by с названной неожиданностью.
2. Каждая живая задача и CALL Wave 5 разведены поимённо: закрыта, убита или перенесена с причиной;
   все lanes волны, если они появились, распущены по правилам review.
3. Семь линз review и дополнительная проверка cut list отработаны; четырёхпользовательская съёмка
   и trailer записаны как изменение scope владельцем, а не как забытая старая работа.
4. Собрана полная матрица A–F из этого CALL и **сверена с реальным App checklist**; у каждой строки
   есть ready/missing/unknown, action, actor и pass evidence.
5. Владельцу показан короткий human brief:
   - recommended verdict волны;
   - точный список обязательного и сознательно optional;
   - публичный title, если его ещё нет;
   - legal choice хозяина (купить/доказать Human Generator либо legal free fallback);
   - один recommended successor contour и кандидат trailer shot list.
6. Review **останавливается** и получает его реальные слова `accepted | revised | rejected | split`
   (или эквивалент по смыслу). CALL/`запускай` не подменяет этот verdict.
7. Только после его слов:
   - закрыта Wave 5 и законно переведён `NOW.bet`;
   - выпущен один самодостаточный `shape` CALL successor-волны;
   - либо, если слов нет, возвращён checkpoint и continuation CALL того же pending review.

## return

Полный RESULT `review`, применённый и закоммиченный в Direction OS, плюс:

- после точного owner verdict — один paste-ready `shape` CALL;
- без verdict — один paste-ready continuation CALL, без самовольного developer task.

## budget

Одна свежая review-нога. Никакого product implementation. Не тратить время на optional assets:
максимум усилий — фактический App checklist, legal gate, честный verdict и точный successor handoff.

END_OF_FILE: live/indie-game-development/work/2026-08-20-call-review-wave-5-steam-minimum.md
