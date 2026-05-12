import cv2
import numpy as np
from mss import mss
import pyautogui
import time

COLOR_1 = np.array([17, 222, 254])
COLOR_2 = np.array([1, 45, 141])

TOLERANCE = 25
CLICK_COOLDOWN = 0.05
pyautogui.PAUSE = 0


CHECK_X = 960 
CHECK_Y = 540 

last_click = 0

print(f"Made by deeb.z (Jimbo1357) Monitoring for Yellow and Dark Red...")

with mss() as sct:
    monitor = {"top": CHECK_Y, "left": CHECK_X, "width": 1, "height": 1}
    
    while True:
        img = np.array(sct.grab(monitor))
        current_pixel = img[0, 0][:3]

        diff1 = np.abs(current_pixel - COLOR_1)
        match1 = np.all(diff1 <= TOLERANCE)

        diff2 = np.abs(current_pixel - COLOR_2)
        match2 = np.all(diff2 <= TOLERANCE)

        if match1 or match2:
            now = time.time()
            if (now - last_click) > CLICK_COOLDOWN:
                pyautogui.click()
                last_click = now
                tag = "YELLOW" if match1 else "DARK RED"
                print(f"TRIGGER: {tag} | Seen: {current_pixel}")

        time.sleep(0.001)