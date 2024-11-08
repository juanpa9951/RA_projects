######   CODES RETRIEVED FROM PERSONAL PC




def distance():
    col2=end_point[0]
    row2=end_point[1]
    col1=start_point[0]
    row1=start_point[1]
    xt=abs(col2-col1)
    yt=abs(row2-row1)
    return xt,yt


##### draws 1 line over image, converts coordenates, display and save screenshot
# import os
# os.chdir(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras\capturas')
# import cv2
# import numpy as np
# import datetime
#
# # Initialize global variables
# drawing = False  # True if the mouse is pressed
# start_point = (-1, -1)
# end_point = (-1, -1)
# line_drawn = False  # True if the line is drawn
# button_pressed=False
# last_time='0'
#
# # Mouse callback function
# def draw_line(event, x, y, flags, param):
#     global start_point, end_point, drawing, line_drawn, button_pressed
#
#     # Check if the click is within the button bounds
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if 10 <= x <= 110 and 460 <= y <= 490:
#             button_pressed = True
#             return
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         start_point = (x, y)
#         line_drawn = False
#
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing:
#             end_point = (x, y)
#
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         end_point = (x, y)
#         line_drawn = True
#         print(f"Line drawn from {start_point} to {end_point}")
#
# # Load the image from local file
# image_path = 'im5.png'  # Replace with your image path
# image = cv2.imread(image_path)
#
# if image is None:
#     print("Could not open or find the image")
#     exit()
#
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_line)
#
# while True:
#     img_copy = image.copy()
#     if start_point != (-1, -1) and end_point != (-1, -1):
#         cv2.line(img_copy, start_point, end_point, (255, 0, 0), 2)
#
#     if line_drawn:
#         text = f"Start: {start_point}, End: {end_point}"
#         cv2.putText(img_copy, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#
#         xt,yt=distance()
#         text2= f"Difference x: {xt}, Difference y: {yt}"
#         cv2.putText(img_copy, text2, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#
#     # Draw the button
#     cv2.rectangle(img_copy, (10, 460), (110, 490), (0, 255, 0), -1)
#     cv2.putText(img_copy, "Save", (30, 480), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
#     cv2.imshow('image', img_copy)
#
#     if button_pressed:
#         screenshot_path = 'screenshot3.jpg'  # Replace with your desired path
#         cv2.imwrite(screenshot_path, img_copy)
#         print(f"Screenshot saved to {screenshot_path}")
#         cv2.putText(img_copy, text3, (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#         current_time = datetime.datetime.now()
#         last_time = current_time.strftime("%H:%M:%S")
#         button_pressed = False
#
#     text3= f"Last saved at: {last_time}"
#     cv2.putText(img_copy, text3, (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#
#     cv2.imshow('image', img_copy)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:  # Press 'ESC' to exit
#         break
#     elif k == ord('s'):  # Press 's' to save the current frame
#         screenshot_path = 'screenshot.jpg'  # Replace with your desired path
#         cv2.imwrite(screenshot_path, img_copy)
#         print(f"Screenshot saved to {screenshot_path}")
#
# cv2.destroyAllWindows()






