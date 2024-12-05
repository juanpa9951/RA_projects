# import cv2
# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog
# import os
# import csv
# from datetime import datetime
# import threading
#
# # Global variables for camera
# capture_flag = True
# camera_feed = None
#
# # Directory for saving screenshots and data
# screenshot_dir = "screenshots"
# data_dir = "data"
#
# # Ensure directories exist
# os.makedirs(screenshot_dir, exist_ok=True)
# os.makedirs(data_dir, exist_ok=True)
#
# # Function to save screenshot and data
# def save_screenshot_and_data():
#     global camera_feed
#
#     if camera_feed is None:
#         print("Camera not initialized!")
#         return
#
#     # Collect user data from the entries
#     user_data = {
#         "ODF": entry1.get(),
#         "Pala": list1.get(),
#         "Proyect": list2.get(),
#         "Packaging": list3.get(),
#         "Numero": list4.get(),
#         "Side": list5.get(),
#         "Stack": list6.get(),
#     }
#
#     # Sanitize inputs for filenames (remove spaces and special characters)
#     sanitized_data = {key: "".join(e for e in value if e.isalnum() or e in "_-") for key, value in user_data.items()}
#
#     # Create a unique filename using the entries
#     filename_base = f"{sanitized_data['Stack']}"
#     filename_base = filename_base[:100]  # Limit filename length for safety
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     screenshot_filename = f"{filename_base}_{timestamp}.png"
#     screenshot_path = os.path.join(screenshot_dir, screenshot_filename)
#
#     # Prepare the image for saving with overlay
#     image_with_text = camera_feed.copy()
#     y_offset = 30  # Initial y-coordinate for text overlay
#     for key, value in user_data.items():
#         text = f"{key}: {value}"
#         cv2.putText(image_with_text,text,(10, y_offset), cv2.FONT_HERSHEY_SIMPLEX,0.6,(0, 255, 0),2,cv2.LINE_AA,)
#         y_offset += 30  # Move down for the next line of text
#
#     # Save the image with overlay
#     cv2.imwrite(screenshot_path, image_with_text)
#
#     # Save data to a CSV file
#     csv_file_path = os.path.join(data_dir, "user_data.csv")
#     file_exists = os.path.isfile(csv_file_path)
#     with open(csv_file_path, mode="a", newline="") as file:
#         writer = csv.DictWriter(file, fieldnames=list(user_data.keys()) + ["timestamp"])
#         if not file_exists:
#             writer.writeheader()
#         writer.writerow({**user_data, "timestamp": timestamp})
#
#     # Update the status label with the filename
#     status_label.config(text=f"Photo saved as: {screenshot_filename}")
#
#     print(f"Screenshot saved to: {screenshot_path}")
#     print("Data saved to CSV.")
#
#
# # Function to run the live camera stream
# def run_camera():
#     global capture_flag, camera_feed
#
#     cap = cv2.VideoCapture("rtsp://LP008:LP008ASM@192.168.2.82:554/stream1")  # Open camera (default: webcam 0)
#
#     while capture_flag:
#         ret, frame = cap.read()
#         if ret:
#             camera_feed = frame.copy()
#             cv2.imshow("Live Camera Feed", frame)
#         if cv2.waitKey(1) & 0xFF == ord("q"):  # Press 'q' to exit
#             capture_flag = False
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
# # Function to stop the program gracefully
# def on_close():
#     global capture_flag
#     capture_flag = False
#     root.destroy()
#
# # Function to save screenshot and data
#
# # GUI setup
# root = tk.Tk()
# root.title("Camera & Data Logger")
# root.protocol("WM_DELETE_WINDOW", on_close)
#
# # Add GUI elements
#
# tk.Label(root, text="ODF:").grid(row=0, column=0, padx=5, pady=5)
# entry1 = tk.Entry(root)
# entry1.grid(row=0, column=1, padx=5, pady=5)
#
# tk.Label(root, text="Pala S:").grid(row=0, column=2, padx=5, pady=5)
# list1 = ttk.Combobox(root, values=["1", "2", "3","4", "5", "6","7", "8", "9"])
# list1.grid(row=0, column=3, padx=5, pady=5)
# list1.set("")  # Default value
#
# tk.Label(root, text="Proyect:").grid(row=1, column=0, padx=5, pady=5)
# list2 = ttk.Combobox(root, values=["V236", "V136", "5X","6X"])
# list2.grid(row=1, column=1, padx=5, pady=5)
# list2.set("")  # Default value
#
# tk.Label(root, text="Packaging:").grid(row=2, column=0, padx=5, pady=5)
# list3 = ttk.Combobox(root, values=["Mesa", "Pallet", "Cuna"])
# list3.grid(row=2, column=1, padx=5, pady=5)
# list3.set("")  # Default value
#
# tk.Label(root, text="Numero:").grid(row=2, column=2, padx=5, pady=5)
# list4 = ttk.Combobox(root, values=["1", "2", "3","4", "5", "6","7", "8", "9","10", "11", "12","13", "14", "15"])
# list4.grid(row=2, column=3, padx=5, pady=5)
# list4.set("")  # Default value
#
# tk.Label(root, text="Side:").grid(row=3, column=0, padx=5, pady=5)
# list5 = ttk.Combobox(root, values=["WW", "LW", "Succion","Presion"])
# list5.grid(row=3, column=1, padx=5, pady=5)
# list5.set("")  # Default value
#
# tk.Label(root, text="STACK:").grid(row=3, column=2, padx=5, pady=5)
# list6 = ttk.Combobox(root, values=["1", "2", "3","4", "5", "6","7", "8", "9"])
# list6.grid(row=3, column=3, padx=5, pady=5)
# list6.set("")  # Default value
#
#
# # Button to take a screenshot
# tk.Button(root, text="Take Screenshot", command=save_screenshot_and_data).grid(row=4, column=0, columnspan=2, pady=10)
#
# # Status label to display the screenshot filename
# status_label = tk.Label(root, text="")
# status_label.grid(row=5, column=0, columnspan=2, pady=10)
#
# # Start the camera stream in a separate thread
# camera_thread = threading.Thread(target=run_camera, daemon=True)
# camera_thread.start()
#
# # Start the GUI loop
# root.mainloop()
#
# # Ensure proper shutdown
# capture_flag = False



