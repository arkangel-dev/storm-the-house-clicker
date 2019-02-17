import numpy as np
import pyautogui
import imutils
import cv2

template = cv2.imread('Alive.png')
img_original = pyautogui.screenshot(region=(18,400, 772, 194))
img_original = cv2.cvtColor(np.array(img_original), cv2.COLOR_RGB2BGR)
img_rgb = cv2.cvtColor(np.array(img_original), cv2.COLOR_RGB2BGR)

w, h = template.shape[:-1]

res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
threshold = 1
loc = np.where(res >= threshold)



targets_center_data_x = []
targets_center_data_y = []
for pt in zip(*loc[::-1]):  # Switch collumns and rows
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
	targets_center_data_y.append(int(pt[1] + (h/2)))
	targets_center_data_x.append(int(pt[0] + (w/2)))


target_count = len(targets_center_data_y)
print("Target count : " + str(target_count))
	
#for x in range(len(targets_bound_box_data_x)):
	

cv2.imwrite('targets.png', img_rgb)
cv2.imwrite('screenshot.png', img_original)

