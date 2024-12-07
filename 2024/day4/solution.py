import itertools

with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

XMAS = "XMAS"

def part1():
    directions = [d for d in itertools.product((-1, 0, 1), repeat=2) if d != (0, 0)]
    assert len(directions) == 8

    count = 0

    def countXmas(i, j):

        if lines[i][j] != "X":
            return 0
        
        xmasCount = 0

        for di, dj in directions:
            i2, j2 = i, j
            xmasCount += 1
            for char in XMAS[1:]:
                i2 += di
                j2 += dj

                if i2 >= len(lines) or i2 < 0 or j2 < 0 or j2 >= len(lines[i2]):
                    xmasCount -= 1
                    break

                if lines[i2][j2] != char:
                    xmasCount -= 1
                    break

        return xmasCount

    for i, line in enumerate(lines):
        for j, _ in enumerate(line):
            count += countXmas(i, j)

    print(count)


def part2():

    def isXmas(i, j):
        
        if lines[i][j] != "A":
            return 0
        
        if i - 1 < 0 or i + 1 >= len(lines) or j - 1 < 0 or j + 1 >= len(lines[i]):
            return 0
        
        if not ((lines[i-1][j-1] == "M" and lines[i+1][j+1] == "S") or (lines[i-1][j-1] == "S" and lines[i+1][j+1] == "M")):
            return 0
        
        if not ((lines[i+1][j-1] == "M" and lines[i-1][j+1] == "S") or (lines[i+1][j-1] == "S" and lines[i-1][j+1] == "M")):
            return 0

        return 1
    
    count = 0

    for i, line in enumerate(lines):
        for j, _ in enumerate(line):
            count += isXmas(i, j)

    print(count)


part2()