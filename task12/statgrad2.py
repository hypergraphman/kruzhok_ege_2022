for i in range(1, 16):
    line = '1' * (201 + i)
    while '1111' in line:
        line = line.replace('1111', '22', 1)
        line = line.replace('222', '1', 1)
    print((201 + i), line)