# import cv2
# import numpy as np
#
# import yolov3
#
# # Load YOLOv5 model
# image = cv2.imread(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Pictures\object detection\ob1.jpg')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# model = yolov5.load('yolov5s.pt')



# import cv2
#
# # Read the image
# image = cv2.imread(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Pictures\object detection\ob1.jpg')
#
# # Convert the image to grayscale
# grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Detect objects in the image
# object_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# faces = object_detector.detectMultiScale(grayscale_image, 1.1, 4)
#
# # Visualize the results
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# # Display the image
# cv2.imshow('Image with detected objects', image)
# cv2.waitKey(0)


# import cv2
#
# image = cv2.imread(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Pictures\object detection\ob2.jpg')
#
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Detect edges using Canny edge detection
# edges = cv2.Canny(gray, 50, 150)
#
# # Detect circles using HoughCircles
# circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1.0, 200, minRadius=1, maxRadius=100)
#
# # Draw circles on the image
# if circles is not None:
#     circles = np.uint16(np.around(circles))
#     for (x, y, r) in circles:
#         cv2.circle(image, (x, y), r, (0, 255, 0), 2)
#
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()







import cv2
import numpy as np

# Read the image
image = cv2.imread(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Pictures\object detection\ob4.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

# Apply Hough Circle Transform
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    1,
    minDist=700,
    param1=50,
    param2=30,
    minRadius=50,
    maxRadius=100
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Draw the outer circle
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Draw the center of the circle
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('Detected circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()



# import cv2
#
# # Read the image
# image = cv2.imread(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Pictures\object detection\ob5.jpg')
#
# # Convert to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Edge detection
# edges = cv2.Canny(gray_image, 50, 150)
#
# # Find contours
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Filter triangles
# filtered_contours = []
# for contour in contours:
#     if len(contour) == 3:
#         # Check angles
#         points = contour.reshape(-1, 2)
#         angles = []
#         for i in range(len(points) - 2):
#             p1 = points[i]
#             p2 = points[i + 1]
#             p3 = points[i + 2]
#             v1 = p2 - p1
#             v2 = p3 - p2
#             cross = v1.dot(v2)
#             if cross > 0:
#                 angles.append(np.arctan2(np.linalg.norm(p2 - p1), np.linalg.norm(p3 - p2)))
#             else:
#                 angles.append(np.pi - np.arctan2(np.linalg.norm(p2 - p1), np.linalg.norm(p3 - p2)))
#
#         # Check ratios
#         ratios = []
#         for i in range(len(angles)):
#             ratio = (angles[i] - angles[(i + 1) % 3]) / (angles[(i + 2) % 3] - angles[i])
#             ratios.append(abs(ratio))
#
#         if all([ratio > 0.5 and ratio < 1.5 for ratio in ratios]):
#             filtered_contours.append(contour)
#
# # Draw contours
# cv2.drawContours(image, filtered_contours, -1, (0, 255, 0), 2)
#
# # Display the image with detected triangles
# cv2.imshow('Image with Detected Triangles', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
