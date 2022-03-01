for a in range(1, 37):
    f = True
    for x in range(1, 1000000):
        da = x % a == 0
        d6 = x % 6 == 0
        d9 = x % 9 == 0
        if not ((not da) <= (d6 <= (not d9))):
            f = False
            break
    if f:
        print(a)