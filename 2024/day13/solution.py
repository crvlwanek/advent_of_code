from functools import lru_cache
from collections import deque

with open("input.txt") as file:
    games = [game.split("\n") for game in file.read().split("\n\n")]


def part1():
    aPrice = 3
    bPrice = 1

    @lru_cache(maxsize=None)
    def findTargetMinCost(x, y, targetX, targetY, currentCost, aPress, bPress, aPresses, bPresses):

        if x > targetX or y > targetY:
            return float("inf")

        if aPresses > 100 or bPresses > 100:
            return float("inf")

        if x == targetX and y == targetY:
            return currentCost

        ax, ay = aPress
        bx, by = bPress

        aMin = findTargetMinCost(x + ax, y + ay, targetX, targetY, currentCost + aPrice, aPress, bPress, aPresses + 1, bPresses)
        bMin = findTargetMinCost(x + bx, y + by, targetX, targetY, currentCost + bPrice, aPress, bPress, aPresses, bPresses + 1)

        return min(aMin, bMin)

    total = 0

    for game in games:

        ax = int(game[0].split("+")[1].split(",")[0])
        ay = int(game[0].split("+")[-1])

        bx = int(game[1].split("+")[1].split(",")[0])
        by = int(game[1].split("+")[-1])

        px = int(game[2].split("=")[1].split(",")[0])
        py = int(game[2].split("=")[-1])

        minCost = findTargetMinCost(0, 0, px, py, 0, (ax, ay), (bx, by), 0, 0)

        if minCost != float("inf"):
            total += minCost

    print(total)


def part2():

    aPrice = 3
    bPrice = 1

    adjustment = 10000000000000
    
    total = 0

    for game in games:

        ax = int(game[0].split("+")[1].split(",")[0])
        ay = int(game[0].split("+")[-1])

        bx = int(game[1].split("+")[1].split(",")[0])
        by = int(game[1].split("+")[-1])

        px = int(game[2].split("=")[1].split(",")[0])
        py = int(game[2].split("=")[-1])

        px += adjustment
        py += adjustment

        aPresses = (px * by - py * bx) / (ax * by - ay * bx)
        bPresses = (px - ax * aPresses) / bx

        if aPresses % 1 == 0 and bPresses % 1 == 0:
            total += aPresses * aPrice + bPresses * bPrice

    print(total)


part2()