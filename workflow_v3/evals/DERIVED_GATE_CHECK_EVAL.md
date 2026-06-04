# Derived Gate Check Eval

status: active_eval

## Purpose

Validate that derived gate checks are generated from real procedure boundaries and remain internal checks rather than separate runtime controllers.

## PASS checks

- Gate is generated from a boundary crossing, evidence gap, risk, or required decision.
- Required evidence or decision is named.
- Pass, fail, defer, or replan result is visible.
- Blocked action is explicit.
- Gate type is one of strategy, discovery, delivery_flow, verification, interface_dependency, risk_gate, or memory_learning.

## WARN checks

- Gate passes with risk, and residual risk is named.
- Gate is deferred with a clear trigger for recheck.

## FAIL checks

- Hardcoded domain gate appears without a boundary reason.
- Irreversible, public, external, or mutation action lacks a gate.
- Gate behaves like separate route authority.

## Required recovery/repair action

Stop the blocked action, produce the needed evidence or decision request, and resume only through the admitted procedure boundary.

END_OF_FILE: workflow_v3/evals/DERIVED_GATE_CHECK_EVAL.md
