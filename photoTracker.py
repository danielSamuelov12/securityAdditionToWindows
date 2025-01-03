import cv2
import shutil
import os

camera_image_path = 'captured_image.jpg'
destination_folder = r'C:\Users\Daniel Samuelov\Documents\captured_images\PhotosOfUsers'

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Cannot open the camera.")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

ret, frame = cap.read()

if not ret:
    print("Failed to capture image.")
    cap.release()
    exit()

cv2.imwrite(camera_image_path, frame)

cap.release()

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

destination_path = os.path.join(destination_folder, os.path.basename(camera_image_path))
if os.path.exists(destination_path):
    file_name, file_extension = os.path.splitext(os.path.basename(camera_image_path))
    counter = 1
    while os.path.exists(destination_path):
        new_file_name = f"{file_name}_{counter}{file_extension}"
        destination_path = os.path.join(destination_folder, new_file_name)
        counter += 1

shutil.copy(camera_image_path, destination_path)

print(f"Image successfully copied to {destination_path}")
