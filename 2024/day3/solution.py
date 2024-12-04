import re

with open("input.txt") as file:
    instructions = "".join(file.readlines())

def part1():
    matches = re.findall("mul\\(([0-9]{1,3}),([0-9]{1,3})\\)", instructions)
    total = sum(int(a) * int(b) for a, b in matches)
    print(total)


def part2():
    mulEnabled = True
    patterns = ["do()", "don't()"]
    instruction = ""
    for token in instructions:

        instruction += token
        if instruction in patterns:
            pass




part1()