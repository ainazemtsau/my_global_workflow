# Mealie MCP Setup

Status: active

Purpose: configure a project-local Codex MCP server that lets Codex sync approved Project `Питание` recipe bundles to Mealie.

## One-Time Virtual Environment Setup

Run from:

```text
C:\my_global_workflow_worktrees\health-and-beauty\directions\health-and-beauty\projects\nutrition
```

Create and populate the local virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install mcp requests pyyaml
```

The project-local Codex config is:

```text
.codex/config.toml
```

It points Codex at:

```text
integrations/mealie/mealie_mcp_server.py
```

## Environment Variables

Set these outside the repository before starting Codex:

```powershell
$env:MEALIE_BASE_URL = "http://localhost:9925"
$env:MEALIE_API_TOKEN = "<token from Mealie>"
```

Do not commit tokens, `.env` files, shell history exports, screenshots with tokens, or copied request headers to GitHub.

## Test `/mcp` In Codex

1. Open Codex in this nutrition project directory.
2. Confirm the project-local `.codex/config.toml` is trusted.
3. Run `/mcp`.
4. Confirm server `mealie` is enabled.
5. Confirm tools are listed:
   - `mealie_healthcheck`
   - `mealie_get_taxonomy`
   - `mealie_validate_recipe_bundle`
   - `mealie_dry_run_recipe_bundle`
   - `mealie_upsert_recipe_bundle`

## MCP Smoke Test

Run only after `MEALIE_BASE_URL` and `MEALIE_API_TOKEN` are set:

```text
Call MCP tool mealie_healthcheck.
Call MCP tool mealie_get_taxonomy.
Call MCP tool mealie_validate_recipe_bundle with weeks/current/MEALIE_RECIPE_BUNDLE.json content.
```

Do not run `mealie_upsert_recipe_bundle` unless the user explicitly asks for a smoke sync or recipe sync.

## Failure States

- `NEEDS_ENV`: `MEALIE_BASE_URL` or `MEALIE_API_TOKEN` is missing.
- `UNREACHABLE`: Mealie did not respond at `/docs` or `/openapi.json`.
- `UNAUTHORIZED`: Mealie rejected the bearer token.
- `STUCK_API_SCHEMA`: local Mealie OpenAPI does not expose the recipe or taxonomy endpoint needed for safe sync.
- `PENDING_MEALIE_SYNC`: GitHub save succeeded, but Mealie sync did not finish.
- `DUPLICATE_CONFLICT`: more than one existing recipe matched the same Project `Питание` recipe identity.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/integrations/mealie/MEALIE_MCP_SETUP.md
