# example 1
# Попробуйте, получив на вход список с разными
# типами данных, например
# [[],12,"asd",True,int,13]
# сохранить список только с числами: [12,13],
# только со строками ["asd"]
x=[[],12,"asd",True,int,13]
y=[]
z=[]
for i in x:
    if type(i)==int:
        y.append(i)
    elif type(i)==str:
        z.append(i)
print(y)
print(z)