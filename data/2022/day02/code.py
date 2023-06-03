with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]


games = ['A X', 'A Y', 'A Z', 'B X', 'B Y', 'B Z', 'C X', 'C Y', 'C Z']

def part1(_data):
    scores = [4, 8, 3, 1, 5, 9, 7, 2, 6]
    _data = sum([scores[games.index(line)] for line in _data])
    return _data


def part2(_data):
    scores = [3, 4, 8, 1, 5, 9, 2, 6, 7]
    _data = sum([scores[games.index(line)] for line in _data])
    return _data


print(f'Part 1: {part1(data)}')

print(f'Part 2: {part2(data)}')

