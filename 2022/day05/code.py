with open('input.txt') as f:
	data = [line for line in f.readlines()]
i = data.index('\n')
stacks, instructions = data[:i], data[i + 1:]

# Parse the layout input into a list of strings where a string represents a stack of boxes
num_of_stacks = max([int(n) for n in stacks[-1].split()])  # Conveniently has the number of stacks
stacks = [row[1::4] for row in stacks[:-1]]
stacks = ["".join([r[i] for r in stacks]).strip() for i in range(num_of_stacks)]

# Parse out our information for moves
instructions = [[int(n) for n in s.split()[1::2]] for s in instructions]

for inst in instructions:
	n, src, dst = inst[0], inst[1]-1, inst[2]-1
	selection = stacks[src][:n]
	stacks[src] = stacks[src][n:]
	stacks[dst] = selection[::-1] + stacks[dst]

result = "".join([s[0] for s in stacks])
print(result)
