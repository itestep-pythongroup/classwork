# example 1
# Попробуйте, используя исключения сохранить из
# списка строк только те, которые приводятся к типу `float`
# без ошибок. И наоборот, сохраните из списка строк
# только те значения, которые не приводятся. Например:
# ["1","if","2","3","blab","false","345.12"]
# => ["1","2","3","345.12"]
# => ["if","blab","false"]
x=["1", "if", "2", "3", "blab", "false", "345.12"]
y=[]
z=[]
for i in x:
    try:
        y.append(float(i))
    except:
        z.append(i)
print(y)
print(z)