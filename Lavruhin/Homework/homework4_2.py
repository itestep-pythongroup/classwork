#Задание факториал 5!
#variant1
def factorial(n):
    x=1
    for i in range (1, n+1):
        x=x*i
    return x
y=5
print(factorial(y))

#variant2
def f(x):
   y=1
   while x>1:
       y*=x
       x-=1
   return y
print (f(5))

#variant3
x = 0
y = 1
while x < 5:
    x = (x + 1)
    y = x * y
print("finished: ", y)

#variant4
def fact(x):
    if x==0:
        return 1
    y=x
    return fact (y-1) * y
print(fact(5))


