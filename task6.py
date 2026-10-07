# Задача 6. Грибы с правильным окончанием.

k = int(input())

if k < 0:
    print("Мы не находили грибы, а только теряли")
else:
    last = k % 10          # последняя цифра
    last_two = k % 100     # последние две цифры
    if last_two >= 11 and last_two <= 14:
        word = "грибов"    # 11-14 всегда "грибов"
    elif last == 1:
        word = "гриб"
    elif last >= 2 and last <= 4:
        word = "гриба"
    else:
        word = "грибов"
    print("Мы нашли в лесу", k, word)
