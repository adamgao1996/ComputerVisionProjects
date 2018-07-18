import cv2
import numpy as np
import matplotlib


def showimage(title,img):
    cv2.imshow(title, img)
    cv2.waitKey()
    cv2d.destroyAllWindows()

# want grey scale can add 0 at the end
input = cv2.imread('./Master OpenCV/images/input.jpg')

# first is an title and the second is an variable
# cv2.imshow("Hello world", input)

# wait to press any key before continue
# cv2.waitKey()
# cv2.destroyAllWindows()

# gives the dimension of the image
# print input.shape
# print "the height is", input.shape[0], "pixels"

# cv2.imwrite('output.jpg', input)

gray_image = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)

# showimage("grey", gray_image)

B, G, R = input[0,0]

print input

pushtest