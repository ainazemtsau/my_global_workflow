RESULT s-review-launch-control-demo-program-v0-binding-005 (call: owner-direct-demo-program-v0-binding-g5-005-20260723)
direction: indie-game-development   track: launch-control   play: review   node/task: g-b847/demo-program-v0-binding-g5-005
outcome: |
  REFUTED — binding fresh G5 нашёл material counterexamples в exact DRAFT `demo-program-v0 correction-005` из commit `bff423dfdeee7b729e5a64ab50ba49bdd7a742f7`, artifact blob `5c3b21312aecffe0a19462373018b902a7b715ef`. Исправленные локальные predicates C2/C4 выдержали опровержение, но весь DRAFT не выдержал. Stage 4 не открыт; active Program Model, Demo Control Room, Brief/slice/route, BUILD и candidate не изменены.

  ### Material counterexample 1 — C3 сохраняет дерево от superseded Brief generation

  1. Materialize final Brief `B1` и D0 reconciliation `R1`; после этого owner даёт exact clean `ACCEPT(B1,R1)`. C2 законно эмитит current `accepted_brief_version=B1`.
  2. Materialize Demo Experience Tree `T1`, derived from `B1`; exact owner/Canon receipt принимает `T1`, все edge pointers присутствуют. C3 законно закрывается по своему literal proof.
  3. Materialize materially different Brief `B2` и reconciliation `R2`; owner даёт exact clean `ACCEPT(B2,R2)`. По собственным правилам C2 `B2` atomically supersedes `B1` и остаётся единственным current C2 token.
  4. Старый C3 receipt для `T1` всё ещё удовлетворяет каждому literal C3 proof component: `accepted tree version`, exact positive owner/Canon receipt и edge pointers. В proof нет identity consumed `accepted_brief_version=B1`, а также нет descendant invalidation при supersession C2. Hard prerequisite `C2` теперь формально green за счёт `B2`, поэтому он не отличает stale `T1` от дерева, derived from current `B2`.
  5. После этого можно materialize slice `Q1` из stale `T1`, получить clean exact C4 `SELECT(Q1)` и продолжить `C4→C5` и downstream graph.

  Нарушенный causal invariant: current chain должен быть `current accepted Brief → tree accepted for that exact Brief → slice selected from that exact current tree`. DRAFT хранит current generation внутри C2/C4, но не переносит parent-generation identity через C3. Это concrete false path, а не просьба о дополнительной детализации.

  ### Material counterexample 2 — P2 допускает двух синхронных наблюдателей вместо causal co-op

  Let exact S9 build run on named players `A/B` and physical PCs `M1/M2`. Both have clean installs; both join one named session. `A` alone performs every outcome-changing input, while `B` is a spectator. Both clients receive the same authoritative result/digests; repeat run and relaunch match; an intentionally corrupted digest produces the required loud divergence capture. Every literal P2 proof item is present: S9 hash, per-PC clean-install/entitlement evidence, player/machine IDs, session ID, repeat result/digests, relaunch and deliberate divergence negative control. Yet P2 observable is false because player 2 never causally changes the outcome.

  A second false valuation uses cached/dirty session state for the P2 session: P2 proof requires clean installs but not clean sessions. A separate S10 clean-session run can supply its own receipt because neither S10 nor S0 binds that clean-session evidence to the P2 session ID. No P3/P4/P6/P7/T7/T8 receipt adds an intervention by named player `B` on `M2` in the P2 session. The false token therefore remains consumable along `P2→S10→S11/S12→S13→S14→S15→S0`.

  Нарушенный causal invariant: two-player proof требует двух игроков на двух физических ПК в clean install/session, где второй игрок причинно меняет результат; shared transport state/digests сами по себе доказывают synchronization, а не cooperation.

  ### Whole-DRAFT verdict matrix

  - REFUTED locally: `C3`, `P2`.
  - SURVIVED locally: `S0–S15`; `P0`, `P1`, `P3–P8`; `D0`; `C0–C2`, `C4–C5`; `T0–T8`. Downstream outcomes are not counted again as REFUTED solely because they can consume one of the two defective upstream tokens.
  - `C2` SURVIVED: only post-materialization exact current `ACCEPT` emits its Brief token; REVISE without acceptance, REJECT, BLOCKED, absent/generic/ambiguous/contradictory/prospective/replayed/stale words and later current negative dispositions emit or preserve nothing.
  - `C4` SURVIVED: only post-materialization exact current `SELECT`/`ACCEPT` of the complete slice/manifest/exclusions/flags emits authority; all attacked negative, stale, replayed and inconsistent cases fail closed.
  - `C3` generic-word guard itself SURVIVED: line 18 requires a positive exact actor/subject-bound receipt. C3 is REFUTED only for missing current C2-generation lineage.
  - `S2` and `S6` SURVIVED generic-word attacks: each still requires an exact positive actor/subject/route action plus first-hand matching readbacks.
  - `P1` remains separate from both P2 witnesses and uninstructed. A `FAIL` disposition was not counted as a separate refutation because the literal shared positive-success invariant already forbids a negative disposition from emitting a positive token.

  ### Structural, scope, route and source checks that survived

  - Independent root parsing: 41 outcomes, exactly nine ordered fields each (`369` fields total); 133 unique hard dependency edges and 133 reverse-consumer edges; no duplicates, missing refs or mirror gaps; DAG; sources `[S1,C0,T0]`; terminal `[S0]`; all 41 outcomes reach S0.
  - correction-004→005 changes exactly four of 369 node fields: C2 observable/proof and C4 observable/proof; all 41 titles, the other 365 fields and the graph are unchanged.
  - October stays `OCTOBER_PRIMARY`. February is an inactive deadline/eligibility envelope until an exact future owner switch; elapsed time or failed October proof cannot switch it, and no detailed February plan is required now.
  - Final Brief/slice do not gate `P0→D0`; Canon can work in parallel and no scripted hook is mandatory.
  - Gas and world-change implementation are required only for their actual `SELECTED` slice flags; `NOT_SELECTED` uses explicit zero-consumer bypass receipts.
  - Base game remains unreleased through the exact selected Next Fest close. Honest UNKNOWN future Steam/account/build/player facts, absence of a chosen Brief/slice/hook, and absence of a detailed February plan were not treated as defects.
  - Official Steam checks survived: October `2026-10-19 10:00 PDT`→`2026-10-26 10:00 PDT`, registration `2026-08-31 23:59 PDT`, required items `2026-10-05`; February `2027-02-22 10:00 PST`→`2027-03-01 10:00 PST`, registration `2027-01-10 23:59 PST`, required items `2027-02-08`; review is typically 3–5 business days with at least seven planned; build review is not QA; 09:30 is correctly an operational target derived from the official 30-minute recommendation, while 10:00 is the event gate.

  ### Review harvest by CHARTER lens

  - Commercial / traction: Steam funnel and October-first route survive, but no public/program authority may consume this DRAFT while its proof chain admits false tokens.
  - Core gameplay depth: a matching result/digest is not evidence that the second player changed the outcome.
  - Co-op-first: the decisive new learning is to test named-player intervention, not mere two-peer presence.
  - Technical feasibility: two-PC identity, clean install, relaunch and divergence checks survive; causal participation and same-session cleanliness need a proof boundary, not an implicit reading.
  - Scope / production: repeated local repairs have left cross-generation semantics distributed across prose. The lower-risk next move is to simplify the model into fewer version-bound proof envelopes before another candidate.
  - Audience workflow: the separate uninstructed clarity participant remains a valid distinct role; this review creates no audience task or Stage 4 action.

  No forecast was recorded for this exact DRAFT review, so no optimistic/pessimistic/wrong-mechanism/wrong-timeline forecast verdict is invented. There is no active-bet cut list in this exact-candidate scope, so no add-back ratio is fabricated.

  New material error classes are established: descendant-generation lineage leakage and insufficient same-session causal co-op proof. Per owner instruction, correction-006 is not created automatically. The leg stops for the owner choice recorded below.
