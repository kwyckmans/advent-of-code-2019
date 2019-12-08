if __name__ == "__main__":
    orbits = {}

    data = ""
    with open("day6/day-six.txt", "r") as f:
        for line in f:
            data += line

    for line in data.split("\n"):
        print(line)
        orbitee, orbiter = tuple(line.split(")"))
        print(f"{orbiter} orbits {orbitee}")
        
        result = orbits.get(orbitee, set()).union({orbitee})
        for orbit in orbits:
            if orbiter in orbits[orbit]:
                orbits[orbit] = orbits[orbit].union(result)

        orbits[orbiter] = result

        print(f"{orbits[orbiter]}")
        # orbits[orbiter] = orbits.get(orbitee, []) + [orbitee]


    total = 0
    for orbit in orbits:
        # print(f"Direct and inderict orbits for {orbit}: {len(orbits[orbit   ])}")
        total += len(orbits[orbit])

    print(total)
    print(orbits["XQ6"])
