import pyodbc
import pandas as pd
###...........CONEXION A SQL SERVER............
driver='{ODBC Driver 17 for SQL Server}'   # utilizar cualquier driver de la lista    ODBC Driver 17 for SQL Server  or   SQL SERVER
server='RAES034'
bd='AdventureWorks2019'
usuario='soporte'
contrasena='1234'
try:
    conexion = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+bd+';Trust_Connection=yes;UID='+usuario+';PWD='+contrasena)
    print('conexion exitosa')
except :
    print('error al intentar')
###...................INFO DE LA TABLA DE INTERES.......................
table_name='dbo].[tabla_pruebas'
column1='nombre'
column2='codigo'
column3='departamento'
# ACA LEEMOS LA TABLA ACTUAL DE SQL
SQL_QUERY = f"""
SELECT TOP (100) [{column1}]
      ,[{column2}]
      ,[{column3}]
  FROM [{bd}].[{table_name}]   
"""
####.......................................................................

sql_DataFrame=pd.read_sql_query(SQL_QUERY,conexion) # dataframe extracted from sql query
print('esta es la tabla actual de sql \n',sql_DataFrame)

#leer la tabla fuente
tabla_forms = pd.read_excel(r'C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\fuente.xlsx')
tabla_forms=tabla_forms[['nombre','codigo','departamento']]
print('esta es la tabla fuente del forms \n',tabla_forms)

#combine tables
combined=pd.concat([sql_DataFrame,tabla_forms],ignore_index=True,sort=False).drop_duplicates()
#find the different rows (new registers)
nuevos_registros = pd.concat([sql_DataFrame,combined]).drop_duplicates(keep=False,ignore_index=True)
print('estas son las diferencias (registros nuevos) \n',nuevos_registros)

idx=0
for w in nuevos_registros[column1]:  #here we write the new registers in the sql table
    value1=nuevos_registros[column1][idx]
    value2=nuevos_registros[column2][idx]
    value3=nuevos_registros[column3][idx]
    SQL_WRITE = f"""
    INSERT INTO [{bd}].[{table_name}] (
        [{column1}],
        [{column2}],
        [{column3}]
    )
    VALUES
        (
            '{value1}',
            '{value2}',
            '{value3}'
        );
    """
    cursor = conexion.cursor()
    cursor.execute(SQL_WRITE)
    cursor.commit()
    cursor.close()
    idx=idx+1

conexion.close()