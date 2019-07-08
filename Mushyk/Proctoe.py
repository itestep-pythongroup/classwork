import math

n = int(input("Ведите число для проверки на простоту:",))

if n < 2:
    print("Число должно иметь значение 2 и более")
    quit()
elif n == 2:
    print("Это простое число")
    quit()

i = 2
limit = int(math.sqrt(n))

while i <= limit:
    if n % i == 0:
        print("Число не является простым")
        quit()
    i += 1

print("Это простое число")