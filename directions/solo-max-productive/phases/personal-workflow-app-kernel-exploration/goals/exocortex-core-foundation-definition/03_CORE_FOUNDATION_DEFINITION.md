# 03 Core Foundation Definition - EXOCORTEX

```yaml
artifact_control:
  artifact_name: "03 Core Foundation Definition - EXOCORTEX"
  schema: core_foundation_definition.v1
  owner_layer: goal_output
  status: ready_for_review
  source_file: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/exocortex-core-foundation-definition/03_CORE_FOUNDATION_DEFINITION.md"
  direction_id: solo-max-productive
  phase_id: personal-workflow-app-kernel-exploration
  goal_id: exocortex-core-foundation-definition
  created_by_stage: C2_CODEX_EXECUTE
  created_at: "2026-05-20"
```

## Definition

EXOCORTEX Core Foundation is the expandable product-level substrate for a persistent personal AI brain / external-brain application.

The core is not a chat wrapper, a fixed assistant persona, a fixed dashboard set, a workflow taxonomy, or a specific model provider. It is the durable layer that lets a user preserve context, reason with a replaceable cognitive engine, act through tools, compose working surfaces, learn from outcomes, and maintain Reality Alignment across changing domains and working styles.

The durable product value lives in:

- persistent memory and context;
- relevant-context selection;
- model-agnostic cognition;
- tool/action extensibility;
- extensible workspace surfaces;
- interaction and process loops;
- expected-outcome vs real-outcome learning;
- Reality Alignment and anti-sycophancy;
- permission, review, and correction controls.

The core must let future models become stronger engines inside the same user substrate. A better model should amplify accumulated memory, tools, workflows, surfaces, skills, reviews, and decision history rather than replace the product.

## Core principles

1. Persistent substrate over single-session assistance.
   EXOCORTEX must maintain continuity across sessions, projects, decisions, tools, and surfaces. The core remembers durable user-world facts, goals, commitments, preferences, decisions, outcomes, and useful procedures without treating raw chat history as the product.

2. Model-agnostic cognitive engine.
   The model reasons, writes, analyzes, and calls tools, but it is replaceable. The core must not depend on one model, provider, context window, prompt style, or assistant role as its durable identity.

3. Relevant context, not maximal context.
   The core must compile the smallest useful context for the current situation. It must not dump the whole user world into the prompt just because a model can accept a large context window.

4. Tools and actions as extensible body.
   Tools, APIs, files, calendars, messages, automations, code execution, and external systems are body parts the brain can use under permission controls. The core defines the extensibility and safety model, not a fixed list of integrations.

5. Surfaces as extensible environments.
   Chat is an entry point, not the whole product. Rooms, dashboards, boards, documents, canvases, inspectors, and widgets are environment forms the system can compose and maintain. No one screen is the core.

6. Interaction and process loops over hardcoded rituals.
   The core supports cycles such as plan, act, review, postmortem, adjust, forget, and retry without assuming one universal productivity method, ritual set, or workflow taxonomy.

7. Learning from prediction error.
   EXOCORTEX improves by comparing expected outcomes with real outcomes, routing mismatches into memory, procedure updates, postmortems, review loops, or forgetting.

8. Reality Alignment over agreement.
   The system is loyal to the user's long-term interests, not only the user's current command. It must challenge scope creep, weak assumptions, avoidant behavior, false certainty, and bad tradeoffs when evidence supports disagreement.

9. User agency, permission, and reversibility.
   The core must preserve user control. Sensitive actions require review, bounded autonomy, auditability, and rollback or correction paths where relevant.

10. Max Vision stays separated from first buildable foundation.
    The final EXOCORTEX vision can be large, but this definition must keep the first buildable boundary small enough to validate the substrate without turning into architecture, roadmap, or implementation planning.

## Adaptation-native substrate principle

EXOCORTEX Core Foundation must be adaptation-native and domain-agnostic.

It must not assume a fixed set of domains, workflows, processes, UI screens, assistant roles, rituals, dashboards, tools, or operating modes.

The core must support adaptation across arbitrary user domains, processes, mechanisms, UI/surface forms, workflows, tools/actions, autonomy levels, memory/context schemas, review/learning/postmortem loops, and Reality Alignment modes.

Adaptive capacity is core. Concrete adapted surfaces, workflows, and tools are usually extensions unless required for the first buildable foundation / Min Proof.

This means the question for any proposed feature is not "Is this useful for the current imagined user?" but "Does this belong to the durable substrate that lets EXOCORTEX adapt to many possible users, domains, tools, surfaces, and operating styles?"

## Core substrate components

