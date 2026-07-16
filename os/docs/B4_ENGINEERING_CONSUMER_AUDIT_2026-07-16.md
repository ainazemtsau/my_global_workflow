# B4 — consumer audit и доказанное сокращение engineering workflow

Дата: 2026-07-16. Область: `ainazemtsau/my_global_workflow` и зарегистрированные product-репозитории,
только tracked state. Product-репозитории инспектировались read-only; `live/**`, Stryker, worktree/ветки и
существующие untracked `1d1a/`, `2073/`, `6a8f/` не затрагивались.

## Вердикт

Старый kill-list нельзя безопасно исполнять. У каждого механического кандидата либо есть живой
не-self-test consumer, либо ценность/граница удаления неоднозначна; по правилу запроса это **KEEP**.
Доказанный согласованный кластер удаления один: многотысячная историческая проза в обязательном
`CONTRACT_VERSION`, уже полностью сохранённая Git. Она заменена компактной картой
`version -> change -> Git locator`; `current`, сравнение product stamp, terminal Re-sync и точный старый
delta сохранены. Ни один gate, script, spec payload или obligation ID не удалён, поэтому `N` честно
остаётся 239. Mandatory reading снижен с 32,511 до 25,726 слов.

## База и метод

Перед изменением `main == origin/main == e0c4912d73aeb00beedbab8dbf76f2d41aa620c7`,
`CONTRACT_VERSION current: 25`, inventory = `49 G + 97 X + 16 R + 19 S + 31 E + 27 U = 239`,
а whitespace-token count по 11 tracked-файлам `os/engineering/**` был 32,511; сам
`CONTRACT_VERSION` — 7,639. Поиск шёл через tracked tree (`git grep ... origin/main -- .`), а не только
`tools/`; исторические docs/ADR/spec/review ссылки учитывались отдельно от исполняющих consumers.

Read-only product snapshots:

| Репозиторий | Проверенная база | Stamp | Статус для B4 |
|---|---|---:|---|
| `GasCoopGame` | `900efdfb86a207596c12d90c58b1e70d02e6db84` (`origin/main`) | 25 | v26 Re-sync; живые consumers почти всех кандидатов. |
| `health-ai` | `335b6396c7f962ee09ee65b533342cb5d75557f1` (`origin/main`) | 11 | Уже функционально отстаёт; v26-only stamp запрещён. |
| `solmax-operating-substrate` | `66c6c431b81b0d688f305a2c8004d74accfd67f3` (`origin/main`) | 25 | v26 control-plane Re-sync; markdown-profile consumers v13/v18. |
| `Zaratusta` | `29562edff935a9d674b99856f2a9a17867b93e8c` (`origin/main`) | нет | Не Re-sync: current PROJECT_SETUP при активации. |
| `life-reset-manager` | `eff57f8308c159f2d5f97f6ee74a91299cf961c8` (`origin/main`) | нет | Не Re-sync: current PROJECT_SETUP при активации. |

Общие OS-consumers проверены в `CONTOUR.md`, `VALIDATION.md`, `PROJECT_SETUP.md`,
`ESCAPE-CLASSES.md`, всех трёх stack-профилях, `coding-agent.md` и
`OBLIGATION_INVENTORY.md`. OS-side self-test для этих product gates нет; механические self-tests живут
в product-репозитории рядом с исполняющими gates. `profiles/unity.md` дополнительно потребляет
deliverable existence и Git-manifest/build/hygiene; TypeScript и markdown profiles не дали скрытых
механических consumers старого kill-list, кроме явно указанной semantic-review границы markdown.
Full-repo grep также нашёл ссылки в `live/**` CALL/RESULT/history и `archive/**` evidence; это
неизменяемые evidence consumers, не engineering authority и не цель B4. Поскольку механические
правила сохранены, ни одна такая ссылка не требует миграции или правки state.

## Consumer map старого kill-list

### v13 — cumulative refuted register: KEEP

