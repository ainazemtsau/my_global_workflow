---
id: i-analytics-allowed-decide-before-public-build-001
_kind: issue
_pos: 29
level: roadmap
route: work
---

## issue
Владелец решил 2026-08-07 дословно: «пускай аналитика допустима, чтобы она нам не мешала, это отдельно проверка, потом решим». Гейт на `UnityConnectSettings.m_Enabled` не ставится, откатывать флаг после ручной сборки больше не надо. Открытым осталось ровно то, что он сам отложил: включённая аналитика в ПУБЛИЧНОЙ сборке — это сбор данных с чужих игроков, и это решается отдельно, а не наследуется по инерции.

## review_when
Перед первой раздачей сборки кому-либо, кроме него самого — то есть вместе со страницей Steam и демо (`i-steam-appid`, узел `g-2b7f`). Закрывается его словом «оставляем» или «выключаем».

## evidence
Его слова этой сессии, дословно в history/2026-08-07-s-review-g-1d84-integrated-house-partial-001.md §owner_approved; закрытая этим же решением предшественница — `i-manual-build-dirties-tree-and-turns-analytics-on-001`.

END_OF_FILE: live/indie-game-development/cards/i-analytics-allowed-decide-before-public-build-001.md
