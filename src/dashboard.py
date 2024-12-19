import streamlit as st
import pandas as pd
import torch
import joblib
from recommender.model import MFModel

st.title("AI-Powered News Personalization and Campaign Optimization Dashboard")

news = pd.read_csv("data/processed/processed_news.csv")
user_profiles = pd.read_csv("data/processed/processed_user_profiles.csv")
campaigns = pd.read_csv("data/processed/processed_campaigns.csv")

st.subheader("Sample News Interactions")
st.dataframe(news.head(20))

st.subheader("User Profiles")
st.dataframe(user_profiles.head(20))

st.subheader("Campaign Performance")
st.dataframe(campaigns.head(20))

st.subheader("Recommend Articles for a User")
user_id_input = st.number_input("Enter a user ID:", min_value=1, value=1, step=1)
if st.button("Recommend"):
    unique_users = news["user_id"].unique()
    unique_items = news["article_id"].unique()
    user_to_idx = {u:i for i,u in enumerate(unique_users)}
    item_to_idx = {i:u for u,i in enumerate(unique_items)}

    model = MFModel(num_users=len(unique_users), num_items=len(unique_items))
    model.load_state_dict(torch.load("recommender_model.pth"))
    model.eval()

    user_idx = user_to_idx.get(user_id_input, None)
    if user_idx is not None:
        items_tensor = torch.tensor(range(len(unique_items)), dtype=torch.long)
        user_tensor = torch.tensor([user_idx]*len(unique_items), dtype=torch.long)
        with torch.no_grad():
            scores = model(user_tensor, items_tensor)
        top_indices = torch.argsort(scores, descending=True)[:5]
        recommended_items = [unique_items[i.item()] for i in top_indices]
        st.write("Recommended Article IDs:", recommended_items)
    else:
        st.write("User not found.")

st.subheader("Optimize Campaign Parameters")
if st.button("Optimize"):
    params = joblib.load("campaign_model.pkl")
    st.write("Run optimize.py script to find best parameters.")