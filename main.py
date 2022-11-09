import cv2
from time import time, sleep
from skimage.metrics import structural_similarity

cap = cv2.VideoCapture(0)

saved_frame = None
i = 0
while True:
    cap.grab()
    ret, current_frame = cap.read()
    
    if saved_frame is None:
        cv2.imwrite(f"slide{i}.png", current_frame)
        saved_frame = current_frame
        i += 1
    else:
        score, diff = structural_similarity(cv2.cvtColor(saved_frame, cv2.COLOR_BGR2GRAY), cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY), full=True)
        if score < 0.7:
            cv2.imwrite(f"slide{i}.png", current_frame)
            saved_frame = current_frame
            i += 1
    sleep(2)