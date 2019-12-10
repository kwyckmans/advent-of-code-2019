import queue

# def search(graph, start):
#     q = queue.Queue()
#     start = (start, True)

#     while not q.empty():
#         v = q.get()
#         if v[0] == 'SAN':
#             return v
        


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

    # orbits["XQ6"]

    my_orbit = orbits["YOU"]
    santa_orbit = orbits["SAN"]

    print(len(my_orbit.difference(santa_orbit)) + len(santa_orbit.difference(my_orbit)))
    # print(orbits["XQ6"])
