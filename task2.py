import math

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("Бесконечно много корней")
        else:
            print("Корней нет")
    else:
        x = -c / b
        print(x)
else:
    d = (b ** 2) - 4 * a * c    
    if d < 0:
        print("Корней нет")
    elif d == 0:
        x = -b / (2 * a)
        print(x)
    else:
        sqd = math.sqrt(d)
        x1 = (-b + sqd) / (2 * a)
        x2 = (-b - sqd) / (2 * a)
        print(x1, x2)
