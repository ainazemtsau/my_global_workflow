RESULT s-shape-001 (call: c-shape-001)
direction: solmax   play: shape   node/task: g-kernel

outcome: |
  g-kernel оформлен как активируемая Wave-0 ставка: "RLK kernel — tiny extensible core".
  Ставка держит исход map без перепланирования: крошечное ядро из ровно 5 частей,
  доказанное через CI: 3-й plugin = 1 register() + 1 handler, 0 строк диффа ядра;
  replay-тест зелёный; effect-tier gate отклоняет tier-2 без owner approval.

  Appetite: 1 calendar week / 3 focused executor-sized increments, без продления.
  Текущая дата shape: 2026-06-15. kill_by: 2026-06-22.

  Выбранный подход:
    "Build tiny kernel + executable acceptance tests in the new Zaratusta repo."
    Почему он выбран: он напрямую доказывает SC2 механически и держит anti-perpetual-draft
    через тесты, а не через документацию.

  Минимальное решение:
    - new product repo Zaratusta initialized as an agent-ready modular repo;
    - one W0 RLK change/spec with acceptance tests;
    - minimal library/core implementing exactly:
      1. Capability Registry;
      2. append-only JSONL ledger with schema_version and reserved upcaster seam;
      3. typed CALL/RESULT envelope + boundary validator;
      4. effect-tier gate 0/1/2 -> owner approval for tier-2;
      5. Engine + Store seams with fake/no-op adapters only;
    - fake capabilities only for proving 0-diff extensibility;
    - CI evidence for 0-diff, replay, and gate rejection.

  Не входит:
    - real claude/codex/API engine implementation;
    - always-on subscriptions, budget accounting, failover;
    - Telegram/voice/channel, web surface, board, kanban;
    - memory/RAG/vector/SQLite-fold beyond JSONL replay;
    - OS write capability;
    - productization, multi-user/auth, deployment, marketplace/plugin catalog.

evidence: |
  Source state read:
    - live/solmax/NOW.md: active_bet.node = none; active_tasks = []; c-shape-001 ready.
    - live/solmax/TREE.md: g-kernel exists as parked W0 node with 5-part RLK done_when.
    - live/solmax/CHARTER.md: lenses, constraints, risk_posture=explore, product repo Zaratusta.
    - live/solmax/history/s-map-001.md: map owner-approved g-kernel first; full card rationale.
    - os/plays/shape.md: shape steps G6/G4 task/cut/lens/kill requirements.
    - os/engineering/PROJECT_SETUP.md and profiles/README.md: first engineering CALL for a
      non-initialized product repo is repo setup; profile absence creates a profile as byproduct.

  Shape evidence:
    - G1: no active bet; active_tasks empty before this shape.
    - G2: tasks are written only into NOW active bet; TREE remains outcome-level.
    - G3: appetite fixed before solution choice: 1 calendar week / 3 focused executor increments.
    - G4: done_when and kill_by are set.
    - G5: final done is not claimed; completion requires executor evidence + later verification.
    - G6: cut_list has real cuts; lens verdicts cover all 6 charter lenses; riskiest assumption
      is tested early via acceptance harness and 0-diff proof tasks.
    - G9: TREE.md change has explicit owner_approved marker in state_changes, citing the
      owner’s actual correction/approval words.

