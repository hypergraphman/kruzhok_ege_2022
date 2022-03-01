import functools


@functools.cache
def fib(n):
    if n == 1 or n == 2:
        return 1
    if n > 2:
        return fib(n - 2) + fib(n - 1)


n = int(input())
print(fib(n))