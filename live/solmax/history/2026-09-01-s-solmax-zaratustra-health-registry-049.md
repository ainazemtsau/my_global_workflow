RESULT s-solmax-zaratustra-health-registry-049
direction: solmax
play: work
node: g-zara-health-vertical
bet: bet-g-zara-health-vertical
task: t-health-registry
call: c-solmax-zaratustra-health-registry-048

outcome: |
  delivered

  В runtime-слое создан явный реестр обработчиков:
  `Handler` — frozen typed record с объявленными `call_sites`;
  `StepCall` — frozen typed record, явно связывающий step с handler.
  `HANDLER_REGISTRY` и `STEP_CALLS` являются прямыми данными, а не
  результатом поиска, import/file conventions или dynamic discovery.

  `validate_handler_registry` роняет существующую единую проверку для обеих
  требуемых конфигураций:
  1. зарегистрированный handler без call sites;
  2. step call, ссылающийся на незарегистрированный handler.

  Четырнадцать contracts, lossless context_item и закрытая instruction
  surface не изменялись. Runner, сценарий, предметный модуль, UI, MCP и
  handler implementation не создавались.

  close: light — because все три строки done_when перевыведены первыми
  руками из committed bytes, точного manifest и фактических command outputs.
  Остатка owner/product/quality judgment нет; свежий G5 не требуется.

  review: n/a — light change under repository-default PROBA.

