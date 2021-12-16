import cv2 as cv
import numpy as np
import pyautogui

resolution = (1920, 1080)

codec = cv.VideoWriter_fourcc(*"XVID")

filname = "Recording_1.mp4"

fps = 120.0

out = cv.VideoWriter(filname, codec, fps, resolution)

cv.namedWindow("Live", cv.WINDOW_NORMAL)

cv.resizeWindow("Live", 480, 270)

while True:
    img = pyautogui.screenshot()
    
    frame = np.array(img)
    
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    
    out.write(frame)
    
    cv.imshow('Live', frame)
    
    if cv.waitKey(1) == 27:
        break

out.release()
cv.destroyAllWindows()
