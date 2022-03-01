def f(start, end):
    a = [0] * 10000
    a[start] = 1
    for i in range(start, end):
        if i == 25:
            a[i] = 0
        a[i + 1] += a[i]
        a[i * 2] += a[i]
    print(a[end])
    return a[end]


print(f(2, 14) * f(14, 29))