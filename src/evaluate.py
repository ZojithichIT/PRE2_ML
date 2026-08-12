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

    # VISUALIZATION
    try:
        import matplotlib.pyplot as plt
        models = list(data['results'].keys())
        rmse_scores = [data['results'][m]['RMSE'] for m in models]
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(models, rmse_scores, color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])
        plt.title('Model Comparison - RMSE (Lower is Better)', fontsize=14)
        plt.ylabel('Root Mean Squared Error (RMSE)', fontsize=12)
        
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 100, f"{yval:,.0f}", ha='center', va='bottom', fontsize=10)
            
        plot_path = os.path.join(base_dir, "data", "processed", "model_comparison.png")
        plt.savefig(plot_path)
        plt.close()
        print(f"\n[+] Visualization saved to: {plot_path}")
    except ImportError:
        print("\n[-] Matplotlib not installed. Skipping visualization.")

if __name__ == "__main__":
    main()
