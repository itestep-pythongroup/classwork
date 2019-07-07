print('**FIRST TASK**')
def _ul(a,b,c):
    return ('<ul>\n'+a+b+c+"</ul>\n")

def _li(x):
    return ('<li>'+x+"</li>\n")

def h1(y):
    return ('<h1>'+y+"</h1>\n")
def p(y):
    return ('<p>'+y+"</p>\n")

print(_ul(_li(h1('how to code')),
         _li(p('Lorem ipsum dolor sit amet, consectetur adipiscing elite')),
         _li('https://youtu.be/X4rU02088Xc')))


print('**SECOND TASK**')
x = 1
y = 1
while y < 5:
    y += 1
    x = x * y

print('finished', x)

print('**THIRD TASK**')
x=1

while x<100:
    x+=1
    if x%2==0:
     print(x)
# далее вместо двойки можем подствлять любіе числа 7,13,11 и т.д

print('**TASK FOURth**')
def primeNum(a):
    b=1
    while b<a:
        b+=1
        if a%b==0:
