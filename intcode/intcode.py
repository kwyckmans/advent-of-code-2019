from typing import List

MEMORY = []


class Processor:
    def __init__(self, program: List[int]):
        # MEMORY = program[:]
        self._memory = program[:]
        self._pc = 0
        self._stop_code = False

        self.operations = {}
        self.operations[1] = [self.add, 4]
        self.operations[2] = [self.multiply, 4]
        self.operations[3] = [self.store, 2]
        self.operations[4] = [self.out, 2]

    @property
    def has_next(self):
        """Indicates if the end of the program is reached or if the stop code flag is set
        """
        return not self._stop_code and self._pc < len(self._memory)

    def step(self):
        """Take one step in the processing of a loaded program.
        """
        op_code = Opcode(str(MEMORY[self._pc]))

        if op_code.is_halt_code():
            self._stop_code = True
            return

        args = MEMORY[self._pc + 1 : self._pc + op_code.param_count]
        params = op_code.get_params(args)

        self.operations[op_code._opcode][0](**params)

        loc = params["loc"]
        print(
            f"PC at {self._pc}. Op code: {op_code} - params {params}- result {MEMORY[loc]}"
        )
        self._pc += op_code.param_count

    def process(self):
        while not self._stop_code and self._pc < len(MEMORY):
            self.step()

    def __getitem__(self, key):
        return self._memory[key]

    def __setitem__(self, key, value):
        self._memory[key] = value

    def multiply(self, a: int, b: int, loc: int):
        MEMORY[loc] = a * b

    def add(self, a: int, b: int, loc: int):
        MEMORY[loc] = a + b

    def store(self, loc: int):
        val = int(input("Please enter a value: "))
        MEMORY[loc] = val

    def out(self, loc: int):
        print(f"output: {MEMORY[loc]}")


class Instruction:
    def __init__(self):
        pass

    def execute(self, **params):
        pass


class Opcode:
    PARAM_FOR_OP = {1: 4, 2: 4, 3: 2, 4: 2, 99: 0}

    def __init__(self, operation: str):
        op = operation[-2:].strip("0")
        self._opcode = int(op)
        if len(operation) > 2:
            self._modes = operation[: len(op)]
        else:
            self._modes = None

        self.param_count = Opcode.PARAM_FOR_OP[self._opcode]

    def is_halt_code(self):
        return self._opcode == 99

    def __str__(self):
        return f"{self._opcode}"

    def get_params(self, args):
        if self._opcode == 1 or self._opcode == 2:
            return {"a": args[0], "b": args[1], "loc": args[2]}

        if self._opcode == 3 or self._opcode == 4:
            return {"loc": args[0]}


if __name__ == "__main__":
    print(" - - - - opcodes - - - -")
    op = Opcode("1")
    print(op._opcode, op._modes)
    op = Opcode("2")
    print(op._opcode, op._modes)
    op = Opcode("02")
    print(op._opcode, op._modes)
    op = Opcode("1103")
    print(op._opcode, op._modes)

    test_program = [1, 0, 00, 00, 1, 0, 0, 0, 3, 0, 4, 0, 99]
    MEMORY = test_program[:]
    proc = Processor(test_program)

    print(f"Starting at {proc._pc}")

    proc.process()

