import cv2
import numpy as np

def union(label_left,label_up,index_list):
    if index_list[label_up] > index_list[label_left]:
        index_list[label_up] = index_list[label_left]
    else:
        index_list[label_left] = index_list[label_up]
    return index_list

def Find(label,index_list):
    while index_list[label] != label:
        label = Find(index_list[label],index_list)
    return label

def p2(image):
    row, column = image.shape[:2]
    labeled_image = np.zeros((row,column), dtype=np.int)
    new_label = 2
    label_list = [0,1]
    index_list = [0,1]

    for i in range(row):
        for j in range(column):
            current_pixel = image[i][j]
            diagnol_neighbor = image[i-1][j-1]
            up_neighbor = image[i-1][j]
            left_neighbor = image[i][j-1]
            if current_pixel == 1:
                if diagnol_neighbor == 0 and up_neighbor == 0 and left_neighbor == 0:
                    label_list.append(new_label)
                    index_list.append(new_label)
                    labeled_image[i][j] = new_label
                    new_label += 1
                elif up_neighbor == 1 and left_neighbor == 1:
                    labeled_image[i][j] = labeled_image[i-1][j]
                    if labeled_image[i][j-1] != labeled_image[i-1][j]:
                        index_list = Union(labeled_image[i][j-1],labeled_image[i-1][j],index_list)
                elif diagnol_neighbor == 1:
                    labeled_image[i][j] = labeled_image[i-1][j-1]
                elif up_neighbor == 1 and left_neighbor == 0:
                    labeled_image[i][j] = labeled_image[i-1][j]
                elif up_neighbor == 0 and left_neighbor == 1:
                    labeled_image[i][j] = labeled_image[i][j-1]

    for i in range(len(index_list)):
        index_list[i] = Find(i,index_list)

    unique_label_list = np.unique(index_list)
    new_unique_label_list = [0,1]
    for i in range(2,len(unique_label_list)):
        new_unique_label_list.append(i)

    for i in range(len(index_list)):
        for j in range(len(unique_label_list)):
            if index_list[i] == unique_label_list[j]:
                index_list[i] = new_unique_label_list[j]

    for i in range(row):
        for j in range(column):
            labeled_image[i][j] = index_list[labeled_image[i][j]]

    return labeled_image, index_list