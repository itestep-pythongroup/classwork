# def ul(item1, item2, item3):
#     wrapped = "<ol>" + item1 + item2 + item3 + "</ol>"
#     return wrapped
#
#
# def li(item):
#     wrapped = "<li>" + item + "</li>"
#     return wrapped
#
#
# print(
#     ul(li("a"),
#        li("b"),
#        ul(li("<h1>Lesson of Python</h1>"),
#           li("<p>This is first step in education</p>"),
#           li("https://www.youtube.com/watch?v=cKRRysbQZsM"))))

x = 0
y = 1
while x < 5 :
    x = x + 1
    y = y * x
print("finished: ", y)