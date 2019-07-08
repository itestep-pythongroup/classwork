# # №1
# # <ol> - исчислимый список
# # <ul> - не исчислимый список
# #1
# def ul(item1, item2, item3):
#     wrapped = "<ul>" + item1 + item2 + item3 + "</ul>"
#     return wrapped
#
# def li(item):
#     wrapped = "<li>" + item + "</li>"
#     return wrapped
#
# print(
#     ul(li("a"),
#        li("b"),
#        ul(li("b1"),
#           li("b2"),
#           li("b3"))))
#
# #2
# def ol(item1, item2, item3):
#     wrapped = "<ol>" + item1 + item2 + item3 + "</ol>"
#     return wrapped
#
# def p(item):
#     wrapped = "<p>" + item + "</p>"
#     return wrapped
#
# print(
#     ol(p("a"),
#        p("b"),
#        ol(p("b1"),
#           p("b2"),
#           p("b3"))))
#
# #3
# def ol(item1, item2, item3):
#     wrapped = "<ol>" + item1 + item2 + item3 + "</ol>"
#     return wrapped
#
#
# def h1(item):
#     wrapped = "<h1>" + item + "</h1>"
#     return wrapped
#
# print(
#     ol(h1("a"),
#        h1("b"),
#        ol(h1("b1"),
#           h1("b2"),
#           h1("b3"))))
#
# #4
# def ol(item1, item2, item3):
#     wrapped = "<ol>" + item1 + item2 + item3 + "</ol>"
#     return wrapped
#
# def li(item):
#     wrapped = "<li>" + item + "</li>"
#     return wrapped
#
# def h1(item):
#     wrapped = "<h1>" + item + "</h1>"
#     return wrapped
#
# def p(item):
#     wrapped = "<p>" + item + "</p>"
#     return wrapped
#
# print(
#     ol(li(h1("Ютуб видео.")),
#        li(p("Инструкция")),
#        li("https://support.google.com/youtube/answer/171780?hl=ru")))
#
# #№2 факториал 5!
# def f(x):
#    y=1
#    while x>1:
#        y*=x
#        x-=1
#    return y
#
# print (f(5))
#
# #№3 вывести четные/не четные числа
# x=1
# y=2
# print ("не четные числа:")
# while x<=1000:
#   print(x)
#   x=x+2
# print ("четные числа:")
# while y<=1000:
#   print (y)
#   y=y+2
#
# # №3 вывести четные/не четные числа
# x = 0
# y = 0
# z = 0
# print("числа делимые на 7:")
# while x <= 1000:
#     print(x)
#     x = x + 7
# print("числа делимые на 11:")
# while y <= 1000:
#     print(y)
#     y = y + 11
# print("числа делимые на 13:")
# while z <= 1000:
#     print(z)
#     z = z + 13

for i in range(1,100):
    x=i%11

x=10
y=10
while x>0
    y=y-1

    
# факториал
def fact(x):
    if x==0:
        return 1
    return fact(x-1)*x

print(fact(5))

def fact(x):
    if x==0:
        return 1
    y=x
    return fact(y-1)*y

print(fact(5))