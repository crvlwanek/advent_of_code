from functools import lru_cache

with open("input.txt") as file:
    towels, designs = file.read().split("\n\n")

    towels = towels.split(", ")
    designs = designs.split("\n")


def part1():

    def canMakeDesign(design: str):
        
        if design == "":
            return True
        
        for towel in towels:
            if design.startswith(towel) and canMakeDesign(design[len(towel):]):
                return True
            
        return False
    
    print(sum(canMakeDesign(design) for design in designs))


def part2():

    @lru_cache(maxsize=None)
    def numWaysToMake(design: str):
        
        if design == "":
            return 1
        
        total = 0

        for towel in towels:
            if design.startswith(towel):
                total += numWaysToMake(design[len(towel):])

        return total
    
    print(sum(numWaysToMake(design) for design in designs))


part2()