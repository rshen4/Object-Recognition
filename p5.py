import numpy as np

def inten_cal(image, x, y, row, column):
    if x < 0 or y < 0 or x > column - 1 or y > row - 1:
        return -1
    else:
        return image[y][x]

def get_gradient(image, x, y, row, column):
    sobel_x = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
    sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

    x_gradient = 0.0
    y_gradient = 0.0

    for i in range(3):
        for j in range(3):
            inten = inten_cal(image, x - 1 + j, y - 1 + i, row, column)
            if inten == -1:
                return 0
            x_gradient += (sobel_x[i][j] * inten)
            y_gradient += (sobel_y[i][j] * inten)
    gradient = np.sqrt(np.power(x_gradient, 2) + np.power(y_gradient, 2))

    return int(round(gradient))

def p5(image): #return edge_image
    row, column = image.shape[:2]
    edge_image = np.empty(image.shape[:2], dtype=int)
    max_inten = 0

    for i in range(row):
        for j in range(column):
            gradient = get_gradient(image, j, i, row, column)
            
            edge_image[i][j] = gradient
            
            if (gradient > max_inten):
                max_inten = gradient
    
    # Compute scaled intensities
    
    for x in np.nditer(edge_image, op_flags=['readwrite']):
        scaled_inten = (float(x) / float(max_inten)) * 255.0
        x[...] = int(round(scaled_inten))
    
    return edge_image