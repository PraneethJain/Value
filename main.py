import cv2
from skimage.metrics import structural_similarity
from time import time

cap = cv2.VideoCapture("https://100.70.74.109:8080/video")

saved_frame = None
last_time = time()
i = 0
while True:
    cap.grab()
    ret, current_frame = cap.read()

    if time() - last_time < 5:
        continue

    if saved_frame is None:
        cv2.imwrite(f"slide{i}.png", current_frame)
        saved_frame = current_frame
        last_time = time()
        i += 1
    else:
        score, diff = structural_similarity(
            cv2.cvtColor(saved_frame, cv2.COLOR_BGR2GRAY),
            cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY),
            full=True,
        )
        if score < 0.85:
            cv2.imwrite(f"slide{i}.png", current_frame)
            saved_frame = current_frame
            last_time = time()
            i += 1
