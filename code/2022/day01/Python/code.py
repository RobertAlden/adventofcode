with open('input.txt') as f:
    data = [line for line in f.readlines()]

data = [line.strip() for line in data]


def list_split(_list, _sep):
    bool_seq = [(i == _sep) for i in _list]
    seq = []
    chunk = []
    for b, v in zip(bool_seq, _list):
        if not b:
            chunk += [v]
        else:
            seq += [chunk]
            chunk = []
    seq += [chunk]
    return seq


data = list_split(data, '')

data = [sum([int(val) for val in group]) for group in data]

print(f"Part 1: {max(data)}")

print(f"Part 2: {sum(sorted(data, reverse=True)[:3])}")