evidence: |
  COMMIT

  repository:
    C:\projects\zaratusta-product
  branch:
    feat/health-contracts
  commit:
    6e8b3fcea623d0e0247c1b2a748e34508985286e
  parent:
    c559d72b3fffd0180bd4e6b900e38ad1841f0754
  subject:
    Add explicit handler registry and call-site gate

  MANIFEST

    M  RESULT.md
    A  docs/adr/0004-explicit-handler-registry.md
    M  src/runtime/AGENTS.md
    M  src/runtime/__init__.py
    A  src/runtime/handler_registry.py
    A  tests/runtime/test_handler_registry.py
    M  tests/runtime/test_public_surface.py
    M  tools/selfcheck.py

  `git diff --exit-code HEAD^ HEAD -- src/vocabulary tests/vocabulary
  tools/check.py validation.config` завершился с кодом 0. Ни один accepted
  contract/automaton файл не изменён.

  COMMITTED DATA

    registry=(Handler(id='handler-alpha', call_sites=('step-alpha',)),)
    step_calls=(StepCall(step='step-alpha', handler='handler-alpha'),)
    registry_findings=()

  Две незаконные конфигурации:

    Handler(id="handler-alpha", call_sites=())

    HANDLER_REGISTRY = (
        Handler(id="handler-alpha", call_sites=("step-alpha",)),
    )
    STEP_CALLS = (
        StepCall(step="step-alpha", handler="handler-missing"),
    )

  ACCEPTED CONTRACT SNAPSHOT

    contract_identities=('area-v1', 'capability-v1', 'operation-v1',
    'workflow-v1', 'step-v1', 'run-v1', 'transition-v1', 'effect-v1',
    'artifact-v1', 'owner-projection-v1', 'trace-event-v1',
    'context-item-v1', 'context-ref-v1', 'permission-v1')

    context_fields=('id', 'context_class', 'owner', 'kind', 'origin',
    'version', 'sensitivity', 'freshness', 'uses', 'boundary_read',
    'boundary_write')

  FOCUSED RED A — HANDLER WITHOUT CALL SITES

    $ uv run --locked python tools/check.py --files src/runtime/handler_registry.py tests/runtime/test_handler_registry.py
    exit=1
    zaratusta check | contract 36 | python 3.13.7
    --- static (config, hygiene): ok
    --- format
    2 files already formatted
    --- lint
    All checks passed!
    --- boundary

    ╔══╗─────────▶╔╗ ╔╗      ╔╗◀───┐
    ╚╣╠╝◀─────┐  ╔╝╚╗║║────▶╔╝╚╗   │
     ║║   ╔══╦══╦╩╗╔╝║║  ╔╦═╩╗╔╝╔═╦══╗
     ║║╔══╣╔╗║╔╗║╔╣║ ║║ ╔╬╣╔╗║║ ║│║╔═╝
    ╔╣╠╣║║║╚╝║╚╝║║║╚╗║╚═╝║║║║║╚╗║═╣║
    ╚══╩╩╩╣╔═╩══╩╝╚═╝╚═══╩╩╝╚╩═╩╩═╩╝
      └──▶║║                    ▲
          ╚╝────────────────────┘

    ---------
    Contracts
    ---------

    Analyzed 30 files, 72 dependencies.
    -----------------------------------

    Layers: runtime over vocabulary over foundation, never upwards KEPT
    foundation is independent of every other module KEPT
    vocabulary is a dictionary: it knows nothing of the layer above it KEPT

    Contracts: 3 kept, 0 broken.
    --- types
    Success: no issues found in 2 source files
    --- tests
    .F...                                                                    [100%]
    ================================== FAILURES ===================================
    ________ test_every_registered_handler_declares_at_least_one_call_site ________

        def test_every_registered_handler_declares_at_least_one_call_site() -> None:
            findings = validate_handler_registry(HANDLER_REGISTRY, STEP_CALLS)

    >       assert all(
                finding.violation is not RegistryViolation.HANDLER_WITHOUT_CALL_SITE for finding in findings
            )
    E       assert False

    tests\runtime\test_handler_registry.py:26: AssertionError
    =========================== short test summary info ===========================
    FAILED tests/runtime/test_handler_registry.py::test_every_registered_handler_declares_at_least_one_call_site
    1 failed, 4 passed in 0.10s

    RED: tests

  CLEANUP A

    worktree_blob exit=0
    12feca5feaeaffbeb58954c7c1ba333f309deb20
    index_blob exit=0
    12feca5feaeaffbeb58954c7c1ba333f309deb20
    cleanup_diff exit=0

  FOCUSED RED B — UNREGISTERED HANDLER

    $ uv run --locked python tools/check.py --files src/runtime/handler_registry.py tests/runtime/test_handler_registry.py
    exit=1
    zaratusta check | contract 36 | python 3.13.7
    --- static (config, hygiene): ok
    --- format
    2 files already formatted
    --- lint
    All checks passed!
    --- boundary

    ╔══╗─────────▶╔╗ ╔╗      ╔╗◀───┐
    ╚╣╠╝◀─────┐  ╔╝╚╗║║────▶╔╝╚╗   │
     ║║   ╔══╦══╦╩╗╔╝║║  ╔╦═╩╗╔╝╔═╦══╗
     ║║╔══╣╔╗║╔╗║╔╣║ ║║ ╔╬╣╔╗║║ ║│║╔═╝
    ╔╣╠╣║║║╚╝║╚╝║║║╚╗║╚═╝║║║║║╚╗║═╣║
    ╚══╩╩╩╣╔═╩══╩╝╚═╝╚═══╩╩╝╚╩═╩╩═╩╝
      └──▶║║                    ▲
          ╚╝────────────────────┘

    ---------
    Contracts
    ---------

    Analyzed 30 files, 72 dependencies.
    -----------------------------------

    Layers: runtime over vocabulary over foundation, never upwards KEPT
    foundation is independent of every other module KEPT
    vocabulary is a dictionary: it knows nothing of the layer above it KEPT

    Contracts: 3 kept, 0 broken.
    --- types
    Success: no issues found in 2 source files
    --- tests
    ..F..                                                                    [100%]
    ================================== FAILURES ===================================
    ______________ test_every_handler_called_by_a_step_is_registered ______________

        def test_every_handler_called_by_a_step_is_registered() -> None:
            findings = validate_handler_registry(HANDLER_REGISTRY, STEP_CALLS)

    >       assert all(
                finding.violation is not RegistryViolation.UNREGISTERED_HANDLER for finding in findings
            )
    E       assert False

    tests\runtime\test_handler_registry.py:34: AssertionError
    =========================== short test summary info ===========================
    FAILED tests/runtime/test_handler_registry.py::test_every_handler_called_by_a_step_is_registered
    1 failed, 4 passed in 0.11s

    RED: tests

  CLEANUP B

    worktree_blob exit=0
    12feca5feaeaffbeb58954c7c1ba333f309deb20
    index_blob exit=0
    12feca5feaeaffbeb58954c7c1ba333f309deb20
    cleanup_diff exit=0

  FULL DELIVER ON COMMIT 6e8b3fcea623d0e0247c1b2a748e34508985286e

    $ uv run --locked python tools/check.py --deliver
    exit=0
    zaratusta check | contract 36 | python 3.13.7
    --- static (config, hygiene, deliver): ok
    --- format
    37 files already formatted
    --- lint
    All checks passed!
    --- boundary

    ╔══╗─────────▶╔╗ ╔╗      ╔╗◀───┐
    ╚╣╠╝◀─────┐  ╔╝╚╗║║────▶╔╝╚╗   │
     ║║   ╔══╦══╦╩╗╔╝║║  ╔╦═╩╗╔╝╔═╦══╗
     ║║╔══╣╔╗║╔╗║╔╣║ ║║ ╔╬╣╔╗║║ ║│║╔═╝
    ╔╣╠╣║║║╚╝║╚╝║║║╚╗║╚═╝║║║║║╚╗║═╣║
    ╚══╩╩╩╣╔═╩══╩╝╚═╝╚═══╩╩╝╚╩═╩╩═╩╝
      └──▶║║                    ▲
          ╚╝────────────────────┘

    ---------
    Contracts
    ---------

    Analyzed 30 files, 72 dependencies.
    -----------------------------------

    Layers: runtime over vocabulary over foundation, never upwards KEPT
    foundation is independent of every other module KEPT
    vocabulary is a dictionary: it knows nothing of the layer above it KEPT

    Contracts: 3 kept, 0 broken.
    --- types
    Success: no issues found in 34 source files
    --- tests
    ........................................................................ [ 42%]
    ........................................................................ [ 85%]
    .........................                                                [100%]
    169 passed in 0.14s

    GREEN: static, format, lint, boundary, types, tests

  FULL SELFCHECK ON COMMIT 6e8b3fcea623d0e0247c1b2a748e34508985286e

    $ uv run --locked python tools/selfcheck.py
    exit=0
    ok   test-layout red
    ok   test-layout green
    ok   orphan-tests red
    ok   orphan-tests green
    ok   skipped-test red
    ok   skipped-test green
    ok   empty-test red
    ok   empty-test green
    ok   scratch red
    ok   scratch keeper red
    ok   scratch green
    ok   shell-script red
    ok   backslash red
    ok   drive-path red
    ok   config-backslash red
    ok   allow-hatch green
    ok   launch-lines green
    ok   launch-drift red
    ok   launch-missing red
    ok   launch-no-readme red
    ok   config missing red
    ok   config key missing red
    ok   config green
    ok   report missing red
    ok   report field red
    ok   cited-artifact red
    ok   report green
    ok   domain-word red
    ok   domain-stem red
    ok   domain green
    ok   transport-word red
    ok   transport-stem red
    ok   transport green
    ok   transport outside src green
    ok   eval red
    ok   importlib red
    ok   re.compile green
    ok   one-per-file green
    ok   two-in-a-file red
    ok   empty-entity-file red
    ok   unnamed-contract red
    ok   entity-in-machinery red
    ok   negative-controls green
    ok   no-rejected-sample red
    ok   no-conforming-sample red
    ok   uncovered-violation red
    ok   handler-registry green
    ok   handler-without-call-site red
    ok   handler-without-call-site red cleanup
    ok   unregistered-handler red
    ok   unregistered-handler red cleanup
    ok   boundary green
    ok   boundary red (runtime)
    ok   boundary red (vocabulary)
    ok   boundary cleanup
    ok   conformance green
    ok   conformance red
    ok   conformance cleanup
    ok   context-translation green
    ok   boundary-write red
    ok   boundary-write red cleanup
    ok   freshness-windows red
    ok   freshness-windows red cleanup
    ok   automaton-instructions green
    ok   unknown-opcode red
    ok   unknown-opcode red cleanup
    ok   undeclared-condition red
    ok   undeclared-condition red cleanup
    ok   undeclared-action red
    ok   undeclared-action red cleanup

    SELFCHECK GREEN: 70 controls, every gate provably fails on a seeded miss

  OFFICIAL DOMAIN/TRANSPORT GATES ON COMMITTED TREE

    domain_free_findings=0
    transport_free_findings=0
    no_dynamic_python_findings=0

  CLEAN TREE

    $ git status --short --branch
    ## feat/health-contracts

    git diff --exit-code: 0
    git diff --cached --exit-code: 0

  `git push` не запускался. Создан только локальный commit; push остаётся
  владельцу.

