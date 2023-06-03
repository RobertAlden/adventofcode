from math import lcm

with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]




def silver():
    items = [line[len('Starting items: '):].split(', ') for line in data if line.startswith('Starting items: ')]
    items = [list(map(int, item_list)) for item_list in items]
    operations = [line[len('Operation: '):] for line in data if line.startswith('Operation: ')]
    operations = [eval(ops.replace('new =', 'lambda x:').replace('old', 'x')) for ops in operations]
    tests = [int(line[len('Test: divisible by '):]) for line in data if line.startswith('Test: divisible by ')]
    send_if_true = [int(line[len('If true: throw to monkey '):]) for line in data if
                    line.startswith('If true: throw to monkey ')]
    send_if_false = [int(line[len('If false: throw to monkey '):]) for line in data if
                     line.startswith('If false: throw to monkey ')]
    activity = [0 for line in data if line.startswith('Monkey ')]

    iterations = 0
    while iterations < 20:
        for i in range(len(activity)):
            while len(items[i]):
                item = items[i].pop(0)
                item = int(operations[i](item)) // 3
                if item % tests[i] == 0:
                    items[send_if_true[i]].append(item)
                else:
                    items[send_if_false[i]].append(item)
                activity[i] += 1
        iterations += 1

    sorted_activity = sorted(activity, reverse=True)
    result = sorted_activity[0] * sorted_activity[1]
    return result


def gold():
    items = [line[len('Starting items: '):].split(', ') for line in data if line.startswith('Starting items: ')]
    items = [list(map(int, item_list)) for item_list in items]
    operations = [line[len('Operation: '):] for line in data if line.startswith('Operation: ')]
    operations = [eval(ops.replace('new =', 'lambda x:').replace('old', 'x')) for ops in operations]
    tests = [int(line[len('Test: divisible by '):]) for line in data if line.startswith('Test: divisible by ')]
    send_if_true = [int(line[len('If true: throw to monkey '):]) for line in data if
                    line.startswith('If true: throw to monkey ')]
    send_if_false = [int(line[len('If false: throw to monkey '):]) for line in data if
                     line.startswith('If false: throw to monkey ')]
    activity = [0 for line in data if line.startswith('Monkey ')]

    iterations = 0
    while iterations < 10000:
        for i in range(len(activity)):
            while len(items[i]):
                item = items[i].pop(0)
                item = int(operations[i](item)) % lcm(*tests)
                if item % tests[i] == 0:
                    items[send_if_true[i]].append(item)
                else:
                    items[send_if_false[i]].append(item)
                activity[i] += 1
        iterations += 1

    sorted_activity = sorted(activity, reverse=True)
    result = sorted_activity[0] * sorted_activity[1]
    return result


print(f'Silver: {silver()}')

print(f'Gold: {gold()}')
