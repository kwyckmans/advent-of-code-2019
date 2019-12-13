from typing import List

class Processor:

    def __init__(self, program: List[int]):
        self._memory = program[:]
        print(f"Loaded {self._memory}")

        self._pc = 0
        self._stop_code = False

        self.operations = {}
        self.operations[1] = [self.add, 4]
        self.operations[2] = [self.multiply, 4]
        self.operations[3] = [self.store, 2]
        self.operations[4] = [self.out, 2]
        self.operations[5] = [self.jump_if_true, 3]
        self.operations[6] = [self.jump_if_false, 3]
        self.operations[7] = [self.less_than, 4]
        self.operations[8] = [self.equals, 4]

        self.wait_for_input = False

        self.output = []
        self.input = []

    def reset(self):
        self._stop_code = False
        self._pc = 0

    @property
    def has_next(self):
        """Indicates if the end of the program is reached or if the stop code flag is set
        """
        return not self._stop_code and self._pc < len(self._memory)

    def step_local_mem(self):
        op_code = Opcode(str(self._memory[self._pc]), self._memory)

        if op_code.is_halt_code():
            self._stop_code = True
            return

        args = self._memory[self._pc + 1 : self._pc + op_code.param_count]
        params = op_code.get_params(args)
        print(
            f"PC at {self._pc}. Op code: {op_code} - arguments {args} - params {params}"
        )


        if not self.wait_for_input:
            pc_modified = self.operations[op_code._opcode][0](**params)

            debug = ""
            for i in range(len(self._memory)):
                debug += f"{i}: {self._memory[i]}, "

            print(debug)

            if not pc_modified:
                self._pc += op_code.param_count

        print(f"Next PC {self._pc}")


    # def step(self):
    #     """Take one step in the processing of a loaded program.
    #     """

    #     op_code = Opcode(str(MEMORY[self._pc]))

    #     if op_code.is_halt_code():
    #         self._stop_code = True
    #         return

    #     args = MEMORY[self._pc + 1 : self._pc + op_code.param_count]
    #     params = op_code.get_params(args)
    #     print(
    #         f"PC at {self._pc}. Op code: {op_code} - arguments {args} - params {params}"
    #     )

    #     if not self.wait_for_input:
    #         pc_modified = self.operations[op_code._opcode][0](**params)

    #         if not pc_modified:
    #             self._pc += op_code.param_count

    #     print(f"Next PC {self._pc}")

    def process(self):
        print(f"Instructions in memory: {len(self._memory)}")
        while not self._stop_code and self._pc < len(self._memory) and not self.wait_for_input:
            self.step_local_mem()

    def __getitem__(self, key):
        return self._memory[key]

    def __setitem__(self, key, value):
        self._memory[key] = value

    def multiply(self, a: int, b: int, loc: int):
        self._memory[loc] = a * b

    def add(self, a: int, b: int, loc: int):
        self._memory[loc] = a + b

    def store(self, loc: int):
        # val = int(input())        
        if not self.input:
            print(f"Waiting for inputs...")
            self.wait_for_input = True
        else:
            val = self.input.pop(0)
            print(f"read {val} from input queue")
            self._memory[loc] = val

    def out(self, loc: int):
        self.output.append(loc)
        print(f"- - - OUTPUT: {loc} - - -")

    def jump_if_false(self, a, b):
        if a == 0:
            self._pc = b
            return True
        # else:
        #     self._pc += 2

    def jump_if_true(self, a, b):
        if a > 0:
            self._pc = b
            return True
        # else:
        #     self._pc += 2

    def less_than(self, a, b, loc):
        if a < b:
            self._memory[loc] = 1
        else:
            self._memory[loc] = 0

    def equals(self, a, b, loc):
        if a == b:
            self._memory[loc] = 1
        else:
            self._memory[loc] = 0


class Instruction:
    def __init__(self):
        pass

    def execute(self, **params):
        pass


