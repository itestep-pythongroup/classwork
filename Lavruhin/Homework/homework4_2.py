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
#разобраться
#def fact(n):
#    n = 5
#    while n > 1:
#    fact (n-1) * n
#
#print(fact(n))