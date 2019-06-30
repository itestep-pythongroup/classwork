x = int(input())

for case in (x):
    if case(1): pass
    if case(2): pass
    if case(3):
        print('Число от 1 до 3')
        break
    if case(4):
        print('Число 4')
    if case(): # default
        print('Другое число')