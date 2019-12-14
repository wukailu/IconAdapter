from preprocess import *
import pandas as pd
import numpy as np
import cv2
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

PATH = './dataset'
H, W = 1000, 500

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean = [0.5, 0.5, 0.5, 0], std = [1, 1, 1, 1])
])

#img = cv2.imread('./dataset/53/icon_folder_light.png', -1)
img = cv2.imread('./dataset/53/aihuishou.aihuishouapp.png', -1)
print(img.shape)
img = Image.fromarray(img)
plt.imshow(img)
plt.show()
#img.ToTensor()
img = transform(img)
print(img)
