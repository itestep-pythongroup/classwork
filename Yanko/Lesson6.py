# СТРОКИ
# юникод. каждый символ имеет свой код


# def hello():
#     print("Hello \U0001f600") # U0001f600 - код символа в юникоде # \ - интерпритатор, экранирование
#     print(r"Hello \U0001f600") # r - сырая строка
#     print("Hello \\U0001f600")  # аналогично сырой строке
#     print(ord("\U0001f600")) # ord - функция которая показывает позицию символа в юникоде (десятичное значение)
#     print(chr(ord("\U0001f600")))  #
#     print(ord("a"))
# hello()
# print("XVXC Ы BV".encode("utf8").decod("ascii")) # кодирование/декодирование строк
# print("XVXC Ы BV".encode("utf8").decod("ascii","replace")) # заменить неизвестный символ
# print("XVXC Ы BV".encode("utf8").decod("ascii","ignore")) # игнорировать неизвестный символ
# print("XVXC Ы BV")


#РЕГУЛЯРКИ

# import re # re - модуль с регулярными выражениями
# regex=re.compile("[A-z]+@[A-z]+\.com")
# print(bool(regex.match("agsdjhf"))) #match - достать почту из списка\что-то с вэб страницы
# print(bool(regex.match("agsdjhfas@gsdge.com")))

# x="привет"
# x.capitalize()

# #Хеши  пароли
# print(12312414124%13)#=>10
# print(10%13)#=>10
# print(hash("ftgjt"))



хешированный_пароль=hash(input("Создайте пароль:"))
ввести_пароль=hash(input("Введите пароль:"))
if хешированный_пароль==ввести_пароль:
    print("Yes")
else:
    print("No")