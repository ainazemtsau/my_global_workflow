# 17 Independent Validation / Review Protocol

Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Side Amendment SA-01C — Validation, Review, Repair, and Concrete Project Setup Boundary Installed at: 2026-05-10T04:56:01.1979556+03:00 Source input: ChatGPT SA-01C installable source output, 2026-05-10 Authority: Trilium canonical after read-back Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

## 1\. Purpose

This note defines when independent validation/review is required and what it must check.

Independent review is required for high-risk, complex, cross-module, security-sensitive, or repeated-failure work.

SA-01A/B/C install governance/contracts only. They do not configure any concrete repo/project.

Concrete project setup happens later per project through CODEX\_PROJECT\_SETUP.

## 2\. What counts as independent review

Independent review means a review pass separate from the implementation pass.

It may be performed by:

*   a human reviewer
*   a separate Codex reviewer mode
*   a specialized subagent
*   a separate model/thread assigned only to review
*   a project-specific review tool or process defined by CODEX\_PROJECT\_SETUP

Ordinary implementer self-review does not count as independent review.

If independent review is required but unavailable, Codex must disclose this and escalate. Codex may not claim that required independent review happened when it did not.

## 3\. Required triggers

Independent review is required when any trigger applies:

| Trigger | Examples |
| --- | --- |
| High-risk work | Data loss risk, irreversible changes, payment/auth/permissions, production-affecting changes, critical workflow contracts. |
| Complex work | Multi-step algorithm changes, broad refactors, unclear acceptance, dependency-sensitive changes. |
| Cross-module work | Changes spanning module boundaries, shared interfaces, shared schemas, routing, storage, or validator contracts. |
| Security/privacy-sensitive work | Secrets, PII, auth, permissions, logging, memory storage, external integrations, policy-sensitive data. |
| Repeated failure | Same validator/review/acceptance failure repeats after repair, or two repair attempts are needed. |
| Architecture-sensitive work | Module map changes, module knowledge changes, AGENTS.md changes, .codex/config.toml changes, workflow contracts. |
| Test-quality risk | Coverage-only tests, shallow tests, missing acceptance mapping, or suspiciously broad mocks. |
| Tool-binding uncertainty | Required Task Master, Serena, Basic Memory, MCP, validators, or subagent binding is missing or ambiguous. |

## 4\. Review checklist

Independent review must check:

1.  Acceptance fit
    
    *   Does the result satisfy the accepted criteria?
    *   Are acceptance criteria mapped to evidence?
    *   Are exclusions and residual risks explicit?
2.  Architecture fit
    
    *   Does the work fit the intended architecture?
    *   Does it avoid unnecessary redesign?
    *   Does it avoid scope expansion?
3.  Module boundary fit
    
    *   Are module interfaces respected?
    *   Are cross-module effects understood?
    *   Are module map/module knowledge updates required?
4.  Test quality
    
    *   Are tests meaningful?
    *   Do they cover normal, edge, negative, regression, and module-boundary cases where relevant?
    *   Are property-based or mutation tests considered where available and relevant?
    *   Were validators run and failures disclosed?
5.  Maintainability
    
    *   Is the implementation understandable and localized?
    *   Are names, structure, and dependencies maintainable?
    *   Does it avoid overfitting to tests?
6.  Security/privacy
    
    *   Are secrets, PII, auth, permissions, logs, and memory writes handled safely where relevant?
    *   Does Basic Memory avoid storing content outside its project/module technical recall policy?
    *   Does the work avoid leaking private or sensitive information?
7.  Tool and authority boundaries
    
    *   Task Master AI is graph substrate, not DONE authority.
    *   Basic Memory is project/module technical recall only, not Trilium canon.
    *   Serena is trigger-based semantic code/navigation/refactor support.
    *   Validators and read-back evidence remain required where applicable.

## 5\. Review outcomes

Review must return one of:

| Outcome | Meaning |
| --- | --- |
| PASS | No blocking issue found; work may proceed to final validation. |
| PASS\_WITH\_NONBLOCKING\_NOTES | Minor issues or risks exist but do not block acceptance. |
| NEEDS\_PATCH | Specific fix required; Codex may enter repair loop if attempt budget remains. |
| NEEDS\_INPUT | Human/project input required before safe continuation. |
| FAIL | Work does not meet acceptance or creates unacceptable risk. |
| STUCK | Tooling, state, or authority conflict prevents safe completion. |

## 6\. Review packet fields

Independent review must produce a review packet containing:

*   reviewer identity/type
*   review scope
*   triggering condition
*   artifacts reviewed
*   acceptance fit result
*   architecture fit result
*   module boundary result
*   test quality result
*   maintainability result
*   security/privacy result where relevant
*   tool/authority boundary result
*   issues found
*   required patches
*   nonblocking notes
*   final review outcome

Codex must include this review packet or a concise faithful summary in the Codex Return Packet.

## 7\. Red flags requiring escalation

Codex must escalate when review finds:

*   acceptance mismatch
*   unsafe or destructive change
*   missing required validator
*   missing acceptance-to-test mapping for code work
*   tests that exist only for count/coverage
*   unapproved module boundary change
*   unapproved concrete setup change
*   Basic Memory used as canonical authority
*   Task Master status used as DONE proof
*   Serena findings used as correctness proof without validators/review
*   security/privacy uncertainty
*   repeated failure after repair
*   review independence required but unavailable

## 8\. Boundary with CODEX\_PROJECT\_SETUP

This protocol defines when review is required and what review must check.

It does not create concrete reviewers, subagents, MCP bindings, repo configs, validation commands, Task Master ledgers, Serena bindings, Basic Memory namespaces, module maps, or module knowledge.

Those concrete bindings are created later per project through CODEX\_PROJECT\_SETUP.

## 9\. Codex Return Packet review evidence

When independent review is required, Codex must return:

*   why review was triggered
*   who/what performed the review
*   review packet or summary
*   blocking findings
*   nonblocking findings
*   patches made in response
*   validators rerun after patch
*   final status
*   unresolved risks

Codex cannot claim DONE for review-triggering work unless required review is completed or the absence of review is escalated.