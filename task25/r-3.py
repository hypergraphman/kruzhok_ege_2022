def dels(n):
    res = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)


def only_odd_dels(n):
    res = []
    for el in dels(n):
        if el % 2 != 0:
            res.append(el)
    return res


start = 77_777_777
end = 88_888_888
for el in range(start, end + 1):
    t = only_odd_dels(el)
    if len(t) == 5:
        print(el, t[1])
