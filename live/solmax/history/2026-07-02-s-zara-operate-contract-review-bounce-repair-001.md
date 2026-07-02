RESULT s-zara-operate-contract-review-bounce-repair-001 (call: owner-writer-bounce-2026-07-02)
direction: solmax   play: repair   node/task: g-zara-operate-contract/repair

outcome: |
  Writer-bounce repaired in packet form; no repository files were modified by
  this session.

  The previous review RESULT was not mechanically applicable because:
  - it changed live/solmax/TREE.md without a writer-detectable owner_approved
    marker / owner words for the TREE diff;
  - it wrote NOW.next as awaiting_decision + prepared_call..., while current
    writer hygiene requires NOW.next to be either a CALL packet or a one-line
    pointer to a self-contained CALL artifact under work/;
  - its prepared shape CALL goal used procedural wording.

  Corrected repair outcome:
  - keep the review verdict: b-zara-operate-contract-002 met/done;
  - close g-zara-operate-contract in TREE.md with explicit owner_approved marker
    and owner words from the bounce message;
  - close the old active bet in NOW.md;
  - keep the next-bet decision open in NOW.decisions;
  - set NOW.next to one one-line pointer:
    work/calls/c-zara-operate-state-shape-001.md;
  - add that work/ CALL artifact as the self-contained recommended next route,
    activated only if owner chooses D-zara-operate-next-bet-001 option A.

evidence: |
  Writer-bounce evidence from owner:
  - "Writer-bounce: RESULT не применён, файлов не менял и commit не делал."
  - "state_changes меняет live/solmax/TREE.md, но RESULT не несёт
    owner_approved marker / owner words для TREE diff."
  - "NOW.next требует, чтобы next был CALL packet либо one-line pointer на
    self-contained CALL artifact under work/."
  - "если prepared_call_if_option_A_is_approved станет настоящим next CALL, его
    goal лучше переформулировать как outcome, без процедурного 'Shape the
    next…'."
  - "Нужен исправленный RESULT/repair, который явно несёт owner approval для
    TREE closure и приводит NOW.next к текущему writer-формату."

  Owner approval used for TREE closure:
  - owner_approved: true
  - owner_words: "Нужен исправленный RESULT/repair, который явно несёт owner approval для TREE closure и приводит NOW.next к текущему writer-формату."

  Reconstructed current truth from the bounced review and prior verified state:
  - active bet: b-zara-operate-contract-002.
  - node: g-zara-operate-contract.
  - all tasks t-1, t-2 and t-3 are closed before review.
  - t-3 clean independent verification PASS against Zaratusta product repo
    commit 79578ac87c73591000409f9f82a3bb4d0e33aa5b.
  - t-3 verdict dimensions:
    complete PASS; backward_clean PASS; forward_clean PASS; smuggling PASS;
    hard rows A3/A9/A10/A13 PASS/PASS/PASS/PASS; W19 HOW firewall PASS;
    development boundary PASS; AGENTS.md authority boundary PASS.
  - product repo commit 79578ac87c73591000409f9f82a3bb4d0e33aa5b contains
    checks/w20-a1-a13-acceptance-map.md with explicit A1-A13 row mapping and
    W19 Not chosen firewall evidence.
  - no new product repair gap was identified by the bounce. The bounce is a
    Direction OS writer-format/G10 application issue, not a product evidence
    failure.

  Verdict preserved:
  - b-zara-operate-contract-002 is met/done.
  - g-zara-operate-contract is done at the Markdown/GitHub-readable authority
    contract substrate level.
  - this still does not prove durable state, runtime/dogfood, or real daily use.

