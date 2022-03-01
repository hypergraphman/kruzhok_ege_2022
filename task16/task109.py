import functools


@functools.cache
def f(n):
    if 2 >= n or n == 8:
        return 0
    if n == 3:
        return 1
    return f(n - 2) + f(n - 1)


for i in range(100):
    if f(i) == 25:
        print(i)