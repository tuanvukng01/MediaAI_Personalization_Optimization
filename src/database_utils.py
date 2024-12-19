from sqlalchemy import create_engine
import pandas as pd

def store_in_sql(db_url, table_name, csv_path):
    engine = create_engine(db_url)
    conn = engine.connect()
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, con=conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    db_url = "sqlite:///project.db"
    store_in_sql(db_url, "raw_news", "data/processed/processed_news.csv")
    store_in_sql(db_url, "raw_articles_metadata", "data/processed/processed_articles.csv")
    store_in_sql(db_url, "raw_user_profiles", "data/processed/processed_user_profiles.csv")
    store_in_sql(db_url, "raw_campaigns", "data/processed/processed_campaigns.csv")
    store_in_sql(db_url, "raw_demographics", "data/processed/processed_demographics.csv")