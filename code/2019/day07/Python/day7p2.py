from intcode import IntCodeUnit, IntCodePool
from itertools import permutations



with open("input.txt") as f:
    data = f.read().split(',')
    program_data = [int(i) for i in data]


phase_setting = [5,6,7,8,9]
Pps = list(permutations(phase_setting))
all_output = []
for ps in Pps:
    output = []

    A = IntCodeUnit(program_data[:],name="A", inputData=[ps[0],0])
    B = IntCodeUnit(program_data[:],name="B", inputData=[ps[1]])
    C = IntCodeUnit(program_data[:],name="C", inputData=[ps[2]])
    D = IntCodeUnit(program_data[:],name="D", inputData=[ps[3]])
    E = IntCodeUnit(program_data[:],name="E", inputData=[ps[4]])

    A.connectOutput(B)
    B.connectOutput(C)
    C.connectOutput(D)
    D.connectOutput(E)
    E.connectOutput(A)
    E.connectOutput(output)

    Pool = IntCodePool(pool=[A,B,C,D,E])
    Pool.run()

    all_output.append(max(output))
print(max(all_output))