# 03 Codex Return Packet Contract
artifact_control:
  artifact_name: "03 Codex Return Packet Contract"
  schema: codex_workflow_contract.v1
  owner_layer: codex_runtime_contract
  status: canonical
  repo_path: "workflow/codex/CODEX_RETURN_PACKET_CONTRACT.md"
  authority: "GitHub repository canonical after file read-back / diff verification / commit verification"
  activation_scope: workflow_runtime_reference
  freshness: refresh_when_codex_runtime_contract_changes
  last_updated: "2026-05-13"

# 03 Codex Return Packet Contract

## Purpose

A Codex Return Packet is the required response from Codex after executing, previewing, blocking, or failing a Codex Wave.

It is the evidence-bearing bridge back to ChatGPT or a human validator. It must be complete enough for validation without relying on private Codex memory.

## Schema authority boundary

This file defines semantic safety requirements for Codex return evidence.

It is not the canonical packet schema authority.

Canonical packet schema lives in:

```text
workflow/transport/CODEX_RETURN_PACKET.md
```

Canonical schema identity:

```yaml
workflow_packet: 1
type: codex_return
schema: codex_return.v1
```

Human-readable names such as `Codex Return Packet` may remain in prose.

Legacy names such as `codex_return_packet`, `codex_return_packet.v1`, and `CODEX_RETURN_PACKET_BEGIN/END` are compatibility aliases only. They must not be treated as canonical schema IDs.

Compatibility mapping:

```text
packet_type: codex_return_packet -> type: codex_return
schema: codex_return_packet.v1 -> schema: codex_return.v1
CODEX_RETURN_PACKET_BEGIN/END -> extensions.legacy_wrapper
unmatched legacy fields -> extensions.legacy_*
```

Producers should emit `codex_return.v1`.

## Final states

Allowed final states:

```text
DONE
NEEDS_INPUT
PARTIAL
STUCK
FAILED

```

State meanings:

*   `DONE`: all requested work within scope is complete, required validators and file read-back / diff verification / commit verification are satisfied, evidence is present, and forbidden targets were not touched.
*   `NEEDS_INPUT`: Codex did not proceed because required context, access, permission, or human decision was missing.
*   `PARTIAL`: Codex completed some work but not all required work; remaining work is explicitly listed.
*   `STUCK`: Codex cannot safely continue and the next action is not obvious.
*   `FAILED`: Codex attempted work and a validator, write, file read-back / diff verification / commit verification, or safety check failed.

## DONE claim rule

Codex may use `DONE` only when all of the following are true:

1.  The requested objective was completed within the allowed scope.
2.  Every changed file or note is listed.
3.  Required validators were run and their outcomes are reported, or an explicit waiver was present in the Wave Card.
4.  Required file read-back / diff verification / commit verification was performed and passed.
5.  Forbidden targets were checked and not changed.
6.  Any remaining issues are explicitly nonblocking.
7.  The return packet includes an exact next route.

Codex must not claim DONE based only on intention, partial inspection, or an unstated assumption.

## Technical discovery evidence rule

When the Codex Wave Card, C1 launch, C2 prompt, or C2 runtime inspection requires technical discovery / architecture reuse preflight, the Codex Return Packet must include `technical_discovery` evidence.

The evidence must be compact and must not copy full product technical docs into ChatGPT.

Required `technical_discovery` evidence:

- whether preflight was required;
- whether preflight ran;
- trigger reasons;
- project-local sources loaded;
- bounded discovery scope;
- existing modules checked;
- existing public interfaces checked;
- similar code or patterns found;
- decision: `reuse_existing`, `extend_existing`, `refactor_existing`, `create_new_module`, `cross_module_request`, `blocked_missing_context`, `human_decision_required`, or `not_applicable`;
- decision reason;
- implementation boundary;
- validation impact;
- whether stop or escalation was required.

Codex must also return `technical_memory_delta` when implementation or discovery creates, changes, supersedes, or invalidates durable technical knowledge.

`technical_memory_delta` must identify whether durable update is required and which product-local artifacts are affected, such as `AGENTS.md`, Project Execution Profile, Validation Profile, Module Map, ADRs, public interface docs, internal module knowledge, or `.codex` memory.

Codex must not use `DONE` when a required technical discovery preflight was skipped, when the discovery decision requires human approval, or when a material architecture decision is outside the approved execution envelope.

## Required Codex Return Packet template

Producers should use the canonical transport template:

```text
workflow/transport/CODEX_RETURN_PACKET.md
```

Required canonical identity:

```yaml
workflow_packet: 1
type: codex_return
schema: codex_return.v1
```

The return must still satisfy this contract's semantic safety requirements:

- final state is explicit;
- requested objective and completed work are stated;
- changed files are listed;
- commands/validators are reported;
- evidence is present;
- file read-back / diff verification / commit verification is reported when required;
- forbidden targets are checked;
- blockers and nonblocking notes are explicit;
- exact next route is included.

Legacy `CODEX_RETURN_PACKET_BEGIN/END` wrapper format is accepted only as a temporary compatibility wrapper and should be normalized under `extensions.legacy_wrapper`.

Legacy shape compatibility must not weaken the DONE claim rule.

## Required GitHub repository install return compatibility

When the wave is specifically a GitHub repository install operation, Codex must use the more specific `CODEX GITHUB CHANGE RESULT` format required by the universal installer.

That install result is considered a specialized Codex Return Packet. It must still satisfy the DONE claim rule above.

## Invalid evidence patterns

These are not sufficient evidence for DONE:

*   “Looks good.”
*   “Should be installed.”
*   “I updated the relevant note.”
*   “Tests should pass.”
*   “No issues found” without naming the check performed.
*   A write claim without file read-back / diff verification / commit verification when file read-back / diff verification / commit verification is required.
*   A validator claim without command, output summary, or explicit unavailable reason.

## Acceptance anchors

This note is acceptable only if these anchors remain visible on file read-back / diff verification / commit verification:

*   `CODEX_RETURN_PACKET_BEGIN`
*   `DONE claim rule`
*   `Required validators were run`
*   `Required file read-back / diff verification / commit verification was performed and passed`
*   `Forbidden targets were checked and not changed`
*   `CODEX_RETURN_PACKET_END`
*   `technical_discovery`
*   `technical_memory_delta`
*   `Codex must not use DONE when a required technical discovery preflight was skipped`
