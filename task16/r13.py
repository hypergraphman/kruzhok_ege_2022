import functools


@functools.cache
def f(n):
    if n <= 5:
        return 2 * n
    if n % 2 == 0:
        return f(n - 2) + 3 * f(n // 2) + n
    return f(n - 1) + f(n - 2) + f(n - 3)


print(f(99) + f(100))