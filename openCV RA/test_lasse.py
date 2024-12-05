# import tkinter as tk
# from tkinter import ttk
#
# # Define data for dependencies
# data = {
#     ("Fruits", "Fresh"): ["Apple", "Banana", "Cherry"],
#     ("Fruits", "Dried"): ["Date", "Raisin", "Fig"],
#     ("Vegetables", "Green"): ["Spinach", "Broccoli", "Lettuce"],
#     ("Vegetables", "Root"): ["Carrot", "Potato", "Beetroot"],
#     ("Animals", "Domestic"): ["Dog", "Cat", "Cow"],
#     ("Animals", "Wild"): ["Elephant", "Fox", "Lion"]
# }
#
#
# def update_combobox_b(event=None):
#     # Get selected values from ComboBox A and ComboBox C
#     selected_a = combobox_a.get()
#     selected_c = combobox_c.get()
#
#     # Determine the values for ComboBox B based on the selected values
#     combobox_b['values'] = data.get((selected_a, selected_c), [])
#     combobox_b.set("")  # Clear the current selection in ComboBox B
#
#
# # Create the main application window
# root = tk.Tk()
# root.title("Multi-Dependent ComboBoxes")
#
# # ComboBox A (first selector)
# label_a = tk.Label(root, text="Select Category:")
# label_a.pack(pady=5)
# combobox_a = ttk.Combobox(root, values=["Fruits", "Vegetables", "Animals"])
# combobox_a.pack(pady=5)
#
# # ComboBox C (second selector)
# label_c = tk.Label(root, text="Select Type:")
# label_c.pack(pady=5)
# combobox_c = ttk.Combobox(root, values=["Fresh", "Dried", "Green", "Root", "Domestic", "Wild"])
# combobox_c.pack(pady=5)
#
# # ComboBox B (dependent on A and C)
# label_b = tk.Label(root, text="Select Item:")
# label_b.pack(pady=5)
# combobox_b = ttk.Combobox(root, values=[])
# combobox_b.pack(pady=5)
#
# # Bind events for selection change in ComboBox A and ComboBox C
# combobox_a.bind("<<ComboboxSelected>>", update_combobox_b)
# combobox_c.bind("<<ComboboxSelected>>", update_combobox_b)
#
# # Start the Tkinter event loop
# root.mainloop()





import tkinter as tk
from tkinter import ttk
import pandas as pd

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

# Function to update Combobox C (Subcategories) based on Combobox A (Categories)
def update_combobox_c(event=None):
    selected_category = combobox_a.get()
    if selected_category in data:
        combobox_c['values'] = list(data[selected_category].keys())  # Subcategories
    else:
        combobox_c['values'] = []
    combobox_c.set("")  # Clear current selection

# Function to update Combobox B (Values) based on Combobox A and C
def update_combobox_b(event=None):
    selected_category = combobox_a.get()
    selected_subcategory = combobox_c.get()
    if selected_category in data and selected_subcategory in data[selected_category]:
        combobox_b['values'] = data[selected_category][selected_subcategory]  # Values
    else:
        combobox_b['values'] = []
    combobox_b.set("")  # Clear current selection

# Tkinter Application
root = tk.Tk()
root.title("Dependent Comboboxes with Excel Data")

# Combobox A (Category selector)
label_a = tk.Label(root, text="Select Category:")
label_a.pack(pady=5)
combobox_a = ttk.Combobox(root, values=list(data.keys()))
combobox_a.pack(pady=5)

# Combobox C (Subcategory selector)
label_c = tk.Label(root, text="Select Subcategory:")
label_c.pack(pady=5)
combobox_c = ttk.Combobox(root)
combobox_c.pack(pady=5)

# Combobox B (Dependent values)
label_b = tk.Label(root, text="Select Item:")
label_b.pack(pady=5)
combobox_b = ttk.Combobox(root, values=[])
combobox_b.pack(pady=5)

# Bind events to update values dynamically
combobox_a.bind("<<ComboboxSelected>>", update_combobox_c)
combobox_c.bind("<<ComboboxSelected>>", update_combobox_b)

# Start the Tkinter event loop
root.mainloop()
