import cv2
from p5 import p5
from p6 import p6
from p7 import p7
from p8 import p8

image = cv2.imread('hough_simple_1.pgm',0)
edge_image = p5(image)
cv2.imwrite('edge_detection.pgm', edge_image)
edge_threshed_image = p6(edge_image, 20)
cv2.imwrite('edge_detection_threshed.pgm', edge_threshed_image[0])
cv2.imwrite('edge_detection_hough.pgm', edge_threshed_image[1])
line_image_out = p7(image, edge_threshed_image[1], 120)
cv2.imwrite('edge_detection_strongline.pgm', line_image_out)
cropped_lines_image = p8(image, edge_threshed_image[1], edge_threshed_image[0], 120)
cv2.imwrite('edge_detection_cropped.pgm', cropped_lines_image)
cv2.imshow("img_edge_detection_cropped", cropped_lines_image_out)
cv2.waitKey(0)