evidence: |
  [ESTABLISHED fresh authority] After a fresh `git fetch origin --prune`, `origin/main` and `origin/wt/indie-game-development` both resolved to publication receipt commit `ed76a48413fedadbb2d8882ea74271fd6b3c3df2`; local HEAD was the same. Tracked status was clean. User-owned untracked `.claude/settings.local.json` was left untouched and untracked.

  [ESTABLISHED exact target] Candidate `bff423dfdeee7b729e5a64ab50ba49bdd7a742f7` is the direct parent of receipt commit `ed76a48413fedadbb2d8882ea74271fd6b3c3df2` and an ancestor of fresh `origin/main`. At the candidate, `live/indie-game-development/history/2026-07-23-s-research-launch-control-demo-program-v0-correction-005.md` is exact blob `5c3b21312aecffe0a19462373018b902a7b715ef`; fresh authority contains the same artifact object.

  [ESTABLISHED binding independence] This root chat is a separate fresh physical session from candidate generation, correction and publication. Fourteen independent read-only subagent passes were used only as a non-binding pre-pass, including adversarial rebuttals of candidate findings. Root independently reread the exact object/current authority, reproduced the mechanical checks and formed the binding counterexamples and binary verdict. Same-family/model identity was not used as a gate.

  [PROVED C3 counterexample pointers] Exact candidate lines 330–356 define C2 atomic current-generation supersession, C3 proof without `accepted_brief_version`, and C4 proof without accepted parent-tree generation identity. Lines 14–18 define positive token/current-owner semantics but add no recursive descendant invalidation. Lines 542–576 test only C2/C4 local current-generation transitions. `live/indie-game-development/work/launch-control/demo-control-room.md:108,139-150` separately requires fresh reads and naming stale work, confirming that stale lineage matters but does not add the missing C3 proof field to this DRAFT.

  [PROVED P2 counterexample pointers] Exact candidate lines 231–235 require causal second-player contribution and clean sessions in the observable but omit both from the literal P2 proof. Lines 242–290 prove lifecycle/transport/local control/network agreement without binding a named second-player intervention to the P2 session. Lines 132–136 add clean-session evidence at S10 but no same-session link or named second-player causal intervention; lines 22–26 forbid build/route/witness mixing but not session mixing. Control Room `:47-64,195-222,248-250,280-281` requires meaningful two-machine co-op and a distinct uninstructed clarity player.

  [PROVED mechanical] Root parser results: `nodes=41`, `ordered_fields=41×9`, dependency edges=`133`, consumer edges=`133`, duplicate refs=`[]`, missing refs=`[]`, mirror gaps=`[]`, acyclic=`true`, topo count=`41`, sources=`[S1,C0,T0]`, terminal=`[S0]`, unreachable-to-S0=`[]`.

  [ESTABLISHED authoritative state] `AGENTS.md`, `.agents/skills/direction-os/SKILL.md`, `.agents/skills/parallel-verify/SKILL.md`, `os/KERNEL.md`, `os/plays/review.md`, `os/adapters/coding-agent.md`, `os/schema/packets.md`, `CHARTER.md`, `TREE.md`, `NOW.md`, the exact candidate, prior correction/binding evidence and declared knowledge/work authorities were read before verdict.

  [ESTABLISHED official Steam primary sources]
  - https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/2026october?l=english
  - https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/feb_2027?l=english
  - https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest?l=english
  - https://partner.steamgames.com/doc/store/review_process?l=english
  - https://partner.steamgames.com/doc/store/releasing?l=english
  - https://partner.steamgames.com/doc/store/application/demos?l=english

  [LIMIT] This result judges only the exact DRAFT. It does not publish or repair the candidate, open Stage 4, run BUILD, select/accept a Brief or slice, switch the route, invent future facts, mutate hot state or touch a product repository.