state_changes: |
  Apply the following exact Direction OS state changes.

  1) live/solmax/TREE.md

  owner_approved marker for this TREE diff:
    owner_approved: true
    owner_words: |
      Нужен исправленный RESULT/repair, который явно несёт owner approval для TREE closure и приводит NOW.next к текущему writer-формату.

  In live/solmax/TREE.md:

  - In top-level owner_approved.evidence, append this list item:
      - '2026-07-02: owner approved TREE closure for g-zara-operate-contract after review verdict met. Owner words: "Нужен исправленный RESULT/repair, который явно несёт owner approval для TREE closure и приводит NOW.next к текущему writer-формату."'

  - For node root.children[g-zara-operate].children[g-zara-operate-contract],
    change exactly:
      status: active
    to:
      status: done

  - Leave this node's appetite, kill_by, goal, done_when and why unchanged as
    historical review context.

  - Do not change g-zara-operate parent status.
  - Do not change g-zara-operate-state, g-zara-operate-runtime or
    g-zara-operate-evolution.
  - Do not add, drop or reorder TREE nodes.

  2) live/solmax/NOW.md

  In live/solmax/NOW.md:

  - Replace the entire active_bet block for b-zara-operate-contract-002 with:
      active_bet:
        status: none
        note: |
          No active bet after repair applied the reviewed closure of
          b-zara-operate-contract-002 on 2026-07-02.

          Review verdict: met/done. g-zara-operate-contract is done at the
          Markdown/GitHub-readable authority-contract substrate level.

          Product evidence:
          - Zaratusta commit:
            79578ac87c73591000409f9f82a3bb4d0e33aa5b
            (`Correct W20 A1-A13 acceptance map boundary`).

          Closed task evidence:
          - t-1 done: product repo evidence maps W20/A1-A13 to Markdown-readable
            artifacts/checks without choosing W19 HOW.
          - t-2 done: smallest Markdown/GitHub-readable operating-manager
            authority contract pack materialized.
          - t-3 done: clean independent verification PASS against commit
            79578ac87c73591000409f9f82a3bb4d0e33aa5b.

          Verified t-3 dimensions:
          - complete: PASS
          - backward_clean: PASS
          - forward_clean: PASS
          - smuggling: PASS
          - hard rows A3/A9/A10/A13: PASS/PASS/PASS/PASS
          - W19 HOW firewall: PASS
          - development boundary: PASS
          - AGENTS.md is repo-local editing guardrail only, not product
            acceptance authority.

          Boundary:
          This does not prove durable state, runtime/dogfood, real daily use,
          storage writer/replay, UI/API/vendor/scheduler/automation, or exact
          schema/layout. Those remain later-child work.

  - Replace:
      route_status: g-zara-operate-contract_verified_pending_review
    with:
      route_status: g-zara-operate-contract_done_next_bet_decision_open

  - Replace the entire top-level tasks list with:
      tasks: []

  - Preserve:
      recurring: []

  - Replace the entire top-level decisions list with:
      decisions:
        - id: D-zara-operate-next-bet-001
          status: open
          created: 2026-07-02
          q: |
            Which Zaratusta operating-manager child should be shaped next after
            g-zara-operate-contract closed as done?
          facts: |
            g-zara-operate-contract review verdict is met/done at the
            authority-substrate level. Product repo commit
            79578ac87c73591000409f9f82a3bb4d0e33aa5b preserves A1-A13 coverage
            and the W19 HOW firewall. This does not prove durable state,
            runtime dogfood or process evolution.
          terms: |
            shape = session that turns a parked node into a bounded active bet.
            state = durable Zaratusta operating context and audit/recovery
              boundary.
            runtime = real owner week/day/intake/planning/review loop.
            evolution = evidence-gated process improvement, not hidden
              self-mutation.
          options:
            - |
              A (recommended): shape g-zara-operate-state.
              why_now: it is the prerequisite for trustworthy memory, audit,
                replay/recovery boundaries and no Direction OS write path before
                runtime dogfood.
              bad_because: delays daily-use/runtime proof by one bet.
            - |
              B: shape g-zara-operate-runtime.
              why_now: attacks daily use and real-depth evidence sooner.
              bad_because: without durable state it risks becoming a chat
                wrapper that cannot preserve decisions/evidence/open loops
                safely.
            - |
              C: shape g-zara-operate-evolution.
              why_now: uses the accepted process/source/context model to design
                process mutation/review mechanics.
              bad_because: premature before the system has durable state or real
                runtime processes to evolve.
          recommendation: |
            A, because the contract creates authority substrate for state and
            runtime. State is the narrowest next risk: Zaratusta must preserve
            context and audit boundaries in its own workspace before a runtime
            loop can be trusted.

  - Preserve:
      open_calls: []

  - In preserved_evidence, append these items if absent:
      - live/solmax/history/2026-07-01-s-zara-operate-contract-repair-t1-t3-state-sync-007.md
      - live/solmax/history/2026-07-02-s-zara-operate-contract-t3-verify-corrected-map-008.md
      - live/solmax/history/2026-07-02-s-zara-operate-contract-review-bounce-repair-001.md
      - live/solmax/work/calls/c-zara-operate-state-shape-001.md
      - github.com/ainazemtsau/zaratusta@79578ac87c73591000409f9f82a3bb4d0e33aa5b
      - github.com/ainazemtsau/zaratusta@79578ac87c73591000409f9f82a3bb4d0e33aa5b/checks/w20-a1-a13-acceptance-map.md

  - Replace NOW.next with exactly this one-line pointer:
      work/calls/c-zara-operate-state-shape-001.md

  3) live/solmax/work/calls/c-zara-operate-state-shape-001.md

  Add this file with exactly this content:

      CALL c-zara-operate-state-shape-001
      to: session
      direction: solmax
      play: shape
      node: g-zara-operate-state
      goal: |
        An owner-approved bounded bet card exists for durable Zaratusta
        operating state and context.
      context: |
        Activation condition:
        - Run this CALL only after owner resolves
          D-zara-operate-next-bet-001 with option A.
        - If owner chooses option B or C, discard this CALL and route the chosen
          node instead.

        Current direction state:
        - live/solmax/CHARTER.md
        - live/solmax/TREE.md
        - live/solmax/NOW.md
        - live/solmax/LOG.md

        Closed prerequisite:
        - g-zara-operate-contract closed as done by
          s-zara-operate-contract-review-bounce-repair-001.
        - Product repo: github.com/ainazemtsau/zaratusta.
        - Verified contract commit:
          79578ac87c73591000409f9f82a3bb4d0e33aa5b.
        - Key product evidence:
          README.md,
          checks/w20-a1-a13-acceptance-map.md,
          checks/markdown-foundation-checklist.md,
          contracts/manager-role.md,
          contracts/workspace-boundaries.md,
          contracts/source-context.md,
          contracts/process-contracts.md,
          contracts/owner-context.md,
          contracts/context-loading.md,
          examples/operating-examples.md,
          docs/decisions/0001-markdown-only-reset.md.

        Contract facts to preserve:
        - W20/A1-A13 is the accepted authority surface.
        - W19 HOW choices remain not chosen.
        - Topic handling is open through process/source/context, not a generic
          domain blacklist.
        - Direction OS and other repos/projects are read-only sources by
          default.
        - Zaratusta writes only to its own workspace/repo unless a future narrow
          integration/procedure is approved.
        - External, irreversible, spend, deletion, message/send or cross-system
          effects require explicit scoped owner approval before effect.

        Review boundary:
        - The closed contract bet proves authority substrate only.
        - It does not prove durable state, runtime/dogfood or real daily use.
      boundaries: |
        Do not modify product repo in this shape session.
        Do not start runtime/dogfood.
        Do not implement UI/channel/API/vendor/scheduler/automation/spend
        controls.
        Do not create any Direction OS write path.
        Do not choose exact database/storage engine/exact schema/exact file
        layout unless shape proves it is the minimal necessary WHAT and the
        owner approves that shape artifact.
        Preserve W20/A1-A13 and the W19 HOW firewall unless a fresh converge
        explicitly changes WHAT.
      done_when: |
        Shape produces one owner-approvable bet card for g-zara-operate-state
        with appetite, kill_by, cut list, lens sweep, riskiest assumption task
        and <=3 half-day tasks. The bet tests the durable-state prerequisite
        without smuggling runtime/UI/API/vendor/scheduler/automation/spend or
        exact schema/layout as contract.
      return: |
        RESULT with owner-approved shape state_changes, exact active_bet if
        approved, and next CALL.
      budget: one focused shape session
      parent: s-zara-operate-contract-review-bounce-repair-001
      surface: chatgpt

      END_OF_FILE: live/solmax/work/calls/c-zara-operate-state-shape-001.md

  4) live/solmax/LOG.md

  Append this line before END_OF_FILE:

      - 2026-07-02 — repair g-zara-operate-contract review writer-bounce: previous review RESULT was not applied; repaired TREE closure with explicit owner_approved marker/owner words, closed b-zara-operate-contract-002 as met after t-1/t-2/t-3 PASS against Zaratusta commit 79578ac87c73591000409f9f82a3bb4d0e33aa5b, and replaced NOW.next with one-line work/ CALL pointer; next-bet decision open, recommendation shape g-zara-operate-state. → history/2026-07-02-s-zara-operate-contract-review-bounce-repair-001.md

  5) live/solmax/history/

  Add this full RESULT as:

      live/solmax/history/2026-07-02-s-zara-operate-contract-review-bounce-repair-001.md

