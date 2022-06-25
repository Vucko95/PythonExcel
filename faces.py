import cv2
import os
from numpy import imag
images = os.listdir('humans')
# print(images)
for image in images:
    image = cv2.imread(f'./humans/{image}', 1)
    face_cascade = cv2.CascadeClassifier('faces.xml')
    faces = face_cascade.detectMultiScale(image, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 4)
    cv2.imwrite(f'./humans/faces-in-{image}.jpeg', image)
