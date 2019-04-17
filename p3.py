import cv2
import copy
import numpy as np

def second_moment(theta, a , b, c):
    second_moment = (a * np.power(np.sin(theta), 2)) - (b * np.sin(theta) * np.cos(theta)) + (c * np.power(np.cos(theta), 2))
    return second_moment

def p3(labeled_image): #return [database, output_image]
    shape = np.shape(labeled_image)
    print(labeled_image)
    row = shape[0]
    column = shape[1]
    attribute_dic = []  #area, x_pos, y_pos, a, b, c, theta_min, theta_max, E_min, E_max
    output_image = copy.copy(labeled_image)
    database = []
    for i in range(row):
        for j in range (column):
            label = labeled_image[i][j]
            if label != 0:
                if label not in attribute_dic:
                    attribute_dic[label] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    attribute_dic[label][0] = attribute_dic[label][0] + 1
                    attribute_dic[label][1] = attribute_dic[label][1] + j
                    attribute_dic[label][2] = attribute_dic[label][2] + i

    for key in attribute_dic:
        attribute_dic[key][1] = attribute_dic[key][1] / attribute_dic[key][0]
        attribute_dic[key][2] = attribute_dic[key][2] / attribute_dic[key][0]

    for i in range(row):
        for j in range(column):
            label = labeled_image[i][j]
            if label > 0:
                i_p = i - attribute_dic[label][2]
                j_p = j - attribute_dic[label][1]
                attribute_dic[label][3] = attribute_dic[label][3] + (j_p * j_p)  # a
                attribute_dic[label][4] = attribute_dic[label][4] + (2 * i_p * j_p)  # b
                attribute_dic[label][5] = attribute_dic[label][5] + (i_p * i_p)  # c

    for key in attribute_dic:
        a = attribute_dic[key][3]
        b = attribute_dic[key][4]
        c = attribute_dic[key][5]

        theta_1 = (np.arctan2(b, a - c)) / 2
        theta_2 = theta_1 + (np.pi / 2)

        E_1 = second_moment(theta_1, a, b, c)
        E_2 = second_moment(theta_2, a, b, c)

        if (E_1 > E_2):
            attribute_dic[key][6] = theta_2
            attribute_dic[key][7] = theta_1
            attribute_dic[key][8] = E_2
            attribute_dic[key][9] = E_1
        else:
            attribute_dic[key][6] = theta_1
            attribute_dic[key][7] = theta_2
            attribute_dic[key][8] = E_1
            attribute_dic[key][9] = E_2

    database_index = 0


    for key in attribute_dic:
        database.append({'label': '', 'x_pos': -1, 'y_pos': -1, 'moment_min': -1, 'orientation': -1,'roundness': -1})
        x_pos = attribute_dic[key][1]
        y_pos = attribute_dic[key][2]
        theta_min = attribute_dic[key][6]

        database[database_index]['label'] = key
        database[database_index]['x_pos'] = x_pos
        database[database_index]['y_pos'] = y_pos
        database[database_index]['moment_min'] = attribute_dic[key][8]
        database[database_index]['orientation'] = np.degrees((np.pi / 2) - theta_min)
        database[database_index]['roundness'] = attribute_dic[key][8] / attribute_dic[key][9]

        database_index = database_index + 1

        cv2.circle(output_image, (x_pos, y_pos), 5, (255,255,255))
        cv2.line(output_image, (int(x_pos - 100 * np.cos(theta_min)), int(y_pos - 100 * np.sin(theta_min))),(int(x_pos + 100 * np.cos(theta_min)), int(y_pos + 100 * np.sin(theta_min))), (255,255,255))

    return [database, output_image]