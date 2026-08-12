# Exploratory Data Analysis (EDA) - Results and Progress

This document tracks the actual findings and progress of the EDA phase, based on the framework defined in `05_EDA.md`.

## 1. Dataset Overview

- **Source File**: `data/raw/statsfinal.csv`
- **Number of rows**: 4,600 (Raw)
- **Number of columns**: 10
- **Features**: `Date` (datetime), `Q-P1` to `Q-P4` (integer quantities), `S-P1` to `S-P4` (float sales values)
- **Target Variable**: `Total_Sales` (computed as the sum of `S-P1` to `S-P4`)

## 2. Data Quality Analysis

- **Redundant Columns**: The `Unnamed: 0` column (acting as a duplicated index) was dropped.
- **Data Types**: The `Date` column was successfully parsed and converted to `datetime` objects.
- **Duplicates**: 0 duplicate records were found.
- **Missing Values**: 26 missing values were detected in the `Date` column. 
- **Action Taken**: Because dates are essential for time-series and regression analysis, and 26 rows represent only ~0.5% of the data, these rows were dropped. The cleaned dataset now has **4,574 rows**.

## 3. Univariate Analysis

All features in the dataset are numeric.

- **Quantities (Q-P1 to Q-P4)**: Average quantities sold range from ~1,123 (P4) up to ~4,123 (P1). The standard deviations are quite large, meaning wide variations in daily sales volumes.
- **Sales (S-P1 to S-P4)**: Average daily sales range from ~\$8,012 (P4) to ~\$17,039 (P3). P3 generates the most revenue on average despite P1 having higher quantity sold, indicating P3 is a higher-priced product.

## 4. Target Variable Analysis

The target variable is `Total_Sales`.

- **Mean**: 51,624.81
- **Median**: 51,874.22
- **Minimum**: 11,296.30
- **Maximum**: 93,819.41
- **Standard Deviation**: 13,800.35
- **Skewness**: -0.04

**Conclusion**: The target variable is almost perfectly symmetrical (Skewness approx 0) and normally distributed, as the mean and median are extremely close. There are no extreme outliers affecting the central tendency. This is an ideal distribution for linear regression models.

## 5. Bivariate & Correlation Analysis

Correlation coefficients between the features and the target variable `Total_Sales`:

1. **S-P3 / Q-P3**: 0.654
2. **S-P2 / Q-P2**: 0.508
3. **S-P1 / Q-P1**: 0.499
4. **S-P4 / Q-P4**: 0.229

*(Note: Quantity and Sales for each product have perfect 1.0 correlation with each other, meaning Sales is a direct multiple of Quantity).*

**Insights**:
- **Product 3** is the primary driver of total sales, showing the strongest positive correlation (~0.65).
- **Product 2** and **Product 1** have a moderate impact (~0.50).
- **Product 4** has a weak correlation (~0.23), contributing the least to the overall sales variations.

## 6. Key Findings

- The dataset is relatively clean, with no duplicates and only minimal missing values.
- Sales and quantities are broken down by 4 separate products, making `Total_Sales` an appropriate aggregated target variable.
