
def quatro(a = int(input('enter number one->')),b = int(input('enter number two->'))):


    if a > 0 and b > 0:
        print('qutro I')
    elif a > 0 and b < 0:
        print('quatro II')
    elif a < 0 and b < 0:
        print('quatro III')
    elif a < 0 and b > 0:
        print('quatro IV')
    elif a==0 or b==0:
        print('undefined')

quatro()

print('*****TASK TWO*****')
def mult_str(x,y):
    x=str(int(x)+int(y))
    print(x)
    print(type(x))
mult_str('2','6')

print('*****TASK ThREE*****')

def _ul(a,b,c):
    return ('<ul>\n'+a+b+c+"</ul>\n")

def _li(x):
    return ('<li>'+x+"</li>\n")

print(_ul(_li('Homework TODO'),
          _ul(_li('first'),
              _li('second')
              ,_li('third')),
          _li('grocery')))

print('end hw')