state_changes: |
  1. Add this full RESULT exactly once at `live/indie-game-development/history/2026-07-23-s-review-launch-control-demo-program-v0-binding-005.md` with its exact END_OF_FILE trailer.
  2. Append the exact `log` line below exactly once to `live/indie-game-development/LOG.md` immediately before its current END_OF_FILE trailer.
  3. Preserve every other tracked file and semantic field unchanged after fresh-state rebase. In particular: no changes to NOW/TREE/CHARTER/knowledge, statuses/open_calls/tracks, Demo Control Room, active Program Model, candidate or publication receipt; no Stage 4, BUILD, correction-006, Brief/slice/route verdict, publication or product-repo action. Leave user-owned untracked `.claude/` untouched.
captures: []
decisions_needed:
  - id: d-demo-program-v0-post-binding-005-001
    q: |
      Как продолжить после двух новых material error classes в exact correction-005?
    options:
      - Упростить модель: свести current Brief→tree→slice и two-player causal proof к меньшему числу version-bound proof envelopes, затем сформировать новый candidate отдельным leg.
      - Продолжить точечное исправление: отдельно авторизовать correction-006 для C3 descendant lineage и P2 same-session causal proof, сохранив остальную 41-outcome модель.
    recommendation: |
      Упростить модель. После нескольких correction-leg новые false-token paths возникают на стыках локальных predicates; меньшее число явно version-bound envelopes снижает риск ещё одного patch-on-prose цикла. Если важнее сохранить всю текущую структуру, второй вариант остаётся допустимым, но требует отдельного fresh correction-leg.
