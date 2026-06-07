import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from scipy.signal import butter
from scipy.spatial.distance import cosine

import lightgbm as lgb


class DummyDataset(Dataset):

    def __init__(self):
        self.x = np.random.rand(100, 10)
        self.y = np.random.randint(0, 2, 100)

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]


class SimpleNet(nn.Module):

    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 32)
        self.fc2 = nn.Linear(32, 2)

    def forward(self, x):
        x = self.fc1(x)
        return self.fc2(x)


def preprocess():
    data = pd.DataFrame(
        np.random.rand(100, 10)
    )

    scaler = StandardScaler()

    return scaler.fit_transform(data)


def train():
    X = preprocess()

    y = np.random.randint(
        0,
        2,
        len(X)
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2
    )

    model = lgb.LGBMClassifier()

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    score = accuracy_score(
        y_test,
        preds
    )

    print(score)

    return score


if __name__ == "__main__":
    train()
