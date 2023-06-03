from intcode import IntCodeUnit

with open("input.txt") as f:
    data = f.read().split(',')
    program_data = [int(i) for i in data]

ICU = IntCodeUnit(program_data, inputData=[1],verbose=True,debug=False)
ICU.run()