DIAGRAM = [["." for _ in range(0, 11)] for _ in range(0, 11)]

LOCATIONS = {}
CROSSINGS = []


def swap(a, b):
    temp = a
    a = b
    b = temp


def draw_wire(icon="o"):
    for location in LOCATIONS:
        print(f"Drawing wire for location {location}")
        start, end = location
        start_x, start_y = start
        end_x, end_y = end

        print(start_x, start_y, end_x, end_y)
        # if start_x > end_x: swap(start_x, start_y)
        # if start_y > end_y: swap(start_y, end_y)

        for x in range(start_x, end_x):
            for y in range(start_y, end_y):
                print("Setting {x},{y}")
                DIAGRAM[y][x] = icon


def plot_wire(directions, wire, marker="x"):
    LOCATIONS[wire] = []

    port = (1, 1)
    loc = port

    DIRS = directions.split(",")

    direction, value = "R", 0
    for instruction in DIRS:
        print(f"At location {loc}")

        direction = instruction[0]
        val = int(instruction[1:])

        print(f"direction {direction}, value {val}")

        if direction == "R":
            start = loc[0]
            end = loc[0] + val

            LOCATIONS[wire].append(((start, loc[1]), (end, loc[1])))

            loc = (end, loc[1])

        elif direction == "U":
            start = loc[1]
            end = loc[1] + val
            LOCATIONS[wire].append(((loc[0], start), (loc[0], end)))

            loc = (loc[0], end)

        elif direction == "L":
            start = loc[0]
            end = loc[0] - val
            LOCATIONS[wire].append(((start, loc[1]), (end, loc[1])))

            loc = (end, loc[1])

        elif direction == "D":
            start = loc[1]
            end = loc[1] - val
            LOCATIONS[wire].append(((loc[0], start), (loc[0], end)))

            loc = (loc[0], end)

        else:
            raise Exception("Impossible direction!", direction)


if __name__ == "__main__":
    with open("day-three.txt", "r") as f:
        WIRES = [line for line in f]

    plot_wire(WIRES[0], "first")
    plot_wire(WIRES[1], "second")

    for wire in LOCATIONS:
        for location in LOCATIONS[wire]:
            print(location)

        print(f"{wire} finished")
