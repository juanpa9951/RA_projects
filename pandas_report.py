import pandas as pd

# DATOS DE CAMPO
file_path=r"C:\Users\jplop\Documents\PythonScripts\file2.csv"
column_names = ['Datetime', 'STACK FULL', 'SIDE','ITEM FULL']
df=pd.read_csv(file_path,names=column_names)
df = df[df['STACK FULL'] != 'STACK: ']
df = df[df['STACK FULL'] != 'STACK: test']
df = df[df['STACK FULL'] != 'STACK: TEST']

#df = df.dropna(subset=['B'])
print(df)
df_sorted = df.sort_values(by='Datetime', ascending=False)
df_sorted[['Date', 'Time']] = df_sorted['Datetime'].str.split(' ', expand=True)
print(df_sorted)
df_sorted[['non1', 'STACK']] = df_sorted['STACK FULL'].str.split(':', expand=True)
df_sorted[['non2', 'ITEM']] = df_sorted['ITEM FULL'].str.split(':', expand=True)
del df_sorted['non1']
del df_sorted['non2']
del df_sorted['STACK FULL']
del df_sorted['ITEM FULL']
# df_sorted['Time'] = pd.to_timedelta(df_sorted['Time'])
# df_sorted['Time Diff'] = df_sorted['Time'] - df_sorted['Time'].shift(-1)
df_sorted['Datetime'] = pd.to_datetime(df_sorted['Datetime'])
df_sorted['Time Diff'] = df_sorted['Datetime'] - df_sorted['Datetime'].shift(-1)
df_sorted['ID'] = df_sorted['STACK'] + '-' + df_sorted['ITEM']
print(df_sorted)

# DATOS DEL TR
file_path2=r"C:\Users\jplop\Documents\PythonScripts\file3.csv"
column_names2 = ['ID','POS','TOTAL POS']
df2=pd.read_csv(file_path2,names=column_names2)
df2['POS']=pd.to_numeric(df2['POS'])
df2['TOTAL POS']=pd.to_numeric(df2['TOTAL POS'])
df2['PROGRESS']=df2['POS']/df2['TOTAL POS']
df2['MISSING']=df2['TOTAL POS']-df2['POS']
df2['PROGRESS %'] = df2['PROGRESS'].apply(lambda x: f"{x * 100:.2f}%")
print(df2)

# COMBINAR CONSULTAS
df_sorted['ID'] = df_sorted['ID'].str.strip()
df2['ID'] = df2['ID'].str.strip()
result = pd.merge(df_sorted,df2, on='ID', how='outer')
print(result)