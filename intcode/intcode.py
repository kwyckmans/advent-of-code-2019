MEMORY = {1: 1, 2: 2, 3: 3}


def multiply(a: int, b: int):
    print("multiplying")
    return a * b


def add(a: int, b: int):
    print("adding")
    return a + b


def store(a: int, location: int):
    print("Storing")
    MEMORY[location] = a


def out(a: int):
    print("outputting")
    return MEMORY[a]


operations = {}
operations[1] = add
operations[2] = multiply
operations[3] = store
operations[4] = out


class Processor:
    def __init__(self):
        self._memory = {}

    def process(self, program: str):
        pass


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