- **Obligations:** `G27`, `X28a`, `X28b`, `X51`, `X53`–`X56`, `S07`, `E22`.
- **OS consumers:** `VALIDATION.md` §Refuted-register, `CONTOUR.md` spec walk/VALIDATE/REPORT,
  `PROJECT_SETUP.md` clause (g), writer-G10 in `coding-agent.md`, inventory rows above.
- **Product consumers:** Gas `AGENTS.md`, `validation.config`, OpenSpec README/template,
  `tools/check.ps1:200,326-339`, `review-check.ps1`, `refuted-register-check.ps1`,
  `escape-class-check.ps1`, cumulative `docs/reviews/REFUTED.md` and review files. The old claim
  “only self-test calls it” is false at current HEAD: `docs/reviews/REFUTED.md:37` has live `R-007`, and
  `docs/reviews/review-c-exec-near-gas-core-authority-001.md:7,18,27,51,63` consumes it. Solmax requires
  `docs/reviews/REFUTED.md` in `tools/check.py:57` and carries the register rule in `AGENTS.md:94-95`.
- **Findings/value:** exact unique-defect attribution to the register is not provable, but live
  persistence/citation and a non-empty post-audit row refute “unused”. Ambiguity means KEEP.
- **If removed / return condition:** independent review/refutation would remain, but cross-leg
  disagreement persistence and duplicate citation would vanish. Reconsider only after every product
  has zero non-self-test register rows/markers and the owner explicitly accepts that loss; then remove
  OS clauses, product scripts/config/templates/registers and self-tests atomically. That would require
  Gas + Solmax functional Re-sync; no removal is owed by v26.

### v14 — fix-class closure: KEEP

- **Obligations:** `G28`, `X24`, `X26a`, `X26b`, `X57`, `E23`.
- **OS consumers:** `VALIDATION.md` §Fix-class-closure, `CONTOUR.md` retry/fix/class sweep,
  `PROJECT_SETUP.md` clause (h), writer-G10 and the inventory.
- **Product consumers:** Gas `tools/check.ps1:204,354`, `fix-class-check.ps1` and its self-test,
  `review-check.ps1`, root/config/template rules, and many real `docs/reviews/review-*.md` `sweep:`
  records. `docs/reviews/review-c-exec-026-resync.md:29-67` records two real false-greens in the v13/v14
  machinery: PowerShell one-element collection unroll accepted substring register IDs, and a typed
  null default made the production fix-class path a no-op while self-test stayed green.
- **Findings/value:** recurrence still happened under earlier forms, but current tree contains
  repaired production consumers and class-sweep evidence. That is ambiguous value, not deletion proof.
- **If removed / return condition:** ordinary review and non-convergence would remain, but no
  class-wide disposal evidence or mechanical reopen. Reconsider only after a measured period with no
  live sweep consumers and an owner decision to rely on judgment; coordinated Gas script/template/
  review-schema removal would be mandatory. V26 removes nothing.

### v18 — cited local artifact existence: KEEP

- **Obligations:** `G29`, `E26`.
- **OS consumers:** `VALIDATION.md` §Cited-artifact existence, closing-report clause in
  `PROJECT_SETUP.md`, inventory.
- **Product consumers:** Gas `tools/check.ps1:114-118`, `result-check.ps1:68-118`, its independent
  `result-check.selftest.ps1:378-445` R9 cases, actual RESULT/review/ADR citations, root/config rules.
  Solmax executes `tools/check.py:230-246,289` and proves both dangling and resolving cases in
  `tools/selfcheck.py:84-96`.
- **Findings/value:** the old audit correctly records one scope miss in the installing leg, but the
  current gate has two independent real product implementations and an always-run light-leg role.
  No evidence proves deletion safe.
- **If removed / return condition:** review existence/ancestry for frozen changes would remain, but
  light-leg dangling RESULT citations would again be unguarded. Reconsider only if closing reports no
  longer cite local artifacts or another existing gate covers the identical key space; remove both
  implementations and self-tests with the text. No v26 removal.

