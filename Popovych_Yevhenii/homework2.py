def f(x,y):
    if x > 0 and y > 0:
        print('I')
    if x < 0 and y > 0:
        print('II')
    if x < 0 and y < 0:
        print('III')
    if x > 0 and y < 0:
        print('IV')
    if x == 0 or y == 0:
        print('undefined')


f(0,1)