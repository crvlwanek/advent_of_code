with open("input.txt") as file:
    lines = file.readlines()

def part1():

    total = 0

    for line in lines:

        testValue, rest = line.strip().split(":")
        operands = rest.split()

        testValue = int(testValue)

        options = []
        for i, operand in enumerate([int(o) for o in operands]):
            if i == 0:
                options.append(operand)
                continue

            add = [o + operand for o in options]
            mult = [o * operand for o in options]
            options = [*add, *mult]

        if testValue in options:
            total += testValue

    print(total)
    

part1()