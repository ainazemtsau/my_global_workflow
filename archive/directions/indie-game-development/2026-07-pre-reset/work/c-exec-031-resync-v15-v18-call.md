CALL c-exec-031
to: executor
kind: engineering
direction: indie-game-development
node: g-9c41
repo: C:\projects\Unity\GasCoopGame_dev
surface: cli
goal: |
  GasCoopGame's engineering run-contract + deliver gate catch up from synced_contract_version 14 to 18 in one pass,
  so c-exec-021 (Sc-reactions) fires on a current base and its review is gated by the CURRENT rules. STRICTLY
  ADDITIVE — no existing green gate weakened; every currently-delivered leg still delivers (grandfather if a new
  gate would retro-fail one). Four contract versions, each wired mechanically (a gate + a seeded-miss, not prose):
    v15 review-scope-split · v16 tool-unavailable-STOP · v17 source-scan-is-never-behavior-evidence + scanner ban ·
    v18 cited-artifact existence. Then bump validation.config synced_contract_version 14 -> 18.

context: |
  - Owner chose the §Re-sync leg NOW (2026-07-04), after the infra debts (DF-2/DF-10/DF-5/RESULT-per-leg) cleared,
    so c-021 starts clean. Base = GasCoopGame main @bbe86eb (post c-exec-030 merge; synced_contract_version=14).
  - The §Re-sync items are SPECIFIED VERBATIM in the workflow repo's os/engineering/CONTRACT_VERSION log (entries
    v15/v16/v17/v18, each with a "§Re-sync OWED: GasCoopGame ..." clause) + the matching VALIDATION.md paragraphs
    (§Review-evidence (iii) for v15; §Behavior evidence by venue for v17; §Cited-artifact existence for v18) and
    PROJECT_SETUP §Strong-check clauses. MIRROR those, not free interpretation. Summary of what to wire:
    * v15 (review-scope-split): the deliver review-file check tools/review-check.ps1 gains the `scope` in
      {in-scope | class-sibling} + `site` (file:line) columns. An IN-SCOPE finding gates
      ({fixed|refuted|owner-ack}); a CLASS-SIBLING carries a `routed <ref>` pointer + does NOT gate; a class-sibling
      with NO routing pointer FAILs; the MECHANICAL anti-dodge — a class-sibling row whose `site` file is INSIDE the
      change's diff FAILs (a git-diff name-membership test); the v14 fix-class-closure sweep may close an OUT-OF-DIFF
      sibling as `n/a because out-of-scope, routed <ref>`. Seeded-miss: an uncountered class-sibling RED, an
      in-diff-site class-sibling RED, a well-formed case GREEN. Kept wired into check.ps1 -Deliver.
    * v16 (tool-unavailable-STOP): mirror into AGENTS.md (the Step-3 run-contract): a required tool/harness the plan
      depends on going UNAVAILABLE (engine Editor down / needed MCP disconnected / headless license absent) is a
      mandatory STOP + owner-contact NAMING the tool, never a workaround/crutch/silent scope-narrowing; any
      exception stands ONLY on the owner's EXPLICIT written owner-ack in chat. Run-contract prose (no new
      deliver-script) — the AGENTS.md line MUST land.
    * v17 (source-scan-is-never-behavior-evidence + self-written-scanner ban): mirror into AGENTS.md the rule —
      engine/shader/render/scene behavior = a real EditMode/PlayMode run OR a live-engine MCP query; engine-free
      logic = real headless tests; look = owner-eye; a static source-text scan is NONE of these; self-written source
      scanners/parsers FORBIDDEN as behavior evidence; the ONLY legal text check is a declared wiring-smoke
      (File.Exists + trivial substring, NO acceptance property / NO negative control / NO property test); a
      scan-oracle's fix is DELETION.
  - ⚠ v17 SCANNER CLASSIFICATION (load-bearing — do NOT get this wrong): the ban targets scanners used as
    PRODUCT-BEHAVIOR evidence. tools/hygiene.ps1, tools/benchmark-discoverability-check.ps1,
    tools/excluded-category-check.ps1 are self-written source-scanners of the TOOLING / TEST-SUITE-HYGIENE family
    (they assert a test is present/compiled/correctly-tagged, NOT product behavior) — v17 PERMITS them. Do NOT
    delete or weaken them; the AGENTS.md v17 text must NAME this tooling-hygiene carve-out explicitly.
  - ⚠ v17 VISUAL SCAN-TESTS = OUT OF SCOPE (cross-track boundary): four BEHAVIOR-evidence source-scanners on main —
    tests/GasCoopGame.Core.Tests/GasVisual/{GasLightBinderScanTests, GasUberShaderScanTests, GoodSampleScanTests,
    SingleCustomEditorScanTests}.cs — ARE banned by v17 and should be DELETED, but they are VISUAL-track files owned
    by c-visual-005 (the clean source-scan retirement re-derive, s-work-046). Do NOT touch them here (a concurrent
    delete would collide with c-visual-005). Instead add them to a `source_scan_ban_grandfathered_pending_c-visual-005`
    list in validation.config (owner-governed) so the bump to 18 is HONEST — the RULE lands now; the visual deletion
    is delegated + tracked. c-visual-005 removes both the files and the grandfather entry.
    * v18 (cited-artifact existence): wire into the ALWAYS-RUN RESULT gate tools/result-check.ps1 (the per-leg gate
      c-exec-030 extracted) — for EVERY leg, each docs/reviews/review-*.md / docs/adr/*.md path the closing report
      (RESULT / docs/results/<id>.md) CITES, rooted in the repo's OWN docs/ tree, must EXIST at HEAD; a dangling
      citation FAILs at whatever commit -Deliver runs. ORTHOGONAL to v10 (v10 keys on the frozen-folder id; this on
      the report's cited paths). A report that OMITS the citation is untouched; a cross-repo path (escaping the repo
      root / a bare os/ ref) is OUT of scope; existence-only (prose-only claim + empty-stub file are NOT caught — no
      content scanner, v17). Seeded-miss (independently authored) must PIN: (a) a same-commit-added ADR citation
      PASSES, (b) a prior-leg already-landed review citation PASSES, (c) a dangling review citation REDs, (d) a
      RESULT omitting the citation PASSES. See VALIDATION §Cited-artifact existence for the exact rule.
  - Contour = the c-024/026/028/030 tooling-leg pattern: do NOT create a frozen openspec/changes/c-exec-031-*/
    folder (that triggers the per-change battery; N/A by absence). The leg's own evidence = an independent RED
    test-author FIRST on every new assert/seeded-miss + a fresh-session G5 + ADR-P-0008 + a
    docs/reviews/review-c-exec-031-*.md record.
  - Toolchain (HARD): Windows PowerShell 5.1 ONLY (no pwsh/PS7 on PATH); ASCII-only in BOM-less .ps1.

