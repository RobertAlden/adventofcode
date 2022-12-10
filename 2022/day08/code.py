from functools import reduce
from itertools import accumulate
from operator import mul

with open('input.txt') as f:
    data = [list(map(int, list(line.strip()))) for line in f.readlines()]


def visible_trees(trees: list) -> int:
    if len(trees) == 0:
        return 0
    return sum([a > b for a, b in zip(trees, [-1] + list(accumulate(trees, func=max)))])


def scenic_view(trees: list, h:int) -> int:
    if len(trees) == 0:
        return 0
    trees = [t >= h for t in trees]
    if True in trees:
        trees = trees[:trees.index(True)+1]
    return len(trees)


def transpose(matrix: list[list]) -> list[list]:
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


dataT = transpose(data)

scenic = 0
for y, row in enumerate(data):
    for x, val in enumerate(row):
        col = dataT[x]
        tree = data[y][x]
        views = [list(reversed(col[:y])), col[y + 1:], list(reversed(row[:x])), row[x + 1:]]
        score = reduce(mul, [scenic_view(v, tree) for v in views])
        if score > scenic:
            scenic = score

print(scenic)
