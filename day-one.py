def calculate_fuel(mass, total = 0):
    weight_left = (mass//3)-2

    if weight_left <= 0:
        return total
    else:
        return calculate_fuel(weight_left, total + weight_left)

if __name__ == "__main__":
    vals = []

    assert calculate_fuel(1969) == 966
    assert calculate_fuel(100756) == 50346

    with open("day-one.txt", "r") as f:
        vals = [int(line) for line in f]
    
    print(f"Part one: {sum(map(lambda i: (i//3) - 2, vals))}")
    print(f"Part two: {sum(map(calculate_fuel, vals))}")

