import pandas as pd
import os

def load_cleaned_data(filepath):
    """Loads the cleaned dataset."""
    df = pd.read_csv(filepath, parse_dates=['Date'])
    return df

def engineer_features(df):
    """Creates new features from existing data."""
    print("=== FEATURE ENGINEERING ===\n")
    
    # 1. Time-based features from Date
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['DayOfWeek'] = df['Date'].dt.dayofweek      # 0=Monday, 6=Sunday
    df['DayOfMonth'] = df['Date'].dt.day
    df['WeekOfYear'] = df['Date'].dt.isocalendar().week.astype(int)
    df['Quarter'] = df['Date'].dt.quarter
    df['IsWeekend'] = (df['DayOfWeek'] >= 5).astype(int)  # 1 if Sat/Sun
    print("1. Created time-based features: Year, Month, DayOfWeek, DayOfMonth, WeekOfYear, Quarter, IsWeekend")
    
    # 2. Total Quantity sold per day
    df['Total_Quantity'] = df[['Q-P1', 'Q-P2', 'Q-P3', 'Q-P4']].sum(axis=1)
    print("2. Created 'Total_Quantity' (sum of Q-P1 to Q-P4)")
    
    # 3. Revenue contribution ratios per product
    df['Ratio_S_P1'] = df['S-P1'] / df['Total_Sales']
    df['Ratio_S_P2'] = df['S-P2'] / df['Total_Sales']
    df['Ratio_S_P3'] = df['S-P3'] / df['Total_Sales']
    df['Ratio_S_P4'] = df['S-P4'] / df['Total_Sales']
    print("3. Created revenue contribution ratios (Ratio_S_P1 to Ratio_S_P4)")
    
    # 4. Average price per unit for each product
    df['AvgPrice_P1'] = df['S-P1'] / df['Q-P1']
    df['AvgPrice_P2'] = df['S-P2'] / df['Q-P2']
    df['AvgPrice_P3'] = df['S-P3'] / df['Q-P3']
    df['AvgPrice_P4'] = df['S-P4'] / df['Q-P4']
    print("4. Created average unit prices (AvgPrice_P1 to AvgPrice_P4)")
    
    # Summary
    print(f"\nFinal dataset shape: {df.shape}")
    print(f"New columns added: {df.shape[1] - 10}")
    print(f"\nAll columns: {list(df.columns)}")
    
    return df

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(base_dir, "data", "processed", "cleaned_statsfinal.csv")
    output_path = os.path.join(base_dir, "data", "processed", "featured_statsfinal.csv")
    
    df = load_cleaned_data(input_path)
    df = engineer_features(df)
    
    df.to_csv(output_path, index=False)
    print(f"\nFeature-engineered data saved to: {output_path}")
