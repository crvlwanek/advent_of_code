from collections import deque, Counter

with open("input.txt") as file:
    guardMap = [list(line.strip()) for line in file.readlines()]

guardChars = { 
    "V": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
}

def isInBounds(i, j):
    return 0 <= i < len(guardMap) and 0 <= j < len(guardMap[i])

def rotate(guard):
    match guard:
        case ">": return "V"
        case "V": return "<"
        case "<": return "^"
        case "^": return ">"
        case _: raise Exception(f"Invalid guard: {guard}")

def findGuard():

    for i, row in enumerate(guardMap):
        for j, char in enumerate(row):
            if char in guardChars:
                return (i, j)
            
    raise Exception("Guard not found...")

def part1():

    i, j = findGuard()
    explored = set()

    explored.add((i, j))
    while isInBounds(i, j):
        guard = guardMap[i][j]
        di, dj = guardChars[guard]
        i2 = i + di
        j2 = j + dj
        if not isInBounds(i2, j2):
            break
        
        if guardMap[i2][j2] == "#":
            guard = guardMap[i][j] = rotate(guard)
        else:
            guardMap[i][j] = "."
            guardMap[i2][j2] = guard
            explored.add((i2, j2))
            i = i2
            j = j2

    print(len(explored))
    
    
def part2():

    def addIfInBounds(newObstacles, l1, l2):
        if isInBounds(l1, l2):
            newObstacles.add((l1, l2))

    i, j = findGuard()
    explored = set()
    obstaclesEncountered = set()

    explored.add((i, j))
    while isInBounds(i, j):
        guard = guardMap[i][j]
        di, dj = guardChars[guard]
        i2 = i + di
        j2 = j + dj
        if not isInBounds(i2, j2):
            break
        
        if guardMap[i2][j2] == "#":
            obstaclesEncountered.add((i, j))
            guard = guardMap[i][j] = rotate(guard)
        else:
            guardMap[i][j] = "."
            guardMap[i2][j2] = guard
            explored.add((i2, j2))
            i = i2
            j = j2

    obstacles = list(obstaclesEncountered)
    newObstacles = set()
    for i, (i1, i2) in enumerate(obstacles):
        for j, (j1, j2) in enumerate(obstacles):
            for k, (k1, k2) in enumerate(obstacles):

                if i == j or j == k or i == k:
                    continue

                if i1 + 1 == j1 and j2 - 1 == k2:
                    l1, l2 = k1 - 1, i2 - 1
                    addIfInBounds(newObstacles, l1, l2)

                if i2 - 1 == j2 and j1 + 1 == k1:
                    l1, l2 = i1 + 1, k2 - 1
                    addIfInBounds(newObstacles, l1, l2)

                if i1 - 1 == j1 and j2 + 1 == k2:
                    l1, l2 = k1 + 1, i2 + 1
                    addIfInBounds(newObstacles, l1, l2)

                if i2 - 1 == j2 and j1 - 1 == k1:
                    l1, l2 = i1 - 1, k2 + 1
                    addIfInBounds(newObstacles, l1, l2)

    print(len(newObstacles))

def part2alt():

    directions = deque([
        (1, 0),
        (0, -1),
        (-1, 0),
        (0, 1),
    ])

    i, j = findGuard()
    explored = set()
    obstaclesEncountered = set()

    explored.add((i, j))
    while isInBounds(i, j):
        guard = guardMap[i][j]
        di, dj = guardChars[guard]
        i2 = i + di
        j2 = j + dj
        if not isInBounds(i2, j2):
            break
        
        if guardMap[i2][j2] == "#":
            obstaclesEncountered.add((i, j))
            guard = guardMap[i][j] = rotate(guard)
        else:
            guardMap[i][j] = "."
            guardMap[i2][j2] = guard
            explored.add((i2, j2))
            i = i2
            j = j2

    def check(obs: set, directions, i1, i2, j1, j2, k1, k2):
        i1 += directions[0][0]
        i2 += directions[0][1]
        j1 += directions[1][0]
        j2 += directions[1][1]
        k1 += directions[2][0]
        k2 += directions[2][1]

        yCounter = Counter(i1, j1, k1)
        xCounter = Counter(i2, j2, k2)

        if len(yCounter) == 2 and len(xCounter) == 2:
            for k, v in yCounter.items():
                if v == 1:
                    l1 = k

            for k, v in xCounter.items():
                if v == 1:
                    l2 = k

            l1 += directions[3][0]
            l2 += directions[3][1]
            if isInBounds(l1, l2):
                obs.add((l1 + l2))

    obstacles = list(obstaclesEncountered)
    newObstacles = set()
    for i, (i1, i2) in enumerate(obstacles):
        for j, (j1, j2) in enumerate(obstacles):
            for k, (k1, k2) in enumerate(obstacles):

                if i == j or j == k or i == k:
                    continue

                for _ in range(4):
                    check(newObstacles, directions, i1, i2, j1, j2, k1, k2)
                    directions.rotate()

    print(len(newObstacles))

part2()