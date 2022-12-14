from itertools import zip_longest, pairwise, chain, repeat

with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

data = [[tuple([int(value) for value in coordinate.split(',')]) for coordinate in line.split(' -> ')] for line in data]


def generate_interval(start, end):
    delta_x, delta_y = end[0] - start[0], end[1] - start[1]
    sign_x = delta_x // abs(delta_x) if delta_x else 0
    sign_y = delta_y // abs(delta_y) if delta_y else 0
    x_values = [(i+1) * sign_x for i in range(abs(delta_x))]
    y_values = [(i+1) * sign_y for i in range(abs(delta_y))]
    return [start] + [(start[0]+x, start[1]+y) for x, y in zip_longest(x_values, y_values, fillvalue=0)]


def silver():
    obstacles = frozenset(chain(*[chain(*[generate_interval(*pair) for pair in pairwise(wall)]) for wall in data]))
    sand = 0
    x, y = 500, 0
    while True:
        options = [next_move for next_move in zip([x, x-1, x+1], repeat(y+1)) if next_move not in obstacles]
        match options:
            case [move, *rest]:
                x, y = move
                if len(floors_below := list(filter(lambda t: t[0] == x and t[1] > y, obstacles))):
                    y = min(floors_below)[1]-1
                else:
                    break
            case []:
                obstacles = obstacles | {(x, y)}
                sand += 1
                x, y = 500, 0
    return sand


def gold():
    obstacles = list(chain(*[chain(*[generate_interval(*pair) for pair in pairwise(wall)]) for wall in data]))
    floor = sorted(obstacles, key=lambda p: p[1], reverse=True)[0][1]+2
    sorted_x = sorted(obstacles, key=lambda p: p[0])
    left, right = sorted_x[0], sorted_x[-1]
    sand = 0
    x, y = 500, 0
    while True:
        options = [next_move for next_move in zip([x, x - 1, x + 1], repeat(y + 1)) if next_move not in obstacles]
        options = [option for option in options if option[1] != floor]
        match options:
            case [move, *rest]:
                x, y = move
                if len(floors_below := list(filter(lambda t: t[0] == x and t[1] > y, obstacles))):
                    y = min(floors_below)[1] - 1
                else:
                    y = floor-1
            case []:
                obstacles.append((x, y))
                sand += 1
                x, y = 500, 0
        if (500, 0) in obstacles:
            break
    return sand


print(f'Silver: {silver()}')

print(f'Gold: {gold()}')
