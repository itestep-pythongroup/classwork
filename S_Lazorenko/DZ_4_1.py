def ol(item1, item2, item3):
    wrapped = "<ol>" + item1 + item2 + item3 + "</ol>"
    return wrapped


def p(item):
    wrapped = "<p>" + item + "</p>"
    return wrapped


print(ol(p("Пентагон раскрыл секрет подлодки, на которой сгорели 14 моряков / ВОТ ТАК за 3 июля"),
         p(
             "Главные события среды, 3 июля, по версии редакции информационных программ Белсата Пентагон рассказал о судне, на котором сгорели 14 моряков"),
         p(
             '''<iframe width="1280" height="720" src='https://www.youtube.com/embed/oR_Jof9dfnU' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''))
      )
