import cv2
import os
import numpy as np
import time
import tkinter as tk
from tkinter import simpledialog, messagebox
import sys
import ctypes
time.sleep(2)
save_path = os.path.expanduser('~') + '\Documents\captured_images'
stored_image_path = os.path.join(save_path, "face_id.jpg")
counterGood = 0
i = 0

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    print("Can't open camera")
    exit()

if not os.path.exists(stored_image_path):
    print("No photo found")
    exit()

stored_image = cv2.imread(stored_image_path)
stored_gray = cv2.cvtColor(stored_image, cv2.COLOR_BGR2GRAY)

while i < 7:
    print("Searching...")

    ret, frame = camera.read()

    if not ret:
        print("Error capturing frame!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face = frame[y:y + h, x:x + w]
        face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        res = cv2.matchTemplate(face_gray, stored_gray, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(res)

        if max_val > 0.5:
            cv2.putText(frame, "Matching!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            print("Matching!")
            counterGood += 1
        else:
            cv2.putText(frame, "Not Matching", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            print("Not Matching")

    cv2.imshow('Camera Feed - You Are Being Captured', frame)
    cv2.waitKey(1)
    i += 1
    time.sleep(1)

camera.release()
cv2.destroyAllWindows()

if counterGood >= 4:
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Success", "Access Granted!", icon="info")
else:
        time.sleep(3)
        os.system('shutdown /s /f /t 1')
