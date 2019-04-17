import cv2
from p3 import p3
import numpy as np

def getRatio(A, B):  # return ratio
    ratio = 0
    if A > B:
        ratio = B/A
    else:
        ratio = A/B
    return ratio

def p4(labeled_image, database):  # return output_image
    database_int = p3(labeled_image)[0]
    database_id = []
    for i in range(len(database_int)):
        min_moment = database_int[i]['moment_min']
        roundness = database_int[i]['roundness']
        for j in range(len(database)):
            min_moment_input = database[j]['moment_min']
            roundness_input = database[j]['roundness']
            if getRatio(min_moment, min_moment_input) > 0.85 and getRatio(roundness,roundness_input) > 0.85:
                database_id.append(database_int[i])
    for i in range(len(database_id)):
        x_pos = database_id[i]['x_pos']
        y_pos = database_id[i]['y_pos']
        theta_min = (np.pi / 2) - np.radians(database_id[i]['orientation'])
        cv2.circle(output_image, (x_pos, y_pos), 5, (255, 255, 255))
        cv2.line(output_image, (int(x_pos - 100 * np.cos(theta_min)), int(y_pos - 100 * np.sin(theta_min))),(int(x_pos + 100 * np.cos(theta_min)), int(y_pos + 100 * np.sin(theta_min))), (255, 255, 255))

    return output_image