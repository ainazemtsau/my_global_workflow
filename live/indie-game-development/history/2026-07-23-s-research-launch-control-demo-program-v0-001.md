RESULT s-research-launch-control-demo-program-v0-001 (call: owner-delegated-demo-director-stage2-2026-07-23)
direction: indie-game-development   track: launch-control   play: research   node/task: g-b847/demo-program-v0-stage-2
outcome: |
  ## DRAFT demo-program-v0

  [STATED] Это research-кандидат причинной Program Model, построенный назад от наблюдаемой публично готовой Steam-demo на свежем `origin/main@4a33f386`. Он НЕ ПРИНЯТ, не является активной Program Model, не меняет Demo Contract, October/February promise, MUST/CUT или authority треков.

  [STATED] У каждого outcome ровно девять полей. `Parent/link` перечисляет прямых потребителей (`used_by`), `Зависимости` — прямые prerequisites; внутренние edges зеркальны. Поля current status намеренно нет: будущая реализация вычисляется из owning-track receipts и evidence. Product handback/merge/test/LOOK — evidence, но не binding Direction close.

  ### S0 — публично готовая Steam-demo
  - Наблюдаемый результат: [UNKNOWN current realization] внешний аккаунт на публичной base-game page видит demo, чисто устанавливает её, два холодных игрока на двух физических ПК проходят один causal co-op attempt, получают единый authoritative result, повторяют запуск; воспроизводимый signature moment понятен и пригоден для capture.
  - Parent/link к демо: [STATED] terminal root; прямых потребителей нет.
  - Зависимости: [STATED] S14.
  - Условие доказанности: [STATED] public URL + anonymous store smoke + clean install/connect/full-loop/result/relaunch receipt на точном live build, без developer assistance.
  - Owning track: [STATED] Launch Control координирует; Marketing/Presentation/Program сохраняют свои функции; [UNKNOWN] точный credentialed release operator.
  - Временной рубеж: [STATED] к 19 Oct 2026, если владелец выбирает October Next Fest; [UNKNOWN] внутренняя дата готовности.
  - Proposal: [INFERRED] PROPOSED MUST только для выбранного October route; owner promise не подразумевается.
  - Ключевая неопределённость: [UNKNOWN] Hook/Contract, доказанный remaining path и route verdict отсутствуют.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/launch-control/demo-control-room.md:41-56,209-250`; https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/2026october?l=english

  ### S1 — private Steam admin inventory
  - Наблюдаемый результат: [UNKNOWN current realization] first-hand readback фиксирует partner/account good standing, tax/bank/identity, app credit, permissions, communications, primary/backup operator — без мутации и публикации.
  - Parent/link к демо: [INFERRED] direct consumer S2.
  - Зависимости: [STATED] нет внутренних; нужен authorized readback.
  - Условие доказанности: [STATED] dated Steamworks screenshots/export с account/app/permission facts и именованными evidence owners.
  - Owning track: [STATED] Marketing + owner-admin; [UNKNOWN] credentialed primary/backup operator.
  - Временной рубеж: [UNKNOWN] нет свежего readback и lead time; Jul 12 snapshot недостаточен.
  - Proposal: [INFERRED] PROPOSED MUST для October eligibility; это inventory, не запуск публичной работы.
  - Ключевая неопределённость: [STATED as of 2026-07-12, UNKNOWN now] apps отсутствовали, один paid credit был не использован, title не выбран.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/marketing/claude-code-handoff-c-marketing-wake-001-2026-07-12.md:14-24,70-77`; `live/indie-game-development/work/marketing/questions/q-capture-setup.md:15-22`.

  ### S2 — owner-gated base-app activation
  - Наблюдаемый результат: [UNKNOWN] владелец выбирает title/activation, paid credit создаёт base-game AppID, права и factual configuration подтверждены; публичная page ещё не подразумевается.
  - Parent/link к демо: [INFERRED] direct consumers S3, S7.
  - Зависимости: [STATED] S1 + отдельные фактические слова/действие владельца.
  - Условие доказанности: [STATED] title verdict, base AppID receipt, permissions readback и audit trail activation.
  - Owning track: [STATED] Marketing + owner; [UNKNOWN] credentialed operator.
  - Временной рубеж: [UNKNOWN] activation duration; должен предшествовать S3/S7.
  - Proposal: [INFERRED] PROPOSED MUST, если сохраняется October option; кандидат title не выбирает.
  - Ключевая неопределённость: [UNKNOWN] title, actual authority и текущая partner readiness.
  - Evidence: [PROVED/STATED pointers] marketing handoff above; `live/indie-game-development/work/launch-control/demo-control-room.md:276-283`; https://partner.steamgames.com/doc/gettingstarted/appfee

  ### S3 — review-ready truthful base-page packet
  - Наблюдаемый результат: [INFERRED] base-game store packet готов к review и содержит только claim-by-claim доказанные текущие факты; unsupported demo-specific claims отсутствуют.
  - Parent/link к демо: [INFERRED] direct consumer S4.
  - Зависимости: [STATED] S2 + claim evidence ledger; [UNKNOWN] минимальный честный claim set.
  - Условие доказанности: [STATED] complete base store checklist, gameplay-only screenshots where claimed, readable title/logo, provenance pointers for every feature statement.
  - Owning track: [STATED] Marketing; Presentation/Program поставляют proof; owner сохраняет public voice gate.
  - Временной рубеж: [UNKNOWN] должен оставить review/rework margin перед S5/S6; asset lead отсутствует.
  - Proposal: [INFERRED] PROPOSED MUST для October registration; broad campaign PROPOSED CUT.
  - Ключевая неопределённость: [UNKNOWN] можно ли собрать честную минимальную page до representative demo proof без фиксации ложного обещания.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/NOW.md:84-92`; `live/indie-game-development/work/program-v2-integration-lab-plan.md:277-290`; https://partner.steamgames.com/doc/store/review_process

  ### S4 — base-page Valve approval
  - Наблюдаемый результат: [UNKNOWN] base-game store presence получила Valve approval.
  - Parent/link к демо: [INFERRED] direct consumer S5.
  - Зависимости: [STATED] S3.
  - Условие доказанности: [STATED] Steamworks review-success receipt именно для base store presence; approval не считается QA demo.
  - Owning track: [STATED] Valve external reviewer; Marketing submitter.
  - Временной рубеж: [STATED] Valve обычно 3–5 business days, проекту велено планировать минимум 7 business days с исправлениями; [UNKNOWN] rework.
  - Proposal: [INFERRED] PROPOSED MUST для S5/S6.
  - Ключевая неопределённость: [UNKNOWN] submission date и correction count.
  - Evidence: [PROVED/STATED pointer] https://partner.steamgames.com/doc/store/review_process

  ### S5 — публичная Coming Soon base page
  - Наблюдаемый результат: [UNKNOWN] approved base page явно опубликована и доступна публично как Coming Soon.
  - Parent/link к демо: [INFERRED] direct consumers S6, S14.
  - Зависимости: [STATED] S4 + explicit publish action.
  - Условие доказанности: [STATED] anonymous public URL/readback и correct app identity.
  - Owning track: [STATED] Marketing + owner public-action gate.
  - Временной рубеж: [STATED] должна предшествовать 31 Aug registration; [UNKNOWN] фактическая latest-safe submission/publication date.
  - Proposal: [INFERRED] PROPOSED MUST для October eligibility.
  - Ключевая неопределённость: [UNKNOWN] approved assets и credentialed publisher.
  - Evidence: [PROVED/STATED pointers] https://partner.steamgames.com/doc/store/coming_soon; https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest

  ### S6 — October registration receipt
  - Наблюдаемый результат: [UNKNOWN] владелец сохраняет October option: регистрация base app сохранена и green check подтверждён; это не участие и не demo completion.
  - Parent/link к демо: [INFERRED] direct consumers S11, S14.
  - Зависимости: [STATED] S5 + фактическое owner action; альтернативой является explicit abandon October, не автоматический February.
  - Условие доказанности: [STATED] Steamworks registration receipt и eligibility readback.
  - Owning track: [STATED] owner + Marketing/Launch Control coordination.
  - Временной рубеж: [PROVED/STATED] 31 Aug 2026 11:59pm PDT; пропуск без receipt делает October MISSED.
  - Proposal: [INFERRED] PROPOSED MUST только для сохранения October; кандидат не решает route.
  - Ключевая неопределённость: [UNKNOWN] owner verdict и eligibility; registration reversible, participation one-use.
  - Evidence: [PROVED/STATED pointer] https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/2026october?l=english

  ### S7 — associated demo AppID
  - Наблюдаемый результат: [UNKNOWN] отдельный demo AppID создан из base app, связан с ним и имеет нужные permissions/configuration surfaces.
  - Parent/link к демо: [INFERRED] direct consumers S8, S9.
  - Зависимости: [STATED] S2 + owner-gated app action.
  - Условие доказанности: [STATED] first-hand association/AppID/config receipt; отдельная demo store page остаётся optional.
  - Owning track: [STATED] Marketing + owner-admin; Program подключается к depot/build, не к public claims.
  - Временной рубеж: [UNKNOWN] должен предшествовать S8/S9; duration отсутствует.
  - Proposal: [INFERRED] PROPOSED MUST для Steam demo.
  - Ключевая неопределённость: [UNKNOWN] permissions/operator и current App Admin state.
  - Evidence: [PROVED/STATED pointer] https://partner.steamgames.com/doc/store/application/demos?l=english

  ### S8 — review-ready demo store packet
  - Наблюдаемый результат: [UNKNOWN] demo store presence/content survey/settings и demo-specific claims готовы к submission и соответствуют реально доказанному candidate.
  - Parent/link к демо: [INFERRED] direct consumer S11.
  - Зависимости: [STATED] S7, C2, P1, P5, P6, P7, T7.
  - Условие доказанности: [STATED] checklist complete; claims/capture traceable to exact representative evidence; separate demo page не требуется.
  - Owning track: [STATED] Marketing + Presentation; Program supplies build truth; owner public voice gate.
  - Временной рубеж: [UNKNOWN] до S11; asset/review-rework durations отсутствуют.
  - Proposal: [INFERRED] PROPOSED MUST для demo review; broad marketing PROPOSED CUT.
  - Ключевая неопределённость: [UNKNOWN] final Contract claims, capture and page form.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/program-v2-integration-lab-plan.md:277-290`; https://partner.steamgames.com/doc/store/application/demos?l=english

  ### S9 — exact demo depot/default-branch package
  - Наблюдаемый результат: [UNKNOWN] exact representative candidate загружен в demo depots, назначен intended/default branch, имеет manifest/build lineage и lawful test access.
  - Parent/link к демо: [INFERRED] direct consumers S10, S12.
  - Зависимости: [STATED] S7, P3, P4, P6, P7, P8, T7, T8.
  - Условие доказанности: [STATED] AppID/depot/build/branch receipt, manifest hash, reproducible packaging command and clean entitlement test.
  - Owning track: [STATED] Program owns candidate/runtime; [UNKNOWN] credentialed Steam build operator.
  - Временной рубеж: [UNKNOWN] packaging pipeline/lead absent; must precede S10/S12.
  - Proposal: [INFERRED] PROPOSED MUST.
  - Ключевая неопределённость: [CONFLICT] CHARTER product repo authority stale; candidate must name one reconciled canonical lineage.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/CHARTER.md:92-98`; `live/indie-game-development/work/launch-control/demo-control-room.md:217-222`; https://partner.steamgames.com/doc/sdk/uploading

  ### S10 — exact-candidate clean hosted go/no-go
  - Наблюдаемый результат: [UNKNOWN] intended Steam branch проходит clean two-PC install/launch/host-join/full-loop/result/relaunch on named supported environments; любой candidate change invalidates receipt.
  - Parent/link к демо: [INFERRED] direct consumers S11, S12, S14.
  - Зависимости: [STATED] S9, P1, P2, P3, P7, P8, T7.
  - Условие доказанности: [STATED] non-dev/test accounts, exact build, two physical machines, checklist, failure capture, negative path and post-change rerun.
  - Owning track: [STATED] Program/Multiplayer + Presentation performance; owner supplies machine window; [UNKNOWN] named hardware/logistics provider.
  - Временной рубеж: [UNKNOWN] before submission and again before release; machine windows/duration missing.
  - Proposal: [INFERRED] PROPOSED MUST; Valve review cannot substitute.
  - Ключевая неопределённость: [UNKNOWN] machine pair, supported OS/spec, runbook and evidence receiver.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/launch-control/demo-control-room.md:195-222,276-281`; https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest

  ### S11 — demo store-presence review submission
  - Наблюдаемый результат: [UNKNOWN] required demo/store presence items submitted for review; submission is not approval.
  - Parent/link к демо: [INFERRED] direct consumers S12, S13.
  - Зависимости: [STATED] S6, S8, S10.
  - Условие доказанности: [STATED] Steamworks submission timestamp and empty local blocker checklist.
  - Owning track: [STATED] Marketing + credentialed operator; Launch Control coordinates route.
  - Временной рубеж: [PROVED/STATED] no later than 5 Oct 2026 for October; optional Press Preview 21 Sep is CUT first.
  - Proposal: [INFERRED] PROPOSED MUST if October retained.
  - Ключевая неопределённость: [UNKNOWN] correction queue and operator.
  - Evidence: [PROVED/STATED pointers] official October page above; https://partner.steamgames.com/doc/store/releasing

  ### S12 — demo build review submission
  - Наблюдаемый результат: [UNKNOWN] exact S9 build submitted after store presence submission, with S10 go/no-go still valid.
  - Parent/link к демо: [INFERRED] direct consumer S13.
  - Зависимости: [STATED] S9, S10, S11.
  - Условие доказанности: [STATED] build-review submission receipt naming exact build/branch and preceding store submission.
  - Owning track: [STATED] Program + credentialed operator.
  - Временной рубеж: [PROVED/STATED] no later than 5 Oct 2026 for October; internal latest-safe UNKNOWN.
  - Proposal: [INFERRED] PROPOSED MUST if October retained.
  - Ключевая неопределённость: [UNKNOWN] resubmission and post-submission candidate changes.
  - Evidence: [PROVED/STATED pointers] https://partner.steamgames.com/doc/store/releasing; official October page above.

  ### S13 — Valve approval of demo surfaces/build
  - Наблюдаемый результат: [UNKNOWN] required submitted store/demo surfaces and exact build are approved; this is an external configuration gate, not QA.
  - Parent/link к демо: [INFERRED] direct consumer S14.
  - Зависимости: [STATED] S11, S12.
  - Условие доказанности: [STATED] first-hand approval readback for both surfaces; S10 remains separately green.
  - Owning track: [STATED] Valve external reviewer; Marketing/Program receive feedback.
  - Временной рубеж: [STATED] typical 3–5 business days, plan at least 7 plus correction; [UNKNOWN] actual queue.
  - Proposal: [INFERRED] PROPOSED MUST.
  - Ключевая неопределённость: [UNKNOWN] correction cycles; approval does not auto-release.
  - Evidence: [PROVED/STATED pointers] https://partner.steamgames.com/doc/store/review_process; https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest

  ### S14 — manual release and live operations
  - Наблюдаемый результат: [UNKNOWN] operator executes `Release Demo`, republishes base page, anonymous user sees Download Demo, post-live representative smoke stays green, monitoring/support and deactivate/reactivate rollback are ready.
  - Parent/link к демо: [INFERRED] direct consumer S0.
  - Зависимости: [STATED] S5, S6, S10, S13.
  - Условие доказанности: [STATED] release/republish receipts, public URL smoke, clean public install/loop receipt, named monitor and rehearsed distribution rollback; copied builds outside Steam remain a documented limit.
  - Owning track: [STATED] Marketing/Launch Control/Program + owner; [UNKNOWN] credentialed primary/backup operator.
  - Временной рубеж: [PROVED/STATED] by 19 Oct 2026 if October retained; duration/rollback lead UNKNOWN.
  - Proposal: [INFERRED] PROPOSED MUST.
  - Ключевая неопределённость: [UNKNOWN] support/rollback operator and public incident threshold.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/launch-control/stabilization-baseline.md:134-135`; https://partner.steamgames.com/doc/store/application/demos?l=english

  ### P1 — final unfamiliar-player hosted proof
  - Наблюдаемый результат: [UNKNOWN] unfamiliar player on supported hosted path, without architecture explanation, identifies state, cause, cooperation, signature moment and result.
  - Parent/link к демо: [INFERRED] direct consumers S8, S10.
  - Зависимости: [STATED] P2, P3, P5, P6, P7, P8, T7 + [UNKNOWN] recruitment/accounts/consent/capture logistics.
  - Условие доказанности: [STATED] scripted observation + falsification rubric + participant words/actions + evidence disposition; an early local probe may run after P6 as PROPOSED SHOULD but does not close P1.
  - Owning track: [STATED] Canon/Presentation receive meaning/readability proof; [UNKNOWN] logistics owner.
  - Временной рубеж: [UNKNOWN] participant source, scheduling lead and duration.
  - Proposal: [CONFLICT] PROPOSED MUST for final release ladder; accepted Skeleton calls the early probe SHOULD.
  - Ключевая неопределённость: [UNKNOWN] participant pool and exact reject threshold; this proof does not close full Canon/Presentation nodes.
  - Evidence: [PROVED/STATED pointer] `live/indie-game-development/work/launch-control/demo-control-room.md:58-64,209-222`.

  ### P2 — two-machine authoritative causal co-op
  - Наблюдаемый результат: [UNKNOWN] two physical PCs reach one authoritative result, second player causally changes outcome, divergence fails loudly.
  - Parent/link к демо: [INFERRED] direct consumers S10, P1.
  - Зависимости: [STATED] P3, P4, P6, P7, T7, T8 + [UNKNOWN] named machine pair/evening slot.
  - Условие доказанности: [STATED] repeat run with same result/digests plus deliberate divergence negative control and capture.
  - Owning track: [STATED] Program/Multiplayer; capability tracks supply inputs.
  - Временной рубеж: [UNKNOWN] exact candidate/machines/run window; at most one real evening run/day is stated, not duration.
  - Proposal: [INFERRED] PROPOSED MUST; 8-player/dedicated/late join/full failure matrix PROPOSED CUT.
  - Ключевая неопределённость: [UNKNOWN] exact authority/host-loss scope; this proof does not close full Program/Grid/Gas nodes.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/launch-control/demo-control-room.md:47-56,195-222,248-250,280-281`.

  ### P3 — minimal player-facing host/join/start UX
  - Наблюдаемый результат: [INFERRED] players can intentionally host/invite-or-join, see readiness, start one attempt and exit/retry without developer action.
  - Parent/link к демо: [INFERRED] direct consumers S9, S10, P1, P2, P8, T8.
  - Зависимости: [STATED] C2, C3, C4, T1.
  - Условие доказанности: [INFERRED] cold two-player traversal of exact accepted lifecycle; unsupported transitions fail clearly.
  - Owning track: [STATED] Canon owns experience meaning; Program/Multiplayer owns runtime UX; exact UI implementer stays inside owning route.
  - Временной рубеж: [UNKNOWN] Contract lifecycle and effort absent.
  - Proposal: [INFERRED] PROPOSED MUST for minimum entry; onboarding/settings PROPOSED SHOULD; rich hub/matchmaking PROPOSED CUT.
  - Ключевая неопределённость: [UNKNOWN] hub is not assumed, save is not a gap until Contract/Tree proves it; this outcome does not close full Program/Canon nodes.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/launch-control/demo-control-room.md:47-64`; `live/indie-game-development/knowledge/g9c41-gas-engine-SPEC.md:55`.

  ### P4 — bounded Program/Multiplayer runtime
  - Наблюдаемый результат: [INFERRED] session/peer identity, ordered input delivery, initial state, transport and failure signaling carry only the chosen demo simulation path.
  - Parent/link к демо: [INFERRED] direct consumers S9, P2, T8.
  - Зависимости: [STATED] C4, T1, T2, T3, T4, T5, T6.
  - Условие доказанности: [STATED] two-peer harness proves identity/order/state/digests and loud failure; local checksum smoke cannot substitute.
  - Owning track: [STATED] Program/Multiplayer; Grid/Gas/Actor/Level keep technical HOW.
  - Временной рубеж: [UNKNOWN] no accepted slice, transport plan or measured duration.
  - Proposal: [INFERRED] PROPOSED MUST for two-machine route.
  - Ключевая неопределённость: [UNKNOWN] whether reconnect/host loss triggers fresh map decision; does not create a new track or close full Program.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/grid-v1-critical-path-plan.md:101-122`; `live/indie-game-development/work/gas-v1-master-plan.md:329-372`.

  ### P5 — readable signature/comprehension surface
  - Наблюдаемый результат: [UNKNOWN] start, danger, joint action, causal consequence, authoritative result and one memorable signature moment are legible without architecture explanation.
  - Parent/link к демо: [INFERRED] direct consumers S8, P1.
  - Зависимости: [STATED] C2, C3, C4, T7, T8.
  - Условие доказанности: [STATED] observation/capture recognizes every state and signature moment; stale read-model negative control fails.
  - Owning track: [STATED] Canon + Presentation + Program; [UNKNOWN] sound production owner only if audio falsification says cue is necessary.
  - Временной рубеж: [UNKNOWN] signal vocabulary, environment and evidence duration.
  - Proposal: [INFERRED] PROPOSED MUST for comprehension; cheap causal audio PROPOSED SHOULD only on trigger; tutorial/polish breadth CUT.
  - Ключевая неопределённость: [UNKNOWN] exact hook/signals; does not close full Canon/Presentation nodes.
  - Evidence: [PROVED/STATED pointer] `live/indie-game-development/work/launch-control/demo-control-room.md:47-64,276-283`.

  ### P6 — permanent representative local loop
  - Наблюдаемый результат: [UNKNOWN] permanent scene repeats `start → pressure → joint action → consequence → result`; simulation creates decision and cooperation changes result.
  - Parent/link к демо: [INFERRED] direct consumers S8, S9, P1, P2.
  - Зависимости: [STATED] C2, C3, C4, T8.
  - Условие доказанности: [STATED] repeated local run without dev help, with positive/negative causal controls.
  - Owning track: [STATED] Program integrates; Canon meaning; target tracks drops.
  - Временной рубеж: [UNKNOWN] old 14 Sep useful-by is not forecast; Hook/slice/throughput missing.
  - Proposal: [INFERRED] PROPOSED MUST.
  - Ключевая неопределённость: [UNKNOWN] exact action/consequence; does not close Program M9 or target roots without original done_when/binding receipts.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/launch-control/demo-control-room.md:41-56,209-220`; `live/indie-game-development/work/minimum-game-frame-v2.md:101-108`.

  ### P7 — clear Contract-defined completion
  - Наблюдаемый результат: [UNKNOWN] attempt reaches one Contract-defined end, both peers agree it is over and player understands what happened.
  - Parent/link к демо: [INFERRED] direct consumers S8, S9, S10, P1, P2.
  - Зависимости: [STATED] C2, C3, C4, T8.
  - Условие доказанности: [STATED] local exact end semantics + P2 network agreement; no dev assistance/dead end.
  - Owning track: [STATED] Launch Control/Canon define promise; Program implements run authority.
  - Временной рубеж: [UNKNOWN] endpoint and implementation duration.
  - Proposal: [INFERRED] PROPOSED MUST; economy/reward/progression PROPOSED CUT.
  - Ключевая неопределённость: [UNKNOWN] extraction/safe-return/retreat are candidates, not accepted demo result; does not close full Frame/Program.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/launch-control/demo-control-room.md:47-54`; `live/indie-game-development/work/minimum-game-frame-v2.md:177-209`.

  ### P8 — clean restart/retry/relaunch semantics
  - Наблюдаемый результат: [UNKNOWN] after end, group starts a second clean attempt; later process/Steam relaunch reproduces supported path without stale authoritative state.
  - Parent/link к демо: [INFERRED] direct consumers S9, S10, P1.
  - Зависимости: [STATED] C2, C3, C4, P3, T8.
  - Условие доказанности: [STATED] two consecutive attempts + process relaunch on exact candidate; claimed variation observed separately.
  - Owning track: [STATED] Program + Level + Canon; save ownership only if Contract requires persistence.
  - Временной рубеж: [UNKNOWN] reset/persistence/variation semantics and duration.
  - Proposal: [INFERRED] PROPOSED MUST for reset/relaunch; moderate variation SHOULD; metaprogression/save migration CUT unless causally selected.
  - Ключевая неопределённость: [UNKNOWN] persistence is not silently required; does not close full save/load/Level/Program gates.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/launch-control/demo-control-room.md:47-64`; `live/indie-game-development/work/minimum-game-frame-v2.md:197-209,240-268`.

  ### C0 — Canon lineage readiness
  - Наблюдаемый результат: [CONFLICT current realization] stable authoritative pointer resolves terminal accepted workflow versus owner-reported newer unfinished Canon work; remaining lineage is binding-closed/cut.
  - Parent/link к демо: [INFERRED] direct consumer C1.
  - Зависимости: [UNKNOWN] missing stable pointer and evidence bundle.
  - Условие доказанности: [STATED] stable pointer + fresh binding Direction receipt/readback; no design implied.
  - Owning track: [STATED] Canon.
  - Временной рубеж: [UNKNOWN] pointer/recovery/review duration.
  - Proposal: [INFERRED] PROPOSED MUST route gate.
  - Ключевая неопределённость: [CONFLICT] accepted workflow exists, newer reported work lacks authority.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/history/2026-07-22-s-work-canon-current-process-plan-readiness-blocked-001.md:5-30`; `live/indie-game-development/NOW.md:60-73`.

  ### C1 — comparable Hook cards and actual owner verdict
  - Наблюдаемый результат: [UNKNOWN] 2–3 complete cards include gas-sphere reactions and materially different comparator; owner actually says choose/revise/reject.
  - Parent/link к демо: [INFERRED] direct consumer C2.
  - Зависимости: [STATED] C0 + owner attention.
  - Условие доказанности: [STATED] cards with promise/journey/signature/falsification + exact owner words.
  - Owning track: [STATED] Canon + owner.
  - Временной рубеж: [UNKNOWN] no cards/choice/duration.
  - Proposal: [INFERRED] PROPOSED MUST; gas-sphere stays parked candidate.
  - Ключевая неопределённость: [UNKNOWN] winning/revised/rejected Hook.
  - Evidence: [PROVED/STATED pointer] `live/indie-game-development/work/launch-control/demo-control-room.md:112-150,209-215`.

  ### C2 — owner-approved Demo Contract v1
  - Наблюдаемый результат: [UNKNOWN] versioned Contract names promise, player journey, signature moment, MUST/SHOULD/CUT, representative test and unknowns after C1 verdict.
  - Parent/link к демо: [INFERRED] direct consumers S8, P3, P5, P6, P7, P8, C3.
  - Зависимости: [STATED] C1.
  - Условие доказанности: [STATED] explicit owner acceptance/revision words on exact version.
  - Owning track: [STATED] Launch Control + owner; Canon supplies experience input.
  - Временной рубеж: [UNKNOWN] owner choice and revision duration.
  - Proposal: [INFERRED] PROPOSED MUST; candidate does not create or accept it.
  - Ключевая неопределённость: [CONFLICT] older baseline used “Demo Contract” terminology, later accepted strategy reclassified it as Skeleton.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/launch-control/demo-control-room.md:76-108,139-150`; `live/indie-game-development/history/2026-07-22-s-work-launch-control-demo-control-room-operating-strategy-accepted-001.md:12-27`.

  ### C3 — accepted Demo Experience Tree
  - Наблюдаемый результат: [UNKNOWN] accepted trace maps `Contract → spine → beat → observable outcome → capability → decision gap` without skipping parents.
  - Parent/link к демо: [INFERRED] direct consumers P3, P5, P6, P7, P8, C4.
  - Зависимости: [STATED] C2.
  - Условие доказанности: [STATED] accepted tree version and evidence pointers for every edge.
  - Owning track: [STATED] Canon.
  - Временной рубеж: [UNKNOWN] tree/review duration.
  - Proposal: [INFERRED] PROPOSED MUST.
  - Ключевая неопределённость: [UNKNOWN] exact beats/capabilities; no automatic BUILD.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/demo-workflow/demo-driven-design-canon-workflow-v1.md:134-181`; `live/indie-game-development/work/launch-control/demo-control-room.md:209-216`.

  ### C4 — target-track dispositions
  - Наблюдаемый результат: [UNKNOWN] every needed target returns ACCEPT/COUNTER/BLOCKED with exact proof receiver and integration event; no response silently weakens track HOW.
  - Parent/link к демо: [INFERRED] direct consumers P3, P4, P5, P6, P7, P8, T2, T3, T4, T5, T6, T7, T8.
  - Зависимости: [STATED] C3.
  - Условие доказанности: [STATED] committed receipts per target and conflict-preserving crosswalk to original done_when.
  - Owning track: [STATED] owning target tracks; Canon/Launch Control coordinate request only.
  - Временной рубеж: [UNKNOWN] response/rework durations.
  - Proposal: [INFERRED] PROPOSED MUST; does not launch BUILD.
  - Ключевая неопределённость: [CONFLICT] narrow demo needs may COUNTER against full Grid/Gas/Level/Presentation prerequisites.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/TREE.md:21-66`; `live/indie-game-development/work/launch-control/demo-control-room.md:93-108,209-216`.

  ### T0 — current Program truth reconciliation
  - Наблюдаемый результат: [CONFLICT current realization] fresh receipt reconciles stale Program Direction snapshot with later product purge/release evidence and names exact canonical refs plus remaining Direction action.
  - Parent/link к демо: [INFERRED] direct consumer T1.
  - Зависимости: [STATED] current operating route first requires fresh Character binding Direction close; that close does not itself free Program.
  - Условие доказанности: [STATED] fresh Program/product/Direction readback and binding reconciliation receipt; no assumed rebuild/release.
  - Owning track: [STATED] Program + Launch Control routing; Character supplies prerequisite receipt.
  - Временной рубеж: [UNKNOWN] Character review and Program reconcile durations.
  - Proposal: [INFERRED] PROPOSED MUST before using Program milestone truth.
  - Ключевая неопределённость: [CONFLICT] current NOW narrative versus later product evidence; product merge/Deliver never substitutes Direction close.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/NOW.md:23-48`; `live/indie-game-development/work/launch-control/demo-control-room.md:406-427,550-561`.

  ### T1 — clean permanent Integration base
  - Наблюдаемый результат: [UNKNOWN] one clean canonical permanent scene/base exists and can accept bounded drops without Integration implementing target work.
  - Parent/link к демо: [INFERRED] direct consumers P3, P4, T2, T3, T4, T5, T6, T7, T8.
  - Зависимости: [STATED] T0.
  - Условие доказанности: [STATED] permanent scene path, clean smoke, seam ownership and binding Program receipt.
  - Owning track: [STATED] Program/Integration.
  - Временной рубеж: [UNKNOWN] reconciliation/base build/review duration.
  - Proposal: [INFERRED] PROPOSED MUST.
  - Ключевая неопределённость: [UNKNOWN] current product base; this outcome does not close later Program M3–M9.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/program-v2-integration-lab-plan.md:18-39,54-117,136-156`.

  ### T2 — bounded Grid drop
  - Наблюдаемый результат: [UNKNOWN] Contract-needed scene gets authoritative cell/commit/topology/contact proof and peer-consumable revisions.
  - Parent/link к демо: [INFERRED] direct consumers P4, T3, T4, T5, T7, T8.
  - Зависимости: [STATED] C4, T1.
  - Условие доказанности: [STATED] exact Contract→Grid crosswalk, track handoff, stale/mid-tick negatives, Integration smoke and binding Direction receipt.
  - Owning track: [STATED] Grid; Program only accepts integration.
  - Временной рубеж: [UNKNOWN] G01 is 1/11 and G02 verdict absent; half-day legs are appetite, not calendar; missing exact subset/consumers.
  - Proposal: [INFERRED] PROPOSED MUST only for accepted bounded need; unrelated breadth CUT.
  - Ключевая неопределённость: [CONFLICT] narrow demo slice versus full M3/M5/second-consumer/Wind; this outcome does not close full Grid TREE node.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/NOW.md:109-119`; `live/indie-game-development/work/grid-v1-critical-path-plan.md:67-99,101-134`.

  ### T3 — bounded live Gas drop
  - Наблюдаемый результат: [UNKNOWN] production tick owns deterministic live composition/source/publication through accepted Grid seam, independent of later world-change proof.
  - Parent/link к демо: [INFERRED] direct consumers P4, T4, T7, T8.
  - Зависимости: [STATED] C4, T1, T2.
  - Условие доказанности: [STATED] repeated ordered/fail-atomic tick, immutable completed view, digest/events, positive/negative/stale controls and binding receipt.
  - Owning track: [STATED] Gas; Grid owns seam; Program integrates.
  - Временной рубеж: [UNKNOWN] node-1 detailed PLAN/BUILD and later node durations absent.
  - Proposal: [INFERRED] PROPOSED MUST only if Contract selects Gas consequence.
  - Ключевая неопределённость: [UNKNOWN] exact demo subset; does not close full Gas V1.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/NOW.md:121-130`; `live/indie-game-development/work/gas-v1-master-plan.md:97-167,416-428`.

  ### T4 — controlled world-change consequence
  - Наблюдаемый результат: [UNKNOWN] one committed topology/structure change alters Gas and one named additional consumer so the player can observe a causal consequence.
  - Parent/link к демо: [INFERRED] direct consumers P4, T7, T8.
  - Зависимости: [STATED] C4, T1, T2, T3, T6 + [UNKNOWN] second consumer selected by target dispositions.
  - Условие доказанности: [STATED] revision/topology evidence, Gas reaction, second-layer reaction, player-visible positive/negative control and binding receipts.
  - Owning track: [STATED] Grid + Gas + Level/Structure + selected consumer; Program integrates.
  - Временной рубеж: [UNKNOWN] second consumer, Level close, topology route and durations.
  - Proposal: [INFERRED] PROPOSED MUST only if chosen Contract requires world change.
  - Ключевая неопределённость: [CONFLICT] full M5/second-consumer gate versus narrower loop; does not close full involved tracks.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/program-v2-integration-lab-plan.md:98-103,184-193`; `live/indie-game-development/work/gas-v1-master-plan.md:263-291`.

  ### T5 — bounded Actor/contact drop
  - Наблюдаемый результат: [UNKNOWN] authoritative player identity/movement/footprint/contact/action receives the selected consequence; View remains non-authoritative.
  - Parent/link к демо: [INFERRED] direct consumers P4, T7, T8.
  - Зависимости: [STATED] C4, T1, T2.
  - Условие доказанности: [STATED] fresh Actor contract/prefab, movement/contact/reaction proof, negative control, Integration smoke and binding receipt.
  - Owning track: [STATED] Character/Actor + Program integration.
  - Временной рубеж: [UNKNOWN] V2 binding close first, then fresh Actor lineage; durations absent.
  - Proposal: [INFERRED] PROPOSED MUST bounded Actor; cosmetic/networked ragdoll CUT.
  - Ключевая неопределённость: [UNKNOWN] exact authority and Grid footprint; does not close Character V2 or full Actor node.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/NOW.md:94-107`; `live/indie-game-development/work/program-v2-integration-lab-plan.md:213-228`; `live/indie-game-development/history/2026-07-23-s-work-characters-v2-published-close-readiness-accept-001.md:4-24,64-105`.

  ### T6 — one representative Level space/drop
  - Наблюдаемый результат: [UNKNOWN] one accepted navigable situation supplies structure/apertures/routes and repeatable reset for chosen loop.
  - Parent/link к демо: [INFERRED] direct consumers P4, T4, T7, T8.
  - Зависимости: [STATED] C4, T1.
  - Условие доказанности: [STATED] start-to-result structural run; procedural option also needs reproducible seed/drop; binding Level disposition/receipt.
  - Owning track: [STATED] Level; Program accepts integration.
  - Временной рубеж: [UNKNOWN] binding Direction review, source choice and duration.
  - Proposal: [INFERRED] PROPOSED MUST one space; multiple maps/wide generation CUT.
  - Ключевая неопределённость: [CONFLICT] authored vs procedural vs thin hybrid; bounded acceptance does not close full Level TREE node without original done_when.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/TREE.md:35-38`; `live/indie-game-development/CHARTER.md:131-137`; `live/indie-game-development/NOW.md:50-58`; `live/indie-game-development/work/program-v2-integration-lab-plan.md:195-211`.

  ### T7 — readability/performance/capture drop
  - Наблюдаемый результат: [UNKNOWN] accepted read models are legible on named provisional hardware/OS/network environments within budget and yield reproducible capture.
  - Parent/link к демо: [INFERRED] direct consumers S8, S9, S10, P1, P2, P5, T8.
  - Зависимости: [STATED] C4, T1, T2, T3, T4, T5, T6.
  - Условие доказанности: [STATED] profile/budget, clarity observation, capture, stale-read-model negative; audio only if P5 falsification requires smallest cue.
  - Owning track: [STATED] Presentation; Program/Gas supply profiling; owner supplies hardware; [UNKNOWN] named hardware and conditional sound production owner.
  - Временной рубеж: [UNKNOWN] environment/budget/capture/audio need and duration.
  - Proposal: [INFERRED] PROPOSED MUST readability/performance/capture; conditional audio SHOULD; broad polish CUT.
  - Ключевая неопределённость: [UNKNOWN] min-spec remains deferred; does not close full Presentation node.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/NOW.md:74-82`; `live/indie-game-development/work/program-v2-integration-lab-plan.md:230-244`; `live/indie-game-development/work/launch-control/demo-control-room.md:276-283`.

  ### T8 — integrated representative candidate
  - Наблюдаемый результат: [UNKNOWN] permanent Program scene accepts P3/P4 and T2–T7 drops, preserves each track's authority, and produces exact candidate for local/player/network/distribution proofs.
  - Parent/link к демо: [INFERRED] direct consumers S9, P2, P5, P6, P7, P8.
  - Зависимости: [STATED] C4, T1, T2, T3, T4, T5, T6, T7, P3, P4.
  - Условие доказанности: [STATED] track handoffs + seam/smoke/negative checks + reproducible scene candidate + binding Program receipt.
  - Owning track: [STATED] Program/Integration; it does not implement missing target work.
  - Временной рубеж: [UNKNOWN] all target dispositions, shared-surface collision map and measured durations.
  - Proposal: [INFERRED] PROPOSED MUST.
  - Ключевая неопределённость: [UNKNOWN] exact Contract-derived subset; accepted candidate does not itself close Program/target roots.
  - Evidence: [PROVED/STATED pointers] `live/indie-game-development/work/program-v2-integration-lab-plan.md:18-39,95-117,296-330`.

  ## Causal reading and route assessment

  [STATED] Hard convergence is three branches: design `C0→C1→C2→C3→C4`, product/player proof `T0..T8 + P3/P4→P6/P7/P8→P2→P1`, and Steam `S1→S2→S3→S4→S5→S6` plus `S7→S8/S9→S10→S11→S12→S13→S14→S0`. Steam inventory/private drafting may advance factually, but public claims and submissions must consume representative evidence.

  [STATED] Current operational capacity is not broad parallelism: one owner-primary verdict/review gate, one serialized product Control/review/Deliver path and one background BUILD; shared seams/files/scenes/contracts/Unity/integration/machines serialize. This model is causal, not a daily schedule, and launches nothing. Evidence: `live/indie-game-development/work/launch-control/demo-control-room.md:400-427,550-563`; `live/indie-game-development/work/program-v2-integration-lab-plan.md:315-330`.

  [INFERRED] Preliminary October-route enum: `UNFORECASTABLE`. [CONFLICT] accepted control artifact also says `AT RISK + UNFORECASTABLE`, but the required one-of-four vocabulary cannot hold a dual enum. [INFERRED] It is not `MISSED` as of 2026-07-23 because 31 Aug and 5 Oct gates are future. `latest_safe_switch = UNKNOWN`: Contract/Tree, internal durations, owner/review/integration/machine queues, cut execution and margins are absent. Before registration, the earliest unresolved hard gate is S6 (31 Aug); after a registration receipt, S11/S12 (5 Oct). Evidence: `live/indie-game-development/work/launch-control/demo-control-room.md:224-250`; `live/indie-game-development/history/2026-07-22-s-work-launch-control-m1-superseded-by-demo-control-room-001.md:57-66`.

  [STATED] Demo-only PROPOSED CUT/PARK: eight-player proof, dedicated server, late join, full failure matrix, several maps/wide generation, economy/progression, full Gas/tool/reaction roster, full destruction/broad polish, optional Press Preview. These cuts do not alter the full-game TREE/CHARTER. Evidence: `live/indie-game-development/work/launch-control/demo-control-room.md:58-74,248-250`.

  [STATED] Preserved sibling obligation: external paid validation by 11 Dec 2026 is not demo completion and Next Fest does not prove it. [STATED] a base-game/Early Access release used for that gate before 1 Mar 2027 would make February Next Fest ineligible. February is only an eligibility-dependent candidate fallback, never an automatic successor. Evidence: `live/indie-game-development/CHARTER.md:11-20`; official February page: https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/feb_2027

  [UNKNOWN] Deferred owner/track decisions, not opened in state: Hook choose/revise/reject; Contract promise and exact MUST/SHOULD/CUT; narrow demo slices versus full target gates; Level authored/procedural/hybrid; lifecycle/persistence; title/App activation/operator; unfamiliar-player logistics; performance environments/conditional sound owner; October registration/participation versus eligibility-dependent February/other public route. No decision is made here.

  ## Non-binding pre-pass result

  [STATED] Six independent read-only generators covered technical spine, evidence truth, player journey, release journey, critical path and failure inversion; a separate miner deduped the DAG and a constraint-inversion strategic-search child preserved five unresolved structural branches.

  [STATED] Four first-round and two second-round independent same-session validators tried to refute causality, authority/evidence, Steam/schedule and scope/ownership. Their material refutations were incorporated: exact mirrored graph semantics; signature outcome; separate Multiplayer/runtime; Contract/Tree/dispositions split; Program reconciliation/base/integration split; Gas versus world-change split; admin/activation/base page/demo AppID/submission/approval/release separation; exact-build rerun; monitoring/rollback; precise functional owners and remaining UNKNOWN operators; no implicit hub/save; demo slices do not close full track gates.

  [STATED] This is only an in-session pre-pass. Binding G5 was NOT performed and cannot be claimed in this physical chat; it requires a separate fresh session. Model adoption and Stage 3/4 remain open.
evidence: |
  [PROVED/STATED] Authority base: clean tracked worktree at `origin/main@4a33f386`; required commit `4a33f386` is an ancestor/equal.
  [PROVED/STATED] Primary local authority: `live/indie-game-development/CHARTER.md`; `TREE.md`; `NOW.md`; `work/launch-control/demo-control-room.md`; `work/launch-control/stabilization-baseline.md`; `work/program-v2-integration-lab-plan.md`; `work/grid-v1-critical-path-plan.md`; `work/gas-v1-master-plan.md`; `work/minimum-game-frame-v2.md`; `work/demo-workflow/demo-driven-design-canon-workflow-v1.md`; current Character/Level/Grid/Gas/Canon/Marketing receipts and CALLs cited per outcome.
  [PROVED/STATED] Official platform sources checked 2026-07-23: https://partner.steamgames.com/doc/store/application/demos ; https://partner.steamgames.com/doc/store/releasing ; https://partner.steamgames.com/doc/store/review_process ; https://partner.steamgames.com/doc/store/coming_soon ; https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest ; October and February pages cited above.
  [STATED] Evidence confidence: accepted quality floor, target authorities, closure rule and external dates are established; DAG links and MUST/SHOULD/CUT are explicit research inferences; missing Contract/Tree, current Steam readback, durations, operators, machine/logistics and target dispositions remain UNKNOWN; source disagreements remain CONFLICT.
state_changes: |
  1. Add this full RESULT at `live/indie-game-development/history/2026-07-23-s-research-launch-control-demo-program-v0-001.md` with its exact END_OF_FILE trailer.
  2. Append the exact `log` line below to `live/indie-game-development/LOG.md` before its existing END_OF_FILE trailer.
  3. Preserve every other file and semantic field unchanged. In particular: no changes to `os/**`, product repos, `CHARTER.md`, `TREE.md`, `NOW.md`/open_calls/roots/status, target tracks, `work/launch-control/demo-control-room.md`, launch-control migration, or any active Program Model; create no track and launch no implementation.
captures: []
decisions_needed: []
play_check:
  - 1 Recite: done — bounded Stage 2 question, one research RESULT/history candidate, mandatory parallel generation/convergence/refutation and no adoption/implementation were restated.
  - 2 Investigate: done — fresh Git/state, all relevant direction/track evidence, product receipts and official Steam/release route were read; six generators, miner and strategic-search were merged/deduped.
  - 3 Confidence: done — every significant claim uses PROVED/STATED, INFERRED, UNKNOWN or CONFLICT; two validator rounds refuted and corrected the draft; remaining change conditions are explicit.
  - 4 Close: done — DRAFT demo-program-v0 and sources returned as a knowledge candidate; binding G5 explicitly remains separate and no owner verdict was inferred.
log: 2026-07-23 · s-research-launch-control-demo-program-v0-001 · research · launch-control · g-b847/demo-program-v0-stage-2: evidence-grounded DRAFT demo-program-v0 built backward across design, player, technical and Steam release journeys; October is UNFORECASTABLE, all gaps/conflicts stay explicit, same-session refutation pre-pass is non-binding, and the candidate remains history-only pending a separate fresh binding G5 review. → history/2026-07-23-s-research-launch-control-demo-program-v0-001.md
next: |
  return-to-owner

END_OF_FILE: live/indie-game-development/history/2026-07-23-s-research-launch-control-demo-program-v0-001.md
