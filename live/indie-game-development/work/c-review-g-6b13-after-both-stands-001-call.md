# CALL — c-review-g-6b13-after-both-stands-001

to: session
direction: indie-game-development
track: хозяин
play: review
node: g-6b13
for: g-6b13
issued: 2026-08-03 by s-work-g-6b13-b3-close-verification-001
status: blocked
unblock_when: |
  Задачи переноски a-4, a-4b, a-5 и a-6 имеют status done, все их продуктовые корни
  возвращены, а владелец дал требуемые словами вердикты. После этого review открывается
  в новой физической задаче, отдельной от последней work-ноги.

goal: |
  Ставка двух стендов получила один честный итоговый вердикт и законный следующий маршрут
  на доказательствах обеих полос.

context: |
  live/indie-game-development/TREE.md g-6b13; live/indie-game-development/NOW.md;
  history/2026-08-03-s-work-g-6b13-b3-close-verification-001.md — полоса хозяина
  завершена binding PASS; история задач a-1…a-6 и b-1…b-3 в NOW/history.
  Полоса хозяина больше не имеет открытой продуктовой работы в этой ставке. Переноска ещё
  не завершена, поэтому этот CALL пока не dispatchable.

boundaries: |
  До выполнения unblock_when не запускать и не выносить владельцу преждевременный verdict.
  Не добавлять задачи, реакции, продуктовую работу или новый bet. Не переписывать карточки
  g-8f31/g-4d7a вместо итогового review; более крупный tree diff маршрутизируется в map.

done_when: |
  Каждый пункт g-6b13.done_when сопоставлен с exact evidence и словами владельца; ставка имеет
  ровно один verdict met|partial|killed|obsolete; TREE/NOW согласованы, обе полосы растворены,
  forecast остаётся no_basis либо получает настоящую калибровку, а следующий узел выбран
  владельцем или сохранён как pending decision.

return: |
  Полный Direction RESULT review с verdict, evidence по четырём пунктам карточки, lens harvest,
  точным tree/NOW diff, forecast, owner words и одним законным следующим frontier.

budget: one fresh physical review session after unblock

END_OF_FILE: live/indie-game-development/work/c-review-g-6b13-after-both-stands-001-call.md
