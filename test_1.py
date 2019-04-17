from p1 import p1
from p2 import p2
from p3 import p3
from p4 import p4
import cv2

# Analyze two objects picture
image = p1('two_objects.pgm', 100)
cv2.imwrite('binary_image.pgm', image)
labeled_image, index_list = p2(image)
cv2.imwrite('labeled_image.pgm', labeled_image)
cv2.imshow('image',labeled_image)
cv2.waitKey(0)
info = p3(labeled_image)
database = info[0]
cv2.imwrite('output_image.pgm', info[1])

# Analyze many objects picture
image = p1('many_objects_1.pgm', 100)
labeled_image, index_list = p2(image)
output_image = p4(labeled_image, database)
cv2.imwrite("Analysis_Result.pgm", output_image)
img = cv2.imread("Analysis_Result.pgm", 0)
cv2.imshow('image',image)
cv2.waitKey(0)