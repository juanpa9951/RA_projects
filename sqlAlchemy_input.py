from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import warnings
warnings.filterwarnings("ignore")



# Define the connection string
server='RAES034'
bd='AdventureWorks2019'
usuario='soporte'
contrasena='1234'
connection_string = f'mssql+pyodbc://{usuario}:{contrasena}@{server}/{bd}?driver=ODBC+Driver+17+for+SQL+Server'

# Create the SQLAlchemy engine
engine = create_engine(connection_string)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define the table structure from SQL, el nombre puede ser cualquier cosa, yo le puse Register
class Register(Base):   # estructura de tabla de sql
    __tablename__ = 'attendance2'
    Person_ID = Column(Integer)
    First_Name = Column(String)
    Last_Name = Column(String)
    Date_Time = Column(String,primary_key=True)
    Last_State = Column(String)

# Create the tables in the database
Base.metadata.create_all(engine)

# Define the inputs to the table
Person_ID='10064'
First_Name='Samuel'
Last_Name='Garcia'
Date_Time=datetime.datetime.now()
Last_State='INGRESO'   # O SALIDA

# Save the inputs in an instance of Register
new_register = Register(Person_ID=Person_ID,First_Name=First_Name,Last_Name=Last_Name, Date_Time=Date_Time, Last_State=Last_State)

# send changes to the database
session.add(new_register)
session.commit()
