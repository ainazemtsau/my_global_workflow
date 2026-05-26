# Wave 1

Wave 1 should use **6 tasks**. Total TIME = **5.0 days**.

The batch is complete enough to produce the usable stack, but it cuts depth where needed: sample outputs are simple proof outputs, GitHub Markdown structure is a short tree/list, and no live Hevy/MacroFactor setup or logging is included.

─────────────────────────────────────
ЗАДАЧИ
─────────────────────────────────────

ЗАДАЧА 1

TRIGGER:
Wave 1 starts after S5 Wave Card acceptance.

ACTION:
Create the M1 Boundary Lock artifact and the working artifact skeleton for the stack. Define, in one short note, the roles and boundaries of:

Training Coach;
Nutrition / Menu Planner;
Recipe Builder;
Hevy;
MacroFactor;
GitHub Direction files.

Explicitly include:

what is being built;
what is not being built;
where execution/tracking lives;
that baselines are starting materials, not immutable doctrine;
that stale nutrition-only framing is not authoritative.

DONE WHEN:
There is a short **00 — Use Boundary** artifact that another person can read in under 2 minutes and answer:

what the Goal builds;
what it refuses to build;
where training execution/logging lives;
where nutrition targets/logging live;
what GitHub Direction files store;
what ChatGPT must not become.

WHY:
This prevents the most expensive failure mode: the stack drifting back into daily logging, app setup, full redesign, or nutrition-only scope.

INPUT:
Execution Pack M1;
Goal Brief;
Direction Current Phase and Canon;
No-gos;
stale file warning.

OUTPUT:
`00 — Use Boundary` draft;
artifact inventory for remaining tasks.

TYPE:
Boundary / scope-lock artifact.

TIME:
0.5 day
(first instinct 0.33 day × 1.5 ≈ 0.5 day)

STATUS:
open

ЗАДАЧА 2

TRIGGER:
Task 1 is DONE.

ACTION:
Create compact context blocks for all three chats:

Training Coach — Context Block;
Nutrition Menu Planner — Context Block;
Recipe Builder — Context Block.

For Nutrition / Menu Planner, cut the nutrition baseline into:

required context: MacroFactor targets placeholder, day-types L/U/C/R, protein target logic, calories/macros by day type, meal timing, sweet-control rules, plate logic, batch-prep structure, adjustment rules, practical preferences;
reference-only: research rationale, long narrative, supplements unless requested, health labs unless outside this Goal, unused examples;
do not include: Daily Operator, Google Sheets TSV workflow, old Weekly Planner / RecipeVault model, anything implying ChatGPT logs food instead of MacroFactor.

For Training Coach, cut the training baseline into:

required context: Hevy week/session placeholder, home weeks 1–4 / gym weeks 5–12 structure, Lower/Upper structure, RIR rules, double progression, deload logic, VR/cardio rules, Achilles/pain constraints, sleep/pain/strength-drop quick rules, weekly check-in metrics;
reference-only: full exercise tables unless needed, full week-by-week narrative, equipment/shopping notes unless requested, nutrition note at end;
do not include: full 12-week document, new training architecture, anything implying Training Coach logs instead of Hevy.

DONE WHEN:
Each context block is compact enough to paste into a new ChatGPT chat and usable without pasting the full baseline documents.

WHY:
This is the core compression layer. If context blocks are too large, the stack will degrade into full-document prompting and fail the Goal boundary.

INPUT:
Task 1 boundary artifact;
Nutrition MasterPlan;
12-week training plan v2;
Execution Pack M2 context cuts.

OUTPUT:
`Training Coach — Context Block`;
`Nutrition Menu Planner — Context Block`;
`Recipe Builder — Context Block`.

TYPE:
Context compression / baseline cut.

TIME:
1.25 days
(first instinct 0.83 day × 1.5 ≈ 1.25 days)

STATUS:
open

ЗАДАЧА 3

TRIGGER:
Task 2 is DONE.

ACTION:
Create copy-paste-ready starter/restart packages for all three chats.

Each package must include:

chat role;
required user input;
compact context block;
default interaction pattern;
output format;
restart rule;
context degradation rule;
boundaries/no-gos.

Required package behavior:

Training Coach must support exercise questions, progression, recovery, pain/limitation framing, and Hevy handoff notes.
Nutrition / Menu Planner must support requested horizon menu/prep planning under MacroFactor targets and manual MacroFactor handoff notes.
Recipe Builder must create RU cooking/GitHub reusable recipe + EN MacroFactor entry version, without building a large recipe vault.

DONE WHEN:
Each package can be pasted into an empty ChatGPT chat, followed by a concrete user request, and produce the intended output without additional GitHub Direction files explanation.

WHY:
The context blocks alone are not enough. The user needs launchable chat packages that define interaction behavior and prevent context drift.

INPUT:
Task 2 context blocks;
Execution Pack M3;
No-gos;
placeholder list.

OUTPUT:
`Training Coach — Starter Restart`;
`Nutrition Menu Planner — Starter Restart`;
`Recipe Builder — Starter Restart`.

TYPE:
Prompt package / restart package.

TIME:
1.25 days
(first instinct 0.83 day × 1.5 ≈ 1.25 days)

STATUS:
open

ЗАДАЧА 4

TRIGGER:
Task 3 is DONE.

ACTION:
Create output templates and the minimal GitHub Markdown storage structure.

Output templates:

