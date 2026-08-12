# Working Rules

## General Rules

1. Do not modify project requirements without user approval.
2. Do not invent dataset information.
3. Do not delete existing project files without approval.
4. Do not change the target variable without approval.
5. Explain important technical decisions before implementation.
6. Keep all major decisions documented in Markdown files.
7. Record AI-assisted development activities in the audit log.

## Data Rules

1. Inspect the dataset before preprocessing.
2. Do not remove rows without identifying the reason.
3. Document missing-value handling.
4. Document outlier handling.
5. Document categorical encoding methods.

## Machine Learning Rules

1. Use regression models because the target is numerical.
2. Use a train/test split.
3. Evaluate models using MAE, MSE and RMSE.
4. Compare multiple models before selecting the final model.
5. Do not select a model only because it is the most complex.

## AI Agent Audit Requirement

The AI Agent MUST automatically update the audit logs
after every completed task.

The user does not need to manually update the audit log.

## Required Audit Files

The AI Agent must maintain:

- `audit/AI_AGENT_LOG.md`
- `audit/PROMPTS.md`
- `audit/DECISIONS.md`

## Audit Update Rules

After every task, the AI Agent MUST:

1. Record the date and time.
2. Record the task requested by the user.
3. Record the prompt or summarize the user instruction.
4. Record the actions performed.
5. Record the files created or modified.
6. Record important decisions made during the task.
7. Record validation or testing performed.
8. Record the final result.
9. Record whether human approval was required.

**Exception**: If the human explicitly requests to skip or not record the audit for a specific task, the AI Agent is authorized to bypass these audit update rules for that task.

## Progress Tracking

After every completed task, the AI Agent MUST update the
`docs/PROGRESS_TRACKER.md` file by checking off `[x]` the
corresponding task items and updating the phase status
and overall completion percentage.

## No Silent Changes

The AI Agent MUST NOT modify project files
without recording the modification in the audit log.

## Decision Logging

If a technical or methodological decision is made,
the AI Agent MUST update `DECISIONS.md`.

Examples:

- Dataset selection
- Feature selection
- Data cleaning strategy
- Outlier handling
- Model selection
- Hyperparameter selection
- Evaluation metric selection

## Prompt Logging

The AI Agent MUST record the user's important prompts
in `PROMPTS.md`.

## Audit Integrity

The AI Agent MUST NOT:

- Delete previous audit records
- Rewrite historical audit records
- Hide failed attempts
- Remove rejected decisions
- Claim that a task was completed if it was not completed

New audit entries should be appended to the existing log.