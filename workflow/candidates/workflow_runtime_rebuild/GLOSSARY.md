# Workflow Runtime Rebuild Glossary

status: candidate

Этот glossary короткий и служит только для Stage 1 candidate package.

## Terms

- Accepted State: явно принятое состояние проекта в canonical storage; не живет только в чате.
- Action Inbox: список candidate actions, которые требуют внимания, но не управляют workflow самостоятельно.
- Action Inbox Item: отдельный candidate action with reason, relation, priority and when_to_run or stale condition.
- Active Front: выбранная часть Direction Spine, которая сейчас движется.
- Adapter: role implementation для ChatGPT, Codex, Claude Code, Deep Research, GitHub, future AI providers or human actions.
- Acceptance Decision: явное решение принять, отклонить или вернуть результат на доработку.
- Check Job: проверка, которую можно запланировать или выполнить для evidence, freshness or quality.
- Direction Spine: простая ось направления с Root Result, Success Conditions, Spine Points and Tracks.
- Evidence: проверяемый результат Run, который поддерживает acceptance review.
- Handler: процесс, который реагирует на Signal и создает candidate action.
- Launch Packet: ограниченный пакет запуска работы для adapter; Stage 1 не задает detailed schema.
- Memory: продвинутые сведения, полезные для продолжения проекта.
- Memory Candidate: сведения, которые могут стать Memory после promotion.
- Next Move: точная следующая инструкция после material chat or decision.
- Node: bounded work item inside local Work Graph.
- Result Packet: возвращенный результат adapter; Stage 1 не задает detailed schema.
- Root Result: главный результат direction.
- Run: конкретное исполнение Work Contract.
- Signal: факт, который сам по себе не меняет state.
- Spine Point: крупная точка движения на Direction Spine.
- Success Conditions: условия, по которым можно оценить достижение Root Result.
- Track: линия внимания внутри direction.
- Work Contract: ограниченный контракт для выполнения node.
- Work Graph: локальный граф work nodes for Active Front.

## Legacy mapping

legacy mapping is only a bridge. old workflow is not the baseline for this candidate package.

- Ledger -> Accepted State / canonical accepted record.
- Obligation -> Work Contract or accepted work item depending on layer.
- Operator -> Run / role execution.
- Receipt -> Evidence / acceptance candidate.
- Verify + Commit -> Acceptance Decision / accepted transition.
- Review Queue -> Action Inbox + Check Jobs.
- Event -> Signal.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/GLOSSARY.md
