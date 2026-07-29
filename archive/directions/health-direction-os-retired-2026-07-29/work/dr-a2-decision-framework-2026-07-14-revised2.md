# DR-A2 — Evidence-based architecture силовой программы при переходе из дома в зал — revised2

**Статус:** финальная bounded correction текущего DR-A2. Это decision framework и evidence ledger, не персональная программа.  
**Фактическая дата последнего поиска/проверки:** **14 июля 2026 года**.  
**Evidence cutoff:** 14 июля 2026 года.  
**Входные файлы:** `DR-A2_decision_framework_2026-07-14-revised.md`, `DR-A2_evidence_ledger_2026-07-14-revised.xlsx`.  
**Correction target:** добавить Pancar 2026, исправить wording Coleman 2024, выполнить bounded backward/forward deload citation sweep, уточнить ACSM wording, E20 traceability, commute-dose и calorie-estimate boundaries.

## 1. Answer-first summary

Наиболее обоснована **адаптивная архитектура**, а не готовая программа: ветки `дальний зал`, `ближний зал` и `дом` должны сохранять общую историю movement/function, но не объявляться килограмм-в-килограмм эквивалентами. Решения `progress / hold / reduce / substitute / rollback / rebuild` должны опираться на повторяемую фактическую реакцию: performance, technique, RPE/RIR, pain/tolerance, bike load, VR load, sleep/energy и next-day function.

Главные bounded conclusions сохранены и уточнены:

