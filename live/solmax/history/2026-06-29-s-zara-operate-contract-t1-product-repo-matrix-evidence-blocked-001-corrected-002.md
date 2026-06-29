RESULT s-zara-operate-contract-t1-product-repo-matrix-evidence-blocked-001-corrected-002 (call: c-zara-operate-contract-t1-product-repo-matrix-evidence)
direction: solmax   play: work   node/task: g-zara-operate-contract/t-1

outcome: |
  Corrected RESULT after second writer bounce.

  Product-repo evidence for t-1 is still not done. The prepared acceptance
  matrix content exists in Direction OS history checkpoint, but the Zaratusta
  product repo does not yet contain the target matrix file and no commit/PR
  evidence was found.

  This correction fixes only handoff/protocol mechanics:
  - the old open call c-zara-operate-contract-t1-product-repo-matrix-evidence is
    explicitly removed;
  - a new schema-valid executor engineering call
    c-zara-operate-contract-t1-product-repo-matrix-evidence-002 is explicitly
    added;
  - NOW.next is explicitly replaced with that same new CALL;
  - no writer-core address is used in the CALL schema.

  No live/** files, LOG.md, history files, product-repo files, commits, or PRs
  were changed by this session.

evidence: |
  Packet schema evidence:
  - os/schema/packets.md defines CALL to as session | research | executor.
  - os/schema/packets.md defines executor CALLs as adding repo and
    kind: engineering | mechanical.
  - Therefore the continuation CALL below uses:
    to: executor
    kind: engineering
    repo: github.com/ainazemtsau/zaratusta

  Existing product-repo evidence from the original blocked session remains valid:

  Direction OS / task basis:
  - Active bet: b-zara-operate-contract-002.
  - Product repo: github.com/ainazemtsau/zaratusta.
  - Task t-1 remains active.
  - t-1 requires product-repo evidence mapping W20/A1-A13 to Markdown-readable
    artifacts/checks without choosing W19 HOW.

  Prepared content evidence:
  - Prepared matrix content exists in:
    live/solmax/history/2026-06-28-s-zara-operate-contract-t1-acceptance-matrix-checkpoint-002.md
  - Target product-repo file:
    openspec/changes/g-zara-operate-contract/acceptance-matrix.md
  - The checkpoint states:
    - A-row headings found: A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13.
    - Each row contains Coverage, Verifier rejection condition, and W19 guard.
    - W19 NOT CHOSEN item count: 10.
    - Product-repo evidence was missing at checkpoint time.

  Product repo evidence checked in the original blocked session:
  - GitHub fetch_file:
    repository_full_name: ainazemtsau/zaratusta
    path: openspec/changes/g-zara-operate-contract/acceptance-matrix.md
    result: 404 Not Found
  - GitHub get_users_recent_prs_in_repo:
    repository_full_name: ainazemtsau/zaratusta
    state: all
    result: []
  - GitHub search_prs:
    repository_full_name: ainazemtsau/zaratusta
    query: acceptance-matrix OR W20 OR g-zara-operate-contract
    result: []
  - GitHub search_commits:
    repository_full_name: ainazemtsau/zaratusta
    query: acceptance-matrix W20 A1 A13
    result: []
  - GitHub search_branches:
    repository_full_name: ainazemtsau/zaratusta
    queries: "zara operate contract acceptance matrix", "acceptance", "g-zara"
    result: []

  LOG format evidence:
  - live/solmax/LOG.md uses bullet lines:
    "- YYYY-MM-DD — <summary>. → history/<file>.md"
  - The LOG.md state_change below follows that format.

  Check output:
  - No product-repo check was run, because no product-repo file/commit/branch/PR
    existed to check in the original blocked session.
  - Static checkpoint check output from the prepared-content session remains:
    A1-A13 headings present; Coverage / Verifier rejection condition / W19 guard
    present per row; W19 NOT CHOSEN count 10.

risks: |
  A-row risk:
  - No content risk found in the prepared checkpoint: A1-A13 are present there.
  - Product evidence risk remains hard-blocking: A1-A13 are not yet present in
    the product repo target file because the file is missing.

  W19 risk:
  - No W19 selection risk found in the prepared checkpoint: W19 items are marked
    NOT CHOSEN there.
  - Product evidence risk remains hard-blocking: W19 NOT CHOSEN markers are not
    yet present in product repo because the target file is missing.

  Topic/domain blacklist risk:
  - No generic topic/domain blacklist was found in the prepared checkpoint summary.
  - Product evidence risk remains hard-blocking: the product repo target file is
    absent, so an independent verifier has no product-repo matrix to inspect.

  Protocol risk fixed in this corrected RESULT:
  - Previous corrected RESULT removed the old open_call but did not explicitly
    replace NOW.next, so NOW.next could remain pointing at a deleted call.
  - This corrected RESULT explicitly replaces NOW.next with the new schema-valid
    executor engineering CALL.

state_changes: |
  NOW.md:
  - Keep task t-1 status: active.

  - Replace task t-1 progress_note with:
    "Session s-zara-operate-contract-t1-product-repo-matrix-evidence-blocked-001-corrected-002
     verified that the prepared acceptance matrix content exists in checkpoint
     live/solmax/history/2026-06-28-s-zara-operate-contract-t1-acceptance-matrix-checkpoint-002.md,
     but product repo ainazemtsau/zaratusta does not yet contain
     openspec/changes/g-zara-operate-contract/acceptance-matrix.md and no PR,
     commit, or branch evidence was found. t-1 remains active pending
     schema-valid executor engineering product-repo evidence."

  - In open_calls, remove the item whose id is:
    c-zara-operate-contract-t1-product-repo-matrix-evidence

  - In open_calls, add this item:
    id: c-zara-operate-contract-t1-product-repo-matrix-evidence-002
    to: executor
    kind: engineering
    for: t-1
    issued: 2026-06-29
    note: |
      Product-repo evidence CALL for the prepared W20/A1-A13 acceptance matrix.
      t-1 remains active until product repo ainazemtsau/zaratusta contains
      openspec/changes/g-zara-operate-contract/acceptance-matrix.md and commit
      or PR evidence is returned. Product-repo writes must use the repo's
      allowed writer path; this Direction OS session did not write directly.

  - Replace NOW.next with exactly this CALL:
    CALL c-zara-operate-contract-t1-product-repo-matrix-evidence-002
    to: executor
    kind: engineering
    direction: solmax
    play: work
    node: g-zara-operate-contract
    task: t-1
    repo: github.com/ainazemtsau/zaratusta
    goal: |
      Product repo contains the W20/A1-A13 acceptance matrix and product-repo
      evidence is returned.
    context: |
      Active bet: b-zara-operate-contract-002.
      Product repo: github.com/ainazemtsau/zaratusta.

      Product-repo writes must use the repo's allowed writer path. A normal
      Direction OS session must not write directly to GitHub.

      Prepared content source:
      live/solmax/history/2026-06-28-s-zara-operate-contract-t1-acceptance-matrix-checkpoint-002.md

      Target product-repo file:
      openspec/changes/g-zara-operate-contract/acceptance-matrix.md

      Current evidence from session
      s-zara-operate-contract-t1-product-repo-matrix-evidence-blocked-001:
      - target file fetch returned 404 Not Found;
      - no matching PR was found;
      - no matching commit was found;
      - no matching branch was found.

      Prepared checkpoint self-check:
      - A1-A13 headings present.
      - Each A row contains Coverage, Verifier rejection condition, and W19 guard.
      - W19 NOT CHOSEN item count: 10.
    boundaries: |
      Do not modify Direction OS repo or any non-Zaratusta repo.
      Write only to github.com/ainazemtsau/zaratusta.
      Preserve W20/A1-A13.
      Keep W19 as PLAN agenda, not WHAT.
      Do not add a generic topic/domain blacklist.
      Do not select DB/API/UI/vendor/scheduler/automation/storage engine/exact
      schema or exact layout as contract.
      Do not weaken the rule that Zaratusta writes only to its own workspace/repo
      by default and other repos/directions/projects are read-only sources by
      default.
    done_when: |
      - Product repo contains a Markdown-readable acceptance matrix for A1-A13.
      - Matrix names which artifact/example/check covers each A row.
      - W19 items are explicitly marked not chosen.
      - No generic topic/domain blacklist appears.
      - No DB/API/UI/vendor/scheduler/automation/storage engine/exact schema is
        selected as contract.
      - Product-repo commit or PR evidence is returned.
      - Check output is returned if any check was run.
    return: |
      RESULT with product repo evidence, changed files, commit or PR reference,
      check output if any, and exact notes on any A-row, W19, topic-open,
      write-boundary, owner-approval, or HOW-firewall risk found.
    budget: half focused day
    parent: s-zara-operate-contract-t1-product-repo-matrix-evidence-blocked-001-corrected-002
    surface: any

  LOG.md:
  - Append exactly this line before END_OF_FILE:
    - 2026-06-29 — work t-1 corrected handoff: product-repo matrix evidence still missing; stale executor open call replaced with schema-valid executor engineering call c-zara-operate-contract-t1-product-repo-matrix-evidence-002 and NOW.next updated to the same call. → history/2026-06-29-s-zara-operate-contract-t1-product-repo-matrix-evidence-blocked-001-corrected-002.md

  history/:
  - Add this RESULT as:
    live/solmax/history/2026-06-29-s-zara-operate-contract-t1-product-repo-matrix-evidence-blocked-001-corrected-002.md

captures:
  - Product-repo t-1 is blocked only on schema-valid executor/product-repo materialization evidence; prepared matrix content already exists in Direction OS history checkpoint.
  - Mechanical writer needs open_calls and NOW.next updated together when replacing an in-flight CALL.
  - writer-core is an execution-path constraint, not a Direction OS CALL to-address unless the OS schema is changed in maintenance.

decisions_needed: []

play_check:
  - "1 Recite: done; task t-1 serves active bet b-zara-operate-contract-002 and requires product-repo evidence mapping W20/A1-A13 to Markdown-readable coverage while leaving W19 unselected."
  - "2 Owner inputs (owner): skipped; this is engineering/product-repo evidence, not owner-content the owner personally lives by, operates, or sends as his own."
  - "3 Do the work: blocked; direct GitHub writes are prohibited for this normal session, target product-repo file is missing, and no PR/commit/branch evidence was found."
  - "4 Self-check: done; original done_when is not met because product repo lacks the matrix and no commit/PR/check evidence exists. Prepared checkpoint content appears to cover A1-A13 and W19 NOT CHOSEN, but that is not sufficient product-repo evidence."
  - "5 Close: corrected after writer bounce; state_changes now mechanically remove the old open_call, add a schema-valid executor engineering open_call, and replace NOW.next with the same new CALL."

log: work t-1 corrected handoff: product-repo matrix evidence still missing; stale executor open call replaced with schema-valid executor engineering call c-zara-operate-contract-t1-product-repo-matrix-evidence-002 and NOW.next updated to the same call.

next: |
  CALL c-zara-operate-contract-t1-product-repo-matrix-evidence-002
  to: executor
  kind: engineering
  direction: solmax
  play: work
  node: g-zara-operate-contract
  task: t-1
  repo: github.com/ainazemtsau/zaratusta
  goal: |
    Product repo contains the W20/A1-A13 acceptance matrix and product-repo
    evidence is returned.
  context: |
    Active bet: b-zara-operate-contract-002.
    Product repo: github.com/ainazemtsau/zaratusta.

    Product-repo writes must use the repo's allowed writer path. A normal
    Direction OS session must not write directly to GitHub.

    Prepared content source:
    live/solmax/history/2026-06-28-s-zara-operate-contract-t1-acceptance-matrix-checkpoint-002.md

    Target product-repo file:
    openspec/changes/g-zara-operate-contract/acceptance-matrix.md

    Current evidence from session
    s-zara-operate-contract-t1-product-repo-matrix-evidence-blocked-001:
    - target file fetch returned 404 Not Found;
    - no matching PR was found;
    - no matching commit was found;
    - no matching branch was found.

    Prepared checkpoint self-check:
    - A1-A13 headings present.
    - Each A row contains Coverage, Verifier rejection condition, and W19 guard.
    - W19 NOT CHOSEN item count: 10.
  boundaries: |
    Do not modify Direction OS repo or any non-Zaratusta repo.
    Write only to github.com/ainazemtsau/zaratusta.
    Preserve W20/A1-A13.
    Keep W19 as PLAN agenda, not WHAT.
    Do not add a generic topic/domain blacklist.
    Do not select DB/API/UI/vendor/scheduler/automation/storage engine/exact
    schema or exact layout as contract.
    Do not weaken the rule that Zaratusta writes only to its own workspace/repo
    by default and other repos/directions/projects are read-only sources by
    default.
  done_when: |
    - Product repo contains a Markdown-readable acceptance matrix for A1-A13.
    - Matrix names which artifact/example/check covers each A row.
    - W19 items are explicitly marked not chosen.
    - No generic topic/domain blacklist appears.
    - No DB/API/UI/vendor/scheduler/automation/storage engine/exact schema is
      selected as contract.
    - Product-repo commit or PR evidence is returned.
    - Check output is returned if any check was run.
  return: |
    RESULT with product repo evidence, changed files, commit or PR reference,
    check output if any, and exact notes on any A-row, W19, topic-open,
    write-boundary, owner-approval, or HOW-firewall risk found.
  budget: half focused day
  parent: s-zara-operate-contract-t1-product-repo-matrix-evidence-blocked-001-corrected-002
  surface: any
END_OF_FILE: live/solmax/history/2026-06-29-s-zara-operate-contract-t1-product-repo-matrix-evidence-blocked-001-corrected-002.md
