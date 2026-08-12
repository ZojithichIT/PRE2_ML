# Phase 4: Model Selection

## Overview
The goal of this project is to predict numerical daily sales (`Total_Sales`), making this a Regression problem. We evaluated 4 distinct regression algorithms.

## Candidate Models

1. **Linear Regression**:
   - A simple, interpretable model assuming a linear relationship between time features and sales. Excellent as a baseline and for capturing clear macro trends.
2. **Decision Tree Regressor**:
   - A non-linear model that splits data based on feature thresholds. Prone to overfitting on time-series data but good for capturing non-linear interactions (like weekends vs weekdays).
3. **Random Forest Regressor**:
   - An ensemble method combining multiple decision trees to reduce overfitting and improve variance.
4. **Gradient Boosting Regressor**:
   - An advanced ensemble method that builds trees sequentially, correcting errors of previous trees. Usually provides top-tier performance on tabular data.

## Implementation Details
As a strict engineering constraint for this project, all models were implemented **from scratch using NumPy and Pandas** (no `scikit-learn` libraries were used for the models).
