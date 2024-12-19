import pandas as pd
import os

def preprocess_data():
    news = pd.read_csv("data/raw/news_data.csv")
    articles = pd.read_csv("data/raw/articles_metadata.csv")
    user_profiles = pd.read_csv("data/raw/user_profiles.csv")
    campaigns = pd.read_csv("data/raw/campaigns_data.csv")
    demographics = pd.read_csv("data/raw/demographics_data.csv")

    news.dropna(inplace=True)
    articles.dropna(inplace=True)
    user_profiles.dropna(inplace=True)
    campaigns.dropna(inplace=True)
    demographics.dropna(inplace=True)

    if not os.path.exists("data/processed"):
        os.makedirs("data/processed")

    news.to_csv("data/processed/processed_news.csv", index=False)
    articles.to_csv("data/processed/processed_articles.csv", index=False)
    user_profiles.to_csv("data/processed/processed_user_profiles.csv", index=False)
    campaigns.to_csv("data/processed/processed_campaigns.csv", index=False)
    demographics.to_csv("data/processed/processed_demographics.csv", index=False)

if __name__ == "__main__":
    preprocess_data()