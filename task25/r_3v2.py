# функция для определения простоты числа
def isPrime(x):
    if x <= 1: return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


start, end = 77777777, 88888888
from math import sqrt

# перебираем все числа из отрезка
for n in range(start, end + 1):
    x = n
    # убираем из разложения числа x на простые множители все двойки
    while x % 2 == 0: x //= 2
    # находим корень четвёртой степени из того, что осталось
    qX = round(sqrt(sqrt(x)))
    # проверяем, является ли x четвёртой степенью простого числа
    if isPrime(qX) and qX ** 4 == x:
        print(n, qX)
