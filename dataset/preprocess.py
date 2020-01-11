import os
import csv
import cv2
import numpy as np
import time

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
            (h, w, _) = img[j].shape
            for x in range(h):
                for y in range(w):
                    if img[j][x][y][3] != 255:
                        img[j][x][y] = [255, 255, 255, 255]
            img[j] = cv2.resize(img[j], (400, 400), cv2.INTER_LANCZOS4)
        image = img[0]
        for j in range(1, k):
            image = np.concatenate([image, img[j]], axis = 1)
        cv2.imwrite('./data_icons/train/' + folders[i] + '.png', image)

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

def usecore():
    f = open('./core.csv', 'r')
    reader = csv.reader(f)
    lst = list(reader)[0]
    k = len(lst)
    folders = os.listdir('./dataset')
    n = len(folders)
    folders.sort()
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
            (h, w, _) = img[j].shape
            for x in range(h):
                for y in range(w):
                    if img[j][x][y][3] != 255:
                        img[j][x][y] = [255, 255, 255, 255]
            img[j] = cv2.resize(img[j], (400, 400), cv2.INTER_LANCZOS4)
        image = img[0]
        for j in range(1, k):
            image = np.concatenate([image, img[j]], axis = 1)
        cv2.imwrite('./data_icons/train/' + folders[i] + '.png', image)

def stackgan():
    f = open('./core.csv', 'r')
    reader = csv.reader(f)
    lst = list(reader)[0]
    k = len(lst)
    folders = os.listdir('./dataset')
    n = len(folders)
    folders.sort()
    if not os.path.exists('./icons'):
        os.mkdir('./icons')
    blank = np.zeros((400, 400, 4), np.uint8)
    blank.fill(255)
    for i in range(n):
        pics = os.listdir('./dataset/' + folders[i])
        pics.sort()
        img = []
        for j in range(k):
            img.append(cv2.imread('./dataset/' + folders[i] + '/' + lst[j], cv2.IMREAD_UNCHANGED))
            (h, w, _) = img[j].shape
            for x in range(h):
                for y in range(w):
                    if img[j][x][y][3] != 255:
                        img[j][x][y] = [255, 255, 255, 255]
            img[j] = cv2.resize(img[j], (400, 400), cv2.INTER_LANCZOS4)
        if not os.path.exists('./icons/' + folders[i]):
            os.mkdir('./icons/' + folders[i])
        if not os.path.exists('./icons/' + folders[i] + '/A'):
            os.mkdir('./icons/' + folders[i] + '/A')
        if not os.path.exists('./icons/' + folders[i] + '/A/train'):
            os.mkdir('./icons/' + folders[i] + '/A/train')
        if not os.path.exists('./icons/' + folders[i] + '/A/test'):
            os.mkdir('./icons/' + folders[i] + '/A/test')
        if not os.path.exists('./icons/' + folders[i] + '/B'):
            os.mkdir('./icons/' + folders[i] + '/B')
        if not os.path.exists('./icons/' + folders[i] + '/B/train'):
            os.mkdir('./icons/' + folders[i] + '/B/train')
        if not os.path.exists('./icons/' + folders[i] + '/B/test'):
            os.mkdir('./icons/' + folders[i] + '/B/test')
        idx = []
        while len(idx) < 4:
            x = np.random.randint(k)
            if not (x in idx):
                idx.append(x)
        idx.sort()
        image = img[0] if 0 in idx else blank
        for j in range(1, k):
            image = np.concatenate([image, img[j] if j in idx else blank], axis = 1)
        cv2.imwrite('./icons/' + folders[i] + '/A/test/' + folders[i] + '.png', image)
        for x in range(4):
            image = img[0] if (0 in idx) and (idx[x] != 0) else blank
            for j in range(1, k):
                image = np.concatenate([image, img[j] if (j in idx) and (idx[x] != j) else blank], axis = 1)
            cv2.imwrite('./icons/' + folders[i] + '/A/train/' + folders[i] + '_' + str(idx[x]) + '.png', image)
        image = img[0]
        for j in range(1, k):
            image = np.concatenate([image, img[j]], axis = 1)
        cv2.imwrite('./icons/' + folders[i] + '/B/test/' + folders[i] + '.png', image)
        for x in range(4):
            cv2.imwrite('./icons/' + folders[i] + '/B/train/' + folders[i] + '_' + str(idx[x]) + '.png', img[idx[x]])

if __name__ == '__main__':
    np.random.seed(int(time.time()))
    #genconfig()
    #gencore()
    #rmdummy()
    #usecore()
    stackgan()
