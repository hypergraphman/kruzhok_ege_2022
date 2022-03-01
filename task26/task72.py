from itertools import pairwise

# f = open('26-72.txt')
f = open('1.txt')
x, y, n = map(int, f.readline().split())
a = sorted([tuple(map(int, el.split())) for el in f.readlines()])
count = 0
row_count = 0
mx_row = 0
row = 0
for el1, el2 in pairwise(a):
    if el1[0] == el2[0]:
        t = el2[1] - el1[1] - 3
        if t > 0:
            count += t
            row_count += t
            if mx_row < row_count:
                mx_row = row_count
                row = el1[0]
    else:
        if el2[0] - el1[0] == 1:
            t = x + 1 - el1[1] - 3
            if t > 0:
                count += t
                row_count += t
                if mx_row < row_count:
                    mx_row = row_count
                    row = el1[0]
        else:
            count += (el2[0] - el1[0] - 1) * (x - 3)
            if mx_row < x - 3:
                mx_row = x - 3
                row = el1[0] + 1
        row_count = 0

el1 = a[-1]
if y - el1[0] == 1:
    t = x + 1 - el1[1] - 3
    if t > 0:
        count += t
        row_count += t
        if mx_row < row_count:
            mx_row = row_count
            row = el1[0]
else:
    count += (el2[0] - el1[0] - 1) * (x - 3)
    if mx_row < x - 3:
        mx_row = x - 3
        row = el1[0] + 1
print(count, row)