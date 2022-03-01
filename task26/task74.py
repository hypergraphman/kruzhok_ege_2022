f = open('26-73.txt')
a = [[0] * 480 for _ in range(640)]
n = int(f.readline())
for _ in range(n):
    row, col = map(int, f.readline().split())
    a[row - 1][col - 1] = 1

mx = 0
row_i = 0
for i, row in enumerate(a, 1):
    start = False
    prev_w = False
    count = 0
    for el in row:
        if el == 1 and not start:
            start = True
            prev_w = True
            count = 1
        elif el == 1 and start and not prev_w:
            count += 1
            prev_w = True
            if mx < count:
                mx = count
                row_i = i
        elif el == 1 and start and prev_w:
            count = 1
        elif el == 0 and start and not prev_w:
            start = False
            count = 0
        elif el == 0 and start and prev_w:
            prev_w = False
print(mx, row_i)
f.close()
