# GitHub Long File Read Guard

```yaml
artifact_control:
  artifact_name: "GitHub Long File Read Guard"
  schema: github_long_file_read_guard.v1
  owner_layer: runtime
  status: canonical
  repo_path: "workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md"
  default_load: yes
  freshness: refresh_when_github_connector_or_runtime_context_loading_rules_change
  last_updated: "2026-05-13"
```

## Purpose

Prevent ChatGPT Direction Project chats from treating truncated GitHub connector reads as complete source authority.

This file is a runtime guard for GitHub file-read transport. It does not replace GitHub as source of truth. It defines when a GitHub read is insufficient.

This file owns GitHub read completeness verification, not source acquisition order. Source/context acquisition order is owned by `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md`.

## Core rule

A GitHub repository file read is **not full-file authority** if any of these are true:

- the tool response contains `truncated due to tool response token budget`;
- the tool response says `Full entry omitted because the tool response token budget was exhausted`;
- the response contains only a compact result when file content is required;
- expected end-of-file marker / tail anchor is absent;
- the chat cannot verify it saw the end of the file;
- base64, raw URL, search result, or alternate fetch still returns a truncated or omitted response;
- line count, byte size, SHA, or tail verification is required for the task but unavailable.

When any trigger is present, the file must be treated as **missing blocking context** for material work that depends on it.

## Required behavior

If material work depends on a file whose GitHub read is not full-file authority, ChatGPT must:

1. Stop the material workflow action.
2. Apply `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md` before selecting Context Request or fallback export.
3. Return a `context_request.v1` naming the exact repository path only when the context remains unavailable or unsafe.
4. Not infer missing content from memory, prior chats, search snippets, or partially returned GitHub content.
5. Not run a stage, produce a final audit verdict, or emit repository changes that depend on unseen content.

## Stage prompt special rule

Stage prompts are request-only by exact stage ID.

If an exact stage prompt file is read from GitHub and the read is truncated, omitted, or lacks tail verification:

- the prompt is considered unavailable for that run;
- the stage must not execute;
- the chat must apply `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md` before returning Context Request for the exact prompt path or requesting a supplied prompt;
- the chat must not reconstruct the prompt from memory.

This applies even when `workflow/stage_registry/STAGE_REGISTRY.md` marks the prompt as `present`.

## Runtime core cache rule

Core workflow files that are required in every Direction Project chat should be loaded as ChatGPT Project Files as a runtime cache.

The runtime cache does not replace GitHub as source of truth. It provides reliable full-file access inside the ChatGPT Project.

If GitHub and Project File cache conflict:

- a verified full GitHub read wins;
- an unverified or truncated GitHub read does not override the Project File cache;
- if the conflict affects material workflow behavior and cannot be verified, return Context Request.

## Acceptable verification

A GitHub read may be treated as complete when the run has sufficient evidence such as:

- no truncation or omitted-content marker;
- expected tail anchor is visible;
- SHA / size / line count are available when needed;
- end-of-file marker is present for files that define one;
- the end-of-file marker appears exactly once and is the last non-whitespace content;
- no content appears after the end-of-file marker;
- Codex read-only verification confirms the file from a local checkout.

A visible `END_OF_FILE` marker is not valid tail authority when later content appears after it. In that case the read is structurally conflicted and must be treated as insufficient for material workflow work until the file is repaired or a different approved tail policy is applied.

Required EOF validation shape for read-back / repository maintenance:

```yaml
eof_marker_validation:
  - file_path:
    marker_text:
    marker_count:
    marker_is_last_non_whitespace: true | false
    content_after_marker: true | false
    result: pass | fail | not_applicable
```

## Project Files cache refresh after repository maintenance

If repository maintenance changes a file that is required in ChatGPT Project Files runtime cache, the maintenance return must explicitly state that the Project File cache must be refreshed before the next material workflow run.

A GitHub commit alone is not enough to refresh ChatGPT Project Files.

Required return section:

```yaml
project_files_cache_refresh_required: true | false
target_chatgpt_project:
manual_refresh_required: true | false
blocking_before_next_material_run: true | false
changed_cached_files:
  - repository_path:
    refresh_reason:
manual_action:
```

## End-of-file marker

`END_OF_FILE: workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`
