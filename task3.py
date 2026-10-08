a = float(input())
b = float(input())
c = float(input())

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
