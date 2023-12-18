##.......EXISTEN METODOS QUE FUNCIONAN...........
##...................NO FUNCIONA..................
# import MySQLdb
# db = MySQLdb.connect(user='soporte',
#                    password='1234',
#                    host='RAES034',   #16.0.1000.6
#                    database='AdventureWorks2019')

##..............................NO FUNCIONA..........
# import mysql.connector
# from mysql.connector import Error
# def create_connection(host_name, user_name, user_password):
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host=host_name,
#             user=user_name,
#             passwd=user_password
#         )
#         print("Connection to MySQL DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#     return connection
# connection = create_connection("RAES034", "soporte", "1234")

##.............................FUNCIONA OK.............
# import pypyodbc as odbc
# import pandas as pd
# DRIVER_NAME="ODBC Driver 17 for SQL Server"    # utilizar cualquier driver de la lista    ODBC Driver 17 for SQL Server  or   SQL SERVER
# SERVER_NAME="RAES034"
# DATABASE_NAME="AdventureWorks2019"
# USER_NAME='soporte'
# PASSWORD='1234'
# connection_string = f"""
#      DRIVER={{{DRIVER_NAME}}};
#      SERVER={SERVER_NAME};
#      DATABASE={DATABASE_NAME};
#      Trust_Connection=yes;
#      UID={USER_NAME};
#      PWD={PASSWORD};
# """
# try:
#     conexion=odbc.connect(connection_string)
#     print('conexion exitosa al servidor')
# except :
#     print('error al intentar conectar')
#
# SQL_QUERY = """
# SELECT TOP (10) [BusinessEntityID]
#       ,[EmailAddressID]
#       ,[EmailAddress]
#       ,[rowguid]
#       ,[ModifiedDate]
#   FROM [AdventureWorks2019].[Person].[EmailAddress]
# """
# sql_DataFrame=pd.read_sql_query(SQL_QUERY,conexion) # dataframe extracted from sql query
# cursor = conexion.cursor()   # these 3 lines are to extract a List called containing the result of the query
# cursor.execute(SQL_QUERY)    #
# sql_List = cursor.fetchall()  #
# for r in sql_List:
#     print(r)
# print(sql_DataFrame)
# cursor.close()
# conexion.close()


# ##.......................FUNCIONA OK.......................
# import pyodbc
# import pandas as pd
# driver='{ODBC Driver 17 for SQL Server}'   # utilizar cualquier driver de la lista    ODBC Driver 17 for SQL Server  or   SQL SERVER
# server='RAES034'
# bd='AdventureWorks2019'
# usuario='soporte'
# contrasena='1234'
# try:
#     conexion = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+bd+';Trust_Connection=yes;UID='+usuario+';PWD='+contrasena)
#     print('conexion exitosa')
# except :
#     print('error al intentar')
#
# SQL_QUERY = """
# SELECT TOP (10) [BusinessEntityID]
#       ,[EmailAddressID]
#       ,[EmailAddress]
#       ,[rowguid]
#       ,[ModifiedDate]n
#   FROM [AdventureWorks2019].[Person].[EmailAddress]
# """
# sql_DataFrame=pd.read_sql_query(SQL_QUERY,conexion) # dataframe extracted from sql query
# print(sql_DataFrame)
# # cursor = conexion.cursor()  # these 1-4 lines are to extract a List containing the result of the query
# # cursor.execute(SQL_QUERY)   # these 2-4 lines are to extract a List containing the result of the query
# # cursor.close()              # these 3-4 lines are to extract a List containing the result of the query
# # sql_List=cursor.fetchall()  # these 4-4 lines are to extract a List containing the result of the query
# # for j in sql_List:
# #     print(j)
#
# conexion.close()



####.......................SQL TEST ALBERTO.......................................................
import pyodbc
import pandas as pd
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
# SQL_WRITE="""
# INSERT INTO [AdventureWorks2019].[dbo].[tabla_pruebas] (
#     nombre,
#     codigo,
#     departamento
# )
# VALUES
#     (
#         'GOKU',
#         74,
#         'AUDITORIA'
#     );
# """
column1='nombre'
column2='codigo'
column3='departamento'
value1='hyag'
value2='37'
value3='disputas'
table_name='dbo].[tabla_pruebas'
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
cursor = conexion.cursor()  # these 1-4 lines are to extract a List containing the result of the query
cursor.execute(SQL_WRITE)   # these 2-4 lines are to extract a List containing the result of the query
cursor.commit()
cursor.close()

SQL_QUERY = """
SELECT TOP (100) [nombre]
      ,[codigo]
      ,[departamento]
  FROM [AdventureWorks2019].[dbo].[tabla_pruebas]
"""
sql_DataFrame=pd.read_sql_query(SQL_QUERY,conexion) # dataframe extracted from sql query
print(sql_DataFrame)

conexion.close()


