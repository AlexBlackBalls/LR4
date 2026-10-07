# Задача 2. Решение уравнения ax^2 + bx + c = 0.
import math

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    # Уравнение превращается в линейное: bx + c = 0
    if b == 0:
        if c == 0:
            print("Бесконечно много корней")
        else:
            print("Корней нет")
    else:
        x = -c / b
        if x == int(x):      # если число целое, убираем ".0"
            x = int(x)
        print(x)
else:
    d = b * b - 4 * a * c    # дискриминант
    if d < 0:
        print("Корней нет")
    elif d == 0:
        x = -b / (2 * a)
        if x == int(x):
            x = int(x)
        print(x)
    else:
        sq = math.sqrt(d)
        x1 = (-b + sq) / (2 * a)
        x2 = (-b - sq) / (2 * a)
        if x1 == int(x1):
            x1 = int(x1)
        if x2 == int(x2):
            x2 = int(x2)
        print(x1, x2)