##### draws 1 line over video, converts coordenates, display and save screenshot
# import cv2
# import numpy as np
# import datetime
#
# # Initialize global variables
# drawing = False  # True if the mouse is pressed
# start_point = (-1, -1)
# end_point = (-1, -1)
# line_drawn = False  # True if the line is drawn
# button_pressed = False
# last_time='0'
#
# # Mouse callback function
#
# def draw_line(event, x, y, flags, param):
#     global start_point, end_point, drawing, line_drawn, button_pressed
#
#     # Check if the click is within the button bounds
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if 10 <= x <= 110 and 460 <= y <= 490:
#             button_pressed = True
#             return
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         start_point = (x, y)
#         line_drawn = False
#
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing:
#             end_point = (x, y)
#
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         end_point = (x, y)
#         line_drawn = True
#         print(f"Line drawn from {start_point} to {end_point}")
#
#
#
# # Capture video from the webcam
# cap = cv2.VideoCapture(0)
#
# if not cap.isOpened():
#     print("Error: Could not open video stream.")
#     exit()
#
# cv2.namedWindow('Video Feed')
# cv2.setMouseCallback('Video Feed', draw_line)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Error: Could not read frame.")
#         break
#
#     img_copy = frame.copy()
#     if start_point != (-1, -1) and end_point != (-1, -1):
#         cv2.line(img_copy, start_point, end_point, (255, 0, 0), 2)
#
#     if line_drawn:
#         text = f"Start: {start_point}, End: {end_point}"
#         cv2.putText(img_copy, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#
#         xt,yt=distance()
#         text2= f"Difference x: {xt}, Difference y: {yt}"
#         cv2.putText(img_copy, text2, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#
#
#     # Draw the button
#     cv2.rectangle(img_copy, (10, 460), (110, 490), (0, 255, 0), -1)
#     cv2.putText(img_copy, "Save", (30, 480), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
#
#
#
#     if button_pressed:
#         screenshot_path = 'screenshot3.jpg'  # Replace with your desired path
#         cv2.imwrite(screenshot_path, img_copy)
#         print(f"Screenshot saved to {screenshot_path}")
#         current_time = datetime.datetime.now()
#         last_time = current_time.strftime("%H:%M:%S")
#         button_pressed = False
#
#     text3= f"Last saved at: {last_time}"
#     cv2.putText(img_copy, text3, (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#     cv2.imshow('Video Feed', img_copy)
#
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:  # Press 'ESC' to exit
#         break
#     elif k == ord('s'):  # Press 's' to save the current frame
#         screenshot_path = 'screenshot2.jpg'  # Replace with your desired path
#         cv2.imwrite(screenshot_path, img_copy)
#         print(f"Screenshot saved to {screenshot_path}")
#
# cap.release()
# cv2.destroyAllWindows()




##### draws 1 rectangle over video, converts coordenates, display and save screenshot
# import cv2
# import numpy as np
#
# # Initialize global variables
# drawing = False  # True if the mouse is pressed
# top_left_corner = (-1, -1)
# bottom_right_corner = (-1, -1)
# rectangle_drawn = False  # True if the rectangle is drawn
# button_pressed = False
#
# # Mouse callback function
# def draw_rectangle(event, x, y, flags, param):
#     global top_left_corner, bottom_right_corner, drawing, rectangle_drawn, button_pressed
#
#     # Check if the click is within the button bounds
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if 10 <= x <= 110 and 460 <= y <= 490:
#             button_pressed = True
#             return
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         top_left_corner = (x, y)
#         rectangle_drawn = False
#
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing:
#             bottom_right_corner = (x, y)
#
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         bottom_right_corner = (x, y)
#         rectangle_drawn = True
#         print(f"Rectangle drawn from {top_left_corner} to {bottom_right_corner}")
#
# # Capture video from the webcam
# cap = cv2.VideoCapture(0)
#
# if not cap.isOpened():
#     print("Error: Could not open video stream.")
#     exit()
#
# cv2.namedWindow('Video Feed')
# cv2.setMouseCallback('Video Feed', draw_rectangle)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Error: Could not read frame.")
#         break
#
#     img_copy = frame.copy()
#     if top_left_corner != (-1, -1) and bottom_right_corner != (-1, -1):
#         cv2.rectangle(img_copy, top_left_corner, bottom_right_corner, (255, 0, 0), 2)
#
#     if rectangle_drawn:
#         text = f"Top-left: {top_left_corner}, Bottom-right: {bottom_right_corner}"
#         cv2.putText(img_copy, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#
#     # Draw the button
#     cv2.rectangle(img_copy, (10, 460), (110, 490), (0, 255, 0), -1)
#     cv2.putText(img_copy, "Save", (30, 480), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
#
#     cv2.imshow('Video Feed', img_copy)
#
#     if button_pressed:
#         screenshot_path = 'path_to_save_screenshot.jpg'  # Replace with your desired path
#         cv2.imwrite(screenshot_path, img_copy)
#         print(f"Screenshot saved to {screenshot_path}")
#         button_pressed = False
#
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:  # Press 'ESC' to exit
#         break
#
# cap.release()
# cv2.destroyAllWindows()




######   this draws multiple lines, fixed image

