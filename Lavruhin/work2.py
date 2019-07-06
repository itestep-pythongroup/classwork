# def print_abc(a,b,c):
#     x=a*b*c
#     print(x)
# print_abc(3,4,5)


#def myprint(hello):
#   print("**",hello,"**")
#
#myprint(input("Веди значение:"))


# def name(y):
#     x=y**2
#     return (x)
# print(name(int(input("Z="))))
# print (type("x"))
# print (type(3))
# print (type(3.3))


def f_t(x):
    if type(x)==str:
        print("str")
    elif type(x)==int:
        print("Int")
    else:
        print ("конец")
f_t(list)
#print (f_t(type(x)))

def ab(a,b):

    x = int(str(a)+str(b))
    print(x)
    print(type(x))

ab(2,3)