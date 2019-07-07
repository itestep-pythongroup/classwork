#version 1
x = 2
print("четные числа: ")
while x <= 100:
    print(x)
    x = x + 2

#version 2
x=1
while x<=10:
    if x%2==0:
        print(x)
    x+=1

x = 0
print("числа делимые на 7:")
while x <= 100:
    print(x)
    x = x + 7
x = 0
print("числа делимые на 11:")
while x <= 100:
    print(x)
    x = x + 11
x = 0
print("числа делимые на 13:")
while x <= 100:
    print(x)
    x = x + 13