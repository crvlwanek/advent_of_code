from collections import deque

with open("input.txt") as file:
    byteList = [list(map(int, line.strip().split(","))) for line in file.readlines()]

directions = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
)

def part1():

    grid = [["."] * 71 for _ in range(71)]
    
    for i in range(1024):
        y, x = byteList[i]

        grid[y][x] = "#"

    q = deque()
    q.append((0, 0, 0))

    exitTile = 70

    seen = set()

    while q:

        x, y, steps = q.popleft()

        if x == exitTile and y == exitTile:
            print(steps)
            break

        for dx, dy in directions:
            x2 = x + dx
            y2 = y + dy

            if 0 <= x2 <= exitTile and 0 <= y2 <= exitTile and grid[y2][x2] != "#" and (x2, y2) not in seen:
                q.append((x2, y2, steps + 1))
                seen.add((x2, y2))
def part2():

    grid = [["."] * 71 for _ in range(71)]

    for i, byte in enumerate(byteList):
        x, y = byte
        grid[y][x] = "#"
        q = deque()
        q.append((0, 0, 0))
        exitTile = 70
        seen = set()

        finished = False

        while q:

            x, y, steps = q.popleft()

            if x == exitTile and y == exitTile:
                finished = True
                break

            for dx, dy in directions:
                x2 = x + dx
                y2 = y + dy

                if 0 <= x2 <= exitTile and 0 <= y2 <= exitTile and grid[y2][x2] != "#" and (x2, y2) not in seen:
                    q.append((x2, y2, steps + 1))
                    seen.add((x2, y2))

        if not finished:
            print(byteList[i])
            break

part2()