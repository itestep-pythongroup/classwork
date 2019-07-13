#example1
def ol(item1, item2, item3):
    x = "<ol>" + item1 + item2 + item3 + "</ol>"
    return x

def p(item):
    x = "<p>" + item + "</p>"
    return x

print(
    ol(p("a"),
       p("b"),
       ol(p("b1"),
          p("b2"),
          p("b3"))))

#example2
def ol(item1, item2, item3):
    x = "<ol>" + item1 + item2 + item3 + "</ol>"
    return x


def li(item):
    x = "<li>" + item + "</li>"
    return x

def h1(item):
    x = "<h1>" + item + "</h1>"
    return x

def p(item):
    x = "<p>" + item + "</p>"
    return x


print(
    ol(li(h1("youtube")),
       li(p("instruction")),
       li("https://support.google.com/youtube/answer/171780?hl=ru")))
