import pandas as pd
import numpy as np
import os

# ============================
# MANUAL IMPLEMENTATION
# ============================

class ManualLinearRegression:
    def __init__(self):
        self.theta = None
    
    def fit(self, X, y):
        X_b = np.c_[np.ones(X.shape[0]), X]
        self.theta = np.linalg.pinv(X_b.T @ X_b) @ X_b.T @ y
    
    def predict(self, X):
        X_b = np.c_[np.ones(X.shape[0]), X]
        return X_b @ self.theta

class SalesPredictor:
    def __init__(self, data_path):
        self.model = ManualLinearRegression()
        self.sc_mean = None
        self.sc_std = None
        self.features = ['Year', 'Month', 'DayOfWeek', 'DayOfMonth', 'WeekOfYear', 'Quarter', 'IsWeekend']
        self._prepare_and_train(data_path)
        
    def _prepare_and_train(self, data_path):
        # Load and clean data just like in training
        df = pd.read_csv(data_path)
        drop_cols = ['Date', 'Q-P1', 'Q-P2', 'Q-P3', 'Q-P4', 'S-P1', 'S-P2', 'S-P3', 'S-P4',
                     'Total_Quantity', 'Ratio_S_P1', 'Ratio_S_P2', 'Ratio_S_P3', 'Ratio_S_P4',
                     'AvgPrice_P1', 'AvgPrice_P2', 'AvgPrice_P3', 'AvgPrice_P4']
        df = df.drop(columns=[c for c in drop_cols if c in df.columns])
        
        X = df[self.features].values
        y = df['Total_Sales'].values
        
        # Fit Scaler
        self.sc_mean = np.mean(X, axis=0)
        self.sc_std = np.std(X, axis=0)
        self.sc_std[self.sc_std == 0] = 1
        
        X_scaled = (X - self.sc_mean) / self.sc_std
        
        # Train on FULL dataset for deployment
        self.model.fit(X_scaled, y)
        print("Model successfully trained on full historical data for Deployment.")
        
    def predict(self, date_str):
        """Predict sales for a given date (YYYY-MM-DD)"""
        dt = pd.to_datetime(date_str)
        
        # Extract features
        x_new = np.array([
            dt.year,
            dt.month,
            dt.dayofweek,
            dt.day,
            dt.isocalendar().week,
            dt.quarter,
            1 if dt.dayofweek >= 5 else 0
        ], dtype=float).reshape(1, -1)
        
        # Scale
        x_scaled = (x_new - self.sc_mean) / self.sc_std
        
        # Predict
        pred = self.model.predict(x_scaled)[0]
        return max(0, pred)  # Sales cannot be negative

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "processed", "featured_statsfinal.csv")
    
    print("Initializing Sales Predictor (Phase 7: Deployment)...")
    predictor = SalesPredictor(data_path)
    
    # Test scenarios
    test_dates = [
        "2024-01-01",  # New Year
        "2024-07-15",  # Mid-summer
        "2024-11-29",  # Black Friday estimation
        "2024-12-25"   # Christmas
    ]
    
    print("\n--- PREDICTING FUTURE SALES SCENARIOS ---")
    for date in test_dates:
        sales = predictor.predict(date)
        print(f"Predicted Total Sales for {date}: ${sales:,.2f}")
