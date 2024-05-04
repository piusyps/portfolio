import os
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, GlobalMaxPooling2D
from tensorflow.keras.optimizers import Adam
from keras_vggface.vggface import VGGFace
import keras

from PIL import Image

from mtcnn import MTCNN

# path in Google Drive
drive_path = "" #"/content/drive/MyDrive/Colab Notebooks/capstone/codes"

# Load models
age_model = tf.keras.models.load_model("/Users/piusyee/GA/personal/projects/capstone/models/model_age.keras")
gender_model = tf.keras.models.load_model("/Users/piusyee/GA/personal/projects/capstone/models/model_gender.keras")
race_model = tf.keras.models.load_model("/Users/piusyee/GA/personal/projects/capstone/models/model_race.keras")

# Define functions for gender, age and race models
def predict_gender(face_image):
    gender = gender_model.predict(face_image)
    return "Male" if gender > 0.5 else "Female"

def age_class(x):
    age_classes = {'0-10': 0,
                 '11-20': 1,
                 '21-30': 2,
                 '31-40': 3,
                 '41-50': 4,
                 '51-60': 5,
                 '61-70': 6,
                 '71-120': 7}

    for bucket, num in age_classes.items():
        if x == num: return bucket

def race_class(x):
    race_classes = {'Asian': 0, 'Black': 1, 'Indian': 2, 'Others': 3, 'White': 4}

    for bucket, num in race_classes.items():
        if x == num: return bucket

# Initialize video capture (0 for webcam, or provide video file path)
cap = cv2.VideoCapture(0) 

# Initialize MTCNN Detector
detector = MTCNN()

while True:
    ret, frame = cap.read()  # Read a frame from the video

    if not ret:  # Handle end of video
        break

    # Detect faces
    faces = detector.detect_faces(frame)

    # Draw bounding boxes and label with predicted gender
    for face in faces:
        x, y, w, h = face['box']
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Extract the face region
        face_image = frame[y:y+h, x:x+w]
        face_image = cv2.resize(face_image, (224, 224)) 
        face_image = np.expand_dims(face_image, axis=0) / 255.0

        # Predict gender
        gender = predict_gender(face_image)

        # Predict age
        age = np.argmax(age_model.predict(face_image))

         # Predict race
        race = np.argmax(race_model.predict(face_image))   

        # Overlay gender label on the image
        cv2.putText(frame, f'Gender: {gender}', (x, y-70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.putText(frame, f'Age: {age_class(age)}', (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.putText(frame, f'Race: {race_class(race)}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the frame with bounding boxes and gender labels
    cv2.imshow('Prediction', frame)

    if cv2.waitKey(1) == ord('q'):  # Press 'q' to quit
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
