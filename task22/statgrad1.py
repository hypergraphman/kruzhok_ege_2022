for i in range(5, 200):
    x = i
    a = 7 * x + 27
    b = 7 * x - 33
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 15:
        print(i)