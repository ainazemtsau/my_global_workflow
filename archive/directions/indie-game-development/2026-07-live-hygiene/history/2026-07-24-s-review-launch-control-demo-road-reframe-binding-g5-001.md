RESULT s-review-launch-control-demo-road-reframe-binding-g5-001 (call: owner-direct-demo-road-reframe-binding-g5-20260724)
direction: indie-game-development   track: launch-control   play: review   node/task: g-b847/demo-road-reframe-binding-g5
outcome: |
  REFUTED — binding fresh G5 нашёл material counterexamples в exact history-only DRAFT commit `3006592c2183e1fb752a2038f9570667aa1aabf9`, path `live/indie-game-development/history/2026-07-24-s-research-launch-control-demo-road-reframe-001.md`, blob `4cd208e7d068c067c856e410df186a67f088b7e1`. Exact candidate действительно опубликован в fresh `origin/main`, но proposed Stage-4 delta нельзя принимать или исполнять. Demo Control Room, NOW/TREE, candidate и product repositories не изменены; Stage 4, BUILD, publication и correction-loop не открыты.

  ### Material counterexample 1 — exact delta оставляет copied current truth

  Candidate закрывает перечень изменений фразой `Иных Stage-4 изменений нет`, но не меняет preamble, §2 и соответствующие строки §4/§11 действующей Диспетчерской. После literal apply останутся `Снимок: 22 июля 2026 года`, present-tense `по-прежнему НЕТ`, `сам hook ещё не выбран`, `текущий ... pilot остаётся WAITING` и `production owner пока UNKNOWN`. Эти утверждения могут устареть вне документа и прямо противоречат новому guard `Current realization — read, not copy`. Замена §§6/10/12/14–17 убирает крупные appendices, но не выполняет заявленное удаление copied snapshots/document-maintenance truth полностью.

  ### Material counterexample 2 — C3 stale-parent lineage всё ещё проходит

  Воспроизводится старый false path. Owner принимает Brief `B1`; затем принимается Tree `T1` с exact identity и positive owner/Canon receipt, который не называет parent `B1`; после этого `B2` supersedes `B1`. Proposed installed rule делает non-current только evidence, `provenance которого называет superseded source`, поэтому receipt `T1`, не называющий `B1`, не инвалидируется. `source identity отсутствует → UNKNOWN` тоже не срабатывает: identity `T1` и positive receipt присутствуют. Фраза evidence-секции кандидата про `exact current parent/source identity` не перенесена в exact installed model как обязательная parent-consumption связь. Значит stale `T1` всё ещё может считаться current после `B2`.

  ### Material counterexample 3 — resource graph не полон для safe inclusion-maximal admission

  Proposed exhaustive list называет agents, files/worktrees, Unity/shared surfaces, machines, owner, review, integration и publication, но пропускает отдельно обязательные в owner-approved `g-b847.done_when` вечерние network slots, Deliver и Direction close. Это не синонимы machines/integration: TREE перечисляет их раздельно, а refit receipt фиксирует physical network proof `at most once per day`. Два otherwise independent ready network flows могут поместиться во все перечисленные candidate-ресурсы, но столкнуться за единственный вечерний network slot; candidate graph не имеет поверхности, на которой обязан назвать и сериализовать эту collision. Поэтому inclusion-maximal **safe** set не выведен.

  ### Material counterexample 4 — уникальные evidence boundaries §§3/8 теряются

  Current §8 требует, чтобы uninstructed player понял `state, cause, cooperation и result`, а Distribution proof — `Clean Steam install/connect/relaunch + accepted capture`. Proposed Player envelope требует отдельного uninstructed participant, но не его четыре comprehension outcomes; Package/Public envelopes не требуют combined clean Steam connect и accepted capture. Аналогично exact accepted-tree и per-target proof-receiver/integration-event границы сведены к generic Canon/track receipts. Dated 41→6 pointer не заменяет living non-substitutable proof condition. Поэтому spectator/dirty-session P2 path закрыт, но более широкий Player/Distribution/target evidence contract сохранён не полностью.

  ### Что выдержало опровержение

  - Fresh publication: `FETCH_HEAD=origin/main=HEAD=caa1af6f6f4b1f9ebd5d0f7bfff4eac6b33ec59c`; ancestor check exact candidate→origin/main вернул exit `0`; candidate и fresh main оба разрешают exact path в blob `4cd208e7d068c067c856e410df186a67f088b7e1`.
  - Механика: шесть envelope rows и девять simulation rows присутствуют; old corpus и mapping дают `41/41`, unique `41/41`, duplicates/missing/extra пусты.
  - Limit: exact marker body даёт `1451` whitespace words и `1471` при отдельном подсчёте table pipes — оба ниже `1500`. Встроенное число `1394` не воспроизвелось, но сам hard limit выдержан.
  - Fresh primary readback, slice/build/route provenance invalidation, local-only serialization, immediate refill, P2 named-clean-session/causal-player guard, October-primary/explicit-February-switch и отсутствие фактической Stage-4/BUILD authority выдержали; C3 parent-generation связь, полный resource graph и сохранность evidence boundaries — нет.

  ### Review harvest по CHARTER lenses

  - Commercial / traction: официальные October/February gates и explicit switch guard сохранены, но потеря Steam connect/capture boundary запрещает public authority.
  - Core gameplay depth: causal second-player intervention теперь явен; generic participant/readability не заменяет точную comprehension proof.
  - Co-op-first: spectator и dirty-session false paths P2 закрыты, но accepted-capture/uninstructed-player границы должны оставаться отдельными.
  - Technical feasibility: resource admission обязан отдельно видеть evening network, Deliver и Direction close, иначе safe parallelism переоценён.
  - Scope / production: section-by-section patch снова оставляет prose residue; более простой будущий вариант — одна полная компактная замена living body либо остановка Stage 4.
  - Audience workflow: отдельный uninstructed witness сохранён как роль, но его exact readable outcome и accepted capture потеряны; никакая audience action этим review не открывается.

  Forecast для exact candidate не был записан, поэтому optimistic/pessimistic/wrong-mechanism/wrong-timeline verdict не выдумывается. В exact-candidate scope нет active-bet cut list, поэтому add-back ratio не фабрикуется.
