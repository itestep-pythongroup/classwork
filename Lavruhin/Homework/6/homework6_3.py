# Используя `xor` оператор сделайте программу,
# котора на вход принимает сначала
# текст а потом пароль и возвращает
# назад зашифрованный текст в виде массива чисел.
# Для этого вам нужно использовать `hash` и `ord`
# функцию и проитерировать каждый символ строки.

print("example 1")
login = 1 ^ 40
print(login ^ 1)
psw = 2 ^ 1980
print(psw ^ 2)

# print(ord("t"))

# print("example 2")
# coded = ord("я") ^ 111
# print(coded)
# print(chr(coded ^ 111))