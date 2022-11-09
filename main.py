import cv2
from time import time, sleep
from skimage.metrics import structural_similarity

cap = cv2.VideoCapture("https://100.70.74.109:8080/video")

saved_frame = None
i = 0
while True:
    ret, current_frame = cap.read()
    cv2.imshow("Input", current_frame)
    
    if saved_frame is None:
        cv2.imwrite(f"slide{i}.png", current_frame)
        saved_frame = current_frame
        i += 1
    else:
        score, diff = structural_similarity(cv2.cvtColor(saved_frame, cv2.COLOR_BGR2GRAY), cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY), full=True)
        if score < 0.6:
            cv2.imwrite(f"slide{i}.png", current_frame)
            saved_frame = current_frame
            i += 1


    c = cv2.waitKey(1)
    if c==27:
        break

cap.release()
cv2.destroyAllWindows()