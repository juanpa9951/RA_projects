import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import csv
from datetime import datetime
import threading

# Global variables for camera
capture_flag = True
camera_feed = None

# Directory for saving screenshots and data
screenshot_dir = "screenshots"
data_dir = "data"

# Ensure directories exist
os.makedirs(screenshot_dir, exist_ok=True)
os.makedirs(data_dir, exist_ok=True)

# Function to save screenshot and data
def save_screenshot_and_data():
    global camera_feed

    if camera_feed is None:
        print("Camera not initialized!")
        return

    # Collect user data from the entries
    user_data = {
        "Entry 1": entry1.get(),
        "Entry 2": entry2.get(),
        "List 1": list1.get(),
        "List 2": list2.get(),
        "Entry 3": entry3.get(),
    }

    # Sanitize inputs for filenames (remove spaces and special characters)
    sanitized_data = {key: "".join(e for e in value if e.isalnum() or e in "_-") for key, value in user_data.items()}

    # Create a unique filename using the entries
    filename_base = f"{sanitized_data['Entry 1']}_{sanitized_data['Entry 2']}_{sanitized_data['List 1']}_{sanitized_data['List 2']}_{sanitized_data['Entry 3']}"
    filename_base = filename_base[:100]  # Limit filename length for safety
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_filename = f"{filename_base}_{timestamp}.png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_filename)

    # Prepare the image for saving with overlay
    image_with_text = camera_feed.copy()
    y_offset = 30  # Initial y-coordinate for text overlay
    for key, value in user_data.items():
        text = f"{key}: {value}"
        cv2.putText(
            image_with_text,
            text,
            (10, y_offset),  # x, y position
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,  # Font scale
            (0, 255, 0),  # Color (Green)
            2,  # Thickness
            cv2.LINE_AA,
        )
        y_offset += 30  # Move down for the next line of text

    # Save the image with overlay
    cv2.imwrite(screenshot_path, image_with_text)

    # Save data to a CSV file
    csv_file_path = os.path.join(data_dir, "user_data.csv")
    file_exists = os.path.isfile(csv_file_path)
    with open(csv_file_path, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(user_data.keys()) + ["Screenshot Path"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({**user_data, "Screenshot Path": screenshot_path})

    # Update the status label with the filename
    status_label.config(text=f"Photo saved as: {screenshot_filename}")

    print(f"Screenshot saved to: {screenshot_path}")
    print("Data saved to CSV.")


# Function to run the live camera stream
def run_camera():
    global capture_flag, camera_feed

    cap = cv2.VideoCapture("rtsp://LP008:LP008ASM@192.168.2.82:554/stream1")  # Open camera (default: webcam 0)

    while capture_flag:
        ret, frame = cap.read()
        if ret:
            camera_feed = frame.copy()
            cv2.imshow("Live Camera Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):  # Press 'q' to exit
            capture_flag = False
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to stop the program gracefully
def on_close():
    global capture_flag
    capture_flag = False
    root.destroy()

# Function to save screenshot and data

# GUI setup
root = tk.Tk()
root.title("Camera & Data Logger")
root.protocol("WM_DELETE_WINDOW", on_close)

# Add GUI elements
tk.Label(root, text="Entry 1:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Entry 2:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="List 1:").grid(row=2, column=0, padx=5, pady=5)
list1 = ttk.Combobox(root, values=["Option A", "Option B", "Option C"])
list1.grid(row=2, column=1, padx=5, pady=5)
list1.set("Option A")  # Default value

tk.Label(root, text="List 2:").grid(row=3, column=0, padx=5, pady=5)
list2 = ttk.Combobox(root, values=["Choice 1", "Choice 2", "Choice 3"])
list2.grid(row=3, column=1, padx=5, pady=5)
list2.set("Choice 1")  # Default value

tk.Label(root, text="Entry 3:").grid(row=4, column=0, padx=5, pady=5)
entry3 = tk.Entry(root)
entry3.grid(row=4, column=1, padx=5, pady=5)

# Button to take a screenshot
tk.Button(root, text="Take Screenshot", command=save_screenshot_and_data).grid(row=5, column=0, columnspan=2, pady=10)

# Status label to display the screenshot filename
status_label = tk.Label(root, text="")
status_label.grid(row=6, column=0, columnspan=2, pady=10)

# Start the camera stream in a separate thread
camera_thread = threading.Thread(target=run_camera, daemon=True)
camera_thread.start()

# Start the GUI loop
root.mainloop()

# Ensure proper shutdown
capture_flag = False