state_changes: |
  1. Закрыть returning call
     `c-solmax-zaratustra-health-registry-048` со статусом `done`.

  2. Установить существующей карточке `t-health-registry` статус `done`.
     Основание: light-close evidence выше отдельно разрешает каждую строку
     done_when по commit/bytes/command-output tokens.

  3. NOW, активную ставку, остальные task/node/call/decision/knowledge cards
     сохранить без изменений. Следующий Direction-CALL из продукта не
     создавать.

captures: |
  Ничего. Runner, предметные обработчики и дальнейшая последовательность
  задач сознательно не входили в CALL.

decisions_needed: |
  Ничего. Все acceptance lines механически проверяемы; owner-verdict не
  требуется.

play_check: |
  1. Recite — done: реализован только явный registry и две стороны
     call-site invariant для активной задачи ставки.
  2. Owner inputs — skipped lawfully: CALL, predecessor и repo contract
     полностью задают результат; owner-content не вводился.
  3. Do the work — done: runtime typed records, validator, public surface,
     ADR, tests и две selfcheck-подсадки закоммичены.
  4. Self-check — done: обе focused подсадки дали ожидаемый RED и восстановили
     исходный blob; committed --deliver, 70-control selfcheck и официальные
     domain/transport gates зелёные.
  5. Close — done: close: light; точный commit/parent/manifest, чистое дерево
     и отсутствие push зафиксированы. Successor Direction-CALL не выдаётся.

log: |
  Создан явный domain-free handler registry и двусторонний build-инвариант
  call sites на локальном commit 6e8b3fc: handler без call site и step call
  к незарегистрированному handler реально роняют ту же tools/check.py;
  selfcheck автоматически восстанавливает обе подсадки и дал 70 controls;
  --deliver дал 169 passed, official domain/transport findings нулевые,
  четырнадцать contracts и context/automaton boundary не изменены, дерево
  чистое, push не выполнялся; t-health-registry закрывается light.

next: |
  HOME to Direction OS solmax. Следующий Direction-CALL из продуктового
  репозитория не выдаётся; свежий frontier разрешает Direction writer после
  применения этого RESULT.

END_OF_FILE: live/solmax/history/2026-09-01-s-solmax-zaratustra-health-registry-049.md