# import cv2
# import os
# os.chdir(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras\capturas')
#
# # Global variables to store points
# points = []
# lines = []
#
# # Mouse callback function to draw lines
# def draw_lines(event, x, y, flags, param):
#     global points, lines, img
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         points.append((x, y))
#
#         # Once we have two points, draw the line and store the line points
#         if len(points) == 2:
#             cv2.line(img, points[0], points[1], (0, 255, 0), 2)
#             lines.append((points[0], points[1]))
#             print(f"Line from {points[0]} to {points[1]}")
#             points = []
#
#     cv2.imshow("Image", img)
#
# # Load an image
# img = cv2.imread('im5.png')
# if img is None:
#     print("Could not open or find the image.")
#     exit(0)
#
# # Create a window and set the mouse callback function
# cv2.namedWindow("Image")
# cv2.setMouseCallback("Image", draw_lines)
#
# # Display the image
# while True:
#     cv2.imshow("Image", img)
#     key = cv2.waitKey(1) & 0xFF
#
#     # Exit the loop when 'q' is pressed
#     if key == ord('q'):
#         break
#
# cv2.destroyAllWindows()









#
# ######## draws 2 lines, reset, and display
# import cv2
# import os
# os.chdir(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras\capturas')
# # Global variables to store points and lines
# points = []
# lines = []
# line_count = 0
#
# # Mouse callback function to draw lines
# def draw_lines(event, x, y, flags, param):
#     global points, lines, img, line_count, original_img
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         points.append((x, y))
#
#         # Once we have two points, draw the line and store the line points
#         if len(points) == 2:
#             cv2.line(img, points[0], points[1], (0, 255, 0), 2)
#             lines.append((points[0], points[1]))
#             print(f"Line from {points[0]} to {points[1]}")
#             points = []
#             line_count += 1
#
#         # Display the coordinates of the first two lines
#         if len(lines) <= 2:
#             for i, line in enumerate(lines):
#                 cv2.putText(img, f"{line[0]} to {line[1]}", (10, 30 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
#
#         # Check if three lines are drawn
#         if line_count == 3:
#             print("Three lines drawn. Resetting the image.")
#             # Reset the image
#             img = original_img.copy()
#             line_count = 0
#             lines.clear()
#
#     cv2.imshow("Image", img)
#
# # Load an image
# original_img = cv2.imread('im5.png')
# if original_img is None:
#     print("Could not open or find the image.")
#     exit(0)
#
# # Make a copy of the original image to reset later
# img = original_img.copy()
#
# # Create a window and set the mouse callback function
# cv2.namedWindow("Image")
# cv2.setMouseCallback("Image", draw_lines)
#
# # Display the image
# while True:
#     cv2.imshow("Image", img)
#     key = cv2.waitKey(1) & 0xFF
#
#     # Exit the loop when 'q' is pressed
#     if key == ord('q'):
#         break
#
# cv2.destroyAllWindows()



# ###### video, draws 2 lines, reset, and display
#
# import cv2
#
# # Global variables to store points and lines
# points = []
# lines = []
# line_count = 0
# drawing = False
#
# # Mouse callback function to draw lines
# def draw_lines(event, x, y, flags, param):
#     global points, lines, line_count, drawing
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         points.append((x, y))
#         drawing = True
#
#         # Once we have two points, draw the line and store the line points
#         if len(points) == 2:
#             lines.append((points[0], points[1]))
#             print(f"Line from {points[0]} to {points[1]}")
#             points = []
#             line_count += 1
#             drawing = False
#
#         # Check if three lines are drawn
#         if line_count == 3:
#             print("Three lines drawn. Resetting the lines.")
#             line_count = 0
#             lines.clear()
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
#
# if not cap.isOpened():
#     print("Error: Could not open video stream.")
#     exit()
#
# # Create a window and set the mouse callback function
# cv2.namedWindow("Live Feed")
# cv2.setMouseCallback("Live Feed", draw_lines)
#
# # Main loop to display the live feed
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Error: Failed to capture image.")
#         break
#
#     # Draw the lines and coordinates on the frame
#     for line in lines:
#         cv2.line(frame, line[0], line[1], (0, 255, 0), 2)
#     for i, line in enumerate(lines):
#         if i < 2:  # Only display the coordinates of the first two lines
#             cv2.putText(frame, f"{line[0]} to {line[1]}", (10, 30 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
#
#     # Display the frame
#     cv2.imshow("Live Feed", frame)
#
#     # Break the loop when 'q' is pressed
#     key = cv2.waitKey(1) & 0xFF
#     if key == ord('q'):
#         break
#
# # Release the webcam and close all windows
# cap.release()
# cv2.destroyAllWindows()






