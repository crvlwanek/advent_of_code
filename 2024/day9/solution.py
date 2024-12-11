with open("input.txt") as file:
    data = file.read()


def part1():
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

    

part1()