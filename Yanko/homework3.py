# №1
# <ol> - исчислимый список
# <ul> - не исчислимый список

def ul(item1, item2, item3):
    wrapped = "<ul>" + item1 + item2 + item3 + "</ul>"
    return wrapped

def li(item):
    wrapped = "<li>" + item + "</li>"
    return wrapped

print(
    ul(li("a"),
       li("b"),
       ul(li("b1"),
          li("b2"),
          li("b3"))))

def ol(item1, item2, item3):
    wrapped = "<ol>" + item1 + item2 + item3 + "</ol>"
    return wrapped

def li(item):
    wrapped = "<li>" + item + "</li>"
    return wrapped

print(
    ol(li("a"),
       li("b"),
       ol(li("b1"),
          li("b2"),
          li("b3"))))