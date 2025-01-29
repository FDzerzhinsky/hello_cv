import cv2
import numpy as np

photo = np.zeros((450, 450, 3), np.uint8)
# photo[:] = 255, 0, 0
x0, x1, y0, y1 = 20, 100, 50, 100
cv2.rectangle(photo, (x0, y0), (x1, y1), (120, 200, 105), thickness=2)
cv2.line(photo, (0, photo.shape[0] // 2), (100, photo.shape[0] // 2), (0, 0, 255), thickness=2)
cv2.imshow('Photo', photo)
cv2.waitKey(0)