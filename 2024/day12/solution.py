with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

DOWN = (1, 0)
UP = (-1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)


directions = (
    DOWN,
    UP,
    RIGHT,
    LEFT
)

def directionToString(direction):

    if direction == DOWN:
        return "down"
    if direction == RIGHT:
        return "right"
    if direction == UP:
        return "up"
    if direction == LEFT:
        return "left"

    raise Exception("you screwed up: " + direction)

def part1():
    visited = set()

    def dfs(i, j, char):

        if not 0 <= i < len(lines) or not 0 <= j < len(lines):
            return (0, 0)

        if (i, j) in visited:
            return (0, 0)
        
        if lines[i][j] != char:
            return (0, 0)
        
        visited.add((i, j))

        perimeter, area = 0, 1

        for di, dj in directions:

            i2, j2 = i + di, j + dj

            if not 0 <= i2 < len(lines) or not 0 <= j2 < len(lines) or lines[i2][j2] != char:
                perimeter += 1

            a, b = dfs(i2, j2, char)

            perimeter += a
            area += b

        return perimeter, area

    total = 0
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            perimeter, area = dfs(i, j, char)
            if area and perimeter:
                print(char, perimeter, area)
            total += perimeter * area

    print(total)

def part2():
    
    visited = set()
    consideredSides = set()

    def explore(i, j, eDirection, sideDirection):
        di, dj = eDirection
        char = lines[i][j]
        si, sj = sideDirection

        i2, j2 = i + di, j + dj
        while 0 <= i2 < len(lines) and 0 <= j2 < len(lines) and lines[i2][j2] == char:
            i3, j3 = i2 + si, j2 + sj
            if not (not 0 <= i3 < len(lines) or not 0 <= j3 < len(lines) or lines[i3][j3] != char):
                break
            
            consideredSides.add((sideDirection, i2, j2))
            i2 += di
            j2 += dj


    def dfs(i, j, char):
        
        if not 0 <= i < len(lines) or not 0 <= j < len(lines):
            return 0, 0

        if (i, j) in visited:
            return 0, 0
        
        if lines[i][j] != char:
            return 0, 0
        
        visited.add((i, j))

        area = 1
        sides = 0

        for direction in directions:

            di, dj = direction
            i2, j2 = i + di, j + dj

            if not 0 <= i2 < len(lines) or not 0 <= j2 < len(lines) or lines[i2][j2] != char:

                if (direction, i, j) not in consideredSides:

                    sides += 1
                    consideredSides.add((direction, i, j))

                    if direction == LEFT or direction == RIGHT:
                        explore(i, j, UP, direction)
                        explore(i, j, DOWN, direction)
                    else:
                        explore(i, j, LEFT, direction)
                        explore(i, j, RIGHT, direction)

            a, s = dfs(i2, j2, char)
            area += a
            sides += s

        return area, sides

    total = 0
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            area, sides = dfs(i, j, char)
            total += area * sides

    print(total)

def printAllOfChar(char):

    for row in lines:
        for char2 in row:

            if char2 == char:
                print(char, end="")
            else:
                print(".", end="")

        print()

part2()