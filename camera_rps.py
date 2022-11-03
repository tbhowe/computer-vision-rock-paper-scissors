#def get_prediction:
#%%
import numpy as np
import cv2
from keras.models import load_model

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def get_prediction():
    move_lookup= {
    0 : "Rock",
    1 : "Paper",
    2 : "Scissors",
    3 : "Nothing"
    }
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    print(prediction)
    cv2.imshow('frame', frame)
    return(move_lookup[prediction.argmax()])

preddy=get_prediction()
print(preddy)
