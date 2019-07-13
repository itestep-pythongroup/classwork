# сырые строки, юникод кодирование декодирование

def hello():
    print("Hello\z \U0001f600")
    print("Hello \\U0001f600")
    print(r"Hello \n\n\n\n\n\n")
    print(chr(ord("\U0001f600")))
    print(ord("a"))
    print("xvxc ы вv".encode("utf8").decode("ascii", "replace"))
    print("xvxc ы вv".encode("utf8").decode("ascii", "ignore"))
    print("xvxc ы вv".encode("utf8").decode("ascii", "strict"))
    print(u"xvxc ы вv")


hello()

# Изменяемость списков

a = [1, 2, 3, 4, 5, 6]
a[0] = "b"
a[1] = "c"

print(a)  # => ['b', 'c', 3, 4, 5, 6]
b = a.append("b")

# Неизменяемость строк

x = "adasd"
x[0] = "z"
print(x)

y = x.capitalize()

print(y)
print(y == x)

n = x + "ZZZZ"
print(n)
print(x)

# методы, доступ по индексу и итерация строк

print("привет".capitalize())
print("\n".join(["1", "2", "3"]))
x = "привети"
print(x.capitalize())
print(x.startswith("приве"))
print(x.startswith("прив4"))
print(x.find("и"))
print(x.isascii())
print("asdsчd".isascii())
print("asdsчd".encode("cp1251"))

print(x[0])
print(x[1])
print(x[2])
print(x[0:4])

for i in x:
    print(i)

# Форматирование строк
print("Привет %s%s" % ("мир", "!"))
print("Привет {0} {1}!".format("мир", 124))

print("{0}____({1})*[{2}]={3}".format("Мясо", 12, 7, 12 * 7))
x = [[1, 2, 3], [1, 2, 3]]

# регулярные выражения
import re

regex = re.compile("[A-z]+@[A-z]+\.com")
print(bool(regex.match("adlkasjdj")))
print(bool(regex.match("asdasda@sdad.com")))

## Mustache templating engine(https://mustache.github.io/)

"""
{{#.}}
  {{#.}}{{.}}{{/.}}\n
{{/.}}
"""

# Хеши и пароли

print(12312414124 % 13)  # => 10
print(10 % 13)  # => 10

print(hash(b"kljkljj"))

input("создайте пароль")
input("введите пароль")

# uuid
import uuid

print(uuid.uuid4())
print(134 + 125)

# переменные тексом

переменная_а = "asdad"
print(переменная_а)

# xor

x = 134 ^ 12587834398735
print(x ^ 134)
print(ord("я"))

print(ord("я"))
coded = ord("я") ^ 1234
print(coded)
print(chr(coded ^ 1234))

# доп.задание

x=input("create psw\n")
    if x == :
    elif:
y=input("enter psw")

print(hash())