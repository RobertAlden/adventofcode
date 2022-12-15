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
    relevant_sensors = [(sensor, distances[idx] - offset) for idx, (sensor, offset) in enumerate(zip(sensors, offsets))
                        if distances[idx] - offset >= 0]
    unique_points_crossing_y = set(chain(*[list(range(sensor[0]-overlap, sensor[0]+overlap))
                                           for sensor, overlap in relevant_sensors]))
    return len(unique_points_crossing_y)


def gold(data, x_max, y_max):
    x_intervals = [[0, x_max]]
    y_intervals = [[0, y_max]]
    sensors = [sensor for sensor, beacon in data]
    distances = [(abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])) for sensor, beacon in data]
    x_occlusions = [(max(sensor[0] - distance, 0), min(sensor[0] + distance, x_max))
                    for sensor, distance in zip(sensors, distances)]
    y_occlusions = [(max(sensor[1] - distance, 0), min(sensor[1] + distance, y_max))
                    for sensor, distance in zip(sensors, distances)]

    return None


print("TEST DATA:")
start = time_ns()
print(f'Silver: {silver(test_input, 10)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

start = time_ns()
print(f'Gold: {gold(test_input, 20, 20)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

print("REAL DATA:")
start = time_ns()
print(f'Silver: {silver(real_input, 2_000_000)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

#start = time_ns()
#print(f'Gold: {gold(real_input, 4_000_000, 4_000_000)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

