# def hello():
#     print("|Hello \U0001f600")
#
# hello()

# import re
# regex = re.compile("[A-z]+@[A-z]+\.com") # выд а до з в любом количестве
# print(bool(regex.match("qwer")))
# print(bool(regex.match("qwer@hello.com")))


# x = input ("Vvedite parol")
k= hash(input ("Vvedite parol"))
# y = input ("Povtorite parol")
c= hash(input ("Povtorite parol"))
if k==c:
    print("Yes")
else:
    print ("go")


