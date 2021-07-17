import pandas as pd

dataframe = pd.read_excel ('75 Material_Type 03.xlsx',header=2)
component_list = dataframe['Component'].tolist()
print(dataframe)
print(component_list)

for i in component_list:
    print(i)

def check_word_upgrade(words,component_list):
    for i in range(len(words)):
        for j in range(len(component_list)):
            if words[i] is component_list[j]:
                print(words[i]," == ",component_list[j])
            else:
                pass
    return

def check_word(words):
    for i in range(len(words)):
        if words[i] == "BEARING":
            return "BEARING"
        else:
            pass