RESULT s-zara-operate-contract-t1-acceptance-matrix-checkpoint-002 (call: c-zara-operate-contract-t1-acceptance-matrix)
direction: solmax   play: work   node/task: g-zara-operate-contract/t-1

outcome: |
  Checkpoint only. Task t-1 remains active pending product-repo commit or PR evidence.

  The W20/A1-A13 acceptance matrix content is prepared and self-checked, but it
  is not yet product-repo evidence because no writer-core commit or PR has been
  returned.

  No further direct GitHub write was attempted after the owner correction.

  Prepared target product-repo file:
  openspec/changes/g-zara-operate-contract/acceptance-matrix.md

evidence: |
  Prepared matrix content covers the requested acceptance surface:

  - A1-A13 are all present.
  - Every A-row has:
    - coverage;
    - verifier rejection condition;
    - W19 guard.
  - W19 PLAN agenda has 10 explicit NOT CHOSEN items.
  - The matrix does not introduce a generic topic/domain blacklist.
  - The matrix does not select DB/API/UI/vendor/scheduler/automation/storage
    engine/exact schema/exact layout as the contract.
  - The matrix gives independent verifier checks for:
    - missing A-row coverage;
    - hidden HOW;
    - topic-open rule;
    - Zaratusta-only write boundary;
    - explicit scoped owner approval before high-effect actions.

  Static self-check performed in-session:
  - A-row headings found: A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13.
  - Each row contains "Coverage", "Verifier rejection condition", and "W19 guard".
  - W19 NOT CHOSEN item count: 10.

  Product-repo evidence is missing:
  - No writer-core commit hash.
  - No PR reference.
  - No product-repo check output.

  Therefore t-1 is not done.

state_changes: |
  NOW.md:
  - Keep t-1 status: active.
  - Add progress note to t-1:
    "Checkpoint s-zara-operate-contract-t1-acceptance-matrix-checkpoint-002
     prepared the W20/A1-A13 acceptance matrix content. t-1 remains active
     pending writer-core product-repo commit or PR evidence. Do not mark done
     until the product repo contains the matrix and check/evidence is returned."

  NOW.md open_calls:
  - Add the next CALL below.

captures:
  - Product-repo writes for this direction must be routed through writer core; normal sessions should return exact prepared content and product-repo evidence requirements.

decisions_needed: []

play_check:
  - 1 Recite: done; t-1 goal is product-repo evidence mapping W20/A1-A13 to Markdown-readable artifacts/checks without choosing W19 HOW.
  - 2 Owner inputs (owner): skipped; this is product-repo verification evidence, not owner-content the owner personally lives by, operates, or sends as his own.
  - 3 Do the work: checkpoint done; matrix content prepared, but product repo was not validly written.
  - 4 Self-check: done; content covers A1-A13 and W19 firewall, but original t-1 done_when is not met because product-repo commit/PR evidence is missing.
  - 5 Close: done as checkpoint; t-1 remains active pending writer-core product-repo evidence.

log: |
  work t-1 checkpoint: W20/A1-A13 acceptance matrix content prepared; t-1 remains active pending writer-core product-repo commit or PR evidence.

