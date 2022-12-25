from time import time_ns

with open('test.txt') as f:
    test_input = [line.strip() for line in f.readlines()]

with open('input.txt') as f:
    real_input = [line.strip() for line in f.readlines()]


def silver(data):
    value_table = ['=', '-', '0', '1', '2']
    bases = [5**i for i in range(30)]
    numbers = [[value_table.index(digit)-2 for digit in number][::-1] for number in data]
    numbers = [sum([a * b for a, b in zip(number, bases)]) for number in numbers]
    total = sum(numbers)
    value = ''
    while total:
        total, r = divmod(total, 5)
        match r:
            case 0 | 1 | 2:
                value = str(r) + value
            case 3:
                total += 1
                value = '=' + value
            case 4:
                total += 1
                value = '-' + value
    return value

print("TEST DATA:")
start = time_ns()
print(f'Silver: {silver(test_input)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

print("REAL DATA:")
start = time_ns()
print(f'Silver: {silver(real_input)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

