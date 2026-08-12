import pandas as pd
import os

def load_cleaned_data(filepath):
    return pd.read_csv(filepath)

def perform_univariate_analysis(df):
    print("=== 3. UNIVARIATE ANALYSIS ===")
    num_cols = ['Q-P1', 'Q-P2', 'Q-P3', 'Q-P4', 'S-P1', 'S-P2', 'S-P3', 'S-P4']
    
    stats = df[num_cols].describe().T[['mean', '50%', 'min', 'max', 'std']]
    stats = stats.rename(columns={'50%': 'median'})
    print(stats.to_string())

def perform_target_analysis(df):
    print("\n=== 4. TARGET VARIABLE ANALYSIS (Total_Sales) ===")
    target = df['Total_Sales']
    print(f"Mean: {target.mean():.2f}")
    print(f"Median: {target.median():.2f}")
    print(f"Min: {target.min():.2f}")
    print(f"Max: {target.max():.2f}")
    print(f"Std Dev: {target.std():.2f}")
    print(f"Skewness: {target.skew():.2f}")

def perform_correlation_analysis(df):
    print("\n=== 5. CORRELATION ANALYSIS ===")
    num_cols = ['Q-P1', 'Q-P2', 'Q-P3', 'Q-P4', 'S-P1', 'S-P2', 'S-P3', 'S-P4', 'Total_Sales']
    corr = df[num_cols].corr()
    print("Correlation with Total_Sales:")
    print(corr['Total_Sales'].sort_values(ascending=False))

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "processed", "cleaned_statsfinal.csv")
    
    df = load_cleaned_data(data_path)
    perform_univariate_analysis(df)
    perform_target_analysis(df)
    perform_correlation_analysis(df)
