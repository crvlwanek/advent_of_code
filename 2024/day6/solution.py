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
        
    def findCycle():
        i, j = findGuard()
        si, sj = i, j
        explored = set()
        guard = guardMap[i][j]
        startGuard = guard

        found = False

        while isInBounds(i, j):
            guard = guardMap[i][j]
            pair = (i, j, guard)

            if pair in explored:
                guardMap[i][j] = "."
                found = True
                break

            explored.add(pair)
            
            di, dj = guardChars[guard]
            i2 = i + di
            j2 = j + dj

            if not isInBounds(i2, j2):
                guardMap[i][j] = "."
                break
            
            if guardMap[i2][j2] == "#":
                guard = guardMap[i][j] = rotate(guard)
            else:
                guardMap[i][j] = "."
                guardMap[i2][j2] = guard
                i = i2
                j = j2

        guardMap[si][sj] = startGuard
        return found

    cycles = 0
    for i, row in enumerate(guardMap):
        for j, char in enumerate(row):

            if char != ".":
                continue

            guardMap[i][j] = "#"
            if findCycle():
                cycles += 1

            guardMap[i][j] = "."

        print(i)

    print(len(guardMap) * len(guardMap[0]))
    print(cycles)

part2()