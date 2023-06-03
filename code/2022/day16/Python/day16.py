from itertools import permutations
from time import time_ns
import re

with open('test.txt') as f:
    test_input = [line.strip() for line in f.readlines()]
    test_input = [[(match[0], int(match[1]), match[2].split(", "))
                   for match in re.findall(r'([A-Z]{2}).*=(\d+).*valves? (.*)', line)][0] for line in test_input]
    test_graph = dict(zip([item[0] for item in test_input], [item[2] for item in test_input]))
    test_values = dict(zip([item[0] for item in test_input], [int(item[1]) for item in test_input]))


with open('input.txt') as f:
    real_input = [line.strip() for line in f.readlines()]
    real_input = [[(match[0], int(match[1]), match[2].split(", "))
                   for match in re.findall(r'([A-Z]{2}).*=(\d+).*valves? (.*)', line)][0] for line in real_input]
    real_graph = dict(zip([item[0] for item in real_input], [item[2] for item in real_input]))
    real_values = dict(zip([item[0] for item in real_input], [int(item[1]) for item in real_input]))


def distances_from_node(node, graph):
    bsf_queue = [node]
    next_nodes = []
    visited = []
    distances = []
    time = 0
    while len(bsf_queue):
        current_node = bsf_queue.pop(0)
        visited.append(current_node)
        distances.append((current_node, time))
        next_nodes += [node for node in graph[current_node] if node not in next_nodes and node not in visited]
        if len(bsf_queue) == 0:
            if len(next_nodes) == 0:
                break
            bsf_queue += next_nodes
            next_nodes = []
            time += 1
    return dict(distances[1:])


# def silver(graph, values):
#     desired_nodes = dict([node, value*30] for node, value in values.items() if value > 0)
#     current_node = 'AA'
#     visited = []
#     score = 0
#     time_elapsed = 0
#     while len(desired_nodes):
#         distances = distances_from_node(current_node, graph)
#         potential_distances = set([distances[key] for key in desired_nodes.keys()])
#         how_far_to_go = max([(sum([value - values[key]*(time_elapsed+distance+1) for key, value in desired_nodes.items()]), distance)
#                              for distance in potential_distances])
#         desired_nodes = {key: value-(values[key]*(distances[key]+1))
#                          for (key, value) in desired_nodes.items() if key in distances}
#         where_to_go = max([(value, key) for key, value in desired_nodes.items() if distances[key] == how_far_to_go[1]])
#         score += where_to_go[0]
#         current_node = where_to_go[1]
#         time_elapsed += how_far_to_go[1] + 1
#         del desired_nodes[current_node]
#     return score

def silver(graph, values):
    desired_nodes = dict([node, value] for node, value in values.items() if value > 0)
    current_node = 'AA'
    steam_released = 0
    time_remaining = 30
    steam_lost_per_turn = sum(desired_nodes.values())
    steam_available = steam_lost_per_turn * time_remaining
    while time_remaining > 0 and len(desired_nodes.keys()) > 0:
        distances = distances_from_node(current_node, graph)
        gains = {node: values[node]*(time_remaining - (distance + 1)) for node, distance in distances.items()
                 if node in desired_nodes.keys() and time_remaining - (distance + 1) >= 0}
        costs = {node: steam_lost_per_turn*(distance + 1) for node, distance in distances.items()
                 if node in desired_nodes.keys() and time_remaining - (distance + 1) >= 0}
        net_value = {node: gains[node] - costs[node] for node in desired_nodes.keys()}
        if len(net_value) == 0:
            break
        next_node = sorted(net_value.items(), key=lambda x: x[1])[-1][0]
        steam_released += gains[next_node]
        time_remaining -= distances[next_node] + 1
        steam_available = steam_lost_per_turn * time_remaining
        steam_lost_per_turn -= values[next_node]
        current_node = next_node
        del desired_nodes[current_node]

    return steam_released


def gold(graph, values):
    pass


print("TEST DATA:")
start = time_ns()
print(f'Silver: {silver(test_graph, test_values)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

start = time_ns()
print(f'Gold: {gold(test_graph, test_values)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

print("REAL DATA:")
start = time_ns()
print(f'Silver: {silver(real_graph, real_values)}, took {(time_ns() - start) / 1_000_000_000} seconds.')
#
# start = time_ns()
# print(f'Gold: {gold(real_graph, real_values)}, took {(time_ns() - start) / 1_000_000_000} seconds.')

