import pandas as pd
import os

def load_data(filepath):
    """Loads the dataset and performs initial structural cleaning."""
    print(f"Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    
    # 1. Drop redundant index column
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
        print("- Dropped redundant 'Unnamed: 0' column.")
        
    # 2. Convert Date to datetime format (format in dataset is DD-MM-YYYY)
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')
        print("- Converted 'Date' column to datetime.")
        
    # 3. Handle missing values
    initial_rows = len(df)
    df = df.dropna(subset=['Date'])
    dropped = initial_rows - len(df)
    if dropped > 0:
        print(f"- Dropped {dropped} rows with missing 'Date'.")
        
    # 4. Create Target Variable (Total Sales)
    sales_cols = ['S-P1', 'S-P2', 'S-P3', 'S-P4']
    if all(col in df.columns for col in sales_cols):
        df['Total_Sales'] = df[sales_cols].sum(axis=1)
        print("- Created 'Total_Sales' column as the sum of all product sales.")
        
    return df

def analyze_data_quality(df):
    """Performs Data Quality Analysis (Step 3 of EDA)."""
    print("\n=== DATA QUALITY ANALYSIS ===")
    
    # Missing values
    print("\n1. Missing Values:")
    missing = df.isnull().sum()
    print(missing[missing > 0] if missing.sum() > 0 else "No missing values found.")
    
    # Duplicate records
    duplicates = df.duplicated().sum()
    print(f"\n2. Duplicate Records: {duplicates}")
    
    # Basic Descriptive Statistics for Numerical columns
    print("\n3. Basic Statistics (Numerical Features):")
    print(df.describe().T[['count', 'mean', 'min', 'max', 'std']])

if __name__ == "__main__":
    # Handle path regardless of where it's executed from
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "raw", "statsfinal.csv")
    
    if os.path.exists(data_path):
        df = load_data(data_path)
        analyze_data_quality(df)
        
        # Save processed data
        processed_dir = os.path.join(base_dir, "data", "processed")
        os.makedirs(processed_dir, exist_ok=True)
        processed_path = os.path.join(processed_dir, "cleaned_statsfinal.csv")
        df.to_csv(processed_path, index=False)
        print(f"\n- Processed data saved to {processed_path}")
    else:
        print(f"Error: Dataset not found at {data_path}")
