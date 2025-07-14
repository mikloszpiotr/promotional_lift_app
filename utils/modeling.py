
import xgboost as xgb
import joblib

def train_gbdt_model(X_train, y_train):
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, max_depth=3)
    model.fit(X_train, y_train)
    return model

def save_model(model, path='models/uplift_model.pkl'):
    joblib.dump(model, path)

def load_model(path='models/uplift_model.pkl'):
    return joblib.load(path)
