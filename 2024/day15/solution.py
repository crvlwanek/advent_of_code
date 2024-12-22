board = []
with open("input.txt") as file:
    board, moves = file.read().split("\n\n")
    moves = "".join(moves.split("\n"))
    board = [list(row) for row in board.split("\n")]

ROBOT = "@"
WALL = "#"
BOX = "O"
EMPTY = "."

BOX_LEFT = "["
BOX_RIGHT = "]"

directions = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

def findRobot(board):
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char == ROBOT:
                return i, j
            
    raise Exception("Robot not found")

def part1():
    rx, ry = findRobot(board)

    for move in moves:
        dx, dy = directions[move]

        x2, y2 = rx + dx, ry + dy

        if board[x2][y2] == WALL:
            continue

        if board[x2][y2] == EMPTY:
            board[rx][ry], board[x2][y2] = board[x2][y2], board[rx][ry]
            rx += dx
            ry += dy
            continue

        if board[x2][y2] != BOX:
            raise Exception("Something other than a box: " + board[x2][y2])
        
        while board[x2][y2] == BOX:
            x2 += dx
            y2 += dy

        # Can't push a wall        
        if board[x2][y2] == WALL:
            continue

        if board[x2][y2] != EMPTY:
            raise Exception("Something other than empty: " + board[x2][y2])
        
        board[x2][y2] = BOX
        board[rx][ry] = EMPTY
        rx += dx
        ry += dy
        board[rx][ry] = ROBOT

    total = 0
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char == BOX:
                total += i * 100 + j

    print(total)


def widenBoard(board):

    newBoard = []

    for row in board:

        newRow = []
        newBoard.append(newRow)

        for char in row:

            if char == WALL:
                newRow.append(WALL)
                newRow.append(WALL)
                continue

            if char == BOX:
                newRow.append(BOX_LEFT)
                newRow.append(BOX_RIGHT)
                continue

            if char == EMPTY:
                newRow.append(EMPTY)
                newRow.append(EMPTY)
                continue

            if char == ROBOT:
                newRow.append(ROBOT)
                newRow.append(EMPTY)
                continue

            raise Exception("Unknown char: " + char)


    return newBoard

board = widenBoard(board)

def part2():
    rx, ry = findRobot(board)

    def addBox(x, y, coords, coordsToCheck):
        char1 = board[x][y]
        if char1 != BOX_LEFT and char1 != BOX_RIGHT:
            raise Exception("Incorrect char: " + char1)
        
        if char1 == BOX_LEFT:
            y2 = y + 1
        else:
            y2 = y - 1

        char2 = board[x][y2]
        if char2 != BOX_LEFT and char2 != BOX_RIGHT:
            raise Exception("Incorrect char: " + char2)
        
        if len(set([char1, char2])) != 2:
            raise Exception("Not two chars: " + char1 + " " + char2)
        
        coords[(x, y)] = char1
        coords[(x, y2)] = char2

        coordsToCheck.append((x, y))
        coordsToCheck.append((x, y2))

    for move in moves:
        dx, dy = directions[move]
        x2, y2 = rx + dx, ry + dy

        if board[x2][y2] == WALL:
            continue

        if board[x2][y2] == EMPTY:
            board[rx][ry], board[x2][y2] = board[x2][y2], board[rx][ry]
            rx += dx
            ry += dy
            continue

        if board[x2][y2] != BOX_LEFT and board[x2][y2] != BOX_RIGHT:
            raise Exception("Something other than a box: " + board[x2][y2])
        
        coords = {}
        coordsToCheck = []
        addBox(x2, y2, coords, coordsToCheck)
        hitWall = False

        while coordsToCheck:

            cx, cy = coordsToCheck.pop()
            cx2 = cx + dx
            cy2 = cy + dy

            if board[cx2][cy2] == WALL:
                hitWall = True
                break

            if board[cx2][cy2] == EMPTY:
                continue

            if (cx2, cy2) in coords:
                continue

            addBox(cx2, cy2, coords, coordsToCheck)

        if hitWall:
            continue

        for (x, y) in coords.keys():
            board[x][y] = EMPTY

        for (x, y), char in coords.items():
            board[x + dx][y + dy] = char

        board[rx][ry] = EMPTY
        rx += dx
        ry += dy
        board[rx][ry] = ROBOT


    total = 0
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char == BOX_LEFT:
                total += i * 100 + j

    print(total)



part2()