boundaries: |
  - INFRA/RUN-CONTRACT ONLY: tools/** (review-check.ps1, result-check.ps1, check.ps1 wiring), validation.config,
    AGENTS.md (run-contract sections), docs/adr/**, docs/reviews/**. NO Core/Field/sim code, NO goldens, NO tick
    path, NO product FEATURE test. Engine worktree GasCoopGame_dev — NEVER dev_2.
  - Do NOT touch the visual track: the 4 GasVisual/*ScanTests.cs STAY (grandfathered pending c-visual-005), NOT
    deleted here. Do NOT touch Render/GasVisual/**, GasUber, or any dev_2 file.
  - PRESERVE the tooling-hygiene scanners: hygiene.ps1, benchmark-discoverability-check.ps1,
    excluded-category-check.ps1 are PERMITTED under v17 — do NOT delete or weaken.
  - ADDITIVE / no-weaken (hard invariant): every existing green gate stays green; every currently-delivered leg
    still delivers. If a new gate would retro-fail an already-delivered leg -> GRANDFATHER it in validation.config
    (owner-governed), never loosen.
  - STOP + surface as an owner decision (do not silently restructure) if: a §Re-sync item cannot be wired without
    touching a Core/sim/visual/dev_2 file; OR the v15 review-scope wiring would change an existing green review
    file's disposition; OR the v18 cited-existence would retro-fail an already-delivered leg's committed RESULT
    (grandfather with owner-ack instead).

done_when: |
  Each of v15/v16/v17/v18 MECHANICALLY wired + seeded-miss self-tested (not prose), and validation.config
  synced_contract_version bumped 14 -> 18 with a log note:
  - v15: tools/review-check.ps1 accepts `scope`+`site`; in-scope gates, class-sibling needs `routed <ref>`
    (missing -> RED), class-sibling `site` INSIDE the diff -> RED; seeded-miss proves BOTH RED controls + a GREEN
    well-formed case; kept wired into check.ps1 -Deliver.
  - v16: AGENTS.md Step-3 run-contract carries the tool-unavailable-STOP + explicit-written-owner-ack clause
    (presence-verified; no deliver-script).
  - v17: AGENTS.md carries the source-scan-ban rule + names the TOOLING-HYGIENE carve-out
    (hygiene/benchmark-discoverability/excluded-category PERMITTED) explicitly; the 4 GasVisual/*ScanTests.cs are
    listed in validation.config source_scan_ban_grandfathered_pending_c-visual-005 (owner-acked cross-track
    delegation). If a deliver check is added for the ban it carries a seeded-miss AND passes on current main.
  - v18: tools/result-check.ps1 gains the cited-artifact-existence check (every leg; repo-rooted docs/reviews +
    docs/adr; dangling citation -> RED; omitted citation -> PASS; cross-repo/prose/stub out of scope) with the
    4-case independently-authored seeded-miss above; kept wired into check.ps1 -Deliver.
  - synced_contract_version 14 -> 18 with a log note recording the v15/v16/v17/v18 mirror + the
    pending-c-visual-005 grandfather.
  Closure: tools/check.ps1 -Deliver GREEN end-to-end on main as-is (all new self-tests pass AND every currently-
  delivered leg still delivers — grandfather if needed, transcript attached); ADR-P-0008 records the §Re-sync + the
  pending-c-visual-005 delegation; a FRESH-session G5 refutes that each new seeded-miss / RED control truly goes
  RED-without-fix / GREEN-with-fix; docs/reviews/review-c-exec-031-*.md record. INDEPENDENT RED test-author FIRST on
  every new assertion/seeded-miss.

return: |
  RESULT routed HOME to indie-game-development/g-9c41 (per contract v18, cite ONLY artifacts committed at the
  delivered tip): commits + the full check.ps1 -Deliver transcript (green, showing the new v15 + v18 self-tests),
  the edited scripts (review-check.ps1, result-check.ps1, check.ps1 wiring), AGENTS.md run-contract diffs (v16/v17
  clauses + the tooling-hygiene carve-out), validation.config (14->18 + the pending-c-visual-005 grandfather),
  ADR-P-0008, the fresh-session G5 record. dev->main merge + push OWNER-GATED. next = return to g-9c41: the repo is
  on v18 -> the road resumes at c-exec-021 (Sc-reactions) — re-harden + fill §PENDING, fire in a fresh owner-present
  PLAN.

budget: |
  One medium infra/run-contract leg (review-check.ps1 + result-check.ps1 + AGENTS.md + validation.config + an ADR;
  four contract versions but all mechanical mirrors of specified items). Honor the STOP-clauses rather than
  silently restructuring, touching the visual track / Core, or weakening a gate.

parent: s-work-051

END_OF_FILE: live/indie-game-development/work/c-exec-031-resync-v15-v18-call.md
