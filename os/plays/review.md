# Play: review

Purpose: close or stop the active bet, harvest learning, update TREE with the owner, recalibrate the direction forecast, and select what comes next.

Reads: CHARTER.md, TREE.md, NOW.md, target history/evidence.
Writes: TREE.md, NOW.md, LOG.md, knowledge/.

Trigger: tasks closed, appetite expired, kill_by breached, evidence made the bet obsolete, or the owner wants to stop/change it. Run in a fresh physical chat; never the work/day chat whose claim is being judged.

## Steps

1. **Verify by refutation** — try to disprove done_when from evidence. Verdict is exactly:
   - `met` — done_when survived refutation;
   - `partial` — named verified value survives but done_when does not;
   - `killed` — appetite/kill_by or evidence stops the bet;
   - `obsolete` — a higher approved strategy change removed its purpose.
   There is no extension. Residual work is parked/dropped and can return only as a newly shaped bet. Compare the bet forecast/against fields with reality and name the surprise.
2. **Harvest per lens** — each CHARTER lens answers what changed elsewhere, even if “nothing”. Name assumptions/edges strengthened or killed and consequences for the roadmap/issues.
3. **Tree diff (owner)** — propose small node additions/drops/dispositions, one artifact at a time. Apply only exact owner-approved cards (G9); larger restructuring routes to map. No tasks.
4. **Add-back check** — inspect the cut list. Name genuinely missed cuts and whether recent cuts are too timid.
5. **Knowledge** — promote at most 1–3 durable learnings, each with a real `read_by`; otherwise keep only history.
6. **Forecast & next** — recalibrate `direction_forecast` from material evidence. Numeric chance needs a cited empirical reference class/calibration; otherwise use `no_basis` with drivers and update trigger. Then offer 2–3 future nodes or pause, with recommendation. Activation uses the KERNEL §2 readiness router, never a direct shape default.
7. **Close** — RESULT records verdict/tree/forecast/issues/log. Pending choice → decision + `awaiting_decision`; chosen node → exactly one readiness-routed CALL.

## Done when

The old bet has one honest verdict; TREE reflects approved learning; NOW contains no stale bet work; forecast is calibrated or explicitly `no_basis`; the owner has a next-node choice.

## Notes

- `partial`, `killed` and `obsolete` are useful outcomes, not disguised done.
- Review never preserves a lane merely because work once existed; a future bet must admit it again.

END_OF_FILE: os/plays/review.md
