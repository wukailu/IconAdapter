import os
import csv

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

if __name__ == '__main__':
    genconfig()
