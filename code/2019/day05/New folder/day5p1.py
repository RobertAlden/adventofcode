with open("input.txt") as f:
	data = f.read().split(',')
program_data = [int(i) for i in data]



input_buffer = []
output_buffer = []
def execute(prog,inp={},debug=False):
	program = prog[:]
	if inp != {}:
		for i in inp.items():
			program[i[0]] = i[1]
	p = 0
	#Functions
	def IO_Read(pos):
		print(program[pos])

	def IO_Write():
		return 1

	# Main Loop
	while True:
		value = str(program[p])
		opcode = int(value[-2:])
		parameters = value[:-2]
		parameter_modes	= [] + list(parameters[::-1])
		args = []
		match opcode:
			case 99: #Halt
				break
			case 1: #Addition
				args = program[p+1:p+4]
				parameter_modes += ['0'] * (len(args)-len(parameter_modes))
				valueA = args[0] if parameter_modes[0] == '1' else program[args[0]]
				valueB = args[1] if parameter_modes[1] == '1' else program[args[1]]
				program[args[2]] = valueA + valueB
			case 2: #Multiply
				args = program[p+1:p+4]
				parameter_modes += ['0'] * (len(args)-len(parameter_modes))
				valueA = args[0] if parameter_modes[0] == '1' else program[args[0]]
				valueB = args[1] if parameter_modes[1] == '1' else program[args[1]]
				program[args[2]] = valueA * valueB

			case 3: #Get Input and Store
				args = [program[p+1]]
				input_value = IO_Write()
				program[args[0]] = input_value

			case 4: #Retrieve and output
				args = program[p+1:p+2]
				IO_Read(args[0])
		if debug:
			print(f'{value},{p}:{parameter_modes} {args}')
		p += len(args) + 1
	return program

execute(program_data,debug=False)