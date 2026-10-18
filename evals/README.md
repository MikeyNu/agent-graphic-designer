# Design evaluation

The [briefs](briefs.json) define twelve realistic tasks. They are not twelve completed tests. Automated repository checks validate their structure, not the quality of designs an agent might produce.

## Run an execution case

1. Select a brief and supply every required fixture. Several cases explicitly require an image, document, or source file from the evaluator; missing fixtures are not evidence of a skill failure.
2. Start an agent with fresh context. Provide the task, approved facts, constraints, fixtures, and path to the skill. Keep `expected_behaviors` and `failure_signals` for the evaluator.
3. Give the agent access to the actual tools available for the run. Record relevant capability limits. Do not secretly provide an expected aesthetic or the diagnosis of a flawed input.
4. Retain the visible roughs, final artifacts, source files, brief, and actual inspection notes.
5. Review against the brief at composition, actual-size, and detail levels. Verify content and production separately.
6. Record observations, failures, corrections, rechecks, and what remains untested. Another agent's critique is not a human audience study.

## Run a reasoning case

Use a fresh context with the problem statement and constraints. Assess whether the agent distinguishes evidence, inference, and missing information, then proposes concrete next actions. A strong explanation does not prove that the agent can execute the design. Keep reasoning cases separate from artifact-creation cases in reports.

## Scoring discipline

Use strong, adequate, or weak for fit, communication, distinctiveness, craft, and coherence. Require visible evidence for artifact judgments. Record technical checks as PASS, FAIL, NOT RUN, or N/A. Do not let a high aesthetic judgment offset a critical defect.

Do not expect a particular palette, font, period, or layout. Different successful approaches are valid. Test for a meaningful concept, appropriate execution, truthful verification, and adaptation to the specific brief.

## Current evidence

See [validation-2026-10-18.md](validation-2026-10-18.md) for the initial implementation's recorded automated checks and selected design exercises. Its limits are part of the result, not an invitation to infer universal reliability.
