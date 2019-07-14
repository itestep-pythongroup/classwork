# example 1
# Попробуйте, используя итерацию
# сделать матрицу 5x5 заполнив её нулями.


y=[]
for i in range(0,5):
    z = []
    for i in range(0,5):
        z.append(i)
    y.append(z)
for i in y:
    print(i)


# example 1.1
x="0,0,0,0,0"
y=[]
for i in x:
    y.append(i)
print("[",x)
print(" ",x)
print(" ",x)
print(" ",x)
print(" ",x,"]")

# Numpy вопрос!