Training Coach — practical answer/adaptation + exact Hevy handoff note.
Nutrition / Menu Planner — menu/prep under `[requested horizon]` + MacroFactor handoff note.
Recipe Builder — RU recipe for cooking/GitHub reusable notes + EN MacroFactor entry version + manual entry notes.

Minimal GitHub Markdown structure:

`AI Support Stack/`
`00 — Use Boundary`
`01 — Context Blocks/`
`02 — Starter Restart Packages/`
`03 — Output Templates/`
`04 — Sample Proof Outputs/`
`05 — Reusable Storage/`
`Recipes/`
`Menus/`
`Prep Templates/`
`MacroFactor Entry Notes/`
`Hevy Handoff Notes/`
`06 — Final Pack`

Keep the structure as a short tree/list only. Do not add tags, taxonomy, daily notes, tables, databases, or vault design.

DONE WHEN:
There are three reusable output templates and one short GitHub Markdown structure note that satisfies M4 without becoming a database.

WHY:
The stack needs a predictable output shape and a place to store launch/reusable artifacts, but storage must stay minimal.

INPUT:
Task 1 boundary artifact;
Task 3 starter/restart packages;
Execution Pack M4;
Acceptance criteria 4–5.

OUTPUT:
`Training Coach — Output Template`;
`Nutrition Menu Planner — Output Template`;
`Recipe Builder — Output Template`;
`Minimal GitHub Direction files Storage Structure`.

TYPE:
Output shape / storage layer.

TIME:
0.75 day
(first instinct 0.5 day × 1.5 = 0.75 day)

STATUS:
open

ЗАДАЧА 5

TRIGGER:
Task 4 is DONE.

ACTION:
Create three simple sample proof outputs using placeholders, not live app data.

Sample 1 — Training Coach:
A practical answer/adaptation using `[current Hevy week/session]` and `[current constraints]`. Include conservative constraints if pain/recovery issue exists and an exact Hevy handoff note.

Sample 2 — Nutrition / Menu Planner:
A short menu/prep output for `[requested horizon]`, using `[current MacroFactor targets]`. Include a MacroFactor handoff note. Keep sample complexity low.

Sample 3 — Recipe Builder:
One reusable recipe with:

RU version for cooking/GitHub reusable notes;
EN version for MacroFactor entry;
clear ingredients and portions;
manual entry notes.

DONE WHEN:
The three samples visibly prove usable output shape and are clearly not daily logs, app setup, or real live execution.

WHY:
This validates that the packages produce the right kind of output before the stack is treated as usable.

INPUT:
Task 4 templates;
Task 3 packages;
Execution Pack M5;
placeholder list.

OUTPUT:
`Training Coach — Sample`;
`Nutrition Menu Planner — Sample`;
`Recipe Builder — Sample`.

TYPE:
Sample proof / output validation.

TIME:
0.75 day
(first instinct 0.5 day × 1.5 = 0.75 day)

STATUS:
open

ЗАДАЧА 6

TRIGGER:
Task 5 is DONE.

ACTION:
Assemble the final copy-paste-ready pack and run a scope/readiness audit.

Final pack must include:

launch instructions;
storage instructions;
restart rules;
context degradation rules;
chat boundaries;
manual Hevy handoff rules;
manual MacroFactor handoff rules;
what not to do in ChatGPT/GitHub files;
what to save in GitHub Direction files;
what to update in `active-goal.md` after S4/S5 artifact completion if needed.

Audit the artifact set against acceptance criteria:

three bounded chat definitions;
context blocks;
starter/restart packages;
output templates;
minimal GitHub Markdown layer;
manual handoff boundaries;
sample proof outputs;
scope protection embedded.

DONE WHEN:
There is one `06 — Final Pack` artifact and a short acceptance map showing that M1–M6 are covered or explicitly noting any gap.

WHY:
The final pack is the usable entry point. Without it, the outputs are fragmented notes rather than a launchable support stack.

INPUT:
Tasks 1–5 outputs;
Execution Pack M6;
Acceptance criteria;
No-gos;
Replan triggers.

OUTPUT:
`06 — Final Pack`;
acceptance criteria coverage map;
known gaps, if any;
ready-to-copy S_E `wave_graph_plan` input summary.

TYPE:
Final packaging / readiness audit.

TIME:
0.5 day
(first instinct 0.33 day × 1.5 ≈ 0.5 day)

STATUS:
open

─────────────────────────────────────
TIME CHECK
─────────────────────────────────────

Task 1: 0.5 day
Task 2: 1.25 days
Task 3: 1.25 days
Task 4: 0.75 day
Task 5: 0.75 day
Task 6: 0.5 day

Total: **5.0 days**

This fits the Wave Length exactly. No buffer remains, so the scope cut rule should be active during execution: reduce sample complexity and GitHub Direction files detail before cutting any of the three chat packages.

─────────────────────────────────────
POTENTIAL BLOCKERS
─────────────────────────────────────

No blocker appears to prevent Task 1 from starting.

Potential non-blocking risks:

- Context blocks become too long.
Response: cut to required context only; keep full baselines reference-only.
- Sample outputs start becoming real live planning.
Response: use placeholders and mark samples as artificial proof outputs.
- GitHub Markdown structure drifts into database design.
Response: keep only the short tree/list.
- Missing live MacroFactor targets or Hevy week/session appears to block work.
Response: use placeholders; live app extraction is out of scope.
- Stale nutrition-only files reappear as authority.
Response: current Goal Brief and Execution Pack win.
- Final pack asks for automation/imports/API.
Response: manual handoff only; automation is out of scope.
