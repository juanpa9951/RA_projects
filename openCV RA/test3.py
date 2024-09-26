import cv2

def zoom_in(frame, zoom_factor):
    # Get the dimensions of the frame
    height, width = frame.shape[:2]

    # Calculate the center of the frame
    center_x, center_y = width // 2, height // 2

    # Calculate the region of interest (ROI) to crop
    new_width = int(width / zoom_factor)
    new_height = int(height / zoom_factor)

    # Make sure the coordinates are within the frame size
    x1 = max(center_x - new_width // 2, 0)
    x2 = min(center_x + new_width // 2, width)
    y1 = max(center_y - new_height // 2, 0)
    y2 = min(center_y + new_height // 2, height)

    # Crop the region of interest (ROI)
    roi = frame[y1:y2, x1:x2]

    # Resize back to the original frame size
    zoomed_frame = cv2.resize(roi, (width, height))

    return zoomed_frame

# Open the video stream (e.g., webcam or video file)
cap = cv2.VideoCapture("rtsp://RA-camara3:RewAir2023@172.16.58.16:554/stream1")  # Change 0 to a filename for video file

# Set the zoom factor (higher means more zoom)
zoom_factor = 3

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Apply zoom
    zoomed_frame = zoom_in(frame, zoom_factor)

    # Display the zoomed frame
    cv2.imshow('Zoomed Video', zoomed_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
