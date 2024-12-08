from collections import defaultdict

with open("input.txt") as file:
    nodeMap = [line.strip() for line in file.readlines()]

def isInBounds(i, j):
    return 0 <= i < len(nodeMap) and 0 <= j < len(nodeMap[i])

def part1():
    freqs = defaultdict(list)

    for i, row in enumerate(nodeMap):
        for j, char in enumerate(row):

            if char == "." or char == "#":
                continue

            freqs[char].append((i, j))

    antinodes = set()
    for _, v in freqs.items():

        for i, (i1, i2) in enumerate(v):
            for j, (j1, j2) in enumerate(v[i+1:], start=i+1):

                d1 = i1 - j1
                d2 = i2 - j2

                k1, k2 = i1 + d1, i2 + d2
                if isInBounds(k1, k2):
                    antinodes.add((k1, k2))

                k1, k2 = j1 - d1, j2 - d2
                if isInBounds(k1, k2):
                    antinodes.add((k1, k2))

    print(len(antinodes))

def part2():
    freqs = defaultdict(list)

    for i, row in enumerate(nodeMap):
        for j, char in enumerate(row):

            if char == "." or char == "#":
                continue

            freqs[char].append((i, j))

    antinodes = set()
    for _, v in freqs.items():

        for i, (i1, i2) in enumerate(v):
            for j, (j1, j2) in enumerate(v[i+1:], start=i+1):

                d1 = i1 - j1
                d2 = i2 - j2

                antinodes.add((i1, i2))
                antinodes.add((j1, j2))

                while not (d1 / 2 != d1 // 2 or d2 / 2 != d2 // 2):
                    d1 //= 2
                    d2 //= 2

            
                k1, k2 = i1 + d1, i2 + d2
                while isInBounds(k1, k2):
                    antinodes.add((k1, k2))
                    k1 += d1
                    k2 += d2

                k1, k2 = i1 - d1, i2 - d2
                while isInBounds(k1, k2):
                    antinodes.add((k1, k2))
                    k1 -= d1
                    k2 -= d2


    print(len(antinodes))
                
 
part2()