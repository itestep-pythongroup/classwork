# example 1
# Попробуйте посчитать сумму всех элементов списка,
# зная что там есть только числа.
# [1,3,4,5] #=> 13
def sum(x):
    y=0
    for i in x:
        y=y+i
    return y
print(sum([1,2,3,4,5]))

# example 1.1
x=[1,2,3,4,5]
y=0
for i in x:
    y+=i
print(y)

# example 1.2
# рекурсия
def s(x):
   if len(x)==1:
        return x[0]
   else:
        return x[0] + s(x[1:])
print(s([1,2,3,4,5]))

