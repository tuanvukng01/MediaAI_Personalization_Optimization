import torch
import torch.nn as nn

class MFModel(nn.Module):
    def __init__(self, num_users, num_items, embedding_dim=64):
        super(MFModel, self).__init__()
        self.user_embedding = nn.Embedding(num_users, embedding_dim)
        self.item_embedding = nn.Embedding(num_items, embedding_dim)
        self.fc = nn.Linear(embedding_dim, 1)

    def forward(self, user, item):
        user_vec = self.user_embedding(user)
        item_vec = self.item_embedding(item)
        x = user_vec * item_vec
        return self.fc(x).squeeze()