x = 8
a = 7 * x + 27
b = 7 * x - 33
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)