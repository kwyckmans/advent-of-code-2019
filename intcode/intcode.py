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
        return not self._stop_code and self._pc < len(self._memory)

    def step(self):
        '''Take one step in the processing of a loaded program.
        
        TODO: WIP: this is just some jumbled together code. Does not actually work yet.
        '''
        # if self._pc < len(self._memory):
        op_code = self._memory[self._pc]

        if op_code == 99:
            self._stop_code = True
            return
        
        params = {}
        params["a"] = self._memory[self._pc + 1]
        params["b"] = self._memory[self._pc + 2]
        loc = self._memory[self._pc + 3]

        
        self._memory[loc] = operations[op_code](**params)
        
        # if op_code == 1:
        #     program[loc] = program[a] + program[b]
        # elif op_code == 2:
        #     program[loc] = program[a] * program[b]
        # else:
        #     raise Exception("Unknown opcode")
        
        self._pc += 4

        # return True

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
