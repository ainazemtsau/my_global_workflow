# RESULT -- s-health-chatgpt-project-memory-fence-001

direction: health - play: repair/work - node: g-health-core - bet: b-health-core-kernel
trigger: owner reported ChatGPT Project using ChatGPT memory/past context during Health AI startup
date: 2026-06-22

## outcome
Health AI's ChatGPT Project bootstrap now has an explicit repo-authority memory fence. It tells ChatGPT to use only
files read from the connected GitHub repository during the turn as current Health AI authority; ignore ChatGPT memory,
Reference chat history, prior project chats, uploaded/manual snapshots, account profile, and provider hidden state as
health/system facts; anchor authoritative facts to repo paths; and block to reduced/no-repo or repair instead of
backfilling from memory.

The stale bootstrap claim "No domain is attached today" was removed from provider-facing docs. Current attached
domains are now determined by `core/extensions/registry.md`, which is the actual source of truth.

## evidence
- health-ai commit: 731348b `health-ai: fence ChatGPT project memory to repo authority`.
- Files changed: `CHATGPT_PROJECT.md`, `AGENTS.md`, `README.md`.
- Official OpenAI docs checked: Projects can reference project and non-project conversations unless project-only
  memory is used; account memory remains active in projects when enabled; older projects may need recreation for
  project-only memory.
- Verification: `python tools/check_kernel_spine.py` -> PASS; `git diff --check -- AGENTS.md CHATGPT_PROJECT.md
  README.md` -> no errors; stale phrase search for "No domain is attached" returned no hits in provider docs.

## state_changes
- live/health/NOW.md: updated next CALL context to reference health-ai @731348b and the new
  `CHATGPT_PROJECT.md` memory fence.
- live/health/LOG.md: appended this session's log line.
- live/health/history/: added this RESULT.
- TREE.md: unchanged.

## captures
- Product hygiene: health-ai local main remains ahead of origin by the earlier no-op init/revert pair plus this new
  commit; push/drop decision is separate.

## decisions_needed
None.

## play_check
- 1 OPEN: done -- owner problem mapped to current incident-fix/product bootstrap surface.
- 2 DIAGNOSE: done -- OpenAI docs + repo inspection showed memory risk and stale provider bootstrap claims.
- 3 DESIGN FIX: done -- minimal authority/memory fence plus registry-authority cleanup; kernel/domain state untouched.
- 4 APPLY/VERIFY: done -- health-ai commit 731348b; kernel check PASS; diff check PASS.
- 5 CLOSE: done -- live/health state reconciled to product commit and next CALL preserved.

## log
health/g-health-core ChatGPT project memory fence: health-ai @731348b tightened project instructions to repo authority
and registry truth; kernel check PASS.

## next
CALL c-health-core-kernel-incident-fix-001
to: session lead + executor (health-ai)
direction: health
node: g-health-core
bet: b-health-core-kernel
repo: C:\projects\health-ai
goal: |
  Nutrition cold-start reaches the next owner-gated PROGRAM checkpoint from the committed delegated-research handoff.
context: |
  Current product state includes health-ai @731348b with ChatGPT Project memory fenced to repo authority. Continue
  from live/health/NOW.md and the committed x_nutrition delegated-research handoff.
boundaries: |
  No ACTIVE nutrition execution menu/grocery/recipe before the owner gate. Do not use ChatGPT memory or prior chats
  as Health AI state. Do not reintroduce synthetic/demo data.
done_when: |
  Delegated Deep Research child has returned its conclusion; PROGRAM has resumed from the committed handoff/cursor;
  the next owner-gated PROGRAM checkpoint is ready; no nutrition execution artifact is ACTIVE without approval; and
  WA-K6/WA-K8 live evidence status is explicitly named.
return: |
  RESULT with product commits/evidence, any owner decision needed, exact live/health state_changes, and the next CALL.
budget: one focused session

END_OF_FILE: live/health/history/2026-06-22-s-health-chatgpt-project-memory-fence-001.md
