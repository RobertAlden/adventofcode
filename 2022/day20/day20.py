from time import time_ns

with open('test.txt') as f:
    test_input = [int(line.strip()) for line in f.readlines()]

with open('input.txt') as f:
    real_input = [int(line.strip()) for line in f.readlines()]


def silver(data):
    unmixed_data = list(enumerate(data[:]))
    for i, value in enumerate(data):
        if value == 0:
            continue
        current_index = unmixed_data.index((i, value))
        item = unmixed_data.pop(current_index)
        new_index = (current_index + value) % len(unmixed_data)
        unmixed_data.insert(new_index, item) if new_index != 0 else unmixed_data.append(item)
    unmixed_data = [x for i, x in unmixed_data]
    start_index = unmixed_data.index(0)
    return sum([unmixed_data[(start_index+1000) % len(unmixed_data)],
                unmixed_data[(start_index+2000) % len(unmixed_data)],
                unmixed_data[(start_index+3000) % len(unmixed_data)]])


def gold(data):
    decryption_key = 811589153
    decrypted_data = [d*decryption_key for d in data]
    unmixed_data = list(enumerate(decrypted_data))

    def mix(mixed_data):
        for ind, value in enumerate(decrypted_data):
            if value == 0:
                continue
            current_index = mixed_data.index((ind, value))
            item = mixed_data.pop(current_index)
            new_index = (current_index + value) % len(mixed_data)
            mixed_data.insert(new_index, item) if new_index != 0 else mixed_data.append(item)
        return mixed_data

    for i in range(10):
        unmixed_data = mix(unmixed_data)

    unmixed_data = [x for i, x in unmixed_data]
    start_index = unmixed_data.index(0)
    return sum([unmixed_data[(start_index + 1000) % len(unmixed_data)],
                unmixed_data[(start_index + 2000) % len(unmixed_data)],
                unmixed_data[(start_index + 3000) % len(unmixed_data)]])




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