import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import csv
from datetime import datetime
import threading
import pandas as pd

# Global variables for camera
capture_flag = True
camera_feed = None

# Directory for saving screenshots and data
screenshot_dir = "screenshots"
data_dir = "data"

# Ensure directories exist
os.makedirs(screenshot_dir, exist_ok=True)
os.makedirs(data_dir, exist_ok=True)

# Load the Excel data
file_path = "tab1.xlsx"  # Replace with your actual Excel file path
data_df = pd.read_excel(file_path, header=None)

# Process the Excel data
categories = data_df.iloc[0]  # First row: Categories
subcategories = data_df.iloc[1]  # Second row: Subcategories
values = data_df.iloc[2:]  # Third row onwards: Values

# Create a nested dictionary for categories and subcategories
data = {}
for col in data_df.columns:
    category = categories[col]
    subcategory = subcategories[col]
    data.setdefault(category, {})[subcategory] = values[col].dropna().tolist()


# Function to save screenshot and data
def save_screenshot_and_data():
    global camera_feed

    if camera_feed is None:
        print("Camera not initialized!")
        return

    # Collect user data from the entries
    user_data = {
        "ODF": entry1.get(),
        "Pala": list1.get(),
        "Proyect": list2.get(),
        "Packaging": list3.get(),
        "Numero": list4.get(),
        "Side": list5.get(),
        "Stack": list6.get(),
    }

    # Sanitize inputs for filenames (remove spaces and special characters)
    sanitized_data = {key: "".join(e for e in value if e.isalnum() or e in "_-") for key, value in user_data.items()}

    # Create a unique filename using the entries
    filename_base = f"{sanitized_data['Stack']}"
    filename_base = filename_base[:100]  # Limit filename length for safety
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_filename = f"{filename_base}_{timestamp}.png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_filename)

    # Prepare the image for saving with overlay
    image_with_text = camera_feed.copy()
    y_offset = 30  # Initial y-coordinate for text overlay
    for key, value in user_data.items():
        text = f"{key}: {value}"
        cv2.putText(image_with_text,text,(10, y_offset), cv2.FONT_HERSHEY_SIMPLEX,0.6,(0, 255, 0),2,cv2.LINE_AA,)
        y_offset += 30  # Move down for the next line of text

    # Save the image with overlay
    cv2.imwrite(screenshot_path, image_with_text)

    # Save data to a CSV file
    csv_file_path = os.path.join(data_dir, "user_data.csv")
    file_exists = os.path.isfile(csv_file_path)
    with open(csv_file_path, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(user_data.keys()) + ["timestamp"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({**user_data, "timestamp": timestamp})

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


# Function to update list5 values
def update_side(event=None):
    selected_category = list2.get()
    if selected_category in data:
        list5['values'] = list(data[selected_category].keys())  # Subcategories
    else:
        list5['values'] = []
    list5.set("")  # Clear current selection

# Function to update list6 values
def update_stack(event=None):
    selected_category = list2.get()
    selected_subcategory = list5.get()
    if selected_category in data and selected_subcategory in data[selected_category]:
        list6['values'] = data[selected_category][selected_subcategory]  # Values
    else:
        list6['values'] = []
    list6.set("")  # Clear current selection



# GUI setup
root = tk.Tk()
root.title("Camera & Data Logger")
root.protocol("WM_DELETE_WINDOW", on_close)

# Add GUI elements

tk.Label(root, text="ODF:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Pala S:").grid(row=0, column=2, padx=5, pady=5)
list1 = ttk.Combobox(root, values=["1", "2", "3","4", "5", "6","7", "8", "9"])
list1.grid(row=0, column=3, padx=5, pady=5)


tk.Label(root, text="Proyect:").grid(row=1, column=0, padx=5, pady=5)
list2 = ttk.Combobox(root, values=list(data.keys()))
list2.grid(row=1, column=1, padx=5, pady=5)


tk.Label(root, text="Packaging:").grid(row=2, column=0, padx=5, pady=5)
list3 = ttk.Combobox(root, values=["Mesa", "Pallet", "Cuna"])
list3.grid(row=2, column=1, padx=5, pady=5)


tk.Label(root, text="Numero:").grid(row=2, column=2, padx=5, pady=5)
list4 = ttk.Combobox(root, values=["1", "2", "3","4", "5", "6","7", "8", "9","10", "11", "12","13", "14", "15"])
list4.grid(row=2, column=3, padx=5, pady=5)


tk.Label(root, text="Side:").grid(row=3, column=0, padx=5, pady=5)
list5 = ttk.Combobox(root)
list5.grid(row=3, column=1, padx=5, pady=5)


tk.Label(root, text="STACK:").grid(row=3, column=2, padx=5, pady=5)
list6 = ttk.Combobox(root)
list6.grid(row=3, column=3, padx=5, pady=5)


# Bind events to update list values dynamically
list2.bind("<<ComboboxSelected>>", update_side)
list5.bind("<<ComboboxSelected>>", update_stack)



# Button to take a screenshot
tk.Button(root, text="Take Screenshot", command=save_screenshot_and_data).grid(row=4, column=0, columnspan=2, pady=10)

# Status label to display the screenshot filename
status_label = tk.Label(root, text="")
status_label.grid(row=5, column=0, columnspan=2, pady=10)


# Start the camera stream in a separate thread
camera_thread = threading.Thread(target=run_camera, daemon=True)
camera_thread.start()


# Start the GUI loop
root.mainloop()

# Ensure proper shutdown
capture_flag = False





