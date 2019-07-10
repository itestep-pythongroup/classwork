# def hello():
#     print("|Hello \U0001f600")
#
# hello()

# import re
# regex = re.compile("[A-z]+@[A-z]+\.com") # выд а до з в любом количестве
# print(bool(regex.match("qwer")))
# print(bool(regex.match("qwer@hello.com")))


# придумай_пароль = input ("Vvedite parol")
Зафишырованый_парольx= hash(input ("Vvedite parol"))
# повтори_пароль = input ("Povtorite parol"), hash- шыфрует пароль
Зафишырованый_парольy= hash(input ("Povtorite parol"))
if Зафишырованый_парольx==Зафишырованый_парольy:
    print("Yes")
else:
    print ("go")