1. **Три и четыре силовых дня остаются открытыми кандидатами.** Актуальная 2026 meta-regression показывает positive dose-response weekly volume с diminishing returns; frequency для hypertrophy совместима с negligible effects, а для strength имеет positive/diminishing relationship. Это не прямой RCT “3 vs 4” в данном owner context. [E02](https://link.springer.com/article/10.1007/s40279-025-02344-w) [E07](https://link.springer.com/article/10.1007/s40279-018-0872-x)
2. **Full-body и split — способы распределения работы, а не окончательный победитель.** Volume-equated split и full-body routines дают сходные pooled outcomes. [E06](https://doi.org/10.1519/JSC.0000000000004774)
3. **ACSM Position Stand 2026 используется как primary/official broad framing.** В E01 отражено: **137 systematic reviews involving over 30,000 participants**; primary PMC/official source set checked; из него не импортируются персональные numeric prescriptions. [E01](https://pmc.ncbi.nlm.nih.gov/articles/PMC12965823/)
4. **Training to failure не является обязательным default.** Proximity-to-failure evidence поддерживает difference between strength and hypertrophy relationships, но не определяет personal RIR. [E03](https://link.springer.com/article/10.1007/s40279-024-02069-2) [E04](https://doi.org/10.1186/s13102-026-01861-z)
5. **Machines и free weights не имеют универсального победителя.** Strength specificity есть; modality selection должен идти через hierarchy, а не идеологию. [E05](https://link.springer.com/article/10.1186/s13102-023-00713-4)
6. **Deload evidence corrected.** Direct but narrow evidence now exists for:
   - complete-cessation / periodic cessation models: Ogasawara 2011, Ogasawara 2013, Coleman 2024; [E24](https://doi.org/10.1111/j.1475-097X.2011.01031.x) [E25](https://link.springer.com/article/10.1007/s00421-012-2511-9) [E22](https://pmc.ncbi.nlm.nih.gov/articles/PMC10809978/)
   - reduced-volume/frequency deload: Pancar 2026. [E23](https://www.nature.com/articles/s41598-026-40612-5)
   Эти источники не доказывают benefit, necessity или superiority of deload и не позволяют выбрать personal deload protocol.
7. **Coleman 2024 wording corrected.** Both groups improved; there were no appreciable between-group differences in increases of lower-body muscle size, local endurance or power, while continuous training showed greater improvements in isometric and dynamic lower-body strength. [E22](https://pmc.ncbi.nlm.nih.gov/articles/PMC10809978/)
8. **Pancar 2026 added.** In 19 untrained young men using randomized within-subject design, reduced-frequency/volume deload weeks produced similar increases in muscle thickness and 10RM to continuous training despite about 18% lower total set volume; no between-condition superiority was shown. [E23](https://www.nature.com/articles/s41598-026-40612-5)
9. **Дальний зал не отклоняется заранее.** Cycling commute — changing fatigue input, не точная dose по километрам. “Kilometres are not exact dose” is an operational/measurement inference, not a result established by concurrent-training meta-analysis. [E11](https://link.springer.com/article/10.1007/s40279-021-01587-7) [E19](https://doi.org/10.3389/fnins.2017.00612) [E20](https://doi.org/10.1097/HCO.0000000000000097)
10. **Велосипед может заменить только часть general warm-up, условно.** Exercise-specific warm-up/ramp-up after cycling remains `Inference`; прямого commute-vs-specific-warm-up experiment не найдено. [E17](https://doi.org/10.1519/JSC.0b013e3181c643a0)
11. **VR классифицируется по фактической реакции.** Wrist/arm wearable calorie validation does not directly validate app/headset calorie estimates; excluding app/headset calories as precise dose is a conservative operational extrapolation. [E13](https://doi.org/10.1136/bjsports-2018-099643) [E14](https://games.jmir.org/2020/3/e17972/)
12. **Rolling schedule, one-variable-at-a-time, last-known-good rollback и отсутствие log debt остаются Inference.** Они полезны для управления неопределённостью, но не являются доказанными scientific prescriptions.

## 2. Scope и explicit cuts

### В scope

- frequency/weekly structure as decision framework;
- переход от 2 × 24 кг fixed dumbbells + bands к системному залу;
- initial volume envelope без назначения чисел;
- intensity, loading, RPE/RIR and proximity-to-failure ranges as evidence boundaries;
- exercise-selection hierarchy без exercise list;
- progression/regression/hold/rebuild logic;
- far gym / near gym / home branch comparison;
- bicycle commute as load, warm-up and cooldown input;
- VR classification rules;
- testing/retesting boundaries;
- strength-specific missed-session resilience;
- bounded deload evidence correction and citation sweep.

### Explicit cuts

Этот revised2 DR-A2 **не**:

- выбирает final frequency, split, exercises, sets, repetitions, loads, personal RIR, deload schedule или mesocycle;
- назначает session-duration cap;
- объявляет medical clearance, диагноз или treatment;
- предполагает отсутствие red-flag symptoms;
- заполняет private unknowns догадками;
- называет владельца sedentary beginner или человеком после многолетнего detraining;
- предполагает скамью дома, регулируемые гантели или дополнительное оборудование;
- трактует велосипед как полную разминку или обратную поездку как автоматический cooldown;
- трактует VR как автоматически light/vigorous;
- превращает coaching conventions в evidence-based prescriptions.

## 3. Research methods

### Базы и источники

Correction-проверка проводилась 14 июля 2026 года через:

- official ACSM page for the 2026 Position Stand;
- supplied PubMed/PMC/DOI canonical identifiers for ACSM 2026, Coleman 2024 and Pancar 2026;
- Springer Nature / Scientific Reports primary article page for Pancar 2026;
- PubMed page for Coleman 2024;
- Springer Nature primary page for Ogasawara 2013;
- citation trail inside Pancar 2026 and Coleman 2024;
- source-to-claim traceability review inside the current DR-A2 ledger.

### Search concepts

- `Pancar deload periods resistance training Scientific Reports 2026 10299`;
- `Coleman one-week deload supervised resistance training PeerJ 2024 e16777`;
- `Ogasawara periodic continued resistance training muscle CSA strength previously untrained men`;
- `Ogasawara continuous periodic strength training 6-month hypertrophy`;
- `Vann active passive recovery high-volume resistance training`;
- `Bickel exercise dosing retain resistance training adaptations`;
- `Tavares reduced training frequency reduced volume resistance training maintenance`;
- `ACSM 2026 resistance training position stand overview of reviews`;
- `talk test exercise intensity review`;
- `wearable energy expenditure validation meta-analysis`.

### Inclusion/exclusion

Included as direct deload/periodic-reduction studies when the study compared a resistance-training programme with a planned interruption or temporary reduction against a continuous or relevant programme structure and reported muscle/strength outcomes.

Excluded adjacent studies when they tested recovery, maintenance, detraining or reduced-volume phases without a temporary deload/reload model capable of answering the DR-A2 deload question.

### ACSM 2026 handling

E01 uses the primary/official record set: PubMed, PMC, DOI and official ACSM page. The ledger records **137 systematic reviews involving over 30,000 participants**. Only broad outcome-domain and evidence-hierarchy conclusions are retained. No personal numeric prescriptions are extracted from E01. [E01](https://pmc.ncbi.nlm.nih.gov/articles/PMC12965823/)

### Deload handling

E22 and E23 now form the direct modern deload correction:

- Coleman 2024: one-week complete RT cessation at midpoint of a 9-week supervised programme in resistance-trained participants. [E22](https://pmc.ncbi.nlm.nih.gov/articles/PMC10809978/)
- Pancar 2026: reduced frequency and set volume during weeks 4 and 8 of an 8-week programme in 19 untrained young men using a randomized within-subject design. [E23](https://www.nature.com/articles/s41598-026-40612-5)

The revised conclusion replaces the previous overly narrow deload framing:

> Direct but narrow evidence exists for complete-cessation and reduced-volume/frequency deload. Evidence remains insufficient to choose an owner-specific protocol or make scheduled deload mandatory.

## 4. Точный applicability profile

Applicability profile unchanged:

- мужчина, 35 лет, около 182 см;
- obesity and approximately 30–35 kg excess mass, актуальная масса private confirmation required;
- not sedentary beginner;
- not long-term complete detraining;
- recent maximum full break approximately three weeks;
- before work-related irregularity, usually about three home strength sessions/week, sometimes four;
- recent exercise details, sets/reps/RIR/RPE and working metrics not fixed;
- older serious sport experience is skill context, not current capacity proof;
- home equipment: two fixed 24 kg dumbbells, ordinary elastic bands, short fabric loop bands, no bench;
- preferred far gym: approximately 6–7.5 km one way by bike;
- near gym: approximately 2.5–3 km one way;
- VR boxing, Beat Saber and other active VR possible;
- bike and VR must be classified by actual response, not distance or calories.

## 5. Established / probable / inference / unknown

| Status | Revised2 conclusion |
|---|---|
| **Established** | Volume has positive dose-response with diminishing returns; no universal machine/free-weight winner; full-body/split equivalence at matched volume is plausible; failure is not mandatory; 1RM is generally reliable; ACSM 2026 is broad primary/official framing. |
| **Probable** | Frequency may help strength but does not prove four beats three; closer-to-failure may help hypertrophy; bands can serve as fallback; active cooldown rarely improves meaningful recovery; complete-cessation and reduced-volume/frequency deload have direct but narrow evidence that does not support mandatory scheduled deload. |
| **Inference** | Rolling schedule, one-variable-at-a-time, last-known-good rollback, no log debt, commute trial count, kilometres-not-dose, gym/home mapping, exercise-specific warm-up after bike, excluding app/headset calories as precise dose. |
| **Unknown** | Final frequency, final split, initial owner dose, personal RIR, exercise list, exact route tolerance, exact VR load, personal deload/rebuild protocol. |

## 6. Frequency: три против четырёх тренировок

E02 remains the primary modern dose-response source. It included 67 studies and 2,058 participants; volume had a positive relation with hypertrophy and strength, while frequency’s hypertrophy effect was compatible with negligible effects and strength effects were positive but diminishing. [E02](https://link.springer.com/article/10.1007/s40279-025-02344-w)

E07 is retained as contextual/background, not as the main modern anchor: after volume equating, frequency superiority for strength was not established in that older meta-analysis. [E07](https://link.springer.com/article/10.1007/s40279-018-0872-x)

### Decision implication

- Three days are evidence-compatible.
- Four days are evidence-compatible only if distribution, practice and session quality improve enough to offset extra commute exposure.
- No final frequency is selected.
- Two days remain fallback/re-entry/minimum branch, not the preferred main architecture.

## 7. Full-body, upper/lower и другие weekly structures

E06 supports treating split and full-body as organizational choices when volume is equated. It does not test this owner’s transition from home equipment to gym while commuting by bike. [E06](https://doi.org/10.1519/JSC.0000000000004774)

Open candidates remain:

- full-body three times per week;
- full-body four times per week;
- upper/lower four times per week;
- rolling function-based sequence;
- hybrid gym/home branch.

A missed-session-resilient architecture should avoid making one missed day remove a key function for a whole calendar week. This is operational inference.

## 8. Переход от домашних тренировок к залу

### Corrected traceability

C33 remains operational inference: a new machine/bar/cable/setup can be unfamiliar even when the pattern is known; technical familiarity must be logged separately from force output. It is not supported by repeated-bout evidence.

E21 is retained only for a narrower empirical point: unaccustomed exercise can create first-bout soreness/damage responses that attenuate with repeated exposure. It is not used as proof of motor learning or technical familiarization. [E21](https://doi.org/10.1249/JES.0000000000000095)

### Decision rule

During the transition:

- record setup, ROM, technique and endpoint separately from load/reps;
- do not interpret first-session awkwardness as pure weakness;
- do not interpret first-session success as proof of recoverability;
- do not use old peak numbers as current capacity.

## 9. Initial volume

Volume direction is supported; exact owner start is not. E02 supports positive volume dose-response with diminishing returns, while E09 shows limited older set-volume evidence. [E02](https://link.springer.com/article/10.1007/s40279-025-02344-w) [E09](https://link.springer.com/article/10.1007/s40279-017-0762-7)

Decision framework:

1. Reconstruct recent actual home dose.
2. Split familiar pattern/familiar implementation, familiar pattern/new implementation, and new implementation.
3. Treat bike and VR as separate load inputs.
4. Select a repeatable testable exposure later in PLAN, not here.
5. Do not escalate frequency, sets, load, proximity-to-failure, bike intensity and VR load simultaneously.

No sets are assigned.

## 10. Intensity, repetitions, RPE/RIR и proximity to failure

E08 supports broad loading ranges for hypertrophy and heavier-load specificity for maximal strength. The E08 corrigendum relationship is noted in the ledger; only broad conclusions are used. [E08](https://doi.org/10.1249/MSS.0000000000002585)

E03 supports different relationships of estimated RIR to strength and hypertrophy. Exact personal RIR remains unknown. [E03](https://link.springer.com/article/10.1007/s40279-024-02069-2)

E04 supports retaining subfailure training as evidence-compatible and rejects mandatory failure as default. [E04](https://doi.org/10.1186/s13102-026-01861-z)

No repetition ranges, percentages, working loads, or personal RIR are prescribed.

## 11. Exercise-selection hierarchy

The hierarchy is retained as synthesis, not a validated scoring instrument:

1. Target movement pattern or muscle function.
2. Joint tolerance.
3. Stability demand.
4. Technical complexity.
5. Safe load creation and adjustment.
6. Objective progression tracking.
7. Fatigue cost.
8. Regression/substitution simplicity.
9. Equipment availability.
10. Owner preference.

E05 directly supports non-ideological use of machines and free weights. No universal modality winner is established; strength specificity matters. [E05](https://link.springer.com/article/10.1186/s13102-023-00713-4)

## 12. Home-equipment branch

Confirmed equipment remains:

- two fixed 24 kg dumbbells;
- ordinary elastic bands;
- short fabric loop bands;
- no bench.

E10 supports elastic resistance as a legitimate strength-training modality in studied protocols, but load standardization is limited. [E10](https://journals.sagepub.com/doi/10.1177/2050312119831116)

Home branch roles:

- fallback during bad logistics;
- re-entry after absence or unstable week;
- temporary reduced load;
- rollback to last-known-good;
- minimum branch when gym commute is not rational.

No home exercise list is created.

## 13. Progression models

E18 provides direct evidence that load progression and repetition progression can both be viable. It does not validate a universal progression algorithm. [E18](https://peerj.com/articles/14142.pdf)

| Model | Status |
|---|---|
| Load progression | Evidence-supported option |
| Repetition progression | Evidence-supported option |
| Double progression | Coaching convention compatible with evidence |
| Set progression | Evidence-compatible, but timing not established |
| ROM/quality progression | Operational option requiring standardized definition |
| Density progression | Optional; changes fatigue and stimulus |
| Same work at lower RPE | Performance signal, not automatically overload |
| One meaningful variable at a time | Attribution/control inference, not proven superior |

## 14. Progress / hold / regress decision matrix

| State | Minimal signal | Decision | Status |
|---|---|---|---|
| Progress | Repeated completion, stable technique, same/lower effort, normal next-day function | Change one measurable variable | Inference |
| Hold | One bad/confounded day, novel setup, weather/sleep changed | Repeat without compensation | Inference |
| Temporary reduction | Comparable repeated underperformance or recovery impairment | Reduce one or more load dimensions | Inference |
| Exercise substitution | Variant-specific intolerance or untrackable technique | Keep function, change variant | Inference |
| Session reduction | Unexpectedly high bike/VR/global fatigue | Do priority work only; no debt | Inference |
| Frequency reduction | Current exposure count not repeatable | Temporarily lower frequency or use home branch | Inference |
| Last-known-good | Escalation broke repeatability | Return to documented stable state | Inference |
| Rebuild | Several unstable weeks or many variables changed | Re-establish baseline then progress | Inference |
| Professional route | Symptoms, unusual/worsening pain, neurological signs, marked functional loss, unresolved clinical facts | Appropriate professional assessment | Established boundary |

## 15. Deload / reduction / rebuild

### Corrected direct evidence

The previous overly narrow deload framing is removed.

**Coleman 2024 / E22 — complete cessation.**  
Both groups improved; there were no appreciable between-group differences in increases of lower-body muscle size, local endurance or power, while continuous training showed greater improvements in isometric and dynamic lower-body strength. This was a single narrow RCT in resistance-trained participants using a one-week complete RT cessation model at the midpoint of a 9-week programme. [E22](https://pmc.ncbi.nlm.nih.gov/articles/PMC10809978/)

**Pancar 2026 / E23 — reduced frequency and volume.**  
Nineteen untrained young men completed a randomized within-subject design. Continuous limbs trained twice weekly for 8 weeks with 6–8 sets per exercise. Deload limbs used the same programme except in weeks 4 and 8, when frequency was reduced to once weekly and volume to 2 sets per exercise; total volume was about 18% lower. Both conditions produced similar increases in muscle thickness and 10RM; no evidence of between-condition superiority was shown. [E23](https://www.nature.com/articles/s41598-026-40612-5)

**Ogasawara 2011 and 2013 / E24–E25 — periodic complete cessation.**  
These older direct studies used 3-week cessation periods between training blocks, mainly bench-press/upper-body models in young/untrained men, and found broadly similar overall hypertrophy/strength outcomes versus continuous training. The 3-week cessation model is longer than typical deload practice and has low/partial applicability to the owner. [E24](https://doi.org/10.1111/j.1475-097X.2011.01031.x) [E25](https://link.springer.com/article/10.1007/s00421-012-2511-9)

### Bounded conclusion

Direct but narrow evidence exists for complete-cessation and reduced-volume/frequency deload. It remains insufficient to choose an owner-specific protocol, make scheduled deload mandatory, or reject reactive hold/reduce/regress/rollback.

### What the evidence does **not** prove

It does not prove:

- deload is beneficial, necessary or superior;
- deload is never useful;
- complete cessation and reduced-volume/frequency deload are interchangeable;
- reactive deload equals planned deload;
- the owner should use any deload week, percentage, schedule or mesocycle;
- missed sessions create training debt.

### Operational answer

- **Mandatory scheduled deload as default:** not supported.
- **Reactive hold/reduce/regress/rollback:** retained as operational options, not proven personal scheme.
- **Training debt after missed sessions:** rejected as an operationally unsafe/unclear acute-load spike.

## 15a. Bounded backward/forward deload citation sweep

### Included direct studies

| Study | Included reason | Boundary |
|---|---|---|
| Ogasawara 2011 / E24 | Direct periodic training versus continued training with 3-week cessation; muscle CSA/strength outcomes | Upper-body bench-press model, previously untrained men, older small study, 3-week cessation not typical deload |
| Ogasawara 2013 / E25 | Direct 24-week continuous versus periodic training with 6-week training blocks and 3-week detraining periods | Bench press/upper body only, young men, 1RM testing every 3 weeks may be a stimulus, long cessation |
| Coleman 2024 / E22 | Direct one-week complete cessation deload at programme midpoint | Trained participants, lower-body outcomes, high-volume programme, complete cessation only |
| Pancar 2026 / E23 | Direct reduced-frequency/volume deload during weeks 4 and 8 | 19 untrained young men, within-subject design, two exercises, 10RM and thickness only |

### Excluded adjacent studies

| Study | Exclusion reason |
|---|---|
| Vann 2021 / E26 | Compared one week active versus passive recovery after high-volume RT and molecular/hypertrophy markers, but no subsequent training/reloading cycle; does not answer whether deload within a programme improves later adaptations. |
| Bickel 2011 / E27 | Reduced-volume maintenance after a training phase; not a temporary deload followed by reload and not a continuous-vs-deload model for programme adaptation. |
| Tavares reduced-training maintenance study / E28 | Reduced-frequency/volume maintenance/detraining model summarized in Pancar; lacks a maintained-full-volume comparator and temporary-reduction-plus-reload model, so no direct deload conclusion. |
| Taper/peaking studies | Excluded because tapering before competition has a different aim from deloading inside a training cycle. |
| General detraining-only studies | Excluded unless they directly compare periodic training/cessation versus continuous RT, because they do not answer planned deload architecture. |

No earlier Ogasawara, Vann or related periodic/recovery studies are silently ignored; they are either included as direct but low-applicability periodic-cessation studies or excluded adjacent with reasons.

## 16. Дальний зал / ближний зал / дом

| Branch | Potential benefit | Potential cost | Decision role |
|---|---|---|---|
| Far gym, 12–15 km bike/day | Preferred; likely better equipment | More route exposure and weather/terrain variability | Primary experiment, not pre-rejected |
| Near gym, 5–6 km bike/day | Lower commute burden | May be less preferred/equipment differs | Rational regression if far route repeatedly degrades outcomes |
| Home | No commute; controlled logistics | Fixed 24 kg dumbbells, bands, no bench | Real fallback/re-entry/rollback branch |

No exact route-trial number is evidence-based. A repeated-exposure rule is operational inference only.

## 17. Bicycle commute as load

E11 supports not rejecting cycling a priori: concurrent aerobic + strength training did not compromise maximal strength or hypertrophy on average. It also indicates explosive strength may be attenuated and does not establish a universal cycling advantage over running. [E11](https://link.springer.com/article/10.1007/s40279-021-01587-7)

**Boundary correction:** “kilometres are not an exact dose” is not a conclusion directly established by E11. It is an operational/measurement inference from the need to track internal and contextual load using session-RPE, talk test and condition fields. [E19](https://doi.org/10.3389/fnins.2017.00612) [E20](https://doi.org/10.1097/HCO.0000000000000097)

### Required commute log

- planned route;
- actual route;
- duration there/back;
- terrain;
- weather/heat/wind;
- RPE there/back;
- talk test;
- leg fatigue before gym;
- quality of main strength work;
- state after return;
- next-day function.

No kilometre-to-dose conversion is made.

## 18. Bicycle as warm-up/cooldown

### Warm-up

A calm ride can plausibly replace the **general aerobic** part of a pre-gym treadmill warm-up when it increases readiness without fatigue. This remains inference from general warm-up evidence. [E17](https://doi.org/10.1519/JSC.0b013e3181c643a0)

The revised C25 remains explicitly downgraded: there is no direct evidence in this file that a bicycle commute replaces exercise-specific warm-up/ramp-up sets for the first demanding resistance exercise.

### Cooldown

A calm return ride can be a low-intensity transition. It is not automatically a recovery-enhancing cooldown. E12 suggests active cooldown generally has limited effect on meaningful recovery outcomes, despite possible faster lactate clearance. [E12](https://link.springer.com/article/10.1007/s40279-018-0916-2)

## 19. VR integration

E14 shows that iVR exertion can differ significantly by implementation even within related modes, so VR must be classified by actual response. [E14](https://games.jmir.org/2020/3/e17972/)

VR classification fields:

- exact app/mode;
- duration;
- session-RPE;
- talk test;
- ventilation;
- arm/shoulder fatigue;
- next-day response;
- subsequent strength performance.

**Boundary correction:** E13 validates wrist/arm activity-monitor energy-expenditure estimates against criterion methods; it does not directly validate app/headset calorie estimates. Therefore, excluding app/headset calories as precise dose is retained as a conservative operational extrapolation, not as a direct empirical validation claim. [E13](https://doi.org/10.1136/bjsports-2018-099643) [E14](https://games.jmir.org/2020/3/e17972/)

## 20. Testing and retesting

E15 supports that 1RM testing is generally reliable, but reliability is not necessity. Exercise complexity and familiarity can affect reliability/interpretation. [E15](https://link.springer.com/article/10.1186/s40798-020-00260-z)

Testing options remain:

- technical baseline;
- repetition-quality baseline;
- load × reps × RPE/RIR baseline;
- fixed-effort performance;
- submax/e1RM;
- optional 1RM when familiar, screened and decision-relevant.

No maximal testing is required.

## 21. Strength-specific adherence and missed-session handling

Operational rules retained as `Inference`:

- rolling sequence over rigid calendar debt;
- no automatic catch-up doubling;
- mapped gym/home variants;
- minimum/shortened session concept without prescribing contents;
- preserve actual completed work, not planned work, in logs;
- branch switch does not erase progression history.

No direct comparative RCT for these architecture rules was identified.

## 22. Missing private owner facts

Still unknown and not filled:

- current body mass;
- resting BP/HR;
- exertional symptoms;
- known cardiovascular, metabolic or renal conditions;
- medication affecting HR, BP, glucose or exercise tolerance;
- injuries, joint pain, ROM limits;
- exact recent home training content;
- current working metrics;
- bike route time/terrain/weather;
- exact gym equipment;
- exact VR apps/modes.

These facts are private and should not be published.

## 23. Evidence conflicts

1. Volume helps, but diminishing returns prevent “more is automatically better.”
2. Frequency may help strength, but four days are not proven superior to three.
3. Closer-to-failure may help hypertrophy, but failure is not mandatory.
4. Heavy loading is strength-specific, but broad loads can support hypertrophy.
5. Machines and free weights show specificity, not universal superiority.
6. Concurrent aerobic work is neutral for maximal strength/hypertrophy on average, but hard same-session commute may still impair acute quality.
7. Deload evidence includes complete-cessation and reduced-volume/frequency direct studies, but it is narrow and does not support mandatory scheduled deload or personal deload protocol.
8. Active cooldown may clear lactate faster, but meaningful recovery benefits are limited/inconsistent.
9. VR can be cardiovascular and/or local fatigue, but actual session classification is required.
10. Operational conventions are retained only as inference.

## 24. Evidence ledger

The full revised2 ledger is provided as:

`DR-A2_evidence_ledger_2026-07-14-revised2.xlsx`

It contains four sheets:

1. **Evidence ledger** — 42 claims and all 25 required fields.
2. **Decision framework** — compact progress/hold/regress and branch framework.
3. **Source index** — 28 sources, including DOI, PMID, PMCID where available, URLs, verification notes and source disposition.
4. **Status glossary** — definitions including `Not applicable — operational synthesis/owner context`.

No orphan source remains: contextual/excluded adjacent sources are explicitly marked with their disposition in Source index and/or the citation sweep.

## 25. Gaps for DR-A3 nutrition

Unchanged boundaries:

- energy intake and deficit strategy;
- protein targets and distribution;
- weight-loss rate;
- recomposition strategy;
- fueling/hydration around bike + lifting;
- body composition monitoring;
- medication/glucose considerations;
- supplements, if separately justified.

No calorie deficit or supplement is prescribed here.

## 26. Gaps for DR-A4 cardio, mobility, warm-up and stretching

Still requires separate evidence synthesis:

- total aerobic dose including commute and VR;
- cycling progression independent of strength progression;
- warm-up protocol details;
- mobility/ROM assessment;
- stretching timing/purpose;
- heat/wind/terrain safety;
- cardio beyond commute.

## 27. Gaps for DR-A5 recovery, sleep, adherence and re-entry

Still separate:

- sleep quantity/quality;
- work stress;
- illness return;
- behavioural adherence;
- detailed re-entry protocols;
- subjective recovery monitoring;
- when fatigue/pain/symptoms require professional assessment.

## 28. Overall confidence

| Domain | Confidence | Reason |
|---|---|---|
| 3 vs 4 superiority | Low for superiority; moderate for no proven superiority | E02/E07 do not directly select a branch |
| Full-body vs split | Moderate | E06 supports similar outcomes at matched volume |
| Volume direction | Moderate-high | E02 current dose-response synthesis |
| Personal starting volume | Low/unknown | Depends on private recent dose and first observations |
| Failure not mandatory | Moderate-high | E03/E04 support subfailure-compatible framework |
| Personal RIR | Unknown | Not derivable from current evidence |
| Machines/free weights | Moderate-high | E05 direct modality meta-analysis |
| Home bands | Moderate | E10 supports strength outcomes but load tracking limited |
| Complete-cessation deload default | Moderate against default use | E22 plus older Ogasawara studies do not show superiority and are narrow |
| Reduced-volume/frequency deload | Low-moderate direct evidence; no personal prescription | E23 direct but small, untrained, within-subject and limited exercises |
| Owner-specific deload protocol | Low/unknown | Direct evidence is narrow and not owner-context specific |
| Cycling compatibility | Moderate for chronic compatibility; low for specific route | E11 not a commute trial |
| Kilometres as dose | Rejected as exact metric by operational inference | Requires internal/contextual logging |
| Cycling warm-up | Low-moderate | General warm-up evidence only; C25 downgraded |
| VR classification | Low-moderate | E14 supports variability; not exact owner apps |
| App/headset calories as precise dose | Rejected by conservative extrapolation | E13 is wrist/arm validation, not headset/app validation |
| 1RM reliability | High | E15 reliability review |
| Rolling/no-debt/last-known-good | Low direct evidence, strong operational rationale | Inference only |

### Final bounded conclusion

Revised2 DR-A2 supports an evidence-led, branch-preserving architecture. It does not activate a programme. The next PLAN session must review private owner facts, reconstruct recent home dose, inspect gym equipment, decide trade-offs and only then assemble a personal starter programme.
