# Phase 7: Model Deployment

## Overview
To transition the best-performing model from a research environment into a production-ready state, a deployment script was created.

## Deployment Architecture
- **Script**: `src/predict.py`
- **Methodology**: Rather than saving and loading large `pickle` files for ensemble models, the deployment script leverages the speed of the **Linear Regression** algorithm. 
- When initialized, `SalesPredictor` instantly trains the Linear Regression model via the Normal Equation on the full historical dataset (to maximize learning data).

## Usage
The script exposes a `predict(date_str)` function.
1. It takes a date string (e.g., `YYYY-MM-DD`).
2. Extracts the 7 required seasonal features.
3. Scales them using the exact Mean and Standard Deviation derived from the historical data.
4. Outputs the projected `Total_Sales` for that date.

## Test Scenarios (Future Forecasting)
The deployment system successfully projected sales for future scenarios:
- **2024-01-01** (New Year): $52,653.11
- **2024-07-15** (Mid-Summer): $51,723.85
- **2024-11-29** (Black Friday): $50,826.83
- **2024-12-25** (Christmas): $50,768.49

The deployment is fully operational.
