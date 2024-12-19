
# AI-Powered News Personalization and Campaign Optimization Platform 🚀📊

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Overview

This project delivers a comprehensive solution leveraging **Data Science** and **ML/AI** techniques for:
- **News Personalization**
- **Digital Advertising Campaign Optimization**

The platform demonstrates technical and analytical capabilities tailored for a **Data Scientist Trainee** position.

### Key Features
- **News Personalization**  
  - Collaborative filtering and matrix factorization for recommending news articles.  
  - Integrates user profiles, article metadata, and historical interactions.  
  - Evaluated using metrics like precision, recall, and MAP.  

- **Campaign Optimization**  
  - Predict campaign **CTR** and **ROI** using machine learning models (e.g., Random Forest).  
  - Optimize campaign parameters (age targeting, bids, etc.) to improve ROI.  
  - Prototypes include simple reinforcement or gradient-based optimization approaches.  

- **Data Engineering & Pipelines**  
  - End-to-end data pipelines with **Python**, **Pandas**, and **DBT** for transformations.  
  - Scalable data processing using **PySpark**.  
  - **AWS integration** for model storage and deployment.

---

## Project Structure

```
project/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   │   ├── news_data.csv
│   │   ├── articles_metadata.csv
│   │   ├── user_profiles.csv
│   │   ├── campaigns_data.csv
│   │   └── demographics_data.csv
│   └── processed/
│       ├── processed_news.csv
│       ├── processed_articles.csv
│       ├── processed_user_profiles.csv
│       ├── processed_campaigns.csv
│       └── processed_demographics.csv
├── dbt/
│   ├── profiles.yml
│   └── models/
│       ├── staging/
│       ├── transforms/
├── notebooks/
│   ├── exploratory_data_analysis.ipynb
│   ├── news_recommendation_prototype.ipynb
│   └── campaign_optimization_prototype.ipynb
├── src/
│   ├── data_preprocessing.py
│   ├── database_utils.py
│   ├── recommender/
│   ├── campaign_optimization/
│   ├── spark_processing.py
│   ├── dashboard.py
│   ├── aws_deployment.py
│   └── data_simulation.py
└── scripts/
    ├── run_data_pipeline.sh
    ├── train_recommender.sh
    ├── train_campaign_model.sh
    └── run_dashboard.sh
```

---

## Technologies Used

- **Programming:** Python
- **Data Processing & Cleaning:** Pandas, DBT, PySpark
- **Machine Learning:** PyTorch (Recommender), scikit-learn (Campaign Model)
- **Visualization & Dashboard:** Matplotlib, Seaborn, Streamlit
- **Cloud & Deployment:** AWS (S3 for model artifacts)
- **Database:** SQL (via SQLAlchemy), DuckDB (via DBT)
- **Environment:** Virtualenv or Conda

---

## Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/tuanvukng01/MediaAI_Personalization_Optimization.git
   cd MediaAI_Personalization_Optimization
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up DBT (Optional)**  
   Ensure you have **DBT** installed and configured. A preconfigured `profiles.yml` is provided.

4. **Run Data Pipeline**
   ```bash
   ./scripts/run_data_pipeline.sh
   ```
   - Simulates and prepares mock datasets.  
   - Preprocesses and stores them in SQL.  
   - Runs DBT transformations to generate feature sets.

5. **Train Recommender Model**
   ```bash
   ./scripts/train_recommender.sh
   ```

6. **Train Campaign Model**
   ```bash
   ./scripts/train_campaign_model.sh
   ```

7. **Run Dashboard**
   ```bash
   ./scripts/run_dashboard.sh
   ```
   Access the **Streamlit dashboard** at: [http://localhost:8501](http://localhost:8501).

---

## Notebooks

- **Exploratory Data Analysis:**  
  `notebooks/exploratory_data_analysis.ipynb`  
  - Initial EDA on processed datasets.  

- **News Recommendation Prototype:**  
  `notebooks/news_recommendation_prototype.ipynb`  
  - Quick prototype to test recommendation results.  

- **Campaign Optimization Prototype:**  
  `notebooks/campaign_optimization_prototype.ipynb`  
  - Experiment with campaign optimization parameters.

---

## AWS Deployment

- Use `aws_deployment.py` to upload trained models to S3.  
- Update `bucket_name` and AWS credentials as required.

---

## Future Improvements

- **NLP Integration:** Article summarization and topic modeling.  
- **Reinforcement Learning:** Sophisticated agent for campaign optimization.  
- **Real-Time Updates:** With **Kafka** and **Spark Streaming**.  
- **Enhanced Dashboard:** Richer visualizations and filters.

---

## License

This project is licensed under the **MIT License**.

---

🎉 **Enjoy exploring the platform!**
