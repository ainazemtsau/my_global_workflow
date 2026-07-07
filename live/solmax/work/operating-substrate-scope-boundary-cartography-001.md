# Operating-substrate architecture/spec cartography — scope & boundary cluster

status: owner_approved_working_graph
session: s-solmax-operating-substrate-architecture-cartography-001-owner-sign
call: c-solmax-operating-substrate-architecture-cartography-001
cluster_id: os-substrate-scope-boundary-001
anchor_question: |
  What is the operating substrate's scope and boundary: what belongs to the
  reusable substrate, and what stays consumer-specific in Zaratusta,
  HLCI/PHL-like systems, Direction-OS/workflow-like systems and future
  projects?

owner_sign:
  status: approved_as_working_graph
  owner_words: |
    Так, ну в принципе, с картой согласен. Просто не всё сейчас однозначно,
    там некоторые вопросы кажутся, может, где-то избыточными, но, возможно,
    при прояснении в них появится смысл, поэтому я, в принципе, с ней
    согласен, можем с ней дальше двигаться.
  interpretation: |
    The owner approves the map for forward movement, with an explicit caveat:
    some questions may be ambiguous or redundant now, but remain useful as
    candidate nodes until forge/cartography clarifies them.

non_freeze_note: |
  This artifact maps questions. It does not answer or freeze the substrate.
  Examples are anchors only. Current Zaratusta and Direction OS artifacts
  remain evidence/source material, not authority. Approval is for the working
  graph, not for treating every node as permanently necessary.

frame_cluster:
  name: "Operating substrate scope and boundary"
  why_cartography_is_needed: |
    The owner corrected Solmax into an umbrella direction and explicitly
    prohibited ChatGPT from autonomously designing the whole substrate.
    The Zaratusta live-use failure showed that surface/spec coverage can look
    complete while the live owner-facing process fails. Therefore the first
    substrate work must separate reusable scope/boundary questions from
    downstream design questions before any card is forged.
  owner_symptom_or_evidence: |
    Owner paused Zaratusta live-use repair and redirected to a reusable
    architecture route; owner clarified the route should follow the
    canon-cartography/canon-forge pattern: first question graph, dependencies,
    variants, research needs and proof anchors; then one owner-approved
    question/card at a time.

inventory:
  existing_decisions:
    - Solmax is an umbrella direction.
    - Zaratusta is the first product/application branch, first consumer,
      failure-case and evidence source.
    - Operating-substrate is a separate sibling architecture/spec route for
      AI-led stateful owner/project processes.
    - Substrate is not a Zaratusta product child.
    - Current Zaratusta and Direction OS artifacts are evidence/source
      material, not authority and not a ready specification.
    - Work mode is owner-led architecture/spec cartography before forge.
  partial_evidence:
    - Zaratusta Operating Manager v1 live trial failed as live personal
      manager behavior despite Markdown surface evidence.
    - Direction OS demonstrates one-session/one-job, CALL/RESULT, durable
      state, gates and review as possible source material.
    - Canon cartography/forge provides a procedural analogy for graph first,
      one owner-approved card later.
  rejected_alternatives:
    - Repair Zaratusta directly as the next move.
    - Put substrate under Zaratusta as a product child.
    - Copy current Zaratusta artifacts into substrate as authority.
    - Let ChatGPT generate the full substrate architecture autonomously.
    - Select/create a substrate repo now.
    - Create implementation code or a detailed test plan now.
  owner_corrections_preserved:
    - "Заратустра ставится в блок"
    - "мы переключаемся вот на этот режим"
    - "сначала ... надо вот архитектуру, где она применяется, как там с ней работать"
    - "да" to Solmax umbrella placement recommendation.
    - "Option A" to minimal umbrella placement repair.
    - "с картой согласен ... можем с ней дальше двигаться" to this working graph.
    - "некоторые вопросы кажутся ... избыточными ... при прояснении в них появится смысл" as caveat.
  known_non_authorities:
    - Current Zaratusta product repo artifacts.
    - Current Direction OS artifacts.
    - Canon-cartography/canon-forge game-development plays.
    - This cartography artifact as a substrate answer; it is a question map only.

