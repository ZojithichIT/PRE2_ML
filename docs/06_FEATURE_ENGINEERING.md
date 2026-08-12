# Phase 3: Feature Engineering

## Overview
This phase focused on creating meaningful predictors (features) for our machine learning models. The logic is implemented in `src/feature_engineering.py` and further refined in `src/train.py`.

## Initial Feature Creation
Initially, we engineered 16 new features:
- **Seasonal Features**: `Year`, `Month`, `DayOfWeek`, `DayOfMonth`, `WeekOfYear`, `Quarter`, `IsWeekend`.
- **Product Popularity**: `Total_Quantity`.
- **Revenue Distributions**: `Ratio_S_P1` to `Ratio_S_P4` (sales percentage of each product).
- **Price Indicators**: `AvgPrice_P1` to `AvgPrice_P4`.

## Refinement (Data Leakage Mitigation)
During model training, we discovered that maintaining quantity, product sales, and ratio columns caused **Data Leakage**, resulting in a "perfect" RMSE of 0.00. The models were simply solving a math equation instead of predicting future trends.

To build a robust forecasting model, we aggressively pruned the features:
- **Dropped**: `Q-P1` to `Q-P4` and `Total_Quantity` (Leakage).
- **Dropped**: `S-P1` to `S-P4` and `Ratio_S_P1` to `Ratio_S_P4` (Leakage).
- **Dropped**: `AvgPrice_P1` to `AvgPrice_P4` (Identified as constants).

## Final Feature Set
The final robust dataset used for training contains **7 time-based features**:
- `Year`, `Month`, `DayOfWeek`, `DayOfMonth`, `WeekOfYear`, `Quarter`, `IsWeekend`.
