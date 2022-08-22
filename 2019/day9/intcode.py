from random import choice

class IntCodeUnit:
    def __init__(self,program,name=None,debug=False,verbose=False,*,inputData):
        self.program = program+[0]*1000
        self.p = 0
        self.relative_base = 0
        if inputData != None:
            self.input_buffer = inputData
        else: 
            self.input_buffer = []

        self.outputUnits = []
        self.output_buffer = []
        self.interrupt = 0
        self.jump = False
        self.debug = debug
        self.name = ""
        self.timeout = 1000000
        self.t_flag = False
        if name != None:
            self.name = name
        else:
            vowels = list("aaeeiioouuy")
            consonents = list("bcdfghjklmnpqrstvwxyz")
            numbers = list("0123456789")
            self.name += choice(list(set(vowels)) + consonents).upper()

            for i in range(2):
                self.name += choice(vowels)
                self.name += choice(consonents)

            for i in range(3):
                self.name += choice(numbers)

        self.verbose = verbose
        if self.verbose:
            print(f"{self.name}: Initialized.")

    def add(self,a,b,c):
        if self.debug:
            print(f'adding {a} to {b} and storing @ {c}')
        self.program[c] = a + b

    def mult(self,a,b,c):
        if self.debug:
            print(f'multiplying {a} and {b} and storing @ {c}')
        self.program[c] = a * b

    def getInput(self,a):
        if len(self.input_buffer) > 0:
            self.program[a] = self.input_buffer.pop(0)
            self.t_flag = False
            if self.debug:
                print(f'getting {self.program[a]} from input')
        else:
            if self.timeout > 0:
                self.timeout -= 1
                self.t_flag = True
            else:
                self.interrupt = -1

    def setOutput(self,d):
        data = d
        if len(self.outputUnits) > 0:
            for a in self.outputUnits:
                if isinstance(a, IntCodeUnit):
                    if self.verbose:
                        print(f"{self.name} says to {a.name}: {data}")
                    a.input_buffer += [data]
                elif isinstance(a, list):
                    if self.verbose:
                        print(f"{self.name} records: {data}")
                    a += [data]
        else:
            if self.verbose:
                print(f"{self.name} says: {data}")
            self.output_buffer += [data]

    def jumpIfTrue(self,a,b):
        if a != 0:
            self.p = b
            self.jump = True
            if self.debug:
                print(f'jumping to instruction {b}')
        else:
            if self.debug:
                print("not jumping")

    def jumpIfFalse(self,a,b):
        if a == 0:
            self.p = b
            self.jump = True
            if self.debug:
                print(f'jumping to instruction {b}')
        else:
            if self.debug:
                print("not jumping")

    def lessThan(self,a,b,c):
        self.program[c] = int(a < b)
        if self.debug:
            print(f'comparing {a} less than {b} and storing in {c}')

    def equalTo(self,a,b,c):
        self.program[c] = int(a == b)
        if self.debug:
            print(f'comparing {a} equal to {b} and storing in {c}')

    def baseShift(self,a):
        self.relative_base += a
        if self.debug:
            print(f'relative base is now {self.relative_base}')

    def getArgs(self,n):
        fArgs = []
        t = 1
        while t <= n:
            if 0 <= self.p < len(self.program):
                fArgs += [self.program[self.p+t]]
            else:
                fArgs += [-5]
                self.interrupt = -10
            t += 1
        return fArgs

    def mutateArgs(self,a,p):
        in_args = a[:]
        out_args = []
        p = str(p)[::-1]
        while len(p) < len(a):
            p += '0'
        p=list(p)
        print(a,"".join(p))
        for ia,pa in zip(in_args,p):
            if pa == '0':
                out_args += [self.program[ia]]
            if pa == '1':
                out_args += [ia]
            if pa == '2':
                out_args += [self.program[ia+self.relative_base]]
        print(out_args,"".join(p))
        return out_args



    def halt(self, *args):
        self.interrupt = 99

    def noOp():
        pass

    def execute(self):
        if self.p > len(self.program):
            self.interrupt = -10
            return

        opcode = self.program[self.p] % 100
        params = self.program[self.p] // 100
        delta = 0
        self.jump = False
        p = self.p
        args = []

        opcodes = {
            -1:[self.noOp,0],
            1:[self.add,3],
            2:[self.mult,3],
            3:[self.getInput,1],
            4:[self.setOutput,1],
            5:[self.jumpIfTrue,2],
            6:[self.jumpIfFalse,2],
            7:[self.lessThan,3],
            8:[self.equalTo,3],
            9:[self.baseShift,1],
            99:[self.halt,0]
        }
        try:
            op = opcodes[opcode]
        except KeyError:
            self.interrupt = -50
            op = opcodes[-1]
        f = op[0]
        args = self.getArgs(op[1])
        args = self.mutateArgs(args,params)

        if self.debug:
            if not self.t_flag:
                print(f"@{self.name}:Inst {self.p}: {self.program[self.p]} - {opcode,args}")
        
        if self.interrupt == 0:
            f(*args)
        
        if not self.jump and not self.t_flag:
            delta = len(args) + 1
        self.p += delta


    def run(self):
        while(self.interrupt == 0):
            if len(self.program) > 0:
                self.execute()
            else:
                self.interrupt = -5
        match self.interrupt:
            case 99:
                if self.verbose:
                    print(f"{self.name}: HALTED (Code {self.interrupt})")
            case -1:
                print(f"{self.name}: Error: Input Timeout (Code {self.interrupt})")
            case -5:
                print(f"{self.name}: Error: No Program Loaded (Code {self.interrupt})")
            case -10:
                print(f"{self.name}: Error: Pointer out of Bounds (Code {self.interrupt})")
            case -50:
                print(f"{self.name}: Error: Instruction Not Found (Code {self.interrupt})")

            case _:
                print(f"{self.name}: Unknown Error (Code {self.interrupt})")

    def connectOutput(self,target):
        if isinstance(target, IntCodeUnit):
            self.outputUnits += [target]
        if isinstance(target, list):
            self.outputUnits += [target]


class IntCodePool:
    def __init__(self, pool=None):
        if pool == None:
            self.pool = [] 
        else:
            self.pool = pool

        self.output_pool = []


    def run(self):
        while(True):
            active = False
            for i in self.pool:
                if i.interrupt == 0:
                    i.execute()
                    active = True
            if not active:
                break


if __name__ == '__main__':
    with open("test.txt") as f:
        data = f.read().split(',')
    program_data = [int(i) for i in data]
    ICU = IntCodeUnit(program_data,inputData = [],verbose=True,debug=True)
    ICU.run()
