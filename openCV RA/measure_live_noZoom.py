###### LIVE VIDEO VERSION WITH DIMENSION MEASUREMENT
def euclidean_distance(point1, point2):
    import math
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
def find_closest_tupleV2(tuples_list_real,tuples_list_autocad, input_tuple):
    #### same as V1 but only 1 output
    closest_tuple_low = None
    closest_tuple_high = None
    idx_low=None
    idx_high=None

    smallest_distance = float('inf')  # Initialize with a large number
    i=0
    for tup in tuples_list_real:
        distance = euclidean_distance(tup, input_tuple)
        if distance < smallest_distance and tup[0]<input_tuple[0] and tup[1]<input_tuple[1]:
            smallest_distance = distance
            closest_tuple_low = tup
            idx_low=i
        i=i+1

    smallest_distance = float('inf')  # Initialize with a large number
    i=0
    for tup in tuples_list_real:
        distance = euclidean_distance(tup, input_tuple)
        if distance < smallest_distance and tup[0]>input_tuple[0] and tup[1]>input_tuple[1]:
            smallest_distance = distance
            closest_tuple_high = tup
            idx_high=i
        i=i+1

    ### interpolate X value from real to autocad
    target_value=input_tuple[0]
    a_prev = tuples_list_real[idx_low][0]
    a_next = tuples_list_real[idx_high][0]
    b_prev = tuples_list_autocad[idx_low][0]
    b_next = tuples_list_autocad[idx_high][0]
    # Perform linear interpolation
    interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
    x_interp=interpolated_value


    ### interpolate Y value from real to autocad
    target_value =input_tuple[1]
    a_prev = tuples_list_real[idx_low][1]
    a_next = tuples_list_real[idx_high][1]
    b_prev = tuples_list_autocad[idx_low][1]
    b_next = tuples_list_autocad[idx_high][1]
    # Perform linear interpolation
    interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
    y_interp=interpolated_value

    xy_tup=(x_interp,y_interp)


    return xy_tup,idx_low,idx_high,closest_tuple_low,closest_tuple_high

# .....LOAD THE TABLE CALIBRATION DATA.......................................................................................................
import pandas as pd
excel_table_calib = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras ASM004\feeder_right.xlsx'
Surface_map = pd.read_excel(excel_table_calib, sheet_name='lona', header=0)
tuples_list_real=[]
tuples_list_pixel=[]
for i in range(0,len(Surface_map)):
    x_tup_pixel = Surface_map['X_pixel'][i]
    y_tup_pixel = Surface_map['Y_pixel'][i]
    tuples_list_pixel.append((x_tup_pixel,y_tup_pixel))
    x_tup_real = Surface_map['X_real'][i]
    y_tup_real = Surface_map['Y_real'][i]
    tuples_list_real.append((x_tup_real,y_tup_real))
def distance_real(col1,col2,row1,row2):
    import math
    start_point_pixel = (col1, row1)
    start_point_real, idx_low1, idx_high1, tup_low1, tup_high1 = find_closest_tupleV2(tuples_list_pixel,tuples_list_real,start_point_pixel)
    end_point_pixel = (col2, row2)
    end_point_real, idx_low2, idx_high2, tup_low2, tup_high2 = find_closest_tupleV2(tuples_list_pixel,tuples_list_real,end_point_pixel)
    distance_X=round(abs(end_point_real[0]-start_point_real[0]),2)
    distance_Y=round(abs(end_point_real[1]-start_point_real[1]),2)
    hyp=round(math.sqrt(distance_X**2+distance_Y**2),2)
    return distance_X, distance_Y,hyp


import cv2
import os
os.chdir(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras ASM004\capturas')

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

# cap = cv2.VideoCapture("rtsp://LP003:LP003ASM@192.168.2.76:554/stream1")  ### asm001
# cap = cv2.VideoCapture("rtsp://LP002:LP002ASM@192.168.2.72:554/stream1")  ### asm005
# cap = cv2.VideoCapture("rtsp://MSM005:LP005ASM@172.16.58.15:554/stream1")  ### ud tapes
# cap = cv2.VideoCapture("rtsp://LP006:LP006ASM@192.168.2.79:554/stream1")  ### asm003 der
# cap = cv2.VideoCapture("rtsp://LP005:LP005ASM@192.168.2.75:554/stream1")  ### asm003 izq
# cap = cv2.VideoCapture("rtsp://LP001:LP001ASM@192.168.2.71:554/stream1")  ### asm002 izq
# cap = cv2.VideoCapture("rtsp://LP004:LP004ASM@192.168.2.78:554/stream1")  ### asm002 der
# cap = cv2.VideoCapture("rtsp://LP008:LP008ASM@192.168.2.82:554/stream1")  ### asm004 der
# cap = cv2.VideoCapture("rtsp://LP009:LP009ASM@192.168.2.84:554/stream1") ### asm004 izq
# cap = cv2.VideoCapture("rtsp://RA-camara3:RewAir2023@172.16.58.16:554/stream1")  ## tagging 1


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
        cv2.line(frame, line[0], line[1], (0, 255, 0), 1)
    for i, line in enumerate(lines):
        if i < 2:  # Only display the coordinates of the first two lines
            col1=line[0][0]
            col2=line[1][0]
            row1=line[0][1]
            row2=line[1][1]
            xt,yt,hyp =distance_real(col1,col2,row1,row2)
            cv2.putText(frame, f"dist x= {xt}, dist y= {yt}, hyp= {hyp}", (10, 30 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1,cv2.LINE_AA)


    # Draw the button
    cv2.rectangle(frame, (button_rect[0], button_rect[1]), (button_rect[2], button_rect[3]), button_color, -1)
    cv2.putText(frame, button_text, (button_rect[0] + 5, button_rect[1] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    # Display the frame
    cv2.imshow("Live Feed", frame)

    # Save screenshot if the button was pressed
    if button_pressed:
        screenshot_filename = f"screenshots\screenshot_{screenshot_count}.png"
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