state_changes: |
  TREE.md:
    owner_approved: true
    owner_approved_by: owner
    owner_approved_for: "activate and shape g-kernel node as the active Wave-0 bet"
    owner_approved_words: |
      "Нужно вернуть исправленный RESULT из shape-сессии с явной отметкой approval для TREE-изменения; после этого writer сможет применить пакет и выдать c-work-kernel-t1."
    edits:
      - Change g-kernel.status: parked -> active.
      - Add shaped fields to g-kernel:
          appetite: "1 calendar week / 3 focused executor-sized increments; no extension"
          kill_by: "2026-06-22: kill/review if W0 acceptance cannot be made green without a 6th
            kernel part, if third plugin requires kernel edits, or if repo setup/CI is still absent."
          shaped_detail: history/s-shape-001.md
      - Keep existing g-kernel.detail: history/s-map-001.md

  NOW.md:
    active_bet:
      node: g-kernel
      title: "Wave-0 — RLK tiny kernel"
      status: active
      appetite: "1 calendar week / 3 focused executor-sized increments; no extension"
      started_at: 2026-06-15
      kill_by:
        date: 2026-06-22
        metric: "W0 acceptance proof"
        threshold: |
          Kill/review if any hold:
            1. no initialized Zaratusta repo with CI and RLK acceptance spec exists by date;
            2. implementing W0 requires adding a 6th kernel part;
            3. third plugin cannot be added as register()+handler with 0 kernel diff;
            4. replay-test or tier-2 gate-test cannot pass without widening scope.
        next_if_true: |
          Open review/verify: refute W0 evidence, then if green mark g-kernel done and shape g-engine.
        next_if_false: |
          Stop appetite. Review: either shrink to repo-setup-only bet or re-shape g-kernel;
          do not extend this bet.
      done_when: |
        Exactly 5 parts and no more:
          1. Capability Registry.
          2. Append-only JSONL ledger with schema_version and reserved upcaster seam.
          3. Typed CALL/RESULT envelope + boundary validator.
          4. Effect-tier gate 0/1/2 -> owner approval for tier-2.
          5. Engine + Store seams.
        CI proves:
          - 0-diff test: adding the 3rd plugin requires 1 register() + 1 handler and 0 kernel edits.
          - replay-test: write -> read -> restore from JSONL ledger.
          - gate-test: tier-2 action without owner approval is rejected.
      approach: |
        Build tiny kernel + executable acceptance tests in the new Zaratusta repo.
      approaches_considered:
        - build: "Tiny RLK library + acceptance tests in Zaratusta" -> selected.
          assumption: "Five-part kernel can stay small while the third plugin is 0-diff."
        - fake_or_reuse: "Start from an existing agent/memory framework and wrap it."
          rejected: "Likely imports hidden kernel decisions and bloats the core."
        - make_unnecessary: "Only write specs/contracts now, postpone code."
          rejected: "Does not satisfy CI/replay/gate done_when."
      minimal_solution: |
        Local-first W0 kernel with fake Engine and fake capabilities only. The product of this
        bet is not a useful assistant; it is a mechanically tested extension substrate.
      not_included:
        - "No real subscription/API engine; Engine seam only with fake/no-op adapter."
        - "No channels, UI/surface, memory/RAG, SQLite/vector store, or dogfood feature."
        - "No OS writing; OS may only become future read-only capability outside W0."
        - "No deployment, multi-user/auth, product packaging, or marketplace."
        - "No 6th kernel part; any need for one triggers review."
      cut_list:
        - cut: "Real claude -p / codex engine implementation."
          why_cut: "Belongs to g-engine; W0 only proves Engine seam."
          parked_to: g-engine
        - cut: "Telegram/voice channel and web surface."
          why_cut: "Belong to g-channel/g-surface; adding them now hides kernel proof inside UI work."
          parked_to: "g-channel / g-surface"
        - cut: "Memory/RAG/SQLite/vector fold."
          why_cut: "Belongs to g-memory; W0 only needs JSONL replay."
          parked_to: g-memory
        - cut: "Actual OS read capability."
          why_cut: "Belongs to g-accrete and must be hard read-only; W0 only forbids OS writes."
          parked_to: g-accrete
        - cut: "Production deployment, multi-user/auth, encryption/key management beyond local dev."
          why_cut: "Not needed to prove local-first kernel mechanics; would inflate W0."
          parked_to: "future review when external surface exists"
        - cut: "Any 6th kernel subsystem."
          why_cut: "Directly violates g-kernel boundary; if needed, kill/review instead of adding."
          parked_to: "none; stop trigger"
      lens_verdicts:
        Extensibility:
          verdict: "task"
          task: "t-2/t-3"
          reason: "Registry + 0-diff third-plugin CI is the core proof."
        Real depth:
          verdict: "not_needed"
          reason: "W0 is substrate, not a deep process; depth starts at g-cognition. W0 preserves ledger evidence for it."
        Agent-buildability:
          verdict: "task"
          task: "t-1"
          reason: "First task creates the repo feedback loop, contracts, CI, AGENTS/REVIEW/OpenSpec."
        Daily use / dogfood:
          verdict: "not_needed"
          reason: "Kernel is not owner-facing; dogfood starts with g-channel/g-surface/g-cognition. W0 uses mechanical smoke tests only."
        Privacy / trust / safety:
          verdict: "task"
          task: "t-2/t-3"
          reason: "Effect-tier gate, boundary validator, local JSONL ledger, and OS-write exclusion are W0 acceptance checks."
        Cost discipline:
          verdict: "not_needed"
          reason: "No model/API/subscription calls in W0; fake Engine seam only. Subscription budgeting is g-engine."
      assumptions_ranked:
        - rank: 1
          assumption: "The 5-part RLK can stay tiny while the 3rd plugin is 0-diff."
          kill_power: "If false, SC2 fails and anti-perpetual-draft risk is active."
          test: "t-2/t-3 acceptance and diff proof."
        - rank: 2
          assumption: "schema_version + reserved upcaster seam is enough for replay without migration complexity."
          kill_power: "If false, ledger/replay trust breaks."
          test: "t-2/t-3 replay-test."
        - rank: 3
          assumption: "effect-tier gate and boundary validator can stay independent of channels/tools."
          kill_power: "If false, privacy/safety architecture entangles the kernel."
          test: "t-2/t-3 gate-test."
        - rank: 4
          assumption: "Repo feedback loop can constrain background agents before kernel code grows."
          kill_power: "If false, agent slop/review backlog starts immediately."
          test: "t-1 setup checklist."
        - rank: 5
          assumption: "Engine/Store seams can postpone real engine/API decisions."
          kill_power: "If false, W0 leaks into g-engine."
          test: "t-2 fake adapter only."
      evaluator: |
        After t-3, a separate review/verify session must try to refute:
          - "third plugin = 0 kernel diff";
          - replay correctness;
          - tier-2 rejection without approval;
          - no 6th kernel part.
        The executor's own report is not enough to mark g-kernel done.
      rollback: |
        If any acceptance proof requires widening W0, revert the product repo change/PR,
        keep history evidence, mark task failed, and trigger review. Do not patch the OS repo
        from the product repo; state changes return only through RESULT.
      forecast: |
        65%: W0 green inside appetite if repo setup is kept austere and Engine remains fake.
        Main risk is setup/toolchain appetite creep, not kernel logic.
      against: |
        This bet should die rather than stretch if the implementation asks for real engine,
        channel, memory, deployment, or a 6th kernel component.

    active_tasks:
      - id: t-1
        status: ready
        kind: executor
        goal: |
          Zaratusta product repo exists with an agent-ready feedback loop and W0 RLK acceptance
          spec/harness prepared.
        done_when: |
          Repo github.com/ainazemtsau/zaratusta is created/initialized locally at C:\projects\Zaratusta
          or the executor reports the exact blocker. PROJECT_SETUP done_when checklist is reported
          with evidence. OpenSpec/change for W0 RLK exists with acceptance tests for:
          0-diff plugin proof, JSONL replay, and tier-2 gate rejection. No RLK product code is required
          beyond skeleton/failing acceptance harness in this task.
        tests_assumption: "Repo feedback loop can constrain agents before kernel code grows."

      - id: t-2
        status: ready
        kind: executor
        goal: |
          Minimal RLK vertical slice implements exactly the 5 kernel parts behind small seams.
        done_when: |
          One-command check is green for registry, JSONL ledger with schema_version/upcaster seam,
          typed CALL/RESULT envelope + boundary validator, effect-tier gate, and Engine/Store fakes.
          No real engine, channel, UI, memory/RAG, OS write path, or 6th kernel part exists.
        tests_assumption: "5-part core can stay tiny without leaking into future waves."

      - id: t-3
        status: ready
        kind: executor
        goal: |
          W0 acceptance proof is green: third plugin requires 0 kernel diff; replay and gate tests pass.
        done_when: |
          CI green. Evidence shows adding the 3rd fake plugin changed only registration/handler
          outside kernel. Replay-test write->read->restore passes. Gate-test rejects tier-2 without
          owner approval. Executor RESULT.md includes outcome/evidence/assumptions/cuts/cost/
          manual-acceptance/next and does not author the next OS task CALL.
        tests_assumption: "0-diff extensibility is mechanically provable, not rhetorical."

    open_calls:
      - id: c-shape-001
        status: done
      - id: c-work-kernel-t1
        status: ready
        note: "Executor CALL for g-kernel/t-1 repo setup + W0 acceptance harness."

    next: |
      CALL c-work-kernel-t1
      to: executor
      direction: solmax
      node: g-kernel   task: t-1
      repo: github.com/ainazemtsau/zaratusta
      kind: engineering
      goal: |
        Zaratusta product repo exists with an agent-ready feedback loop and W0 RLK acceptance
        spec/harness prepared, so background agents can build the tiny RLK under mechanical gates.
      context: |
        - Direction state: live/solmax/NOW.md, live/solmax/TREE.md, live/solmax/CHARTER.md.
        - g-kernel full rationale: live/solmax/history/s-map-001.md.
        - Product repo proposed: github.com/ainazemtsau/zaratusta; local path C:\projects\Zaratusta.
        - Engineering setup procedure: os/engineering/PROJECT_SETUP.md.
        - Stack profiles: os/engineering/profiles/README.md; check for existing matching profile first.
        - W0 RLK acceptance target:
          exactly 5 parts and no more:
            1. Capability Registry;
            2. append-only JSONL-ledger with schema_version and reserved upcaster seam;
            3. typed CALL/RESULT envelope + boundary validator;
            4. effect-tier gate 0/1/2 -> owner approval for tier-2;
            5. Engine + Store seams.
        - Build mode: background agents, small independently-verifiable increments.
      boundaries: |
        - Do not write to the workflow OS repo.
        - Do not implement real claude/codex/API engine; only fake/no-op Engine seam if needed.
        - Do not build channels, UI/surface, memory/RAG, deployment, auth, marketplace, or OS-read capability.
        - Do not add a 6th kernel component.
        - Do not author the next OS CALL; executor returns RESULT.md/evidence only.
        - If stack choice is missing, run the short PROJECT_SETUP stack interview and record ADR-0001.
      done_when: |
        All hold or exact blocker is reported:
          - repo exists locally and/or remotely at the proposed locations;
          - one-command check + CI feedback loop exists per PROJECT_SETUP;
          - root AGENTS.md, CLAUDE.md, REVIEW.md, validation.config, docs/adr/ADR-0001,
            docs/FRICTION.md, openspec/, _scratch/, and module AGENTS.md exist as applicable;
          - dependency-boundary check and seeded violation proof exist;
          - deliver-time RESULT.md gate exists and fails on missing/invalid RESULT.md;
          - W0 RLK OpenSpec/change exists with acceptance criteria/tests for 0-diff plugin proof,
            JSONL replay, and tier-2 gate rejection;
          - setup checklist evidence is reported item by item.
      return: |
        Executor RESULT.md with:
          outcome, evidence, assumptions, cuts, cost, manual-acceptance, next.
        Include commit/PR links or local commit hash, check output, seeded-failure evidence,
        and any stack-profile state_changes that the workflow writer must apply.
      budget: one executor increment

  history/:
    - Add live/solmax/history/s-shape-001.md containing this RESULT verbatim.

  LOG.md:
    - Add newest-first:
      "2026-06-15 — shape g-kernel: Wave-0 RLK оформлен как активная ставка
      (appetite 1 week; 3 executor tasks; cuts: no engine/channel/UI/memory/API/OS write/6th part);
      TREE activation owner_approved in s-shape-001; next → c-work-kernel-t1 repo setup + W0
      acceptance harness. → history/s-shape-001.md"

