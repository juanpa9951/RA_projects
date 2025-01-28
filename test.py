import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def submit_form():
    # Get the values from the input fields
    user_string = entry_string.get()
    user_list = combo_list.get()  # Get the selected value from the dropdown

    # Print the values to the console
    print(f"String Input: {user_string}")
    print(f"Selected List Item: {user_list}")

    # Optionally, show a message box with the inputs
    messagebox.showinfo("Form Submitted", f"String: {user_string}\nSelected Item: {user_list}")


# Create the main window
root = tk.Tk()
root.title("User Form")

# Create and place the label and entry for the string input
label_string = tk.Label(root, text="Enter a String:")
label_string.pack(pady=5)

entry_string = tk.Entry(root, width=40)
entry_string.pack(pady=5)

# Create and place the label and dropdown for the list input
label_list = tk.Label(root, text="Select an Item:")
label_list.pack(pady=5)

# Define the options for the dropdown
options = ["tea", "coffee", "soda", "water"]

# Create a Combobox (dropdown) with the options
combo_list = ttk.Combobox(root, values=options, width=37)
combo_list.current(0)  # Set the default selected item (optional)
combo_list.pack(pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=20)

# Start the main event loop
root.mainloop()