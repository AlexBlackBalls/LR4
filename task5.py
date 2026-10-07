# Задача 5. Сколько дней осталось до Нового года (год не високосный).

m = int(input())
d = int(input())

# Сколько дней в месяце m
if m == 2:
    days_in_month = 28
elif m == 4 or m == 6 or m == 9 or m == 11:
    days_in_month = 30
else:
    days_in_month = 31

# Проверка корректности ввода
if m < 1 or m > 12 or d < 1 or d > days_in_month:
    print(-1)
else:
    # Сколько дней прошло в предыдущих месяцах
    if m == 1:
        before = 0
    elif m == 2:
        before = 31
    elif m == 3:
        before = 59
    elif m == 4:
        before = 90
    elif m == 5:
        before = 120
    elif m == 6:
        before = 151
    elif m == 7:
        before = 181
    elif m == 8:
        before = 212
    elif m == 9:
        before = 243
    elif m == 10:
        before = 273
    elif m == 11:
        before = 304
    else:
        before = 334
    day_of_year = before + d
    print(365 - day_of_year)