captures:
  - Review/state RESULT templates should not write NOW.next as awaiting_decision under current writer hygiene; use a CALL packet or one-line pointer to a self-contained work/ CALL artifact.
  - TREE closure in review/repair must carry an explicit owner_approved marker and owner words in the RESULT, even when the review verdict itself is evidence-based.

decisions_needed:
  - id: D-zara-operate-next-bet-001
    q: |
      Какой следующий child shaping запускать после закрытия
      g-zara-operate-contract?
    options:
      - |
        A: g-zara-operate-state — рекомендовано.
        Минус: откладывает runtime/dogfood на одну ставку.
      - |
        B: g-zara-operate-runtime.
        Минус: без durable state есть риск chat-wrapper без надёжной памяти и
        audit boundary.
      - |
        C: g-zara-operate-evolution.
        Минус: преждевременно, пока state/runtime ещё не дали живых процессов
        для эволюции.
    recommendation: |
      A: g-zara-operate-state, потому что это самый узкий следующий
      prerequisite после contract layer.

play_check:
  - "1 Name the contradiction: done — previous review RESULT had valid review substance but failed writer mechanics: missing TREE owner_approved marker/owner words and invalid NOW.next shape."
  - "2 Reconstruct: done — reconstructed newest truth from owner bounce, current writer requirements, prior closed tasks, t-3 PASS and verified product commit 79578ac87c73591000409f9f82a3bb4d0e33aa5b."
  - "3 Propose corrected state: done — corrected TREE owner approval marker, NOW active_bet closure, open decision, one-line work/ CALL pointer for NOW.next and outcome-goal shape CALL artifact."
  - "4 Confirm: done — owner requested this repair and supplied approval words: \"Нужен исправленный RESULT/repair, который явно несёт owner approval для TREE closure и приводит NOW.next к текущему writer-формату.\""
  - "5 Friction: skipped — writer correctly enforced existing Role 1/G10 hygiene; template-risk captured, no OS rule change applied here."

log: |
  repair g-zara-operate-contract review writer-bounce: previous review RESULT was not applied; repaired TREE closure with explicit owner_approved marker/owner words, closed b-zara-operate-contract-002 as met after t-1/t-2/t-3 PASS against Zaratusta commit 79578ac87c73591000409f9f82a3bb4d0e33aa5b, and replaced NOW.next with one-line work/ CALL pointer; next-bet decision open, recommendation shape g-zara-operate-state.

next: |
  work/calls/c-zara-operate-state-shape-001.md

END_OF_FILE: live/solmax/history/2026-07-02-s-zara-operate-contract-review-bounce-repair-001.md
