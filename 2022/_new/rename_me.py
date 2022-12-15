from time import time_ns

with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]


def silver():
    pass


def gold():
    pass


start = time_ns()
print(f'Silver: {silver()}, took {(time_ns() - start) / 1_000_000_000} seconds.')

start = time_ns()
print(f'Gold: {gold()}, took {(time_ns() - start) / 1_000_000_000} seconds.')
