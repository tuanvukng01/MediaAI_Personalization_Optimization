import torch
from torch.utils.data import Dataset


class NewsDataset(Dataset):
    def __init__(self, interactions):
        self.user_item_pairs = interactions[["user_idx", "item_idx"]].values
        self.users = self.user_item_pairs[:, 0]
        self.items = self.user_item_pairs[:, 1]
        self.ratings = interactions["rating"].values

    def __len__(self):
        return len(self.user_item_pairs)

    def __getitem__(self, idx):
        user = self.users[idx]
        item = self.items[idx]
        rating = self.ratings[idx]
        return torch.tensor(user, dtype=torch.long), torch.tensor(item, dtype=torch.long), torch.tensor(rating,
                                                                                                        dtype=torch.float)