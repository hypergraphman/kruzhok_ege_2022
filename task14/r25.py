def ten_to_p(n, p):
    res = ''
    while n > 0:
        d = n % p
        if d > 9:
            d = chr(ord('A') - 10 + d)
        res = str(d) + res
        n //= p
    return res


n = 49**7 + 7**21 - 7
print(ten_to_p(n, 7).count('6'))