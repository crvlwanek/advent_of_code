from collections import Counter

with open("input.txt") as file:
    lines = file.readlines()


def part1():
    firstLocations, secondLocations = zip(*[line.split() for line in lines])

    firstLocations = sorted(list(firstLocations))
    secondLocations = sorted(list(secondLocations))

    total = 0
    for locationA, locationB in zip(firstLocations, secondLocations):
        total += abs(int(locationA) - int(locationB))

    print(total)


def part2():
    firstLocations, secondLocations = zip(*[line.split() for line in lines])

    counts = Counter(secondLocations)

    total = sum(counts.get(location, 0) * int(location) for location in firstLocations)
    print(total)


part2()