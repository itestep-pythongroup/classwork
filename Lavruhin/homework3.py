print("1 part")
def f1(x,y):
    if x>0 and y>0:
        print("I")
    elif x<0 and y>0:
        print("II")
    elif x<0 and y<0:
        print("III")
    elif x>0 and y<0:
        print("IV")
    else:
        print("undefined")
f1(1,3)

print("3 part")
def f3(x,y):
    z=x+y
    print(z)
f3(3,4)
f3(5,6)

print("2 part")
def f2