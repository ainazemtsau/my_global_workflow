RESULT s-research-launch-control-minimal-authority-001 (call: owner-plain-launch-control-restructure-2026-07-24)
direction: indie-game-development   track: launch-control   play: research   node/task: g-b847/minimal-authority
outcome: |
  ## Исследовательский вывод — DRAFT, структурно не применён

  [INFERRED recommendation] Лучший вариант — **A: сохранить стабильный id `launch-control`, переименовать label в `Demo Release Control` и превратить трек из живого плана в stateless high-level steering role**. Старый `Demo Control Room` не сокращать и не чинить: после отдельного owner verdict его нужно вывести из authority. Новый track, scheduler, dashboard, causal DAG, daily-plan archive или local play не нужны.

  ### Почему текущая конструкция сломалась

  1. [STATED] `work/launch-control/demo-control-room.md` обещал не копировать состояние, но вырос до 586 строк, dated snapshot и §§14–17 с дневными/event appendices. Output стал второй системой истины рядом с TREE/NOW/CALL/RESULT.
  2. [STATED] Попытка заранее описать весь путь как 41 outcome / 133 edges прошла механические проверки, но пропустила stale-parent и ложные player-proof пути; последующее сжатие в шесть envelopes снова было binding-refuted за copied truth, provenance, resource и evidence-boundary gaps.
  3. [STATED] Текущий launch-control root BLOCKED на одном Character result, хотя Grid и Gas READY. Это прямо противоречит `os/plays/work.md`: outcome-dispatch root управляет циклом, его continuation — READY refill, а не ожидание одного foreign result.
  4. [INFERRED] Полный global resource graph и полный future plan принципиально хрупки при изменяемом demo: любой новый факт требует поддерживать ещё одну модель. Нужны локальные proof boundaries и точные source identities, а не новая центральная схема.
  5. [INFERRED] Субъективные `10–15%` сейчас создают ложную точность: нет стабильного scope, critical-path intervals, resource model, duration distributions и сопоставимого throughput.

  ### Целевая архитектура A

  **Постоянная часть — минимальная.** Owner-approved `g-b847` хранит только outcome и operating invariants, hard cap 250 слов, без current status, задач или HOW: выбранное публичное demo выпущено по October 2026 route; February 2027 включается только точными словами владельца; качество доказывается current product/player/Steam evidence; scope режется раньше proof floor; target tracks владеют technical HOW. Текущий basis/horizon/running/cuts в TREE не копируются.

  **Authority.** Owner + Canon владеют смыслом и принятым Demo Contract/basis; Demo Release Control только потребляет его. Root всегда различает `accepted_demo_basis: NONE|artifact@identity` и отдельный `proof_horizon: artifact@identity`. Текущий expedition checkpoint — только DRAFT learning horizon: одна конкретная экспедиция от pre-entry до safe return / partial disaster / wipe. Journey shell сам по себе не доказывает demo; representative proof позже требует хотя бы одного причинного двухигрокового решения, вызванного тогда-current accepted gas/grid behaviour и expedition pressure. Horizon не открывает definition-dependent design/BUILD и не разблокирует Canon.

  **Один одноразовый экран.** На start-day, material return, owner verdict или hard-date checkpoint свежая сессия выводит ≤400 слов: selected route + next hard gate; последний реальный product/player result либо `NONE`; exact accepted basis + proof horizon; running и ranked launchable `0..N` outcomes; named exclusions; `protect / cut-next / cut-trigger`; mechanical route class + next recompute trigger. Экран не копируется в living state; RESULT/history хранит только receipt/evidence.

  **Parallelism.** Owner выбирает 0..N из законного набора. Target activation происходит отдельным target-track leg; controller не мутирует foreign root. Исключение допустимо только из-за current KERNEL/owner WIP rule, отсутствующей authority/dependency либо named shared resource, который занят, недоступен **или UNKNOWN**. Shared resources включают owner attention, worktree/file/Unity surfaces, physical/network machines, review, integration, Deliver, Direction close и Valve queue. Неизвестная доступность не считается свободной; agent count и дополнительная controller quota capacity не доказывают.

  **Definition provenance.** Каждый новый definition-dependent CALL несёт literal `demo_basis: <artifact>@<identity>`; done_when/return требуют echo в RESULT evidence. Независимый CALL несёт bounded `basis_independent: <scope>`. Missing/old identity fail closed. После B1→B2 evidence B1 не считается current, а root попадает в `RECONCILE`; Launch Control его не меняет. Старый `to: executor` CALL без собственного basis guard **никогда не получает product paste/launch**: сначала disposition-only request или target-owned Direction reconciliation, затем target checkpoint/replacement с новым id. Running work остаётся non-dispatchable и reconciles on return. Центральный DAG и новый schema field не нужны.

  **Forecast.** Ровно один class по precedence: (1) `MISSED`, если selected-route hard gate уже прошёл unmet либо eligibility необратимо false; иначе (2) `UNFORECASTABLE`, если отсутствует любой input, нужный для dated critical-path interval; иначе (3) `CREDIBLE`, только если conservative upper bound + owner-set margin проходит каждый следующий hard gate и нет critical blocker; иначе (4) `AT RISK`. Публикуются assumptions, interval, missing inputs и recompute trigger. До отдельного margin verdict и измеримых inputs October честно остаётся `UNFORECASTABLE`, не процентом.

  **Cadence.** Это event-driven refill плюс утренний read при фактическом старте дня и sparse hard-date checks, а не обязательный дневной вопрос, stored Daily Command или quota. Если за день ничего материального не изменилось, новый план не производится.

  ### Законный переход — три отдельных атомарных лега

  Переход нельзя делать одним мегакоммитом; каждый leg имеет собственный play/RESULT/commit:

  1. **Canon-owned work/review:** owner-approved поправка supersedes противоречивое правило в `demo-driven-design-canon-workflow-v1.md`, по которому Launch Control владеет Demo Contract; Canon/owner сохраняют definition authority. Canon root заменяется target-owned checkpoint без DCR pointer и остаётся WAITING на accepted basis либо exact Canon-compliant override.
  2. **Owner-approved map:** `g-b847` переписывается в release outcome + ≤250-word contract; label становится `Demo Release Control`, стабильные `launch-control` и `outcome_dispatch` сохраняются. Старый Launch root остаётся недиспетчеризуемым на время перехода.
  3. **Launch-controlled work/repair:** BLOCKED DCR-dependent root заменяется self-contained READY refill, все remaining live/panel pointers мигрируют, а `demo-control-room.md` становится короткой historical/not-authority tombstone. Только после этого стартует probe.

  Старый DCR не tombstone до третьего leg; между legs definition-dependent work не получает новый launch. Так сохраняются one-play/one-RESULT и foreign-track authority.

  ### Falsifiable operating probe

  Pre-register один seven-day window и оценить первые три consecutive qualifying material returns; ни один intervening controller/owner leg не пропускается, <3 returns = `INCONCLUSIVE`. Каждый cycle pin-ит Git HEAD, TREE/NOW blobs, CALL ids, accepted basis/horizon, official URL + retrieval time + relevant extracted values/content hash. Нормализованный output: `(call-id, source identity, launch|exclude|reconcile, reason, collision surface)`, running set, route class, protect/cut-next/trigger.

  Обязательные cases: B1→consumer→B2 negative control; independent-work control; shared-resource collision/UNKNOWN. Root READY на входе/выходе; DCR reads/edits, copied status narrative, technical HOW, guessed percent и uncited basis = 0. Каждый screen ≤400 слов; combined active controller+owner attention ≤30 минут/cycle. Active intervals exclude unattended build/test/network/queue waits and overlap is not double-counted. Management-vs-delivery time записывается только как diagnostic, не PASS gate. Любой FAIL разрешает добавить только один доказанно недостающий механизм; отдельный binding fresh G5 проверяет installed result после probe.

  ### Отброшенные альтернативы

  - **B — убрать отдельный track:** технически возможно, но делает владельца постоянным global arbiter и теряет bounded cross-track outcome requests.
  - **C — передать authority в Program:** уменьшает число ролей, но создаёт integration bias и сейчас завязывает release steering на BLOCKED Program root.
  - **Чинить/сжимать DCR, строить новый dashboard/DAG/Gantt или fixed daily queue:** воспроизводит уже наблюдавшийся failure class.

  [CURRENT STATE] Ничего из архитектуры A этим RESULT не принято и не установлено. Текущие TREE, track label, BLOCKED launch-control root, Canon root/workflow и Demo Control Room сохраняются дословно; добавлена только pending owner decision.
