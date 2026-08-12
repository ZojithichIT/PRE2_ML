# Project Decisions

## Decision 001

Date: 2026-08-12

### Decision

Treat Product Sales prediction as a regression problem.

### Reason

The target variable is numerical.

### Alternatives Considered

- Classification
- Regression
- Time-series forecasting

### Final Choice

Regression

### Approved By

Human

## Decision 002

Date: 2026-08-12

### Decision

Switch dataset to `statsfinal.csv`.

### Reason

User explicitly requested to change to the new data and restart the EDA process.

### Alternatives Considered

- Continue with `extracted_product_info_amazon.csv`.

### Final Choice

`statsfinal.csv`

### Approved By

Human

## Decision 003

Date: 2026-08-12

### Decision

Adopt strict Audit Logging Requirements.

### Reason

User mandated that the AI Agent MUST automatically update the audit logs after every completed task without manual prompts, and provided a comprehensive rule template.

### Alternatives Considered

- Retain previous basic rules.

### Final Choice

Adopted strict user-provided Audit Requirement template.

### Approved By

Human

## Decision 004

Date: 2026-08-12

### Decision

Drop rows with missing `Date` values.

### Reason

Only 26 out of 4600 rows (0.5%) had missing dates, which is statistically insignificant. Imputation for a key time-series index is risky.

### Alternatives Considered

- Forward-fill or Backward-fill imputation.

### Final Choice

Drop missing rows (dropna).

### Approved By

AI Agent (Delegated by user)

## Decision 005

Date: 2026-08-12

### Decision

Define Target Variable as `Total_Sales`.

### Reason

The dataset tracks 4 distinct products (S-P1 to S-P4). To align with the overall project objective of predicting "Product Sales", a consolidated `Total_Sales` feature was computed as the sum of the 4 individual product sales.

### Alternatives Considered

- Predict sales for only one product.
- Multi-target regression.

### Final Choice

Create and predict aggregate `Total_Sales`.

### Approved By

AI Agent (Delegated by user)

## Decision 006

Date: 2026-08-12

### Decision

Create a new file `docs/05b_EDA_RESULTS.md` instead of overwriting `05_EDA.md`.

### Reason

The user requested an *additional* file to track results and progress. `05_EDA.md` acts as a template/checklist, while `05b_EDA_RESULTS.md` will contain the actual findings.

### Alternatives Considered

- Overwrite `docs/05_EDA.md`.

### Final Choice

Create `docs/05b_EDA_RESULTS.md`.

### Approved By

AI Agent (Interpreting user prompt)

## Decision 007

Date: 2026-08-12

### Decision

Add an exception to the strict Audit Update Rules.

### Reason

The strict audit rules created a conflict when the user explicitly requested a task to be performed without logging it. To resolve this and grant the user ultimate control, an exception clause was added.

### Alternatives Considered

- Refuse the user's request continuously.

### Final Choice

Add the exception clause to `03_WORKING_RULES.md`.

### Approved By

Human

## Decision 008

Date: 2026-08-12

### Decision

Engineer 16 new features across 4 categories: time-based, aggregation, ratios, and unit prices.

### Reason

Time-based features (Month, DayOfWeek, Quarter, IsWeekend) capture seasonal/cyclical patterns. Total_Quantity provides an aggregate demand signal. Revenue ratios reveal each product's daily contribution share. Average unit prices uncover pricing dynamics.

### Alternatives Considered

- Use only time-based features.
- Use lag features (rolling averages).

### Final Choice

Create all 16 features to maximize the information available to the models.

### Approved By

AI Agent (Delegated by user)

## Decision 009

Date: 2026-08-12

### Decision

Enforce automatic `PROGRESS_TRACKER.md` updates after every completed task.

### Reason

The user identified that the progress tracker was not being automatically updated and requested a rule to enforce it.

### Alternatives Considered

- Manual updates only when requested.

### Final Choice

Add mandatory rule to `03_WORKING_RULES.md`.

### Approved By

Human

## Decision 010

Date: 2026-08-12

### Decision

Drop `Q-P*`, `S-P*`, `Ratio*`, and `AvgPrice*` columns during model training.

### Reason

Identified severe Data Leakage where models achieved a mathematically perfect RMSE of 0.00. Dropping these features forced the algorithms to act as true Time-Series Forecasters.

### Alternatives Considered

- Keep the features and report artificial 0.00 RMSE (Rejected as bad ML practice).

### Final Choice

Drop all leaky features.

### Approved By

AI Agent (Delegated by user)

## Decision 011

Date: 2026-08-12

### Decision

Train Linear Regression on-the-fly in `predict.py` instead of loading a `pickle` file.

### Reason

Since the Linear Regression model uses the Normal Equation, it trains instantly on 4,000 rows. It saves complexity and storage space by refitting on the fly compared to dumping and loading model states.

### Alternatives Considered

- Dump the trained model weights and scaler params to `models/*.pkl`.

### Final Choice

On-the-fly training for Deployment.

### Approved By

AI Agent

## Decision 012

Date: 2026-08-12

### Decision

Convert `evaluate.py` into a report generator rather than a math evaluator.

### Reason

All math evaluation logic (MAE, MSE, RMSE) was already deeply integrated into `train.py` for simplicity in the "From Scratch" setup. Moving it out would require refactoring `train.py`. Having `evaluate.py` simply parse the saved `model_results.json` to generate a formatted table respects the existing structure while making the placeholder file functional.

### Alternatives Considered

- Refactor `train.py` to only train and dump weights, leaving all evaluation logic to `evaluate.py`.

### Final Choice

Read `model_results.json` and generate a report.

### Approved By

AI Agent