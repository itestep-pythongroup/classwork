print("Задача I")
x=[]
x.append(10)
x.append(9)
x.append(8)
x.append(7)
x.append(6)
x.append(5)
x.append(4)
x.append(3)
x.append(2)
x.append(1)
print(x)
for i in x:
    print(i)

print("Задача 2")
x=[]
y=0
for z in range(5):
    x.append([])
    for i in range(5):
        x[z].append(y)
for z in x:
    print(z)

print("Задача 3")
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

print("Задача 4")
y=["1","if","2","3","blab","false","345.12"]
x=[]
z=[]
for i in y:
  try:
    x.append(float(i))
  except:
    z.append(i)
print(x)
print(z)

print("Задача 5")
x=[1,3,4,5]
print (sum(x))

print("Задача 6")
x=[1,2,3,4,5,6]
y=0
z=[]
for i in x:
    y+=i
    z.append(y)
print(z)

