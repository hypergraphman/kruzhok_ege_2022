for a in range(1, 100):
    f = True
    for k in range(1, 1000):
        for n in range(1, 1000):
            d1 = 5 * k + 6 * n > 57
            d2 = k <= a
            d3 = n < a
            if not (d1 or d2 and d3):
                f = False
                break
    if f:
        print(a)