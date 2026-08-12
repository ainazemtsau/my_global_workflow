RESULT s-solmax-zaratustra-map-evidence-025 (call: c-solmax-zaratustra-map-evidence-025)
direction: solmax   play: research   node: g-zara

outcome: |
  ## Вывод

  Утверждённый порядок `1 → 2 → 3 → 4 → 5 → 6` выдержал проверку.
  Health остаётся лучшим известным первым probe именно для этого владельца,
  потому что здесь уже есть реальный сценарий и след неудачного live-use, — но
  только как явно неклинический, низкопоследственный процесс. Внешние данные не
  дают оснований заменить Area/Capability/Operation/Workflow/Run, локальный web
  UI, typed verdicts или subscriptions-as-first-class другой архитектурой.

  При этом свежая проверка нашла четыре материально недостающие outcome-границы:
  intended-use и stop boundary первого Health-процесса; trust/taint boundary для
  контекста; срок годности qualification при изменении access/provider policy;
  post-activation observation и испытанный rollback улучшения. Это не
  implementation preferences. Поэтому returning map leg должен сохранить
  порядок и остальные принятые решения, но перед записью спорных четырёх
  карточек показать владельцу один узкий пакет поправок.

  ## Компетентный baseline 2026

  **STATED из первичных источников.** Современные agent systems отделяют
  предсказуемые workflows от открытых agents и рекомендуют начинать с простых
  composable patterns; structured output гарантирует форму, но не истинность;
  durable execution восстанавливается из сохранённого state/event history, а
  внешние эффекты при replay/retry всё равно требуют idempotency; trace нужен
  для диагностики, но outcome-eval и повторные trials нужны для доказательства.
  Anthropic отдельно показывает, что при 75% успеха одного trial вероятность
  трёх успехов подряд всего около 42%, а дефект grader/scaffold однажды сдвинул
  измеренный результат с 42% до 95% — evaluator тоже надо проверять.

  Источники: [Anthropic, Building effective agents, 2024-12-19](https://www.anthropic.com/engineering/building-effective-agents),
  [Anthropic, Demystifying evals, 2026-01-09](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents),
  [Temporal Workflow Execution, current docs, получено 2026-08-12](https://docs.temporal.io/workflow-execution),
  [LangGraph interrupts, current docs, получено 2026-08-12](https://docs.langchain.com/oss/python/langgraph/interrupts),
  [MCP tools specification, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/tools).

  **INFERRED baseline для данного charter — не выбор framework/database:**

  1. Один полезный low-consequence vertical в одном небольшом deployable
     приложении: app-owned versioned contracts только для реально исполняемых
     Area/Capability/Operation/Workflow/Step/Run, один registered handler и
     deterministic transitions; модель возвращает bounded typed verdict.
  2. Три разделённых state plane: authoritative typed facts с provenance;
     run events/checkpoints; opaque prose/artifacts/transcripts, из которых
     deterministic code не извлекает семантику.
  3. Узкий executor/access port. Local, paid subscription и cloud API — разные
     first-class access paths; каждый run фиксирует exact model snapshot,
     provider, auth/access subtype, adapter/tool/instruction/schema versions,
     quota/cost/availability и дату policy evidence.
  4. Явная effect boundary: read-only default, typed effect intent, approval для
     внешних/необратимых/spend-bearing действий, idempotency key, audit и
     approve/reject/resume.
  5. Тонкий localhost UI над typed projections: start, pending, approval,
     result, trace. Это task surface, а не ранняя generic chat/dashboard platform.
  6. App-owned trace плюс маленький workflow-specific eval set: deterministic
     contract/effect/state checks, реальные failure cases, human-calibrated
     semantic grader и несколько trials. Второй access path квалифицируется уже
     на этой задаче. Embedded graph, полноценный durable engine, generalized
     router или observability stack добавляются только когда crash/restart,
     multi-day wait, concurrency либо реальные failures это потребовали.

  Обычные издержки baseline: schema migrations и преждевременно неверные
  abstractions; повтор effects при replay; provider/schema/tool и quota drift;
  чувствительные данные в state/traces; ложная уверенность grader; UI/eval
  infrastructure, ставшая продуктом вместо workflow; а у полного durable или
  observability stack — отдельные workers/services, version skew, backups и
  operator burden. Provider compatibility также не тождественна: официальные
  Agents SDK docs прямо предупреждают, что adapters поддерживают неодинаковые
  feature semantics ([OpenAI Agents SDK models, получено 2026-08-12](https://openai.github.io/openai-agents-python/models/)).

  ## Проверенные аналоги — evidence отдельно от inference

  1. **Home Assistant — полезный local vertical до платформы.** **STATED:** проект
     начался с одной личной задачи управления Philips Hue, затем вырос до
     integrations, config-entry lifecycle и quality scale; актуальные правила
     2026 для первого contribution требуют минимальный single-platform slice, а
     не максимальный уровень сразу. Источники:
     [10 years of Home Assistant, 2023-09-17](https://www.home-assistant.io/blog/2023/09/17/10-years-home-assistant/),
     [integration architecture, updated 2026-06-15](https://developers.home-assistant.io/docs/architecture_components/),
     [integration quality scale, updated 2026-06-17](https://developers.home-assistant.io/docs/core/integration-quality-scale/),
     [contributing an integration, updated 2026-07-12](https://developers.home-assistant.io/docs/core/integration/contributing_to_core/).
     **INFERRED:** долговечность пришла через concrete utility → narrow lifecycle
     contract → tests/migrations/quality, не через полный meta-model заранее.
     **Confidence: high. Limit:** home automation не доказывает AI semantics.

  2. **VS Code — contract после dogfood, stable и proposed lanes раздельно.**
     **STATED:** к 1.0 команда шесть месяцев использовала продукт ежедневно и
     проверила extension API более чем на 1000 extensions; extensions работают в
     отдельном host, лениво активируются и не получают DOM, а proposed APIs не
     допускаются в stable Marketplace. Источники:
     [VS Code 1.0, 2016-04-14](https://code.visualstudio.com/blogs/2016/04/14/vscode-1.0),
     [Extension Host, current docs, получено 2026-08-12](https://code.visualstudio.com/api/advanced-topics/extension-host),
     [Using Proposed API, current docs, получено 2026-08-12](https://code.visualstudio.com/api/advanced-topics/using-proposed-api).
     **INFERRED:** node 4 прав в stable registration boundary, но стабилизировать
     её надо после разнообразного use, с отдельным experimental lane.
     **Confidence: high. Limit:** это не durable workflow engine.

  3. **Obsidian — continuity через owner-owned files, но extensions не равны
     trust.** **STATED:** authoritative notes — обычные local Markdown files, а
     индекс перестраивается; одновременно Obsidian признаёт, что community
     plugins наследуют права приложения, и только в 2026 ввёл автоматический
     scan новых releases. Источники:
     [How Obsidian stores data, current docs, получено 2026-08-12](https://obsidian.md/help/data-storage),
     [Plugin security, current docs, получено 2026-08-12](https://obsidian.md/help/plugin-security),
     [The future of Obsidian plugins, 2026-05-12](https://obsidian.md/blog/future-of-plugins/).
     **INFERRED:** переносимый app-independent state усиливает continuity, но
     extensibility без least privilege оставляет trust debt.
     **Confidence: high. Limit:** notes не являются executable runs.

  4. **Anthropic Research/Claude Code — explicit artifacts, tracing и selective
     parallelism.** **STATED:** production research сохраняет plan до context
     truncation, использует tracing и version coexistence; internal eval сообщил
     +90.2% против single-agent breadth task, но agents тратили примерно 4×, а
     multi-agent system примерно 15× chat tokens. Long-running coding harness
     использует progress artifact, feature inventory, Git и clean handoffs,
     потому что compaction alone оставлял незадокументированную half-finished
     работу. Источники:
     [Multi-agent research system, 2025-06-13](https://www.anthropic.com/engineering/multi-agent-research-system),
     [Effective harnesses for long-running agents, 2025-11-26](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
     **INFERRED:** continuity принадлежит inspectable artifacts/checkpoints, а
     parallel routing оправдан лишь decomposable value. **Confidence:
     medium-high:** числа vendor-internal, без equal-token independent trial.

  Общий surviving pattern четырёх аналогов:
  `конкретная польза → узкая граница → реальное разнообразие/отказы →
  compatibility/evals → recovery/governance`. Масштаб install/plugin counts не
  использовался как доказательство успеха.

  ## Сильнейший аргумент против baseline sequence

  Внешний и локальный evidence не опровергает порядок шести nodes; он опровергает
  возможный порядок доказательств **внутри node 1**. Текущий draft позволяет
  долго закрывать ontology/contracts/UI/eval-harness criteria до первого
  наблюдаемого полезного поведения. Локальный прежний trial уже дал именно
  `state/intake/handback bureaucracy` без полезного owner-leading flow.
  Anthropic рекомендует simplest composable pattern, OpenAI — start small и
  validate real use, а текущая экономическая рекомендация OpenAI от 2026-07-14
  требует считать cost per accepted outcome, attempts, latency и human review,
  прежде чем масштабировать governance/infra
  ([OpenAI, Managing AI investments, 2026-07-14](https://openai.com/index/managing-ai-investments-in-agentic-era/)).

  Поэтому первый внешний proof event node 1 должен быть один полезный,
  low-consequence end-to-end Health run через самый тонкий безопасный путь;
  generalized contracts/projections/evals расширяются из его traces и failures.
  До него остаётся только minimum safety envelope: typed identity/input/output,
  authority/effect, continuation/result/trace, intended-use/privacy boundary и
  stop behavior. Это не отменяет уже принятые typed contracts, UI и evals — это
  делает их рост зависимым от полезности. **Confidence: high.** Ответ изменит
  shape, в котором первый executable checkpoint уже измеряет реальную полезность
  до расширения общих компонентов.

  ## Шесть точных nodes

  | node | verdict | evidence-backed boundary перед записью карты | confidence / что изменит ответ |
  |---|---|---|---|
  | `g-zara-health-vertical` | **change** | `low-consequence` не операционализирован. Добавить intended use: только general-wellness, administrative/organizational или self-observation; запретить diagnosis, treatment, medication change и time-critical recommendation; определить out-of-scope stop/handoff и данные, видимые каждому executor. Первый proof event — полезный run, не объём платформы. [FDA General Wellness guidance, January 2026](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-wellness-policy-low-risk-devices); [WHO LMM health guidance, 2024-01-18](https://www.who.int/news/item/18-01-2024-who-releases-ai-ethics-and-governance-guidance-for-large-multi-modal-models). | **High** на safety gap, **medium** на лучший probe. Exact workflow с уже явными exclusions снимет safety change; три бесполезных/обременительных run или необходимость clinical advice отменят Health-first. |
  | `g-zara-trusted-context-state` | **change** | Provenance не делает source instructions доверенными. Добавить trust/taint class, separation instructions vs untrusted data, least-privilege effect/tool scope и adversarial cases для indirect prompt injection, cross-source instruction conflict и privilege escalation. [OWASP LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/). | **High.** Явная существующая trust boundary и эти тесты в точном acceptance снимут change. |
  | `g-zara-model-qualification-routing` | **change** | Qualification сейчас инвалидируется изменением workflow/instruction/adapter/tool/model, но не terms, training/data-use, retention, auth/workspace, automation scope, quota, price, availability или tool policy. Добавить evidence date/effective version, expiry и эти triggers; no silent fallback сохранить. Current OpenAI и Anthropic docs подтверждают разные meters/surfaces для subscription и API, а [Anthropic notice, 2026-06-16](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) прямо приостановил ранее объявленный отдельный subscription Agent-SDK credit. | **High.** Contract с policy-expiry снимет change. Два task-eval access paths без material decision difference отодвинут optimization, но не registry truth. |
  | `g-zara-extensible-areas-workflows` | **investigate** | Goal уже требует no change в central routing, authority, trace и navigation semantics, но done_when прямо проверяет только central-router semantics. Перед closure нужен recorded semantic/file diff по всем четырём surfaces, плюс явный privilege/isolation boundary handler. Это делает уже принятое outcome falsifiable, не требует нового topology/tooling. | **Medium-high.** Если card acceptance прямо наследует весь goal и проверка фиксирует zero central semantic diff, verdict становится **keep**; реальная вторая Area, требующая kernel semantics edit, станет material **change**. |
  | `g-zara-daily-owner-use` | **keep** | Три Areas, recurring reliance, explicit better-than-plain-chat owner judgment, разделение usefulness/burden/abandonment и cross-surface no-duplicate-effect закрывают риск «популярность/UI polish = success». Field testing соответствует [NIST GenAI Profile, 2024-07-26](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence). | **High.** Ответ изменит только отказ cross-surface identity/idempotency на реальных effects либо изменение owner charter success criterion. |
  | `g-zara-governed-improvement` | **change** | Pre-activation benchmark и наличие rollback не ловят latent regression после activation. Для activated candidate добавить bounded canary/observation, incident/regression monitoring, заранее разрешённый fail-safe suspension и испытанный rollback; owner-only activation/authority expansion и owner re-enable сохраняются. [NIST GenAI Profile, 2024-07-26](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence); [Google SRE Canarying Releases, получено 2026-08-12](https://sre.google/workbook/canarying-releases/). | **High.** Явный post-activation observation и exercised rollback снимут change; rejection-only cycle не докажет activated improvement. |

  ## Health-first, пределы и условия пересмотра

  Health остаётся лучшим **owner-specific** первым probe после node-1 correction:
  он соединяет известную владельцу задачу, богатый failure evidence и проверку
  sensitive-context/effect boundaries. Это не общий вывод о том, что Health
  обычно лучший AI vertical, и не health advice. Если безопасный неклинический
  workflow нельзя сформулировать, он не даёт полезность за три low-consequence
  runs, требует regulated/clinical inference либо нарушает Solmax no-preemption,
  первым должен стать другой low-risk Area.

  Ограничения: exact first workflow, hardware, concurrency, run duration,
  remote/multi-user access и фактическая data sensitivity не заданы; vendor
  case studies не являются независимыми reliability studies; subscription
  automation rights и quotas меняются. В частности, свежий notice Anthropic
  противоречит нынешней фразе CHARTER про отдельный приблизительно $20 Agent-SDK
  credit — это отдельный authority-compliant repair, не изменение карты в этой
  research-ноге. Crash/restart и duplicate-effect injection, три реальные runs,
  two-adapter parity/eval и human calibration grader — ближайшие данные, которые
  могут сдвинуть baseline.

  Parallel source branches были сведены nominal-group методом. Six-node
  refutation была только same-session intra-family pre-pass и не является
  binding G5 или доказательством closure любого будущего node; обязательная
  fresh separate-session refutation остаётся там, где её требует done_when.

evidence: |
  Полностью прочитаны указанные CALL источники: CHARTER, g-solmax, g-zara,
  owner-approved draft, обе knowledge notes и checkpoint owner approval; также
  проверены NOW, сам child и returning parent. `archive/**` не использовался.

  Первичные source families, получены 2026-08-12: Anthropic engineering/docs;
  OpenAI official guides/docs; MCP specification; Temporal/LangGraph durable
  execution docs; FDA/WHO/NIST/OWASP safety guidance; Home Assistant, VS Code и
  Obsidian first-party histories/developer docs. Прямые ссылки и даты стоят у
  каждого finding выше. Established facts маркированы `STATED`; перенос на
  Zaratustra — `INFERRED`; vendor-internal цифры названы как таковые.

  Проверенная access-path улика: [OpenAI Codex authentication, получено 2026-08-12](https://learn.chatgpt.com/docs/auth)
  разделяет ChatGPT sign-in и usage-based API key; [Claude Code authentication,
  получено 2026-08-12](https://code.claude.com/docs/en/authentication) разделяет
  subscription, Console/API, organization и cloud-provider credentials;
  [llama.cpp server docs, current master, получено 2026-08-12](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
  показывают local HTTP path с частичной OpenAI-compatible surface. Это
  подтверждает first-class plurality, но не взаимозаменяемость путей.

state_changes: |
  - Close c-solmax-zaratustra-map-evidence-025 with this fresh map_evidence and
    no successful Direction-OS child CALL.
  - On direct parent c-solmax-zaratustra-map-finalize-026, record receipt
    history/2026-08-12-s-solmax-zaratustra-map-evidence-025.md, remove
    waiting_on=c-solmax-zaratustra-map-evidence-025 and set status=ready.
  - Save this full RESULT and append its journal line to the child and parent.
    Do not mutate any node, CHARTER, NOW, knowledge, approved draft, product
    repository or Zaratustra runtime implementation.

captures:
  - Returning map leg: preserve order and all settled decisions, but present one
    narrow owner verdict covering exact additions to nodes 1, 2, 3 and 6 before
    writing those disputed cards.
  - Node 4 shape/closure: record a semantic/file diff proving that the second
    Area changes none of central routing, authority, trace or navigation.
  - Separate authority-compliant repair: reconcile CHARTER's stale separate
    Anthropic Agent-SDK credit statement with the 2026-06-16 official pause.

decisions_needed:
  - c-solmax-zaratustra-map-finalize-026 must obtain one narrow owner verdict on
    the four material boundary additions; no other approved product decision or
    the six-node order needs reopening.

play_check:
  - '1 Recite: done — one bounded question, five required report parts, one focused research leg and return-to-parent were restated before research.'
  - '2 Investigate: done — independent baseline, far-analogy, access-path, reliability and counterargument branches used current official/primary sources and were merged/deduped; no archive, implementation or product mutation.'
  - '3 Confidence: done — every main finding separates STATED evidence from INFERRED transfer, gives confidence, limits and evidence that would change the answer.'
  - '4 Close: done — compact baseline, four verified analogies, strongest counterargument, exact six-row table and Health-first verdict returned as fresh map_evidence.'
  - 'Owner authority guard: research did not alter the approved draft or decide its corrections; material refutations return to the parent for one narrow owner verdict.'
  - 'G5 provenance: six-node refutation here is a same-session intra-family pre-pass only, not binding fresh review and not closure evidence.'

log: - 2026-08-12 — fresh 2026 map evidence kept the 1→6 order and conditional Health-first probe, found four material acceptance gaps, and readied the returning map leg for one narrow owner verdict.

next: |
  return-to-parent c-solmax-zaratustra-map-finalize-026

END_OF_FILE: live/solmax/history/2026-08-12-s-solmax-zaratustra-map-evidence-025.md
