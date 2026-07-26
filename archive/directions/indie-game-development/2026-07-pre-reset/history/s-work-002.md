# RESULT — s-work-002 (work, 2026-06-13) — g-9c41/t-1 re-planned: product repo FULL re-create (c-setup-001)

```yaml
RESULT s-work-002 (call: c-work-001, continued — owner re-opened the plan)
direction: indie-game-development   play: work   node/task: g-9c41 / t-1
outcome: |
  The plan for t-1 is re-sequenced to SETUP-FIRST. The owner decided (2026-06-13) to fully
  delete and RE-CREATE the product repo from scratch through our process (PROJECT_SETUP),
  rather than build t-1 on the existing foundation — to standardize on the OS rules and kill
  the dual-harness confusion. Decisions locked: (R1) full delete + re-create; (R2) strictly
  our process from the start; (R3) latest Unity = 6.3 LTS (verified: the old repo's 6000.4.x
  was the 6.4 TECH-STREAM, non-LTS; 6.3 LTS / 6000.3.x is the production-correct latest); (R4)
  a NEW repo. The owner has NO deep Unity experience and explicitly delegated the two technical
  questions to me, asking that I verify his domain assumptions and give simple advice — so I
  decided them with plain rationale: engine-free core targets netstandard2.1 (Unity can always
  load it) + a net8.0 test project; core-gate CI from day one (no Unity license), Unity PlayMode
  CI DEFERRED until engine-dependent tests exist. Setup executor CALL c-setup-001 framed (repo
  bootstrap per PROJECT_SETUP). The retired c-exec-001 (which reused the now-to-be-deleted
  foundation) is superseded. The OS-vs-repo harness maintenance flag is RESOLVED by this
  decision (the codex-native-execution-layer harness is retired in favour of the OS CONTOUR).
evidence: |
  - Owner words (this exchange): "ПОЛНОСТЬЮ удалить все файлы и заново инициализировать проект
    ПО НАШИМ ПРАВИЛАМ"; "проект практически пустой и нам не нужный... можем и новый репозиторий
    создать"; "давай заново... полностью удалять и идти по нашему процессу с самого начала";
    "нужно последнюю [Unity] использовать"; repo: "1 давай новый"; tech Qs: "2 не понимаю что
    это значит / 3 ... полагаюсь тут на тебя возьми что реально лучше для нас"; "у меня нет
    глубокого опыта с Unity... технически ты должен проверять мои предположения... давать очень
    простые советы... большой опыт в программировании но в enterprise".
  - Unity version verified (web, June 2026): 6.3 = latest LTS (6000.3.x, supported to Dec 2027);
    6.4 (6000.4.x, e.g. the old repo's 6000.4.7f1) = Mainline/tech stream, NOT LTS. For a
    commercial Steam build, LTS is correct -> owner's "6.3" validated with a reason.
    Sources: unity.com/releases/unity-6/support; unity.com/releases/editor/whats-new/6000.3.0f1;
    unity.com/releases/editor/whats-new/6000.4.9f1.
state_changes: |
  live/indie-game-development/NOW.md:
    - active_tasks t-1: status `active` -> `blocked_on c-setup-001` (product repo being re-created
      from scratch; the t-1 build CALL issues after setup DONE). Goal/done_when unchanged.
    - open_calls: c-exec-001 RETIRED (superseded by full re-create) and REPLACED by c-setup-001
      (in_flight); c-frame-002 kept.
    - next: the c-exec-001 build CALL -> the full c-setup-001 setup CALL.
  live/indie-game-development/LOG.md: append the re-plan line -> history/s-work-002.md.
  live/indie-game-development/history/: + s-work-002.md (this RESULT).
  No TREE.md / CHARTER.md change; active_bet g-9c41 unchanged (appetite/kill_by intact, G3).
captures:
  - "FEEDBACK (also saved to memory): owner has deep ENTERPRISE programming experience (Java/full-stack) but NO deep Unity/gamedev experience. Verify/challenge his Unity-domain assumptions rather than accepting them; on technical questions give VERY simple advice, explain the proposal + what to choose, use enterprise analogies (TFM ~ Java version), avoid unexplained Unity jargon; when he says 'не понимаю' and delegates, decide with a plain-language rationale."
  - "RESOLVED: the s-work-001 maintenance capture (OS-CONTOUR vs codex-native-execution-layer dual harness) is closed by this decision — the product repo standardizes on the OS engineering contour; the codex layer is retired with the old repo. No maintenance session needed for this point."
  - "FRAME touch-up (updates c-frame-002 / charter canonization): product repo will be a NEW github.com/ainazemtsau/GasCoopGame (old renamed -> GasCoopGame-archive). Canonize the NEW repo + Unity 6.3 LTS in CHARTER.md once setup is DONE."
  - "SCHEDULE watch: the full repo re-create consumes part of the Fable-5 window (closes 2026-06-22); the t-1 net-spike now starts AFTER setup. Appetite is unchanged (6w to 2026-07-24, G3). Monitor that t-1..t-3 still fit before the 2026-06-30 kill-gate checkpoint; if setup eats too much, t-3 falls back to Opus 4.8 per NOW.md."
decisions_needed: []
play_check:
  - "1 recite: done — t-1 goal/done_when + bet g-9c41 restated (prior turns); confirmed t-1's build is now gated on a full repo re-create per the owner."
  - "2 owner-inputs (owner): done — this exchange WAS the owner-input step (PROJECT_SETUP step 1 stack interview). Owner decided R1 full delete+recreate, R2 strictly our process, R3 latest Unity (verified 6.3 LTS, not the repo's 6.4 tech-stream), R4 new repo ('давай новый'); delegated the two technical questions ('не понимаю... полагаюсь на тебя') and stated he has no deep Unity experience -> verify his assumptions + simple advice (his words quoted in evidence)."
  - "3 do-the-work: done — engineering path. Framed setup executor CALL c-setup-001 (repo bootstrap per PROJECT_SETUP). Decided the owner-delegated technical choices with plain-language rationale (PlayMode-CI deferred; core netstandard2.1 + tests net8.0). Did not design beyond the stack ADR — architecture detail is the executor's PLAN."
  - "4 self-check: done — c-setup-001 done_when = the PROJECT_SETUP mechanical checklist (green gates + evidence) + engine-free-core headless build + the unity.md profile byproduct. This is exactly the owner's ask to 'be sure everything sets up properly per our process'."
  - "5 close: done — this RESULT is the session's final authored message; t-1 -> blocked_on c-setup-001; c-exec-001 retired; next = c-setup-001; maintenance flag resolved; agent-CLI applies state_changes as its own writer after emitting this."
log: "2026-06-13 — work (g-9c41/t-1, re-plan): owner decided FULL clean RE-CREATE of the product repo via our process (PROJECT_SETUP) on a NEW repo, latest Unity = 6.3 LTS (verified — old repo was on 6.4 tech-stream, non-LTS). Old codex-native-execution-layer harness retired -> maintenance flag RESOLVED (standardize on OS). Decided owner-delegated tech choices with plain rationale: engine-free core netstandard2.1 + net8.0 tests; core-CI day-1, Unity PlayMode-CI deferred. Framed setup CALL c-setup-001 (clean-slate bootstrap, asmdef boundary, profiles/unity.md byproduct); retired c-exec-001 (built on the now-to-be-deleted foundation). t-1 -> blocked_on c-setup-001. next = c-setup-001 (owner installs Unity 6.3 LTS via Hub). -> history/s-work-002.md"
next: |
  CALL c-setup-001
  to: executor
  kind: engineering (repo bootstrap — os/engineering/PROJECT_SETUP.md)
  repo: NEW github.com/ainazemtsau/GasCoopGame (fresh; old repo renamed -> GasCoopGame-archive,
        kept read-only as evidence; local C:\projects\Unity\GasCoopGame re-created clean)
  direction: indie-game-development
  node: g-9c41   task: t-1 (PRECONDITION — setup runs BEFORE the t-1 build)
  parent: c-work-001
  goal: |
    A fresh, OS-aligned product repo exists and PASSES the PROJECT_SETUP done-when checklist:
    a clean Unity 6.3 LTS project whose architecture puts ALL game logic in an engine-free C#
    core that builds & tests HEADLESS (zero Unity refs, mechanically enforced), with Unity
    reduced to render/input/transport adapters — set up entirely through OUR process, not the
    old harness. This is the precondition the t-1 net-spike then builds on.
  context: |
    - REPLACES the old GasCoopGame (codex-native-execution-layer harness, Unity 6.4 tech-stream,
      A1_SETUP_ONLY). Full clean slate, owner-decided 2026-06-13 (R1 delete+recreate, R2 strictly
      our process, R3 latest Unity, R4 new repo). Old repo archived as evidence, never a build target.
    - Owner stack interview (PROJECT_SETUP step 1) -> ADR-0001:
      * Unity 6.3 LTS (6000.3.x, latest patch in Hub; LTS to Dec 2027). NOT the 6.4 tech stream.
      * Engine-free core = standalone .NET project (.csproj/.sln), TARGET netstandard2.1 (Unity can
        always load it); test project TARGET net8.0 via `dotnet test`. (R13.)
      * Unity = render/input/transport adapters only; networking is an edge wrapper (R14).
      * Net vendor FishNet enters in t-1, NOT setup (transport seam left empty).
      * Core-gate CI from day one (dotnet build/test + dependency-boundary lint — no Unity license);
        Unity PlayMode CI (GameCI + license secret) DEFERRED until engine-dependent tests exist.
    - Run contract to INSTALL = os/engineering/CONTOUR.md distilled into root AGENTS.md
      (planner/builder/validator; plan->ledger->build->gates->report; builder cannot weaken the
      oracle; retries<=3 then escalate; done = gates green + evidence). NOT the codex layer.
    - Bet rules R12-R15 (this NOW.md) constrain the architecture.
  boundaries: |
    - Owner has NO deep Unity experience: make every Unity-specific choice yourself with a
      plain-language rationale in the report; do not ask the owner to adjudicate Unity internals.
    - Owner physical step (cannot be automated — Hub GUI): install Unity 6.3 LTS + create the Unity
      project. Everything else (core .csproj, asmdefs, gates, CI, profile, run contract) is yours.
    - GitHub destructive ops (rename/archive the old repo, create the new one) need an explicit
      owner go at execution time before running them.
    - NO gameplay / gas / networking code in setup — the empty, gated skeleton only (t-1+ fill it).
    - Do NOT import old code/foundation (R2 clean slate). Old CoreFoundation/GridTopology are
      reference-only; re-create only what t-1 needs, fresh, in the new module layout.
  done_when: |
    The PROJECT_SETUP "Done when" checklist passes WITH EVIDENCE:
    - one-command check (format+lint+type+tests) green locally AND in CI;
    - dependency-boundary check exists and FAILS on a seeded violation (e.g. UnityEngine ref in core);
    - the engine-free core builds & tests HEADLESS via `dotnet` with ZERO Unity refs;
    - root AGENTS.md <=150 lines with working commands + the run-contract section; >=1 module AGENTS.md;
    - REVIEW.md, validation.config, docs/adr/ADR-0001 (the stack decision above), docs/FRICTION.md,
      openspec/ exist;
    - `_scratch/` exists and a seeded file in it cannot be committed;
    - test-hygiene gates fail on seeded violations;
    - os/engineering/profiles/unity.md CREATED (byproduct) and returned in state_changes;
    - Unity PlayMode CI with license recorded as DEFERRED (explicitly out until adapters exist).
  return: |
    REPORT: the PROJECT_SETUP checklist with evidence per item (commands + outputs), the new repo
    URL, ADR-0001 text, the created os/engineering/profiles/unity.md (in state_changes for the
    workflow repo), assumptions, anything deferred. State DONE | NEEDS INPUT | STUCK. Surface
    blockers early (Unity license, Hub install). On DONE -> next = the t-1 build CALL on the clean
    repo (engine-free core scaffold + 3-mode composition root + FishNet host+2-client hash handshake
    + honest FishNet verdict; the retired c-exec-001 is the template for it).
  budget: a focused one-time setup pass; 2x over or a hard blocker (license/Hub) -> stop & report.
  surface: cli; owner installs Unity 6.3 LTS via Hub in parallel.
```

END_OF_FILE: live/indie-game-development/history/s-work-002.md
