def func(x, y):
    avg = (x + y) / 2
    start = 0
    end = n
    while True:
        i = (start + end + 1) // 2
        if end - start == 1:
            return start + 1
        if a[i] == avg:
            return i
        if avg > a[i]:
            start = i
        else:
            end = i


f = open('26-47.txt')
n = int(f.readline())
a = sorted([int(x) for x in f.readlines()])
mx_k = 0
count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        k = func(a[i], a[j])
        if k > 0 and k % 100 == 0:
            count += 1
            mx_k = max(mx_k, k)
print(count, mx_k)


