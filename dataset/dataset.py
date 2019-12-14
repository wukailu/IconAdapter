from preprocess import *
import sys
import pandas as pd
import numpy as np
import cv2
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from PIL import Image

H, W = 500, 500
FULL_CHANNEL = False

tr3 = transforms.Normalize(mean = [0.5, 0.5, 0.5], std = [1, 1, 1])
tr4 = transforms.Normalize(mean = [0.5, 0.5, 0.5, 0.5], std = [1, 1, 1, 1])

class dataset(Dataset):
    def __init__(self, paths, label):
        self.img = paths
        self.label = label
    def __getitem__(self, idx):
        img = cv2.imread(self.img[idx], cv2.IMREAD_UNCHANGED if FULL_CHANNEL else cv2.IMREAD_COLOR)
        img = Image.fromarray(img)
        img = img.resize((H, W))
        img = transforms.ToTensor()(img)
        img = tr4(img) if FULL_CHANNEL else tr3(img)
        label = self.label[idx]
        return img, label
    def __len__(self):
        return len(self.img)

if __name__ == '__main__':
    paths, label = genconfig()
    dataset = dataset(paths, label)
    dataloader = DataLoader(dataset, batch_size = 16, shuffle = True)
    print('checking data...')
    for img, label in dataloader:
        pass
    print('finished!')
