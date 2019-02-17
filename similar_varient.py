import numpy as np
import pyautogui
import imutils
import cv2
import time

while True:
	# img_rgb = cv2.imread('screenshot.png')
	# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	
	image_raw = pyautogui.screenshot(region=(18,350, 772, 300))
	img_rgb = cv2.cvtColor(np.array(image_raw), cv2.COLOR_RGB2BGR)
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	
	template = cv2.imread('alive.png',0)
	w, h = template.shape[::-1]
	# target_count = 8
	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = .925
	loc = np.where( res >= threshold)
	
	# for pt in zip(*loc[::-1]):
		# pyautogui.click((pt[0] + 20),(pt[1] + 360))
		# pyautogui.click((pt[0] + 20),(pt[1] + 360))
		# print(pt[0])
		# print(pt[1])
	pt = [0,0]
	if len(loc[1]) != 0:
		pt[0] = loc[1][0]
		pt[1] = loc[0][0]
		# print(pt[0])
		# print(pt[1])
		if (pt[1]) and (pt[0]):
			pyautogui.click((pt[0] + 25),(pt[1] + 360))
			pyautogui.click((pt[0] + 25),(pt[1] + 360))
		
	#print(target_count)
	#cv2.imwrite('Detected.png', img_rgb)
	#time.sleep(3)