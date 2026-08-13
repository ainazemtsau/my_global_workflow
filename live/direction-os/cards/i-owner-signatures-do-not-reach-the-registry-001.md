---
id: i-owner-signatures-do-not-reach-the-registry-001
_kind: issue
level: direction
route: repair
evidence: history/2026-08-13-s-map-g-one-screen-split-001.md
_pos: 6
---

## issue
Подписи владельца не доезжают до реестра, а живут только в улике. Замер 2026-08-13: `live/direction-os/cards/owner_approved.md` содержит записи ТОЛЬКО от 2026-08-11, ни одной от 2026-08-12, — при том что 2026-08-12 он подписал четыре несущие строки узла сводного экрана (вид экрана, простое изложение, счёт по обоим репозиториям, уход записей о проблемах с первого экрана). Все четыре лежат в `work/converge-g-one-screen.md`, а `os/schema/direction-files.md` объявляет `work/` — «Outputs/evidence, not state». Ядро называет носителем одобрения именно реестр (G9, «RESULT marks `owner_approved`»). Второй случай того же класса, найденный тогда же: отчёт ноги `s-converge-g-one-screen-003` назван датой 2026-08-12, а лёг коммитом 2026-08-13 15:07, — а раздел ИСТОРИЯ берёт день из ИМЕНИ файла (`panel/serve.py:456-458`), и таких расхождений уже 6 из 238 у indie. Оба случая — про одно: запись о том, что произошло, делается по памяти ноги, а не по часам и не по реестру.
END_OF_FILE: live/direction-os/cards/i-owner-signatures-do-not-reach-the-registry-001.md