evidence: |
  [STATED owner/problem source] User attachment `C:\Users\Anton\.codex\attachments\656ce319-27d3-43ec-a9df-047028d3f7dd\pasted-text.txt` and the owner message of 2026-07-24: mutable demo, October primary/February fallback, high-level outcome steering, owner-controlled parallel launches, no technical HOW and no monolithic fixed plan.

  [STATED current authority] `os/KERNEL.md`; `os/plays/research.md`; `os/plays/work.md:34`; `os/schema/packets.md`; `os/schema/direction-files.md:127-149`; `live/indie-game-development/CHARTER.md`; `TREE.md:63-69`; full `NOW.md`; `work/launch-control/demo-control-room.md`; current launch-control and Canon root CALLs; `work/demo-workflow/demo-driven-design-canon-workflow-v1.md`; `history/2026-07-24-s-repair-demo-working-hypothesis-checkpoint-g10-001.md`; `history/2026-07-24-s-review-launch-control-demo-road-reframe-binding-g5-001.md`; earlier binding-005 review.

  [STATED official route facts] October: https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/2026october?l=english — registration 2026-08-31 23:59 PDT, required items 2026-10-05, event 2026-10-19 10:00 PDT through 2026-10-26 10:00 PDT, public store page/demo and one-Next-Fest eligibility. February: https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/feb_2027 — registration 2027-01-10 23:59 PST, required items 2027-02-08, event 2027-02-22 10:00 PST through 2027-03-01 10:00 PST. Review: https://partner.steamgames.com/doc/store/review_process?language=english — typical 3–5 business days, plan at least 7 business days. Demo mechanics/page/build: https://partner.steamgames.com/doc/store/application/demos?l=english.

  [INFERRED practice fit] Rolling-wave/high-level release planning with near-term detail: https://www.pmi.org/blog/optimize-your-project-life-cycle-using-agile. Working evidence, welcome change and regular adaptation: https://agilemanifesto.org/principles.html and https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf. Fixed time with variable scope and unknown-first work: https://basecamp.com/shapeup/1.2-chapter-03 and https://basecamp.com/shapeup/3.4-chapter-13. Tiny-team playtest loop: https://media.gdcvault.com/gdc2026/Slides/Cronin_Brian_PlaytestingProcessForUltraSmallTeams.pdf. Reporting should not add counterproductive work: https://www.gov.uk/service-manual/agile-delivery/measuring-reporting-progress. Probabilistic schedule confidence requires integrated scope/dependencies/duration distributions rather than a guessed percentage: https://standards.nasa.gov/sites/default/files/standards/MSFC/A/0/msfchdbk3684a.pdf.

  [ESTABLISHED investigation] Five independent nominal-group generators plus two failure-inversion/baseline searches converged on stateless steering and rejected another living plan. Three initial same-session validators refuted missing migration, weak expedition acceptance, ambiguous forecast and non-falsifiable probe criteria; root incorporated all material findings. Three further fresh same-session validators then attacked the repaired package; root accepted the remaining transaction-topology, conflicting Canon authority, UNKNOWN-resource, stale executor-root and time-accounting counterexamples. These are in-session pre-passes only, not binding G5.

  [LIMITS] Private Steamworks eligibility/AppIDs/current registration, an accepted Demo Contract/basis, final content, measured throughput/durations/resources and an owner-set forecast margin are unavailable. Current class is therefore UNFORECASTABLE unless a higher-precedence MISSED fact appears. No adoption, route switch, product work or binding close is claimed.

  [FRESH APPLY BASE] Immediately before apply, `git fetch origin main` succeeded; HEAD `22ef60281c01eec75e213a49bc392be48b590877`, origin/main `caa1af6f6f4b1f9ebd5d0f7bfff4eac6b33ec59c`, divergence `0 behind / 1 ahead`, tracked worktree clean.
