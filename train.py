import cv2
import os
import numpy as np
from PIL import Image

path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create(radius=1, neighbors=8, grid_x=8, grid_y=8)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def get_images_and_labels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]

    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        img = Image.open(imagePath).convert('L')
        img_numpy = np.array(img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])

        faces = detector.detectMultiScale(img_numpy, 1.2, 5)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples, ids

faces, ids = get_images_and_labels(path)

recognizer.train(faces, np.array(ids))

if not os.path.exists("trainer"):
    os.makedirs("trainer")

recognizer.save("trainer/trainer.yml")

print("Training done")