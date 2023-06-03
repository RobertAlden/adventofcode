from string import ascii_letters

with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

def part1(_data):
    _data = [(line[:len(line)//2], line[len(line)//2:]) for line in _data]
    _data = [list(set(g1).intersection(set(g2)))[0] for g1, g2 in _data]
    _data = sum([ascii_letters.index(c)+1 for c in _data])
    return _data

def part2(_data):
    _data = [_data[idx*3:idx*3+3] for idx in range(len(data)//3)]
    _data = [list(set(g1).intersection(set(g2).intersection(g3)))[0] for g1, g2,g3 in _data]
    _data = sum([ascii_letters.index(c) + 1 for c in _data])
    return _data


print(f'Part 1: {part1(data)}')

print(f'Part 2: {part2(data)}')
