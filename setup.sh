#!/bin/bash

# Create the base structure
mkdir -p project
cd project || exit

# Create root-level files
touch README.md requirements.txt

# Create the data directory structure
mkdir -p data/raw data/processed
touch data/raw/news_data.csv
touch data/raw/articles_metadata.csv
touch data/raw/user_profiles.csv
touch data/raw/campaigns_data.csv
touch data/raw/demographics_data.csv
touch data/processed/processed_news.csv
touch data/processed/processed_articles.csv
touch data/processed/processed_user_profiles.csv
touch data/processed/processed_campaigns.csv
touch data/processed/processed_demographics.csv

# Create the dbt directory structure
mkdir -p dbt/models/staging dbt/models/transforms
touch dbt/profiles.yml
touch dbt/models/staging/staging_campaigns.sql
touch dbt/models/staging/staging_news.sql
touch dbt/models/staging/staging_articles.sql
touch dbt/models/staging/staging_user_profiles.sql
touch dbt/models/staging/staging_demographics.sql
touch dbt/models/transforms/campaign_features.sql
touch dbt/models/transforms/news_features.sql
touch dbt/models/transforms/user_features.sql
touch dbt/models/transforms/article_features.sql

# Create the notebooks directory
mkdir -p notebooks
touch notebooks/exploratory_data_analysis.ipynb
touch notebooks/news_recommendation_prototype.ipynb
touch notebooks/campaign_optimization_prototype.ipynb

# Create the src directory structure
mkdir -p src/recommender src/campaign_optimization
touch src/__init__.py
touch src/data_preprocessing.py
touch src/database_utils.py
touch src/recommender/__init__.py
touch src/recommender/dataset.py
touch src/recommender/model.py
touch src/recommender/train.py
touch src/campaign_optimization/__init__.py
touch src/campaign_optimization/model.py
touch src/campaign_optimization/optimize.py
touch src/spark_processing.py
touch src/dashboard.py
touch src/aws_deployment.py
touch src/data_simulation.py

# Create the scripts directory
mkdir -p scripts
touch scripts/run_data_pipeline.sh
touch scripts/train_recommender.sh
touch scripts/train_campaign_model.sh
touch scripts/run_dashboard.sh

echo "Directory structure generated successfully!"