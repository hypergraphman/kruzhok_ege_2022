import functools


@functools.cache
def f(n):
    if n < 10:
        return n
    return f(g(n))


@functools.cache
def g(n):
    if n < 10:
        return n
    return n % 10 + g(n // 10)


print(f(12345678987654321))