from collections import Counter
from itertools import chain, product
from time import time_ns
import re

with open('test.txt') as f:
    test_input = [line.strip() for line in f.readlines()]
    test_input = [[(int(match[0]), int(match[1]))
                   for match in re.findall(r'(-?\d+),\W..(-?\d+)', line)] for line in test_input]


with open('input.txt') as f:
    real_input = [line.strip() for line in f.readlines()]
    real_input = [[(int(match[0]), int(match[1]))
                   for match in re.findall(r'(-?\d+),\W..(-?\d+)', line)] for line in real_input]


def silver(data, y):
    sensors = [sensor for sensor, beacon in data]
    distances = [(abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])) for sensor, beacon in data]
    offsets = [abs(y - sensor[1]) for sensor in sensors]
    relevant_sensors = [(sensor, distance - offset)
                        for sensor, distance, offset in zip(sensors, distances, offsets) if distance - offset >= 0]
    unique_points_crossing_y = set(chain(*[list(range(sensor[0]-overlap, sensor[0]+overlap))
                                           for sensor, overlap in relevant_sensors]))
    return len(unique_points_crossing_y)


def gold(data, x_max, y_max):
    sensors = [sensor for sensor, beacon in data]
    distances = [(abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])) for sensor, beacon in data]
    shells = [list(zip(range(sensor[0] + distance+1, sensor[0], -1), range(sensor[1], sensor[1] + distance+1)))
              for distance, sensor in zip(distances, sensors)]
    shells = [shell+[(-y, x) for x, y in shell] for shell in shells]
    shells = list(chain(*[shell + [(-x, -y) for x, y in shell] for shell in shells]))
    shells = [(x, y) for x, y in shells if 0 <= x <= x_max and 0 <= y <= y_max]
    valid_positions = []
    for x, y in shells:
        for sensor, distance in zip(sensors, distances):
            if abs(x - sensor[0])+abs(y - sensor[1]) < distance:
                break
        else:
            valid_positions.append((x, y))
    return [x * 4_000_000 + y for x, y in valid_positions][0]


print("TEST DATA:")
start = time_ns()
print(f'Silver: {silver(test_input, 10)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

start = time_ns()
print(f'Gold: {gold(test_input, 20, 20)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

print("REAL DATA:")
start = time_ns()
print(f'Silver: {silver(real_input, 2_000_000)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

start = time_ns()
print(f'Gold: {gold(real_input, 4_000_000, 4_000_000)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

