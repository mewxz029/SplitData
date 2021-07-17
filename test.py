import pandas as pd
import csv

dataframe = pd.read_excel ('75 Material_Type 03.xlsx', sheet_name='75 Material_Type 03')
material_des = dataframe['Material_Description'].tolist()

x = ['A','B','C','D','A']
y = ['AAA','C','D','BBB']

def compare(x,y):
    for i in range(len(x)):
        for j in range(len(y)):
            print(i,j)
            print(x[i]," compare with ",y[j])
            if x[i] is y[j]:                
                return x[i]

material_des_collection = []
#print("return",compare(x,y))
for i in range(len(material_des)):
    material_des_split = material_des[i].split(sep=",")
    for j in range(len(material_des_split)):
        material_des_collection.append(material_des_split[j])

# Remove Duplicate Words => list to set
material_des_set = set(material_des_collection)
#print(material_des_set)

# Covert no duplicate words set to list
material_des_set_to_list = list(material_des_set)

print(material_des_collection.count("BREAKER"))
print(len(material_des_collection))
print(len(material_des_set_to_list))

dict_material = {}
dict_csv = []
for i in range(len(material_des_set_to_list)):
    count = material_des_collection.count(material_des_set_to_list[i])
    dict_material.update({
        i:{
            "No" : i+1, 
            "Name" : material_des_set_to_list[i],
            "Count" : count
        }
    })
       
#print(dict_material)
for i in dict_material:
    dict_csv.append(dict_material[i])

print(dict_csv)


"""csv_columns = ['No','Name','Count']
csv_file = "CountNames.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_csv:
            writer.writerow(data)
except IOError:
    print("I/O error")"""