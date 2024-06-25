import cv2
import numpy as np
img = cv2.imread('im1.png', 1)
img = cv2.resize(img, (0, 0),fx=1, fy=1)



hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

result = cv2.bitwise_and(img, img, mask=mask)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 15)
corners = np.int0(corners)

for corner in corners:
	x, y = corner.ravel()
	cv2.circle(img, (x, y), 7, (255, 0, 0), -1)

# for i in range(len(corners)):
# 	for j in range(i + 1, len(corners)):
# 		corner1 = tuple(corners[i][0])
# 		corner2 = tuple(corners[j][0])
# 		color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
# 		cv2.line(img, corner1, corner2, color, 1)



cv2.imshow('original', img)
cv2.imshow('color detection', result)
cv2.imshow('mascara', mask)


cv2.waitKey(0)
cv2.destroyAllWindows()