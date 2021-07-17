import pandas as pd
import csv
from check_word import *

dataframe = pd.read_excel ('75 Material_Type 03.xlsx', sheet_name='75 Material_Type 03')
material_des = dataframe['Material_Description'].tolist()

dict_material = { 
    0:{
        "Component":"POWERSUPPLY",
        "Brand":"YOKOGAWA"
    }
}
k=0

for i in range(len(material_des)):
    material_des_split = material_des[i].split(sep=',')
    for j in range(len(material_des_split)):
        for h in range(len(component_list)):
            if component_list[h].count(material_des_split[j]) >= 1: 
                k+=1               
                x = component_list[h]
                dict_material.update({
                    i : {
                        "No" : i+1,
                        "Component" : x,
                        "Brand" : None
                    }
                })

dict_csv = []

for i in dict_material:
    dict_csv.append(dict_material[i])

print(dict_csv)
print(k)

"""csv_columns = ['No','Component','Brand']
csv_file = "Check_Material_Component.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_csv:
            writer.writerow(data)
except IOError:
    print("I/O error")"""
