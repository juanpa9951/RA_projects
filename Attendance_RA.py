def attendance(person_id,states_path):
        import datetime
        import pandas as pd
        import pyodbc
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

        ####.....................last known status...........................................
        states=pd.read_csv(states_path)  # read the last known states of the available persons

        ####...........................Main Program........................................
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
                result=str(first_name)+' '+str(last_name)+' '+str(person_id)+' registró '+str(state_new)+' a las '+str(date_time_register)   # print confirmation
            else:
                result='codigo No existente'

        elif person_id=='off':
            sw=0
        elif person_id=='':
            result=''
        else:
            result='codigo No existente'

        conexion.close()
        return result

