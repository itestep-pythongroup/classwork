# 1
# def m4():
#     return 4
#
# print(m4,m4())

#2
# def m4():
#     return 4
#
# print("m4 =",m4,",m4() =",m4())

#3
# def m4():
#     x=1
#     return x+3
#
# print("m4 =",m4,",m4() =",m4())

#4
# def a(b):
#     print(b)
#
# x=3
# a(x)

#5
# x=3
# def a():
#     print(x)
# a()

#6
# def a():
#     print(x)
# x = 3
# a()

# #7
# def m4():
#     x=1
#     return x+3
#
# def m5(name,x):
#     a=x()
#     print(name,"=",a)
#
# m5("m4",m4)
# # name = "m4"
# # a=x() - отображает состояние функции в данный момент


# разбор домашки:

# def ul(item1,item2,item3):
#     return ("<ul>"+item1+item2+item3+"</ul>")
# print (ul("Hello " ,"World" ,"!"))
#
# def li(item):
#     return("<li>"+item+"</li>")
# print (li("World"))


# pass - пропуск
# HTML теги для разметки страницы:
# 1) ul - список HTML
# 2) li -

# def ul(item1,item2,item3):
#     wrapped = "<ul>" + item1 + item2 + item3 + "</ul>"
#     return (wrapped)
#
# def li(item):
#     wrapped =("<li>" + item + "</li>")
#     return wrapped
#
# print (li("World"))

# Генерация списка

# def ul(item1,item2,item3):
#     wrapped = "<ul>" + item1 + item2 + item3 + "</ul>"
#     return (wrapped)
#
# def li(item):
#     wrapped =("<li>" + item + "</li>")
#     return wrapped
#
# print (
#     ul(li("a"),
#        li("b"),
#        ul(li("b1"),
#           li("b2"),
#           li("b3"))))

# def ul(item1,item2,item3):
#     wrapped = "<ul>" + item1 + item2 + item3 + "</ul>"
#     return (wrapped)
#
# def li(item):
#     wrapped =("<li>" + item + "</li>")
#     return wrapped
#
# def b(item):
#     wrapped =("<b>" + item + "</b>")
#     return wrapped
#
# print (
#     ul(li("a"),
#        li(b("b")),
#        ul(li("b1"),
#           li("b2"),
#           li("b3"))))

# Итерация

# x=0
# while True:
#     x=x+1
#     print(x)

x = 0
while x<3:
    x = x+1
    print("finished",x)
