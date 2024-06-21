### THIS CODE FILTERS IMAGES ACCORDING TO A COLOR RANGE, CREATES A MASK SHOWING ONLY THE OBJECTS (PIXELS) WITH THAT COLOR

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


#### CODES INDEX
#### 1 THIS CODE FILTERS IMAGES ACCORDING TO A COLOR RANGE, CREATES A MASK SHOWING ONLY THE OBJECTS (PIXELS) WITH THAT COLOR
#### 2 THIS CODE RECEIVES A TEMPLATE IMAGE AND IT TRIES TO FIND THE TEMPLATE INSIDE ANOTHER PICTURE USING DIFFERENT METHODS
#### 3 THIS CODE DISPLAYS PIXEL POSITION MAP ACROSS THE IMAGE
#### 4 THIS CODE FINDS OBJECTS IN A UNIFORM BACKGROUND AND MEASURES THEM INSIDE AN IMAGE
#### 5 THIS CODE JOINS SEPARATE PICTURES INTO 1 PANOMARIC
#### 6 THIS CODE DISPLAYS COLOR MAP VALUES ACROSS THE IMAGE
#### 7 THIS CODE IS FOR DETECTING BORDERS OF OBJECTS USING CHANGES IN PIXELS AND MEASURES THEM
#### 8 THIS CODE FINDS REAL TIME VIDEO OBJECTS IN A UNIFORM BACKGROUND AND MEASURES THEM
#### 9 THIS CODE FINDS LIVE POSITIONS OF ITEMS IN UNIFORM BACKGROUND WITH REFERENCE POSITIONS
#### 10 THIS CODE DISPLAYS LIVE COLOR MAP VALUES ACROSS THE IMAGE
#### 11 THIS CODE DISPLAYS LIVE PIXEL POSITIONS ACROSS THE IMAGE
#### 12 THIS CODE CALCULATES THE DISTANCE TRAVELLED BY A BLACK LINE (OR POINT) TRAVELLING ACROSS THE IMAGE ON A VIDEO