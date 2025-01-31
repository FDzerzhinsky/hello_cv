import cv2
import numpy


photo = cv2.imread('images/image1.webp')
# photo = cv2.imread('images/pepper.jpg')
img = numpy.zeros(photo.shape[:2], dtype = 'uint8')
circle = cv2.circle(img.copy(), (400, 400), 80, 255, -1)
rectangle = cv2.rectangle(img.copy(), (25, 25), (250, 250), 255, -1)

img = cv2.bitwise_and(photo, photo, mask = circle)
# img = cv2.bitwise_or(circle, rectangle)
# img = cv2.bitwise_xor(circle, rectangle)
# img = cv2.bitwise_not(circle, rectangle)
cv2.imshow('Circle', img)
# cv2.imshow('Rectangle', rectangle)
cv2.waitKey(0)

