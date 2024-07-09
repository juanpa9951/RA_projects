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
button_position = (10, 80)
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
    radius = 10
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
    global mouse_x, mouse_y, points, lines_drawn

    # Open a connection to the webcam (0 is the default camera)
    cap = cv2.VideoCapture("rtsp://LP008:LP008ASM@192.168.2.82:554/stream1")

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    cv2.namedWindow('Video Feed')
    cv2.setMouseCallback('Video Feed', mouse_callback)

    zoom_factor = 5.0  #    ### 5.0  Adjust zoom factor as needed
    zoom_size_ratio = 0.3   ### 0.3    # Size of the zoomed window relative to the original frame

    while True:
        # Read a frame from the video feed
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        height, width = frame.shape[:2]

        # Apply zoom and draw circle to the frame based on the mouse position
        zoomed_frame = zoom_and_draw_circle(frame, zoom_factor, mouse_x, mouse_y)

        # Resize the zoomed frame to fit in the corner
        zoomed_frame_height = int(height * zoom_size_ratio)
        zoomed_frame_width = int(width * zoom_size_ratio)
        zoomed_frame_small = cv2.resize(zoomed_frame, (zoomed_frame_width, zoomed_frame_height))

        # Overlay the zoomed frame onto the original frame
        x_offset, y_offset = 10, 10  # Position of the zoomed frame in the corner
        frame[y_offset:y_offset + zoomed_frame_height, x_offset:x_offset + zoomed_frame_width] = zoomed_frame_small

        # Draw lines between clicked points
        # Draw the lines and coordinates on the frame
        for line in lines:
            cv2.line(frame, line[0], line[1], (0, 255, 0), 2)

        # Display the combined frame
        cv2.imshow('Video Feed', frame)

        # Exit loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
