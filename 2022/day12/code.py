from itertools import chain


def silver():
    with open('input.txt') as f:
        data = [line.strip() for line in f.readlines()]
    y_range = len(data)
    x_range = len(data[0])
    data = [line.replace('S', '`') for line in data]
    data = [line.replace('E', '{') for line in data]
    data = [[ord(c) - 96 for c in row] for row in data]

    visited = []
    bfs_queue = []
    start = [[[y, x] for x, value in enumerate(row) if value == 0] for y, row in enumerate(data) if 0 in row][0][0]
    target = [[[y, x] for x, value in enumerate(row) if value == 27] for y, row in enumerate(data) if 27 in row][0][0]

    def adjacent(y, x):
        candidates = [[y + 1, x], [y - 1, x], [y, x + 1], [y, x - 1]]
        return [[_y, _x] for _y, _x in candidates if _y in range(y_range) and _x in range(x_range)]

    bfs_queue.append([start])
    visited.append(start)
    while len(bfs_queue) > 0:
        current_path = bfs_queue.pop(0)
        current = current_path[-1]
        if current == target:
            return len(current_path) - 1
        cells = adjacent(current[0], current[1])
        cells = [cell for cell in cells if (cell not in visited) and
                 (data[cell[0]][cell[1]] - 1) <= data[current[0]][current[1]]]
        visited += cells
        bfs_queue += [current_path + [cell] for cell in cells]
    return -1


def gold():
    with open('input.txt') as f:
        data = [line.strip() for line in f.readlines()]
    y_range = len(data)
    x_range = len(data[0])
    data = [line.replace('S', 'a') for line in data]
    data = [line.replace('E', '{') for line in data]
    data = [[ord(c) - 96 for c in row] for row in data]

    paths = []
    start = list(chain(*[[[y, x] for x, value in enumerate(row) if value == 1] for y, row in enumerate(data) if 1 in row]))
    target = [[[y, x] for x, value in enumerate(row) if value == 27] for y, row in enumerate(data) if 27 in row][0][0]

    def bfs(_y, _x):
        visited = []
        bfs_queue = []

        def adjacent(y, x):
            candidates = [[y + 1, x], [y - 1, x], [y, x + 1], [y, x - 1]]
            return [[_y, _x] for _y, _x in candidates if _y in range(y_range) and _x in range(x_range)]

        bfs_queue.append([[_y, _x]])
        visited.append([_y, _x])
        while len(bfs_queue) > 0:
            current_path = bfs_queue.pop(0)
            current = current_path[-1]
            if current == target:
                return len(current_path) - 1
            cells = adjacent(current[0], current[1])
            cells = [cell for cell in cells if (cell not in visited) and
                     (data[cell[0]][cell[1]] - 1) <= data[current[0]][current[1]]]
            visited += cells
            bfs_queue += [current_path + [cell] for cell in cells]
        return x_range*y_range+1

    return min([bfs(s[0], s[1]) for s in start])


print(f'Silver: {silver()}')

print(f'Gold: {gold()}')


