# External Mealie MCP

Status: disabled_for_project_writes

Purpose: record why the old external MCP path is not the authoritative Mealie write path for Project `Питание`.

## Current Write Path

Use:

```text
integrations/mealie/mealie_api_sync.py
```

The script writes recipes through Mealie HTTP API and verifies native structured ingredient read-back.

## Disabled MCP

The previous MCP server was:

```text
rldiao/mealie-mcp-server
```

External install path:

```text
C:\my_global_workflow_tools\mealie-mcp-server
```

Project config:

```text
.codex/config.toml
mcp_servers.mealie.enabled = false
```

Do not use this MCP for recipe upsert or meal planner writes. It can produce Mealie ingredients where note/display is populated but amount, unit, and food are not reliably populated.

## Allowed Use

The generic MCP may be used only for non-authoritative read-only inspection when direct API access is unavailable. Any actual write must go through `MEALIE_API_SYNC.md` or a future user-approved MCP wrapper that delegates to the same native structured ingredient contract.

## Responsibility Boundary

Project `Питание` outputs a compact `PITANIE_CODEX_CARD` only.

Codex performs:

- GitHub durable state save;
- Mealie recipe sync through the project-local API tool;
- Mealie meal planner sync through the project-local API tool;
- read-back validation that normal ingredients are not note-only rows.

The ChatGPT Project must not claim GitHub save or Mealie sync without Codex evidence.

## Failure States

- `PENDING_MEALIE_SYNC`: GitHub save succeeded, but recipe or meal planner sync did not finish.
- `NEEDS_ENV`: Mealie API URL or token is missing.
- `STUCK`: Mealie read-back does not preserve native structured ingredient fields.
- `STUCK_MEAL_PLAN_DUPLICATE_RISK`: planner slots are duplicative and cannot be safely updated before create.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/integrations/mealie/EXTERNAL_MEALIE_MCP.md
