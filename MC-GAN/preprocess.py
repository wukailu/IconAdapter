import os
import csv
import cv2
import numpy as np

def genconfig():
    folders = os.listdir('./dataset')
    n = len(folders)
    folders.sort()
    images, labels = [], []
    for i in range(n):
        pics = os.listdir('./dataset/' + folders[i])
        m = len(pics)
        pics.sort()
        for j in range(m):
            images.append('./dataset/' + folders[i] + '/' + pics[j])
            labels.append((folders[i], pics[j]))

    csvfile = open('./image_config.csv', 'w')
    writer = csv.writer(csvfile)
    writer.writerow(images)
    csvfile.close()

    csvfile = open('./label_config.csv', 'w')
    writer = csv.writer(csvfile)
    writer.writerow(labels)
    csvfile.close()
    return images, labels

def gencore():
    folders = os.listdir('./dataset')
    n = len(folders)
    folders.sort()
    lst = os.listdir('./dataset/' + folders[0])
    for i in range(1, n):
        pics = os.listdir('./dataset/' + folders[i])
        pics.sort()
        k = len(lst)
        tmp = []
        for j in range(k):
            if lst[j] in pics:
                tmp.append(lst[j])
        lst = tmp
    print(len(lst))
    csvfile = open('./core.csv', 'w')
    writer = csv.writer(csvfile)
    writer.writerow(lst)
    csvfile.close()
    k = len(lst)
    if not os.path.exists('./data_icons'):
        os.mkdir('./data_icons')
    if not os.path.exists('./data_icons/train'):
        os.mkdir('./data_icons/train')
    for i in range(n):
        pics = os.listdir('./dataset/' + folders[i])
        pics.sort()
        img = []
        for j in range(k):
            img.append(cv2.imread('./dataset/' + folders[i] + '/' + lst[j], cv2.IMREAD_UNCHANGED))
            img[j] = cv2.resize(img[j], (192, 192))
        image = img[0]
        for j in range(1, k):
            image = np.concatenate([image, img[j]], axis = 1)
        cv2.imwrite('./data_icons/' + folders[i] + '.png', image)

def rmdummy():
    folders = os.listdir('./dataset')
    n = len(folders)
    for i in range(n):
        pics = os.listdir('./dataset/' + folders[i])
        m = len(pics)
        for j in range(m):
            if 'com' not in pics[j]:
                os.system('rm ./dataset/' + folders[i] + '/' + pics[j])
                continue

if __name__ == '__main__':
    #genconfig()
    gencore()
    #rmdummy()
