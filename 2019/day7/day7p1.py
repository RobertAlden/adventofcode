from intcode import IntCodeUnit
from itertools import permutations



with open("input.txt") as f:
    data = f.read().split(',')
    program_data = [int(i) for i in data]


phase_setting = [0,1,2,3,4]
Pps = list(permutations(phase_setting))
output = []
for ps in Pps:
    A = IntCodeUnit(program_data,name="A",inputData=[ps[0],0])
    B = IntCodeUnit(program_data,name="B",inputData=[ps[1]])
    C = IntCodeUnit(program_data,name="C",inputData=[ps[2]])
    D = IntCodeUnit(program_data,name="D",inputData=[ps[3]])
    E = IntCodeUnit(program_data,name="E",inputData=[ps[4]])

    A.connectOutput(B)
    B.connectOutput(C)
    C.connectOutput(D)
    D.connectOutput(E)
    
    A.run()
    B.run()
    C.run()
    D.run()
    E.run()
    output += E.output_buffer
print(max(output))