evidence: |
  [ESTABLISHED fresh publication] Непосредственно перед writer apply выполнен fresh `git fetch origin main`. `git rev-parse FETCH_HEAD`, `git rev-parse origin/main` и `git rev-parse HEAD` дали `caa1af6f6f4b1f9ebd5d0f7bfff4eac6b33ec59c`. `git merge-base --is-ancestor 3006592c2183e1fb752a2038f9570667aa1aabf9 origin/main` вернул exit `0`. `git rev-parse <candidate>:<path>` и `git rev-parse origin/main:<path>` оба дали `4cd208e7d068c067c856e410df186a67f088b7e1`; `git cat-file -t` подтвердил `blob`. Worktree был tracked-clean.

  [PROVED residual-copy counterexample] Candidate `live/indie-game-development/history/2026-07-24-s-research-launch-control-demo-road-reframe-001.md:16-109`, особенно exact no-other-change boundary `:109`. Untargeted surviving assertions: `live/indie-game-development/work/launch-control/demo-control-room.md:3,5,43,150,278`. Focused `rg` воспроизвёл каждую строку. Новый read-not-copy guard находится в candidate `:57-59` и не удаляет эти противоречащие ему literals.

  [PROVED C3 counterexample] Exact installed invalidation predicates: candidate `:28,32,45,53,57-59,137`. Они требуют identity/current receipt и инвалидируют descendants только когда provenance называет old source; обязательного consumed-parent identity нет. Candidate assertion `:164` требует `exact current parent/source identity`, но лежит вне `[MODEL-PORTION]` и не меняет exact Stage-4 delta. Исходный `B1→T1→B2` false path и его нарушенный invariant воспроизводятся из `live/indie-game-development/history/2026-07-23-s-review-launch-control-demo-program-v0-binding-005.md:6-14,63`.

  [PROVED resource counterexample] Candidate resource list: `live/indie-game-development/history/2026-07-24-s-research-launch-control-demo-road-reframe-001.md:39`; WIP guard `:43`. Authoritative `live/indie-game-development/TREE.md:63-69`, особенно `:66`, отдельно требует `integration/Deliver/Direction close`, physical machines и evening network slots. Owner-approved refit evidence `live/indie-game-development/history/2026-07-22-s-map-launch-control-demo-control-room-refit-001.md:142,166-167` фиксирует network proof at most once/day и те же отдельные resources.

  [PROVED boundary-loss counterexample] Current living boundaries: `live/indie-game-development/work/launch-control/demo-control-room.md:213-220`, особенно accepted Tree `:215`, target proof receiver/integration event `:216`, uninstructed comprehension `:219` и clean Steam install/connect/relaunch + accepted capture `:220`. Proposed model has only generic participant/readability at candidate `:34` and broad non-substitution at `:71`; focused search finds no `accepted capture`, `install/connect`, `proof receiver`, `integration event` or four-part uninstructed comprehension in the exact installed portion.

  [ESTABLISHED mechanical survivors] Independent root parse of correction-005 headings and crosswalk expansion returned `actual_count=41`, `actual_unique=41`, `mapped_count=41`, `mapped_unique=41`, `missing=[]`, `extra=[]`, `duplicates=[]`. Exact counts returned `envelopes=6`, `simulations=9`. Marker-exclusive count returned `1451` whitespace tokens; counting separated Markdown pipes returned `1471`; both are `<1500`.

  [ESTABLISHED route sources] Fresh official Steamworks readback matches candidate dates/eligibility: October runs `2026-10-19 10:00 PDT`→`2026-10-26 10:00 PDT`, registration `2026-08-31 23:59 PDT`, required items `2026-10-05`; February runs `2027-02-22 10:00 PST`→`2027-03-01 10:00 PST`, registration `2027-01-10 23:59 PST`, required items `2027-02-08`. Sources: https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/2026october?l=english and https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/feb_2027 . Exact owner switch, not elapsed time, remains the candidate authority guard.

  [ESTABLISHED no-authority mutation] `git diff-tree --no-commit-id --name-status -r 3006592c2183e1fb752a2038f9570667aa1aabf9` names only `M live/indie-game-development/LOG.md` and `A` the research history file. Candidate `:170-174` and publication receipt `live/indie-game-development/history/2026-07-24-s-work-publish-launch-control-demo-road-reframe-main-001.md` preserve NOW/TREE/CHARTER/knowledge/Control Room/product repos and deny Stage 4, BUILD, correction-006 or content/route verdict.

  [ESTABLISHED binding independence] This root review is a separate fresh physical session from candidate research, prior validators and publication. Twelve independent read-only subagents supplied only non-binding same-leg pre-passes; root independently reran fresh Git/object, corpus/count, line-level counterexample and official-source checks and formed this binding verdict. Model/provider identity was not used as a gate.

  [LIMIT] This RESULT judges only the exact published DRAFT. It does not modify or adopt the candidate, execute its Stage-4 delta, mutate Demo Control Room/NOW/TREE, open BUILD/publication, touch product repositories or create a correction. A future action requires the owner's simplification choice below and a separate authorized leg.
