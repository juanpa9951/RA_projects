###### LIVE FEED MEASUREMENT WITH ZOOM AND DIFFERENT COLORS

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

# Global variables to store the mouse position and clicked points
mouse_x, mouse_y = 0, 0
points = []
lines_drawn = 0
lines = []
line_count = 0
drawing = False
button_pressed = False

# Define button properties
button_text = "Save Screenshot"
button_color = (0, 255, 0)
button_position = (10, 900)
button_size = (150, 30)
button_rect = (button_position[0], button_position[1], button_position[0] + button_size[0], button_position[1] + button_size[1])


def zoom_and_draw_circle(frame, zoom_factor, x, y):
    height, width = frame.shape[:2]

    # Calculate the cropping coordinates
    new_width, new_height = int(width / zoom_factor), int(height / zoom_factor)
    x1 = max(0, x - new_width // 2)
    y1 = max(0, y - new_height // 2)
    x2 = min(width, x + new_width // 2)
    y2 = min(height, y + new_height // 2)

    # Ensure the cropped area does not go out of the frame
    if x2 - x1 < new_width:
        x2 = x1 + new_width
    if y2 - y1 < new_height:
        y2 = y1 + new_height

    # Crop and resize the frame
    zoomed_frame = frame[y1:y2, x1:x2]
    zoomed_frame = cv2.resize(zoomed_frame, (width, height))

    # Draw a small blue circle in the middle of the zoomed frame
    center_x, center_y = width // 2, height // 2
    radius = 7
    color = (255, 0, 0)  # Blue color in BGR
    thickness = -1  # Filled circle
    cv2.circle(zoomed_frame, (center_x, center_y), radius, color, thickness)

    return zoomed_frame


def mouse_callback(event, x, y, flags, param):
    global mouse_x, mouse_y, points, lines_drawn, points, lines, line_count, drawing, button_pressed
    if event == cv2.EVENT_MOUSEMOVE:
        mouse_x, mouse_y = x, y
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


def main():
    global mouse_x, mouse_y, points, lines_drawn,button_pressed

    #### Open a connection to the webcam (0 is the default camera)
    # cap = cv2.VideoCapture("rtsp://LP003:LP003ASM@192.168.2.76:554/stream1")  ### asm001
    # cap = cv2.VideoCapture("rtsp://LP002:LP002ASM@192.168.2.72:554/stream1")  ### asm005
    # cap = cv2.VideoCapture("rtsp://MSM005:LP005ASM@172.16.58.15:554/stream1")  ### ud tapes
    # cap = cv2.VideoCapture("rtsp://LP006:LP006ASM@192.168.2.79:554/stream1")  ### asm003 der
    # cap = cv2.VideoCapture("rtsp://LP005:LP005ASM@192.168.2.75:554/stream1")  ### asm003 izq
    # cap = cv2.VideoCapture("rtsp://LP001:LP001ASM@192.168.2.71:554/stream1")  ### asm002 izq
    # cap = cv2.VideoCapture("rtsp://LP004:LP004ASM@192.168.2.78:554/stream1")  ### asm002 der
    # cap = cv2.VideoCapture("rtsp://LP008:LP008ASM@192.168.2.82:554/stream1")  ### asm004 der
    cap = cv2.VideoCapture("rtsp://LP009:LP009ASM@192.168.2.84:554/stream1") ### asm004 izq
    # cap = cv2.VideoCapture("rtsp://RA-camara3:RewAir2023@172.16.58.16:554/stream1")  ## tagging 1

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    cv2.namedWindow('Video Feed')
    # cv2.namedWindow("Video Feed", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('Video Feed', mouse_callback)

    zoom_factor = 5.0  #    ### 5.0  Adjust zoom factor as needed
    zoom_size_ratio = 0.3   ### 0.3    # Size of the zoomed window relative to the original frame

    screenshot_count = 0

    while True:
        # Read a frame from the video feed
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        height, width = frame.shape[:2]
        #print("height ",height," width ", width)

        # Apply zoom and draw circle to the frame based on the mouse position
        zoomed_frame = zoom_and_draw_circle(frame, zoom_factor, mouse_x, mouse_y)

        # Resize the zoomed frame to fit in the corner
        zoomed_frame_height = int(height * zoom_size_ratio)
        zoomed_frame_width = int(width * zoom_size_ratio)
        zoomed_frame_small = cv2.resize(zoomed_frame, (zoomed_frame_width, zoomed_frame_height))

        # Overlay the zoomed frame onto the original frame
        x_offset, y_offset = 10, 10  # Position of the zoomed frame in the corner
        frame[y_offset:y_offset + zoomed_frame_height, x_offset:x_offset + zoomed_frame_width] = zoomed_frame_small


        # Draw the lines and coordinates on the frame
        color_line1 = (0, 255, 0)
        color_line2 = (255, 150, 0)


        ln=0    #### this is for assigning different colors
        for line in lines:
            if ln == 0:
                color_line = color_line1
            else:
                color_line = color_line2
            cv2.line(frame, line[0], line[1], color_line, 1)
            ln=ln+1
        for i, line in enumerate(lines):
            if i < 2:  # Only display the coordinates of the first two lines
                col1 = line[0][0]
                col2 = line[1][0]
                row1 = line[0][1]
                row2 = line[1][1]
                xt, yt, hyp = distance_real(col1, col2, row1, row2)
                if i==0:    #### this is for assigning different colors
                    color_line=color_line1
                else:
                    color_line = color_line2
                cv2.putText(frame, f"dist x= {xt}, dist y= {yt}, hyp= {hyp}", (1000, 30 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color_line, 1, cv2.LINE_AA)


        # Draw the button
        cv2.rectangle(frame, (button_rect[0], button_rect[1]), (button_rect[2], button_rect[3]), button_color, -1)
        cv2.putText(frame, button_text, (button_rect[0] + 5, button_rect[1] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 0, 0), 1, cv2.LINE_AA)

        # Display the combined frame
        cv2.imshow('Video Feed', frame)

        # Save screenshot if the button was pressed
        if button_pressed:
            screenshot_filename = rf"C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras\capturas\screenshots\screenshot_{screenshot_count}.png"
            cv2.imwrite(screenshot_filename, frame)
            print(f"Screenshot saved as {screenshot_filename}")
            button_pressed = False
            screenshot_count += 1


        # Exit loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
