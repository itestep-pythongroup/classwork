# пример 1
def m4():
    x=1
    return x + 3

def m5(name,x):
    a=x()
    print(name,"=",a)

m5("m4",m4)

# homework 3 view
def ul(item1,item2,item3):
    x = "<ul>" + item1 + item2 + item3 + "</ul>"
    return x

def li(item):
    x = "<li>" + item + "</li>"
    return x

print(
    ul(li("Homework TODO"),
       li("First task"),
       ul(li("Second task"),
          li("Third task"),
          li("Groceries TODO"))))
# пример 2
x = 0
while True:
    if x==3:
        break
    x=x+1
print("end:",x)
# пример 3
x = 0
while x < 7:
    if x == 4:
        x = x + 1
        continue
    x = x + 2

print("finished: ", x)