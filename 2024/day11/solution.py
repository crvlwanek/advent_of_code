from functools import lru_cache

def getStones():    
    with open("input.txt") as file:
        stones = [int(n) for n in file.read().strip().split()]
    return stones

def part1():
    
    blink = 75
    stones = getStones()
    for _ in range(blink):

        newStones = []

        for stone in stones:

            if stone == 0:
                newStones.append(1)
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                a, b = s[:len(s)//2], s[len(s)//2:]
                newStones.append(int(a))
                newStones.append(int(b))
            else:
                newStones.append(stone * 2024)

        stones = newStones

    print(len(stones))


def part2():

    stones = getStones()

    @lru_cache(maxsize=None)
    def dfs(stone, blink):

        if blink == 0:
            return 1
        
        if stone == 0:
            return dfs(1, blink-1)
        
        s = str(stone)
        if len(s) % 2 == 0:
            a, b = int(s[:len(s)//2]), int(s[len(s)//2:])
            return dfs(a, blink-1) + dfs(b, blink-1)
        
        return dfs(stone * 2024, blink-1)
    
    blink = 75
    total = 0

    for stone in stones:
        total += dfs(stone, blink)

    print(total)


part2()