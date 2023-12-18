import pyodbc

# Path to your .mdb file
#    r"C:\Users\Juan Pablo Lopez\Downloads\att2000.mdb"

# Connect to the database
conn = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/Juan Pablo Lopez/Downloads/att2000.mdb')

# Create a cursor
cursor = conn.cursor()

# Execute a query
cursor.execute('SELECT * FROM CHECKINOUT')

# Fetch all results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()