### v8 — named approach / substitution STOP: KEEP

- **Obligations:** `X01`, `X02`, conditional owner-ack evidence `E30a`.
- **OS consumers:** `CONTOUR.md` boundary/ESCALATE, `VALIDATION.md` substitution/refutation rule,
  `PROJECT_SETUP.md`, writer carry-back and inventory.
- **Product consumers:** Gas `coverage-check.ps1:63-111,240-275,497`, wired from
  `check.ps1:208,392`, plus proposals/specs, root/config, REVIEW and ADR-P-0003.
- **Findings/value:** no verified post-install unique catch was found; the original c-exec-012
  substitution/fabricated-approval witness resolves in Git. A same-author string compare is weak but
  not valueless, and active frozen specs consume the token. Ambiguity => KEEP.
- **If removed / return condition:** owner STOP and fresh refutation remain, but silent named-route
  substitution loses its only cheap product tripwire. Reconsider after no active proposal/spec uses an
  approach token and a documented owner decision; delete checker cases/schema/text atomically. No v26
  product change.

### v9 — escape-class walk: KEEP

- **Obligations:** `G22`, `R01`–`R16`, `S06`, `S08` (plus the shared spec-silence gate).
- **OS consumers:** all `ESCAPE-CLASSES.md`, `CONTOUR.md` §b, `VALIDATION.md`,
  `PROJECT_SETUP.md`, inventory and the maintenance late-defect ratchet.
- **Product consumers:** Gas `docs/engineering/ESCAPE-CLASSES.md`,
  `escape-class-check.ps1` + self-test, `tools/check.ps1:181,289,326-339`, every applicable frozen
  spec/template/README, root/config and review docs. The tree also records the repaired vapor-catcher
  false-green. Other profiles preserve semantic review rather than copying the PowerShell gate.
- **Findings/value:** registry rows are backed by named late defects; “zero mechanical finds” does not
  prove the questions redundant. The user explicitly forbade deletion merely for no catch. KEEP.
- **If removed / return condition:** ordinary acceptance/property/review survives, but recurring
  cross-feature blind-spot prompts and catcher regimes vanish. Reconsider only with row-by-row evidence
  that every `R` is duplicated by a surviving independent obligation and after removing every product
  walk/check/spec consumer in the same commit. No v26 removal.

### v7 — deliverable coverage/existence: KEEP

- **Obligations:** `G23`, `X31`, `X71`–`X73`, `S09`, `S10a`, `S10b`, `S11`, `E25`, Unity `U10`.
- **OS consumers:** `CONTOUR.md` §c/LOOK, `VALIDATION.md` Enabled≠written,
  `PROJECT_SETUP.md` clause (c), `profiles/unity.md`, writer done_when reconciliation and inventory.
- **Product consumers:** Gas `coverage-check.ps1` (deliverable sections at `:129,201,211`),
  `check.ps1:208,392`, `openspec/CHANGE_SPEC_TEMPLATE.md:117`, README, root/config and real specs.
- **Findings/value:** the original missing composer/scene is a resolved unique scope-drop witness.
  Lack of a later logged catch is not evidence that current active coverage rows are removable.
- **If removed / return condition:** tests/review remain, but promised engine artifacts may disappear
  silently. Reconsider only after there are no engine/done_when consumers and another surviving gate
  exact-matches every promise; delete spec rows and checker together. No v26 removal.

### v10 — review-evidence wrapper: KEEP

- **Obligations:** `G24`, `X27a`, `X27b`, `X46`–`X52`, `E21` (with v13/v14 sharing later fields).
- **OS consumers:** `VALIDATION.md` §Review-evidence, `CONTOUR.md` VALIDATE/REPORT,
  `PROJECT_SETUP.md` clause (d), writer-G10 and inventory. The irreducible owner-requested floor is
  `G24 + X46 + X47 + E21`: file exists, id matches, reviewed commit is an ancestor.