captures:
  - "Losing approach: reuse/wrap existing agent or memory framework later only if W0 fails; default parked because it risks hidden kernel bloat."
  - "Losing approach: spec-only kernel without code; parked because it cannot satisfy CI/replay/gate evidence."
  - "Future security hardening: encryption/key management for external surfaces; not W0, revisit when g-channel/g-surface exposes data beyond local dev."

decisions_needed: []

play_check:
  - 1 recite: done — g-kernel goal/done_when restated from TREE/history; parent g-zara outcome is personal exocortex with tiny extensible RLK; node goal is an outcome, not an activity.
  - 2 appetite first: done — appetite fixed before solution talk: 1 calendar week / 3 focused executor increments; outside-view comparables: repo setup feedback loop, small library vertical slice, acceptance proof.
  - 3 approaches then minimal solution: done — compared build vs reuse/wrap vs spec-only; selected build tiny kernel + executable acceptance tests; losing approaches captured.
  - 4 scope hammer: done — cut_list has real cuts: real engine, channels, UI/surface, memory/RAG, OS read/write, deployment/auth, 6th part.
  - 5 lens sweep: done — all 6 charter lenses have verdicts: Extensibility task; Real depth not_needed; Agent-buildability task; Daily use not_needed; Privacy/trust task; Cost discipline not_needed.
  - 6 riskiest assumption: done — assumptions ranked by kill-power; top assumption tested through t-2/t-3, with t-1 constraining agent-buildability first.
  - 7 tasks: done — 3 tasks, each executor-sized; t-1 repo setup/acceptance harness, t-2 minimal 5-part vertical slice, t-3 0-diff/replay/gate proof; evaluator and rollback named first for executor-heavy bet.
  - 8 kill criteria: done — kill_by metric + threshold + date set; next_if_true and next_if_false defined; no appetite extension.
  - 9 close (owner): done — owner explicitly approved the required TREE-change correction and apply path with: "Нужно вернуть исправленный RESULT из shape-сессии с явной отметкой approval для TREE-изменения; после этого writer сможет применить пакет и выдать c-work-kernel-t1."

