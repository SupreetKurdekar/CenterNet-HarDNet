import numpy as np
import cv2
from datetime import datetime
import os


folder_path = "/home/supreet/mobileDetTraining/images_storage"

cap = cv2.VideoCapture(cv2.CAP_V4L2)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("none")
        break

    # Display the resulting frame
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)

    if key == ord('c'):
        date = datetime.now().strftime("img_%Y_%m_%d-%I_%M_%S_%f_%p")
        filepath = os.path.join(folder_path,date)
        cv2.imwrite(filepath)


    if key == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()