| Component | Core responsibility | Boundary |
| --- | --- | --- |
| Persistent memory/context substrate | Preserve durable user-world context: goals, projects, people, commitments, preferences, decisions, procedures, outcomes, corrections, and environment state. | Core defines persistence responsibilities and correction/forgetting needs, not database design or schema implementation. |
| Experience and outcome record | Capture enough event, decision, action, expectation, result, and correction history to support review and learning. | Core concept only. It is not an Event Ledger prototype or storage architecture. |
| Context Compiler | Select and assemble relevant context for the current task, including active goal, memory, constraints, tools, autonomy level, recent errors, and response style. | Core must avoid whole-world prompt dumping. Retrieval algorithms and prompt formats are not selected here. |
| Model-agnostic cognitive engine interface | Treat models as replaceable reasoning engines that can read compiled context, use tools, generate outputs, and update proposals. | Core does not select provider, model, API, routing, or fine-tuning strategy. |
| Tools/actions extensibility layer | Let EXOCORTEX act through an expandable set of read, draft, write-with-approval, bounded-autonomous, and forbidden actions. | Core defines extensibility and permission categories, not a fixed tool registry implementation or MCP plan. |
| Interaction/process loop substrate | Support reusable loops such as think, plan, act, review, postmortem, update memory, adjust procedure, and escalate. | Core must not hardcode one workflow method, role taxonomy, ritual calendar, or operating mode. |
| Workspace surface substrate | Support composable environments such as chat, rooms, boards, documents, dashboards, canvases, inspectors, and widgets. | Core treats surfaces as adaptable forms. Specific UI screens, mockups, and omnichannel buildout are extensions unless needed for Min Proof. |
| Outcome learning and postmortem loop | Compare expected outcome with actual outcome, identify mismatch, classify learning value, and route updates into memory, procedures, reviews, or forgetting. | Core defines the loop. It does not build a prediction engine, dopamine system, or postmortem product yet. |
| Reality Alignment layer | Challenge unsupported assumptions, scope creep, self-deception, poor tradeoffs, and sycophantic agreement. Support disagreement levels and evidence-backed objections. | Core defines non-sycophantic behavior. It does not require a full red-team module or cognitive-bias product now. |
| Permission, trust, and review controls | Separate read-only, draft-only, approval-required, bounded autonomous, and forbidden actions. Preserve inspectability and correction paths. | Core defines control requirements. It does not choose authentication, storage, or security architecture. |
| Adaptation classifier | Classify proposed capabilities as Core, First buildable foundation, Extension, Max Vision, or Not-now. | Core keeps scope stable. It is not a backlog, roadmap, or feature prioritization system. |

## First buildable foundation / Min Proof boundary

The first buildable foundation is the smallest product proof that the EXOCORTEX substrate can work. It is not the full app, not a polished product suite, and not an implementation plan inside this artifact.

Min Proof should prove the core substrate behaviors:

- the system can preserve persistent memory/context across sessions;
- the system can compile relevant context for a current task without prompt-dumping the whole user world;
- the system can use a replaceable model as cognitive engine;
- the system can expose at least one safe tool/action pathway under permission boundaries;
- the system can support at least one extensible workspace surface beyond raw chat, if needed to prove surfaces-as-environment;
- the system can record an expected outcome and compare it with a real outcome;
- the system can route mismatch into memory, review, procedure update, or forgetting;
- the system can challenge a bad or weakly supported user request through Reality Alignment;
- the system can classify new proposed features without absorbing Max Vision into the first build.

Min Proof should exclude:

- full architecture;
- stack, provider, storage, API, or deployment choice;
- full memory model implementation;
- Event Ledger prototype;
- tool registry implementation;
- MCP integration plan;
- automation implementation;
- mobile, desktop, messenger, voice, or omnichannel buildout;
- full dashboard, room, canvas, kanban, or widget library;
- full roadmap or backlog;
- autonomous product execution graph.

Min Proof is successful when it validates that the substrate can adapt and compound. It is not successful merely because a chat interface, dashboard, or prototype exists.

## Max Vision vs Core vs Extension vs Not-now classifier

Use this classifier for every proposed feature, subsystem, or surface.

