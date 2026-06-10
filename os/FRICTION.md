# FRICTION — журнал трения

Append-only. Одна строка на случай: дата, направление/сессия, что именно тёрло. Правка OS разрешена только по точке с ≥2 записями (KERNEL §7).

Формат: `<дата> <направление|os> <play>: <что произошло, одна строка>`

2026-06-10 os design-review: внешнее ревью до пилота, П1–П7 приняты владельцем (guide play, recurring, EXTENDING, truncation guard + collect, stack profiles, repo FRICTION, brainstorm route, binaries) → fixed в коммите "Apply external design review"

END_OF_FILE: os/FRICTION.md
