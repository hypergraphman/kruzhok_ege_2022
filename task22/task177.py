from itertools import permutations

alf = 'НННЧЧЧ'
words = set()
for word in permutations(alf):
    word = ' '.join(word)
    words.add(word)

for word in sorted(words):
    print(word)