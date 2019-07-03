# def m4():
#     x=1
#     return x + 3
#
# def m5(name,x):
#     print(name,"=",x)
#
# print("m4=",m4, m4())

# def a(b):
#     print(b)
# x=3
# a(x)

# def ul(item1,item2,item3):
#     pass
# def li(item):
#     pass

def ul(item1,item2,item3):
    return ("<ul=>"+item1+item2+item3+"</ul>")
print (ul("M","oo","se"))

def li(item):
    wrapped = "<li>" + item + "</li>"
    return wrapped
print(
    ul(li("a"),
       li("b"),
       ul(li("b1"),
          li("b2"),
          li("b3"))))