from time import time_ns

with open('test.txt') as f:
    test_input = [line.strip().split(" ") for line in f.readlines()]

with open('input.txt') as f:
    real_input = [line.strip().split(" ") for line in f.readlines()]


def silver(data):
    tree = dict()
    constants = dict()
    for relationship in data:
        if len(relationship) == 2:
            # Assignment
            constants[relationship[0][:-1]] = int(relationship[1])
        elif len(relationship) == 4:
            # Expression
            tree[relationship[0][:-1]] = relationship[1:]
    while len(tree.keys()) > 0:
        for key, value in list(tree.items()):
            tree[key] = [v if v not in constants else constants[v] for v in value]  # replace constant names with values
        constants.clear()
        for varname, expression in list(tree.items()):
            match expression:
                case int() as A, str() as op, int() as B:
                    # produce new constants by evaluating complete expressions
                    constants[varname] = eval(f"int({A}{op}{B})")
                    del tree[varname]
    return list(constants.values()).pop()


def gold(data):
    tree = dict()
    constants = dict()
    lut = [(value[0][:-1], value[1:]) for value in data]
    for name, value in lut:
        if len(value) == 1:
            constants[name] = int(value[0])
        else:
            if name == 'root':
                tree['root'] = value[0], '==', value[2]
            else:
                tree[name] = value
    del constants['humn']

    while len(tree.keys()) > 0:
        before = list(tree.items())
        for key, value in list(tree.items()):
            tree[key] = [v if v not in constants else constants[v] for v in value]  # replace constant names with values
        constants.clear()
        for varname, expression in list(tree.items()):
            match expression:
                case int() as A, str() as op, int() as B:
                    # produce new constants by evaluating complete expressions
                    constants[varname] = eval(f"int({A}{op}{B})")
                    del tree[varname]
        after = list(tree.items())
        if before == after:
            break
    while len(tree.keys()) > 1:
        a, _, c = tree['root']
        _a, operator, _c = None, None, None
        value = None
        if (isinstance(a, str)) and (isinstance(c, int)):  # e.g. 'aaaa' == 25
            _a, operator, _c = tree[a]
            del tree[a]
            value = c
        elif (isinstance(c, str)) and (isinstance(a, int)):  # e.g. 25 == 'aaaa'
            _a, operator, _c = tree[c]
            del tree[c]
            value = a
        ops = {'+': '-', '-': '+', '*': '/', '/': '*'}
        operator = ops[operator]  # get inverse of operation
        res = ""
        if (isinstance(_a, str)) and (isinstance(_c, int)):  # tree['aaaa'] = 'bbbb' * 5
            res = f'int({value}{operator}{_c})'
            tree['root'] = _a, '==', eval(res)
        elif (isinstance(_c, str)) and (isinstance(_a, int)):  # tree['aaaa'] = 5 * 'bbbb'
            if operator == '+':  # Because - isn't commutative
                res = f'int(-({value}{ops[operator]}{_a}))'  # Do the commutative inverse instead
            elif operator == '*':   # Because / isn't commutative
                res = f'int(1/({value}{ops[operator]}{_a}))'  # Do the commutative inverse instead
            else:
                res = f'int({value}{operator}{_a})'
            tree['root'] = _c, '==', eval(res)
    return tree['root'][2]



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