| Class | Definition | Acceptance test | Examples |
| --- | --- | --- | --- |
| Core | Durable substrate capability without which EXOCORTEX becomes a thin assistant wrapper or cannot adapt across domains. | Removing it breaks persistence, model replaceability, context compilation, tool/action extensibility, learning, surfaces-as-environment, Reality Alignment, or safe adaptation. | Persistent memory/context substrate, Context Compiler, model-agnostic engine interface, permission categories, outcome learning loop, Reality Alignment. |
| First buildable foundation / Min Proof | The smallest concrete proof needed to validate that a core capability works at all. | It directly proves a core principle and is small enough to avoid architecture, roadmap, or full product expansion. | One bounded memory/context flow, one relevant-context compilation path, one safe action pathway, one outcome review loop, one minimal surface if needed. |
| Extension / future surface | Useful adapted expression of the core for a domain, workflow, toolset, UI form, automation, or operating style. | Removing it does not break the core substrate, but adding it later may make EXOCORTEX more useful. | Project rooms, weekly review room, canvas, kanban, meeting center, automation builder, messenger access, specialized dashboards. |
| Max Vision | Long-horizon product expression of the core at mature scale. | It describes where the substrate could grow after validated foundations and later decisions. It should inspire boundaries, not define immediate scope. | Omnichannel body, Dream Lab, broad strategy engine, automation foundry, dynamic UI generation, large widget ecosystem. |
| Not-now | Work that is premature, forbidden, or scope-expanding for this Goal or the first foundation boundary. | It requires implementation, stack/provider/storage/API choice, full architecture, broad roadmap, prototype work, or a human decision not present in this Goal. | Tech stack shortlist, database architecture, Event Ledger prototype, Memory Model prototype, MCP plan, UI mockups, full app roadmap. |

Decision rules:

- If the feature is a specific UI screen, workflow, ritual, tool, domain process, assistant role, or automation, default to Extension unless it is the smallest proof needed for Min Proof.
- If the feature selects technology, provider, API, storage, deployment, or implementation architecture, classify as Not-now.
- If the feature expresses mature product ambition but is not needed to validate the substrate now, classify as Max Vision.
- If the feature protects adaptation across arbitrary domains, processes, surfaces, tools, autonomy levels, memory schemas, learning loops, or Reality Alignment modes, consider Core.
- If a feature is useful only for the current imagined workflow, it is not Core by default.

## Non-goals

This definition does not authorize:

- app implementation;
- tech stack choice;
- full technical architecture;
- database or storage architecture;
- model provider selection;
- API design;
- UI mockups;
- Event Ledger prototype;
- Memory Model prototype;
- Tool registry implementation;
- MCP integration plan;
- automation implementation;
- mobile, desktop, messenger, voice, or omnichannel buildout;
- Task Master graph creation;
- Codex product execution graph;
- full product roadmap or backlog;
- mutation of Project Files;
- mutation of `08_DIRECTION_MAP.md`;
- sibling Direction changes.

The EXOCORTEX concept seed remains concept input. It is not an executable roadmap and does not make every listed product idea part of the core.

## Validation criteria

A reviewer can accept this Core Foundation Definition only if all checks pass:

1. Definition check.
   The artifact defines EXOCORTEX as a persistent personal AI brain / external-brain substrate, not a chat wrapper, prompt, model, fixed assistant role, or fixed UI.

2. Memory/context persistence check.
   Persistent memory and context are core, including durable user-world facts, goals, decisions, outcomes, procedures, corrections, and forgetting/correction needs.

3. Model interoperability check.
   The model is a replaceable cognitive engine. The durable product core is outside model weights and should compound with future models.

4. Context Compiler check.
   Relevant-context selection is core and explicitly avoids dumping the whole user world into a prompt.

5. Tools/actions extensibility check.
   Tools/actions are defined as an extensible body with permission boundaries, not as a fixed implementation list.

6. Interaction/process loop check.
   The core supports loops for planning, action, review, learning, correction, and escalation without hardcoding one workflow taxonomy.

7. Workspace surfaces check.
   Workspace surfaces are extensible environments. No fixed dashboard, room, board, canvas, or chat screen is treated as the product core.

8. Outcome learning / prediction error check.
   The core includes an expected-outcome vs real-outcome learning loop that can route mismatches into memory, procedure updates, postmortems, review, or forgetting.

9. Reality Alignment / anti-sycophancy check.
   Non-sycophantic disagreement and reality-check behavior are core, especially against scope creep, unsupported assumptions, bad tradeoffs, and self-deception.

10. First buildable foundation boundary check.
    The Min Proof boundary is explicit and excludes implementation, stack, provider, storage, API, full architecture, prototype, automation buildout, omnichannel expansion, and roadmap work.

11. Classifier check.
    A reviewer can classify proposed work as Core, First buildable foundation / Min Proof, Extension / future surface, Max Vision, or Not-now.

12. Adaptation breadth test.
    The definition still holds if the user later needs a completely different domain, process, UI surface, workflow, toolset, autonomy level, memory schema, review loop, Reality Alignment style, or working style.

13. Non-goal check.
    The artifact does not choose architecture, stack, provider, storage, APIs, UI mockups, implementation path, Task Master graph, Codex product execution graph, or product roadmap.

14. Review readiness check.
    The artifact is coherent enough for R1 review and phase-progress gating without additional external research, product implementation, or architecture decisions.
