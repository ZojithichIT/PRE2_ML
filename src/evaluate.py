import os
import json

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_path = os.path.join(base_dir, "data", "processed", "model_results.json")
    
    if not os.path.exists(results_path):
        print("Error: model_results.json not found. Please run src/train.py first.")
        return

    with open(results_path, 'r') as f:
        data = json.load(f)
        
    print("=" * 60)
    print(f"{'MODEL EVALUATION REPORT':^60}")
    print("=" * 60)
    
    print(f"{'Model':<20} | {'MAE':<10} | {'MSE':<15} | {'RMSE':<10}")
    print("-" * 60)
    
    for model, metrics in data['results'].items():
        print(f"{model:<20} | {metrics['MAE']:<10,.2f} | {metrics['MSE']:<15,.2f} | {metrics['RMSE']:<10,.2f}")
    
    print("-" * 60)
    print(f"[*] BEST MODEL: {data['best_model']} (Selected based on lowest RMSE)")
    print("=" * 60)
    print(f"Features used ({len(data['features'])}): {', '.join(data['features'])}")

if __name__ == "__main__":
    main()