- **Product consumers:** Gas `review-check.ps1`, `review-check.v15.selftest.ps1`,
  `check.ps1:185,263,304`, root/config/template and the full real `docs/reviews/` corpus. Solmax keeps
  review/refutation as semantic truth in `AGENTS.md`/ADR even where compiled gates are n/a.
- **Findings/value:** the wrapper is not supposed to find code defects; it prevents delivery before
  the independent review that the old audit itself credits for 147/148 findings. The richer fields are
  entangled with v13–v15 consumers, so safely isolating “~30 lines” is not proved here. KEEP.
- **If removed / return condition:** no acceptable removal while the required minimal existence +
  ancestry floor remains. A later simplification needs a measured alternate schema, a full consumer
  migration and seeded misses in one product Re-sync; never delete review or binding fresh G5.

### v12 — property table/token: KEEP

- **Obligations:** `G14a`, `G14b`, `G26`, `X37`, `X66`, `X67`, `S14a`–`S14e`, `E24`.
- **OS consumers:** `VALIDATION.md` §Property-layer, `CONTOUR.md` post-build property audit,
  `PROJECT_SETUP.md` clause (f), inventory.
- **Product consumers:** Gas `coverage-check.ps1`, template/README/spec property tables,
  `tests/GasCoopGame.Core.Tests/GasCoopGame.Core.Tests.csproj:18-20` (CsCheck 3.2.2),
  `Field/Reactions/ReactionPropertyTests.cs` and `Property/PropertyLayerPilotTests.cs`; root/config/ADRs.
  Solmax explicitly marks compiled property machinery n/a rather than pretending to run it.
- **Findings/value:** real property suites and recorded ordering/seam witnesses exist. The request
  explicitly requires CsCheck/property tests and post-build independent value, so table/token deletion
  is not authorized and its gate consumers are live.
- **If removed / return condition:** none inside B4. Only a future owner request with an equally
  enforceable mapping from required property classes to real categorized tests could replace these IDs.

### “SHA manifests — 844 lines”: candidate absent; shared Git guard KEEP

- **Obligations:** the retired NearGas plan-document pin has no current ID. The current v23 freeze Git
  manifest is `E07` and is explicitly protected; do not conflate it with the old product pin.
- **Consumers:** `FrozenNearGasManifest` is absent from Gas `origin/main`. The remaining shared
  `GitCommittedArtifactGuard` is live at
  `tests/GasCoopGame.Core.Tests/Field/Coarse/CoarseArtifactTests.cs:135`; its implementation and
  mechanism tests are `tests/GasCoopGame.Core.Tests/Tooling/GitCommittedArtifactGuard.cs` and
  `tests/GasCoopGame.Core.Tests/Tooling/GitBlobIdentityTests.cs:59,89,112,132,151`.
  `tools/git-blob-identity.ps1` remains v24 committed-artifact tooling.
- **Findings/value:** the audit correction is confirmed: roughly 15 lines of plan pinning are already
  gone; the ~830-line shared cluster is not dead. There is therefore nothing in-scope to delete.
- **If removed / return condition:** only after full-tree call sites are zero and a surviving git-native
  mechanism proves the same committed bytes. Product-only change, not a v26 Re-sync action.

### Three source scanners: KEEP (product-local, not an OS deletion)

- **Obligations:** no distinct OS inventory IDs. V17's `X29a/X29b` bans source scans as *behaviour
  evidence*; Gas config classifies these three as permitted deterministic-core boundary/hygiene checks.
- **Consumers:** Gas `tools/check.ps1:50,58,66` always invokes `zero-float-scan.ps1`,
  `int-overflow-scan.ps1`, `type-hardcode-scan.ps1`; ADR-0011/0012/0017/0018/0019 and tests/specs name
  their local invariants. `excluded-category-check.ps1` is outside B4 by explicit boundary.
