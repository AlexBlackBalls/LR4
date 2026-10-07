# Задача 3. Существует ли треугольник и какого он вида.

a = float(input())
b = float(input())
c = float(input())

# Сумма любых двух сторон должна быть больше третьей
if a + b > c and a + c > b and b + c > a:
    print("Да")
    if a == b and b == c:
        print("Равносторонний")
    elif a == b or a == c or b == c:
        print("Равнобедренный")
    else:
        print("Разносторонний")
else:
    print("Нет")
