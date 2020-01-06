from dataset.preprocess import genconfig
import cv2
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms as T
from PIL import Image
import numpy as np


class Icon(Dataset):
    def __init__(self, image_size=(256, 256), channel=4, transforms=None, mode = "train"):
        """
        return normalized images and their labels that label = (folder_id, image_id)
        :param transforms: transforms applied on PIL image
        :param mode: train or test
        :param image_size: tuple or int to specify the shape
        :param channel: 3 for rgb, 4 with alpha
        """
        if isinstance(image_size, int):
            image_size = (image_size, image_size)
        if channel < 3 or channel > 4:
            raise NotImplementedError("channel must be 3 or 4")
        self.img, self.label = genconfig()
        lens = int(len(self.label)*0.9)
        if mode == "train":
            self.img = self.img[:lens]
            self.label = self.label[:lens]
        elif mode == "test":
            self.img = self.img[lens:]
            self.label = self.label[lens:]
        else:
            raise NotImplementedError("mode must be train or test")

        self.channel = channel
        self.shape = image_size
        self.transform = transforms
        if self.transform is None:
            self.transform = T.Compose([T.ToTensor(), T.Normalize(mean=np.ones(channel)*0.5, std=np.ones(channel)*0.5)])

    def __getitem__(self, idx):
        img = Image.fromarray(cv2.imread(self.img[idx], cv2.IMREAD_UNCHANGED if self.channel == 4 else cv2.IMREAD_COLOR))
        img = img.resize(self.shape)
        return self.transform(img), self.label[idx]

    def __len__(self):
        return len(self.img)


if __name__ == '__main__':
    dataloader = DataLoader(Icon(), batch_size=16, shuffle=True)
    print('checking data...')
    for img, label in dataloader:
        print(img, type(img), img.shape)
        print(label, type(label))
        break
    print('finished!')
