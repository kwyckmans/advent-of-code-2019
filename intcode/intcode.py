from typing import List

MEMORY = {1: 1, 2: 2, 3: 3}

def multiply(a: int, b: int):
    return a * b


def add(a: int, b: int):
    return a + b


def store(a: int, location: int):
    MEMORY[location] = a


def out(a: int):
    return MEMORY[a]


operations = {}
operations[1] = add
operations[2] = multiply
operations[3] = store
operations[4] = out


class Processor:
    def __init__(self, program: List[int]):
        self._memory = program[:]
        self._pc = 0
        self._stop_code  = False

    @property
    def has_next(self):
        '''Indicates if the end of the program is reached or if the stop code flag is set
        '''
        return not self._stop_code and self._pc < len(self._memory)

    def step(self):
        '''Take one step in the processing of a loaded program.
        '''
        # TODO Add check to see if end is reached and throw exception

        op_code = self._memory[self._pc]

        if op_code == 99:
            self._stop_code = True
            return
        
        params = {}
        params["a"] = self._memory[self._pc + 1]
        params["b"] = self._memory[self._pc + 2]
        loc = self._memory[self._pc + 3]
        
        self._memory[loc] = operations[op_code](**params)

        print(f"PC at {self._pc}. Op code: {op_code} - A {params['a']} - B {params['b']} - loc {loc} - result {self._memory[loc]}")
        self._pc += 4


    def process(self, program):
        self._memory = program[:]
        instruction_pointer = 0

        while instruction_pointer < len(program):
            op_code = self._memory[instruction_pointer]

            if op_code not in [1,2,99]:
                raise Exception("Unknwon opcode")

            if op_code == 99:
                break

            params = {}
            params["a"] = self._memory[self._memory[instruction_pointer + 1]]
            params["b"] = self._memory[self._memory[instruction_pointer + 2]]
            loc = self._memory[instruction_pointer + 3]

            self._memory[loc] = operations[op_code](**params)

            instruction_pointer += 4

    def __getitem__(self, key):
        return self._memory[key]

    def __setitem__(self, key, value):
        self._memory[key] = value

class OpCode:
    def __init__(self, operation: str):
        pass


if __name__ == "__main__":
    for i in range(1, 5):
        params = {}
        if i == 1 or i == 2:
            params["a"] = 2
            params["b"] = 5
        elif i == 3:
            params["a"] = 2
            params["location"] = 5
        else:
            params["a"] = 3

        print(operations[i](**params))
