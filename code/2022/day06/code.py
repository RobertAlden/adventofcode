with open('input.txt') as f:
    data = [line for line in f.readlines()]


def part1(_data):
    scan_size = 4
    for d in _data:
        for i in range(len(d)-scan_size):
            region = d[i:i+scan_size]
            if len(set(region)) == scan_size:
                return i+scan_size


def part2(_data):
    scan_size = 14
    for d in _data:
        for i in range(len(d) - scan_size):
            region = d[i:i + scan_size]
            if len(set(region)) == scan_size:
                return i + scan_size


print(f"Part 1: {part1(data)}")

print(f"Part 2: {part2(data)}")