graph_nodes:
  - id: q01_system_class
    plain_question: "Для какого класса систем/процессов вообще существует operating substrate?"
    why_it_matters: |
      Без класса систем любое следующее обсуждение либо станет "всё про AI",
      либо сожмётся обратно до Zaratusta. Это главный scope gate.
    answer_shape: taxonomy
    status: ready
    dependency_type: hard_prerequisite
    blocks:
      - "q02_boundary_rule: boundary rule depends on knowing the class whose invariants are being separated."
      - "q03_consumer_families: consumer variants are meaningless until the system class is named."
      - "q05_state_responsibilities/q06_procedure_responsibilities/q08_live_vs_internal: these can over-design if the substrate class is not bounded."
      - "q12_proof_anchor_policy: proof cases depend on which systems count."
    do_not_solve_here: |
      Do not define state schema, procedure list, call protocol, repo, test
      harness, storage, UI or implementation.
    needs_research: comparable_systems
    needs_anchor: source_artifact
    confusion_traps:
      - Treating "all AI agents" as in-scope.
      - Treating "Zaratusta only" as in-scope.
      - Letting examples become authority.
    forge_handoff:
      plain_question: "Для какого класса систем/процессов вообще существует operating substrate?"
      why_now: "This is the first hard prerequisite; every other node depends on the scope class."
      must_decide: "In-scope class, explicit near/out-of-scope edge cases, and which examples are only anchors."
      must_not_decide: "State model, procedure model, call protocol, proof harness, repo, implementation."
      parent_locks: "Solmax umbrella; substrate sibling route; Zaratusta/Direction OS artifacts are evidence not authority; owner-led card."
      expected_answer_shape: taxonomy
      first_owner_question: "Какие 2-3 examples точно должны count, and which tempting examples should not count?"
      return_to_graph_if: "Owner cannot classify Zaratusta/HLCI/Direction OS-like examples, or a downstream node needs a wider/narrower class."

  - id: q02_boundary_rule
    plain_question: "По какому правилу отличаем substrate invariant от consumer-specific policy/behavior?"
    why_it_matters: |
      Это предотвращает копирование Zaratusta/Direction OS как spec и
      предотвращает растворение reusable substrate в локальных product rules.
    answer_shape: invariant
    status: ready
    dependency_type: co_frame
    blocks:
      - "q04_source_authority_policy: evidence cannot be promoted safely without a boundary rule."
      - "q05-q11: every candidate substrate topic needs this rule to avoid freezing local consumer details."
      - "q14_repo_artifact_boundary: repo/spec placement depends on what is reusable vs local."
    do_not_solve_here: |
      Do not choose concrete invariant content for state/procedure/interface;
      only decide the boundary rule a future card will apply.
    needs_research: best_practice
    needs_anchor: diagram
    confusion_traps:
      - Calling every repeated pattern an invariant.
      - Calling every owner preference consumer-specific.
      - Using current OS mechanics as the boundary by default.
    forge_handoff:
      plain_question: "По какому правилу отличаем substrate invariant от consumer-specific policy/behavior?"
      why_now: "Scope without boundary rule will not stop downstream overreach."
      must_decide: "Boundary criteria and what evidence can justify moving a local pattern into substrate."
      must_not_decide: "Which exact state/procedure/interface mechanisms become invariants."
      parent_locks: "Current artifacts evidence not authority; no full architecture; no implementation."
      expected_answer_shape: invariant
      first_owner_question: "Что должно be reusable even when consumer changes, and what must remain local even if repeated?"
      return_to_graph_if: "The rule cannot classify at least Zaratusta, Direction OS and a future project example."

  - id: q03_consumer_families
    plain_question: "Какие consumer families должны быть represented as examples: Zaratusta, HLCI/PHL, Direction-OS-like, future projects?"
    why_it_matters: |
      The substrate must generalize across more than one consumer, but absent
      context can make phantom requirements. This node controls which examples
      are evidence sources for later cards.
    answer_shape: taxonomy
    status: needs_preface
    dependency_type: co_frame
    blocks:
      - "q12_proof_anchor_policy: proof scenarios require representative families."
      - "q04_source_authority_policy: each family needs source/authority status."
      - "q11_multi_agent_boundary: tool/model assumptions may differ by family."
    do_not_solve_here: |
      Do not import HLCI/PHL details without owner-provided context; do not
      define consumer specs.
    needs_research: comparable_systems
    needs_anchor: source_artifact
    confusion_traps:
      - Inventing HLCI/PHL details.
      - Treating future unknown projects as concrete requirements.
      - Using too many families before the boundary rule exists.
    forge_handoff:
      plain_question: "Какие consumer families должны быть represented as examples?"
      why_now: "Needed soon after q01/q02 to choose proof anchors and avoid Zaratusta-only bias."
      must_decide: "Representative families and their evidence status."
      must_not_decide: "Any consumer's actual product behavior or implementation."
      parent_locks: "Zaratusta first consumer/failure-case; other families only if owner provides context or labels them as hypothetical."
      expected_answer_shape: taxonomy
      first_owner_question: "Which examples are mandatory anchors for substrate, and which are just later candidates?"
      return_to_graph_if: "A family lacks enough context to be used without invention."

  - id: q04_source_authority_policy
    plain_question: "Когда existing artifacts are evidence, and when can any artifact become substrate authority?"
    why_it_matters: |
      This is the safety valve after the Zaratusta failure: surface artifacts
      can be useful but cannot prove substrate truth by themselves.
    answer_shape: evaluation_rubric
    status: ready
    dependency_type: owner_policy
    blocks:
      - "q05-q10: existing state/procedure/interface examples cannot be copied until their evidence status is clear."
      - "q12_proof_anchor_policy: proof anchors require source classes and authority rules."
    do_not_solve_here: |
      Do not accept any current artifact as substrate spec; define the
      evidence/authority rule only.
    needs_research: failure_cases
    needs_anchor: owner_transcript
    confusion_traps:
      - Mistaking a clean Markdown contract for live readiness.
      - Treating a working OS rule as universal because it works here.
      - Rejecting all existing artifacts instead of demoting them to evidence.
    forge_handoff:
      plain_question: "Когда existing artifacts are evidence, and when can any artifact become substrate authority?"
      why_now: "Without this, every later card risks copying current artifacts as hidden authority."
      must_decide: "Evidence classes, authority promotion criteria, and what owner sign is required."
      must_not_decide: "The content of any downstream substrate card."
      parent_locks: "Zaratusta failure evidence; current artifacts evidence not authority."
      expected_answer_shape: evaluation_rubric
      first_owner_question: "What proof would make an existing artifact eligible to influence substrate, without becoming authority by default?"
      return_to_graph_if: "The rule cannot explain why Zaratusta Markdown evidence was insufficient."

  - id: q05_state_responsibilities
    plain_question: "Какие state responsibilities are substrate-level, if any, and which state stays consumer-specific?"
    why_it_matters: |
      State is a known candidate topic, but state details are downstream of
      scope and boundary. Solving it early would freeze substrate design.
    answer_shape: state_model
    status: downstream
    dependency_type: downstream
    blocks:
      - "q08_live_vs_internal: internal audit/reporting boundary depends on which state responsibilities are reusable."
      - "q09_source_context_boundary: source/context can be state, input or evidence depending on state responsibilities."
      - "q12_proof_anchor_policy: proof must check actual state continuity only after responsibilities are clear."
    do_not_solve_here: |
      Do not choose storage, schema, file format, DB/API/runtime, or exact
      state surfaces.
    needs_research: best_practice
    needs_anchor: scenario
    confusion_traps:
      - Replaying Zaratusta operating-manager-v1 surfaces as substrate.
      - Confusing durable state with all context.
      - Choosing storage/HOW while asking WHAT.
    forge_handoff:
      plain_question: "Какие state responsibilities are substrate-level, if any?"
      why_now: "Only after q01/q02/q04; then state can be framed without copying a consumer."
      must_decide: "Responsibility boundaries, not storage or schema."
      must_not_decide: "Persistence tech, exact fields, Zaratusta workspace layout."
      parent_locks: "Scope/boundary card; source authority policy."
      expected_answer_shape: state_model
      first_owner_question: "What must never be forgotten across sessions for any in-scope process?"
      return_to_graph_if: "The answer depends on one consumer's local workspace."

  - id: q06_procedure_responsibilities
    plain_question: "Что counts as substrate procedure model, and what remains a consumer-specific play/process?"
    why_it_matters: |
      Procedure is central to AI-led stateful processes, but freezing a
      procedure taxonomy before scope/boundary would recreate a local OS.
    answer_shape: procedure_model
    status: downstream
    dependency_type: downstream
    blocks:
      - "q07_call_session_boundary: calls between procedures need procedure boundaries first."
      - "q10_owner_question_policy: owner questions attach to procedures only after procedure authority is clear."
      - "q13_incremental_coherence_rule: card sequencing depends on procedure granularity."
    do_not_solve_here: |
      Do not define the procedure list, lifecycle, play syntax or process
      mutation rules.
    needs_research: comparable_systems
    needs_anchor: diagram
    confusion_traps:
      - Treating Direction OS plays as universal substrate procedures.
      - Treating product workflows as substrate lifecycle.
      - Solving process mutation before procedure identity.
    forge_handoff:
      plain_question: "Что counts as substrate procedure model, and what remains consumer-specific?"
      why_now: "After scope/boundary, procedure identity controls calls, owner questions and evolution."
      must_decide: "Procedure abstraction and separation from local plays."
      must_not_decide: "Specific procedure catalogue, syntax, automation, scheduler."
      parent_locks: "Scope/boundary card; no Direction OS copying as authority."
      expected_answer_shape: procedure_model
      first_owner_question: "When a process step repeats across consumers, what makes it reusable substrate rather than local play?"
      return_to_graph_if: "The answer requires choosing concrete Zaratusta or Direction OS procedures."

  - id: q07_call_session_boundary
    plain_question: "Какие call/session rules are substrate-level, including one chat = one task, and which are Direction-OS-specific?"
    why_it_matters: |
      Bounded sessions are a known successful pattern, but they may be
      substrate invariant, local OS policy, or only a proof technique.
    answer_shape: call_protocol
    status: downstream
    dependency_type: downstream
    blocks:
      - "q11_multi_agent_boundary: multi-agent orchestration needs call/session semantics."
      - "q12_proof_anchor_policy: transcript/scenario proof depends on session boundaries."
    do_not_solve_here: |
      Do not define packet schemas, orchestration protocol, message format or
      scheduler.
    needs_research: best_practice
    needs_anchor: source_artifact
    confusion_traps:
      - Treating CALL/RESULT exactly as substrate.
      - Ignoring why bounded sessions prevent drift.
      - Mixing human chat lifecycle with agent executor lifecycle.
    forge_handoff:
      plain_question: "Какие call/session rules are substrate-level, and which are Direction-OS-specific?"
      why_now: "After procedure boundaries; calls are between procedures/sessions."
      must_decide: "Reusable call/session principles."
      must_not_decide: "Exact packet schema, transport, tool routing, automation."
      parent_locks: "Direction OS is source material, not authority."
      expected_answer_shape: call_protocol
      first_owner_question: "Is one chat = one task a substrate invariant, a Direction OS policy, or a default proof discipline?"
      return_to_graph_if: "The owner cannot separate workflow-OS convenience from substrate necessity."

  - id: q08_live_vs_internal
    plain_question: "Как отделяется live owner interface from internal state/audit/reporting layer?"
    why_it_matters: |
      The Zaratusta failure was partly live-use behavior collapsing into
      state/intake/handback bureaucracy. This boundary prevents internal
      machinery from replacing useful owner-leading behavior.
    answer_shape: interface_model
    status: downstream
    dependency_type: downstream
    blocks:
      - "q12_proof_anchor_policy: live behavior proof must observe both owner-facing flow and internal evidence."
      - "q10_owner_question_policy: owner questions appear at the live interface but may be driven by internal uncertainty."
    do_not_solve_here: |
      Do not design UI, prompts, message templates, handback format or audit
      schema.
    needs_research: failure_cases
    needs_anchor: owner_transcript
    confusion_traps:
      - Equating complete handback with helpful live operation.
      - Hiding internal state from audit.
      - Making the live interface a dump of internal machinery.
    forge_handoff:
      plain_question: "Как отделяется live owner interface from internal state/audit/reporting layer?"
      why_now: "After state/procedure responsibilities, before proof of live readiness."
      must_decide: "Interface/internal separation principle."
      must_not_decide: "Exact UI, prompt, report or audit format."
      parent_locks: "Zaratusta failure transcript; no detailed test plan now."
      expected_answer_shape: interface_model
      first_owner_question: "What should the owner experience directly, and what should remain internal evidence unless asked?"
      return_to_graph_if: "The answer tries to solve UI instead of the boundary."

  - id: q09_source_context_boundary
    plain_question: "Что является substrate-level source/context loading, and what is local consumer source policy?"
    why_it_matters: |
      Stateful owner/project processes need source loading, but sources vary
      by consumer, privacy boundary and current repo/workspace model.
    answer_shape: interface_model
    status: downstream
    dependency_type: downstream
    blocks:
      - "q04_source_authority_policy: source loading needs evidence/authority classification."
      - "q12_proof_anchor_policy: scenarios need known source/context inputs."
    do_not_solve_here: |
      Do not choose loaders, connectors, indexing, context-window strategy,
      embeddings, storage or exact source hierarchy.
    needs_research: best_practice
    needs_anchor: scenario
    confusion_traps:
      - Treating every source as equally authoritative.
      - Confusing context loading with memory/state.
      - Choosing tools before source policy.
    forge_handoff:
      plain_question: "Что является substrate-level source/context loading, and what is local consumer source policy?"
      why_now: "After source authority policy and scope/boundary."
      must_decide: "Reusable responsibilities for source/context handling."
      must_not_decide: "Connectors, indexes, exact loading algorithm, storage."
      parent_locks: "Artifacts evidence not authority; privacy/trust constraints."
      expected_answer_shape: interface_model
      first_owner_question: "Which source/context duties must every in-scope process perform regardless of consumer?"
      return_to_graph_if: "The answer requires a specific repo/tool implementation."

  - id: q10_owner_question_policy
    plain_question: "Какие owner questions/approvals are substrate-level gates, and which are local product decisions?"
    why_it_matters: |
      The owner decides. A reusable substrate needs explicit rules for when
      AI must ask, assume, recommend or stop, but the content of decisions
      differs by consumer.
    answer_shape: evaluation_rubric
    status: downstream
    dependency_type: owner_policy
    blocks:
      - "q13_incremental_coherence_rule: small-step development requires knowing which decisions need owner sign."
      - "q12_proof_anchor_policy: proof must include owner-gate behavior."
    do_not_solve_here: |
      Do not define all approval tiers, product permissions, medical/safety
      domains or exact G9 clone.
    needs_research: failure_cases
    needs_anchor: owner_transcript
    confusion_traps:
      - Letting AI silently freeze architecture.
      - Asking the owner too often because the substrate lacks default rules.
      - Copying Direction OS G9 as universal without review.
    forge_handoff:
      plain_question: "Какие owner questions/approvals are substrate-level gates?"
      why_now: "After scope/boundary; before architecture cards can safely freeze further decisions."
      must_decide: "Reusable owner-decision gate types."
      must_not_decide: "Every local effect tier or product-specific approval rule."
      parent_locks: "Owner-led process; AI never freezes substrate autonomously."
      expected_answer_shape: evaluation_rubric
      first_owner_question: "Which decisions must always come to you, even in future consumers?"
      return_to_graph_if: "The answer becomes a full governance system instead of gate categories."

  - id: q11_multi_agent_boundary
    plain_question: "Multi-agent operation with ChatGPT, Codex, Claude and others: substrate responsibility or adapter/consumer responsibility?"
    why_it_matters: |
      The owner builds through multiple agents, but tool specifics change.
      This node separates reusable coordination principles from provider/tool
      implementation.
    answer_shape: call_protocol
    status: downstream
    dependency_type: downstream
    blocks:
      - "q14_repo_artifact_boundary: execution surfaces and repos depend on orchestration boundary."
      - "q12_proof_anchor_policy: provider/model comparison needs stable scenario semantics."
    do_not_solve_here: |
      Do not choose models, APIs, routing, costs, CLI setup, orchestration
      engine, or provider evaluation plan.
    needs_research: tool_capability
    needs_anchor: prototype_trace
    confusion_traps:
      - Baking current ChatGPT/Codex/Claude capabilities into substrate.
      - Treating model evaluation as intuition rather than scenario evidence.
      - Mixing executor implementation with process architecture.
    forge_handoff:
      plain_question: "Multi-agent operation: substrate responsibility or adapter/consumer responsibility?"
      why_now: "After call/session semantics and proof anchor policy are clearer."
      must_decide: "Reusable orchestration boundary."
      must_not_decide: "Provider choice, exact routing, API, CLI, budget mechanism."
      parent_locks: "Build mode uses background AI agents; cost discipline; no implementation now."
      expected_answer_shape: call_protocol
      first_owner_question: "What must stay true if ChatGPT, Codex or Claude are swapped?"
      return_to_graph_if: "The answer depends on today's tool feature rather than stable process need."

  - id: q12_proof_anchor_policy
    plain_question: "Какие proof anchors are required before saying a substrate card works?"
    why_it_matters: |
      The prior failure showed surface coverage is insufficient. Future cards
      need proof anchors without turning this session into a detailed test plan.
    answer_shape: proof
    status: research_first
    dependency_type: proof_downstream
    blocks:
      - "implementation_readiness: no implementation bet should start without proof policy."
      - "q05/q08/q11 verification: state/live/multi-agent claims need different anchors."
    do_not_solve_here: |
      Do not create a test plan, harness, dataset, benchmark or repo. Do not
      choose provider evaluation mechanics.
    needs_research: evaluation_methods
    needs_anchor: owner_transcript
    confusion_traps:
      - Treating transcript tests as the whole proof model.
      - Treating Markdown completeness as proof.
      - Designing a harness before scope/boundary.
    forge_handoff:
      plain_question: "Какие proof anchors are required before saying a substrate card works?"
      why_now: "After q01/q02/q04; before any implementation readiness claim."
      must_decide: "Proof anchor categories and what claims they can support."
      must_not_decide: "Detailed test plan, tooling, repo, datasets, provider benchmark."
      parent_locks: "Scenario/transcript/proof model from the start; no detailed test plan now."
      expected_answer_shape: proof
      first_owner_question: "What evidence would have caught the Zaratusta live-use failure before calling it ready?"
      return_to_graph_if: "The proof need reveals missing state/interface/source boundary questions."

  - id: q13_incremental_coherence_rule
    plain_question: "Как substrate развивается small-step without losing architectural coherence?"
    why_it_matters: |
      The owner wants small steps, but the route must not become scattered
      cards with no architecture spine or another perpetual draft.
    answer_shape: procedure_model
    status: needs_preface
    dependency_type: co_frame
    blocks:
      - "architecture-card sequencing: future forge order depends on coherence rule."
      - "gap/rebalance behavior: hidden prerequisites need a return path."
    do_not_solve_here: |
      Do not design the full development methodology, active bet, task plan
      or implementation sequence.
    needs_research: failure_cases
    needs_anchor: source_artifact
    confusion_traps:
      - Over-planning the whole substrate before any card.
      - Forging disconnected cards with no dependency graph.
      - Treating gap events as failure instead of normal cartography feedback.
    forge_handoff:
      plain_question: "Как substrate развивается small-step without losing architectural coherence?"
      why_now: "Needed as a route rule after first card, but not before scope/boundary."
      must_decide: "Card sequencing/rebalance principle."
      must_not_decide: "Implementation roadmap, detailed test plan, repo structure."
      parent_locks: "One question/card at a time; gap events return to cartography."
      expected_answer_shape: procedure_model
      first_owner_question: "What would make you feel the cards are coherent rather than random local decisions?"
      return_to_graph_if: "The rule requires answers to state/procedure/proof nodes first."

  - id: q14_repo_artifact_boundary
    plain_question: "Где живут substrate specs/cards/artifacts now, and when would repo/product boundaries become a question?"
    why_it_matters: |
      The current route has no substrate repo selected. Premature repo
      selection would look like progress while freezing implementation
      surfaces too early.
    answer_shape: repo_boundary
    status: downstream
    dependency_type: implementation_downstream
    blocks:
      - "implementation_bet_activation: no repo/product bet should start until scope/proof/artifact boundary is understood."
    do_not_solve_here: |
      Do not select or create a repo, file hierarchy, package, runtime,
      schema or product boundary.
    needs_research: none
    needs_anchor: source_artifact
    confusion_traps:
      - Treating a repo as the architecture.
      - Putting substrate back under Zaratusta for convenience.
      - Letting work artifacts become accepted spec without owner sign.
    forge_handoff:
      plain_question: "Где живут substrate specs/cards/artifacts now, and when would repo/product boundaries become a question?"
      why_now: "Only after several cards or when implementation pressure appears."
      must_decide: "Artifact/repo decision trigger."
      must_not_decide: "Actual repo selection or structure."
      parent_locks: "Operating-substrate repo none selected; architecture lives in Direction OS state until later owner-approved route."
      expected_answer_shape: repo_boundary
      first_owner_question: "What evidence would make a separate substrate repo worth choosing later?"
      return_to_graph_if: "The question appears before scope/proof cards exist."

