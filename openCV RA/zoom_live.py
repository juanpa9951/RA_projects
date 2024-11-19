import cv2

# Initialize variables for mouse position and zoom factor
mouse_x, mouse_y = 0, 0
zoom_factor = 3
zoom_size = 150  # Size of the square around the mouse to zoom into

# Function to update mouse coordinates
def update_mouse_position(event, x, y, flags, param):
    global mouse_x, mouse_y
    if event == cv2.EVENT_MOUSEMOVE:
        mouse_x, mouse_y = x, y

# Capture video from the default camera
cap = cv2.VideoCapture("rtsp://RA-camara3:RewAir2023@172.16.58.16:554/stream1")


# Set up mouse callback to capture mouse position
cv2.namedWindow("Live Stream with Zoom")
cv2.setMouseCallback("Live Stream with Zoom", update_mouse_position)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Calculate the coordinates of the zoomed ROI
    start_x = max(0, mouse_x - zoom_size // 2)
    start_y = max(0, mouse_y - zoom_size // 2)
    end_x = min(frame.shape[1], mouse_x + zoom_size // 2)
    end_y = min(frame.shape[0], mouse_y + zoom_size // 2)

    # Extract the region of interest (ROI) around the mouse pointer
    roi = frame[start_y:end_y, start_x:end_x]

    # Resize the ROI to simulate zooming
    zoomed_roi = cv2.resize(roi, (zoom_size * zoom_factor, zoom_size * zoom_factor), interpolation=cv2.INTER_LINEAR)

    # Define the top-left corner where the zoomed ROI will be displayed
    overlay_x, overlay_y = 10, 10  # Offset from the top-left corner

    # Overlay the zoomed ROI on the frame
    frame[overlay_y:overlay_y + zoomed_roi.shape[0], overlay_x:overlay_x + zoomed_roi.shape[1]] = zoomed_roi

    # Display the frame
    cv2.imshow("Live Stream with Zoom", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()







