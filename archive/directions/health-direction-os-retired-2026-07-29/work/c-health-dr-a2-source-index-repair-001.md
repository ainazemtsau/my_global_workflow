# READY TO LAUNCH — not registered/in flight

CALL c-health-dr-a2-source-index-repair-001
to: session
direction: health
play: work
node: g-health-training-activity-system
goal: |
  DR-A2 evidence package is citation-complete for the bounded deload sweep and ready for final close verification while remaining a decision framework only.
context: |
  Work only from the canonical saved artifacts:
  - live/health/work/dr-a2-decision-framework-2026-07-14-revised2.md
  - live/health/work/dr-a2-evidence-ledger-2026-07-14-revised2.xlsx
  - live/health/history/2026-07-14-s-health-dr-a2-artifacts-preserve-001.md

  The prior audit passed content, scope, workbook structure and visual quality.
  Remaining source-index facts:
  - E26 PMID: 34138821; canonical URL: https://pubmed.ncbi.nlm.nih.gov/34138821/
  - E27 PMID: 21131862; canonical URL: https://pubmed.ncbi.nlm.nih.gov/21131862/
  - E28 full citation: Tavares LD, de Souza EO, Ugrinowitsch C, Laurentino GC,
    Roschel H, Aihara AY, Cardoso FN, Tricoli V. Effects of different strength
    training frequencies during reduced training period on strength and muscle
    cross-sectional area. European Journal of Sport Science. 2017;17(6):665-672.
    DOI: 10.1080/17461391.2017.1298673
    PMID: 28316261
    Online date: 2017-03-19
    Canonical URL: https://pubmed.ncbi.nlm.nih.gov/28316261/
boundaries: |
  Preserve revised2 as immutable evidence; create revised3 outputs rather than overwriting.
  Change only E26-E28 source metadata and necessary revised3 filename/version references.
  Do not change scientific claims, applicability judgments, decision rules or scope.
  Do not activate a programme, frequency, split, exercise list, sets, repetitions,
  loads, personal RIR, deload schedule or mesocycle.
  Do not edit NOW.md, TREE.md, CHARTER.md or current Health HQ routing.
done_when: |
  Revised3 MD and XLSX exist under live/health/work.
  E26-E28 metadata is complete and matches the canonical source records above.
  Workbook still has 4 sheets, 42 claim rows, 25 required ledger fields and 28 source rows;
  required cells and refresh triggers are nonblank; formula-error scan is empty; every sheet passes visual inspection.
  The package still states that it is a decision framework only and activates no personal programme.
return: |
  RESULT with revised3 paths and SHA256 hashes, exact workbook QA evidence,
  boundary confirmation, no NOW/TREE changes, and a final-close verification route.
budget: one session

END_OF_FILE: live/health/work/c-health-dr-a2-source-index-repair-001.md
