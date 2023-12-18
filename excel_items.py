import pandas as pd
import os

Routing_total0 = {'Resource': ['na'], 'Description Activities': ['na'],'Time (Hr)': ['na'],'Item-Version': ['na'],'Status': ['na'],'Project': ['na'],'Description': ['na']}
Routing_total = pd.DataFrame(data=Routing_total0)

item_list=pd.read_excel(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\PowerBi dashboard\Item for routing\item list.xlsx')
item_list=item_list[['Item-Version','Status','Project','Description']]
item_list=item_list.drop_duplicates(subset='Item-Version',ignore_index=True)


Path_Routing=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\PowerBi dashboard\Routings'
Files_Routing=os.listdir(Path_Routing)

idx=0
for k1 in Files_Routing:
    file_name = f"{Path_Routing}\{k1}"
    tabla_rout = pd.read_excel(file_name)
    tabla_rout=tabla_rout[['Resource','Description Activities','Time (Hr)']]
    tabla_rout['Item-Version']=item_list['Item-Version'][idx]
    tabla_rout['Status'] = item_list['Status'][idx]
    tabla_rout['Project'] = item_list['Project'][idx]
    tabla_rout['Description'] = item_list['Description'][idx]
    Routing_total = pd.concat([Routing_total, tabla_rout], ignore_index=False, sort=False)
    idx=idx+1

print('esta es la tabla total \n',Routing_total[['Item-Version','Resource','Description Activities']])
Routing_total.to_csv('Routing_final',index=False)

print(Files_Routing)