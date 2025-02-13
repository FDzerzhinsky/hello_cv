import cv2
import numpy as np
import imutils, easyocr
from matplotlib import pyplot as plt

img = cv2.imread('images/num1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img)
plt.show()