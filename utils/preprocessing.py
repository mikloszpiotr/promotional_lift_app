
import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_prepare_data(filepath):
    df = pd.read_csv(filepath)
    features = ['price', 'competitor_price', 'is_promoted']
    target = 'sales'
    X = df[features]
    y = df[target]
    return train_test_split(X, y, test_size=0.2, random_state=42), df