log: shape g-kernel — Wave-0 RLK активирован как 1-week bet with 3 executor tasks; TREE owner_approved; next c-work-kernel-t1

next: |
  CALL c-work-kernel-t1
  to: executor
  direction: solmax
  node: g-kernel   task: t-1
  repo: github.com/ainazemtsau/zaratusta
  kind: engineering
  goal: |
    Zaratusta product repo exists with an agent-ready feedback loop and W0 RLK acceptance
    spec/harness prepared, so background agents can build the tiny RLK under mechanical gates.
  context: |
    - Direction state: live/solmax/NOW.md, live/solmax/TREE.md, live/solmax/CHARTER.md.
    - g-kernel full rationale: live/solmax/history/s-map-001.md.
    - Product repo proposed: github.com/ainazemtsau/zaratusta; local path C:\projects\Zaratusta.
    - Engineering setup procedure: os/engineering/PROJECT_SETUP.md.
    - Stack profiles: os/engineering/profiles/README.md; check for existing matching profile first.
    - W0 RLK acceptance target:
      exactly 5 parts and no more:
        1. Capability Registry;
        2. append-only JSONL-ledger with schema_version and reserved upcaster seam;
        3. typed CALL/RESULT envelope + boundary validator;
        4. effect-tier gate 0/1/2 -> owner approval for tier-2;
        5. Engine + Store seams.
    - Build mode: background agents, small independently-verifiable increments.
  boundaries: |
    - Do not write to the workflow OS repo.
    - Do not implement real claude/codex/API engine; only fake/no-op Engine seam if needed.
    - Do not build channels, UI/surface, memory/RAG, deployment, auth, marketplace, or OS-read capability.
    - Do not add a 6th kernel component.
    - Do not author the next OS CALL; executor returns RESULT.md/evidence only.
    - If stack choice is missing, run the short PROJECT_SETUP stack interview and record ADR-0001.
  done_when: |
    All hold or exact blocker is reported:
      - repo exists locally and/or remotely at the proposed locations;
      - one-command check + CI feedback loop exists per PROJECT_SETUP;
      - root AGENTS.md, CLAUDE.md, REVIEW.md, validation.config, docs/adr/ADR-0001,
        docs/FRICTION.md, openspec/, _scratch/, and module AGENTS.md exist as applicable;
      - dependency-boundary check and seeded violation proof exist;
      - deliver-time RESULT.md gate exists and fails on missing/invalid RESULT.md;
      - W0 RLK OpenSpec/change exists with acceptance criteria/tests for 0-diff plugin proof,
        JSONL replay, and tier-2 gate rejection;
      - setup checklist evidence is reported item by item.
  return: |
    Executor RESULT.md with:
      outcome, evidence, assumptions, cuts, cost, manual-acceptance, next.
    Include commit/PR links or local commit hash, check output, seeded-failure evidence,
    and any stack-profile state_changes that the workflow writer must apply.
  budget: one executor increment

END_OF_FILE: live/solmax/history/s-shape-001.md
