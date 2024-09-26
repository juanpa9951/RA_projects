

import cv2
import numpy as np
import os
import tkinter as tk
from PIL import Image, ImageTk

# Predefined directory to save screenshots
save_directory = r"C:\Users\Juan Pablo Lopez\Downloads"  # You can change this to your desired folder

# Create the directory if it doesn't exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Screenshot counter
screenshot_counter = 0
screenshot_button_pressed = False

# Function to capture and save the screenshot
def save_screenshot(frame):
    global screenshot_counter
    screenshot_counter += 1
    # Create the file path with an incrementing number
    file_path = os.path.join(save_directory, f"screenshot_{screenshot_counter}.png")
    cv2.imwrite(file_path, frame)
    print(f"Screenshot saved as: {file_path}")

# Function to capture frames from the cameras and display in Tkinter window
def update_frame():
    global screenshot_button_pressed, combined_frame

    # Capture frames from both cameras
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if ret1 and ret2:
        # Resize frames to ensure they have the same width
        frame1 = cv2.resize(frame1, (1280, 480))  # Resize to 640x480
        frame2 = cv2.resize(frame2, (1280, 480))  # Resize to 640x480

        # Concatenate frames one above the other (vertically)
        combined_frame = np.vstack((frame1, frame2))

        # Convert the frame to RGB for displaying in Tkinter
        combined_frame_rgb = cv2.cvtColor(combined_frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(combined_frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)

        # Update the Tkinter label with the new frame
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)

    # If screenshot button is pressed, save the screenshot
    if screenshot_button_pressed:
        save_screenshot(combined_frame)
        screenshot_button_pressed = False

    # Schedule the next frame update
    video_label.after(10, update_frame)

# Function to handle screenshot button press
def on_screenshot_button():
    global screenshot_button_pressed
    screenshot_button_pressed = True

# Open video streams for two cameras
cap1 = cv2.VideoCapture("rtsp://RA-camara3:RewAir2023@172.16.58.16:554/stream1")  # Camera 1
cap2 = cv2.VideoCapture("rtsp://RA-camaras:RewAir2023@172.16.58.142:554/stream1")  # Camera 2

# Check if cameras are opened successfully
if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Cannot open one or both video streams.")
    exit()

# Create the main Tkinter window
root = tk.Tk()
root.title("Camera Stream with Screenshot Button")

# Create a label in the Tkinter window to show the video stream
video_label = tk.Label(root)
video_label.pack()

# Create a button to take a screenshot
screenshot_button = tk.Button(root, text="Take Screenshot", command=on_screenshot_button)
screenshot_button.pack()

# Start updating the frame in the Tkinter window
update_frame()

# Start the Tkinter event loop
root.mainloop()

# Release the video streams when the window is closed
cap1.release()
cap2.release()
