import cv2

faces = cv2.CascadeClassifier('faces.xml')
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = faces.detectMultiScale(img, scaleFactor=1.2, minNeighbors=3)
    for (x, y, w, h) in result:
        cv2.rectangle(img, (x, y), (x + w, y + h), (200, 120, 100), 3)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# img = cv2.imread('images/people2.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#

# result = faces.detectMultiScale(img, scaleFactor = 1.1, minNeighbors=3)
#
# for (x, y, w, h) in result:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
# cv2.imshow('Faces', img)
# cv2.waitKey(0)