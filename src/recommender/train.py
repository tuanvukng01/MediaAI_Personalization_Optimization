import pandas as pd
import torch
from torch.utils.data import DataLoader
import torch.optim as optim
import torch.nn as nn
from dataset import NewsDataset
from model import MFModel
import os

if __name__ == "__main__":
    df = pd.read_csv("../data/processed/processed_news.csv")

    unique_users = df["user_id"].unique()
    unique_items = df["article_id"].unique()
    user_to_idx = {u: i for i, u in enumerate(unique_users)}
    item_to_idx = {i: idx for idx, i in enumerate(unique_items)}
    df["user_idx"] = df["user_id"].map(user_to_idx)
    df["item_idx"] = df["article_id"].map(item_to_idx)
    df["rating"] = 1.0

    all_combinations = pd.MultiIndex.from_product([unique_users, unique_items], names=["user_id","article_id"])
    full_df = pd.DataFrame(index=all_combinations).reset_index()
    full_df = pd.merge(full_df, df[["user_id","article_id","rating","user_idx","item_idx"]], on=["user_id","article_id"], how="left")
    full_df["rating"] = full_df["rating"].fillna(0)
    full_df["user_idx"] = full_df["user_idx"].fillna(full_df["user_id"].map(user_to_idx))
    full_df["item_idx"] = full_df["item_idx"].fillna(full_df["article_id"].map(item_to_idx))

    positives = full_df[full_df["rating"]==1]
    negatives = full_df[full_df["rating"]==0].sample(frac=0.1, random_state=42)
    training_data = pd.concat([positives, negatives], ignore_index=True)

    dataset = NewsDataset(training_data)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    model = MFModel(num_users=len(unique_users), num_items=len(unique_items))
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.BCEWithLogitsLoss()

    model.train()
    for epoch in range(5):
        for user, item, rating in dataloader:
            optimizer.zero_grad()
            preds = model(user, item)
            loss = criterion(preds, rating)
            loss.backward()
            optimizer.step()

    torch.save(model.state_dict(), "recommender_model.pth")