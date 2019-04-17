import copy
import cv2
import numpy as np

def p7(image, hough_image, hough_thresh): #return line_image
    line_image = copy.copy(image)
    row, column = image.shape[:2]
    diagonal = np.sqrt(np.power(row, 2) + np.power(column, 2))
    shape_hough_image = np.shape(hough_image)
    radius_resolu = shape_hough_image[0]
    theta_resolu = shape_hough_image[1]
    for radius_id in range(radius_resolu):
        for theta_id in range(theta_resolu):
            if hough_image[radius_id][theta_id] > hough_thresh:
                radius = (((2 * diagonal) / radius_resolu) * radius_id) - diagonal
                theta = ((np.pi / theta_resolu) * theta_id) - (np.pi / 2)
                x = radius * np.cos(theta + (np.pi / 2))
                y = radius * np.sin(theta + (np.pi / 2))
                x_1 = x - diagonal * np.cos(theta)
                y_1 = y - diagonal * np.sin(theta)
                x_2 = x + diagonal * np.cos(theta)
                y_2 = y + diagonal * np.sin(theta)
                cv2.line(line_image, (int(round(x_1)), int(round(y_1))), (int(round(x_2)), int(round(y_2))), (255, 255, 255))
    return line_image
                