import tkinter as tk
import keyboard
import time
from PIL import ImageTk, Image

last_states_path=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\output.csv'  # this is a .csv listing the [existent codes,first name,last name,last state]

def attendance(person_id, last_states_path):
    import datetime
    import pandas as pd
    import pyodbc
    x=yeah
    ##########...........CONEXION A SQL SERVER...........................................................
    driver = '{ODBC Driver 17 for SQL Server}'  # utilizar cualquier driver de la lista    ODBC Driver 17 for SQL Server  or   SQL SERVER
    server = 'RAES034'
    bd = 'AdventureWorks2019'
    usuario = 'soporte'
    contrasena = '1234'
    table_name = 'dbo].[attendance2'
    try:
        conexion = pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + bd + ';Trust_Connection=yes;UID=' + usuario + ';PWD=' + contrasena)
        print('conexion exitosa a SQL server')
    except:
        print('error al intentar conectarse a SQL')

    ####.....................last known status...........................................
    states = pd.read_csv(last_states_path)  # read the last known states of the available persons

    ####...........................Main Program........................................
    if person_id.isnumeric():  # check if the user entered a code number
        if int(person_id) in states['Person_ID'].values:  # check if the code exists
            index_to_modify = states.index[states['Person_ID'] == int(person_id)].tolist()[0]  # find the index of the person code in the states file
            if states.loc[index_to_modify, 'Status'] == 0:  # change the state of the person from in to out, or out to in
                states.at[index_to_modify, 'Status'] = 1
                state_new = 'INGRESO'
            else:
                states.at[index_to_modify, 'Status'] = 0
                state_new = 'SALIDA'
            states.to_csv(last_states_path, index=False)  # update the last known states file
            date_time_register = datetime.datetime.now()  # extract the datetime of the event
            first_name = states.loc[index_to_modify, 'First_Name']
            last_name = states.loc[index_to_modify, 'Last_Name']
            SQL_WRITE = f"""
            INSERT INTO [{bd}].[{table_name}] (
                [Person_ID],
                [Last_State],
                [Date_Time],
                [First_Name],
                [Last_Name]
            )
            VALUES
                (
                    '{person_id}',
                    '{state_new}',
                    '{date_time_register}',
                    '{first_name}',
                    '{last_name}'
                );
            """
            cursor = conexion.cursor()
            cursor.execute(SQL_WRITE)
            cursor.commit()
            cursor.close()
            result = str(first_name) + ' ' + str(last_name) + ' ' + str(person_id) + ' registró ' + str(
                state_new) + ' a las ' + str(date_time_register)  # print confirmation
        else:
            result = 'codigo No existente'

    elif person_id == 'off':
        sw = 0
    elif person_id == '':
        result = ''
    else:
        result = 'codigo No existente'

    conexion.close()
    return result

def wait_press_enter():  # this function presses Enter 2 seconds after typing any number
    time.sleep(2)  # Wait for 2 seconds
    keyboard.send('enter')  # Press the Enter key
#............................................................................

def print_input(event=None): # this function executes the main code after the enter key press
    entered_text = entry.get()
    try:
        result_line=attendance(entered_text,last_states_path)
    except:
        result_line="Error de fichaje doble"
    text_box.insert(1.0, f"{result_line}\n")
    entry.delete(0, tk.END)  # Clear the entry after printing

##....................to force the Enter key press............................
keyboard.add_hotkey('1', wait_press_enter)  # assign the key of number 1 to the wait_press_enter function
keyboard.add_hotkey('2', wait_press_enter)  # assign the key of number 2 to the wait_press_enter function
keyboard.add_hotkey('3', wait_press_enter)  # assign the key of number 3 to the wait_press_enter function
keyboard.add_hotkey('4', wait_press_enter)  # assign the key of number 4 to the wait_press_enter function
keyboard.add_hotkey('5', wait_press_enter)  # assign the key of number 5 to the wait_press_enter function
keyboard.add_hotkey('6', wait_press_enter)  # assign the key of number 6 to the wait_press_enter function
keyboard.add_hotkey('7', wait_press_enter)  # assign the key of number 7 to the wait_press_enter function
keyboard.add_hotkey('8', wait_press_enter)  # assign the key of number 8 to the wait_press_enter function
keyboard.add_hotkey('9', wait_press_enter)  # assign the key of number 9 to the wait_press_enter function
keyboard.add_hotkey('esc', lambda: keyboard.unhook_all_hotkeys())
#.....................................................................................


# Create the main window
root = tk.Tk()
root.title("User Input")

# Load the image file
image = Image.open(r"C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Pictures\rewair2.JPG")  # Replace "image.png" with your image file name and path
photo = ImageTk.PhotoImage(image)
# Create a Label for the image
image_label = tk.Label(root, image=photo)
image_label.pack()

# first label
label = tk.Label(root, text="ACERQUE LA TARJETA AL LECTOR")
label.pack()

# Create an Entry widget for user input
entry = tk.Entry(root, width=30)
entry.pack()

# Bind the <Return> or <KP_Enter> key to the print_input function
entry.bind("<Return>", print_input)
entry.bind("<KP_Enter>", print_input)

# # Create a button to print the input
# print_button = tk.Button(root, text="Print Input", command=print_input)
# print_button.pack()

# intermediate label
label = tk.Label(root, text="ÚLTIMOS REGISTROS")
label.pack()

# Create a Text widget to display printed text
text_box = tk.Text(root, width=80, height=10)
text_box.pack()


# Start the main loop
root.mainloop()
