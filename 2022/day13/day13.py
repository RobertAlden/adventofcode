from itertools import zip_longest, pairwise

with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

data = [eval(line) for line in data if line != '']
packets = list(zip(data[::2], data[1::2]))


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
                if (result := in_order((left, right))) is not None:
                    return result
                continue
            case (int(), list()):
                # Mismatched types, promote the int to a list.
                if (result := in_order(([[left]], [right]))) is not None:
                    return result
                continue
            case (list(), int()):
                # Mismatched types, promote the int to a list.
                if (result := in_order(([left], [[right]]))) is not None:
                    return result
                continue
            case (None, int()) | (None, list()):
                # Left list ran out first, order is correct.
                return True
        return False


def silver():
    return sum([idx+1 for idx, val in enumerate([in_order(pair) for pair in packets]) if val])


def gold():
    global data
    data += [[[2]], [[6]]]
    while not all(is_sorted := [in_order(pair) for pair in pairwise(data)]):
        for i, ordered in enumerate(is_sorted):
            (data[i], data[i + 1]) = (data[i + 1], data[i]) if not ordered else (data[i], data[i + 1])
    return (data.index([[2]])+1) * (data.index([[6]])+1)


print(f'Silver: {silver()}')

print(f'Gold: {gold()}')
