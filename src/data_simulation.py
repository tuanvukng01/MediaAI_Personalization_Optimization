import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

np.random.seed(42)

def generate_news_data(num_records=50):
    users = np.random.randint(1, 21, size=num_records)
    articles = np.random.randint(100, 200, size=num_records)
    categories = np.random.choice(["politics", "sports", "tech", "business", "health", "entertainment"], size=num_records)
    timestamps = [datetime(2024,12,1) + timedelta(days=int(x)) for x in np.random.randint(0,30,size=num_records)]
    df = pd.DataFrame({"user_id":users, "article_id":articles, "category":categories, "timestamp":timestamps})
    return df

def generate_articles_metadata(num_articles=50):
    article_ids = np.arange(100, 100+num_articles)
    authors = np.random.choice(["Alice", "Bob", "Carol", "Dave", "Eve"], size=num_articles)
    lengths = np.random.randint(300, 2000, size=num_articles)
    publish_dates = [datetime(2024,12,1) + timedelta(days=int(x)) for x in np.random.randint(0,60,size=num_articles)]
    df = pd.DataFrame({"article_id": article_ids, "author": authors, "length": lengths, "publish_date": publish_dates})
    return df

def generate_user_profiles(num_users=20):
    user_ids = np.arange(1, num_users+1)
    prefs = np.random.choice(["politics", "sports", "tech", "business", "health", "entertainment"], size=num_users)
    df = pd.DataFrame({"user_id": user_ids, "preferred_category": prefs})
    return df

def generate_campaigns_data(num_campaigns=50):
    campaign_ids = [f"C{i}" for i in range(1, num_campaigns+1)]
    ages = np.random.randint(20,60,size=num_campaigns)
    genders = np.random.choice(["M","F","O"],size=num_campaigns)
    clicks = np.random.randint(10,300,size=num_campaigns)
    impressions = np.random.randint(200,1000,size=num_campaigns)
    cost = np.random.randint(50,500,size=num_campaigns)
    df = pd.DataFrame({
        "campaign_id": campaign_ids,
        "age": ages,
        "gender": genders,
        "clicks": clicks,
        "impressions": impressions,
        "cost": cost
    })
    return df

def generate_demographics_data(num_users=20):
    user_ids = np.arange(1,num_users+1)
    ages = np.random.randint(18,70,size=num_users)
    genders = np.random.choice(["M","F","O"],size=num_users)
    locations = np.random.choice(["US","UK","CA","AU","IN","DE","FR","CN","JP"], size=num_users)
    df = pd.DataFrame({"user_id": user_ids, "age": ages, "gender": genders, "location": locations})
    return df

if __name__=="__main__":
    if not os.path.exists("data/raw"):
        os.makedirs("data/raw")
    news_df = generate_news_data()
    news_df.to_csv("data/raw/news_data.csv", index=False)
    articles_df = generate_articles_metadata()
    articles_df.to_csv("data/raw/articles_metadata.csv", index=False)
    user_profiles_df = generate_user_profiles()
    user_profiles_df.to_csv("data/raw/user_profiles.csv", index=False)
    campaigns_df = generate_campaigns_data()
    campaigns_df.to_csv("data/raw/campaigns_data.csv", index=False)
    demographics_df = generate_demographics_data()
    demographics_df.to_csv("data/raw/demographics_data.csv", index=False)