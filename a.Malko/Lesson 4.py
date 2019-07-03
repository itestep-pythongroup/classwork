def m4():
    x=1
    return x+3
    print(m4, m4())


def m5(name,x):
    print(name,"=",x())
m5("m4",m4)


