#адрес файовой системы
#python -m http.server - прописать в терминале
#127.0.0.1:8000 - ввести в браузере

#итерация
#[] - список
#x.append - добавить в список
#x=[]
#x.append("a")
#x.append("b")
#x.append("c")
#x.append("4")
#print(x)
#
#for i in x:
# # i - каждый элемент сиска, переменная
# #for i in x[0:2]: - срезать список
# #x[0:2] - срезать список
#     print(i)
# #достать из списка
#print(x[0])
#print(x[1])
#print(x[2])
#print(x[3])


# x=[]
# x.append("a")
# x.append("b")
# x.append("c")
# x.append("d")
# x.append("e")
# x.append("f")
# x.append("g")
# x.append("h")
# print(x)
# for i in x:
#     print(i)

# x="abcdfgh"
# y=[]
# print(x)
# for i in x:
#     y.append(i)
#     print(i)
# print(y)

# #виды ошибок
# 1/0
# p==True #ошибка наименования
# int("aaa") #ошибка приведения к типу
# int([]) #ошибка строки

# def a(): #ошибка отступов
# x=1

# def a(x,y,z):
#     if x==3:
#         if y==5:
#             if z==6:
#                 int([])
#
# a(3,5,6)

# #try - перехватывает ошибки
#
# def a(x,y,z):
#     if x==3:
#         if y==5:
#             if z==6:
#                 int([])
#
# try:
#     a(3,5,6)
# except:
#     print("error")
# finally: #используется для закрытия файла/соединений
#     print ("исполнится всегда")


#try:
#    x=int(input("Enter number->"))
#   print(x)
#except:
#    print("error")
#x.