- **Findings/value:** the integer scan missed a real overflow, but a miss does not prove the different
  deterministic-boundary predicate useless. Current value is ambiguous and the files are product-owned.
- **If removed / return condition:** a separate product maintenance request must show zero remaining
  policy/spec/test consumers or a surviving equivalent real-venue predicate, then delete script,
  `check.ps1` call and local authority together. V26 does not touch them.

### `CONTRACT_VERSION` historical prose: DELETE/COMPACT

- **Obligations:** none; history/rationale is excluded by the inventory occurrence rule.
- **Consumers:** `coding-agent.md` needs only integer comparison and missing version rows;
  `PROJECT_SETUP.md` and product configs need current stamp/inventory provenance; old audit/handoff and
  Git need evidence. No gate parses the long prose.
- **Findings/value:** the current map preserves every version and exact Git locator. The full old text
  remains retrievable at base SHA `e0c4912d73aeb00beedbab8dbf76f2d41aa620c7`; B4 itself resolves via tag
  `engineering-contract-v26`. This is the only proved redundant mandatory-reading cluster.
- **Remaining protection:** monotonic `current`, product drift guard, terminal Re-sync instructions,
  current active authority and Git exact delta. **Return condition:** restore a particular fact only if
  a future Re-sync cannot be derived from its compact row plus cited commit; restore that fact, never the
  full narrative. Product impact is metadata-only, plus safe removal of inert Gas history-note fields
  listed below.

### “11 of 14 spec sections”: KEEP; numerical premise no longer matches current tree

- **Obligations:** current payload inventory is `S01`–`S14e` (19 independently removable payloads),
  with gates and evidence consumers named above.
- **Consumers:** Gas current template has five top-level payload headings
  (`CHANGE_SPEC_TEMPLATE.md:17,24,52,98,112`), not the claimed 14-section shape; its tables feed
  coverage, escape, NegativeControl, property and v23 handoff consumers. OS CONTOUR/VALIDATION/
  PROJECT_SETUP and inventory point to them.
- **Findings/value:** no coherent eleven-section deletion set exists at current HEAD. Cutting text
  while live gates parse the payload would create exactly the dangling consumers forbidden by B4.
- **If removed / return condition:** propose stable IDs, prove each has no unique gate/evidence value,
  then remove its product check/self-test/template consumer before or with authority. No section removed.

### v21 “fully”: historical carrier prose compacted; active descendants KEEP

- **Obligations:** current `S12` (`behavioral-red|evidence-only`) and `R16` evidence-class integrity
  descend through v22/v23; `X32` keeps semantic judgment out of proxy scanners. The exact v21 prose
  recipe/PLAN-AMEND carrier is already superseded by the terminal v23 route and is not counted.
- **Consumers:** Gas `AGENTS.md:131-132,403`, template/README, current NearGas ADR/spec rows and v23
  validation note consume the split and immutable independent RED; OS CONTOUR/VALIDATION carry v23.
- **Findings/value:** “delete v21 fully” would wrongly remove still-active descendants. B4 deletes only
  its redundant long history narrative and keeps a compact v21 locator.
- **If removed / return condition:** none while `S12/R16` and product rows remain. A future semantic
  simplification must name a narrower current ID and migrate every gate/spec consumer atomically.

## Applied change and inventory result

Changed authority is deliberately small: `CONTRACT_VERSION` compact map/current v26,
`PROJECT_SETUP.md` v26 provenance values, B3 reading-ceiling text, inventory provenance, and adapter
wording “version rows” instead of “log lines”. `CONTOUR.md`, `VALIDATION.md`, `ESCAPE-CLASSES.md` and
all profiles are byte-unchanged. Removed IDs: none. Added leg duties: none. Counts remain
`49 + 97 + 16 + 19 + 31 + 27 = N239`; compression is not recorded as deletion.

## Full scenario walkthrough

1. **PLAN:** owner-readable plan, change class, acceptance ledger, invariant/spec-silence/escape walk,
   deliverable coverage and applicable NegativeControl/property payloads still resolve in current
   authority; v26 history is not an execution input.
