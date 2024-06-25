import tkinter as tk
import keyboard
import time
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Time
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from PIL import ImageTk, Image
from sqlalchemy import func, cast, Integer
import socket

def attendance(person_id):
    import datetime
    import pandas as pd
    import pyodbc
    ##########...........CONEXION A SQL SERVER...........................................................
    # Define the database connection parameters
    server = 'SQL-NEW'  # Replace with your SQL Server instance name or IP address
    database = 'DEMO_RA_ES_3'  # Replace with the name of your database
    username = 'saprepuser2'  # Replace with your database username
    password = 'wOxC0:R>xC!KC'  # Replace with your database password

    bd = 'DEMO_RA_ES_3'
    table_name = 'dbo].[@RA_ATTENDANCE'


    # Create a SQLAlchemy engine
    connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
    engine = create_engine(connection_string)

    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()

    # Define the table structure from SQL, el nombre puede ser cualquier cosa, yo le puse Register
    class Register(Base):  # estructura de tabla de sql
        __tablename__ = '@RA_ATTENDANCE'
        Code = Column(String)
        Name = Column(String)
        U_Person_ID = Column(String)
        U_Last_State = Column(String)
        U_Date_Time = Column(DateTime, primary_key=True)
        U_First_Name = Column(String)
        U_Last_Name = Column(String)
        U_CNumber = Column(String)
        U_Source = Column(String)
        U_Time = Column(String)
        U_Device = Column(String)


    class UpadateState(Base):
        __tablename__ = '@RA_ACC'
        U_Person_ID = Column(String, primary_key=True)
        U_Status = Column(String)
        U_Time = Column(String)
        U_Date_Time = Column(DateTime)
        U_CNumber = Column(String)
    # Create the tables in the database
    Base.metadata.create_all(engine)

    try:
        # Define your SQL query
        sql_query = """
            SELECT [U_Person_ID]
                  ,[U_AUT]
                  ,[U_AUT2]
                  ,[U_AUT3]
                  ,[U_Direction]
                  ,[U_Device]
                  ,[U_Serial]
                  ,[U_PName]
                  ,[U_CNumber]
                  ,[U_Status]
                  ,[U_First_Name]
                  ,[U_Last_Name]
                  ,[U_Time]
                  ,[U_Date_Time]
      
              FROM [DEMO_RA_ES_3].[dbo].[@RA_ACC]
            """
    except:
        print('error al intentar conectarse a SQL')
    # Use pandas to read the query results into a DataFrame
    employees_df = pd.read_sql_query(sql_query, engine)

    ####.....................last known status...........................................
    states = employees_df  # read the last known states of the available persons

    #

    ####...........................Main Program........................................

    date_time_register = datetime.datetime.now()  # extract the datetime of the event
    formatted_time = datetime.datetime.now().time()
    x=0
    test=0

    if person_id.isnumeric():  # check if the user entered a code number

        if person_id in states['U_CNumber'].values:  # check if the code exists
        # if int(person_id) in states['U_Person_ID'].values:  # check if the code exists
            # index_to_modify = states.index[states['U_Person_ID'] == int(person_id)].tolist()[0]  # find the index of the person code in the states file
            index_to_modify = states.index[states['U_CNumber'] == person_id].tolist()[0]
            DateIn = states.loc[states['U_CNumber'] == person_id, 'U_Date_Time'].iloc[0]

            def calculate_time_difference(current_time, input_time):
                """
                Calculate the time difference between two datetime objects.
                """
                difference = current_time - input_time
                return difference

                # Assuming 'DateIn' and 'Status' are already defined
                # Calculate the current datetime

                # Calculate the time difference

            time_diff = calculate_time_difference(date_time_register, DateIn)

            # Check if time difference is more than 8 hours and status is 1
            hours_difference = time_diff.total_seconds() / 3600
            segdiff = time_diff.total_seconds()


            if states.loc[index_to_modify, 'U_Status'] == str(0) and segdiff >= 25:  # change the state of the person from in to out, or out to in
                # states.at[in10064
                # dex_to_modify, 'Status'] = 1
                state_new = 'ENTRADA'
                state_acces = 1
            elif states.loc[index_to_modify, 'U_Status'] == str(1) and hours_difference <= 13 and segdiff >= 25:
                # states.at[index_to_modify, 'Status'] = 0
                state_new = 'SALIDA'
                state_acces = 0
                # states.to_csv(last_states_path, index=False)  # update the last known states file
            elif hours_difference > 13 and states.loc[index_to_modify, 'U_Status'] == str(1):
                state_new = 'OLVIDO SALIR'
                x = 1
                state_acces = 0
            elif pd.isnull(states.loc[index_to_modify, 'U_Status']):
                state_new = 'INGRESO'
                state_acces = str(1)
            # else:
            #     test = 2

            #     state_new = 'INGRESO'
            #     state_acces = str(1)
            try:
                # Update the record
                session.query(UpadateState) \
                    .filter(UpadateState.U_CNumber == person_id) \
                    .update({UpadateState.U_Status: state_acces,
                             UpadateState.U_Time: formatted_time,
                             UpadateState.U_Date_Time: date_time_register})
                session.commit()
            except Exception as e:
                print(f"An error occurred: {e}")
                session.rollback()


            #date_time_register = date_time_register.strftime("%Y-%m-%d %H:%M:%S")
            first_name = states.loc[index_to_modify, 'U_First_Name']
            last_name = states.loc[index_to_modify, 'U_Last_Name']
            DateIn = states.loc[index_to_modify, 'U_Date_Time']
            # max_id = session.query(func.max(Register.Code)).scalar()
            max_id = session.query(func.max(cast(Register.Code, Integer))).scalar()
            # next_id = 1 if max_id is None else int(max_id) + 1
            next_id = int(max_id) + 1
            card = states.loc[index_to_modify, 'U_Person_ID']
            device = socket.gethostname()

        # Save the inputs in an instance of Register
            new_register = Register(Code=next_id, Name=next_id, U_Person_ID=card, U_Last_State=state_new, U_Date_Time=date_time_register,
                                    U_First_Name=first_name, U_Last_Name=last_name, U_CNumber=person_id, U_Source='A', U_Time=formatted_time, U_Device=device)


            # send changes to the database
            session.add(new_register)
            session.commit()

            if x == 1:
                new_register = Register(Code=next_id+1, Name=next_id+1, U_Person_ID=card, U_Last_State='INGRESO',
                                    U_Date_Time=date_time_register,
                                    U_First_Name=first_name, U_Last_Name=last_name, U_CNumber=person_id, U_Source='A',
                                    U_Time=formatted_time, U_Device=device)
                session.add(new_register)
                session.commit()


            # Close the SQLAlchemy engine when done (optional)
            engine.dispose()
            result = str(first_name) + ' ' + str(last_name) + ' ' + str(card) + ' registró ' + str(
                state_new) + ' a las ' + str(date_time_register)  # print confirmation
        else:
            result = 'Usuario no Existente'

    elif person_id == 'off':
        sw = 0
    elif person_id == '':
        result = ''
    else:
        result = 'codigo No existente'

    # engine.close()
    return result

def wait_press_enter():  # this function presses Enter 2 seconds after typing any number
    time.sleep(2)  # Wait for 2 seconds
    keyboard.send('enter')  # Press the Enter key

def print_input(event=None): # this function executes the main code after the enter key press
    entered_text = entry.get()
    try:
        result_line=attendance(entered_text)
    except:
        result_line='error de fichaje'
    text_box.insert(1.0, f"{result_line}\n")
    entry.delete(0, tk.END)  # Clear the entry after printing

##....................to force the Enter key press............................
keyboard.add_hotkey('1', wait_press_enter)
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
image = Image.open(r"C:\Users\admabs\Pictures\rewair2.JPG")  # Replace "image.png" with your image file name and path
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