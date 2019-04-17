import numpy as np

def p6(edge_image, edge_thresh): #return [edge_thresh_image, hough_image]
    shape = np.shape(edge_image)
    num_rows = shape[0]
    num_cols = shape[1]
    diagonal = np.sqrt(np.power(num_rows, 2) + np.power(num_cols, 2))
    theta_resolu = 800
    radius_resolu = diagonal
    accumulating_matrix = np.zeros((radius_resolu, theta_resolu), dtype=int)
    hough_image = np.zeros((radius_resolu, theta_resolu), dtype=int)
    edge_thresh_image = np.empty(shape, dtype=int)
    max_value = 1
    for i in range(num_rows):
        for j in range(num_cols):
            if edge_image[i][j] > edge_thresh:
                edge_thresh_image[i][j] = 255
                for theta_id in range(theta_resolu):
                    theta = ((np.pi / theta_resolu) * theta_id) - (np.pi / 2)
                    radius = (i * np.cos(theta)) - (j * np.sin(theta))
                    radius_id = int(round(((radius_resolu) / (2 * diagonal)) * (radius + diagonal)))
                    accumulating_matrix[radius_id][theta_id] = accumulating_matrix[radius_id][theta_id] + 1
                    if (accumulating_matrix[radius_id][theta_id] > max_value):
                        max_value = accumulating_matrix[radius_id][theta_id]
            else:
                edge_thresh_image[i][j] = 0
    
    for i in range(int(round(radius_resolu))):
        for j in range(theta_resolu):
            hough_image[i][j] = int(round((float(accumulating_matrix[i][j]) / float(max_value)) * 255.0))
    
    return [edge_thresh_image, hough_image]
    