2. **SURFACE-FREEZE:** separate fresh surface author, ≤400-word decision page, ≤400 added production
   lines, real public signatures, exact Git manifest, compiler-green build, hygiene and sidecars all
   remain v23 obligations.
3. **Independent RED:** fresh test-author writes the immutable complete behavioral RED artifact;
   compile/discovery/behavioral failure and binding fresh artifact-backed refutation still gate BUILD.
4. **BUILD:** fresh builder pins reviewed surface+RED, cannot edit either, makes tests pass, preserves
   compilation/hygiene, NegativeControls, property audit and v24 independently-derived mutation scope
   with score ≥70.
5. **Review:** independent review, reviewed-commit ancestry, scope split, refutation/register,
   fix-class sweep, binding fresh G5 and owner eye remain.
6. **Deliver:** full suite/evidence/RESULT, deliverable existence, cited-artifact existence and all
   applicable product checks remain. A **light leg** has no frozen OpenSpec folder, so the heavy
   strong-check battery is N/A by artifact absence exactly as before; normal mechanical checks,
   honest RESULT, literal cited-artifact existence, review/refutation as applicable and owner eye still
   close it. A **STOP path** still fires on >400 surface, unavailable required tool, named-approach
   substitution, non-compiling/non-behavioral RED, retry non-convergence or malformed/incomplete
   mutation scope. History compaction removes no route edge and cannot make the normal path impossible.

## Один финальный product Re-sync packet

Apply only in later product-owned Re-sync sessions, never in this OS maintenance commit:

1. **GasCoopGame (25→26):** keep every script/gate/test/spec section. In `validation.config`, set
   `synced_contract_version: 26`, `obligation_inventory_version: 26`, keep
   `obligation_ceiling: 239`, and set `obligation_inventory_source: <full v26 OS commit SHA>`.
   Replace the six consumer-free history fields
   `synced_contract_version_note`, `synced_contract_version_v19_note`,
   `synced_contract_version_v20_note`, `synced_contract_version_v21_note`,
   `synced_contract_version_v23_note`, `synced_contract_version_v24_note` with one concise
   `synced_contract_version_note: "v26; no product gate removed; exact history in my_global_workflow Git"`.
   Full-tree proof before deletion: each old field currently occurs only in `validation.config:9-14`.
   After edit, `git grep` for the five versioned field names must be empty; JSON parse, repo-native
   non-mutation check and existing gate self-tests must remain green. Do not run Stryker for v26.
2. **solmax-operating-substrate (25→26):** no rule/script deletion or simplification. Update the same
   four stamp/provenance values to 26/239/`<v26 SHA>`, then run `python tools/selfcheck.py` and
   `python tools/check.py`; cited-artifact and REFUTED consumers must remain present.
3. **health-ai (11→26):** **not eligible for a B4-only bump.** Its
   `validation.config:2` and `tools/check_training_activity_thin_slice.py:389` exact-match v11, and it
   still owes terminal, stack-appropriate functional reconciliation for rows 12–24 plus v25 inventory.
   A separate product Re-sync installs or explicitly marks n/a every applicable row, then changes both
   tokens to `os-engineering-contract.v26`, records inventory 26/239/source, and runs the repo-native
   thin-slice checker. B4 itself deletes/simplifies no health rule or script.
4. **Zaratusta / life-reset-manager:** no stamp and no tracked candidate consumer; do nothing now.
   On activation, apply current PROJECT_SETUP directly at v26. Do not invent an intermediate Re-sync.

No dangling-consumer proof for the B4 cluster is therefore exact: OS adapters now read version rows;
Gas's removable keys have zero tracked consumers outside their own declarations; Solmax removes
nothing; health cannot stamp current before functional reconciliation; unstamped repos change nothing.

END_OF_FILE: os/docs/B4_ENGINEERING_CONSUMER_AUDIT_2026-07-16.md
