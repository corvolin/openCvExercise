import cv2
import numpy as np 

image = cv2.imread("russianblue.jpeg")
logo = cv2.imread("cdlogo.jpg")

rows, columns, channels = image.shape
roi1 = logo[0:rows, 0:columns]

img2grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2grey, 10, 255, cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi1,roi1,mask = mask_inv)
img2_fg = cv2.bitwise_and(image,image,mask = mask)

dst = cv2.add(img1_bg,img2_fg)
logo[0:rows, 0:columns ] = dst

cv2.imshow('mask', logo)
cv2.waitKey(0)
cv2.destroyAllWindows()