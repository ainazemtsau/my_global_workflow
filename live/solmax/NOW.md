# NOW — solmax

active_bet:
  node: g-kernel
  title: "Wave-0 — RLK tiny kernel"
  status: held_by_owner
  hold:
    since: 2026-06-17
    owner_words: "сейчас хочу отложить этот проект..."
    reason: |
      Owner redirected current priority from Solmax/W0 kernel work to a personal life reset:
      health, productivity, schedule, deep psychological work, binge-eating/insecurity work,
      and self-disclosure.
    effect: |
      Do not launch t-2 or t-3 while this hold is active.
      Do not re-issue c-converge-arch-kernel-001 while this hold is active.
      Q1-Q15 in work/converge-g-kernel.md are explicitly deferred, not answered.
      work/converge-g-kernel.md is not an API lock.
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
    status: done
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
    status: held_by_owner
    kind: executor
    goal: |
      Minimal RLK vertical slice implements exactly the 5 kernel parts behind small seams.
    done_when: |
      One-command check is green for registry, JSONL ledger with schema_version/upcaster seam,
      typed CALL/RESULT envelope + boundary validator, effect-tier gate, and Engine/Store fakes.
      No real engine, channel, UI, memory/RAG, OS write path, or 6th kernel part exists.
    tests_assumption: "5-part core can stay tiny without leaking into future waves."
    note: |
      Held by owner on 2026-06-17. Q1-Q15 are explicitly deferred with the whole project,
      not answered as API decisions. Do not launch as executor work until owner resumes Solmax
      and chooses the next route.

  - id: t-3
    status: held_by_owner
    kind: executor
    goal: |
      W0 acceptance proof is green: third plugin requires 0 kernel diff; replay and gate tests pass.
    done_when: |
      CI green. Evidence shows adding the 3rd fake plugin changed only registration/handler
      outside kernel. Replay-test write->read->restore passes. Gate-test rejects tier-2 without
      owner approval. Executor RESULT.md includes outcome/evidence/assumptions/cuts/cost/
      manual-acceptance/next and does not author the next OS task CALL.
    tests_assumption: "0-diff extensibility is mechanically provable, not rhetorical."
    note: |
      Held by owner on 2026-06-17. Depends on t-2 and on an active W0 route; do not launch
      while the Solmax/kernel hold is active.

recurring: []

open_calls:
  - id: c-shape-001
    status: done
  - id: c-work-kernel-t1
    status: done
    note: |
      Returned setup evidence: `ainazemtsau/zaratusta` exists, CI is green on
      18d74b1114428be8df5ece48bf6d89f3b2776a75, and W0 scaffold/gates/OpenSpec exist.
  - id: c-converge-kernel-001
    status: done
    note: |
      RETROFIT converge wrote `work/converge-g-kernel.md`, then repair corrected it from
      over-closed RESOLVE into FORM/AGENDA: only born-closed history imports are answered;
      Q1-Q15 require owner signoff before t-2/t-3 can freeze kernel API.
  - id: c-converge-arch-kernel-001
    status: blocked
    note: |
      Blocked/held after owner deferred the Solmax/W0 project on 2026-06-17.
      Q1-Q15 in work/converge-g-kernel.md are explicitly deferred, so the blocker is no longer
      "unsigned agenda items" alone; the active blocker is owner hold on the project.
      Re-issue converge-arch only if the owner resumes Solmax and sibling-bearing contracts
      still need architecture closure.
  - id: c-converge-kernel-q1-q15
    status: done
    note: |
      Closed as owner-approved deferral, not API answer. Owner chose to defer the current
      project: "сейчас хочу отложить этот проект..." Q1-Q15 are deferred; t-2/t-3 and
      converge-arch remain held.

decision_inbox:
  - q: "Accept TypeScript/Node 22 as the W0 setup stack?"
    options:
      - "Accept TypeScript/Node 22 for W0."
      - "Reject and rerun setup with another stack."
    recommendation: "Accept TypeScript/Node 22; it already has green local checks and CI for W0 repo setup."
  - q: "What should happen with the occupied local path `C:\projects\Zaratusta`?"
    options:
      - "Keep the product clone at `C:\projects\zaratusta-product`."
      - "Move/rename the existing non-git vault and reclone product repo to `C:\projects\Zaratusta`."
    recommendation: "Keep `C:\projects\zaratusta-product` unless exact local-path alignment matters; the proposed path contains pre-existing user content and is not a git repo."

next: |
  awaiting_new_session:
    recommended_next_CALL:
      id: c-frame-life-reset-001
      to: session
      direction: life-reset
      play: frame
      node: root
      goal: |
        Frame a new personal-life direction around health, productivity, schedule, deep
        psychological work, binge-eating/insecurity work, and self-disclosure, in a way that
        becomes grounded, safe, and operational rather than an unbounded self-overhaul.
      context: |
        Owner paused Solmax/W0 on 2026-06-17 with the words:
        "сейчас хочу отложить этот проект и занятсья тем что бы наладить свою жизнь..."
        Current desired territory:
        - become maximally productive and healthy;
        - establish a schedule;
        - seek a very deep transcendent / transformative experience;
        - dig deeply into psychology;
        - work through binge eating and insecurity;
        - meet "demons";
        - disclose/unfold the self.
      boundaries: |
        Do not continue Solmax/W0 in this session.
        Do not turn this into a huge abstract self-improvement manifesto.
        Do not prescribe medical or psychiatric treatment; if clinical risk appears, route to
        appropriate professional support.
        First frame must reduce the ambition into a safe, concrete first bet.
      done_when: |
        A first-direction frame exists with mission, constraints, success criteria, risk posture,
        and one candidate first bet small enough to start.
      return: |
        RESULT with proposed CHARTER/TREE state_changes only after owner approval, captures,
        decisions_needed if any, and next CALL.
      budget: one session

END_OF_FILE: live/solmax/NOW.md
