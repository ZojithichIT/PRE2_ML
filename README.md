# Predicting Product Sales (Machine Learning Project)

## 📌 Project Overview
This project is a **Time-Series Forecasting** problem that applies Machine Learning to predict the total sales revenue (Total Sales) of an e-commerce company based on historical data.

### 🌟 Key Highlights:
1. **Algorithms from Scratch**: All machine learning models (Linear Regression, Decision Tree, Random Forest, Gradient Boosting) are implemented entirely from scratch using `numpy` matrix operations, demonstrating a deep mathematical understanding of core algorithms.
2. **Data Leakage Mitigation**: Successfully detected and eliminated leaky variables (such as exact sales quantities and individual product revenue). This forced the models to genuinely learn temporal forecasting patterns rather than performing simple arithmetic.
3. **Lightweight Deployment**: Selected Linear Regression as the final production model due to its robust fit for linear temporal data and instantaneous training time via the Normal Equation.

---

## 📂 Project Structure

```text
ML_Project_Predicting_Product_Sales/
│
├── README.md               # Project overview (You are reading this)
├── 314.md                  # Detailed discussion log and Q&A
│
├── docs/                   # Documentation for each Phase (01 to 11)
│   ├── 01_DEFINE_PROBLEM.md
│   ├── 02_PLAN.md
│   ├── 03_WORKING_RULES.md
│   ├── 04_DATA_PREPARATION.md
│   ├── 05_EDA.md
│   ├── 05b_EDA_RESULTS.md  # EDA analysis results
│   ├── 06_FEATURE_ENGINEERING.md
│   ├── 07_MODEL_SELECTION.md
│   ├── 08_MODEL_TRAINING.md
│   ├── 09_MODEL_EVALUATION.md
│   ├── 10_MODEL_DEPLOYMENT.md
│   ├── 11_FINAL_REPORT.md  # Final project report
│   └── PROGRESS_TRACKER.md # Progress tracking (100% Complete)
│
├── audit/                  # Automated AI Logging
│   ├── AI_AGENT_LOG.md
│   ├── PROMPTS.md
│   └── DECISIONS.md
│
├── data/                   
│   ├── raw/                # Raw data (statsfinal.csv)
│   └── processed/          # Cleaned data and model results
│
└── src/                    # Source Code
    ├── data_preparation.py # Data cleaning script
    ├── eda_analysis.py     # Exploratory Data Analysis script
    ├── feature_engineering.py # Feature extraction script
    ├── train.py            # Contains 4 custom ML models and training logic
    ├── evaluate.py         # Model evaluation report generator
    └── predict.py          # Real-world forecasting script (Deployment)
```

---

## ⚙️ How It Works

The project operates through an end-to-end pipeline:
1. **Data Prep**: Reads raw `statsfinal.csv`, removes unnecessary indices and handles missing dates.
2. **EDA**: Analyzes distributions and statistical behaviors of the 4 target products.
3. **Feature Engineering**: Converts the `Date` column into macro-level temporal features (Year, Month, Day, Quarter, Weekend flag). Prunes leakage-prone variables.
4. **Training**: Trains 4 distinct manual algorithms in parallel. The best performing model (Linear Regression) is selected based on RMSE.
5. **Predicting**: Given a specific future date (e.g., 2024-12-25), the system automatically scales the temporal features and predicts expected revenue using historical patterns.

---

## 🚀 How to Run

### Prerequisites
You only need two basic Python libraries:
```bash
pip install numpy pandas
```

### Pipeline Execution Steps
All source code is located in the `src/` directory. Open your terminal at the root directory (`ML_Project_Predicting_Product_Sales`) and run the following commands in order:

**1. Clean Data:**
```bash
python src/data_preparation.py
```

**2. Extract Features:**
```bash
python src/feature_engineering.py
```

**3. Run EDA:**
```bash
python src/eda_analysis.py
```

**4. Train Models (Takes ~1-2 minutes due to manual Ensembles):**
```bash
python src/train.py
```

**5. View Model Evaluation Report:**
```bash
python src/evaluate.py
```

**6. Deploy & Predict Future Sales:**
```bash
python src/predict.py
```
*The output of `predict.py` will display the projected total sales for various future milestones.*
