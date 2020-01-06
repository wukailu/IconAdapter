from dataset.preprocess import genconfig
from PIL import Image
import cv2
import os
from os import path

if __name__ == '__main__':
    images, labels = genconfig()
    for img_path, label in zip(images, labels):
        dir = "../StarGan/icon/" + label[0]
        if not os.path.exists(dir):
            os.mkdir(dir)

        try:
            Image.fromarray(cv2.imread(img_path, cv2.IMREAD_UNCHANGED)).resize((256, 256)).save(path.join(dir, label[1]))
        except Exception:
            print(img_path)
            # os.remove(img_path)