dependency_edges:
  - from: q01_system_class
    to: q02_boundary_rule
    why_blocks: |
      A boundary rule needs a named class of systems; otherwise it cannot
      tell universal substrate from local consumer policy.
  - from: q01_system_class
    to: q03_consumer_families
    why_blocks: |
      Consumer families are only meaningful as examples of a system class,
      not as a shopping list of all possible projects.
  - from: q02_boundary_rule
    to: q04_source_authority_policy
    why_blocks: |
      Evidence cannot become authority unless there is a rule for when local
      repeated patterns count as reusable.
  - from: q04_source_authority_policy
    to: q05_state_responsibilities
    why_blocks: |
      Current Zaratusta/Direction OS state surfaces are tempting source
      material; authority policy prevents copying them as substrate.
  - from: q04_source_authority_policy
    to: q06_procedure_responsibilities
    why_blocks: |
      Direction OS plays are working examples but not automatically substrate
      procedures.
  - from: q05_state_responsibilities
    to: q08_live_vs_internal
    why_blocks: |
      Interface/internal separation depends on what state continuity and
      audit responsibilities are reusable.
  - from: q06_procedure_responsibilities
    to: q07_call_session_boundary
    why_blocks: |
      Calls are between procedures/sessions; procedure identity must exist
      before call/session rules can be classified.
  - from: q07_call_session_boundary
    to: q11_multi_agent_boundary
    why_blocks: |
      Multi-agent orchestration depends on what a session/call/handoff means.
  - from: q03_consumer_families
    to: q12_proof_anchor_policy
    why_blocks: |
      Proof anchors need representative consumer examples; otherwise proof
      will overfit Zaratusta or become abstract.
  - from: q12_proof_anchor_policy
    to: q14_repo_artifact_boundary
    why_blocks: |
      Repo/product implementation should not be selected until there is a
      proof policy for substrate claims.
  - from: q13_incremental_coherence_rule
    to: "future_forge_order"
    why_blocks: |
      Without a rebalance rule, cards can drift into disconnected local
      answers or a new perpetual architecture draft.

