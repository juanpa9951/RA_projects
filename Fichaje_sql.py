import keyboard
import time
import datetime
import pandas as pd
import pyodbc
###########......... this function is required for enter pressing........................
def wait_press_enter():  # this function presses Enter 2 seconds after typing any number
    time.sleep(2)  # Wait for 2 seconds
    keyboard.send('enter')  # Press the Enter key
#............................................................................

##########...........CONEXION A SQL SERVER...........................................................
driver='{ODBC Driver 17 for SQL Server}'   # utilizar cualquier driver de la lista    ODBC Driver 17 for SQL Server  or   SQL SERVER
server='RAES034'
bd='AdventureWorks2019'
usuario='soporte'
contrasena='1234'
table_name='dbo].[attendance2'
try:
    conexion = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+bd+';Trust_Connection=yes;UID='+usuario+';PWD='+contrasena)
    print('conexion exitosa a SQL server')
except :
    print('error al intentar conectarse a SQL')
#...................................................................................

####.....................last known status...........................................
states_path=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\output.csv'  # location of last known states file
states=pd.read_csv(states_path)  # read the last known states of the available persons
#.........................................................................................

####...........................Main Program........................................
sw=1
while sw==1:   # this loops
    keyboard.add_hotkey('1', wait_press_enter) # assign the key of number 1 to the wait_press_enter function
    keyboard.add_hotkey('2', wait_press_enter) # assign the key of number 2 to the wait_press_enter function
    keyboard.add_hotkey('3', wait_press_enter) # assign the key of number 3 to the wait_press_enter function
    keyboard.add_hotkey('4', wait_press_enter) # assign the key of number 4 to the wait_press_enter function
    keyboard.add_hotkey('5', wait_press_enter) # assign the key of number 5 to the wait_press_enter function
    keyboard.add_hotkey('6', wait_press_enter) # assign the key of number 6 to the wait_press_enter function
    keyboard.add_hotkey('7', wait_press_enter) # assign the key of number 7 to the wait_press_enter function
    keyboard.add_hotkey('8', wait_press_enter) # assign the key of number 8 to the wait_press_enter function
    keyboard.add_hotkey('9', wait_press_enter) # assign the key of number 9 to the wait_press_enter function
    keyboard.add_hotkey('esc', lambda: keyboard.unhook_all_hotkeys())  # assign the key 'esc' to anull all previous key functions
    person_id=input('ACERQUE LA TARJETA---> ')   # user input
    keyboard.unhook_all_hotkeys() # anull all previous key functions , i think should go here instead of at the end
    if person_id.isnumeric():   # check if the user entered a code number
        if int(person_id) in states['Person_ID'].values:   # check if the code exists
            index_to_modify = states.index[states['Person_ID'] == int(person_id)].tolist()[0]   # find the index of the person code in the states file
            if states.loc[index_to_modify,'Status'] == 0:    # change the state of the person from in to out, or out to in
                states.at[index_to_modify, 'Status'] = 1
                state_new = 'INGRESO'
            else:
                states.at[index_to_modify, 'Status'] = 0
                state_new = 'SALIDA'
            states.to_csv(states_path, index=False)   # update the last known states file
            date_time_register = datetime.datetime.now()   # extract the datetime of the event
            first_name=states.loc[index_to_modify,'First_Name']
            last_name=states.loc[index_to_modify,'Last_Name']
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
            print('persona ',person_id, ' registro ' ,state_new,' a las ', date_time_register)   # print confirmation
        else:
            print('codigo No existente')

    elif person_id=='off':
        sw=0
    elif person_id=='':
        print('')
    else:
        print('codigo No existente')

keyboard.unhook_all_hotkeys()
conexion.close()
print('End of program')

