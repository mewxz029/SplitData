import pandas as pd

dataframe = pd.read_excel ('75 Material_Type 03.xlsx',header=2)
component_list = dataframe['Component'].tolist()
"""print(dataframe)
print(component_list)

for i in component_list:
    print(i)"""

def ifcheck(x,y):
    if(x == y):
        return x

def check_word_upgrade(x,y,_dict,count):
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] is y[j]:                
                _dict.update({count : {"Component" : x[i]}})
    return _dict

def check_word(words):
    for i in range(len(words)):
        if words[i] == "BEARING":
            return "BEARING"
        else:
            pass

def check_def(x):
    return x+10