def f(start, end):
    a = [0] * 10000
    a[start] = 1
    for i in range(start, end):
        a[i + 1] += a[i]
        a[i + 2] += a[i]
        a[i * 3] += a[i]
    print(a[end])
    return a[end]


print(f(2, 8) * f(8, 10) * f(10, 12))