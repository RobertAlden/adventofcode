from time import time_ns

with open('test.txt') as f:
    test_input = [line.strip() for line in f.readlines()]

with open('input.txt') as f:
    real_input = [line.strip() for line in f.readlines()]


def silver():
    pass


def gold():
    pass


print("TEST DATA:")
start = time_ns()
print(f'Silver: {silver(test_input)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

start = time_ns()
print(f'Gold: {gold(test_input)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

print("REAL DATA:")
start = time_ns()
print(f'Silver: {silver(real_input)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

start = time_ns()
print(f'Gold: {gold(real_input)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

