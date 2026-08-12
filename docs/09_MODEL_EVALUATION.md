# Phase 6: Model Evaluation

## Overview
The performance of the 4 manual models was evaluated on the unseen test set (20% of the data) using Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).

## Evaluation Results
*Note: You can view these results dynamically by running `python src/evaluate.py`.*

| Model | MAE | MSE | RMSE |
|-------|-----|-----|------|
| **Linear Regression** | 11,169.90 | 189,899,295.89 | **13,780.40** |
| **Gradient Boosting** | 11,210.83 | 193,658,659.80 | 13,916.13 |
| **Random Forest** | 11,293.49 | 195,569,773.27 | 13,984.63 |
| **Decision Tree** | 12,694.57 | 248,156,049.20 | 15,752.97 |

## Model Selection Decision
- **Winner**: **Linear Regression**.
- **Reasoning**: Linear Regression achieved the lowest RMSE score (13,780.40), slightly beating Gradient Boosting. 
- **Context**: In this time-series forecasting context where features are purely temporal (Year, Month, Quarter), Linear Regression (with proper standardization) effectively captures the macroscopic trends without falling into the trap of overfitting that affects deep Decision Trees on calendar data.
- **Business Impact**: An RMSE of ~13,780 on an average daily revenue of ~$51,624 shows that the model is practical for rough baseline forecasting based entirely on the calendar date.
