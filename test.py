x = ['A','B','C','D']
y = ['AAA','C','D','BBB']

def compare(x,y):
    for i in range(len(x)):
        for j in range(len(y)):
            print(i,j)
            print(x[i]," compare with ",y[j])
            if x[i] is y[j]:                
                return x[i]

print("return",compare(x,y))