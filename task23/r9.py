def f(start, end):
    a = [0] * 10000
    a[start] = 1
    for i in range(start, end):
        if i == 75:
            a[i] = 0
        a[i + 1] += a[i]
        a[i * 2] += a[i]
    print(a[end])
    return a[end]

print(f(1, 25) * f(25, 100))