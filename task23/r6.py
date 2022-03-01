def f(start, end):
    a = [0] * 10000
    a[start] = 1
    for i in range(start, end):
        if i + 1 == end:
            a[i + 1] += a[i - 1]
        else:
            a[i + 1] += a[i]
        if 2 * i == end:
            a[i * 2] += a[i - 1]
        else:
            a[i * 2] += a[i]
    print(a[end])
    return a[end]


print(f(4, 17))