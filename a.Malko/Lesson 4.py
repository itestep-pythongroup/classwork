# def m4():
#     x=1
#     return x+3
#     print(m4, m4())
#
#
# def m5(name,x):
#     print(name,"=",x())
# m5("m4",m4)

def ul(item1,item2,item3):
    return "<ul>\n"+li(item1) + "\n" + li(item2)+li(item3)+"</ul>"
# print(ul("its1","its2","its3"))


def li(item):
    return "<li>"+item+"</li>"
# print(li("item"))
# print(ul(li("Homework"),ul(li("first"),li("second\n"),li("third\n")),li("final")))
print(ul('1','2','3'))