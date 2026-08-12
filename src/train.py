import pandas as pd
import numpy as np
import os
import json

# ============================
# MANUAL IMPLEMENTATIONS
# (No scikit-learn used)
# ============================

def manual_train_test_split(X, y, test_size=0.2, random_state=42):
    """Split data into train and test sets manually."""
    np.random.seed(random_state)
    n = len(X)
    indices = np.random.permutation(n)
    test_count = int(n * test_size)
    test_idx = indices[:test_count]
    train_idx = indices[test_count:]
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]

def manual_standard_scaler_fit_transform(X_train):
    """Fit and transform using Z-score standardization."""
    mean = np.mean(X_train, axis=0)
    std = np.std(X_train, axis=0)
    std[std == 0] = 1  # Avoid division by zero for constant features
    X_scaled = (X_train - mean) / std
    return X_scaled, mean, std

def manual_standard_scaler_transform(X, mean, std):
    """Transform using pre-computed mean and std."""
    return (X - mean) / std

def calc_mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def calc_mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def calc_rmse(y_true, y_pred):
    return np.sqrt(calc_mse(y_true, y_pred))

# ============================
# LINEAR REGRESSION
# (Normal Equation)
# ============================

class ManualLinearRegression:
    def __init__(self):
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        # Add bias column (ones)
        X_b = np.c_[np.ones(X.shape[0]), X]
        # Normal equation: theta = (X^T X)^(-1) X^T y
        self.theta = np.linalg.pinv(X_b.T @ X_b) @ X_b.T @ y
        self.bias = self.theta[0]
        self.weights = self.theta[1:]
    
    def predict(self, X):
        X_b = np.c_[np.ones(X.shape[0]), X]
        return X_b @ self.theta

# ============================
# DECISION TREE REGRESSOR
# ============================

class ManualDecisionTreeNode:
    def __init__(self, value=None, feature=None, threshold=None, left=None, right=None):
        self.value = value
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right

class ManualDecisionTreeRegressor:
    def __init__(self, max_depth=10, min_samples_split=5):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None
    
    def fit(self, X, y):
        self.root = self._build_tree(X, y, depth=0)
    
    def _build_tree(self, X, y, depth):
        if depth >= self.max_depth or len(y) < self.min_samples_split:
            return ManualDecisionTreeNode(value=np.mean(y))
        
        best_feature, best_threshold, best_mse = None, None, float('inf')
        
        for feature_idx in range(X.shape[1]):
            thresholds = np.percentile(X[:, feature_idx], np.arange(10, 100, 10))
            for threshold in thresholds:
                left_mask = X[:, feature_idx] <= threshold
                right_mask = ~left_mask
                if left_mask.sum() < 2 or right_mask.sum() < 2:
                    continue
                mse = (np.var(y[left_mask]) * left_mask.sum() +
                       np.var(y[right_mask]) * right_mask.sum()) / len(y)
                if mse < best_mse:
                    best_mse = mse
                    best_feature = feature_idx
                    best_threshold = threshold
        
        if best_feature is None:
            return ManualDecisionTreeNode(value=np.mean(y))
        
        left_mask = X[:, best_feature] <= best_threshold
        left = self._build_tree(X[left_mask], y[left_mask], depth + 1)
        right = self._build_tree(X[~left_mask], y[~left_mask], depth + 1)
        return ManualDecisionTreeNode(feature=best_feature, threshold=best_threshold, left=left, right=right)
    
    def predict(self, X):
        return np.array([self._predict_one(x, self.root) for x in X])
    
    def _predict_one(self, x, node):
        if node.value is not None:
            return node.value
        if x[node.feature] <= node.threshold:
            return self._predict_one(x, node.left)
        return self._predict_one(x, node.right)

# ============================
# RANDOM FOREST REGRESSOR
# ============================

class ManualRandomForestRegressor:
    def __init__(self, n_trees=50, max_depth=10, min_samples_split=5, max_features_ratio=0.7, random_state=42):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_features_ratio = max_features_ratio
        self.random_state = random_state
        self.trees = []
        self.feature_indices = []
    
    def fit(self, X, y):
        np.random.seed(self.random_state)
        n_samples, n_features = X.shape
        n_select = max(1, int(n_features * self.max_features_ratio))
        
        for i in range(self.n_trees):
            # Bootstrap sampling
            indices = np.random.choice(n_samples, size=n_samples, replace=True)
            feat_idx = np.random.choice(n_features, size=n_select, replace=False)
            
            tree = ManualDecisionTreeRegressor(max_depth=self.max_depth, min_samples_split=self.min_samples_split)
            tree.fit(X[np.ix_(indices, feat_idx)], y[indices])
            self.trees.append(tree)
            self.feature_indices.append(feat_idx)
    
    def predict(self, X):
        predictions = np.array([tree.predict(X[:, feat_idx]) for tree, feat_idx in zip(self.trees, self.feature_indices)])
        return np.mean(predictions, axis=0)

