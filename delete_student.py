import sqlite3
import os
import cv2

id = input("Enter Student ID to delete: ")

# 🔥 1. DELETE FROM DATABASE
conn = sqlite3.connect("students.db")
c = conn.cursor()

c.execute("DELETE FROM students WHERE id=?", (id,))
conn.commit()
conn.close()

print("Student removed from database ✅")

# 🔥 2. DELETE IMAGES FROM DATASET
dataset_path = "dataset"

deleted = False

for file in os.listdir(dataset_path):
    if file.startswith(f"User.{id}."):
        os.remove(os.path.join(dataset_path, file))
        deleted = True

if deleted:
    print("Images deleted ✅")
else:
    print("No images found")

# 🔥 3. AUTO RETRAIN MODEL (VERY IMPORTANT)
print("Retraining model...")

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = []
ids = []

for file in os.listdir(dataset_path):
    if file.endswith(".jpg"):
        path = os.path.join(dataset_path, file)

        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        id_file = int(file.split(".")[1])

        detected_faces = detector.detectMultiScale(img, 1.2, 5)

        for (x, y, w, h) in detected_faces:
            faces.append(img[y:y+h, x:x+w])
            ids.append(id_file)

if len(faces) > 0:
    recognizer.train(faces, np.array(ids))
    recognizer.save("trainer/trainer.yml")
    print("Model updated ✅")
else:
    print("No data left to train")

print("Done 🎉")