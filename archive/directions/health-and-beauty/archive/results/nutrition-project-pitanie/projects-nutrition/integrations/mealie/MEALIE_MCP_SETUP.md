# Mealie MCP Setup

Status: disabled_for_project_writes

Purpose: historical setup notes for the generic external Mealie MCP server.

## Current Project Rule

Do not use the generic Mealie MCP server for Project `Питание` recipe or meal planner writes.

Use the project-local API tool instead:

```text
integrations/mealie/mealie_api_sync.py
```

The project-local Codex config keeps the generic MCP entry disabled:

```text
.codex/config.toml
mcp_servers.mealie.enabled = false
```

## Why Disabled

The generic MCP path can collapse ingredients into a single display/note string. Project `Питание` requires native Mealie ingredient fields:

```text
quantity
unit
food
note
```

This is required so Mealie shows amount, unit, and product separately instead of storing the ingredient as one note.

## Historical Server

The old selected server was:

```text
rldiao/mealie-mcp-server
```

External install path:

```text
C:\my_global_workflow_tools\mealie-mcp-server
```

Do not restore this as the write path unless the user explicitly requests a new MCP wrapper and it preserves the API sync contract from `MEALIE_API_SYNC.md`.

## Secrets

No Mealie API keys, bearer headers, cookies, copied request headers, `.env` files, or screenshots with secrets belong in GitHub.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/integrations/mealie/MEALIE_MCP_SETUP.md
