RESULT s-repair-kernel-t1-state (call: review-feedback-before-merge)
direction: solmax   play: repair   node/task: g-kernel/t-1

outcome: |
  NOW.md repaired: g-kernel/t-1 is no longer owner-blocked on repo access.
  The Zaratusta product repo exists remotely, has green CI, and contains the W0 setup scaffold.
  The old blocked attempt remains in history as an earlier failed executor environment.

evidence: |
  - `gh repo view ainazemtsau/zaratusta` returned private repo
    https://github.com/ainazemtsau/zaratusta with default branch `main`.
  - GitHub Actions run 27591433389 succeeded for
    18d74b1114428be8df5ece48bf6d89f3b2776a75:
    https://github.com/ainazemtsau/zaratusta/actions/runs/27591433389
  - Local product clone `C:\projects\zaratusta-product` is clean at commit
    `18d74b1 Tighten RESULT deliver gate`.
  - Direct Windows path probe: `C:\projects\Zaratusta` exists, but `git -C
    C:\projects\Zaratusta status` fails with "not a git repository"; this narrows the path issue
    to a local-path conflict, not a missing path.
  - Review feedback identified the stale blocker in NOW.md before merge.

state_changes: |
  NOW.md:
    - t-1.status: blocked -> done.
    - Remove t-1.blocked_reason and t-1.unblock_condition.
    - c-work-kernel-t1.status: blocked -> done.
    - Replace c-work-kernel-t1 note with setup evidence pointer:
      `ainazemtsau/zaratusta` exists, CI green on 18d74b1114428be8df5ece48bf6d89f3b2776a75,
      W0 scaffold/gates/OpenSpec exist.
    - Replace product-repo-access decision with two narrowed decisions:
      accept or reject TypeScript/Node 22 stack; decide whether to keep product clone at
      `C:\projects\zaratusta-product` or reclaim `C:\projects\Zaratusta`.
    - next -> awaiting_decision for those two owner decisions before t-2.

  LOG.md:
    - Add newest-first:
      "2026-06-16 — repair g-kernel/t-1: stale blocked state replaced with DONE after
      Zaratusta repo/CI evidence; local path conflict narrowed to an owner decision.
      → history/2026-06-16-s-repair-kernel-t1-state.md"

  os/engineering/profiles/:
    - Add `typescript-node.md` stack profile returned by the executor setup result.

captures:
  - "Repo-scoped MCP servers with external write permissions should stay out of shared `.codex/config.toml`; user-local config is the safer place."
decisions_needed:
  - q: "Accept TypeScript/Node 22 as the W0 setup stack?"
    options: ["Accept TypeScript/Node 22", "Reject and rerun setup with another stack"]
    recommendation: "Accept; the repo setup and CI are already green on this stack."
  - q: "Where should the local product clone live?"
    options: ["Keep C:\projects\zaratusta-product", "Move existing vault and reclone to C:\projects\Zaratusta"]
    recommendation: "Keep `C:\projects\zaratusta-product` unless exact path alignment matters."
play_check:
  - "1 Name the contradiction: done — NOW.md says repo/path access is blocked; current evidence says remote repo and CI exist, while the Windows path exists but is not a git repo."
  - "2 Reconstruct: done — newest evidence from GitHub repo/CI and local product clone outranks the older blocked executor attempt."
  - "3 Propose corrected state: done — t-1 done; c-work-kernel-t1 done; blocker narrowed to stack/path owner decisions."
  - "4 Confirm: done — owner requested applying the review corrections before merge: \"Нужно поправить перед мержем.\""
  - "5 Friction: skipped — no OS rule defect found; this was stale state after a later successful executor run."
log: "repair g-kernel/t-1: stale blocked state replaced with DONE after Zaratusta repo/CI evidence; local path conflict narrowed to an owner decision"
next: |
  awaiting_decision:
    owner should accept or reject the TypeScript/Node W0 stack and choose whether to keep
    the product clone at `C:\projects\zaratusta-product` before launching t-2.

END_OF_FILE: live/solmax/history/2026-06-16-s-repair-kernel-t1-state.md
