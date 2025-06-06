import cv2
import numpy as np
cap = cv2.VideoCapture(1)
kernel = np.ones((5,5), np.uint8)
while True:
    success, img = cap.read()
    # img = cv2.GaussianBlur(img, (13, 13), 0)
    img = cv2.Canny(img, 90, 90)
    img = cv2.dilate(img, kernel, iterations=2)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

img = cv2.imread('images/image1.webp')

#   Ресайз изображения
divider = 1
img = cv2.resize(img, (int(img.shape[1] // divider), int(img.shape[0] // divider)))

#   Приведение к градациям серого
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #   Блюр изображения
# img = cv2.GaussianBlur(img, (1,1), 0)
# cv2.imshow('Blured', img)
# cv2.waitKey(0)

#   Нахождение границ
kernel = np.ones((5,5), np.uint8)
img = cv2.Canny(img, 500, 500)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
# cv2.imshow('Canned', img)
# cv2.waitKey(0)

#   Обрезка изображения
# slice_x = (300,500)
# slice_y = (300,500)
# cv2.imshow('Brith-miled', img[slice_y[0]:slice_y[1], slice_x[0]:slice_x[1]])
# cv2.waitKey(0)