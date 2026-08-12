RESULT s-solmax-zaratustra-map-owner-approved-checkpoint-025 (call: c-solmax-next-bet-selection-024)
direction: solmax   play: map   node: g-zara

outcome: |
  Владелец утвердил точную шестинодовую карту Zaratustra, её порядок,
  замену незавершённой старой ветки operating-manager и старт с первого
  полезного Health-среза. Утверждённая архитектурная граница —
  Area -> Capabilities/Operations + Workflows -> Runs; локальное красивое
  web-представление является обязательным потребителем структуры уже в
  первом узле.

  Карта пока не переносится в node-карточки: обязательный свежий
  map_evidence отсутствует и владелец его не снимал. Эта checkpoint-нога
  сохраняет точный утверждённый проект без потери решений и открывает одну
  ограниченную research-ногу. Если она не найдёт материального
  противоречия, следующая map-нога записывает карту без повторного опроса
  владельца; только конкретное опровержение возвращается ему на решение.

evidence: |
  Owner verdicts в этой сессии:
  - каждая из исходных карточек 1-6 принята отдельным `A` / `**A**`;
  - порядок принят отдельным `A`;
  - уточнение про семейство/провайдера/режим доступа принято вместе с
    Карточкой 3 словами владельца: "принимаю карточку 3";
  - запрет программного понимания прозы уточнён владельцем: Python работает
    только с metadata и конкретными полями в конкретном формате, а другая
    модель может оценивать прозу;
  - после обсуждения уровней владелец сказал: "модель принимаю" — принята
    модель Area -> Capabilities/Operations + Workflows -> Runs;
  - локальный owner-facing web UI принят отдельным `A`;
  - финальный verdict на показанную итоговую карту, замену старой ветки и
    старт с узла 1: `A`.

  Полный owner-approved draft сохранён в
  work/zaratustra-owner-approved-map-draft-025.md. Он явно отделяет старый
  Health Reclamation как evidence/migration source от нового runtime,
  сохраняет operating-substrate отдельной веткой и запрещает parser,
  regex, compiler или interpreter для свободной прозы.

state_changes: |
  - Add work/zaratustra-owner-approved-map-draft-025.md as the exact
    owner-approved, non-authoritative checkpoint draft consumed by research
    and the returning map leg.
  - Add work/calls/c-solmax-zaratustra-map-evidence-025.md and live call card
    c-solmax-zaratustra-map-evidence-025: play=research, status=ready,
    parent=c-solmax-zaratustra-map-finalize-026.
  - Add work/calls/c-solmax-zaratustra-map-finalize-026.md and live call card
    c-solmax-zaratustra-map-finalize-026: play=map, status=waiting,
    waiting_on=c-solmax-zaratustra-map-evidence-025.
  - Append this full RESULT and the LOG line. Do not change any node, NOW,
    CHARTER, old Health card, operating-substrate card or product repository.

captures: []

decisions_needed: []

play_check:
  - '1 Recite: done — mission, success criteria and current two-branch Solmax tree were restated in owner language.'
  - '2 Candidates & evidence: owner supplied and repeatedly refined the candidate system; fresh map_evidence is still missing and was not waived, therefore a research child is opened before state mutation.'
  - '3 Skeleton: done — the six-node map was shown on one screen and its order was separately accepted.'
  - '4-5 Cards/verdicts: done in owner space — every card was shown separately and accepted, including later exact corrections for evals, routing, opaque prose, Area taxonomy, Health-as-evidence and web-first UI.'
  - '6 Order: done — owner accepted 1 vertical Health slice, 2 context/state, 3 model qualification, 4 extensibility, 5 daily value, 6 governed improvement.'
  - '7 Depth: done — only top-level outcomes are retained; concrete Health capabilities/workflows belong to later convergence/shape.'
  - '8 Lens sweep: done — all six charter lenses are covered; no invented gap node.'
  - '9 Close: checkpoint — G9 owner approval exists, but the play requires fresh map_evidence; no node is written until the child returns.'
  - 'G1/G2: no bet, task or execution lane created; only one ready planning research frontier plus its waiting parent.'
  - 'G10: state changes are carried only by this RESULT; no live state was edited during discussion.'

log: - 2026-08-12 — map Zaratustra checkpoint (s-solmax-zaratustra-map-owner-approved-checkpoint-025): owner approved the six-node Area/Workflow/Run and web-first map, old-branch replacement and Health-first start; exact draft preserved, fresh map_evidence opened before node mutation.

next: |
  c-solmax-zaratustra-map-evidence-025 — fresh research session. It returns
  map_evidence to c-solmax-zaratustra-map-finalize-026; absent a material
  refutation, that map leg writes the already-approved map without reopening
  owner decisions.

END_OF_FILE: live/solmax/history/2026-08-12-s-solmax-zaratustra-map-owner-approved-checkpoint-025.md
