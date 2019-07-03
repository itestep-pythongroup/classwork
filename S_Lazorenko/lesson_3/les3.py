# def step(x):
#     return x**2
#     print(x)
# x=6
# print(step(x))

# print (type(9.9)==int)
# print (type(12)==str)
# print (type("x"))

# def tip(x):
#     print(x)
#     if type(x)==(int):
#         print("int")
#     elif type(x)==(str):
#         print("str")
#     elif type(x) == (float):
#         print("float")
# tip("c")

# def preoobrazovanie(a,b):
#     x=('a'+'b')
#     print(preoobrazovanie())
#
# def ul(item1, item2, item3):
#      return "<ul>"+ item2+item2+item3+"<ul>"
#
# def li(item):
#       return "<li>" + item + "</li>"
# print (ul(li("a"),
#        li("привет"),
#        ul(li("пока"),
#           li("до завтра"),
#           li("до послезавтра"))))
# послезавтра
# x=0
# while True:
#    if x == 3:
#        break
#    x=x+1
# print("finished: ",x)

x = 0
while x < 7:
    if x == 4:
        x = x + 1
        continue
    x = x + 2

print("finished: ", x)
