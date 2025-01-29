import cv2
import numpy as np

img = cv2.imread('images/image1.webp')
# img = cv2.flip(img, 1)

def rotate(img_param, angle):
    height, width = img_param.shape[:2]
    point = width // 2, height // 2
    matrix = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img_param, matrix, (width, height))

def transform(img_param, x,y):
    height, width = img_param.shape[:2]
    matrix = np.float32([[1,0,x],[0,1,y]])
    return cv2.warpAffine(img_param, matrix, (width, height))

# img = transform(img, 100, 100)
# img = rotate(img, 90)
cv2.imshow('Image', img)
cv2.waitKey(0)
