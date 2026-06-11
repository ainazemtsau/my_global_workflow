# 00 Phase Brief

```yaml
phase:
  id: ai-nutrition-operating-layer
  name: "Собрать AI-операционный слой питания без тяжёлого трекинга"
  state: active
  started_at: "2026-05-12"
  direction: directions/health-and-beauty
  workflow_version: vNext-R
```

## Critical constraint

Нет устойчивого AI-процесса питания: меню, рецепты, отклонения, дневные коррекции, долгосрочные выводы и сохранение состояния не связаны в один рабочий слой. MacroFactor/detailed tracking создаёт лишний friction, а один длинный ChatGPT-chat со временем деградирует.

## Minimum outcome

Есть AI Nutrition Operating Layer v0: state packet, active menu object, prompt modes, exception correction, recipe/prep builder, review/state update protocol, storage rules, restart/context refresh rules, and sample flows.

## Validation signal

Система проходит типовые сценарии:

1. Составить/обновить меню.
2. Дать совет по текущему дню.
3. Скорректировать остаток дня после переедания или off-menu eating.
4. Добавить рецепт/prep note.
5. Сделать day/week summary и обновить persistent state.

## Scope in

- AI nutrition command process.
- Nutrition State Packet.
- Active Menu object.
- Daily Nutrition Operator mode.
- Menu Architect mode.
- Recipe / Prep Builder mode.
- Review / State Update mode.
- Exception-only tracking.
- Day correction logic.
- Storage/save protocol.
- Restart/context refresh rules.
- Existing menu review.
- Recipe/prep support.
- Gradual use of air fryer, multicooker, vacuum sealer where useful.

## Scope out

- MacroFactor-centered workflow.
- Self-hosted food tracker setup.
- Detailed calorie/macro ledger.
- Tracking every meal by default.
- API/import automation.
- Perfect Notion/Trillium database design.
- Huge recipe vault.
- Daily food log as source of truth.
- Medical/clinical nutrition layer.
- Full health architecture redesign.
