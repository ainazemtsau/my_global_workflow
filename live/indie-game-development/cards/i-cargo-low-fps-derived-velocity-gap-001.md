---
id: i-cargo-low-fps-derived-velocity-gap-001
kind: issue
pos: 16
level: execution
route: work
---

## issue
CAPTURE: в опубликованном cargo-стенде `AuthoritativeCargoRoster.DeriveVelocity` выводит скорость из разницы поз, и два тика в одном low-FPS кадре могут потерять гашение. Ограничение не чинилось, отдельного решения по нему нет.

## review_when
Если будущая ставка снова допускает cargo-физику: до заявления о готовом поведении решить, принимать ли ограничение или расширять шов скоростью.

## evidence
history/2026-08-04-s-work-g-6b13-a4-close-verification-checkpoint-002.md §evidence 9; `docs/results/c-exec-two-carry-one-physical-cargo-proba-001.md`.

END_OF_FILE: live/indie-game-development/cards/i-cargo-low-fps-derived-velocity-gap-001.md
