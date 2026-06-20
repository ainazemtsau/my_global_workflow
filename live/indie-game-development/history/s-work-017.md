# RESULT — s-work-017 (g-9c41): give the gas-model doc TEETH — guardrails so replanning can't bypass it

direction indie-game-development / node g-9c41 / role guardrail (owner-requested assurance that the new gas-model doc is taken into account for replanning). Additive NOW.md markers only — nothing decided, nothing weakened, bet spine untouched.

## outcome

The owner asked to be SURE the new gas-model document (work/gas-model-design-full-2026-06-20.md) will actually drive replanning — because the plans need substantial rework, and a big doc can quietly be filed while the stale plan proceeds by inertia. Answer = mechanical teeth, not a promise. Four additive markers were placed at every spot in NOW.md where the OLD trajectory could leak through, each pointing at the doc:

1. **d-gasmodel-redesign-001 status** → `open — BLOCKING the next g-9c41 bet`: no Wave-3/next bet may be SHAPED for g-9c41 until this decision is made against the full doc.
2. **kill_by.next_if_true** → SUSPENDED: the auto-roll "coarse sim done → roll to Wave 3 (T2 detail + no-jerk handoff)" is HELD; the doc may re-frame Wave 3 entirely.
3. **wave_plan Wave 3** → marked PROVISIONAL / PRE-redesign: re-framed by the doc §K if the owner picks dorога A+; the text is kept for reference, NOT a settled trajectory.
4. **review CALL** → a ⚠️ HARD PRECONDITION: the review MAY NOT roll g-9c41 to the old Wave 3; it MUST first decide d-gasmodel-redesign-001 (A+/B/C) against the doc, **confirm the doc was actually consumed (cite its §K/§G/§H)**, and if A+ re-shape from the §K chunks with §G load-probes first.

Net effect: any future review/shape session that tries to proceed on g-9c41 will hit a blocking decision + suspended old plan that force it to open and use the doc. Nothing is decided here (d-gasmodel-redesign-001 stays OPEN — the owner ratifies A+/B/C at the review); nothing is weakened (purely additive).

## evidence

- NOW.md now carries the four markers (grep: `BLOCKING the next g-9c41 bet`, `SUSPENDED 2026-06-20`, `Wave 3 below is PROVISIONAL`, `HARD PRECONDITION (2026-06-20`), all referencing work/gas-model-design-full-2026-06-20.md.
- No TREE/CHARTER edit; no task/bet status change; active bet g-9c41 spine, done_when, appetite untouched. The guardrails only annotate the OLD plan as provisional/suspended and the decision as blocking.

## state_changes

- NOW.md decision_inbox d-gasmodel-redesign-001: status string → `open — BLOCKING the next g-9c41 bet` + a **BLOCKING** clause in the comment.
- NOW.md kill_by.next_if_true: replaced with a SUSPENDED marker pointing at the doc.
- NOW.md active_bet.wave_plan: PROVISIONAL banner above the Wave-3 block.
- NOW.md next (review CALL): a ⚠️ HARD PRECONDITION line at the top of the CALL.
- LOG.md: appended the s-work-017 line.
- NO decision made; NO TREE/CHARTER/bet/task change.

## captures

- This is the structural answer to "will the big doc actually be used": convert an OPEN decision that could reframe a bet into a BLOCKING gate + suspend the stale plan it would replace, so inertia can't bypass it. Cheap, additive, reversible (the decision unblocks the markers when resolved).

## decisions_needed

- None. The blocking decision d-gasmodel-redesign-001 is resolved by the owner at the review (A+/B/C), using the doc.

## play_check

- "Recite — owner wants assurance the new gas-model doc drives the (substantial) replanning, not get shelved."
- "Guardrail — added 4 additive markers (blocking decision / suspended next_if_true / provisional wave_plan / review hard-precondition), all pointing at the doc; confirm-consumed clause added to the review CALL."
- "Safety — nothing decided (d-gasmodel stays OPEN), nothing weakened (additive only); bet spine untouched (don't-break-what-works, G9/G6 respected — the real re-shape is the review/shape's job with owner approval)."
- "(owner) — the request «убедиться что примем в расчёт новый документ … придётся сильно переделать планы» is the owner's words; the markers encode exactly that, without pre-deciding the redesign."
- "Close — RESULT; committed; review remains next (now gated on the doc)."

## log

work/guardrail (g-9c41, s-work-017): owner asked to GUARANTEE the new gas-model doc is taken into account for replanning → gave it teeth. 4 additive NOW.md markers all pointing at work/gas-model-design-full-2026-06-20.md: d-gasmodel-redesign-001 → BLOCKING the next g-9c41 bet; kill_by.next_if_true → SUSPENDED; wave_plan Wave 3 → PROVISIONAL/PRE-redesign; review CALL → ⚠️ HARD PRECONDITION (decide A+/B/C against the doc first, confirm consumed, re-shape from §K with §G probes if A+). Nothing decided (stays OPEN), nothing weakened (additive); bet spine untouched. → history/s-work-017.md

## next

Unchanged: **review g-9c41** in a fresh session — now GATED on d-gasmodel-redesign-001, which forces consuming the full doc before any next bet. If the owner picks dorога A+, the review/shape re-frames the next bet from the doc's §K chunks (§G load-probes first), likely a re-shape past the 07-24 wall. This OS repo is committed locally; push is owner-gated.

END_OF_FILE: live/indie-game-development/history/s-work-017.md