state_changes: |
  1. Add this complete RESULT exactly once at `live/indie-game-development/history/2026-07-24-s-review-launch-control-demo-road-reframe-binding-g5-001.md` with its exact END_OF_FILE trailer.
  2. Append the exact `log` line below exactly once to `live/indie-game-development/LOG.md` immediately before its current END_OF_FILE trailer.
  3. Preserve every other current file and semantic field unchanged after fresh-state rebase. In particular: no changes to NOW/TREE/CHARTER/knowledge, statuses/open_calls/tracks, `work/launch-control/demo-control-room.md`, candidate/prior reviews/publication receipts, os/**, target/product repositories or user-owned `.claude/`; no Stage 4, adoption, BUILD, publication, route/content/technical verdict or correction-loop.
captures: []
decisions_needed:
  - id: d-demo-road-reframe-post-binding-g5-001
    q: |
      Как упростить путь после REFUTED exact compact-section candidate?
    options:
      - "A — FULL-BODY COMPACT REPLACEMENT: отдельным future research leg заменить весь living body Диспетчерской одним compact artifact с исчерпывающими resource/evidence boundaries и без current snapshots. Минус: более крупный единичный diff потребует новой publication и fresh binding G5."
      - "B — STOP STAGE 4: сохранить текущую принятую Диспетчерскую и оставить этот reframe только history evidence без correction. Минус: copied appendices и maintenance debt останутся, но новая authority не появится."
    recommendation: |
      A — full-body compact replacement. Он устраняет сам источник двух refutation classes: неполный секционный patch и разнесённые по prose parent/resource/evidence predicates. Это только owner choice; candidate или correction этим RESULT не создаётся.
play_check:
  - 1 Verify by refutation: done — exact fresh commit/path/blob and current authority were attacked; reproducible residual-copy, C3 parent-lineage, resource-graph and evidence-boundary counterexamples establish binding REFUTED, while publication/count/limit/P2/route/no-authority claims were separately rederived.
  - 2 Harvest per lens: done — all six CHARTER lenses were answered; the shared lesson is that compactness cannot erase parent provenance, scarce network/close resources or non-substitutable player/distribution evidence.
  - 3 Update the tree: skipped by explicit owner boundary — state changes are review RESULT + one LOG line only; no owner-approved TREE diff exists.
  - 4 Add-back check: skipped with reason — this exact-candidate parallel-track review has no active-bet cut list, so no missed-cut ratio is invented.
  - 5 Knowledge: skipped by explicit owner boundary — all durable findings remain in this review RESULT; no knowledge edit is authorized.
  - 6 Select next: done as owner simplification choice — full-body compact replacement versus stopping Stage 4 is returned with A recommended; neither option is executed and no CALL is created.
  - 7 Close: done — one binding REFUTED RESULT declares history/LOG-only state changes and awaits the owner's choice without Stage 4, BUILD, publication or automatic correction.
log: 2026-07-24 · s-review-launch-control-demo-road-reframe-binding-g5-001 · review · launch-control · g-b847/demo-road-reframe-binding-g5: binding fresh G5 REFUTED exact candidate 3006592c/blob 4cd208e7 because its exact delta leaves copied current truth, permits a C3 receipt without consumed-parent provenance, omits required network/Deliver/Direction-close resources and drops unique player/distribution evidence boundaries; publication, 41/41 crosswalk, <1500 limit, nine simulations, P2 and October/explicit-February guards otherwise survived, with no Stage 4, BUILD or correction opened. → history/2026-07-24-s-review-launch-control-demo-road-reframe-binding-g5-001.md
next: |
  awaiting_decision d-demo-road-reframe-post-binding-g5-001. No correction, Stage 4, BUILD or publication CALL is opened until the owner chooses A or B.

END_OF_FILE: live/indie-game-development/history/2026-07-24-s-review-launch-control-demo-road-reframe-binding-g5-001.md
