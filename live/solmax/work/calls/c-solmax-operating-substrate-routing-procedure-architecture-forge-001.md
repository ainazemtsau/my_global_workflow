CALL c-solmax-operating-substrate-routing-procedure-architecture-forge-001
to: session
direction: solmax
play: local/architecture-forge
node: g-operating-substrate

goal: |
  One owner-approved Q7 architecture card defines the Minimal Stable
  Bootstrap routing/procedure boundary: the minimum stable semantics needed
  to create and operate concrete process packs now, including preserved
  procedure definitions, local intake routing, bounded invocation,
  ownership, uncertainty/no-route handling, result, continuation and
  writer/apply behavior, without selecting a universal procedure
  catalogue, schema, provider-routing system, orchestration framework,
  runtime or implementation.

context: |
  Read:
  - live/solmax/CHARTER.md
  - live/solmax/TREE.md
  - live/solmax/NOW.md
  - live/solmax/plays/architecture-forge.md
  - live/solmax/work/operating-substrate-universal-structure-cartography-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-core-invariant-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-relationship-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-process-pack-instantiation-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-shared-owner-context-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-persistence-history-001.md
  - live/solmax/work/operating-substrate-routing-procedure-minimal-bootstrap-steering-001.md
  - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md

  Q7 plain question:
  "Как process routes intake to procedures, and what is reusable
  procedure structure vs local play/process?"

  Owner steering:

  - "как бы я хочу это побыстрее стартануть"
  - "не жертвуя качеством"
  - "для процесса вообще не нужно знать, что это"
  - "Сейчас только вот Codex"
  - "Скорее всего только Codex и ChatGPT"
  - "я бы не хотел, чтобы мы как бы завязывались"
  - "саму структуру процесса сделать так, чтобы он был готов, чтобы на его
    основе создавались процессы"
  - "writer процедуры, они в любом случае будут ... отдельно записываться,
    и они должны будут сохраняться"
  - route confirmation: "A"

  Interpretation of the owner steering:

  - Q7 must optimize for the smallest stable substrate that enables
    creation of the first several real processes.
  - Provider neutrality means replaceable execution adapters, not a
    current multi-provider orchestration requirement.
  - Current practical realization is expected to use:
    - ChatGPT Project for read-only owner-facing reasoning, routing,
      proposals, results and continuation;
    - Codex for local executor and writer procedures.
  - Claude Code or another executor is optional later.
  - ChatGPT, Codex and future models/tools do not define process meaning.
  - Writer remains a logical validated apply boundary.
  - Each concrete process pack may preserve its own writer procedure or
    writer policy defining write scope, preconditions, authority,
    validation, result, evidence and conflict behavior.
  - The physical writer does not have to remain a separate agent or chat
    forever.
  - After Q7, the route should test implementation readiness and defer
    non-blocking architecture rather than automatically completing every
    downstream card first.

  Accepted parent locks:

  - Q1-Q6 remain unchanged.
  - Operating-substrate is a stable model- and carrier-neutral kernel with
    pluggable process packs.
  - Concrete processes are created through process packs rather than kernel
    modification.
  - Service zones are semantic responsibility families, not physical
    components.
  - Atomic claims have one primary normative owner.
  - Concrete procedure catalogues and routing policy are process-pack
    concerns.
  - Invoke, delegate and handoff have different ownership effects.
  - Every open obligation has one current next-action owner.
  - Delegation retains parent integration and accountability.
  - Capability does not imply authority.
  - Query, event, evidence, propose, validate, authorize, apply, result and
    continue remain distinct.
  - Accepted state, history, source, evidence, memory and continuation
    remain distinct.
  - Durable mutation crosses a validated writer/apply boundary.
  - Procedure changes do not silently reinterpret active work.
  - No final service-block list, schema, provider, carrier, runtime,
    topology or implementation is accepted.

  Minimum Q7 pressure:

  1. A procedure is a separately preserved first-class process definition,
     not an informal prompt suggestion.

  2. The process pack owns its actual procedures, applicability and local
     routing rules.

  3. Intake routes to one bounded procedure, bounded clarification,
     explicit no-applicable-procedure treatment or another named legitimate
     next route.

  4. An invocation establishes semantically:
     - bounded objective;
     - selected procedure meaning;
     - required context and accepted-state/source basis;
     - current ownership;
     - available authority and allowed effects;
     - success, stop and failure meaning;
     - required result and continuation.

  5. Procedure selection is not acceptance, execution, ownership transfer,
     human authorization or durable mutation.

  6. Missing input, ambiguity, no applicable procedure and unavailable
     mandatory capability remain explicit; no silent nearest-match or
     fallback.

  7. Delegated child work returns to the parent integration owner.

  8. Result closes or checkpoints the bounded obligation.

  9. Portable continuation enables another ChatGPT or Codex run to continue
     without reconstructing the full transcript.

  10. Durable changes use the writer/apply boundary.

  11. Procedure-definition changes give active work an explicit compatible
      resume, revalidation/migration, pin/drain, handoff/replacement,
      block/rejection or named-unresolved disposition, expressed
      proportionally rather than as visible owner bureaucracy.

  The architecture-forge must offer two or three viable variants inside the
  Minimal Stable Bootstrap direction. It must not reopen the discarded
  provider/framework-heavy route as the recommendation.

