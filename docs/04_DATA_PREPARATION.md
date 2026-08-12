# Phase 2: Data Preparation

## Overview
This document outlines the steps taken to clean and prepare the raw sales data (`data/raw/statsfinal.csv`) for analysis and modeling. The data preparation process was fully automated in `src/data_preparation.py`.

## Steps Performed

1. **Redundant Column Removal**: 
   - Dropped the `Unnamed: 0` column which acted as an unnecessary duplicate index.
2. **Date Parsing**: 
   - Converted the `Date` column from string format to pandas `datetime` objects to allow for time-series extraction later.
3. **Missing Value Handling**: 
   - Detected 26 rows with missing dates. Since dates are critical for this analysis and these rows represent only ~0.5% of the data, they were dropped.
4. **Target Variable Creation**: 
   - Created the `Total_Sales` column by summing the daily sales of all products (`S-P1` + `S-P2` + `S-P3` + `S-P4`).

## Output
The cleaned dataset was saved to `data/processed/cleaned_statsfinal.csv` with 4,574 rows and 10 columns, ready for exploratory data analysis (EDA) and feature engineering.
