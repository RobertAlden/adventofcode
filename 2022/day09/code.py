from itertools import chain

with open('input.txt') as f:
    data = [line.strip().split(' ') for line in f.readlines()]


def convert(movelist):
    table = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    return list(chain(*[[(table[direction])]*int(distance) for direction, distance in movelist]))


def follow(a, b):
    return abs(a[0]-b[0]) > 1 or abs(a[1]-b[1]) > 1


def drag(h, t):
    dx = h[0] - t[0]
    dy = h[1] - t[1]
    if dx:
        dx //= abs(dx)
    if dy:
        dy //= abs(dy)
    return t[0] + dx, t[1] + dy


def silver():
    rope_length = 2
    moves = convert(data)
    rope = [(0, 0)] * rope_length
    positions = []
    for m in moves:
        rope[0] = (rope[0][0]+m[0], rope[0][1]+m[1])
        for idx, link in enumerate(rope[:-1]):
            if follow(rope[idx], rope[idx+1]):
                rope[idx+1] = drag(rope[idx], rope[idx+1])
        if rope[-1] not in positions:
            positions.append(rope[-1])
    return len(positions)


def gold():
    rope_length = 10
    moves = convert(data)
    rope = [(0, 0)] * rope_length
    positions = []
    for m in moves:
        rope[0] = (rope[0][0] + m[0], rope[0][1] + m[1])
        for idx, link in enumerate(rope[:-1]):
            if follow(rope[idx], rope[idx + 1]):
                rope[idx + 1] = drag(rope[idx], rope[idx + 1])
        if rope[-1] not in positions:
            positions.append(rope[-1])
    return len(positions)


print(f'Silver: {silver()}')

print(f'Gold: {gold()}')
