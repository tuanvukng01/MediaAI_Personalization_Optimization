import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_campaign_model(input_csv, model_path):
    df = pd.read_csv(input_csv)
    df["ctr"] = df["clicks"]/df["impressions"]
    X = df[["age","clicks","impressions","cost"]]
    y = df["ctr"]
    model = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42)
    model.fit(X, y)
    joblib.dump(model, model_path)

if __name__ == "__main__":
    train_campaign_model("../data/processed/processed_campaigns.csv", "campaign_model.pkl")