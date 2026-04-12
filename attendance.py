import cv2
import sqlite3
from datetime import datetime
from database import mark_attendance

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cam = cv2.VideoCapture(0)

marked_today = set()

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        face_img = cv2.resize(gray[y:y+h,x:x+w], (200,200))

        id, conf = recognizer.predict(face_img)

        if 30 < conf < 60:
            cursor.execute("SELECT name FROM students WHERE id=?", (id,))
            result = cursor.fetchone()

            if result:
                name = result[0]

                if id not in marked_today:
                    now = datetime.now()
                    date = now.strftime("%Y-%m-%d")
                    time = now.strftime("%H:%M:%S")

                    mark_attendance(id, name, date, time)
                    marked_today.add(id)

                label = f"{name} ({round(conf,1)})"
            else:
                label = "Unknown"
        else:
            label = "Unknown"

        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img,label,(x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)

    cv2.imshow("Attendance", img)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()