# ###### video, draws 2 lines, reset, and display with distance calculator
#
# import cv2
#
# # Global variables to store points and lines
# points = []
# lines = []
# line_count = 0
# drawing = False
#
# # Mouse callback function to draw lines
# def draw_lines(event, x, y, flags, param):
#     global points, lines, line_count, drawing
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         points.append((x, y))
#         drawing = True
#
#         # Once we have two points, draw the line and store the line points
#         if len(points) == 2:
#             lines.append((points[0], points[1]))
#             print(f"Line from {points[0]} to {points[1]}")
#             points = []
#             line_count += 1
#             drawing = False
#
#         # Check if three lines are drawn
#         if line_count == 3:
#             print("Three lines drawn. Resetting the lines.")
#             line_count = 0
#             lines.clear()
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
#
# if not cap.isOpened():
#     print("Error: Could not open video stream.")
#     exit()
#
# # Create a window and set the mouse callback function
# cv2.namedWindow("Live Feed")
# cv2.setMouseCallback("Live Feed", draw_lines)
#
# # Main loop to display the live feed
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Error: Failed to capture image.")
#         break
#
#     # Draw the lines and coordinates on the frame
#     for line in lines:
#         cv2.line(frame, line[0], line[1], (0, 255, 0), 2)
#     for i, line in enumerate(lines):
#         if i < 2:  # Only display the coordinates of the first two lines
#             col1=line[0][0]
#             col2=line[1][0]
#             row1=line[0][1]
#             row2=line[1][1]
#             xt=abs(col2-col1)
#             yt=abs(row2-row1)
#             cv2.putText(frame, f"dist x= {xt}, dist y= {yt}", (10, 30 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1,cv2.LINE_AA)
#
#     # Display the frame
#     cv2.imshow("Live Feed", frame)
#
#     # Break the loop when 'q' is pressed
#     key = cv2.waitKey(1) & 0xFF
#     if key == ord('q'):
#         break
#
# # Release the webcam and close all windows
# cap.release()
# cv2.destroyAllWindows()






