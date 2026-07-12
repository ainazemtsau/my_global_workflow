CALL c-solmax-operating-substrate-first-process-creator-t1-risk-gate-001
to: session
direction: solmax
play: work
node: g-operating-substrate-first-process-creator
task: t-1

goal: |
  Falsify or validate, before implementation, that a semantically complete
  owner-facing Process Creator can turn ordinary owner intent into a
  concrete process-pack candidate without requiring the owner to operate
  internal routing, state, admission, audit or child-agent machinery.

context: |
  Read:
  - live/solmax/CHARTER.md
  - live/solmax/TREE.md
  - live/solmax/NOW.md
  - live/solmax/work/operating-substrate-minimal-bootstrap-implementation-readiness-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-core-invariant-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-relationship-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-process-pack-instantiation-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-shared-owner-context-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-persistence-history-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-routing-procedure-001.md
  - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md
  - live/solmax/history/2026-07-12-s-solmax-operating-substrate-first-process-creator-shape-001.md

  Binding shape:
  - active bet:
    b-operating-substrate-first-process-creator-bootstrap-001
  - appetite:
    3 focused execution days; no mandatory bounded functionality may be
    cut to fit.
  - t-1 is a no-write pre-implementation kill gate.
  - Q1-Q7 are binding.
  - Q8-Q12 remain downstream unless a concrete named semantic gap appears.
  - Q13 is proof-before-live-claim.
  - Q14 choices are implementation-specific.

  Use this bounded exemplar for the walkthrough:

  Process intent:
  "Create an evidence-to-decision process that accepts an owner decision
  question, determines which decision criteria and sources are mandatory,
  compares two or three legitimate options, and returns a concise
  recommendation, evidence, uncertainties, unresolved owners and portable
  continuation."

  Exemplar properties:
  - read-only;
  - no durable or external effect;
  - one owner-facing integration owner;
  - evidence and source requirements are process-pack-owned;
  - the process must not invent a missing mandatory criterion;
  - output should be a useful decision brief, bounded clarification, clear
    block or continuation, not internal process machinery.

  Required adverse branch:
  - the intake omits one material decision criterion whose value could
    reverse the recommendation;
  - the creator must either ask one bounded question or return an explicit
    blocked/unresolved disposition;
  - it must not guess the criterion, silently choose a nearest procedure or
    report a completed decision.

boundaries: |
  No repository writes.
  No durable process-pack artifact creation.
  No implementation, schema, carrier, runtime, repository or topology
  selection.
  Do not reopen or weaken Q1-Q7.
  Do not require full Q8-Q12 completion.
  Do not treat ChatGPT, Codex or another current adapter as process
  semantics.
  Do not freeze a universal process-pack template, manifest, field list,
  service-block list or procedure catalogue.
  Concrete procedures, routing, domain evidence/effect policy and writer
  policy remain process-pack-owned.
  Structural coverage is not useful-live proof.
  Do not ask the owner to choose internal procedure names, responsibility
  classes, lifecycle labels or state planes.
  Do not create a t-2 implementation CALL after FAIL.

done_when: |
  Produce one complete no-write walkthrough with:

  1. The owner-facing intake as the owner would naturally provide it.
  2. The minimum clarification/routing behavior.
  3. The resulting complete candidate pack semantic outline.
  4. Explicit coverage of:
     - objective and applicability;
     - concrete process boundaries;
     - process vocabulary;
     - procedures and local routing;
     - state/context/source/memory/history/evidence/artifact/result
       distinctions;
     - authority/effects and escalation;
     - writer policy;
     - capability requirements and degraded routes;
     - success, stop, failure and recovery;
     - continuation and compatibility;
     - process-specific structural and live-proof scenarios.
  5. Atomic classification of each material concern as:
     - inherited kernel;
     - reusable-service candidate;
     - process-pack declaration;
     - owner-profile concern;
     - adapter/implementation concern.
  6. One primary normative owner for each material atomic claim.
  7. The adverse missing-criterion branch without invented input or silent
     fallback.
  8. The concise owner-facing closure that would be shown by default.
  9. The deeper inspectable semantic trace used only for refutation.
  10. An explicit verdict:

      PASS only if:
      - Q1-Q7 are sufficient;
      - no unnamed Q8-Q12 answer is required;
      - the full creator flow is semantically complete;
      - the owner-facing flow is not bureaucratic;
      - the adverse path is safe and useful;
      - implementation neutrality is preserved.

      FAIL otherwise, with exactly one primary failure class:
      - named architecture gap;
      - creator-flow/UX failure;
      - pack-owned policy gap;
      - implementation-mapping issue;
      - insufficient evidence.

  No file or durable state mutation occurs.

return: |
  RESULT containing:
  - PASS or FAIL;
  - falsification evidence;
  - complete candidate pack semantic outline;
  - owner-facing walkthrough;
  - adverse-path walkthrough;
  - Q1-Q7 conformance matrix;
  - any concrete named semantic gap;
  - anti-bureaucracy verdict;
  - exact task-state changes.

  If PASS:
  - mark t-1 done;
  - activate t-2;
  - return one ready executor CALL for t-2 that treats its concrete
    repository/carrier/layout choice as bounded implementation, not
    substrate architecture.

  If FAIL:
  - do not activate t-2;
  - route according to the identified failure class;
  - preserve the active bet only when the failure is repairable within
    appetite and existing scope;
  - otherwise trigger review/kill without extending appetite.

budget: 0.25 focused execution day
parent: b-operating-substrate-first-process-creator-bootstrap-001
surface: chatgpt

END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-first-process-creator-t1-risk-gate-001.md
