import math

POINTS = {}
POINTS["first"] = set()
POINTS["second"] = set()


LOCATIONS = {}
LOCATIONS["first"] = {}
LOCATIONS["second"] = {}


class Location:
    def __init__(self, x, y, steps):
        self._x = x
        self._y = y
        self._steps = steps

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def steps(self):
        return self._steps

    def __eq__(self, other):
        if isinstance(other, Location):
            return self.x == other.x and self.y == other.y

        return NotImplemented

    def __str__(self):
        return f"({self.x}, {self.y} after {self.steps} steps)"

    def __key(self):
        return (self.x, self.y)

    def __hash__(self):
        return hash(self.__key())


def manhattan_distance(location):
    return abs(location[0] - 1) + abs(location[1] - 1)


def plot_wire(directions, wire, marker="x"):
    port = (1, 1)
    loc = port

    DIRS = directions.split(",")

    direction, value = "R", 0
    steps = 1
    for instruction in DIRS:

        direction = instruction[0]
        val = int(instruction[1:])
        if direction == "R":
            start = loc[0]
            end = loc[0] + val
            y = loc[1]

            for i in range(start + 1, end + 1):
                POINTS[wire].add((i, y))
                LOCATIONS[wire][(i, y)] = steps
                steps += 1

            loc = (end, loc[1])

        elif direction == "U":
            start = loc[1]
            end = loc[1] + val
            x = loc[0]

            for i in range(start + 1, end + 1):
                POINTS[wire].add((x, i))
                LOCATIONS[wire][(x, i)] = steps

                steps += 1

            loc = (loc[0], end)

        elif direction == "L":
            start = loc[0]
            end = loc[0] - val
            y = loc[1]

            for i in range(start - 1, end - 1, -1):
                POINTS[wire].add((i, y))
                LOCATIONS[wire][(i, y)] = steps

                steps += 1

            loc = (end, loc[1])

        elif direction == "D":
            start = loc[1]
            end = loc[1] - val
            x = loc[0]

            for i in range(start - 1, end - 1, -1):
                POINTS[wire].add((x, i))
                LOCATIONS[wire][(x, i)] = steps

                steps += 1

            loc = (loc[0], end)

        else:
            raise Exception("Impossible direction!", direction)


if __name__ == "__main__":
    with open("day-three.txt", "r") as f:
        WIRES = [line for line in f]

    print(f"Processing instructions: {WIRES[0]}")
    plot_wire(WIRES[0], "first")
    print(f"Processing instructions: {WIRES[1]}")

    plot_wire(WIRES[1], "second")

    distances = map(
        lambda loc: manhattan_distance(loc),
        POINTS["first"].intersection(POINTS["second"]),
    )

    print(f"Minimum distance is: {min(distances)}")

    intersection_steps = []
    for loc in LOCATIONS["first"]:
        if loc in LOCATIONS["second"]:
            intersection_steps.append(
                LOCATIONS["first"][loc] + LOCATIONS["second"][loc]
            )

    print(f"Minimum number of steps: {min(intersection_steps)}")
