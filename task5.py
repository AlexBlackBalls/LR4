m = int(input())
d = int(input())

if m == 2:
    dim = 28
elif m == 4 or m == 6 or m == 9 or m == 11:
    dim = 30
else:
    dim = 31

if m < 1 or m > 12 or d < 1 or d > dim:
    print(-1)
else:
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
    day = before + d
    print(365 - day)
