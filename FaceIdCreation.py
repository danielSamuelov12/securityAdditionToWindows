import cv2
import os
import time

save_path = os.path.expanduser('~') + '\\Documents\\captured_images'
if not os.path.exists(save_path):
    os.makedirs(save_path)

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    print("error")
    exit()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

print("taking photo...")

time.sleep(3)

ret, frame = camera.read()

if not ret:
    print("error")
    exit()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Frame', frame)

image_path = os.path.join(save_path, "face_id.jpg")
cv2.imwrite(image_path, frame)
print(f"image taken{image_path}")

camera.release()
cv2.destroyAllWindows()
