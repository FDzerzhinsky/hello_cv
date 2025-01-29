import cv2
import numpy as np
img = cv2.imread('images/pepper.jpg')
divider = 2
img = cv2.resize(img, (int(img.shape[1] // divider), int(img.shape[0] // divider)))
new_img = np.zeros(img.shape, dtype = 'uint8')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5,5), 0)
img = cv2.Canny(img, 100, 150)
cont, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(new_img, cont, -1, (200, 100, 13), 1)
cv2.imshow('Image', new_img)
cv2.waitKey(0)