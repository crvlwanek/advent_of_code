with open("input.txt") as file:
    data = file.read()

placeholder = chr(100000)

def stringify(data):
    chars = []
    for i, num in enumerate(data):
        if i % 2 == 0:
            fileId = i // 2
            chars.append(chr(fileId) * int(num))
        else:
            chars.append(placeholder * int(num))

    return "".join(chars)

def part1():
    s = stringify(data)
    array = list(s)

    l, r = 0, len(array) - 1

    while l < r:

        while array[l] != placeholder:
            l += 1

        while array[r] == placeholder:
            r -= 1

        if l >= r:
            break

        array[l], array[r] = array[r], array[l]

    pl = True
    for i, char in enumerate(array[::-1]):
        if char != placeholder:
            pl = False

        if not pl and char == placeholder:
            raise Exception("Incorrect char on index: " + str(i))

    total = 0
    for i, char in enumerate(array):
        if char != placeholder:
            total += ord(char) * i

    print(total) 


def part2():
    s = stringify(data)
    array = list(s)

    r = len(array) - 1

    while r > 0:
        l = 0
        while array[l] != placeholder:
            l += 1
        
        while array[r] == placeholder:
            r -= 1

        char = array[r]

        if l >= r:
            break

        dr = 0
        while array[r - dr - 1] == array[r]:
            dr += 1
        
        while l < r:

            dl = 0
            while array[l + dl + 1] == placeholder:
                dl += 1

            if dl >= dr:
                for i in range(dr + 1):
                    array[l + i], array[r - i] = array[r - i], array[l + i]

                break

            while array[l] == placeholder:
                l += 1

            while array[l] != placeholder:
                l += 1
            
        while array[r] == char or array[r] == placeholder:
            r -= 1

    total = 0
    for i, char in enumerate(array):
        if char != placeholder:
            total += ord(char) * i

    print(total)
    

part2()