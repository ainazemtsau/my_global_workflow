# Mealie Sync Protocol

Status: active

Purpose: define durable GitHub recipe storage and operational Mealie sync for Project `Питание`.

## Authority

```yaml
github: durable_recipe_source
mealie: operational_recipe_app
chatgpt_project: bundle_and_codex_card_author
codex: github_save_and_mealie_sync_executor
```

GitHub is the durable source for approved recipe bundles and catalog JSON files.

Mealie is the operational recipe app for searching, cooking, and meal planning. Mealie state is not the durable planning source.

ChatGPT Project `Питание` creates approved menu content, recipe details, `MEALIE_RECIPE_BUNDLE.json`, and one compact `PITANIE_CODEX_CARD`. It must not claim GitHub or Mealie was updated.

Codex saves approved files to GitHub and syncs recipes and meal planner entries to Mealie through existing external MCP server `mealie` from `rldiao/mealie-mcp-server`.

## Secrets

Mealie API keys are supplied only by environment variable:

```text
MEALIE_API_KEY
```

Repository files must not contain API tokens, bearer headers, copied cookies, or personal Mealie credentials.

## Recipe Identity

Primary durable recipe identity:

```text
extras.pitanie_recipe_id
```

Fallback duplicate check:

```text
exact recipe name + chatgpt-pitanie tag + week tag
```

If duplicate identity is ambiguous, Codex must report a conflict and must not create an uncontrolled duplicate.

## Failure Handling

If GitHub save succeeds but Mealie sync fails:

```text
Status: PENDING_MEALIE_SYNC
```

If the external Mealie MCP server or required tools are unavailable:

```text
Status: STUCK_MEALIE_MCP_UNAVAILABLE
```

If a duplicate conflict is detected:

```text
Status: STUCK
Reason: DUPLICATE_CONFLICT
```

If existing meal plan entries would be duplicated and the MCP cannot safely update/delete before creating new entries:

```text
Status: STUCK_MEAL_PLAN_DUPLICATE_RISK
```

The return must include the exact bundle path, the failed tool or endpoint, and the recommended next action.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/integrations/mealie/MEALIE_SYNC_PROTOCOL.md
