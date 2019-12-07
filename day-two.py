PROGRAM = [
    1,
    12,
    2,
    3,
    1,
    1,
    2,
    3,
    1,
    3,
    4,
    3,
    1,
    5,
    0,
    3,
    2,
    1,
    9,
    19,
    1,
    19,
    5,
    23,
    2,
    23,
    13,
    27,
    1,
    10,
    27,
    31,
    2,
    31,
    6,
    35,
    1,
    5,
    35,
    39,
    1,
    39,
    10,
    43,
    2,
    9,
    43,
    47,
    1,
    47,
    5,
    51,
    2,
    51,
    9,
    55,
    1,
    13,
    55,
    59,
    1,
    13,
    59,
    63,
    1,
    6,
    63,
    67,
    2,
    13,
    67,
    71,
    1,
    10,
    71,
    75,
    2,
    13,
    75,
    79,
    1,
    5,
    79,
    83,
    2,
    83,
    9,
    87,
    2,
    87,
    13,
    91,
    1,
    91,
    5,
    95,
    2,
    9,
    95,
    99,
    1,
    99,
    5,
    103,
    1,
    2,
    103,
    107,
    1,
    10,
    107,
    0,
    99,
    2,
    14,
    0,
    0,
]

test = ([1,0,0,0,99],[2,0,0,0,99])
test2 = [2,3,0,3,99]
test3 = [2,4,4,5,99,0]
test4 = [1,1,1,4,99,5,6,0,99]

def process(program):
    instruction_pointer = 0

    while instruction_pointer < len(program):
        op_code = program[instruction_pointer]

        if op_code == 99:
            break

        a = program[instruction_pointer + 1]
        b = program[instruction_pointer + 2]
        loc = program[instruction_pointer + 3]

        if op_code == 1:
            program[loc] = program[a] + program[b]
        elif op_code == 2:
            program[loc] = program[a] * program[b]
        else:
            raise Exception("Unknown opcode")
        

        instruction_pointer += 4

if __name__ == "__main__":
    memory = PROGRAM[:]
    
    process(memory)
    print(f"Result: {memory[0]}")
    print(f"Validate: {PROGRAM[0]}")

    for noun in range(0,100):
        for verb in range(0,100):
            memory = PROGRAM[:]
            memory[1] = noun
            memory[2] = verb
            process(memory)

            if memory[0] == 19690720:
                print(f"noun: {noun} , verb: {verb}, answer: {100 * noun + verb}")
                break
