# v21 executable-binding handoff conformance

This contract closes one witnessed failure class: a PLAN can look complete, pass a prose review and still leave an
independent RED author unable to construct a fixture, invoke a seam or observe the required state. The failure must be
found before the owner approves the plan and before an EXECUTE/BUILD CALL exists.

The executable OS witness is [v21_conformance.py](v21_conformance.py). This document defines the product-facing rule.
It does not duplicate the complete SETUP, writer, archive, light or BUILD state machines defined in `PROJECT_SETUP.md`,
`VALIDATION.md`, `packets.md` and `coding-agent.md`.

## Binding rule

For every frozen/G0 change:

1. `PLAN/author` enters with only exact base, acceptance, installed validation-toolchain and conformance authority. A
   TESTABILITY path/blob or PLAN receipt cannot exist in that entry CALL.
2. The planner creates candidate `P`. Its allowed delta is the declared proposal/PLAN/tasks/spec/ADR packet plus
   `TESTABILITY.md`. It may not write product source, acceptance tests, oracle registration or a GREEN verdict.
3. Writer persists the complete planner RESULT and, through the normal event -> mechanical finalizer -> child sequence,
   creates a fresh finalized `PLAN/binding-validator` CALL for exact `P`.
4. A different fresh read-only validator independently derives the obligation union from the Direction `done_when` and
   frozen spec. It must not trust the planner's coverage list as the source of that union. In a clean scratch tree at the
   exact base it generates its own ephemeral binding probes and runs the product's real pinned compiler, discovery tool
   and one-test filtered runner for every obligation and for the union.
5. Any missing/unresolved binding, skipped command, write to the product, stale candidate, non-unique discovery, PASS or
   wrong sentinel is `PLAN RED`. Writer routes the complete gap list back to `PLAN/author`; no owner-verdict CALL exists.
6. Only a persisted GREEN validator RESULT and a fresh finalizer may create `PLAN/verdict`. That CALL freezes candidate,
   TESTABILITY mode/blob/input-manifest hash, validator session, actual observations and PLAN receipt. Only the owner's
   explicit `accepted` words for those exact unchanged bytes may authorize fresh EXECUTE. `revised|split` starts a new
   candidate and full binding validation; `rejected` creates no EXECUTE.
7. EXECUTE starts with a third role: the independent RED author. It derives real acceptance tests from the frozen spec,
   using TESTABILITY only for syntax/routes. It cannot read or reuse validator scratch probe bytes and cannot be the
   planner, binding validator or builder.

There remain exactly five engineering phases: `SETUP | RE-SYNC | PLAN | EXECUTE | BUILD`. `binding-validator` is a PLAN
substage, not a sixth phase.

## Required chronology

```text
C-plan-call
  < W-plan-candidate
  < W-binding-validator-call
  < W-plan-receipt
  < W-verdict-call
  < W-verdict-result
  < W-execute-call
```

- `W-plan-candidate` is the persisted `PLAN-CANDIDATE` RESULT from the planner. It has no GREEN, PLAN receipt or owner
  verdict.
- `W-binding-validator-call` contains finalized `plan-stage: binding-validator`, exact candidate `P`, candidate event,
  base/acceptance/toolchain authority and TESTABILITY pins.
- `W-plan-receipt` is the persisted `PLAN-GATED` RESULT from the distinct validator session. It records actual commands,
  exits, discovery ids, per-filter criteria, union result, clean before/after status and `product-writes: []`.
- `W-verdict-call` is created by a later mechanical finalizer and cites both strict-ancestor events.
- `W-verdict-result` contains the owner's actual words. `W-execute-call` is created by another later finalizer.

Every RESULT history path is `history/<YYYY-MM-DD>-<session-id>.md`. `NOW.next` contains a complete CALL or a schema-valid
pointer, never a bare id. Event and finalizer commits use `<direction> <play> <node/task>: <log line>`. These are the
existing writer contract, not alternative fixture conventions.

## TESTABILITY.md contract

`TESTABILITY.md` is a machine-readable binding contract authored with candidate `P`; it is not a validator verdict and
does not contain acceptance-test or validator-probe source. It contains:

- `change-id`, exact base authority/commit and exact Direction acceptance hash. Candidate commit `P` is intentionally
  absent because TESTABILITY is part of `P`; the later writer-finalized binding-validator CALL/event pins `P` and the
  TESTABILITY path/mode/blob externally;
- an ordinal manifest for proposal, PLAN, tasks, every delta spec, referenced ADR and each exact-base public/test-harness
  declaration used by a binding;
- the complete independently derivable obligation list and the planner's one-to-one coverage list;
- a closed typed binding registry;
- per-obligation `construct | act | observe | negative | source | skeleton` routes;
- exact compiler/discovery/runner identities required by the product adapter;
- no `GREEN`, no `plan-receipt`, no persisted probe source and no acceptance test.

TESTABILITY is excluded from its recursive input manifest and is pinned externally by path/mode/blob plus the manifest
hash. A later packet/spec/ADR/base/toolchain change invalidates the validator receipt.

### Binding registry

Every reference resolves exactly once. The permitted kinds are disjoint:

- typed literal;
- exact-base production producer with fully qualified signature and visibility;
- test-local source artifact with exact generated path/mode/blob;
- runtime resource with exact path/mode/blob and an exact loader/codec callable;
- constructed object instance with constructor, ownership and lifetime;
- callable action/observer with the exact owning instance, signature, ordered typed arguments and return;
- typed single-producer slot with operation/object lifetime;
- negative control bound to one concrete operation instance and one exact fault phase.

A source path cannot stand in for an instance, a method name cannot stand in for its owner, raw bytes cannot stand in
for a typed value, and `operation:Step` cannot stand in for a concrete operation instance. The graph is acyclic,
type/arity/visibility correct and fully reachable from an obligation.

