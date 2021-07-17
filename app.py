import pandas as pd
from check_word import *

dataframe = pd.read_excel ('75 Material_Type 03.xlsx', sheet_name='75 Material_Type 03')
material_des = dataframe['Material_Description'].tolist()
#print(dataframe['Material_Description'])
#print(material_des[1])

#material_des_split = str(material_des[1]).split(sep=',')
#print(material_des_split)

dict_material = { 
    0:{
        "Component":"POWERSUPPLY",
        "Brand":"YOKOGAWA"
    }
}

for i in range(len(material_des)):
    #print(material_des[i]) #string
    material_des_split = material_des[i].split(sep=',')
    print(material_des_split)
    print(check_word_upgrade(material_des_split,component_list))
    """dict_material.update({
        i : {
            "Component" : check_word_upgrade(material_des_split,component_list)
        }
    })"""

print(component_list)


"""for i in range(len(material_des)):
    material_des_split = str(material_des[i]).split(sep=',')
    print(material_des[i])    
    dict_material.update({
        i : {
            "Component" : check_word(material_des_split[i])
        }
    })"""

#print(dict_material)


"""split = str(dataframe['Material_Description']).split(sep=',')
print(split)"""