boundaries: |
  Do not revise or reopen Q1-Q6.
  Do not treat this CALL as owner approval of the Q7 card.
  Do not copy Direction OS play names, CALL/RESULT fields or repository
  layout as universal substrate architecture.
  Do not copy Zaratusta procedures or interaction rhythm.
  Do not define a universal procedure catalogue.
  Do not define exact procedure, routing, invocation, result, continuation
  or writer schemas.
  Do not define fields, identifiers, version syntax or exact lifecycle
  enums.
  Do not select Agents SDK or another agent framework.
  Do not design multi-provider orchestration.
  Do not design automatic model selection or strong-model routing.
  Do not choose a classifier, planner, rules engine, policy engine, graph
  engine, scheduler, task queue or orchestration algorithm.
  Do not select deterministic, model-directed, policy or hybrid routing as
  the one universal implementation.
  Do not hardcode ChatGPT or Codex into kernel or process-pack semantics.
  Do not draft the actual ChatGPT Project instruction or Codex adapter
  instruction in this card.
  Do not define actual Health, game, Zaratusta or Direction OS procedures.
  Do not select repository layout, carrier, application, runtime, transport,
  provider, model, topology or deployment.
  Do not turn semantic concerns into a final reusable-service or physical
  service-block list.
  Do not implement.
  Do not change Direction OS.
  Keep Q8-Q14 downstream except for identifying which may be required by the
  subsequent implementation-readiness checkpoint.

done_when: |
  One atomic Q7 architecture card is explicitly owner-approved and:

  1. preserves Q1-Q6 unchanged;

  2. defines a minimal stable reusable routing/procedure contract sufficient
     to create the first several process packs without choosing provider or
     orchestration architecture;

  3. defines procedure as a separately preserved first-class process
     definition while leaving actual catalogues and domain routing inside
     process packs;

  4. distinguishes procedure selection, invocation, accepted obligation,
     execution, result and continuation without freezing exact entities or
     schemas;

  5. states the semantic minimum each invocation establishes: objective,
     procedure meaning, applicability, context, accepted-state/source
     basis, ownership, authority/effects, success/stop/failure, result and
     continuation;

  6. defines proportional behavior for ambiguity, missing input, no
     applicable procedure, conflicting route, unavailable mandatory
     capability and explicit process gap;

  7. preserves invoke/delegate/handoff ownership distinctions and retained
     parent integration;

  8. defines writer as a logical validated apply boundary and explains how
     a process-pack-local writer procedure/policy may be durably preserved
     without freezing Codex or a separate writer agent as architecture;

  9. defines enough procedure identity and active-work compatibility to
     prevent silent procedure mutation, while leaving version syntax and
     migration representation open;

  10. preserves a simple current bootstrap mapping in which ChatGPT Project
      may be read-only and Codex may execute writes, without making either
      semantic authority;

  11. includes an anti-bureaucracy rule: the owner receives useful result,
      bounded decision, clear block or continuation rather than internal
      routing and lifecycle machinery;

  12. passes one Health-like safety/evidence pressure and one
      game/productive-play exploratory pressure;

  13. records rejected alternatives including provider/framework-first
      architecture, prompt-as-procedure, classifier-as-architecture,
      silent fallback, ownerless routing and one universal writer agent;

  14. records the owner's selected architecture direction and final
      approval words from the forge session;

  15. records evidence limits, child/downstream questions, hidden
      prerequisites, graph verdict and gap_event;

  16. routes next to an implementation-readiness checkpoint that classifies
      remaining Q8-Q14 concerns by whether they block the first process
      creator;

  17. selects no procedure catalogue, syntax, schema, router algorithm,
      provider, carrier, topology, implementation, consumer template or
      final service-block list.

return: |
  RESULT with the owner-approved Q7 architecture card, owner direction
  choice and approval words, accepted minimal bootstrap semantics,
  process-pack and writer boundary, uncertainty/no-route behavior,
  active-work compatibility, rejected alternatives, Health/game pressures,
  evidence limits, child/downstream questions, graph/gap verdict, exact
  state_changes and a ready implementation-readiness continuation CALL.

budget: one focused session
parent: s-solmax-operating-substrate-routing-procedure-direction-repair-001
surface: chatgpt

END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-routing-procedure-architecture-forge-001.md
