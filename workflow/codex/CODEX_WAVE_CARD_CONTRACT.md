# 02 Codex Wave Card Contract
artifact_control:
  artifact_name: "02 Codex Wave Card Contract"
  schema: codex_workflow_contract.v1
  owner_layer: codex_runtime_contract
  status: canonical
  repo_path: "workflow/codex/CODEX_WAVE_CARD_CONTRACT.md"
  authority: "GitHub repository canonical after file read-back / diff verification / commit verification"
  activation_scope: workflow_runtime_reference
  freshness: refresh_when_codex_runtime_contract_changes
  last_updated: "2026-05-13"

# 02 Codex Wave Card Contract

## Purpose

A Codex Wave Card is an executable handoff packet from ChatGPT, a stage prompt, or a recovery process to Codex.

It tells Codex exactly what to inspect, preview, change, test, install, repair, or validate. It also defines allowed scope, forbidden scope, evidence requirements, validator requirements, and the required return packet.

This contract defines semantic safety requirements for Codex waves. It does not define the final C1 or C2 prompts.

## Schema authority boundary

This file is not the canonical packet schema authority.

Canonical packet schema lives in:

```text
workflow/transport/CODEX_WAVE_CARD.md
```

Canonical schema identity:

```yaml
workflow_packet: 1
type: codex_wave
schema: codex_wave.v1
```

Human-readable names such as `Codex Wave Card` may remain in prose.

Legacy names and wrappers such as `codex_wave_card: 1` and `CODEX_WAVE_CARD_BEGIN/END` are compatibility aliases only. They must not be treated as canonical schema IDs.

Compatibility mapping:

```text
codex_wave_card: 1 -> workflow_packet: 1 / type: codex_wave / schema: codex_wave.v1
CODEX_WAVE_CARD_BEGIN/END -> extensions.legacy_wrapper
allowed_targets -> repository.allowed_paths or allowed_actions, depending on value type
forbidden_targets -> repository.forbidden_paths or forbidden_actions, depending on value type
unmatched legacy fields -> extensions.legacy_*
```

Producers should emit `codex_wave.v1`.

## Core rules

1. Codex must treat the Wave Card as the immediate work authorization.
2. Codex must not infer write permission from surrounding conversation when the Wave Card says read-only, preview, inspect, or validation only.
3. Codex must not write outside canonical `allowed_paths`, `allowed_actions`, or explicitly equivalent normalized legacy scope.
4. Codex must not touch canonical `forbidden_paths`, `forbidden_actions`, or explicitly equivalent normalized legacy scope.
5. Codex must return a Codex Return Packet using `codex_return.v1`, or a tolerated legacy shape normalized to `codex_return.v1`.
6. Codex must not claim DONE unless required evidence and file read-back / diff verification / commit verification requirements are satisfied.
7. Codex must preserve unknown extension fields unless explicitly instructed to normalize or replace the packet.
8. A Wave may reference Task Master, but Task Master is never canonical for workflow content and never independently proves DONE.

## Required Codex Wave Card template

Producers should use the canonical transport template:

```text
workflow/transport/CODEX_WAVE_CARD.md
```

Required canonical identity:

```yaml
workflow_packet: 1
type: codex_wave
schema: codex_wave.v1
```

The wave must still satisfy this contract's semantic safety requirements:

- Codex mode is explicit;
- write permission is explicit;
- allowed scope is bounded;
- forbidden scope is bounded;
- required sources are named;
- task objective and non-goals are explicit;
- evidence requirements are explicit;
- validators are explicit or their absence is explained;
- Task Master permissions, if any, are explicit and do not become DONE authority;
- return packet requirements are explicit.

Legacy `CODEX_WAVE_CARD_BEGIN/END` wrapper format and `codex_wave_card: 1` shape are accepted only as temporary compatibility wrappers and should be normalized under `extensions.legacy_wrapper`.

Legacy `allowed_targets` / `forbidden_targets` should be mapped to canonical `allowed_paths` / `forbidden_paths` or action-level fields according to value type.

Legacy shape compatibility must not authorize writes outside the canonical allowed scope.

## Codex behavior requirements

When Codex receives a Wave Card, it must:

1.  Read all required canonical sources it can access.
2.  Report missing required sources before attempting writes.
3.  Return a preview when `codex_mode` is `PREVIEW_FIRST`.
4.  Wait for the exact apply command when `requires_explicit_apply_command` is true.
5.  Apply only the previewed changes unless the user gives a new Wave Card.
6.  Read back every created or changed GitHub repository file when the task involves GitHub repository.
7.  Run required validators when available.
8.  State explicitly when a validator cannot be run.
9.  Return a complete Codex Return Packet.
10.  Avoid creating final stage prompts before Step 7+.

## Invalid Wave Card outcomes

Codex must return `NEEDS_INPUT` or `STUCK`, not DONE, when:

*   required canonical sources are inaccessible;
*   write scope is ambiguous;
*   allowed targets and requested work conflict;
*   forbidden paths would need to be touched;
*   validators required for DONE cannot run and no waiver is present;
*   file read-back / diff verification / commit verification is required but cannot be performed;
*   the Wave Card asks Codex to overwrite active Workflow vNext without explicit global activation approval.

## Acceptance anchors

This note is acceptable only if these anchors remain visible on file read-back / diff verification / commit verification:

*   `CODEX_WAVE_CARD_BEGIN`
*   `requires_explicit_apply_command: true`
*   `allowed_targets`
*   `forbidden_targets`
*   `must_not_mark_done_without_wave_validation: true`
*   `CODEX_WAVE_CARD_END`
