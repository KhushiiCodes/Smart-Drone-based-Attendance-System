import cv2
import os
import time
from database import add_student, create_databases

create_databases()

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

id = input("Enter Student ID: ")
name = input("Enter Name: ")

add_student(id, name)

path = 'dataset'
if not os.path.exists(path):
    os.makedirs(path)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cam.isOpened():
    print("Camera not opening ❌")
    exit()

# 🔥 Force window to front
cv2.namedWindow("Register", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Register", cv2.WND_PROP_TOPMOST, 1)

count = 0
last_capture_time = 0

print("\n📷 Capturing images slowly... Move your face (left/right/up/down)")

while True:
    ret, img = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        current_time = time.time()

        # 🔥 Capture every 0.5 sec (SLOW & CONTROLLED)
        if current_time - last_capture_time > 0.5:
            count += 1
            cv2.imwrite(f"{path}/User.{id}.{count}.jpg", face)
            last_capture_time = current_time

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

    # 🔥 Show count on screen
    cv2.putText(img, f"Images: {count}/30", (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Register", img)

    key = cv2.waitKey(1)

    if key == 27 or key == ord('q') or count >= 30:
        break

cam.release()
cv2.destroyAllWindows()

print("Registration Complete ✅")