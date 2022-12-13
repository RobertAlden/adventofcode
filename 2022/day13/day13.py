from itertools import zip_longest

with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

data = [eval(line) for line in data if line != '']
data1 = [line for line_number, line in enumerate(data) if line_number % 2 == 0]
data2 = [line for line_number, line in enumerate(data) if line_number % 2 == 1]

packets = list(zip(data1, data2))

def silver():
    def in_order(pair):
        element_pairs = zip_longest(pair[0], pair[1], fillvalue=None)
        for left, right in element_pairs:
            # Handle int, list and list, int cases and int, None cases
            match (left, right):
                case (int(), int()):
                    # Both are ints, if they are equal, check the next elements, otherwise:
                    if left == right:
                        continue
                    return left < right
                case (list(), list()):
                    # If both are lists, check if they are equal, if so continue, otherwise recurse.
                    if left == right:
                        continue
                    return in_order((left, right))
                case (int(), list()):
                    # Mismatched types, promote the int to a list.
                    return in_order(([left], right))
                case (list(), int()):
                    # Mismatched types, promote the int to a list.
                    return in_order((left, [right]))
                case (None, int()) | (None, list()):
                    # Left list ran out first, order is correct.
                    return True
            return False

    return sum([idx+1 for idx, val in enumerate([in_order(pair) for pair in packets]) if val])


def gold():
    pass


print(f'Silver: {silver()}')

# print(f'Gold: {gold()}')
