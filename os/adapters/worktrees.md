# Adapter: parallel work & git worktrees

How to run several directions (and several sessions) at once without corrupting state. Core principle (research-backed): **many minds, one pen** -- thinking and executing parallelize freely; applying state changes to ONE direction is serialized.

## Concurrency model

| What | Parallelism |
|---|---|
| Chat sessions (ChatGPT/Claude, any play) | Parallel across/within directions; starts still obey track WIP and CALL budgets -- sessions only emit RESULTs |
| Executor runs in product repos | Parallel per the engineering contour: each run on its own branch/PR, or its own cloud VM (zero-setup option for parallel runs) |
| Writers across DIFFERENT directions | Fully parallel -- `live/<id>/` paths are disjoint; push races resolve mechanically (see protocol) |
| Applying RESULTs within ONE direction | **One at a time.** Queue them; when each turn arrives, re-read current state and semantically rebase its explicit delta |
| Maintenance on os/** | One session at a time (MAINTENANCE.md already enforces one problem per session) |

Parallel sessions inside one direction are legal (G1 caps the primary bet at <=3 active tasks and owner-set non-paused track slots; `open_calls` is the dispatch frontier) -- only their *applies* serialize.

**Concurrent sessions within one direction -- two hygiene rules** (for a direction running several workstreams at once, e.g. an engine bet plus a parallel visual track):

- **IDs derive from the CALL, never a shared counter.** In track-mode a session id includes its stable call id plus attempt (`canon-c117-a1`); child CALL ids namespace under their issuing call. Parallel children inside one track therefore cannot collide. Legacy single-track state may keep its old prefix/counter until migration.
- **Re-sync before EVERY apply, not just at session start.** A session that writes state more than once re-runs `git fetch && reset --hard origin/main` and re-reads NOW.md before EACH write -- a concurrent same-direction apply may have landed since the last read. Stale packet bases are expected: the writer rebases the RESULT's explicit delta onto that fresh state and preserves current values outside it. Edit only your workstream's own regions; the `updated:` line and the shared decision / pending lists are the hot spots.

Direction tracks are first-class **dispatch**, not git isolation or extra bets: `NOW.tracks` groups mergeable `open_calls`, while the primary track alone owns `NOW.bet` and tasks. Product executors still isolate writes in product branches/worktrees under their repo contract. Create a new Direction only when work needs a genuinely separate mission/charter/root authority; category names such as another game, canon, visuals, or marketing do not decide that split by themselves.

## Mechanics: one worktree per direction

For agent CLI sessions (writer, own-writer sessions), give each direction its own worktree and open it as a separate project in the code assistant:

```bash
git worktree add ../wf-<direction-id> -b wt/<direction-id> origin/main
# remove when direction is paused: git worktree remove ../wf-<direction-id>
```

Root `AGENTS.md`/`CLAUDE.md` travel with every worktree -- sessions there need no extra setup.

`wt/<id>` branches are plumbing, never authority: **state is what is on main.** Chat connectors read main; a session in a worktree resets to origin/main before working.

## Writer apply protocol (per job, in the direction's worktree)

Semantic merge behavior is defined only by `os/adapters/coding-agent.md` Role 1; this file defines serialization and git transport.

```bash
git fetch origin && git reset --hard origin/main   # writer holds no state between jobs
# ...semantic-rebase the RESULT delta, update LOG/history, maintain END_OF_FILE trailers...
git add -A && git commit -m "<direction>[/<track>] <play> <node/task>: <log line>"
git push origin HEAD:main \
  || (git pull --rebase origin main && git push origin HEAD:main)
```

The git rebase-retry resolves races between directions automatically (disjoint paths -> no conflicts). If two applies hit the SAME direction, serialize them: finish one, restart the other from fresh main, and semantic-rebase its RESULT delta. Do not resolve stale state by force or by keeping git conflict-marker sides wholesale. Stop only if the fresh-state rebase exposes an irreconcilable logical collision or invalid packet/`next` CALL; commit/blob drift alone is not a failure.

## Rules

1. One RESULT at a time per direction; across directions -- freely parallel.
2. Never commit direction state to a worktree branch and leave it there: apply = push to main, immediately. Unpushed state does not exist (assume interruption).
3. Track routing lives in `NOW.md`; engineering write isolation lives in the product repo (branches/PRs/cloud VMs per CONTOUR), not in workflow worktrees.

END_OF_FILE: os/adapters/worktrees.md
