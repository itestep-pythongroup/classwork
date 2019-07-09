print('**FIRST TASK**')

y=[]
x='123456789'

for i in x:
    y.append(i)
list.reverse(y)
print(y)


print('**SECOND TASK**')

y = []
x = []
z = '00000'
for i in z:
    y.append(i)

    x.append(y)

print(x)

print('**THIRD  TASK**')

y=[12,"asd",True,int,13]
x=[]
z=[]
for i in y:
    if type(i)==int:
        x.append(i)
    elif type(i)==str:
        z.append(i)
print(x)
print(z)

print('**FOURTH  TASK**')
y = ["1", "if", "2", "3", "blab", "false", "345.12"]
x = []
z = []

for i in y:
    try:
        x.append(float(i))
    except:
        z.append(i)

print(x)
print(z)

print('**FIVE  TASK**')
x = [1, 3, 4, 5]
y = 0
for i in x:
    y += i

print(y)

print('**SIX TASK**')
x = [1, 2, 3, 4, 5, 6]
y = 0
z = []
for i in x:
    y += i
    z.append(y)

print(z)