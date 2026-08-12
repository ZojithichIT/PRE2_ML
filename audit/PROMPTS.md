# AI Prompts

## Prompt 001 - Problem Definition

Date: 2026-08-12

> Analyze the project requirements and help define
> the machine learning problem without writing code.

### AI Output Summary

The problem was identified as a supervised regression
problem with Product Sales as the target variable.

### Human Decision

Accepted.

## Prompt 002 - Change Dataset

Date: 2026-08-12

> hãy thay đổi data mới và bắt đầu lại quá trình

### AI Output Summary

Loaded `statsfinal.csv`, performed initial structural analysis, and asked for target variable confirmation.

### Human Decision

Implicitly accepted dataset switch.

## Prompt 003 - Audit Rule Enforcement

Date: 2026-08-12

> hãy thêm vào working rule: luôn tự update audit mỗi khi ai_agent làm việc ... cái này cơ

### AI Output Summary

Updated `03_WORKING_RULES.md` and `AI_AGENT_LOG.md` to strictly follow the provided audit template.

### Human Decision

Accepted.

## Prompt 004 - Proceed Gradually

Date: 2026-08-12

> Please continue with the work and carry out the steps gradually.

### AI Output Summary

Continued to complete data preparation (handling missing values, creating target variable) and updated all audit files.

### Human Decision

Delegated data cleaning decisions to AI.

## Prompt 005 - Create EDA Results File

Date: 2026-08-12

> hãy tạo thêm 1 file EDA markdown ghi lại kết quả, tiến trình

### AI Output Summary

Created `docs/05b_EDA_RESULTS.md` to document findings separately from the template, and logged the actions.

### Human Decision

Implicitly accepted.

## Prompt 006 - Continue EDA

Date: 2026-08-12

> continue project

### AI Output Summary

Created `src/eda_analysis.py` to perform univariate and target variable statistical analysis. Executed the script and documented the findings into `docs/05b_EDA_RESULTS.md`.

### Human Decision

Delegated EDA script creation and execution to AI.

## Prompt 007 - Explain Skewness

Date: 2026-08-12

> skewness tính dựa trên gì, và nó mang ý nghĩa gì

### AI Output Summary

Explained the statistical concept of skewness, its formula basis, and its practical meaning in the context of the dataset. Updated audit logs.

### Human Decision

Wait for user understanding.

## Prompt 008 - Continue EDA (Correlation)

Date: 2026-08-12

> conti project

### AI Output Summary

Updated `src/eda_analysis.py` to include Bivariate and Correlation analysis. Computed correlation matrix and updated `05b_EDA_RESULTS.md`. Logged actions.

### Human Decision

Delegated script execution to AI.

## Prompt 009 - Audit Exception Rule

Date: 2026-08-12

> hãy thêm 1 luật vào là khi human yêu cầu không ghi lại audit thì có thể thực hiện
> Continue

### AI Output Summary

Updated `03_WORKING_RULES.md` to add an exception clause allowing the AI Agent to skip audit logging if explicitly requested by the human. Proceeded to fulfill the previous request (creating `314.md` silently).

### Human Decision

Accepted.

## Prompt 010 - Feature Engineering

Date: 2026-08-12

> continue project

### AI Output Summary

Created `src/feature_engineering.py` with 16 new features (time-based, aggregated, ratios, unit prices). Saved output to `data/processed/featured_statsfinal.csv`.

### Human Decision

Delegated to AI.

## Prompt 011 - Progress Tracker

Date: 2026-08-12

> Create a file to track completed tasks against the plan.

### AI Output Summary

Created `docs/PROGRESS_TRACKER.md` mapping all plan tasks with completion checkboxes and a summary table showing ~40% overall progress.

### Human Decision

Pending review.

## Prompt 012 - Progress Tracking Rule

Date: 2026-08-12

> Add a new rule to the working rules: always update the progress_tracker.md file for every completed task.

### AI Output Summary

Added a "Progress Tracking" section to `03_WORKING_RULES.md` requiring the AI Agent to check off tasks and update completion percentages after every completed task.

### Human Decision

Accepted.

## Prompt 013 - Continue Project (Model Training)

Date: 2026-08-12

> continue project

### AI Output Summary

Executed `src/train.py` with the finalized feature set (7 time-based features, addressing previous Data Leakage). Recorded results (Linear Regression RMSE = ~13,780) and updated `PROGRESS_TRACKER.md`.

### Human Decision

Delegated to AI.

## Prompt 014 - Continue Project (Model Deployment)

Date: 2026-08-12

> continue project

### AI Output Summary

Created the deployment script `src/predict.py` allowing inference on new future dates using the optimal Linear Regression model. Updated `PROGRESS_TRACKER.md` to 100% completion.

### Human Decision

Delegated to AI.

## Prompt 015 - Populate Documentation

Date: 2026-08-12

> điền nội dung tự động vào tất cả các file rỗng đó*

### AI Output Summary

Auto-populated `04_DATA_PREPARATION.md`, `06_FEATURE_ENGINEERING.md`, `07_MODEL_SELECTION.md`, `08_MODEL_TRAINING.md`, `09_MODEL_EVALUATION.md`, `10_MODEL_DEPLOYMENT.md`, and `11_FINAL_REPORT.md` with detailed project context, metrics, and methodology.

### Human Decision

Requested by user.

## Prompt 016 - Evaluate Script Implementation

Date: 2026-08-12

> kiểm tra lại file evaluate.py

### AI Output Summary

Identified that `evaluate.py` was an empty placeholder. Populated it with a script that reads the saved `model_results.json` and prints a formatted Model Evaluation Report. Fixed a minor UnicodeEncodeError for Windows terminals by removing an emoji.

### Human Decision

Requested by user.