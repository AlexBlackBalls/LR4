# Задача 1. Максимальное и минимальное из трёх чисел.

# Читаем три значения как текст (так мы сможем вывести их в том же виде, как их ввели)
a_text = input()
b_text = input()
c_text = input()

# Для сравнения превращаем текст в числа
a = float(a_text)
b = float(b_text)
c = float(c_text)

# Ищем максимум: число, которое не меньше двух остальных
if a >= b and a >= c:
    maximum = a_text
elif b >= a and b >= c:
    maximum = b_text
else:
    maximum = c_text

# Ищем минимум: число, которое не больше двух остальных
if a <= b and a <= c:
    minimum = a_text
elif b <= a and b <= c:
    minimum = b_text
else:
    minimum = c_text

print(maximum, minimum)
