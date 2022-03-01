line = 'ffffgabcabhjjjjabjjjabcabcabkllllll'
cur_len = 0
max_len = 0
t = 'abc'
for i in range(len(line) - 1):
    if line[i] == t[cur_len % len(t)]:
        cur_len += 1
        if max_len < cur_len:
            max_len = cur_len
    else:
        cur_len = 0
print(max_len)
