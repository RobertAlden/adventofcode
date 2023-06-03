with open('input.txt') as f:
    data = [line.strip().split(' ') for line in f.readlines()]

data = [(inst[0], int(inst[1])) if len(inst) > 1 else (inst[0], 0) for inst in data]


def silver():
    X = 1
    timeline = [1]
    for inst in data:
        cmd, val = inst
        if len(timeline) > 220:
            break
        if cmd == 'addx':
            timeline += [X, X+val]
            X += val
        else:
            timeline += [X]

    return sum([(val * (idx+1)) for idx, val in enumerate(timeline) if idx+1 in [20, 60, 100, 140, 180, 220]])


def gold():
    X = 1
    timeline = [1]
    for inst in data:
        cmd, val = inst
        if cmd == 'addx':
            timeline += [X, X+val]
            X += val
        else:
            timeline += [X]
    screen = ['#' if abs(((idx) % 40)-val) <= 1 else ' ' for idx, val in enumerate(timeline)]
    screen = [screen[i:i+40] for i in range(0, len(screen), 40)]
    for i in screen:
        print("".join(i))
    return screen


print(f'Silver: {silver()}')

print(f'Gold: {gold()}')