# ============================
# GRADIENT BOOSTING REGRESSOR
# ============================

class ManualGradientBoostingRegressor:
    def __init__(self, n_estimators=100, max_depth=3, learning_rate=0.1, random_state=42):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.learning_rate = learning_rate
        self.random_state = random_state
        self.trees = []
        self.initial_prediction = None
    
    def fit(self, X, y):
        self.initial_prediction = np.mean(y)
        current_pred = np.full(len(y), self.initial_prediction)
        
        for i in range(self.n_estimators):
            residuals = y - current_pred
            tree = ManualDecisionTreeRegressor(max_depth=self.max_depth, min_samples_split=5)
            tree.fit(X, residuals)
            update = tree.predict(X)
            current_pred += self.learning_rate * update
            self.trees.append(tree)
    
    def predict(self, X):
        pred = np.full(X.shape[0], self.initial_prediction)
        for tree in self.trees:
            pred += self.learning_rate * tree.predict(X)
        return pred

# ============================
# MAIN EXECUTION
# ============================

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "processed", "featured_statsfinal.csv")
    
    # 1. Load data
    df = pd.read_csv(data_path)
    print(f"Loaded: {df.shape}")
    
    # 2. Drop columns that cause data leakage or are constant/non-numeric
    # S-P1 to S-P4: Total_Sales = sum of these → direct leakage
    # Q-P1 to Q-P4: Since prices are constant, Sales = Qty * Price → perfect linear leakage
    # Total_Quantity: sum of Q-P columns → also leaks
    # Ratio_S_P1 to P4: Ratio = S-Px / Total_Sales → leaks target
    # AvgPrice: constant values → no predictive power
    # Date: non-numeric, already extracted into time features
    drop_cols = ['Date',
                 'Q-P1', 'Q-P2', 'Q-P3', 'Q-P4',
                 'S-P1', 'S-P2', 'S-P3', 'S-P4',
                 'Total_Quantity',
                 'Ratio_S_P1', 'Ratio_S_P2', 'Ratio_S_P3', 'Ratio_S_P4',
                 'AvgPrice_P1', 'AvgPrice_P2', 'AvgPrice_P3', 'AvgPrice_P4']
    df = df.drop(columns=[c for c in drop_cols if c in df.columns])
    print(f"After dropping leaky/constant columns: {df.shape}")
    print(f"Remaining features: {[c for c in df.columns if c != 'Total_Sales']}")
    
    # 3. Separate X and y
    target = 'Total_Sales'
    feature_names = [c for c in df.columns if c != target]
    X = df[feature_names].values
    y = df[target].values
    print(f"Features: {len(feature_names)}, Samples: {len(X)}")
    
    # 4. Train/Test split
    X_train, X_test, y_train, y_test = manual_train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Train: {len(X_train)}, Test: {len(X_test)}")
    
    # 5. Standardize for Linear Regression
    X_train_scaled, sc_mean, sc_std = manual_standard_scaler_fit_transform(X_train)
    X_test_scaled = manual_standard_scaler_transform(X_test, sc_mean, sc_std)
    
    # 6. Train and evaluate all models
    models = {
        'Linear Regression': (ManualLinearRegression(), X_train_scaled, X_test_scaled),
        'Decision Tree': (ManualDecisionTreeRegressor(max_depth=10), X_train, X_test),
        'Random Forest': (ManualRandomForestRegressor(n_trees=50, max_depth=10), X_train, X_test),
        'Gradient Boosting': (ManualGradientBoostingRegressor(n_estimators=100, max_depth=3), X_train, X_test),
    }
    
    results = {}
    print("\n=== MODEL TRAINING & EVALUATION ===\n")
    
    for name, (model, X_tr, X_te) in models.items():
        print(f"Training {name}...", end=" ")
        model.fit(X_tr, y_train)
        y_pred = model.predict(X_te)
        
        mae = calc_mae(y_test, y_pred)
        mse = calc_mse(y_test, y_pred)
        rmse = calc_rmse(y_test, y_pred)
        
        results[name] = {'MAE': round(mae, 2), 'MSE': round(mse, 2), 'RMSE': round(rmse, 2)}
        print("Done!")
        print(f"  MAE:  {mae:,.2f}")
        print(f"  MSE:  {mse:,.2f}")
        print(f"  RMSE: {rmse:,.2f}\n")
    
    # 7. Find best model
    best_name = min(results, key=lambda k: results[k]['RMSE'])
    print(f"=== BEST MODEL: {best_name} (RMSE: {results[best_name]['RMSE']:,.2f}) ===")
    
    # 8. Save results
    results_path = os.path.join(base_dir, "data", "processed", "model_results.json")
    with open(results_path, 'w') as f:
        json.dump({'results': results, 'best_model': best_name, 'features': feature_names}, f, indent=2)
    print(f"\nResults saved to: {results_path}")