next: |
  CALL c-zara-operate-contract-t1-product-repo-matrix-evidence
  to: executor
  kind: engineering
  direction: solmax
  play: work
  node: g-zara-operate-contract
  task: t-1
  repo: github.com/ainazemtsau/zaratusta
  goal: |
    Product repo contains Markdown-readable evidence that maps W20/A1-A13 to
    concrete artifact/example/procedure/check coverage while keeping W19 choices
    unselected.
  context: |
    Active bet: b-zara-operate-contract-002.
    Product repo: github.com/ainazemtsau/zaratusta.

    Use writer core for product-repo writes. A normal session must not write to
    GitHub directly.

    Target product-repo file:
    openspec/changes/g-zara-operate-contract/acceptance-matrix.md

    Prepared file content:

    # g-zara-operate-contract — W20/A1-A13 Acceptance Matrix

    Status: product-repo evidence request for `b-zara-operate-contract-002` / `t-1`.

    This matrix is a Markdown-readable verifier surface. It maps each W20/A-row to
    the artifact, example, and check handles that must cover it. The handles are
    review handles, not future file paths, storage schema, database schema, UI
    layout, process cadence, scheduler design, automation plan, engine choice, API
    adapter, vendor choice, or repository layout.

    The storage location of this matrix in the product repo is a practical evidence
    location only. It does not select the future layout for source registry, process
    registry, owner context, examples, or checks.

    ## Source basis

    - Direction: `solmax`
    - Node: `g-zara-operate-contract`
    - Active bet: `b-zara-operate-contract-002`
    - Source WHAT: `live/solmax/work/converge-g-zara-operate-contract.md`
    - Verified source result:
      `live/solmax/history/2026-06-28-s-zara-operate-contract-converge-verify-trace-repair-004.md`
    - Binding surface: W20/A1-A13.
    - W19 status: PLAN agenda only; not selected as WHAT in this product layer.

    ## Artifact, example, procedure, and check handles

    These handles name concrete Markdown-readable evidence that the later contract
    pack must expose. They are intentionally path-free.

    ### Artifacts

    - `ART-MANAGER-ROLE-CARD`: manager role and authority boundary, separate from
      process, source, owner-context, and state artifacts.
    - `ART-SOURCE-REGISTRY-ENTRY`: source/context item card with source identity,
      scope, read/write status, freshness/trust marker, and allowed use.
    - `ART-PROCESS-CONTRACT`: inspectable process contract card with purpose, inputs,
      outputs, authority/effect tier, required source context, owner approval gates,
      and examples/tests.
    - `ART-OWNER-CONTEXT-CARD`: owner-context card for durable owner facts,
      preferences, decisions, approvals, evidence, unknowns, context summaries, and
      state-change requests inside the Zaratusta workspace.

    ### Procedure

    - `PROC-CONTEXT-LOAD`: context-loading procedure that declares loaded
      source/context bundle, missing context, and route when context is insufficient.

    ### Examples

    - `EX-CAPTURE-NONCOMMITMENT`: capture/backlog item is not an accepted commitment.
    - `EX-PLAN-PROPOSAL`: plan proposal is not an accepted commitment and names
      displacement before commitment change.
    - `EX-ET2-APPROVAL`: external, irreversible, spend, deletion, message/send, or
      material cross-system effect is blocked until explicit scoped owner approval
      exists.
    - `EX-TOPIC-OPEN-SOURCE-OWNED`: high-stakes or source-owned request is handled
      through source/process/context rather than refused by topic.
    - `EX-UNSOURCED-OR-UNAPPROVED-BLOCK`: unsourced source-owned instruction or
      unapproved side effect is blocked before effect.
    - `EX-OS-READ-ONLY`: Direction OS and other repos/directions/projects are
      read-only sources by default.

    ### Checks

    - `CHK-A-COVERAGE`: every A1-A13 row names artifact/example/procedure/check
      coverage and a rejection condition.
    - `CHK-TOPIC-OPEN`: no generic topic/domain exclusion list appears, and topic is
      not used as the refusal reason.
    - `CHK-WRITE-BOUNDARY`: Zaratusta default writes stay inside its own
      workspace/repo; Direction OS and other systems are read-only sources by
      default unless a later approved narrow integration/procedure exists.
    - `CHK-OWNER-APPROVAL`: approval-required effects are blocked before effect
      unless explicit scoped owner approval exists.
    - `CHK-HOW-FIREWALL`: W19 choices remain unselected.

    ## A-row matrix

    ### A1 — role separation / anti-monolith

    W20 row: manager role is separate from source registry, process contracts,
    owner-context structure, and state artifacts; no monolithic prompt closes the
    node.

    Coverage:

    - Artifacts: `ART-MANAGER-ROLE-CARD`, `ART-SOURCE-REGISTRY-ENTRY`,
      `ART-PROCESS-CONTRACT`, `ART-OWNER-CONTEXT-CARD`.
    - Check: `CHK-A-COVERAGE`.

    Verifier rejection condition: reject if the pack claims a single prompt,
    persona, chat transcript, or unstructured instruction blob satisfies the manager
    contract without separate visible role, source, process, owner-context, and state
    surfaces.

    W19 guard: this requires separation of concerns only. It does not select file
    layout, storage, schema, runtime, UI, engine, or database.

    ### A2 — authority basis on route/state/commitment changes

    W20 row: every manager output that changes route, state, or commitment carries
    an authority basis, process/source context basis, effect tier, and
    workspace/write boundary.

    Coverage:

    - Artifacts: `ART-MANAGER-ROLE-CARD`, `ART-PROCESS-CONTRACT`.
    - Procedure: `PROC-CONTEXT-LOAD`.
    - Examples: `EX-CAPTURE-NONCOMMITMENT`, `EX-PLAN-PROPOSAL`,
      `EX-ET2-APPROVAL`, `EX-OS-READ-ONLY`.
    - Checks: `CHK-OWNER-APPROVAL`, `CHK-WRITE-BOUNDARY`.

    Verifier rejection condition: reject if a route, state request, or commitment
    change lacks any of: authority basis, process/source context basis, effect tier,
    or workspace/write boundary.

    W19 guard: effect-tier visibility does not select scoring thresholds, runtime
    implementation, scheduler, storage engine, API, or exact schema.

    ### A3 — topic-open rule

    W20 row: no generic domain/topic blacklist; the manager may work on any
    owner-requested topic through the right process and source context.

    Coverage:

    - Artifacts: `ART-PROCESS-CONTRACT`, `ART-SOURCE-REGISTRY-ENTRY`.
    - Procedure: `PROC-CONTEXT-LOAD`.
    - Example: `EX-TOPIC-OPEN-SOURCE-OWNED`.
    - Check: `CHK-TOPIC-OPEN`.

    Verifier rejection condition: reject if the pack contains a broad topic/domain
    exclusion list or refuses an owner-requested topic merely because of subject
    area. It may still block a missing source, missing process, missing approval, or
    unsafe side effect before effect.

    W19 guard: this is an authority rule, not a domain process library and not an
    external truth-source claim.

    ### A4 — source/context item visibility

    W20 row: every source/context item has source id/path/link, owner/scope,
    read/write status, freshness/trust marker, and allowed use.

    Coverage:

    - Artifact: `ART-SOURCE-REGISTRY-ENTRY`.
    - Procedure: `PROC-CONTEXT-LOAD`.
    - Examples: `EX-OS-READ-ONLY`, `EX-TOPIC-OPEN-SOURCE-OWNED`.
    - Check: `CHK-WRITE-BOUNDARY`.

    Verifier rejection condition: reject if a source/context item can be used
    without visible source identity, scope, read/write status, freshness/trust, or
    allowed-use boundary.

    W19 guard: field names, storage format, database, exact file layout, and exact
    schema remain unchosen. The contract is only that these properties are visible in
    Markdown-readable evidence.

    ### A5 — loaded bundle / missing context / insufficient-context route

    W20 row: every nontrivial operation declares the loaded source/context bundle,
    missing context, and route if context is insufficient.

    Coverage:

    - Procedure: `PROC-CONTEXT-LOAD`.
    - Artifacts: `ART-SOURCE-REGISTRY-ENTRY`, `ART-PROCESS-CONTRACT`.
    - Examples: `EX-TOPIC-OPEN-SOURCE-OWNED`,
      `EX-UNSOURCED-OR-UNAPPROVED-BLOCK`.
    - Check: `CHK-A-COVERAGE`.

    Verifier rejection condition: reject if a nontrivial output acts as if context is
    loaded while the loaded bundle, missing context, or insufficiency route is absent
    or implicit.

    W19 guard: the route names an operating outcome, not a scheduler, automation,
    external integration procedure, or storage/replay mechanism.

    ### A6 — owner-context structure

    W20 row: owner-context structure represents durable owner facts, preferences,
    decisions, approvals, evidence, unknowns, context summaries, and state-change
    requests inside the Zaratusta workspace.

    Coverage:

    - Artifact: `ART-OWNER-CONTEXT-CARD`.
    - Examples: `EX-CAPTURE-NONCOMMITMENT`, `EX-PLAN-PROPOSAL`,
      `EX-ET2-APPROVAL`.
    - Checks: `CHK-WRITE-BOUNDARY`, `CHK-OWNER-APPROVAL`.

    Verifier rejection condition: reject if owner-context evidence is an
    unstructured chat-memory claim or omits durable representation for owner facts,
    preferences, decisions, approvals, evidence, unknowns, summaries, or
    state-change requests.

    W19 guard: this does not select durable-state writer, replay, ledger, DB,
    storage backend, exact schema, exact file layout, or chat-memory implementation.

    ### A7 — process registry contract

    W20 row: process registry entries are inspectable contracts with purpose,
    inputs, outputs, authority/effect tier, required source context, owner approval
    gates, and examples/tests.

    Coverage:

    - Artifact: `ART-PROCESS-CONTRACT`.
    - Examples: `EX-ET2-APPROVAL`, `EX-TOPIC-OPEN-SOURCE-OWNED`,
      `EX-UNSOURCED-OR-UNAPPROVED-BLOCK`.
    - Checks: `CHK-OWNER-APPROVAL`, `CHK-TOPIC-OPEN`.

    Verifier rejection condition: reject if a process is only a prompt, habit, or
    hidden instruction and lacks inspectable purpose, inputs, outputs, authority,
    effect tier, required source context, approval gates, or tests/examples.

    W19 guard: this does not choose exact research procedure mechanics, process file
    layout, process schema, engine, vendor, UI, scheduler, or automation.

    ### A8 — no matching process route / process mutation gate

    W20 row: no matching process routes to process draft/research/review; process
    creation or mutation is a proposal or ET2 action with owner approval; hidden
    self-rewrite is invalid.

    Coverage:

    - Artifact: `ART-PROCESS-CONTRACT`.
    - Procedure: `PROC-CONTEXT-LOAD`.
    - Examples: `EX-UNSOURCED-OR-UNAPPROVED-BLOCK`, `EX-ET2-APPROVAL`.
    - Checks: `CHK-OWNER-APPROVAL`, `CHK-HOW-FIREWALL`.

    Verifier rejection condition: reject if the manager silently creates, edits, or
    uses a process without representing creation/mutation as draft, research, review,
    proposal, or owner-approved ET2 action.

    W19 guard: deep research is a route, not an exact research procedure, vendor,
    API, automation, or scheduler selection.

    ### A9 — read-only external sources / Zaratusta write boundary

    W20 row: Direction OS and other repos/directions/projects are read-only sources
    by default; Zaratusta writes only to its own workspace/repo unless an explicit
    narrow integration/procedure is approved.

    Coverage:

    - Artifacts: `ART-SOURCE-REGISTRY-ENTRY`, `ART-OWNER-CONTEXT-CARD`.
    - Examples: `EX-OS-READ-ONLY`, `EX-ET2-APPROVAL`.
    - Check: `CHK-WRITE-BOUNDARY`.

    Verifier rejection condition: reject if the pack gives Zaratusta a default write
    path into Direction OS or any other repo/direction/project, or if it weakens the
    default write boundary to "write wherever useful."

    W19 guard: future non-Zaratusta integrations are not selected here. They remain
    unavailable unless a later explicit narrow integration/procedure is approved.

    ### A10 — explicit scoped owner approval before high-effect actions

    W20 row: external, irreversible, spend, deletion, message/send, or material
    cross-system effects require explicit scoped owner approval before effect.

    Coverage:

    - Artifacts: `ART-MANAGER-ROLE-CARD`, `ART-PROCESS-CONTRACT`,
      `ART-OWNER-CONTEXT-CARD`.
    - Examples: `EX-ET2-APPROVAL`, `EX-UNSOURCED-OR-UNAPPROVED-BLOCK`.
    - Check: `CHK-OWNER-APPROVAL`.

    Verifier rejection condition: reject if approval is inferred from silence,
    historical preference, assistant confidence, or generic permission rather than
    explicit current scoped owner approval before the effect.

    W19 guard: this does not select spend controls, automation, scheduler, API,
    vendor, or external integration mechanics.

    ### A11 — commitment semantics for intake/planning/logging

    W20 row: intake/planning/logging preserve commitment semantics: captures are not
    commitments; plans distinguish proposal from accepted commitment and name
    displacement; log responses are bounded to loaded context.

    Coverage:

    - Artifacts: `ART-MANAGER-ROLE-CARD`, `ART-OWNER-CONTEXT-CARD`.
    - Procedure: `PROC-CONTEXT-LOAD`.
    - Examples: `EX-CAPTURE-NONCOMMITMENT`, `EX-PLAN-PROPOSAL`.
    - Check: `CHK-A-COVERAGE`.

    Verifier rejection condition: reject if a capture/backlog item is treated as an
    accepted commitment, a proposal becomes commitment without acceptance, a plan
    change omits displacement, or a log response uses context that was not loaded.

    W19 guard: this does not select horizon durations, cadence, month/12-week model,
    scoring, thresholds, UI, scheduler, or automation.

    ### A12 — high-stakes/source-owned routing without topic refusal

    W20 row: high-stakes/source-owned requests are routed by process/source/context;
    examples/tests must show answer, summarize, draft, track, or route behavior
    without topic refusal, while unsourced source-owned instructions and unapproved
    side effects are blocked before effect.

    Coverage:

    - Artifacts: `ART-SOURCE-REGISTRY-ENTRY`, `ART-PROCESS-CONTRACT`.
    - Procedure: `PROC-CONTEXT-LOAD`.
    - Examples: `EX-TOPIC-OPEN-SOURCE-OWNED`,
      `EX-UNSOURCED-OR-UNAPPROVED-BLOCK`.
    - Checks: `CHK-TOPIC-OPEN`, `CHK-OWNER-APPROVAL`.

    Verifier rejection condition: reject if a request is refused merely by topic, or
    if the pack lets the manager invent source-owned instructions or perform an
    unapproved side effect.

    W19 guard: source/process/context handling does not create a topic blacklist,
    runtime agent, external integration, API, or automation.

    ### A13 — first-layer Markdown/GitHub readability and HOW firewall

    W20 row: first implementation layer is GitHub/Markdown-readable source registry,
    process registry, owner-context structure, context-loading procedure, and
    examples/tests; exact UI/storage/vendor/schema/cadence/scoring/scheduler/
    automation/API choices remain unchosen at this layer.

    Coverage:

    - Artifacts: `ART-SOURCE-REGISTRY-ENTRY`, `ART-PROCESS-CONTRACT`,
      `ART-OWNER-CONTEXT-CARD`.
    - Procedure: `PROC-CONTEXT-LOAD`.
    - Examples: all examples listed above.
    - Check: `CHK-HOW-FIREWALL`.

    Verifier rejection condition: reject if the pack requires a DB, API, UI,
    runtime/chat agent, vendor, scheduler, automation, storage engine, exact schema,
    exact source/process/owner-context file layout, exact cadence, or scoring policy
    to satisfy A1-A12.

    W19 guard: A13 is the HOW firewall. It fixes only Markdown/GitHub readability for
    the first layer.

    ## W19 PLAN agenda explicitly not chosen

    The following W19 items are not selected as WHAT and are not implementation
    contracts in this matrix:

    - exact UI/channel/surface: NOT CHOSEN.
    - exact storage/schema/file layout/database: NOT CHOSEN.
    - exact engine/vendor/framework/API/subscription adapter: NOT CHOSEN.
    - exact horizon durations/cadence/month/12-week model: NOT CHOSEN.
    - exact non-caving weighing/scoring policy and thresholds: NOT CHOSEN.
    - exact implementation of state writer and replay: NOT CHOSEN.
    - exact research procedure mechanics: NOT CHOSEN.
    - exact automation/scheduler/spend controls: NOT CHOSEN.
    - exact external integration procedure for future non-Zaratusta writes: NOT CHOSEN.
    - exact source registry/process registry/owner-context file layout: NOT CHOSEN.

    ## Independent verifier procedure

    A verifier can reject the product evidence mechanically:

    1. Coverage: every A1-A13 row above must have at least one artifact, example,
       procedure, or check handle, plus a rejection condition.
    2. Topic-open: no evidence may add a topic/domain exclusion list or refuse owner
       requests merely by subject area.
    3. Write-boundary: no evidence may give Zaratusta default write access outside
       the Zaratusta workspace/repo.
    4. Owner-approval: no evidence may allow external, irreversible, spend, deletion,
       message/send, or material cross-system effect before explicit scoped owner
       approval.
    5. HOW firewall: no evidence may require or select DB/API/UI/vendor/scheduler/
       automation/storage engine/exact schema/exact layout/cadence/scoring as the
       contract.
    6. Missing coverage: any row without visible artifact/example/procedure/check
       coverage is a hard fail.
    7. Hidden HOW: any row whose coverage only works by assuming a runtime, storage
       backend, exact schema/layout, engine, API, UI, scheduler, automation, or
       vendor is a hard fail.
  boundaries: |
    Do not modify the Direction OS repo or any non-Zaratusta repo.

    Product-repo writes, cleanup, branch handling, commits, or PR creation must
    be performed only by writer core. Do not use direct GitHub write actions from
    a normal session.

    Preserve W20/A1-A13.
    Keep W19 as PLAN agenda, not WHAT.
    Do not introduce a generic topic/domain blacklist.
    Do not implement runtime/chat agent, state writer/replay/ledger/DB/storage
    backend, UI/channel/surface, engine/vendor/framework/API adapter, scheduler,
    automation, spend controls, or external integration procedure.
    Do not choose exact file layout or exact schema as future contract.
    Do not copy LifeReset wholesale.
    Do not weaken the rule that Zaratusta writes only to its own workspace/repo
    by default and other repos/directions/projects are read-only sources by default.
  done_when: |
    - Product repo contains a Markdown-readable acceptance matrix for A1-A13.
    - Matrix names which artifact/example/check covers each A row.
    - W19 items are explicitly marked not chosen.
    - No generic topic/domain blacklist appears.
    - No DB/API/UI/vendor/scheduler/automation/storage engine/exact schema is
      selected as contract.
    - The matrix is sufficient for an independent verifier to reject hidden HOW
      or missing A-row coverage.
    - Product-repo commit or PR evidence is returned.
    - Check output is returned if any check was run.
    - Any accidental branch from the earlier interrupted attempt is inspected and
      either ignored as harmless, removed, or adopted according to writer-core policy.
  return: |
    RESULT with product repo evidence, changed files/commit or PR reference,
    check output if any, and exact notes on any A-row or W19 risk found.
  budget: half focused day

END_OF_FILE: live/solmax/history/2026-06-28-s-zara-operate-contract-t1-acceptance-matrix-checkpoint-002.md
