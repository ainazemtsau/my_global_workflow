# Mealie MCP Setup

Status: active

Purpose: setup notes for the external Mealie MCP server used by Project `Питание`.

## Selected Server

Use:

```text
rldiao/mealie-mcp-server
```

External install path:

```text
C:\my_global_workflow_tools\mealie-mcp-server
```

Project-local config:

```text
.codex/config.toml
```

It must run the external server:

```text
uv --directory C:\my_global_workflow_tools\mealie-mcp-server\src run server.py
```

## Environment Variables

Set these outside the repository before starting Codex:

```powershell
$env:MEALIE_BASE_URL = "http://localhost:9925"
$env:MEALIE_API_KEY = "<token from Mealie>"
```

Do not commit tokens, `.env` files, shell history exports, screenshots with tokens, or copied request headers to GitHub.

## Test `/mcp` In Codex

1. Open Codex in this nutrition project directory.
2. Confirm the project-local `.codex/config.toml` is trusted.
3. Run `/mcp`.
4. Confirm server `mealie` is enabled.
5. Confirm Mealie recipe, category, tag, shopping list, and meal plan tools are listed.
6. Confirm a bulk meal plan creation tool such as `create_mealplan_bulk` is available before running meal planner sync.

## MCP Smoke Test

Run only after `MEALIE_BASE_URL` and `MEALIE_API_KEY` are set:

```text
Use read-only Mealie MCP tools to list categories/tags or inspect available meal plan tools.
```

Do not run real recipe upsert or meal planner creation unless the user explicitly asks for a smoke sync or recipe sync.

## Failure States

- `NEEDS_ENV`: `MEALIE_BASE_URL` or `MEALIE_API_KEY` is missing.
- `STUCK_MEALIE_MCP_UNAVAILABLE`: external MCP server or required Mealie tools are unavailable.
- `PENDING_MEALIE_SYNC`: GitHub save succeeded, but Mealie sync did not finish.
- `STUCK_MEAL_PLAN_DUPLICATE_RISK`: meal plan entries appear duplicative and cannot be safely updated/deleted through MCP before create.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/integrations/mealie/MEALIE_MCP_SETUP.md
