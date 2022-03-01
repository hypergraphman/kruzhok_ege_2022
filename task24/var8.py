import itertools

print(max(map(sum, itertools.pairwise(map(len, open('24.txt').readline().split('Z'))))) + 1)