class Opcode:
    PARAM_FOR_OP = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 99: 0}

    def __init__(self, operation: str, memory: List):
        self._memory = memory
        mode, op = operation[:-2], operation[-2:]
        self._opcode = int(op)

        # print("m",mode, "o", op)
        if mode is not None:
            # print(op, operation[: len(op) -1])
            self._modes = mode.zfill(3)
        else:
            self._modes = "000"

        self.param_count = Opcode.PARAM_FOR_OP[self._opcode]

    def is_halt_code(self):
        return self._opcode == 99

    def __str__(self):
        return f"{self._opcode} - {self._modes}"

    def get_params(self, args):
        params = {}
        # TODO: store param names with the functions, so I can loop here instead of the if/else
        if (
            self._opcode == 1
            or self._opcode == 2
            or self._opcode == 7
            or self._opcode == 8
        ):
            if self._modes[2] == "0":
                print(f"param is arg {args[0]}. Memory contents: {self._memory[args[0]]}")
                params["a"] = self._memory[args[0]]
            else:
                params["a"] = args[0]

            if self._modes[1] == "0":
                print(f"param is {self._memory[args[0]]}")
                params["b"] = self._memory[args[1]]
            else:
                params["b"] = args[1]

            params["loc"] = args[2]

            return params

        if self._opcode == 3:
            return {"loc": args[0]}

        if self._opcode == 4:
            if self._modes[2] == "0":
                print(
                    f"opcode 4 in positional mode, with argument {args[0]}, memory contains {self._memory[args[0]]}"
                )
                return {"loc": self._memory[args[0]]}
            else:
                return {"loc": args[0]}

        if self._opcode == 5 or self._opcode == 6:
            if self._modes[2] == "0":
                params["a"] =  self._memory[args[0]]
            else:
                params["a"] = args[0]
            
            if self._modes[1] == "0":
                params["b"] =  self._memory[args[1]]
            else:
                params["b"] = args[1]
            
            return params

class Amplifier(Processor):
    def __init__(self, name: str, program: List, next: "Amplifier", phase: int):
        super().__init__(program)
        self.next = next
        self.input.append(phase)
        self._name = name

    def process_pipeline(self):
        if not self._stop_code:
            self.process()

            if self.wait_for_input:
                print(f"Giving control to {self.next._name}")
                self.next.process()

    def out(self, loc:int):
        self.output.append(loc)
        self.next.input.append(loc)
        print(f" ~OUTPUT: {loc} ~")

        
def test_amplifiers():
    print("- - - TESTING AMPLIFIERS - - - ")
    program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

    E = Amplifier("E", program, None, 5)
    D = Amplifier("D", program, E, 6)
    C = Amplifier("C", program, D, 7)
    B = Amplifier("B", program, C, 8)
    A = Amplifier("A", program, B, 9)

    E.next = A

    A.input.append(0)
    A.process_pipeline()
    print(A.output.pop())

if __name__ == "__main__":
    print(" - - - - opcodes - - - -")
    # op = Opcode("1")
    # print(op._opcode, op._modes)
    # op = Opcode("2")
    # print(op._opcode, op._modes)
    # op = Opcode("02")
    # print(op._opcode, op._modes)
    # op = Opcode("1103")
    # print(op._opcode, op._modes)

    # op = Opcode("1002")
    # print(op._opcode, op._modes)

    # op = Opcode("104")
    # print(op._opcode, op._modes)
    # test_program = [11101, 5, 5, 0, 11101, 10, 2, 0, 3, 5, 4, 5, 99]
    # MEMORY = test_program[:]
    # proc = Processor([11101, 5, 5, 0, 11101, 10, 2, 0, 3, 5, 4, 5, 99])

    # print(f"Starting at {proc._pc}")
    # proc.input.append(2)
    # proc.process()


    # proc = Processor([1,2,2,0,99])
    # proc.process()
    # print(proc._memory)

    # proc = Processor([2,3,2,3,99])
    # proc.process()
    # print(proc._memory)

    # proc = Processor([1,2,2,0,2,0,2,0,99])
    # proc.process()
    # print(proc._memory)

    

    # MEMORY = [1002, 4, 3, 4, 33]
    # proc = Processor([])
    # proc.process()

    # print("Immediate mode - ouput 1 if not equal to 0")
    # MEMORY = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    # proc = Processor([])
    # proc.process()

    # print("Position mode - ouput 1 if not equal to 0")
    # proc.reset()
    # MEMORY = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    # proc = Processor([])
    # proc.process()

    # print("Position mode - ouput 1 if equal to 8")
    # proc.reset()
    # MEMORY = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    # proc.process()

    # print("Position mode - ouput 1 if less than 8")
    # proc.reset()
    # MEMORY = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    # proc.process()

    # print("Immediate mode - ouput 1 if equal to 8")
    # proc.reset()
    # MEMORY = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    # proc.process()

    # print("Immediate mode - ouput 1 if less than 8")
    # proc.reset()
    # MEMORY = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    # proc.process()

    # MEMORY = [
    #     3, 21,
    #     1008, 21, 8, 20,
    #     1005, 20, 22,
    #     107, 8, 21, 20,
    #     1006, 20, 31, 
    #     1106, 0, 36,
    #     98, 0, 0, 1002,
    #     21, 125, 20, 4,
    #     20,
    #     1105,
    #     1,
    #     46,
    #     104,
    #     999,
    #     1105,
    #     1,
    #     46,
    #     1101,
    #     1000,
    #     1,
    #     20,
    #     4,
    #     20,
    #     1105,
    #     1,
    #     46,
    #     98,
    #     99,
    # ]
    # print("Larger test: 999 if < 8, 1000 if = 8, 1001 if > 8")
    # proc.reset()
    # proc.process()

    test_amplifiers()
