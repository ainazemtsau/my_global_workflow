# Adapter: parallel work & git worktrees

How to run several directions (and several sessions) at once without corrupting state. Core principle (research-backed): **many minds, one pen** — thinking and executing parallelize freely; applying state changes to ONE direction is serialized.

## Concurrency model

| What | Parallelism |
|---|---|
| Chat sessions (ChatGPT/Claude, any play) | Unlimited, across and within directions — they don't write, they emit RESULTs |
| Executor runs in product repos | Parallel per the engineering contour: each run on its own branch/PR, or its own cloud VM (zero-setup option for parallel runs) |
| Writers across DIFFERENT directions | Fully parallel — `live/<id>/` paths are disjoint; push races resolve mechanically (see protocol) |
| Applying RESULTs within ONE direction | **One at a time.** Queue them; two RESULTs editing the same NOW.md must not race |
| Maintenance on os/** | One session at a time (MAINTENANCE.md already enforces one problem per session) |

Parallel sessions inside one direction are legal (G1 still caps ≤3 active tasks; `open_calls` shows who is running) — only their *applies* serialize.

## Mechanics: one worktree per direction

For agent CLI sessions (writer, own-writer sessions), give each direction its own worktree and open it as a separate project in the code assistant:

```bash
git worktree add ../wf-<direction-id> -b wt/<direction-id> origin/main
# remove when direction is paused: git worktree remove ../wf-<direction-id>
```

Root `AGENTS.md`/`CLAUDE.md` travel with every worktree — sessions there need no extra setup.

`wt/<id>` branches are plumbing, never authority: **state is what is on main.** Chat connectors read main; a session in a worktree resets to origin/main before working.

## Writer apply protocol (per job, in the direction's worktree)

```bash
git fetch origin && git reset --hard origin/main   # writer holds no state between jobs
# ...apply state_changes, update LOG/history, maintain END_OF_FILE trailers...
git add -A && git commit -m "<direction> <play> <node/task>: <log line>"
git push origin HEAD:main \
  || (git pull --rebase origin main && git push origin HEAD:main)
```

The rebase-retry resolves races between directions automatically (disjoint paths → no conflicts). A conflict during rebase can only mean two applies hit the SAME direction concurrently — stop, don't force: apply one, re-run the other.

## Rules

1. One RESULT at a time per direction; across directions — freely parallel.
2. Never commit direction state to a worktree branch and leave it there: apply = push to main, immediately. Unpushed state does not exist (assume interruption).
3. Engineering parallelism lives in the product repo (branches/PRs/cloud VMs per CONTOUR), not in workflow worktrees.

END_OF_FILE: os/adapters/worktrees.md
