from time import time_ns
from itertools import zip_longest, pairwise, chain, repeat

with open('test.txt') as f:
    test_input = [line.strip() for line in f.readlines()]

with open('input.txt') as f:
    real_input = [line.strip() for line in f.readlines()]


test_input = [[tuple([int(value) for value in vec.split(',')]) for vec in line.split(' -> ')] for line in test_input]
real_input = [[tuple([int(value) for value in vec.split(',')]) for vec in line.split(' -> ')] for line in real_input]


def generate_interval(start, end):
    delta_x, delta_y = end[0] - start[0], end[1] - start[1]
    sign_x = delta_x // abs(delta_x) if delta_x else 0
    sign_y = delta_y // abs(delta_y) if delta_y else 0
    x_values = [(i+1) * sign_x for i in range(abs(delta_x))]
    y_values = [(i+1) * sign_y for i in range(abs(delta_y))]
    return [start] + [(start[0]+x, start[1]+y) for x, y in zip_longest(x_values, y_values, fillvalue=0)]


def silver(data):
    obstacles = frozenset(chain(*[chain(*[generate_interval(*pair) for pair in pairwise(wall)]) for wall in data]))
    sand = 0
    x, y = 500, 0
    while True:
        options = [next_move for next_move in zip([x, x-1, x+1], repeat(y+1)) if next_move not in obstacles]
        if len(options) > 0:
            x, y = options[0]
            if len(floors_below := list(filter(lambda t: t[0] == x and t[1] > y, obstacles))):
                y = min(floors_below)[1]-1
            else:
                break
        else:
            obstacles = obstacles | {(x, y)}
            sand += 1
            x, y = 500, 0
    return sand


def gold(data):
    obstacles = frozenset(chain(*[chain(*[generate_interval(*pair) for pair in pairwise(wall)]) for wall in data]))
    floor = sorted(obstacles, key=lambda p: p[1], reverse=True)[0][1]+2
    sand = 1
    bsf_queue = [500]
    y = 1
    next_batch = []
    while len(bsf_queue) > 0:
        x = bsf_queue.pop(0)
        potential_moves = [x, x - 1, x + 1]
        potential_moves = [move for move in potential_moves if move not in next_batch]
        potential_moves = [move for move in potential_moves if (move, y) not in obstacles]
        next_batch += potential_moves
        sand += len(potential_moves)
        if len(bsf_queue) == 0:
            y += 1
            if len(next_batch) == 0 or y == floor:
                return sand
            bsf_queue += next_batch[:]
            next_batch = []


print("TEST DATA:")
start = time_ns()
print(f'Silver: {silver(test_input)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

start = time_ns()
print(f'Gold: {gold(test_input)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

print("REAL DATA:")
start = time_ns()
print(f'Silver: {silver(real_input)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

start = time_ns()
print(f'Gold: {gold(real_input)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

