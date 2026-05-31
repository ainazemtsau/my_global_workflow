# Workflow v3 Quality and Recovery

status: active_skeleton_namespace_corrected

## Core rules

No hidden state change.

No validation means no done claim.

Chat output, Codex output, Project Files/Sources, Signals, Handler results, Action Inbox items, Check Jobs, and document existence do not create accepted state.

## Context/source gate

Checks:

- source authority is identified;
- exact repo/path/ref is known when exact state matters;
- read completeness and limitations are stated;
- Project Files/Sources are classified as cache/context;
- missing or stale source is visible.

Fails when required source is missing, stale cache is treated as truth, or repository state is guessed.

## Entity coverage gate

Checks:

- every entity in `workflow_v3/interfaces/00_ENTITY_REGISTRY.md` appears in `workflow_v3/interfaces/99_COVERAGE_MATRIX.md`;
- each entity has a canonical definition file/interface;
- storage location is identified when applicable;
- related Signals, Handlers, packets/templates, state mutation rights, and acceptance/update requirements are visible where applicable;
- unresolved risks are named instead of hidden.

Fails when an interface entity can be lost, redefined independently, or routed without coverage.

## Direction lifecycle gate

Checks:

- Direction lifecycle transitions use visible lifecycle Signals and lifecycle Handlers;
- lifecycle Handler output remains candidate only;
- Direction Spine, Direction Map, Active Front, Work Graph, and Work Contract transitions are not selected by chat intuition;
- every state-changing lifecycle transition has Event Loop Closure and acceptance/update path;
- blocked lifecycle transition stops product work until repaired, accepted, or split.

Fails when lifecycle state is invented, accepted silently, or advanced without visible closure.

## Scope gate

Checks:

- work has one bounded target;
- in-scope and out-of-scope boundaries are explicit;
- allowed and forbidden paths/surfaces are known;
- no unrelated continuation or phase jump occurs.

Fails when scope expands, mixes independent jobs, or requires forbidden surfaces.

## Evidence gate

Checks:

- expected evidence is defined;
- result includes evidence or an explicit no-evidence reason;
- validation output supports the claim;
- conflicting evidence is named.

Fails when a done claim lacks validation or evidence.

## Acceptance gate

Checks:

- result remains candidate unless explicitly accepted;
- Acceptance Decision is separate and visible;
- no adapter accepts its own output;
- human action is not assumed complete without confirmation.

Fails when acceptance is inferred or hidden.

## Signal/Handler misuse gate

Checks:

- Signal remains an emitted event/fact record;
- Signal is not an Action Inbox item;
- Handler remains a registry rule/process that creates candidate output only;
- Action Inbox stores candidate actions, not raw signals;
- Check Job remains bounded verification;
- Event Loop Closure appears after material work/review;
- legacy import signal is handled by `legacy_import_guard_handler`;
- no accepted-state mutation from Signal, Handler, or Action Inbox.

Fails when:

- Signal treated as accepted state;
- Handler executes work;
- Action Inbox stores raw untriaged signals as backlog;
- event loop closure omitted after material work;
- legacy import signal ignored.

Recovery:

- block or reject the unsafe result;
- rerun same-scope closure with EVENT LOOP CLOSURE;
- convert only selected candidate actions into Check Jobs, Launch Packets, repair Next Moves, or human decision requests;
- use `legacy_import_guard_handler` before touching legacy state.

## Progression Router misuse gate

Checks:

- Event Loop Closure uses `progression_router_handler` after material work or review closes;
- one `primary_next_move` is selected before any optional secondary candidates;
- transfer steps include a complete Transition Packet or next-chat prompt;
- Codex handoff returns to the same current chat for verification and closure;
- next material chat waits until the current material target is accepted, persisted, verified, or explicitly stopped;
- Action Inbox remains candidate storage, not a roadmap.

Fails when:

- next step is guessed without closure;
- multiple next steps are launched silently;
- Action Inbox becomes roadmap;
- acceptance or persistence is skipped;
- a transfer step only says to create a package instead of providing the complete packet;
- product work continues after a blocking signal.

Recovery:

- stop the unsafe continuation;
- rerun EVENT LOOP CLOSURE with `progression_router_handler`;
- choose one `primary_next_move`;
- provide a complete Transition Packet when transfer is needed;
- return for human/parent acceptance when acceptance is unclear.

## Chat lifecycle/handoff gate

Checks:

- child chat, parent chat, next material chat, Check Job, Codex run, Codex result verification, human decision surface, and Runtime Console/status chat boundaries are explicit;
- child chat serves the current parent target and returns to parent;
- child chat is not next material chat;
- next material chat starts only after current material target is accepted, persisted, verified, or explicitly stopped;
- required child results are returned before parent synthesis;
- Parent Recovery Block exists when multiple children are launched.

Fails when child work becomes an independent execution track, missing child evidence is synthesized, or next material chat starts before the current target is closed.

Recovery:

- stop synthesis when required child result is missing;
- request missing child result or rerun a narrowed child prompt;
- produce Parent Recovery Block;
- rerun Event Loop Closure and Progression Router after child/parent status is clear.

## Codex validation gate

Checks:

- branch name;
- commit SHA when committed;
- changed files;
- allowed paths only;
- forbidden paths unchanged;
- validation results;
- EOF markers for Markdown;
- residual risks;
- project refresh requirements.

Fails when Codex changes forbidden paths, omits evidence, returns unverifiable changes, or claims done after failed validation.

## Project setup refresh gate

Checks:

- Project Instructions UI update requirement is reported separately;
- Project Files/Sources refresh requirement is reported separately;
- request-only source refresh requirement is reported separately;
- do-not-upload sources are identified;
- actual Project updates are not implied by repository commits.

Fails when a file change implies a Project UI update or Project Files/Sources refresh without a separate authorized rollout package.

## Rollback/coexistence gate

Checks:

- current Workflow OS remains available as legacy/rollback;
- old files are not deleted, renamed, moved, or decommissioned;
- non-adopted Directions remain under the old Workflow OS;
- rollback path is not weakened.

Fails when a package silently replaces old Workflow OS behavior or old Direction state.

## Recovery outcomes

Use the smallest sufficient recovery outcome.

`blocked result` - return when work cannot safely continue because source, scope, permission, validation, or acceptance is missing.

`same-package repair` - repair within the same allowed scope when validation failed and the repair does not need broader authority.

`human decision request` - ask for a decision when safe progress depends on judgment, acceptance, scope, permission, or credentials.

`rollback/revert` - undo or reject a candidate change when it violated boundaries or cannot be repaired safely.

`future package split` - park work for a later explicit package when the need is real but outside current scope.

END_OF_FILE: workflow_v3/QUALITY_AND_RECOVERY.md
