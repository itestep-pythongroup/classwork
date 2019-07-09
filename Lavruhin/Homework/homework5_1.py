# example 1
# Попробуйте, используя итерацию сделать список
# [10,9,8,7,6,5,4,3,2,1,0]

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
x.append(0)
print(x)

# example 1.1
x="109876543210"
y=[]
for i in x:
    y.append(i)
print(y)
# проблема с цыфрой 10