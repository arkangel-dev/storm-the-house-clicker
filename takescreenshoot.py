# import the necessary packages
import numpy as np
import pyautogui
import imutils
import cv2

image = pyautogui.screenshot(region=(18,350, 772, 300))
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("in_memory_to_disk.png", image)