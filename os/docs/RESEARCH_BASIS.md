# Research basis — почему OS устроена именно так

Сводка трёх исследований (июнь 2026): практики работы с фронтирными ассистентами, методики планирования/отсечения скоупа, разборы существующих LLM-workflow систем. Каждый пункт: источник → механизм OS, который из него следует.

## 1. Сессии и контекст

| Факт (источник) | Механизм OS |
|---|---|
| Единственный выживший дизайн долгих циклов — свежий контекст на каждую итерацию, состояние только в файлах: Anthropic harnesses, Ralph loop; AutoGPT-поколение деградировало без внешнего done-условия ([Anthropic](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), [ghuntley.com/ralph](https://ghuntley.com/ralph/), [taivo.ai](https://www.taivo.ai/__why-autogpt-fails-and-how-to-fix-it/)) | Сессия = свежий контекст; KERNEL §2 (контракт сессии); RESULT обязателен |
| «Assume interruption»: несохранённое состояние не существует ([memory tool docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)) | KERNEL §1; писатель коммитит каждый RESULT |
| Эффективная длина контекста кратно меньше заявленной; деградация от длины и дистракторов ([NoLiMa](https://arxiv.org/abs/2502.05167), [Lost in the Middle](https://arxiv.org/abs/2307.03172), [Context Rot](https://research.trychroma.com/context-rot)) | Малые state-файлы «на один экран»; брифинг вместо реплея истории; правила в начало, CALL в конец (адаптер ChatGPT) |
| Раздутые файлы правил игнорируются; каждая строка должна окупаться; противоречия инструкций бьют по сильным моделям сильнее ([Claude Code best practices](https://code.claude.com/docs/en/best-practices), [GPT-5 prompting guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide), [ETH: context files могут вредить](https://arxiv.org/abs/2602.11988)) | Бюджеты: ядро ≤1500 слов, play ≤600 (KERNEL §7); единый порядок авторитета (шапка KERNEL) |
| После двух неудачных исправлений чистая сессия с лучшим промптом обыгрывает длинную с накопленными правками ([Claude Code best practices](https://code.claude.com/docs/en/best-practices)) | Two-strikes rule (KERNEL §2) |
| Manus: перечитывание/переписывание плана в хвост контекста — механизм против дрейфа цели ([Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)) | «Recite» — первый шаг work/shape/research |

## 2. Делегирование и проверка

| Факт | Механизм OS |
|---|---|
| Универсальная схема задачи: Goal / Context / Constraints / Done-when ([Codex best practices](https://developers.openai.com/codex/learn/best-practices), [делегационный контракт Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system), [Devin docs](https://docs.devin.ai/essential-guidelines/instructing-devin-effectively)) | CALL = ровно эти поля + return + budget (KERNEL §4) |
| Галлюцинированное «выполнено» измеримо реально ([GPT-5 system card](https://cdn.openai.com/gpt-5-system-card.pdf)); done только по запускаемой проверке/доказательству ([Claude Code docs](https://code.claude.com/docs/en/best-practices)) | Гейт G5: evidence, не заявление |
| Проверять должен свежий контекст, не автор; формулировать как попытку опровергнуть (сикофантия: [SycophancyEval](https://arxiv.org/abs/2310.13548)) | review в отдельной сессии, шаг «verify by refutation» (G5) |
| 44% отказов мультиагентных систем — спецификация, дальше — верификация, не «слабые модели» ([MAST](https://arxiv.org/abs/2503.13657)) | Усилие OS вложено в пакеты и review, а не в новых агентов |
| Запись — однопоточная: один владелец артефакта; параллельные сессии советуют, не пишут ([Cognition](https://cognition.ai/blog/dont-build-multi-agents)) | Только writer пишет в live/**; research-дети не трогают состояние |
| Надёжность, не способность — ограничитель: 80%-горизонт в 4-6 раз короче 50%-го; messy-задачи роняют всё ([METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)) | Задача ≤ полдня сфокусированной работы; бюджет в каждом CALL; ранний выход «blocked» |

## 3. Планирование и скоуп

| Факт | Механизм OS |
|---|---|
| Appetite прежде плана; дедлайн нерастяжим, режется только скоуп; circuit breaker убивает не влезшее ([Shape Up](https://basecamp.com/shapeup/1.2-chapter-03), [гл. 9](https://basecamp.com/shapeup/2.3-chapter-09)) | Гейт G3: операция «продлить» не существует; review хоронит бет по истечении |
| Scope hammering: must-have легитимен, только если пережил задокументированную попытку выкинуть ([Shape Up гл. 14](https://basecamp.com/shapeup/3.5-chapter-14)); алгоритм Маска: «не вернул 10% вырезанного — резал мало» ([startuparchive](https://www.startuparchive.org/p/elon-musk-explains-his-5-step-algorithm-for-running-companies)) | Гейт G6 (cut list обязателен) + add-back check в review |
| WIP-лимиты работают по закону Литтла; переключение контекста съедает до 20-40% ([APA](https://www.apa.org/topics/research/multitasking)) | Гейт G1; pulse-пункт 7 о распылении владельца |
| Rolling wave: детально — только ближняя волна; детальные планы дальнего будущего гниют ([PMI](https://www.pmi.org/learning/library/manage-innovation-programs-rolling-wave-3515)) | Гейт G2: задачи только в активном бете; дерево — только outcomes |
| Riskiest assumption first ([Lean/RAT](https://modelthinkers.com/mental-model/riskiest-assumption-test)); kill-критерии «метрика+порог+дата», написанные заранее ([Annie Duke, Quit](https://www.tobysinclair.com/post/summary-quit-by-annie-duke)); пре-мортем даёт ~30% к выявлению причин ([Klein, HBR](https://hbr.org/2007/09/performing-a-project-premortem)) | G6 (RAT-задача), G4 (kill_by), frame шаг 4 (пре-мортем ≥5) |
| Планы врут систематически; лечится внешним взглядом по референс-классу ([Flyvbjerg](https://arxiv.org/pdf/1302.2544)) | frame шаг 2 и shape шаг 2 (outside view, сравнимые случаи) |
| Параллельные варианты до выбора дают лучший результат и больше дивергенции, чем итерация одного варианта; set-based подход Toyota ([Dow et al. 2010](https://dl.acm.org/doi/10.1145/1879831.1879836), [Sobek & Ward](https://sloanreview.mit.edu/article/toyotas-principles-of-setbased-concurrent-engineering/)) | shape шаг 3 (2–3 структурно разных подхода до выбора); map шаг 2 (≥1 неочевидный путь в карточках) |
| Инди-реальность: медианная игра ~$249; третьи игры зарабатывают ~2x дебютов; Steam-страница за 6-12 мес до релиза; демо+Next Fest = измеримая валидация ([VGI report](https://app.sensortower.com/vgi/assets/reports/VGI_Global_Indie_Games_Market_Report_2024.pdf), [howtomarketagame](https://howtomarketagame.com/2025/03/10/when-should-i-post-my-steam-coming-soon-page/)) | Не правило OS, а контент для outside_view и knowledge/ игрового направления |
| Еженедельный обзор — петля, без которой система перестаёт быть доверенной ([GTD weekly review](https://gettingthingsdone.com/wp-content/uploads/2014/10/Weekly_Review_Checklist.pdf)); стадийные гейты Go/Kill по заранее заданным критериям ([Cooper, Stage-Gate](https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/)) | pulse (9 булевых пунктов); review как гейт бета |

## 4. Человек в петле и мета-работа

| Факт | Механизм OS |
|---|---|
| Частые подтверждения вырождаются в штамповку; человек, мониторящий надёжную автоматику, перестаёт ловить отказы ([Parasuraman & Manzey](https://journals.sagepub.com/doi/10.1177/0018720810376055), [approval fatigue](https://aipatternbook.com/approval-fatigue)) | Решения — редкие и батчем (G7); тиры действий, тир-0/1 не прерывают (adapters/autonomy) |
| Рабочая модель контакта: async-инбокс с verbs approve/edit/reject/answer ([12-factor-agents](https://github.com/humanlayer/12-factor-agents), [agent-inbox](https://github.com/langchain-ai/agent-inbox)); продакшн-прецедент тиров — Operator ([OpenAI](https://openai.com/index/introducing-operator/)) | decisions-инбокс в NOW.md; стадия 3 автономии |
| Люди систематически не замечают, что система им в минус (METR RCT: −19% при ощущении +20%) ([METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)) | pulse меряет минуты-владельца vs закрытые беты («honesty instrument») |
| Мета-работа — главный убийца персональных систем: второй мозг-«мавзолей», GTD как вторая работа; выжившие системы держат жёсткие бюджеты простоты и меняются только после повторного отказа простой формы ([Westenberg](https://www.joanwestenberg.com/i-deleted-my-second-brain-692aa40d59d5f06dd5131e43/), [New Yorker](https://www.newyorker.com/tech/annals-of-technology/the-rise-and-fall-of-getting-things-done), [spec-kit constitution](https://github.com/github/spec-kit/blob/main/spec-driven.md)) | KERNEL §7 (бюджеты + правка только по ≥2 трениям); 6 типов файлов; knowledge только с потребителем; G8 (intake) |
| Конвергенция git+markdown как памяти агентов (Anthropic, [Letta context repositories](https://www.letta.com/blog/context-repositories), [Cline memory bank](https://github.com/cline/prompts/blob/main/.clinerules/memory-bank.md), [AGENTS.md](https://agents.md/)); фикс-набор файлов с ролями «медленное/быстрое» состояние | live/<id>/ : CHARTER (медленное) / TREE / NOW (быстрое) / LOG / history / knowledge |

Полные отчёты трёх исследований — в истории сессии аудита; сюда вынесено всё, что несёт нагрузку в дизайне.

END_OF_FILE: os/docs/RESEARCH_BASIS.md
