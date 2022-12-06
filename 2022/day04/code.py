import re
with open('input.txt') as f:
    data = [line for line in f.readlines()]

data = [re.split(r'[,-]', line.strip()) for line in data]
data = [((int(line[0]), int(line[1])), (int(line[2]), int(line[3]))) for line in data]


def part1(_data):
    def overlaps(range_tuple):
        ((s1, e1), (s2, e2)) = range_tuple
        return (s1 <= s2 and e1 >= e2) or (s1 >= s2 and e1 <= e2)

    _data = [overlaps(rt) for rt in _data]

    return sum(_data)


def part2(_data):
    def overlaps_any(range_tuple):
        ((s1, e1), (e2, s2)) = range_tuple
        return (s1 <= s2 and e1 >= e2) or (s1 >= s2 and e1 <= e2)

    _data = [overlaps_any(rt) for rt in _data]

    return sum(_data)


print(f'Part 1: {part1(data)}')

print(f'Part 2: {part2(data)}')
