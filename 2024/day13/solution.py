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

        @lru_cache(maxsize=None)
        def followPath(path, ax, ay, bx, by, px, py):
            cost = 0
            x = y = 0

            while path > 1:
                if path & 1 == 1:
                    x += ax
                    y += ay
                    cost += aPrice
                else:
                    x += bx
                    y += by
                    cost += bPrice

                path >>= 1

            overshotTarget = x > px or y > py
            hitTarget = x == px and y == px

            return overshotTarget, hitTarget, cost


        minCost = float("inf")
        queue = deque([1])

        print(game)

        while queue:
            curr = queue.popleft()

            aPath = (curr << 1) | 1
            aOvershot, aHit, aCost = followPath(aPath, ax, ay, bx, by, px, py)

            if aHit:
                minCost = min(aCost, minCost)
            elif not aOvershot:
                queue.append(aPath)

            bPath = (curr << 1)
            bOvershot, bHit, bCost = followPath(bPath, ax, ay, bx, by, px, py)

            if bHit:
                minCost = min(bCost, minCost)
            elif not bOvershot:
                queue.append(bPath)

        if minCost != float("inf"):
            total += minCost

    print(total)


part2()