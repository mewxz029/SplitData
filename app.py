import pandas as pd
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
            if material_des_split[j] == component_list[h]: 
                k+=1               
                x = material_des_split[j]
                dict_material.update({
                    i : {
                        "Component" : x,
                        "Brand" : None
                    }
                })


print(dict_material)
print(k)
