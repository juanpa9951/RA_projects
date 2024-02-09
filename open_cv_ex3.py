import numpy as np
import cv2

img_ori = cv2.resize(cv2.imread(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Pictures\object detection\im5.png', -1), (0, 0), fx=1, fy=1)

img = cv2.resize(cv2.imread(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Pictures\object detection\im5.png', 0), (0, 0), fx=1, fy=1)
template = cv2.resize(cv2.imread(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Pictures\object detection\tem5.png', 0), (0, 0), fx=1, fy=1)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img_ori, location, bottom_right, 155, 5)
    cv2.imshow('Match', img_ori)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# print(img[130][340])