Each route names, without prose aliases:

- construction of every topology, face, impulse/source input, handler, loopback and golden input;
- the exact action overload and every ordered argument source;
- one consistent audit/observer route and every compared field, including counters and hidden state;
- exact golden loader/codec and comparator argument/return routes;
- operation-local fault-selector input, returned slot, owner operation and before/during/after controls;
- ownership/reference/delegation observations;
- source-isolation inputs and observations;
- the complete no-implementation skeleton.

If a proposed public API is absent at the base, the probe uses an exact reflection/dynamic signature and reaches a named
runtime missing-member sentinel. A direct uncompilable call is not evidence. Existing routes must actually execute and
then reach a validator-owned sentinel; the probe does not assert the future behavioral acceptance result.

## Fresh binding-validator result

The validator receives exact `P`, but independently parses `done_when` and the spec to derive the obligation union. It
then performs all of the following in scratch outside the product worktree:

1. Verify base/candidate/toolchain/manifest and a clean byte-identical product tree.
2. Resolve the complete typed DAG and expand each skeleton.
3. Generate ephemeral binding-only source itself. Planner-supplied source is invalid.
4. Invoke the real product compiler with every compile source explicit.
5. Invoke real discovery and require exactly one unique id per obligation and the exact union.
6. Invoke the real filtered runner with only declared runtime resources and require each exact binding sentinel.
7. Materialize every operation-local fault phase, invoke its exact seam and type-observe the full audit, ownership and
   delegation surfaces. It makes no rollback, equality, golden-value or other future behavioral assertion; those belong
   only to the later independent acceptance RED author.
8. Return all gaps in one complete sweep, not only the first failure.
9. Prove `product-writes: []` and unchanged status/tree before and after.

The pinned tool identity includes real executable or interpreter path, version and content hash; script path/mode/blob;
and every loaded dependency. A descriptor string, executable bit, nickname, boolean `compiled: true`, copied expected
stdout or unlisted dynamic load is not executable evidence.

The PLAN receipt is a canonical hash over candidate/base/acceptance/toolchain/TESTABILITY pins, candidate event,
validator session, exact per-obligation and union observations, and before/after status. It first appears in the
validator RESULT. Planner session, validator session, owner-verdict session, RED-author session and builder session are
pairwise distinct.

## Independent acceptance RED

After owner approval, the RED author sees only:

- frozen spec as behavioral authority;
- pinned TESTABILITY bindings and exact-base public/test-harness manifest as syntax/route authority;
- the validator event/receipt, not its scratch source;
- no planner PLAN/tasks/ADR as a behavioral oracle and no builder/new implementation.

R is a fresh spec-derived acceptance-test/oracle commit. Its source is not copied from the binding probe, its author
session is distinct, and the builder cannot edit it. The red-boundary gate independently compiles, uniquely discovers
and runs R before builder control. This separation is deliberate: PLAN proves that tests can be written; the later RED
author independently decides what the frozen spec means.

## Product installation and re-sync

The OS witness does not replace the product-native adapter. SETUP/RE-SYNC must install a read-only
`plan_handoff_check` that:

- binds the real stack compiler/discovery/runner/interpreter and dependencies;
- implements `plan-entry`, `plan-binding`, `pre-execution`, `red-boundary`, `resume`, `deliver` and `close` checks;
- runs the OS-owned negative classes below against disposable exact-base product fixtures;
- stores an independently authored/reviewed adapter bundle (source plus output manifest) and exact conformance receipt;
- refuses stamp v21 when any case is missing, skipped, nonmaterialized or returns the wrong exit.

GasCoopGame remains contract v20 until this re-sync succeeds. Its current NearGas packet must then be regenerated and
receive a fresh full binding validation; a local amendment or historical BUILD checkpoint cannot be promoted.

## Executable OS witness

Run from the Direction OS repository root:

```powershell
python os/engineering/v21_conformance.py
```

The parent pins the resolved interpreter path/version/SHA-256 and script SHA-256, launches every case in a fresh child
process, dynamically compiles validator-generated probes, uniquely discovers them, runs each filter and checks exact
sentinels. The expected terminal field is `"status": "V21_CONFORMANCE_GREEN"`.

The current witness has one positive and 62 negative cases. A parent, per-case child, fresh validator child, real isolated
CPython compiler child, discovery child, per-filter runner children and union runner child are distinct processes. The
validator consumes immutable external done_when/spec/event bytes and the candidate typed registry/recipes; one generic
executor is the only path to completion. Every negative has an independent exact `(error-code, path)` oracle plus a
pre/post mutation fingerprint, so a broken mutator or worker is fatal rather than a successful RED.

The corpus removes the concrete create/topology/face-impulse/owned-handler/audit/loopback/fault-selector/operation-slot/
golden/codec/source/hidden-state routes, including a two-gap complete sweep. It also seeds signature, owner, ordered
argument, same-typed source edge, return/slot type, visibility, resource path/mode/size/blob, fault ownership, graph
cycle/reachability/producer, candidate/authority/toolchain, compile/discovery/filter/union, copied-sentinel and actual
product-write failures. The receipt contains observed commands/exits/hashes and before/after product-tree hashes, not
candidate booleans.

The witness is a regression test for the OS rule, not proof that an arbitrary product adapter is correct. The binding
GREEN for a real change comes only from that product's fresh native validator run against its exact candidate/base. This
contract prevents the witnessed elementary binding class from first surfacing in BUILD; it does not claim that no subtle
semantic specification mistake can ever survive human and adversarial review.

END_OF_FILE: os/engineering/V21-CONFORMANCE.md
