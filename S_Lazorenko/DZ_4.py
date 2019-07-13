def ol(item1, item2, item3):
    wrapped = "<ol>" + item1 + item2 + item3 + "</ol>"
    return wrapped


def p(item):
    wrapped = "<p>" + item + "</p>"
    return wrapped


print(
    ol(p("сам привет"),
       p("сама привет"),
       p("все с приветом"))
       )
