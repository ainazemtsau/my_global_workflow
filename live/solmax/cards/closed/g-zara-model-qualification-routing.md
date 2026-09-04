---
id: g-zara-model-qualification-routing
_kind: node
_parent: g-zara
status: dropped
label: Проверенная экономичная маршрутизация
hook: Каждая операция использует самый дешёвый доказанно подходящий access path.
_pos: 2
---

## goal
For each typed operation/workflow, Zaratustra recommends and uses the least
expensive available model-provider-access combination that has demonstrated
the required quality, tools, privacy and safety for that exact configuration.
## done_when
1. The executor registry separates model family, concrete variant/snapshot,
   provider, access mode (`local | subscription | cloud_api`), runtime/adapter,
   tools, context limits, privacy, effects, availability, quota and cost.
2. Eval results qualify an exact combination of procedure/workflow version,
   prompt/instruction version, model/provider/access, adapter, tools and
   context policy; there is no global "best model" rating.
3. Routing uses only typed requirements and qualification records, never
   Python interpretation of the payload prose.
4. Selection order is privacy/safety, required capabilities/quality, then
   cost/quota/latency. Fallback is pre-authorized or explicitly asks/blocks;
   no silent provider substitution occurs.
5. At least two real access paths work, including a paid subscription path;
   local and multiple cloud/API/subscription providers (including Qwen-family
   offerings) are representable without kernel changes.
6. The owner can override a recommendation only with another qualified
   option; an unqualified combination gives a plain explanation and evidence
   link.
7. Each qualification records its evidence-retrieval date, effective
   provider/access policy version and expiry/recheck condition. A material
   change of workflow, instruction, adapter, tool set, model snapshot, terms,
   training/data-use setting, retention/locality, authentication/account or
   workspace type, automation scope, availability, quota, price or tool policy
   invalidates the affected qualification until rerun.
8. The web view explains recommendations and alternatives in owner language
   and exposes the supporting benchmark on demand.
## why
This sends simple work to local/cheap models, reserves frontier subscriptions
for hard planning and makes model switching measurable without weakening
privacy or results.
## edge
The owner already has real repetitive workloads and several subscriptions;
qualification can use his tasks rather than public leaderboards that ignore
his tools, files and rules.
## risk
Maintaining benchmarks may cost more than routing saves. If qualification does
not change real choices after several workflows, reduce it to a manually
maintained allowed/recommended list with regression gates.
## журнал
2026-09-04 · dropped — содержание перешло в волну 4 (g-zara-w4-surfaces): таблица уровней и исполнителей в реестре, дешёвая модель на сводках. Три отложенные идеи владельца перевешены туда же. · history/2026-09-04-s-solmax-zaratustra-v2-map-055.md
2026-08-13 · map Zaratustra finalized: owner-approved six-node 1→6 roadmap recorded with four evidence-backed boundaries, old unfinished operating-manager branch dropped, and Health converge opened as the sole frontier · history/2026-08-13-s-solmax-zaratustra-map-finalize-026.md
END_OF_FILE: live/solmax/cards/closed/g-zara-model-qualification-routing.md
