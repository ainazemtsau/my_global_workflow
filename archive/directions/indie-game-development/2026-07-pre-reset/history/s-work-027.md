# s-work-027 — work (g-9c41 / S2b): fix the canon ADR citation + author + harden the S2b CALL (c-exec-018)

Date: 2026-06-28
Play: work (resolve the ADR finding + author the next executor CALL); writer-after-RESULT
Direction / node / task: indie-game-development / g-9c41 / S2b
Job: session + writer (owner «да» to both: fix the canon ADR citation + write the c-018 order)

## outcome

Two coupled deliverables on owner «да»:
1. **Canon ADR citation FIXED** (d-adr-lockstep-citation-001 ANSWERED). The input-lockstep lock is now correctly cited as
   **ADR-0002** («Network determinism: lockstep over FishNet, input-bus only») throughout the canon; the repo's ADR-0010
   (test-sandbox) is no longer mis-cited as the lock. 5 surgical edits + one authoritative §1 correction note, grounded
   first-hand in GasCoopGame `ADR-0016` (the S2a retirement ADR, which records the same correction) + `ADR-0002`.
2. **S2b executor CALL c-exec-018 AUTHORED + adversarially HARDENED** → work/c-exec-018-call.md. The load-bearing lockstep
   loopback determinism proof on the clean post-S2a base (GasCoopGame main @2e24a24).

## evidence

- Canon edits (5): §1 (authoritative correction note: lock=ADR-0002, ADR-0010=test-sandbox, host-broadcast detour=
  ADR-0003/0004(+0005-part,+0008) retired ADR-0016/S2a) + the §2-line-12 lock-change rule + Факт-1 + §6 hangar + §7 burial +
  §9-map c-exec-004 banner. Grounded in GasCoopGame ADR-0016 («Read every canon/CALL "ADR-0010 (input-lockstep)" as
  ADR-0002») + ADR-0002 (accepted 2026-06-13).
- c-018 CALL: six KERNEL §4 fields + ведро + the ADR-0002 lock + the RNG-control drop + chunk-span S4-deferral +
  §9.5 membership/spec-silence + auto-coverage-seam + G0-frozen + END_OF_FILE.
- Hardening: workflow wf_e4074544-feb — 28 agents, 6 adversarial lenses (determinism / lock-ADR / scope / verifiability /
  drift / plan-completeness) → per-finding refute-verify → synthesis. 16 raised → 10 survived → **1 must-fix + 6 should-fix**
  folded; ZERO lock-change, ZERO re-design (all text-only).
  - MUST-FIX (real bug it caught): done_when 4(c) demanded a RED control against a region-fold-order seam that does NOT
    exist at S2b (the live MeaningChecksum folds region_id as a per-cell VALUE, no per-region rollup loop — that's S4) →
    an unfalsifiable "must-trip"; re-scoped to recorded spec-silence (mirroring the RNG drop).
  - SHOULD-FIX: awake-queue→active-front control (contradiction with the not-yet-built §9.5 list); S5 boundary added;
    §9 шов-5 bitmap trip-wire restored; 3 stale canon line-cites (57→58, 106→107, 78→79 — shifted by THIS session's own §1
    edit) → name-anchored (drift-proof); RW5 full path added.

## play_check

1. Recite — DONE. Owner «да» = (a) fix the canon ADR citation + (b) author c-018. Both are the surfaced next steps.
2. Owner inputs (owner) — the canon edit touches the owner-signed canon → done ONLY on the owner's explicit «да» (G9);
   recorded. The c-018 CALL is a machine artifact (not owner-content); the owner participates at the S2b build PLAN.
3. Do the work — DONE. Read the actual ADR files first (ADR-0016/0002) before editing the owner-signed canon to get the
   correction RIGHT (not a blind find-replace that would create a chronological impossibility). Authored c-018 framing the
   outcome (no solution design). Ran a focused hardening pass; folded only verified text-only findings.
4. Self-check — DONE. Canon edits trace to ADR-0016/0002; the must-fix bug (unbuilt-seam RED control) verified first-hand
   against VoxelField.cs and re-scoped; the line-cite drift (my own §1 edit) caught + name-anchored.
5. Close — DONE (this RESULT). S2b CALL framed; next = owner opens c-018.

## state_changes
- knowledge/g9c41-gas-engine-SPEC.md: 5 ADR citation edits (lock = ADR-0002; §1 correction note).
- work/c-exec-018-call.md: NEW (S2b CALL, hardened).
- NOW.md decision_inbox: d-adr-lockstep-citation-001 → answered (applied).
- NOW.md active_tasks S2b: note → CALL authored + hardened.
- NOW.md open_calls: c-exec-018 → framed.
- NOW.md next: IMMEDIATE NEXT → open c-exec-018; push += s-work-027.
- LOG.md: + one line. history/s-work-027.md: this.

## captures
- (none new) — the 3 stale canon line-cites were a side-effect of THIS session's §1 edit (+1 line); fixed in-session via
  name-anchored cites. NB for future canon edits: CALLs cite canon by line number → a canon insert shifts them; prefer
  name-anchored cites (recorded in c-018 as the pattern).

## decisions_needed
- (none) — d-adr-lockstep-citation-001 resolved (owner «да» → option A applied).

## log
2026-06-28 — work (g-9c41/S2b): fixed the canon ADR lock citation (ADR-0010→ADR-0002, owner «да»); authored + hardened the S2b CALL (c-exec-018).

## next
OPEN c-exec-018 (S2b, load-bearing lockstep loopback) in a FRESH GasCoopGame_dev session — PLAN (owner present, §Re-sync
FIRST) on the clean post-S2a base (main @2e24a24). The idle S2a build session has no further code task → close it. On
c-018's GREEN return → a separate OS writer applies the RESULT + closes S2 (S2a+S2b). next slice after S2 = S3.

END_OF_FILE: live/indie-game-development/history/s-work-027.md
