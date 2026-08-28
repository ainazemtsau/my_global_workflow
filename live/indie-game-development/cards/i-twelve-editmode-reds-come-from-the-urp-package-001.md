---
id: i-twelve-editmode-reds-come-from-the-urp-package-001
_kind: issue
level: execution
route: work
status: open
_pos: 142
---

## issue
**ДВЕНАДЦАТЬ КРАСНЫХ, У КОТОРЫХ НИ ОДНО УТВЕРЖДЕНИЕ НЕ ПРОВАЛЕНО.**

Замерено ногой `t-scene-restore-1`: двенадцать EditMode-тестов сборки `HouseBuilding` красные, и у
всех двенадцати одно и то же сообщение —

> `Unhandled log message: ... Asset Packages/com.unity.render-pipelines.universal/.../
> ReadonlyMaterialConverterTests.MaterialReferenceBuilder.cs has no meta file, but it is in an
> immutable folder`

Файл действительно лежит в `Library/PackageCache` без `.cs.meta`. Это **дефект поставки пакета
URP**, из репозитория неисправимый. Логика тестов проходит; валит их политика тест-фреймворка
«неожиданная ошибка в консоли = красный».

**ЭТО УЖЕ ТРЕТЬЯ ВСТРЕЧА С ОДНОЙ СТРОКОЙ, И В ЭТОМ ВЕСЬ ВОПРОС.** Две предыдущие ноги наткнулись на
неё и обошли локально, через `LogAssert.ignoreFailingMessages = true` — в `RealAddressConnectionTests`
и в `HouseholderSnapshotOnTheWireTests`. Классы `HouseBuiltEditModeTests` и `HouseFurnishedEditModeTests`
такой защиты не имеют. Тест самой ноги, `FirstHouseInSceneEditModeTests`, среди упавших ОТСУТСТВУЕТ
и проходит.

**Почему не починено на месте:** это правка чужих тестовых файлов, не связанных ни со сценой, ни с
портами, а решение — глушить ошибку в третьем месте или починить один раз централизованно — стоит
принимать отдельно, иначе к пятой встрече в проекте будет пять локальных глушилок и ни одного места,
где это записано как известное.

**Что делает это дороже, чем выглядит:** красное, которое всегда красное и всегда «не наше», через
несколько повторений перестают читать. Ровно это и есть механизм, которым мимо гейта проезжает
настоящий дефект.
## review_when
Первая нога, чей EditMode-прогон в сборке HouseBuilding встанет красным без объяснимой причины в своей работе — тогда решается один раз: глушить централизованно или обновлять пакет. До тех пор каждая нога, встретившая эту строку, обязана назвать её здесь, а не заводить четвёртую локальную глушилку молча.
## evidence
docs/results/c-exec-g-5a7c-scene-restore-1-001.md §«факты, возвращённые наверх», пункт 7; Library/PackageCache/com.unity.render-pipelines.universal/**/ReadonlyMaterialConverterTests.MaterialReferenceBuilder.cs без .cs.meta; обходы в RealAddressConnectionTests и HouseholderSnapshotOnTheWireTests; origin/main @ fd322155.
END_OF_FILE: live/indie-game-development/cards/i-twelve-editmode-reds-come-from-the-urp-package-001.md
