moves = [
    lambda x: (x[0] + 3, x[1]),
    lambda x: (x[0] * 2, x[1]),
    lambda x: (x[0], x[1] + 3),
    lambda x: (x[0], x[1] * 2)
]


def petr(rocks, turn=1):
    if turn > 2:
        return 0, 100500  # После 2 хода игра закончилась ничьей
    endings = set()
    for f in moves:
        new_rocks = f(rocks)
        if sum(new_rocks) > 42:
            return 1, turn  # выиграл Петя
        endings.add(ivan(new_rocks, turn))
    if 1 in [x[0] for x in endings]:  # Если есть выигрышная стратегия
        return max(endings, key=lambda x: [x[0], -x[1]])  # Выбираем ту, что гарантирует наибыстрейшую победу
    if 0 in [x[0] for x in endings]:
        return 0, 100500  # Если выиграть не можем, сводим к ничьей
    return max(endings)  # Иначе затягиваем игру


def ivan(rocks, turn=1):
    endings = set()
    for f in moves:
        new_rocks = f(rocks)
        if sum(new_rocks) > 42:
            return -1, turn
        endings.add(petr(new_rocks, turn + 1))
    if -1 in [x[0] for x in endings]:
        return min(endings)
    if 0 in [x[0] for x in endings]:
        return 0, 100500
    return max(endings)


for s in range(1, 33):
    print(s, petr((10, s)))




