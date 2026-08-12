# Phase 5: Model Training

## Overview
Model training was executed using the script `src/train.py`.

## Data Splitting & Scaling
- The cleaned dataset containing 4,574 valid rows was split using an 80/20 ratio.
- Training set: 3,660 samples.
- Testing set: 914 samples.
- **Scaling**: A manual standard scaler (StandardScaler) was implemented to scale the features (`Year`, `Month`, etc.) to zero-mean and unit-variance. This is especially crucial for Linear Regression stability.

## Custom Implementations
Since external machine learning libraries were restricted, the following algorithms were written from scratch in NumPy:
- **Linear Regression**: Implemented using the Normal Equation (Moore-Penrose Pseudoinverse).
- **Decision Tree Regressor**: Implemented recursive binary splitting based on Variance Reduction.
- **Random Forest Regressor**: Built by bootstrapping data and ensembling multiple custom Decision Trees.
- **Gradient Boosting Regressor**: Built sequentially by fitting trees to the negative gradients (residuals) of the previous step.

## Training Process
The models were trained on the 7 time-based features to predict `Total_Sales`. Because of the custom Python/NumPy implementations, training the ensemble models (Random Forest, Gradient Boosting) was computationally intensive but successfully completed.