# ###### video, draws 2 lines, reset, and display with distance calculator, save screenshot
import cv2
import os
os.chdir(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras\capturas')


# Global variables to store points, lines, and button state
points = []
lines = []
line_count = 0
drawing = False
button_pressed = False

# Define button properties
button_text = "Save Screenshot"
button_color = (0, 255, 0)
button_position = (10, 80)
button_size = (150, 30)
button_rect = (button_position[0], button_position[1], button_position[0] + button_size[0], button_position[1] + button_size[1])

# Mouse callback function to draw lines and handle button click
def draw_lines(event, x, y, flags, param):
    global points, lines, line_count, drawing, button_pressed

    if event == cv2.EVENT_LBUTTONDOWN:
        if button_rect[0] <= x <= button_rect[2] and button_rect[1] <= y <= button_rect[3]:
            button_pressed = True
            return

        points.append((x, y))
        drawing = True

        # Once we have two points, draw the line and store the line points
        if len(points) == 2:
            lines.append((points[0], points[1]))
            print(f"Line from {points[0]} to {points[1]}")
            points = []
            line_count += 1
            drawing = False

        # Check if three lines are drawn
        if line_count == 3:
            print("Three lines drawn. Resetting the lines.")
            line_count = 0
            lines.clear()

# Initialize the webcam


camera_url_der="rtsp://LP008:LP008ASM@192.168.2.82:554/stream1"
camera_url_izq="rtsp://LP009:LP009ASM@192.168.2.84:554/stream1"
cap = cv2.VideoCapture(camera_url_der)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Create a window and set the mouse callback function
cv2.namedWindow("Live Feed")
cv2.setMouseCallback("Live Feed", draw_lines)

# Main loop to display the live feed
screenshot_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Draw the lines and coordinates on the frame
    for line in lines:
        cv2.line(frame, line[0], line[1], (0, 255, 0), 2)
    for i, line in enumerate(lines):
        if i < 2:  # Only display the coordinates of the first two lines
            col1=line[0][0]
            col2=line[1][0]
            row1=line[0][1]
            row2=line[1][1]
            xt=abs(col2-col1)
            yt=abs(row2-row1)
            cv2.putText(frame, f"dist x= {xt}, dist y= {yt}", (10, 30 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1,cv2.LINE_AA)


    # Draw the button
    cv2.rectangle(frame, (button_rect[0], button_rect[1]), (button_rect[2], button_rect[3]), button_color, -1)
    cv2.putText(frame, button_text, (button_rect[0] + 5, button_rect[1] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    # Display the frame
    cv2.imshow("Live Feed", frame)

    # Save screenshot if the button was pressed
    if button_pressed:
        screenshot_filename = f"screenshot_{screenshot_count}.png"
        cv2.imwrite(screenshot_filename, frame)
        print(f"Screenshot saved as {screenshot_filename}")
        button_pressed = False
        screenshot_count += 1

    # Break the loop when 'q' is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()



###### image, draws 2 lines, reset, and display with distance calculator, save screenshot
# import cv2
# import os
# os.chdir(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras\capturas')
#
# # Global variables to store points, lines, and button state
# points = []
# lines = []
# line_count = 0
# drawing = False
# button_pressed = False
#
# # Define button properties
# button_text = "Save Screenshot"
# button_color = (0, 255, 0)
# button_position = (10, 80)
# button_size = (150, 30)
# button_rect = (button_position[0], button_position[1], button_position[0] + button_size[0], button_position[1] + button_size[1])
#
# # Mouse callback function to draw lines and handle button click
# def draw_lines(event, x, y, flags, param):
#     global points, lines, line_count, drawing, button_pressed
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if button_rect[0] <= x <= button_rect[2] and button_rect[1] <= y <= button_rect[3]:
#             button_pressed = True
#             return
#
#         points.append((x, y))
#         drawing = True
#
#         # Once we have two points, draw the line and store the line points
#         if len(points) == 2:
#             lines.append((points[0], points[1]))
#             print(f"Line from {points[0]} to {points[1]}")
#             points = []
#             line_count += 1
#             drawing = False
#
#         # Check if three lines are drawn
#         if line_count == 3:
#             print("Three lines drawn. Resetting the lines.")
#             line_count = 0
#             lines.clear()
#
# # Load an image from a local file
# image_path = 'F3.png'
# original_img = cv2.imread(image_path)
# if original_img is None:
#     print("Error: Could not open or find the image.")
#     exit()
#
# # Create a copy of the original image to draw on
# img = original_img.copy()
#
# # Create a window and set the mouse callback function
# cv2.namedWindow("Image")
# cv2.setMouseCallback("Image", draw_lines)
#
# # Initialize screenshot count
# screenshot_count = 0
#
# # Main loop to display the image and handle interactions
# while True:
#     frame = img.copy()
#
#     # Draw the lines and coordinates on the frame
#     for line in lines:
#         cv2.line(frame, line[0], line[1], (0, 255, 0), 2)
#     for i, line in enumerate(lines):
#         if i < 2:  # Only display the coordinates of the first two lines
#             col1=line[0][0]
#             col2=line[1][0]
#             row1=line[0][1]
#             row2=line[1][1]
#             xt=abs(col2-col1)
#             yt=abs(row2-row1)
#             cv2.putText(frame, f"dist x= {xt}, dist y= {yt}", (10, 30 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1,cv2.LINE_AA)
#
#
#     # Draw the button
#     cv2.rectangle(frame, (button_rect[0], button_rect[1]), (button_rect[2], button_rect[3]), button_color, -1)
#     cv2.putText(frame, button_text, (button_rect[0] + 5, button_rect[1] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
#
#     # Display the frame
#     cv2.imshow("Image", frame)
#
#     # Save screenshot if the button was pressed
#     if button_pressed:
#         screenshot_filename = f"screenshot_{screenshot_count}.png"
#         cv2.imwrite(screenshot_filename, frame)
#         print(f"Screenshot saved as {screenshot_filename}")
#         button_pressed = False
#         screenshot_count += 1
#
#     # Break the loop when 'q' is pressed
#     key = cv2.waitKey(1) & 0xFF
#     if key == ord('q'):
#         break
#
# # Close all windows
# cv2.destroyAllWindows()



