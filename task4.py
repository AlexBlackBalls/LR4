x = float(input())
y = float(input())

circle = x * x + y * y <= 1
triangle = x <= 0 and y <= 0 and x + y >= -2

if circle or triangle:
    print("Да")
else:
    print("Нет")