play_check:
  - 1 Verify by refutation: done — exact fresh target and all 41 outcomes were attacked; isolated C2/C4 fixes and declared route/scope/Steam guards survived, while reproducible C3 and P2 false-token paths establish REFUTED. No forecast existed for this exact DRAFT review.
  - 2 Harvest per lens: done — all six CHARTER lenses were answered; the material cross-lens effect is that co-op causality and current-generation lineage must be proof-bound before any commercial/public authority.
  - 3 Update the tree: skipped by explicit owner boundary — this exact binding leg authorizes only history/LOG; no owner-approved TREE diff exists, and no hot-state edit is invented.
  - 4 Add-back check: skipped with reason — this exact-candidate review has no active-bet cut list; no missed-cut ratio is fabricated.
  - 5 Knowledge: skipped by explicit owner boundary — durable learning is retained in this binding history RESULT only; no knowledge file is authorized.
  - 6 Select next: done as owner decision — options are simplify the model or authorize a separate correction-006; simplify is recommended. Neither option is executed and no Stage 4/BUILD CALL is opened.
  - 7 Close: done — one binding RESULT returns REFUTED, history/LOG-only state changes and an awaiting owner choice; no candidate correction, publication, Stage 4 or BUILD occurs.
log: 2026-07-23 · s-review-launch-control-demo-program-v0-binding-005 · review · launch-control · g-b847/demo-program-v0-binding-g5-005: binding fresh G5 REFUTED exact DRAFT bff423df/blob 5c3b2131 because C3 can preserve a tree from a superseded Brief generation and P2 can emit on spectator or dirty-session evidence without a same-session second-player causal intervention; isolated C2/C4 gates, the 41×9 mirrored 133-edge DAG and route/scope/Steam guards otherwise survived; Stage 4, BUILD and correction-006 remain closed pending owner choice. → history/2026-07-23-s-review-launch-control-demo-program-v0-binding-005.md
next: |
  awaiting_decision d-demo-program-v0-post-binding-005-001. No correction-006, Stage 4, BUILD or publication CALL is opened until the owner chooses simplify-model or continue-correction.

END_OF_FILE: live/indie-game-development/history/2026-07-23-s-review-launch-control-demo-program-v0-binding-005.md