state_changes: |
  1. `live/indie-game-development/NOW.md`: set `updated` to `2026-07-24 by s-research-launch-control-minimal-authority-001`; add pending decision `d-launch-control-minimal-authority-001` under track `launch-control` with the exact A/B/C options and recommendation below; preserve every track, ordinary/outcome CALL, status, receipt, task, recurring item and all unrelated semantics exactly.
  2. `live/indie-game-development/work/board/dashboard.html`: regenerate existing owner-panel mirrors only — update render stamp, decision count `0 → 1`, add one full-width plain-language card for `d-launch-control-minimal-authority-001`, add the 24 July research journal item, retain only 24/23/22 July, preserve current open-work cards and open findings.
  3. `live/indie-game-development/LOG.md`: append the exact `log` line below once before its EOF trailer.
  4. Add this full RESULT exactly once at `live/indie-game-development/history/2026-07-24-s-research-launch-control-minimal-authority-001.md` with its exact EOF trailer.
  5. Preserve every other file and meaning unchanged. Specifically do NOT edit TREE/CHARTER/knowledge/os/**, tracks/labels/outcome_dispatch, any open CALL/root/status, `demo-driven-design-canon-workflow-v1.md`, either Canon/launch-control CALL artifact, `demo-control-room.md`, product/Canon repositories, route selection or forecast state; do not start any transition leg, target work, BUILD, publication or binding G5.
captures:
  - После owner verdict A переход выполняется ровно тремя отдельными atomic legs: Canon authority/root → map outcome/label → Launch root/tombstone/probe.
  - Steam recurring sentinel рассматривается только если seven-day probe докажет, что owner/event checkpoints пропускают hard-date checks.
decisions_needed:
  - id: d-launch-control-minimal-authority-001
    track: launch-control
    q: Какую архитектуру управления выпуском demo принять вместо действующей Demo Control Room?
    options:
      - A — сохранить `launch-control` как stateless `Demo Release Control`; тремя atomic legs передать Demo Contract authority Canon/owner, переписать g-b847, поставить READY refill, tombstone DCR и запустить deterministic seven-day probe.
      - B — удалить отдельный control track/outcome_dispatch и оставить owner-mediated global frontier из TREE/NOW.
      - C — передать outcome_dispatch в Program и удалить отдельный launch-control track.
    recommendation: A — сохраняет high-level cross-track steering и owner choice 0..N, использует существующий OS без новой living plan surface, не смешивает integration с release authority и имеет измеримый fail-fast probe.
play_check:
  - 1 Recite: done — bounded research question restated as choosing a robust high-level demo-release management architecture; no structure/product mutation and no owner input required before investigation.
  - 2 Investigate: done — full owner attachment, current Direction authority/failure lineage, official Valve sources and primary planning/playtest sources were read; five independent generators plus two strategic failure-inversion searches were parent-merged/deduped.
  - 3 Confidence: done — established/inferred/unknown are separated; two rounds of three fresh same-session validators attacked exact claims; every material refutation was accepted into the final three-leg transition, authority, UNKNOWN-resource, stale-root, forecast and probe rules; validation remains explicitly non-binding.
  - 4 Close: done — one decision-ready research RESULT records the recommended architecture, alternatives, lawful migration and deterministic probe; only pending decision/history/LOG/panel state changes are declared, with no adoption or downstream CALL.
log: 2026-07-24 — research (g-b847/minimal-authority, s-research-launch-control-minimal-authority-001): converged the failed Demo Control Room/DAG/envelope lineage into decision-ready option A — stateless Demo Release Control with Canon-owned definition, READY event refill, exact basis provenance, mechanical no-percent forecast, three-leg migration and deterministic seven-day probe; A/B/C owner verdict is pending, no structure, root, DCR or product work changed. → history/2026-07-24-s-research-launch-control-minimal-authority-001.md
next: |
  awaiting_decision d-launch-control-minimal-authority-001

END_OF_FILE: live/indie-game-development/history/2026-07-24-s-research-launch-control-minimal-authority-001.md
