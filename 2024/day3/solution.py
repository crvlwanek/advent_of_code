import re

with open("input.txt") as file:
    instructions = "".join(file.readlines())

def part1():
    matches = re.findall("mul\\(([0-9]{1,3}),([0-9]{1,3})\\)", instructions)
    total = sum(int(a) * int(b) for a, b in matches)
    print(total)


def part2():
    pattern = "mul\\(([0-9]{1,3}),([0-9]{1,3})\\)"
    mulInstructions = [(match.start(), int(match.group(1)), int(match.group(2))) for match in re.finditer(pattern, instructions)]
    doOrDont = [(match.start(), match.group()) for match in re.finditer("(do\\(\\)|don't\\(\\))", instructions)]

    total = 0
    mulPointer = 0
    doOrDontPointer = 0
    enableMultiply = True

    while mulPointer < len(mulInstructions):

        cIndex, conditional = doOrDont[doOrDontPointer]
        mIndex, mA, mB = mulInstructions[mulPointer]

        while cIndex < mIndex and doOrDontPointer < len(doOrDont) - 1:
            enableMultiply = conditional == "do()"
            doOrDontPointer += 1
            cIndex, conditional = doOrDont[doOrDontPointer]

        #assert cIndex > mIndex, f"c: {cIndex}, m: {mIndex}"

        if enableMultiply:
            total += mA * mB

        mulPointer += 1

    print(total)

# This is pretty bad code but it's the best I could come up with
def part2Alt():

    def isPartialMul(command):

        charDict = {i: char for i, char in enumerate("mul(")}
        nums = [""]
        
        for i, char in enumerate(command):

            if i in charDict:
                if charDict[i] != char:
                    return False
                
                continue

            if char.isdigit():
                nums[-1] += char
                if len(nums[-1]) > 3:
                    return False
                
                continue

            if char == ",":
                if len(nums) > 1:
                    return False
                
                nums.append("")
                continue

            return False
        
        return True

    commands = ["do()", "don't()"]
    partials = set()

    for command in commands:
        for i in range(1, len(command)):

            partial = command[:i]
            assert not not partial
            assert partial != command
            partials.add(partial)

    command = ""
    enableMultiply = True
    total = 0

    pattern = "mul\\(([0-9]{1,3}),([0-9]{1,3})\\)"

    for token in instructions:
        command += token

        if command in commands:
            enableMultiply = command == "do()"
            command = ""
            continue

        if command in partials:
            continue

        match = re.match(pattern, command)
        if match:
            if enableMultiply:
                total += int(match.group(1)) * int(match.group(2))
            
            command = ""
            continue

        if isPartialMul(command):
            print(command)
            continue

        command = token
        
    print(total)


part2Alt()