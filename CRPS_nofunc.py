#import libraries
import time
import numpy as np
import cv2
from keras.models import load_model

# load keras model for RPS
model = load_model('keras_model.h5')



# define a video capture object
cap = cv2.VideoCapture(0)

# create np array to store model input
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

 # timebase initialise
time_init=time.time() 

move_lookup= {
    0 : "Rock",
    1 : "Paper",
    2 : "Scissors",
    3 : "Nothing"
    }

# TEXT OPTIONS
# font
font = cv2.FONT_HERSHEY_SIMPLEX   
# White in BGR
color = (255, 255, 255) 


# run a 10-second capture countup
while time.time() < time_init+10:
      
    # Capture the video frame
    # by frame
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cdowntext = str(int(time_init+10-time.time()))
    predicttext=move_lookup[prediction.argmax()]
    frame2=cv2.putText(frame, cdowntext, (50, 50), font, 1, color, 2, cv2.LINE_AA)
    frame2=cv2.putText(frame, predicttext, (100, 50), font, 1, color, 2, cv2.LINE_AA)
    # Display the resulting frame
    cv2.imshow('frame', frame2)
    #print(move_lookup[prediction.argmax()])
   
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()