---
id: i-panel-cannot-reach-the-game-repo-001
_kind: issue
level: direction
route: map
evidence: history/2026-08-13-s-map-g-one-screen-split-001.md
_pos: 4
---

## issue
Доля работы в систему обязана считать ОБА репозитория — подписано владельцем 2026-08-12 («делай как сказал по всем трем»), — но входа для этого нет физически. Панель ходит в git ровно одной командой с прибитым корнем (`panel/serve.py:19` задаёт `ROOT`, `:148-151` — единственный вызов), конфигурационной поверхности нет вообще: в `panel/` ни одного файла настроек, `getenv`/`environ` в `serve.py` — ноль вхождений, строки `C:/projects/Unity/GasCoopGame` нет нигде в `panel/`, `os/`, `live/` и `osctl.py` вне архива. Единственный тип файла, где такой факт мог бы жить, это запрещает: `os/schema/direction-files.md` — «repo paths, branches, worktrees … are read from that authority at use time, never frozen here». Замер 2026-08-13: без второго репозитория доля читается 14,6 / 17,3 / 27,2%, с ним — 11,2 / 9,3 / 12,3%, то есть на июле знак меры переворачивается. Это не параметр плана, а условие исполнимости подписанной строки: пока входа нет, число премортема 1 на экран встать не может.
END_OF_FILE: live/direction-os/cards/i-panel-cannot-reach-the-game-repo-001.md
