# 16 Test Quality and Review Policy

Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Side Amendment SA-01C — Validation, Review, Repair, and Concrete Project Setup Boundary Installed at: 2026-05-10T04:56:01.1979556+03:00 Source input: ChatGPT SA-01C installable source output, 2026-05-10 Authority: Trilium canonical after read-back Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

## 1\. Purpose

This note defines the minimum quality bar for tests and validation used in Codex-supported work.

Tests written only for count, coverage, or appearance are forbidden.

Code work requires acceptance-to-test mapping. Codex must show which acceptance criteria are covered by which tests, validators, reviews, or explicit residual-risk notes.

SA-01A/B/C install governance/contracts only. They do not configure any concrete repo/project.

Concrete project setup happens later per project through CODEX\_PROJECT\_SETUP.

## 2\. Test quality rule

A useful test must be capable of detecting a meaningful defect in the accepted work.

A test is low-value or invalid when it:

*   exists only to increase test count
*   exists only to increase coverage percentage
*   asserts that a mock was called without checking behavior
*   duplicates implementation logic instead of expected behavior
*   tests a constant or import without validating a user-visible or module-visible outcome
*   has no clear failure condition
*   can pass when the feature is broken
*   relies on excessive snapshots without targeted assertions
*   ignores edge, negative, regression, or module-boundary behavior where relevant
*   weakens existing validation
*   encodes stale behavior that conflicts with accepted criteria
*   hides defects behind over-mocking

Coverage is a signal, not DONE authority.

## 3\. Acceptance-to-test mapping

For code work, Codex must include an acceptance-to-test map before claiming completion.

Minimum map fields:

| Field | Requirement |
| --- | --- |
| Acceptance criterion | Exact criterion from the human brief, stage packet, Codex Wave Card, or issue/task. |
| Test/validator/review evidence | Test file, test name, command, validator, manual check, or review item. |
| Category | Normal, edge, negative, regression, module-boundary, property-based, mutation, security/privacy, performance, or manual. |
| Result | pass, fail, skipped with reason, unavailable with reason, or residual risk. |
| Notes | What the evidence proves and what it does not prove. |

If an acceptance criterion cannot be tested directly, Codex must say why and provide the strongest available alternate evidence.

## 4\. Required test design categories

Where relevant to the work, test design must include:

*   normal success case
*   edge case
*   negative/error case
*   regression case for a known or likely prior failure
*   module-boundary case for inputs/outputs crossing module interfaces
*   integration or smoke case for high-risk wiring
*   security/privacy case when sensitive data, permissions, auth, or external services are involved
*   documentation/read-back validation when work changes Trilium notes or durable docs

Not every category is required for every small change. Codex must justify omitted categories when the category is relevant but not covered.

## 5\. Property-based and mutation testing

Property-based testing is supported where available and relevant, especially for:

*   parsers
*   validators
*   serializers
*   transformations
*   routing logic
*   invariant-heavy domain logic
*   boundary-heavy modules

Mutation testing is supported where available and relevant, especially when:

*   tests are suspected to be shallow
*   coverage is high but confidence is low
*   logic is safety-critical or high-risk
*   prior bugs escaped existing tests

Property-based and mutation testing are not mandatory for every task. They should be used when the project has tooling and the risk/benefit is justified.

## 6\. Validators and commands

CODEX\_PROJECT\_SETUP must define project validation commands for the concrete repo/project.

For implementation work, Codex must run the relevant validators unless blocked.

Validator evidence must include:

*   command
*   working directory
*   environment assumptions if relevant
*   pass/fail result
*   output summary
*   failures and repair attempts
*   validators not run and why
*   remaining risk

Codex must not substitute unrelated commands for required validators.

## 7\. Review expectations for tests

Review must check test quality, not just test existence.

A reviewer must look for:

*   acceptance criteria with no evidence
*   tests that cannot fail meaningfully
*   tests that only mirror implementation
*   excessive mocking
*   missing negative cases
*   missing edge cases
*   missing module-boundary cases
*   stale expectations
*   validator gaps
*   security/privacy gaps where relevant
*   lowered or deleted tests

For high-risk, complex, cross-module, security-sensitive, or repeated-failure work, independent review is required under the Independent Validation / Review Protocol.

## 8\. Codex Return Packet test evidence

Codex must return:

*   acceptance-to-test map
*   validators run
*   test files changed or added
*   tests intentionally not added and why
*   edge/negative/regression/module-boundary coverage summary
*   property-based or mutation testing used, or why not used when relevant
*   known residual risk
*   review result if review was required

Codex cannot claim DONE from passing tests alone. DONE requires acceptance fit, architecture/module fit, validator evidence, review where required, and no unresolved blocker.