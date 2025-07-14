
import xgboost as xgb
import joblib
import os

def train_gbdt_model(X_train, y_train):
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, max_depth=3)
    model.fit(X_train, y_train)
    return model

def save_model(model, path='models/uplift_model.pkl'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)

def load_model(path='models/uplift_model.pkl'):
    return joblib.load(path)
