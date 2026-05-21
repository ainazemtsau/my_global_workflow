# External Mealie MCP

Status: active

Purpose: document the external MCP server used by Project `Питание` for Mealie recipe and meal planner sync.

## Selected MCP

```text
rldiao/mealie-mcp-server
```

External install path:

```text
C:\my_global_workflow_tools\mealie-mcp-server
```

Codex project config:

```text
.codex/config.toml
```

The config must point to the external server with:

```text
uv --directory C:\my_global_workflow_tools\mealie-mcp-server\src run server.py
```

Do not use a custom project-local Mealie MCP server.

## Environment

Required environment variables:

```text
MEALIE_BASE_URL
MEALIE_API_KEY
```

No Mealie API keys, bearer headers, cookies, copied request headers, `.env` files, or screenshots with secrets belong in GitHub.

## Responsibility Boundary

Project `Питание` outputs a compact `PITANIE_CODEX_CARD` only.

Codex performs:

- GitHub durable state save;
- Mealie recipe sync through existing MCP tools;
- Mealie meal planner sync through existing MCP tools.

The ChatGPT Project must not claim GitHub save or Mealie sync without Codex evidence.

## Failure States

- `PENDING_MEALIE_SYNC`: GitHub save succeeded, but recipe or meal planner sync did not finish.
- `STUCK_MEALIE_MCP_UNAVAILABLE`: external MCP server or required Mealie MCP tools are unavailable.
- `STUCK_MEAL_PLAN_DUPLICATE_RISK`: meal plan entries appear duplicative and the MCP cannot safely update/delete before creating new entries.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/integrations/mealie/EXTERNAL_MEALIE_MCP.md
