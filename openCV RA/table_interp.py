# THIS CODE IS FOR FINDING THE CLOSEST MATCH VALUE IN A TABLE OF LASER ANGLES

import pandas as pd

# Specify the path to your Excel file
excel_file_path = r'C:\Users\jplop\Documents\PythonScripts\table_test.xlsx'

# Load the Excel file into a DataFrame, specifying sheet name and header row
df = pd.read_excel(excel_file_path, sheet_name='Sheet1', header=0)

# Display the DataFrame
print(df)

# this loop is for filling the gaps in the original table
N_points=df.shape[0]   # number of rows of the table
angles=[]
distance=[]
for i in range(0,N_points):
   if i<N_points-1:
        a1=df.iloc[i,0]
        a2=df.iloc[i+1,0]
        a_int=a1+(a2-a1)/2
        angles.append(a1)
        angles.append(a_int)
        d1=df.iloc[i,1]
        d2=df.iloc[i+1,1]
        d_int=d1+(a_int-a1)/(a2-a1)* (d2-d1) # interpolation formula
        distance.append(d1)
        distance.append(d_int)
   else:
        angles.append(df.iloc[i,0])
        distance.append(df.iloc[i,1])

new_df1 = pd.DataFrame({'Angles': angles, 'Distance': distance,'Laser':1}) # this is the result expanded table

# this extra tables are for simulating the tables of other lasers
new_df2 = pd.DataFrame({'Angles': angles, 'Distance': distance,'Laser':2})
new_df2['Distance']= new_df2['Distance']*1.23
new_df3 = pd.DataFrame({'Angles': angles, 'Distance': distance,'Laser':3})
new_df3['Distance']= new_df3['Distance']*1.35
new_df4 = pd.DataFrame({'Angles': angles, 'Distance': distance,'Laser':4})
new_df4['Distance']= new_df4['Distance']*1.48

#..............Join the tables into a single one
new_df=pd.concat([new_df1, new_df2, new_df3, new_df4])
new_df = new_df.reset_index(drop=True)
print(new_df)


# Value to find the closest match for
value_to_lookup = 7710

# Find the index of the row with the closest match in column 'Value_A'
closest_index = (new_df['Distance'] - value_to_lookup).abs().idxmin()

# Retrieve the corresponding value in column 'Value_B'
corresponding_value = new_df.at[closest_index, 'Angles']
corresponding_laser = new_df.at[closest_index, 'Laser']

print(f"Value to lookup: {value_to_lookup}")
print(f"Closest match in column 'Distance': {new_df.at[closest_index, 'Distance']}")
print(f"Corresponding value in column 'Angles': {corresponding_value}")
print(f"Laser number: {corresponding_laser}")

# to remove from the table the laser that is already used
new_df = new_df[new_df['Laser'] != corresponding_laser]
