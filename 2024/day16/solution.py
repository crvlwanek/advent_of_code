from collections import deque

with open("input.txt") as file:
    maze = [line.strip() for line in file.readlines()]

WALL = "#"
START = "S"
END = "E"
EMPTY = "."

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTIONS = [
    UP,
    RIGHT,
    DOWN,
    LEFT
]

ROTATE_SCORE = 1000

def rotateClockwise(direction):
    index = DIRECTIONS.index(direction)
    return DIRECTIONS[(index + 1) % 4]

def rotateCounterclockwise(direction):
    index = DIRECTIONS.index(direction)
    return DIRECTIONS[(index - 1) % 4]

assert rotateClockwise(UP) == RIGHT,"Incorrect rotation"
assert rotateCounterclockwise(UP) == LEFT,"Incorrect rotation"

def findStart():

    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char == START:
                return (i, j)
            
    raise Exception("Start not found")

def part1():
    queue = deque([(findStart(), RIGHT, 0)])
    seen = {}
    minScore = float("inf")

    while queue:
        coord, direction, score = queue.popleft()
        seen[(coord, direction)] = score

        x, y = coord
        dx, dy = direction

        if maze[x][y] == END:
            minScore = min(score, minScore)
            continue

        x2 = x + dx
        y2 = y + dy

        if maze[x2][y2] != WALL:
            queue.append(((x2, y2), direction, score + 1))

        cw = rotateClockwise(direction)
        if ((x, y), cw) not in seen or seen[((x, y), cw)] > score + ROTATE_SCORE:
            queue.append(((x, y), cw, score + ROTATE_SCORE))

        ccw = rotateCounterclockwise(direction)
        if ((x, y), ccw) not in seen or seen[((x, y), ccw)] > score + ROTATE_SCORE:
            queue.append(((x, y), ccw, score + ROTATE_SCORE))

    print(minScore)

# This takes a very long time to run because there's sooooooo much memory copying
def part2():
    queue = deque([(findStart(), RIGHT, 0, set())])
    seen = {}
    minScore = float("inf")
    paths = []

    while queue:
        coord, direction, score, path = queue.popleft()
        seen[(coord, direction)] = score
        path.add(coord)

        x, y = coord
        dx, dy = direction

        if maze[x][y] == END:
            if score < minScore:
                paths = [path]
            elif score == minScore:
                paths.append(path)

            minScore = min(score, minScore)
            continue

        x2 = x + dx
        y2 = y + dy

        if maze[x2][y2] != WALL:
            queue.append(((x2, y2), direction, score + 1, set(path)))

        cw = rotateClockwise(direction)
        if ((x, y), cw) not in seen or seen[((x, y), cw)] > score + ROTATE_SCORE:
            queue.append(((x, y), cw, score + ROTATE_SCORE, set(path)))

        ccw = rotateCounterclockwise(direction)
        if ((x, y), ccw) not in seen or seen[((x, y), ccw)] > score + ROTATE_SCORE:
            queue.append(((x, y), ccw, score + ROTATE_SCORE, set(path)))

    print(paths)
    allPaths = set()
    for path in paths:
        allPaths.update(path)

    print(len(allPaths))

part2()