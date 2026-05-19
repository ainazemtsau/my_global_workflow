# Context Acquisition Policy

```yaml
artifact_control:
  artifact_name: "Context Acquisition Policy"
  schema: context_acquisition_policy.v1
  owner_layer: runtime
  status: canonical
  repo_path: "workflow/runtime/CONTEXT_ACQUISITION_POLICY.md"
  default_load: yes
  freshness: refresh_when_context_acquisition_or_prompt_loading_rules_change
  last_updated: "2026-05-19"
```

## Purpose

This file is the canonical runtime authority for how required repository context, exact repository paths, exact stage prompts, Project Files, attachments, pasted launch cards, GitHub connector/tool reads, Codex local exports, and user exports become available in the current ChatGPT run.

GitHub read completeness verification is delegated to:

```text
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
```

## Acquisition order

For exact repository context or exact stage prompt context, apply this order:

1. Current Project Files / attachments / pasted launch card.
2. Verified GitHub connector/tool read by exact repository_path and ref when available in the current ChatGPT run.
3. Chunked GitHub read or blob/raw read when full read is too large and the connector/tool supports it.
4. Codex read-only local export only if GitHub read is unavailable, failed, truncated, omitted, tail/EOF-unverified, unsafe, not exposed in the current run, or local checkout verification is specifically required.
5. User manual upload/export only if the above are unavailable or unsafe.

## Definitions

- `available`: the required context is present in the current run and is complete enough for the intended material use.
- `unavailable`: the required context remains absent, incomplete, unsafe, or unverified after allowed source acquisition attempts.
- `connector_available`: a GitHub connector/tool is exposed in the current ChatGPT run and can read the requested exact repository path/ref.
- `connector_unavailable`: no GitHub connector/tool is exposed in the current ChatGPT run, or the exposed tool cannot safely read the requested exact path/ref.
- `verified_full_read`: the content was read without truncation, omission, unsupported summarization, or unresolved completeness gaps.
- `tail_or_eof_verified`: the run has sufficient tail or EOF evidence under `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`.
- `acquisition_attempted`: a source path was actually attempted and the result was recorded.
- `skipped_with_reason`: a source path was not attempted and the blocking reason was recorded.
- `blocking_missing_context`: required context is unavailable and material work must not proceed safely without it.

`Unavailable` means unavailable after allowed source acquisition attempts, not merely absent from Project Files or attachments.

## GitHub-first rule

If the current ChatGPT run has a GitHub connector/tool exposed and an exact repository path/ref is known, the chat must attempt verified GitHub acquisition before returning Context Request or asking Codex/user to export the file.

If the GitHub connector/tool is not exposed in the current run, the chat must not pretend it tried GitHub. It must record `connector_unavailable` / `not_exposed` in `acquisition_audit` and then use Codex/user fallback according to this policy.

## Stage prompt availability

If an exact stage prompt path is known and the prompt is read through GitHub connector/tool with no truncation/omission and sufficient tail/EOF verification according to `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`, the prompt is available in the current run and may be used to execute the stage.

`manual_prompt_required` is valid only after allowed acquisition paths have been attempted, are unavailable, or are explicitly unsafe.

Prompt availability through a verified GitHub read must still follow the active Launch Card, stage registry, and runtime routing constraints.

## Context Request audit

Context Request for exact repository context is invalid unless `acquisition_audit` states whether Project Files, attachments, GitHub connector/tool, Codex local export, and user manual export were attempted, unavailable, failed, skipped, or not applicable.

For exact repository context or exact stage prompt context, `acquisition_audit` must identify the requested path/ref, required use, source attempts, verification evidence when available, and the remaining blocker.

## Stage-close launch boundary

A closing stage must not request next-stage prompt text, next-stage attachments, or downstream execution-only repository exports merely to run the next stage. It may request extra context only if that context is required to decide or construct the launch card itself. The next stage chat/run performs acquisition according to this policy.

Launch cards may list exact source paths for downstream acquisition without requiring the current stage to fetch, paste, or attach downstream prompt/files. If prompt text is not included, the launch card must state that the next run must acquire the prompt under this policy before downstream execution is allowed.

## End-of-file marker

`END_OF_FILE: workflow/runtime/CONTEXT_ACQUISITION_POLICY.md`
