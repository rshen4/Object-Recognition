import cv2
import numpy as np
def p1(gray_image,thresh_val):
    thresh_val = 100
    image = cv2.imread(gray_image, 0)
    row, column = image.shape[:2]
    for i in range(row):
        for j in range (column):
            if image[i,j]>= thresh_val:
                image[i,j] = 255
            else:
                image[i,j] = 0
    return image
    cv2.imshow('image',image)
    cv2.waitKey(0)

# gray_image = "two_objects.pgm"
# image = cv2.imread(gray_image, 0)
# row, column = image.shape[:2]
# for i in range(row):
#     for j in range (column):
#         if image[i,j]>= thresh_val:
#             image[i,j] = 255
#         else:
#             image[i,j] = 0
# cv2.imshow('image',image)
# cv2.waitKey(0)

    # image = p1('two_objects.pgm', 100)
    # cv2.imwrite('binary_image.pgm', image)
    # image = cv2.imread('binary_image.pgm', 0)
    # cv2.imshow('image', image)
    # cv2.waitKey(0)