with open("input.txt") as f:
	data = f.read().split(',')
program_data = [int(i) for i in data]

def execute(prog,inp={},debug=False):
	program = prog[:]
	if inp != {}:
		for i in inp.items():
			program[i[0]] = i[1]
	p = 0
	while program[p] != 99:
		opcode = program[p]
		if opcode == 1: # Add then store
			args = program[p+1:p+4]
			a = program[args[0]]
			b = program[args[1]]
			dest = args[2]
			if debug:
				print(f'Adding {a} + {b}, stored in pos:{dest}')
			program[dest] = a+b
			p += 4
		elif opcode == 2: # Multiply then store
			args = program[p+1:p+4]
			a = program[args[0]]
			b = program[args[1]]
			dest = args[2]
			if debug:
				print(f'Multiplying {a} + {b}, stored in pos:{dest}')
			program[dest] = a*b
			p += 4
		else:
			p+=4

	return program

for i in range(0,99):
	for k in range(0,99):
		try:
			output = execute(program_data,{1:i,2:k})
			if output[0] == 19690720:
				print(100*i+k)
		except IndexError:
			pass
