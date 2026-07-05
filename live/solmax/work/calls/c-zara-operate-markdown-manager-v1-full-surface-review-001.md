CALL c-zara-operate-markdown-manager-v1-full-surface-review-001
to: session
direction: solmax
play: review
node: g-zara-operate-state
goal: |
  Review active bet b-zara-operate-markdown-manager-v1-full-surface-001 for
  closure after t-3 PASS verification and decide the next route.
context: |
  Active bet:
  - b-zara-operate-markdown-manager-v1-full-surface-001
  - node: g-zara-operate-state
  - appetite: 3 focused days
  - kill_by: 2026-07-11

  Completed task evidence:
  - t-1 scaffold:
    github.com/ainazemtsau/zaratusta@dec12c4b1f449e4afdc304fec4d679f67b72f567
    contracts/operating-manager-v1-workspace-state-scaffold.md
  - t-2 surface:
    github.com/ainazemtsau/zaratusta@29562edff935a9d674b99856f2a9a17867b93e8c
  - t-3 verification:
    live/solmax/history/2026-07-05-s-zara-operate-markdown-manager-v1-full-surface-t3-001.md

  t-3 verdict:
  - PASS.
  - All required surfaces verified: inbox/intake, backlog/open loops, current
    operating state, week/day, reviews, decisions/commitments, source/context,
    audit/replay, process mutation, examples/checks, and handback/reporting.
  - W20/A1-A13 preserved.
  - W19/HOW firewall clean.
  - Workspace/effect/source boundaries preserved.
  - No Direction OS write path.
  - Topic-open/source-context handling intact.
  - No generic topic blacklist.
  - No forbidden implementation choice.

  NOW.md next_if_true says:
  - Review this bet for closure, then decide the next route: runtime/dogfood
    or evolution.
boundaries: |
  Do not modify Direction OS repo or product repo.
  Do not implement runtime, dogfood, UI, API, vendor, storage, scheduler,
  automation, spend controls, external integration, or future non-Markdown
  architecture in this review.
  Do not reopen product implementation unless review finds a concrete
  contradiction in t-3 evidence.
  Do not create a Direction OS write path.
done_when: |
  Review determines whether the active bet is done, killed, or needs a repair
  route. If done, review proposes the next route decision using the bet's
  next_if_true/next_if_false and evidence from t-1/t-2/t-3.
return: |
  RESULT with bet closure verdict, evidence, state_changes for NOW/TREE/LOG,
  any owner decisions needed for next route, captures, and next CALL or
  awaiting_decision.
budget: one focused session
parent: c-zara-operate-markdown-manager-v1-full-surface-t3-001
surface: cli

END_OF_FILE: live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-surface-review-001.md