recommended_route:
  recommended_next: |
    Run one architecture-forge session for a single card:
    "Operating-substrate scope/boundary card".
    It should co-frame q01_system_class and q02_boundary_rule because scope
    without boundary cannot guide downstream nodes, and boundary without scope
    has no domain. It must not answer q03-q14.
  alternatives:
    - option: "Start with q12_proof_anchor_policy"
      rejected_because: |
        Proof anchors need scope and representative consumer families first;
        starting here risks designing a test plan for the wrong object.
    - option: "Start with q05_state_responsibilities"
      rejected_because: |
        State is tempting and concrete, but it would likely copy Zaratusta or
        Direction OS surfaces before the source/authority boundary is clear.
    - option: "Return to Zaratusta product repair"
      rejected_because: |
        This violates the approved route: Zaratusta is paused and remains
        evidence/failure-case, not the substrate child task.

gap_rebalance_rule: |
  If a later architecture-forge session finds a hidden prerequisite, unclear
  plain question, wrong answer shape, missing research/proof need, or the
  owner says the session is going the wrong way, it must checkpoint a
  gap_event and return to local/architecture-cartography instead of inventing
  architecture. Rebalance the graph if:
  - a forge card changes the meaning/order of 3 or more downstream nodes;
  - a new consumer family becomes mandatory evidence;
  - a node marked downstream becomes a hard prerequisite;
  - proof needs show that the current scope/boundary cannot be validated;
  - the owner rejects the map or says it is framing the wrong system;
  - a node preserved as candidate proves redundant or meaningfully merges
    with another node.

END_OF_FILE: live/solmax/work/operating-substrate-scope-boundary-cartography-001.md
