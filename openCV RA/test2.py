import cv2

# Global variables to store the mouse position
mouse_x, mouse_y = 0, 0


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
    global mouse_x, mouse_y
    if event == cv2.EVENT_MOUSEMOVE:
        mouse_x, mouse_y = x, y


def main():
    global mouse_x, mouse_y

    # Open a connection to the webcam (0 is the default camera)
    cap = cv2.VideoCapture("rtsp://LP008:LP008ASM@192.168.2.82:554/stream1")

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    cv2.namedWindow('Video Feed')
    cv2.setMouseCallback('Video Feed', mouse_callback)

    zoom_factor = 5.0  # Adjust zoom factor as needed
    zoom_size_ratio = 0.3  # Size of the zoomed window relative to the original frame

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
        x_offset, y_offset = 1300, 10  # Position of the zoomed frame in the corner
        frame[y_offset:y_offset + zoomed_frame_height, x_offset:x_offset + zoomed_frame_width] = zoomed_frame_small

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
